import hashlib
from typing import Any
import pytest
import knuckles
from knuckles import Subsonic, SubsonicResponse, Song, License


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
def params(user, client) -> dict[str, str]:
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
def subsonic(user, password, client) -> Subsonic:
    return knuckles.Subsonic(
        url="http://example.com",
        user=user,
        password=password,
        client=client,
    )
