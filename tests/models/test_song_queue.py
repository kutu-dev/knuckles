from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.play_queue import PlayQueue
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_play_queue: list[Response],
    username: dict[str, Any],
) -> None:
    add_responses(mock_get_play_queue)

    response = subsonic.bookmarks.get_play_queue()
    response.username = "Foo"
    response = response.generate()

    assert response.user.username == username


@responses.activate
def test_save(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_play_queue: list[Response],
    mock_save_play_queue: list[Response],
) -> None:
    add_responses(mock_get_play_queue)
    add_responses(mock_save_play_queue)

    response = subsonic.bookmarks.get_play_queue()
    response = response.save()

    assert type(response) is PlayQueue
