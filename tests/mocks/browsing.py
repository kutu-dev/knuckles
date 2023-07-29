from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def genre() -> dict[str, Any]:
    return {"songCount": 1, "albumCount": 1, "value": "Jazz"}


@pytest.fixture
def mock_get_genres(mock_generator: MockGenerator, genre: dict[str, Any]) -> Response:
    return mock_generator("getGenres", {}, {"genres": {"genre": [genre]}})


@pytest.fixture
def album(song: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "200000021",
        "parent": "100000036",
        "album": "Forget and Remember",
        "title": "Forget and Remember",
        "name": "Forget and Remember",
        "isDir": True,
        "coverArt": "al-200000021",
        "songCount": 20,
        "created": "2021-07-22T02:09:31+00:00",
        "duration": 4248,
        "playCount": 0,
        "artistId": "100000036",
        "artist": "Comfort Fit",
        "year": 2005,
        "genre": "Hip-Hop",
        "song": [song],
        "played": "2023-03-26T22:27:46Z",
        "userRating": 4,
    }


@pytest.fixture
def mock_get_album(mock_generator: MockGenerator, album: dict[str, Any]) -> Response:
    return mock_generator("getAlbum", {"id": album["id"]}, {"album": album})


@pytest.fixture
def song(genre: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "nonIntId",
        "parent": "parentId",
        "isDir": False,
        "title": "Fly Me to the Moon",
        "album": "Nothing But The Best",
        "artist": "Frank Sinatra",
        "track": 8,
        "year": 2008,
        "genre": genre["value"],
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
def mock_get_song(mock_generator: MockGenerator, song: dict[str, Any]) -> Response:
    return mock_generator("getSong", {"id": song["id"]}, {"song": song})
