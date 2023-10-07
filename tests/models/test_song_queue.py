from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.play_queue import PlayQueue
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_play_queue: Response,
    username: dict[str, Any],
) -> None:
    responses.add(mock_get_play_queue)

    response = subsonic.bookmarks.get_play_queue()
    response.username = "Foo"
    response = response.generate()

    assert response.user.username == username


@responses.activate
def test_save(
    subsonic: Subsonic,
    mock_get_play_queue: Response,
    mock_save_play_queue: Response,
) -> None:
    responses.add(mock_get_play_queue)
    responses.add(mock_save_play_queue)

    response = subsonic.bookmarks.get_play_queue()
    response = response.save()

    assert type(response) is PlayQueue
