from typing import Any

import responses
from responses import Response

from knuckles import Subsonic
from knuckles.models.bookmark import Bookmark


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)

    requested_bookmark = subsonic.bookmarks.get_bookmark(song["id"])
    requested_bookmark.position = 0
    requested_bookmark = requested_bookmark.generate()

    assert requested_bookmark.position == bookmark["position"]


@responses.activate
def test_create(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_create_bookmark: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_create_bookmark)

    requested_bookmark = subsonic.bookmarks.get_bookmark(song["id"])
    requested_bookmark = requested_bookmark.create()

    assert type(requested_bookmark) == Bookmark


@responses.activate
def test_update(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_create_bookmark: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_create_bookmark)

    requested_bookmark = subsonic.bookmarks.get_bookmark(song["id"])
    requested_bookmark = requested_bookmark.update()

    assert type(requested_bookmark) == Bookmark


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    mock_delete_bookmark: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)
    responses.add(mock_delete_bookmark)

    requested_bookmark = subsonic.bookmarks.get_bookmark(song["id"])
    requested_bookmark = requested_bookmark.delete()

    assert type(requested_bookmark) == Bookmark
