from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def num_of_album() -> int:
    return 20


@pytest.fixture
def album_list_offset() -> int:
    return 16


@pytest.fixture
def from_year() -> int:
    return 2007


@pytest.fixture
def to_year() -> int:
    return 2024


@pytest.fixture
def mock_get_album_list_random_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "random",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_newest_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "newest",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_highest_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "highest",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_frequent_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "frequent",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_recent_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "recent",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_alphabetical_by_name_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "alphabeticalByName",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_alphabetical_by_artist_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "alphabeticalByArtist",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_starred_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "starred",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_by_year_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    from_year: int,
    to_year: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "byYear",
            "size": num_of_album,
            "offset": album_list_offset,
            "fromYear": from_year,
            "toYear": to_year,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_by_genre_non_id3(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    genre: dict[str, Any],
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList",
        {
            "type": "byGenre",
            "size": num_of_album,
            "genre": genre["value"],
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_random(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "random",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_newest(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "newest",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_highest(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "highest",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_frequent(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "frequent",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_recent(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "recent",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_alphabetical_by_name(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "alphabeticalByName",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_alphabetical_by_artist(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "alphabeticalByArtist",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_starred(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "starred",
            "size": num_of_album,
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_by_year(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    from_year: int,
    to_year: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "byYear",
            "size": num_of_album,
            "offset": album_list_offset,
            "fromYear": from_year,
            "toYear": to_year,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def mock_get_album_list_by_genre(
    mock_generator: MockGenerator,
    album: dict[str, Any],
    num_of_album: int,
    genre: dict[str, Any],
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> list[Response]:
    return mock_generator(
        "getAlbumList2",
        {
            "type": "byGenre",
            "size": num_of_album,
            "genre": genre["value"],
            "offset": album_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"albumList2": {"album": [album]}},
    )


@pytest.fixture
def num_of_songs() -> int:
    return 125


@pytest.fixture
def mock_get_random_songs(
    mock_generator: MockGenerator,
    num_of_songs: int,
    genre: dict[str, Any],
    from_year: int,
    to_year: int,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getRandomSongs",
        {
            "genre": genre["value"],
            "fromYear": from_year,
            "toYear": to_year,
            "musicFolderId": music_folders[0]["id"],
        },
        {"randomSongs": {"song": [song]}},
    )


@pytest.fixture
def song_list_offset() -> int:
    return 27


@pytest.fixture
def mock_get_songs_by_genre(
    mock_generator: MockGenerator,
    genre: dict[str, Any],
    songs_count: int,
    song_list_offset: int,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getSongsByGenre",
        {
            "genre": genre["value"],
            "count": songs_count,
            "offset": song_list_offset,
            "musicFolderId": music_folders[0]["id"],
        },
        {"songsByGenre": {"song": [song]}},
    )


@pytest.fixture
def now_playing_entry(username: str, song: dict[str, Any]) -> dict[str, Any]:
    return {
        "username": username,
        "minutesAgo": 79,
        "playerId": 25565,
        "playerName": "dorothy",
        **song,
    }


@pytest.fixture
def mock_get_now_playing(
    mock_generator: MockGenerator, now_playing_entry: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getNowPlaying", {}, {"nowPlaying": {"entry": [now_playing_entry]}}
    )


@pytest.fixture
def mock_get_starred_non_id3(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
    album: dict[str, Any],
    artist: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getStarred",
        {"musicFolderId": music_folders[0]["id"]},
        {"starred": {"song": [song], "album": [album], "artist": [artist]}},
    )


@pytest.fixture
def mock_get_starred(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
    album: dict[str, Any],
    artist: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "getStarred2",
        {"musicFolderId": music_folders[0]["id"]},
        {"starred2": {"song": [song], "album": [album], "artist": [artist]}},
    )
