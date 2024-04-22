from typing import Any

import responses
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_album_list_random(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_random: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_random)

    response = subsonic.lists.get_album_list_random(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_newest(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_newest: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_newest)

    response = subsonic.lists.get_album_list_newest(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_highest(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_highest: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_highest)

    response = subsonic.lists.get_album_list_highest(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_frequent(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_frequent: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_frequent)

    response = subsonic.lists.get_album_list_frequent(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_recent(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_recent: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_recent)

    response = subsonic.lists.get_album_list_recent(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_name(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_name: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_name)

    response = subsonic.lists.get_album_list_alphabetical_by_name(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_artist: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_artist)

    response = subsonic.lists.get_album_list_alphabetical_by_artist(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_starred(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_starred: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_starred)

    response = subsonic.lists.get_album_list_starred(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_year(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_year: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    from_year: int,
    to_year: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_year)

    response = subsonic.lists.get_album_list_by_year(
        from_year, to_year, num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_genre(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_genre: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    genre: dict[str, Any],
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_genre)

    response = subsonic.lists.get_album_list_by_genre(
        genre["value"], num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]
