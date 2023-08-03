from typing import Any

import pytest
import responses
from responses import Response

from knuckles import Subsonic
from knuckles.exceptions import MissingPlaylistName
from knuckles.models.playlist import Playlist


@responses.activate
def test_playlist_generate(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response.name = "Foo"
    response = response.generate()

    assert type(response) == Playlist
    assert response.name == playlist["name"]


@responses.activate
def test_playlist_create(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_create_playlist: Response,
    mock_update_comment_and_public: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_create_playlist)
    responses.add(mock_update_comment_and_public)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response = response.create()

    assert type(response) == Playlist


@responses.activate
def test_playlisy_create_none_name_value(
    subsonic: Subsonic, mock_get_playlist: Response, playlist: dict[str, Any]
):
    responses.add(mock_get_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response.name = None

    with pytest.raises(
        MissingPlaylistName,
        match=(
            "A non None value in the name parameter"
            + "is necessary to create a playlist"
        ),
    ):
        response.create()


@responses.activate
def test_playlist_update(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_update_comment_and_public: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_update_comment_and_public)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response = response.update()

    assert type(response) == Playlist


@responses.activate
def test_playlist_delete(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_delete_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_delete_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response = response.delete()

    assert type(response) == Playlist
