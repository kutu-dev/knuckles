from typing import Any

import responses
from knuckles import Bookmark, Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_bookmarks: list[Response],
    song: dict[str, Any],
    bookmark: dict[str, Any],
) -> None:
    add_responses(mock_get_bookmarks)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response.position = 0
    response = response.generate()

    assert response.position == bookmark["position"]


@responses.activate
def test_create(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_bookmarks: list[Response],
    mock_create_bookmark: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_bookmarks)
    add_responses(mock_create_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.create()

    assert type(response) is Bookmark


@responses.activate
def test_update(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_bookmarks: list[Response],
    mock_create_bookmark: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_bookmarks)
    add_responses(mock_create_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.update()

    assert type(response) is Bookmark


@responses.activate
def test_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_bookmarks: list[Response],
    mock_delete_bookmark: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_bookmarks)
    add_responses(mock_delete_bookmark)

    response = subsonic.bookmarks.get_bookmark(song["id"])
    response = response.delete()

    assert type(response) is Bookmark
