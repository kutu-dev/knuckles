import json
from typing import Any, Callable, Protocol

import knuckles
import pytest
import requests
import responses
from _pytest.fixtures import FixtureRequest
from knuckles.subsonic import Subsonic
from responses import GET, POST, Response, matchers

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


@pytest.fixture(params=["GET", "POST"])
def subsonic(
    request: FixtureRequest, base_url: str, username: str, password: str, client: str
) -> Subsonic:
    if request.param == "GET":
        method = knuckles.RequestMethod.GET
    else:
        method = knuckles.RequestMethod.POST

    return knuckles.Subsonic(
        url=base_url,
        user=username,
        password=password,
        client=client,
        request_method=method,
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
    ) -> list[Response]:
        ...


def match_json(
    mocked_data: dict[str, Any]
) -> Callable[[requests.PreparedRequest], tuple[bool, str]]:
    def inner(
        response: requests.PreparedRequest,
    ) -> tuple[bool, str]:
        print(response.body)
        print(mocked_data)

        if type(response.body) is not str:
            return (
                False,
                "The request body wasn't a string",
            )

        for key, value in json.loads(response.body).items():
            print(key, value)

            if key not in mocked_data:
                continue

            # When the passed value is a list different checks should be made,
            # this happens when the same parameters is in the request multiple times,
            # this happens for example when using
            # the parameter "songId" in the endpoint "createPlaylist".
            if (
                type(value) is list
                and type(mocked_data[key]) is str
                and (
                    mocked_data[key] in value
                    # The values inside the list "value" can sometimes be integers,
                    # so a extra check is needed for them.
                    or (
                        str.isdigit(mocked_data[key]) and int(mocked_data[key]) in value
                    )
                )
            ):
                continue

            if str(value) != str(mocked_data[key]):
                return (
                    False,
                    f"The value '{value}' in the key '{key}' is"
                    + f"not equal to '{mocked_data[key]}'",
                )

        return (True, "")

    return inner


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
    ) -> list[Response]:
        mocked_params = params.copy()
        if extra_params is not None:
            mocked_params.update(extra_params)

        mocked_data = {"subsonic-response": {**subsonic_response}}
        if extra_data is not None:
            mocked_data["subsonic-response"].update(extra_data)

        return [
            Response(
                method=GET,
                headers=headers,
                content_type=content_type,
                url=f"{base_url}/rest/{endpoint}",
                match=[matchers.query_param_matcher(mocked_params, strict_match=False)],
                json=mocked_data if body is None else None,
                body=body,
                status=200,
            ),
            Response(
                method=POST,
                headers=headers,
                content_type=content_type,
                url=f"{base_url}/rest/{endpoint}",
                match=[match_json(mocked_params)],
                json=mocked_data if body is None else None,
                body=body,
                status=200,
            ),
        ]

    return inner


class AddResponses(Protocol):
    def __call__(self, responses_list: list[Response]) -> None:
        ...


@pytest.fixture
def add_responses() -> AddResponses:
    def inner(responses_list: list[Response]) -> None:
        for response in responses_list:
            responses.add(response)

    return inner
