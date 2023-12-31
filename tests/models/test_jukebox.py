from typing import Any

import responses
from knuckles import Jukebox
from knuckles.subsonic import Subsonic
from responses import Response


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
    response = response.start()

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_stop(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_stop: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_stop)

    response = subsonic.jukebox.status()
    response = response.stop()

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_skip_without_offset(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_skip_without_offset: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response = response.skip(0)

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_skip_with_offset(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_skip_without_offset: Response,
    offset_time: int,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response = response.skip(0, offset_time)

    assert type(response) is Jukebox


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
    response = response.shuffle()

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
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
    response = response.set_gain(jukebox_status["gain"])

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_clear(
    subsonic: Subsonic,
    mock_jukebox_control_status: Response,
    mock_jukebox_control_clear: Response,
) -> None:
    responses.add(mock_jukebox_control_status)
    responses.add(mock_jukebox_control_clear)

    response = subsonic.jukebox.status()
    response = response.clear()

    assert type(response) is Jukebox


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
    response = response.set(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
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
    response = response.remove(0)

    assert type(response) is Jukebox
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
    response = response.add(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
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
    response = response.add(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
    assert response.playlist[0].id == song["id"]  # type: ignore[index]
