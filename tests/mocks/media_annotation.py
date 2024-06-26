from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def mock_star_song(
    mock_generator: MockGenerator, song: dict[str, Any]
) -> list[Response]:
    return mock_generator("star", {"id": song["id"]})


@pytest.fixture
def mock_star_album(
    mock_generator: MockGenerator, album: dict[str, Any]
) -> list[Response]:
    return mock_generator("star", {"albumId": album["id"]})


@pytest.fixture
def mock_star_artist(
    mock_generator: MockGenerator, artist: dict[str, Any]
) -> list[Response]:
    return mock_generator("star", {"artistId": artist["id"]})


@pytest.fixture
def mock_unstar_song(
    mock_generator: MockGenerator, song: dict[str, Any]
) -> list[Response]:
    return mock_generator("unstar", {"id": song["id"]})


@pytest.fixture
def mock_unstar_album(
    mock_generator: MockGenerator, album: dict[str, Any]
) -> list[Response]:
    return mock_generator("unstar", {"albumId": album["id"]})


@pytest.fixture
def mock_unstar_artist(
    mock_generator: MockGenerator, artist: dict[str, Any]
) -> list[Response]:
    return mock_generator("unstar", {"artistId": artist["id"]})


@pytest.fixture
def mock_set_rating_zero(
    song: dict[str, Any], mock_generator: MockGenerator
) -> list[Response]:
    return mock_generator("setRating", {"id": song["id"], "rating": 0})


@pytest.fixture
def scrobble_time() -> int:
    return 1678935707000


@pytest.fixture
def mock_scrobble_submission(
    mock_generator: MockGenerator, song: dict[str, Any], scrobble_time: int
) -> list[Response]:
    return mock_generator(
        "scrobble", {"id": song["id"], "time": scrobble_time, "submission": True}
    )


@pytest.fixture
def mock_scrobble_now_playing(
    mock_generator: MockGenerator, song: dict[str, Any], scrobble_time: int
) -> list[Response]:
    return mock_generator(
        "scrobble", {"id": song["id"], "time": scrobble_time, "submission": False}
    )
