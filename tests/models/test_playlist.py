from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.playlist import Playlist
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response.name = "Foo"
    response = response.generate()

    assert type(response) is Playlist
    assert response.name == playlist["name"]


@responses.activate
def test_create(
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

    assert type(response) is Playlist


@responses.activate
def test_update(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_update_comment_and_public: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_update_comment_and_public)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response = response.update()

    assert type(response) is Playlist


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_delete_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_delete_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    response = response.delete()

    assert type(response) is Playlist


@responses.activate
def test_add(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_add_song_to_playlist: Response,
    playlist: dict[str, Any],
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_add_song_to_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])
    # Remove the default songs from the mock_get_playlist mock
    response.songs = []
    response.song_count = 0

    response = response.add_songs([song["id"]])

    assert response.songs is not None
    assert response.songs[0].id == song["id"]
    assert response.song_count == 1


@responses.activate
def test_remove(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_remove_song_to_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_remove_song_to_playlist)

    response = subsonic.playlists.get_playlist(playlist["id"])

    response = response.remove_songs([0])

    assert response.songs is not None
    assert response.songs == []
    assert response.song_count == 0
