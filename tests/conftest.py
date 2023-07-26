from typing import Any, Protocol

import knuckles
import pytest
from knuckles.subsonic import Subsonic
from responses import GET, Response, matchers


@pytest.fixture
def user() -> str:
    return "user"


@pytest.fixture
def password() -> str:
    return "password"


@pytest.fixture
def client() -> str:
    return "client"


@pytest.fixture
def subsonic(user: str, password: str, client: str) -> Subsonic:
    return knuckles.Subsonic(
        url="http://example.com",
        user=user,
        password=password,
        client=client,
    )


@pytest.fixture
def params(user: str, client: str) -> dict[str, str]:
    return {
        "u": user,
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


@pytest.fixture
def license() -> dict[str, Any]:
    return {
        "valid": True,
        "email": "user@example.com",
        "licenseExpires": "2017-04-11T10:42:50.842Z",
        "trialExpires": "2015-03-11T12:36:38.753Z",
    }


@pytest.fixture
def message() -> dict[str, Any]:
    return {
        "username": "admin",
        "time": 1678935707000,
        "message": "Api Script Testing",
    }


@pytest.fixture
def messages(message: dict[str, Any]) -> dict[str, Any]:
    return {"chatMessage": [message]}


class ResponseGenerator(Protocol):
    def __call__(
        self,
        endpoint: str,
        extra_params: dict[str, Any] = {},
        extra_data: dict[str, Any] = {},
    ) -> Response:
        ...


@pytest.fixture
def response_generator(
    params: dict[str, str], subsonic_response: dict[str, Any]
) -> ResponseGenerator:
    def inner(
        endpoint: str,
        extra_params: dict[str, Any] = {},
        extra_data: dict[str, Any] = {},
    ) -> Response:
        return Response(
            method=GET,
            url=f"https://example.com/rest/{endpoint}",
            match=[
                matchers.query_param_matcher(
                    {**params, **extra_params}, strict_match=False
                )
            ],
            json={"subsonic-response": {**subsonic_response, **extra_data}},
            status=200,
        )

    return inner


@pytest.fixture
def mock_ping(response_generator: ResponseGenerator) -> Response:
    return response_generator("ping")


@pytest.fixture
def mock_get_license(
    response_generator: ResponseGenerator, license: dict[str, Any]
) -> Response:
    return response_generator("getLicense", {}, {"license": license})


@pytest.fixture
def mock_add_chat_message(
    response_generator: ResponseGenerator, message: dict[str, Any]
) -> Response:
    return response_generator("addChatMessage", {"message": message["message"]})


@pytest.fixture
def mock_get_chat_messages(
    response_generator: ResponseGenerator, messages: dict[str, Any]
) -> Response:
    return response_generator("getChatMessages", {}, {"chatMessages": messages})
