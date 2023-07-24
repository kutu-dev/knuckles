from typing import Any

import knuckles
import pytest
from knuckles import Subsonic


@pytest.fixture
def client() -> str:
    return "client"


@pytest.fixture
def user() -> str:
    return "user"


@pytest.fixture
def password() -> str:
    return "password"


@pytest.fixture
def subsonic(user: str, password: str, client: str) -> Subsonic:
    return knuckles.Subsonic(
        url="http://example.com",
        user=user,
        password=password,
        client=client,
    )


@pytest.fixture
def params(user: str, client: str) -> dict[str, str]:
    return {
        "u": user,
        "v": "1.16.1",
        "c": client,
        "f": "json",
    }


@pytest.fixture
def song() -> dict[str, Any]:
    return {
        "id": "nonIntId",
        "parent": "parentId",
        "isDir": False,
        "title": "Fly Me to the Moon",
        "album": "Nothing But The Best",
        "artist": "Frank Sinatra",
        "track": 8,
        "year": 2008,
        "genre": "Jazz",
        "coverArt": "coverId",
        "size": 19866778,
        "contentType": "audio/flac",
        "suffix": "flac",
        "starred": "2020-03-27T09:45:27Z",
        "duration": 147,
        "bitRate": 880,
        "path": "Nothing But The Best/Fly Me to the Moon.flac",
        "playCount": 37,
        "played": "2023-03-26T22:27:46Z",
        "discNumber": 1,
        "created": "2020-03-14T17:51:22.112827504Z",
        "albumId": "albumId",
        "artistId": "artistId",
        "type": "music",
        "isVideo": False,
        "userRating": 5,
        "averageRating": 4.8,
    }


@pytest.fixture
def jukebox_status() -> dict[str, Any]:
    return {"currentIndex": 7, "playing": True, "gain": 0.9, "position": 67}


@pytest.fixture
def jukebox_playlist(
    jukebox_status: dict[str, Any], song: dict[str, Any]
) -> dict[str, Any]:
    jukebox_status["entry"] = [song]

    return jukebox_status


@pytest.fixture
def subsonic_response() -> dict[str, Any]:
    return {
        "subsonic-response": {
            "status": "ok",
            "version": "1.16.1",
            "type": "knuckles",
            "serverVersion": "0.1.3 (tag)",
            "openSubsonic": True,
        }
    }


@pytest.fixture
def song_response(
    subsonic_response: dict[str, Any], song: dict[str, Any]
) -> dict[str, Any]:
    subsonic_response["subsonic-response"]["song"] = song

    return subsonic_response


@pytest.fixture
def jukebox_status_response(
    subsonic_response: dict[str, Any], jukebox_status: dict[str, Any]
) -> dict[str, Any]:
    subsonic_response["subsonic-response"]["jukeboxStatus"] = jukebox_status

    return subsonic_response


@pytest.fixture
def jukebox_playlist_response(
    subsonic_response: dict[str, Any], jukebox_playlist: dict[str, Any]
) -> dict[str, Any]:
    subsonic_response["subsonic-response"]["jukeboxPlaylist"] = jukebox_playlist

    return subsonic_response
