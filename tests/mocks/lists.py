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
def from_year() -> int:
    return 2007


@pytest.fixture
def to_year() -> int:
    return 2024


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
