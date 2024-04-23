from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_search_song_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_song_non_id3: list[Response],
    song: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_song_non_id3)

    response = subsonic.searching.search_non_id3(
        song["title"], 1, 0, 0, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is not None
    assert response.songs[0].title == song["title"]
    assert response.albums is None
    assert response.artists is None


@responses.activate
def test_search_album_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_album_non_id3: list[Response],
    album: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_album_non_id3)

    response = subsonic.searching.search_non_id3(
        album["title"], 0, 0, 1, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is not None
    assert response.albums[0].title == album["title"]
    assert response.artists is None


@responses.activate
def test_search_artist_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_artist_non_id3: list[Response],
    artist: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_artist_non_id3)

    response = subsonic.searching.search_non_id3(
        artist["name"], 0, 0, 0, 0, 1, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is None
    assert response.artists is not None
    assert response.artists[0].name == artist["name"]


@responses.activate
def test_search_song(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_song: list[Response],
    song: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_song)

    response = subsonic.searching.search(
        song["title"], 1, 0, 0, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is not None
    assert response.songs[0].title == song["title"]
    assert response.albums is None
    assert response.artists is None


@responses.activate
def test_search_album(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_album: list[Response],
    album: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_album)

    response = subsonic.searching.search(
        album["title"], 0, 0, 1, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is not None
    assert response.albums[0].title == album["title"]
    assert response.artists is None


@responses.activate
def test_search_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_search_artist: list[Response],
    artist: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_search_artist)

    response = subsonic.searching.search(
        artist["name"], 0, 0, 0, 0, 1, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is None
    assert response.artists is not None
    assert response.artists[0].name == artist["name"]
