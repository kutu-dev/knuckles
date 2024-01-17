from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def message() -> dict[str, Any]:
    return {
        "username": "admin",
        "time": 1678935707000,
        "message": "Api Script Testing",
    }


@pytest.fixture
def mock_add_chat_message(
    mock_generator: MockGenerator, message: dict[str, Any]
) -> list[Response]:
    return mock_generator("addChatMessage", {"message": message["message"]})


@pytest.fixture
def messages(message: dict[str, Any]) -> dict[str, Any]:
    return {"chatMessage": [message]}


@pytest.fixture
def mock_get_chat_messages(
    mock_generator: MockGenerator, messages: dict[str, Any]
) -> list[Response]:
    return mock_generator("getChatMessages", {}, {"chatMessages": messages})
