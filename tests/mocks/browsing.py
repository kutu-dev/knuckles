from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def music_folders() -> list[dict[str, Any]]:
    return [{"id": "1", "name": "music"}]


@pytest.fixture
def mock_get_music_folders(
    mock_generator: MockGenerator, music_folders: dict[str, Any]
) -> Response:
    return mock_generator(
        "getMusicFolders", {}, {"musicFolders": {"musicFolder": music_folders}}
    )


@pytest.fixture
def genre() -> dict[str, Any]:
    return {"songCount": 1, "albumCount": 1, "value": "Jazz"}


@pytest.fixture
def mock_get_genres(mock_generator: MockGenerator, genre: dict[str, Any]) -> Response:
    return mock_generator("getGenres", {}, {"genres": {"genre": [genre]}})


@pytest.fixture()
def artist(album: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "37ec820ca7193e17040c98f7da7c4b51",
        "name": "2 Mello",
        "coverArt": "ar-37ec820ca7193e17040c98f7da7c4b51_0",
        "albumCount": 1,
        "userRating": 5,
        "averageRating": 4.5,
        "artistImageUrl": "https://example.com/artist.png",
        "starred": "2017-04-11T10:42:50.842Z",
        "album": [album],
    }


@pytest.fixture()
def artists(artist: dict[str, Any]) -> dict[str, Any]:
    return {
        "ignoredArticles": "The An A Die Das Ein Eine Les Le La",
        "index": [
            {
                "name": "#",
                "artist": [artist],
            }
        ],
    }


@pytest.fixture()
def mock_get_artists(
    mock_generator: MockGenerator,
    artists: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> Response:
    return mock_generator(
        "getArtists", {"musicFolderId": music_folders[0]["id"]}, {"artists": artists}
    )


@pytest.fixture()
def mock_get_artist(mock_generator: MockGenerator, artist: dict[str, Any]) -> Response:
    return mock_generator("getArtist", {"id": artist["id"]}, {"artist": artist})


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
        "notes": "Example note",
        "musicBrainzId": "6e1d48f7-717c-416e-af35-5d2454a13af2",
        "lastFmUrl": "https://example.com/lastfm/album",
        "smallImageUrl": "https://example.com/album/small.png",
        "mediumImageUrl": "https://example.com/album/medium.png",
        "largeImageUrl": "https://example.com/album/large.png",
    }


@pytest.fixture
def mock_get_album_info(
    mock_generator: MockGenerator, album: dict[str, Any], album_info: dict[str, Any]
) -> Response:
    return mock_generator(
        "getAlbumInfo2", {"id": album["id"]}, {"albumInfo": album_info}
    )


@pytest.fixture
def artist_info(artist: dict[str, Any]) -> dict[str, Any]:
    return {
        "biography": {},
        "musicBrainzId": "1",
        "lastFmUrl": "",
        "smallImageUrl": "http://localhost:8989/play/art/f20070e8e11611cc53542a38801d60fa/artist/2/thumb34.jpg",
        "mediumImageUrl": "http://localhost:8989/play/art/2b9b6c057cd4bf21089ce7572e7792b6/artist/2/thumb64.jpg",
        "largeImageUrl": "http://localhost:8989/play/art/e18287c23a75e263b64c31b3d64c1944/artist/2/thumb174.jpg",
        "similarArtist": [artist],
    }


@pytest.fixture
def mock_get_artist_info(
    mock_generator: MockGenerator, artist: dict[str, Any], artist_info: dict[str, Any]
) -> Response:
    return mock_generator(
        "getArtistInfo2",
        {
            "id": artist["id"],
        },
        {"artistInfo2": artist_info},
    )


@pytest.fixture
def mock_get_artist_info_with_all_optional_params(
    mock_generator: MockGenerator, artist: dict[str, Any], artist_info: dict[str, Any]
) -> Response:
    return mock_generator(
        "getArtistInfo2",
        {
            "id": artist["id"],
            "count": len(artist_info["similarArtist"]),
            "includeNotPresent": False,
        },
        {"artistInfo2": artist_info},
    )
