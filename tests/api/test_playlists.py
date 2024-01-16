from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_playlists(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_playlists: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_playlists)

    response = subsonic.playlists.get_playlists()

    assert type(response[0].songs) is list
    # Access the ID3 of the first song of the first playlist
    assert response[0].songs[0].id == song["id"]


@responses.activate
def test_get_playlists_with_a_selected_user(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_playlists_with_a_selected_user: list[Response],
    song: dict[str, Any],
    username: str,
) -> None:
    add_responses(mock_get_playlists_with_a_selected_user)

    response = subsonic.playlists.get_playlists(username)

    assert type(response[0].songs) is list
    # Access the ID3 of the first song of the first playlist
    assert response[0].songs[0].id == song["id"]


@responses.activate
def test_get_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_playlist: list[Response],
    playlist: dict[str, Any],
    song: dict[str, Any],
    username: str,
) -> None:
    add_responses(mock_get_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])

    assert response.id == playlist["id"]
    assert response.name == playlist["name"]
    assert response.comment == playlist["comment"]
    assert response.owner.username == playlist["owner"]
    assert response.public == playlist["public"]
    assert response.created == parser.parse(playlist["created"])
    assert response.changed == parser.parse(playlist["changed"])
    assert response.song_count == playlist["songCount"]
    assert response.duration == playlist["duration"]
    assert type(response.songs) is list
    assert response.songs[0].id == song["id"]
    assert response.cover_art.id == song["coverArt"]
    assert type(response.allowed_users) is list
    assert response.allowed_users[0].username == username


@responses.activate
def test_create_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_create_playlist: list[Response],
    mock_update_comment_and_public: Response,
    playlist: dict[str, Any],
    song: dict[str, Any],
) -> None:
    add_responses(mock_update_comment_and_public)
    add_responses(mock_create_playlist)
    response = subsonic.playlists.create_playlist(
        playlist["name"], playlist["comment"], playlist["public"], [song["id"]]
    )

    assert response.id == playlist["id"]
    assert response.comment == playlist["comment"]
    assert response.public == playlist["public"]
    assert type(response.songs) is list
    assert response.songs[0].id == song["id"]


@responses.activate
def test_update_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_update_playlist: list[Response],
    playlist: dict[str, Any],
    song: dict[str, Any],
) -> None:
    add_responses(mock_update_playlist)

    response = subsonic.playlists.update_playlist(
        playlist["id"],
        playlist["name"],
        playlist["comment"],
        playlist["public"],
        [song["id"]],
        [0],
    )

    assert response.id == playlist["id"]
    # It should be None as the complete list of songs is unknown
    assert response.songs is None


@responses.activate
def test_delete_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_playlist: list[Response],
    playlist: dict[str, Any],
) -> None:
    add_responses(mock_delete_playlist)

    response = subsonic.playlists.delete_playlist(playlist["id"])

    assert type(response) is Subsonic
