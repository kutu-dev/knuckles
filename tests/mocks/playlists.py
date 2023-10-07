from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def playlist(song: dict[str, Any], username: str) -> dict[str, Any]:
    return {
        "id": "800000075",
        "name": "Chill",
        "comment": "comment",
        "owner": username,
        "public": True,
        "created": "2023-03-16T03:18:41+00:00",
        "changed": "2023-03-16T03:18:41+00:00",
        "songCount": 1,
        "duration": 304,
        "entry": [song],
        "coverArt": song["coverArt"],
        "allowedUser": [username],
    }


@pytest.fixture
def mock_get_playlists(
    mock_generator: MockGenerator, playlist: dict[str, Any]
) -> Response:
    return mock_generator("getPlaylists", {}, {"playlists": {"playlist": [playlist]}})


@pytest.fixture
def mock_get_playlists_with_a_selected_user(
    mock_generator: MockGenerator, playlist: dict[str, Any], username: str
) -> Response:
    return mock_generator(
        "getPlaylists", {"username": username}, {"playlists": {"playlist": [playlist]}}
    )


@pytest.fixture
def mock_get_playlist(
    mock_generator: MockGenerator, playlist: dict[str, Any]
) -> Response:
    return mock_generator("getPlaylist", {"id": playlist["id"]}, {"playlist": playlist})


@pytest.fixture
def mock_create_playlist(
    mock_generator: MockGenerator,
    playlist: dict[str, Any],
    song: dict[str, Any],
) -> Response:
    return mock_generator(
        "createPlaylist",
        {"name": playlist["name"], "songId": song["id"]},
        {"playlist": playlist},
    )


@pytest.fixture
def mock_update_playlist(
    mock_generator: MockGenerator,
    playlist: dict[str, Any],
    song: dict[str, Any],
) -> Response:
    return mock_generator(
        "updatePlaylist",
        {
            "playlistId": playlist["id"],
            "name": playlist["name"],
            "comment": playlist["comment"],
            "public": True,
            "songIdToAdd": song["id"],
            "songIndexToRemove": 0,
        },
    )


@pytest.fixture
def mock_update_comment_and_public(
    mock_generator: MockGenerator,
    playlist: dict[str, Any],
) -> Response:
    return mock_generator(
        "updatePlaylist",
        {
            "playlistId": playlist["id"],
            "comment": playlist["comment"],
            "public": True,
        },
    )


@pytest.fixture
def mock_delete_playlist(
    mock_generator: MockGenerator, playlist: dict[str, Any]
) -> Response:
    return mock_generator("deletePlaylist", {"id": playlist["id"]})
