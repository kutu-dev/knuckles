from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_get_bookmarks(
    subsonic: Subsonic, mock_get_bookmarks: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_get_bookmarks)

    response = subsonic.bookmarks.get_bookmarks()

    assert response[0].song.id == song["id"]


@responses.activate
def test_get_bookmark(
    subsonic: Subsonic,
    mock_get_bookmarks: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_get_bookmarks)

    response = subsonic.bookmarks.get_bookmark(song["id"])

    assert response.song.id == song["id"]
    assert response.position == bookmark["position"]
    assert response.user.username == bookmark["username"]
    assert response.comment == bookmark["comment"]
    assert response.created == parser.parse(bookmark["created"])
    assert response.changed == parser.parse(bookmark["changed"])


@responses.activate
def test_create_bookmark(
    subsonic: Subsonic,
    mock_create_bookmark: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_create_bookmark)

    response = subsonic.bookmarks.create_bookmark(
        song["id"], bookmark["position"], bookmark["comment"]
    )

    assert response.song.id == song["id"]


@responses.activate
def test_update_bookmark(
    subsonic: Subsonic,
    mock_create_bookmark: Response,
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    responses.add(mock_create_bookmark)

    response = subsonic.bookmarks.update_bookmark(
        song["id"], bookmark["position"], bookmark["comment"]
    )

    assert response.song.id == song["id"]


@responses.activate
def test_delete_bookmark(
    subsonic: Subsonic, mock_delete_bookmark: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_delete_bookmark)

    response = subsonic.bookmarks.delete_bookmark(song["id"])

    assert type(response) == Subsonic
