from typing import Any, Protocol

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def jukebox_playlist(
    jukebox_status: dict[str, Any], song: dict[str, Any]
) -> dict[str, Any]:
    return {**jukebox_status, "entry": [song]}


@pytest.fixture
def mock_jukebox_control_get(
    mock_generator: MockGenerator, jukebox_playlist: dict[str, Any]
) -> Response:
    return mock_generator(
        "jukeboxControl", {"action": "get"}, {"jukeboxPlaylist": jukebox_playlist}
    )


class JukeboxStatusGenerator(Protocol):
    def __call__(
        self,
        action: str,
        extra_params: dict[str, Any] = {},
    ) -> Response:
        ...


@pytest.fixture
def jukebox_status() -> dict[str, Any]:
    return {"currentIndex": 7, "playing": True, "gain": 0.9, "position": 67}


@pytest.fixture
def jukebox_status_generator(
    mock_generator: MockGenerator, jukebox_status: dict[str, Any]
) -> JukeboxStatusGenerator:
    """A factory function to generate all the Response objects
    that returns jukebox_status as their data."""

    def inner(action: str, extra_params: dict[str, Any] = {}) -> Response:
        return mock_generator(
            "jukeboxControl",
            {"action": action, **extra_params},
            {"jukeboxStatus": jukebox_status},
        )

    return inner


@pytest.fixture
def mock_jukebox_control_status(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("status")


@pytest.fixture
def mock_jukebox_control_set(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("set")


@pytest.fixture
def mock_jukebox_control_start(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("start")


@pytest.fixture
def mock_jukebox_control_stop(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("stop")


@pytest.fixture
def mock_jukebox_control_skip_without_offset(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("skip", {"index": 0})


@pytest.fixture
def offset_time() -> int:
    return 1


@pytest.fixture
def mock_jukebox_control_skip_with_offset(
    jukebox_status_generator: JukeboxStatusGenerator, offset_time: int
) -> Response:
    return jukebox_status_generator("skip", {"index": 0, "offset": offset_time})


@pytest.fixture
def mock_jukebox_control_add(
    jukebox_status_generator: JukeboxStatusGenerator, song: dict[str, Any]
) -> Response:
    return jukebox_status_generator("add", {"id": song["id"]})


@pytest.fixture
def mock_jukebox_control_clear(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("clear")


@pytest.fixture
def mock_jukebox_control_remove(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("remove", {"index": 0})


@pytest.fixture
def mock_jukebox_control_shuffle(
    jukebox_status_generator: JukeboxStatusGenerator,
) -> Response:
    return jukebox_status_generator("shuffle")


@pytest.fixture
def mock_jukebox_control_set_gain(
    jukebox_status_generator: JukeboxStatusGenerator, jukebox_status: dict[str, Any]
) -> Response:
    return jukebox_status_generator("setGain", {"gain": jukebox_status["gain"]})
