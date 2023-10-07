from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.bookmark import Bookmark
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response.position = 0
    response = response.generate()

    assert response.position == bookmark["position"]


@responses.activate
def test_create(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_create_bookmark: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_create_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.create()

    assert type(response) is Bookmark


@responses.activate
def test_update(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_create_bookmark: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_create_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.update()

    assert type(response) is Bookmark


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_delete_bookmark: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_delete_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.delete()

    assert type(response) is Bookmark
