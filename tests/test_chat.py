from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models import ChatMessage
from responses import matchers


@responses.activate
def test_add_chat_messages(
    subsonic: Subsonic, params: dict[str, str], song_response: dict[str, Any]
) -> None:
    params["message"] = "Hello World!"

    responses.add(
        responses.GET,
        url="https://example.com/rest/addChatMessage",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=song_response,
        status=200,
    )

    response: Subsonic = subsonic.add_chat_message("Hello World!")

    assert type(response) is Subsonic


@responses.activate
def test_get_chat_messages(
    subsonic: Subsonic, params: dict[str, str], song_response: dict[str, Any]
) -> None:
    song_response["subsonic-response"]["chatMessages"] = {
        "chatMessage": [
            {
                "username": "admin",
                "time": 1678935707000,
                "message": "Api Script Testing",
            },
            {
                "username": "user",
                "time": 1678935699000,
                "message": "Api Script Testing",
            },
        ]
    }

    responses.add(
        responses.GET,
        url="https://example.com/rest/getChatMessages",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=song_response,
        status=200,
    )

    response: list[ChatMessage] = subsonic.get_chat_messages()

    assert response[0].username == "admin"
    assert response[0].time == 1678935707000
    assert response[0].message == "Api Script Testing"
    assert response[1].username == "user"
    assert response[1].time == 1678935699000
    assert response[1].message == "Api Script Testing"
