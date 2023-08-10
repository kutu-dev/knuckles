from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_play_queue: Response,
    username: dict[str, Any],
) -> None:
    responses.add(mock_get_play_queue)

    requested_queue = subsonic.bookmarks.get_play_queue()
    requested_queue.username = "Foo"
    requested_queue = requested_queue.generate()

    assert requested_queue.user.username == username


@responses.activate
def test_save(
    subsonic: Subsonic,
    mock_get_play_queue: Response,
    mock_save_play_queue: Response,
) -> None:
    responses.add(mock_get_play_queue)
    responses.add(mock_save_play_queue)

    requested_queue = subsonic.bookmarks.get_play_queue()
    requested_queue = requested_queue.save()

    assert True is False
    # assert type(requested_queue) is PlayQueue
