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


@pytest.fixture
def album_info() -> dict[str, Any]:
    return {
        "notes": 'Download the full release here (creative commons). These cripsy beats are ripe with thumping funk and techno influences, sample wizardry and daring shuffles. Composed with the help of unique sound plugins which were especially programmed to measure Comfort Fit’s needs and wishes, we think the chances aren’t bad that you’ll fall for the unique sound signature, bounce and elegance of this unusual Hip Hop production. Ltj bukem / Good looking Rec., UK: "Really love this music." Velanche / XLR8R, UK: "Awesome job he\'s done... overall production is dope." Kwesi / BBE Music, UK: "Wooooooowwwww... WHAT THE FUCK! THIS IS WHAT',
        "musicBrainzId": "6e1d48f7-717c-416e-af35-5d2454a13af2",
        "smallImageUrl": "http://localhost:8989/play/art/0f8c3cbd6b0b22c3b5402141351ac812/album/21/thumb34.jpg",
        "mediumImageUrl": "http://localhost:8989/play/art/41b16680dc1b3aaf5dfba24ddb6a1712/album/21/thumb64.jpg",
        "largeImageUrl": "http://localhost:8989/play/art/e6fd8d4e0d35c4436e56991892bfb27b/album/21/thumb174.jpg",
    }


@pytest.fixture
def mock_get_album_info(
    mock_generator: MockGenerator, album: dict[str, Any], album_info: dict[str, Any]
) -> Response:
    return mock_generator(
        "getAlbumInfo2", {"id": album["id"]}, {"albumInfo": album_info}
    )
