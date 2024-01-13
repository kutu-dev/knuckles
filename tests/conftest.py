from typing import Any, Protocol

import knuckles
import pytest
from knuckles.subsonic import Subsonic
from responses import GET, Response, matchers

pytest_plugins = [
    "tests.mocks.system",
    "tests.mocks.chat",
    "tests.mocks.jukebox_control",
    "tests.mocks.media_annotation",
    "tests.mocks.media_library_scanning",
    "tests.mocks.browsing",
    "tests.mocks.user_management",
    "tests.mocks.playlists",
    "tests.mocks.sharing",
    "tests.mocks.podcast",
    "tests.mocks.internet_radio",
    "tests.mocks.bookmarks",
    "tests.mocks.searching",
    "tests.mocks.media_retrieval",
]


@pytest.fixture
def username() -> str:
    return "user"


@pytest.fixture
def password() -> str:
    return "password"


@pytest.fixture
def client() -> str:
    return "client"


@pytest.fixture
def base_url() -> str:
    return "https://example.com"


@pytest.fixture
def subsonic(base_url: str, username: str, password: str, client: str) -> Subsonic:
    return knuckles.Subsonic(
        url=base_url,
        user=username,
        password=password,
        client=client,
    )


@pytest.fixture
def params(username: str, client: str) -> dict[str, str]:
    return {
        "u": username,
        "v": "1.16.1",
        "c": client,
        "f": "json",
    }


@pytest.fixture
def subsonic_response() -> dict[str, Any]:
    return {
        "status": "ok",
        "version": "1.16.1",
        "type": "knuckles",
        "serverVersion": "0.1.3 (tag)",
        "openSubsonic": True,
    }


class MockGenerator(Protocol):
    def __call__(
        self,
        endpoint: str,
        extra_params: dict[str, Any] | None = None,
        extra_data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        content_type: str = "",
        body: Any = None,
    ) -> Response:
        ...


@pytest.fixture
def mock_generator(
    base_url: str,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> MockGenerator:
    def inner(
        endpoint: str,
        extra_params: dict[str, Any] | None = None,
        extra_data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        content_type: str = "",
        body: Any = None,
    ) -> Response:
        mocked_params = params.copy()
        if extra_params is not None:
            mocked_params.update(extra_params)

        mocked_data = {"subsonic-response": {**subsonic_response}}
        if extra_data is not None:
            mocked_data["subsonic-response"].update(extra_data)

        return Response(
            method=GET,
            headers=headers,
            content_type=content_type,
            url=f"{base_url}/rest/{endpoint}",
            match=[matchers.query_param_matcher(mocked_params, strict_match=False)],
            json=mocked_data if body is None else None,
            body=body,
            status=200,
        )

    return inner
