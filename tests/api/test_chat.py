from datetime import datetime
from typing import Any

import responses
from knuckles import ChatMessage, Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_add_chat_messages(
    add_responses: AddResponses,
    subsonic: Subsonic,
    message: dict[str, Any],
    mock_add_chat_message: list[Response],
) -> None:
    add_responses(mock_add_chat_message)

    response: Subsonic = subsonic.chat.add_chat_message(message["message"])

    assert type(response) is Subsonic


@responses.activate
def test_get_chat_messages(
    add_responses: AddResponses,
    subsonic: Subsonic,
    message: dict[str, Any],
    mock_get_chat_messages: list[Response],
) -> None:
    add_responses(mock_get_chat_messages)

    response: list[ChatMessage] = subsonic.chat.get_chat_messages()

    assert response[0].username == message["username"]

    # Divide by 1000 because messages are saved in milliseconds instead of seconds
    assert response[0].time == datetime.fromtimestamp(message["time"] / 1000)

    assert response[0].message == message["message"]
