from typing import Any

import responses
from responses import Response

from knuckles.models import Jukebox
from knuckles.subsonic import Subsonic


@responses.activate
def test_jukebox_generate(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_get: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_get)

    response = subsonic.jukebox.status()

    assert response.playlist is None

    jukebox = response.generate()

    assert jukebox.playlist is not None
    assert jukebox.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_start(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_start: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_start)

    response = subsonic.jukebox.status()
    response.start()


@responses.activate
def test_jukebox_stop(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_stop: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_stop)

    response = subsonic.jukebox.status()
    response.stop()


@responses.activate
def test_jukebox_skip_without_offset(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_skip_without_offset: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response.skip(0)


@responses.activate
def test_jukebox_skip_with_offset(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_skip_without_offset: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response.skip(0, 1)


@responses.activate
def test_jukebox_shuffle(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_shuffle: Response,
    mock_jukebox_control_get: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_shuffle)
    responses.add(mock_jukebox_control_get)

    response = subsonic.jukebox.status()
    response.shuffle()
    # Ignore the error as in normal conditions it should exists
    assert response.playlist[0].id == song["id"]  # type: ignore[index]


@responses.activate
def test_jukebox_set_gain(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_set_gain: Response,
    jukebox_status: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_set_gain)

    response: Jukebox = subsonic.jukebox.status()
    response.set_gain(jukebox_status["gain"])


@responses.activate
def test_jukebox_clear(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_clear: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_clear)

    response = subsonic.jukebox.status()
    response.clear()


@responses.activate
def test_jukebox_set(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_set: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_set)

    response: Jukebox = subsonic.jukebox.status()
    response.set(song["id"])

    # Ignore the error as in normal conditions it should exists
    assert response.playlist[0].id == song["id"]  # type: ignore[index]


@responses.activate
def test_jukebox_remove_with_populated_playlist(
    subsonic: Subsonic,
    mock_jukebox_control_get: Response,
    mock_jukebox_control_remove: Response,
) -> None:
    responses.add(mock_jukebox_control_get)
    responses.add(mock_jukebox_control_remove)

    response: Jukebox = subsonic.jukebox.get()
    response.remove(0)

    assert response.playlist == []


@responses.activate
def test_jukebox_add_with_a_populated_playlist(
    subsonic: Subsonic,
    mock_jukebox_control_get: Response,
    mock_jukebox_control_add: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_get)
    responses.add(mock_jukebox_control_add)

    response: Jukebox = subsonic.jukebox.get()
    response.add(song["id"])

    # Ignore the error as in normal conditions it should exists
    assert response.playlist[1].id == song["id"]  # type: ignore[index]


@responses.activate
def test_jukebox_add_without_a_populated_playlist(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_get: Response,
    mock_jukebox_control_add: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_get)
    responses.add(mock_jukebox_control_add)

    response: Jukebox = subsonic.jukebox.status()
    response.add(song["id"])

    # Ignore the error as in normal conditions it should exists
    assert response.playlist[0].id == song["id"]  # type: ignore[index]
