from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def music_folders() -> list[dict[str, Any]]:
    return [{"id": "1", "name": "music"}]


@pytest.fixture
def mock_get_music_folders(
    mock_generator: MockGenerator, music_folders: list[dict[str, Any]]
) -> list[Response]:
    return mock_generator(
        "getMusicFolders", {}, {"musicFolders": {"musicFolder": music_folders}}
    )


@pytest.fixture
def modified_date() -> int:
    return 117


@pytest.fixture
def indexes(artist: dict[str, Any]) -> dict[str, Any]:
    return {
        "ignoredArticles": "The An A Die Das Ein Eine Les Le La",
        "index": [
            {
                "name": "C",
                "artist": [artist],
            },
        ],
    }


@pytest.fixture
def mock_get_indexes(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    modified_date: int,
    indexes: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getIndexes",
        {"musicFolderId": music_folders[0]["id"], "ifModifiedSince": modified_date},
        {"indexes": indexes},
    )


@pytest.fixture
def music_directory(song: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "1",
        "parent": "0",
        "name": "music",
        "starred": "2023-03-16T03:18:41+00:00",
        "userRating": 1,
        "averageRating": 1.6,
        "playCount": 360,
        "child": [song],
    }


@pytest.fixture
def mock_get_music_directory(
    mock_generator: MockGenerator, music_directory: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getMusicDirectory",
        {"id": music_directory["id"]},
        {"directory": music_directory},
    )


@pytest.fixture
def genre() -> dict[str, Any]:
    return {"songCount": 1, "albumCount": 1, "value": "Jazz"}


@pytest.fixture
def mock_get_genres(
    mock_generator: MockGenerator, genre: dict[str, Any]
) -> list[Response]:
    return mock_generator("getGenres", {}, {"genres": {"genre": [genre]}})


@pytest.fixture()
def artist(base_url: str, album: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "37ec820ca7193e17040c98f7da7c4b51",
        "name": "2 Mello",
        "coverArt": "ar-37ec820ca7193e17040c98f7da7c4b51_0",
        "albumCount": 1,
        "userRating": 5,
        "averageRating": 4.5,
        "artistImageUrl": f"{base_url}/artist.png",
        "starred": "2017-04-11T10:42:50.842Z",
        "album": [album],
        "musicBrainzId": "189002e7-3285-4e2e-92a3-7f6c30d407a2",
        "sortName": "Mello (2)",
        "roles": ["artist", "albumartist", "composer"],
    }


@pytest.fixture()
def artists(artist: dict[str, Any]) -> dict[str, Any]:
    return {
        "ignoredArticles": "The An A Die Das Ein Les Le La",
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
) -> list[Response]:
    return mock_generator(
        "getArtists", {"musicFolderId": music_folders[0]["id"]}, {"artists": artists}
    )


@pytest.fixture()
def mock_get_artist(
    mock_generator: MockGenerator, artist: dict[str, Any]
) -> list[Response]:
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
        "recordLabels": [{"name": "Sony"}],
        "musicBrainzId": "189002e7-3285-4e2e-92a3-7f6c30d407a2",
        "genres": [{"name": "Hip-Hop"}, {"name": "East coast"}],
        "artists": [
            {"id": "ar-1", "name": "Artist 1"},
            {"id": "ar-2", "name": "Artist 2"},
        ],
        "displayArtist": "Artist 1 feat. Artist 2",
        "releaseTypes": ["Album", "Remixes"],
        "moods": ["slow", "cool"],
        "sortName": "lagerfeuer (8-bit)",
        "originalReleaseDate": {"year": 2001, "month": 3, "day": 10},
        "releaseDate": {"year": 2001, "month": 3, "day": 10},
        "isCompilation": False,
        "discTitles": [
            {"disc": 0, "title": "Disc 0 title"},
            {"disc": 2, "title": "Disc 1 title"},
        ],
    }


@pytest.fixture
def mock_get_album(
    mock_generator: MockGenerator, album: dict[str, Any]
) -> list[Response]:
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
        "bpm": 134,
        "comment": "This is a song comment",
        "sortName": "Polar expedition",
        "musicBrainzId": "189002e7-3285-4e2e-92a3-7f6c30d407a2",
        "genres": [{"name": "Hip-Hop"}, {"name": "East coast"}],
        "artists": [
            {"id": "ar-1", "name": "Artist 1"},
            {"id": "ar-2", "name": "Artist 2"},
        ],
        "displayArtist": "Artist 1 feat. Artist 2",
        "albumArtists": [
            {"id": "ar-6", "name": "Artist 6"},
            {"id": "ar-7", "name": "Artist 7"},
        ],
        "displayAlbumArtist": "Artist 6 & Artist 7",
        "contributors": [
            {"role": "composer", "artist": {"id": "ar-3", "name": "Artist 3"}},
            {"role": "composer", "artist": {"id": "ar-4", "name": "Artist 4"}},
            {"role": "lyricist", "artist": {"id": "ar-5", "name": "Artist 5"}},
            {
                "role": "performer",
                "subRole": "Bass",
                "artist": {"id": "ar-5", "name": "Artist 5"},
            },
        ],
        "displayComposer": "Artist 3, Artist 4",
        "moods": ["slow", "cool"],
        "replayGain": {
            "trackGain": 0.1,
            "albumGain": 1.1,
            "trackPeak": 9.2,
            "albumPeak": 9,
            "baseGain": 0,
        },
    }


@pytest.fixture
def mock_get_song(
    mock_generator: MockGenerator, song: dict[str, Any]
) -> list[Response]:
    return mock_generator("getSong", {"id": song["id"]}, {"song": song})


@pytest.fixture
def video() -> dict[str, Any]:
    return {"id": "videoId", "suffix": "mpv"}


@pytest.fixture
def mock_get_videos(
    mock_generator: MockGenerator,
    video: dict[str, Any],
) -> list[Response]:
    return mock_generator("getVideos", {}, {"videos": {"video": [video]}})


@pytest.fixture
def video_info() -> dict[str, Any]:
    return {
        "captions": {"id": "0", "name": "Planes 2.srt"},
        "audioTrack": [
            {"id": "1", "name": "English", "languageCode": "eng"},
        ],
        "conversion": {"id": "37", "bitRate": "1000"},
        "id": "7058",
    }


@pytest.fixture
def mock_get_video_info(
    mock_generator: MockGenerator, video: dict[str, Any], video_info: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getVideoInfo", {"id": video["id"]}, {"videoInfo": video_info}
    )


@pytest.fixture
def album_info(base_url: str) -> dict[str, Any]:
    return {
        "notes": "Example note",
        "musicBrainzId": "6e1d48f7-717c-416e-af35-5d2454a13af2",
        "lastFmUrl": f"{base_url}/lastfm/album",
        "smallImageUrl": f"{base_url}/album/small.png",
        "mediumImageUrl": f"{base_url}/album/medium.png",
        "largeImageUrl": f"{base_url}/album/large.png",
    }


@pytest.fixture
def mock_get_album_info_non_id3(
    mock_generator: MockGenerator, album: dict[str, Any], album_info: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getAlbumInfo", {"id": album["id"]}, {"albumInfo": album_info}
    )


@pytest.fixture
def mock_get_album_info(
    mock_generator: MockGenerator, album: dict[str, Any], album_info: dict[str, Any]
) -> list[Response]:
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
def max_num_similar_artists() -> int:
    return 21


@pytest.fixture
def artist_include_not_present() -> bool:
    return False


@pytest.fixture
def mock_get_artist_info_non_id3(
    mock_generator: MockGenerator,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
    max_num_similar_artists: int,
    artist_include_not_present: bool,
) -> list[Response]:
    return mock_generator(
        "getArtistInfo",
        {
            "id": artist["id"],
            "count": max_num_similar_artists,
            "includeNotPresent": artist_include_not_present,
        },
        {"artistInfo": artist_info},
    )


@pytest.fixture
def mock_get_artist_info(
    mock_generator: MockGenerator,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
    max_num_similar_artists: int,
    artist_include_not_present: bool,
) -> list[Response]:
    return mock_generator(
        "getArtistInfo2",
        {
            "id": artist["id"],
            "count": max_num_similar_artists,
            "includeNotPresent": artist_include_not_present,
        },
        {"artistInfo2": artist_info},
    )


@pytest.fixture
def mock_get_artist_info_minimal(
    mock_generator: MockGenerator, artist: dict[str, Any], artist_info: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getArtistInfo2",
        {
            "id": artist["id"],
        },
        {"artistInfo2": artist_info},
    )


@pytest.fixture
def songs_count() -> int:
    return 125


@pytest.fixture
def mock_get_similar_songs_non_id3(
    mock_generator: MockGenerator, song: dict[str, Any], songs_count: int
) -> list[Response]:
    return mock_generator(
        "getSimilarSongs",
        {"id": song["id"], "count": songs_count},
        {"similarSongs": {"song": [song]}},
    )


@pytest.fixture
def mock_get_similar_songs(
    mock_generator: MockGenerator, song: dict[str, Any], songs_count: int
) -> list[Response]:
    return mock_generator(
        "getSimilarSongs2",
        {"id": song["id"], "count": songs_count},
        {"similarSongs2": {"song": [song]}},
    )


@pytest.fixture
def mock_get_top_songs(
    mock_generator: MockGenerator,
    artist: dict[str, Any],
    songs_count: int,
    song: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getTopSongs",
        {"artist": artist["name"], "count": songs_count},
        {"topSongs": {"song": [song]}},
    )
