from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def mock_search_song(
    mock_generator: MockGenerator,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> Response:
    return mock_generator(
        "search3",
        {"songCount": 1, "songOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult3": {"song": [song]}},
    )


@pytest.fixture
def mock_search_album(
    mock_generator: MockGenerator, music_folders, album: dict[str, Any]
) -> Response:
    return mock_generator(
        "search3",
        {"albumCount": 1, "albumOffset": 0},
        {"musicFolderId": music_folders[0]["id"], "searchResult3": {"album": [album]}},
    )


@pytest.fixture
def mock_search_artist(
    mock_generator: MockGenerator, music_folders, artist: dict[str, Any]
) -> Response:
    return mock_generator(
        "search3",
        {"artistCount": 1, "artistOffset": 0},
        {
            "musicFolderId": music_folders[0]["id"],
            "searchResult3": {"artist": [artist]},
        },
    )
