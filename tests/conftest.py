from typing import Any, Protocol

import pytest
from responses import GET, Response, matchers

pytest_plugins = [
    "tests.subsonic",
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
        extra_params: dict[str, Any] = {},
        extra_data: dict[str, Any] = {},
        headers: dict[str, str] = {},
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
        extra_params: dict[str, Any] = {},
        extra_data: dict[str, Any] = {},
        headers: dict[str, str] = {},
        content_type: str = "",
        body: Any = None,
    ) -> Response:
        return Response(
            method=GET,
            headers=headers,
            content_type=content_type,
            url=f"{base_url}/rest/{endpoint}",
            match=[
                matchers.query_param_matcher(
                    {**params, **extra_params}, strict_match=False
                )
            ],
            json={"subsonic-response": {**subsonic_response, **extra_data}}
            if body is None
            else None,
            body=body,
            status=200,
        )

    return inner
