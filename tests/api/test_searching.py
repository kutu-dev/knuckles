from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_search_song(
    subsonic: Subsonic,
    mock_search_song: Response,
    song: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_search_song)

    response = subsonic.searching.search(
        song["title"], 1, 0, 0, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is not None
    assert response.songs[0].title == song["title"]
    assert response.albums is None
    assert response.artists is None


@responses.activate
def test_search_album(
    subsonic: Subsonic,
    mock_search_album: Response,
    album: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_search_album)

    response = subsonic.searching.search(
        album["title"], 0, 0, 1, 0, 0, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is not None
    assert response.albums[0].title == album["title"]
    assert response.artists is None


@responses.activate
def test_search_artist(
    subsonic: Subsonic,
    mock_search_artist: Response,
    artist: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_search_artist)

    response = subsonic.searching.search(
        artist["name"], 0, 0, 0, 0, 1, 0, music_folders[0]["id"]
    )

    assert response.songs is None
    assert response.albums is None
    assert response.artists is not None
    assert response.artists[0].name == artist["name"]
