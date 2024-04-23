from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def mock_search_song_non_id3(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search2",
        {"songCount": 1, "songOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult2": {"song": [song]}},
    )


@pytest.fixture
def mock_search_album_non_id3(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    album: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search2",
        {"albumCount": 1, "albumOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult2": {"album": [album]}},
    )


@pytest.fixture
def mock_search_artist_non_id3(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    artist: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search2",
        {"artistCount": 1, "artistOffset": 0},
        {
            "musicFolderId": music_folders[0]["id"],
            "searchResult2": {"artist": [artist]},
        },
    )


@pytest.fixture
def mock_search_song(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search3",
        {"songCount": 1, "songOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult3": {"song": [song]}},
    )


@pytest.fixture
def mock_search_album(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    album: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search3",
        {"albumCount": 1, "albumOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult3": {"album": [album]}},
    )


@pytest.fixture
def mock_search_artist(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    artist: dict[str, Any],
) -> list[Response]:
    return mock_generator(
        "search3",
        {"artistCount": 1, "artistOffset": 0},
        {
            "musicFolderId": music_folders[0]["id"],
            "searchResult3": {"artist": [artist]},
        },
    )
