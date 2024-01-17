from typing import Any

import responses
from knuckles import Jukebox
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_jukebox_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_get: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_get)

    response = subsonic.jukebox.status()

    assert response.playlist is None

    jukebox = response.generate()

    assert jukebox.playlist is not None
    assert jukebox.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_start(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_start: list[Response],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_start)

    response = subsonic.jukebox.status()
    response = response.start()

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_stop(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_stop: list[Response],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_stop)

    response = subsonic.jukebox.status()
    response = response.stop()

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_skip_without_offset(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_skip_without_offset: list[Response],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response = response.skip(0)

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_skip_with_offset(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_skip_without_offset: list[Response],
    offset_time: int,
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_skip_without_offset)

    response: Jukebox = subsonic.jukebox.status()
    response = response.skip(0, offset_time)

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_shuffle(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_shuffle: list[Response],
    mock_jukebox_control_get: Response,
    song: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_shuffle)
    add_responses(mock_jukebox_control_get)

    response = subsonic.jukebox.status()
    response = response.shuffle()

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
    assert response.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_set_gain(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_set_gain: list[Response],
    jukebox_status: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_set_gain)

    response: Jukebox = subsonic.jukebox.status()
    response = response.set_gain(jukebox_status["gain"])

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_clear(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_clear: list[Response],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_clear)

    response = subsonic.jukebox.status()
    response = response.clear()

    assert type(response) is Jukebox


@responses.activate
def test_jukebox_set(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_set: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_set)

    response: Jukebox = subsonic.jukebox.status()
    response = response.set(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
    assert response.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_remove_with_populated_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_get: list[Response],
    mock_jukebox_control_remove: list[Response],
) -> None:
    add_responses(mock_jukebox_control_get)
    add_responses(mock_jukebox_control_remove)

    response: Jukebox = subsonic.jukebox.get()
    response = response.remove(0)

    assert type(response) is Jukebox
    assert response.playlist == []


@responses.activate
def test_jukebox_add_with_a_populated_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_get: list[Response],
    mock_jukebox_control_add: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_get)
    add_responses(mock_jukebox_control_add)

    response: Jukebox = subsonic.jukebox.get()
    response = response.add(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
    assert response.playlist[1].id == song["id"]


@responses.activate
def test_jukebox_add_without_a_populated_playlist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_jukebox_control_status: list[Response],
    mock_jukebox_control_get: list[Response],
    mock_jukebox_control_add: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_jukebox_control_status)
    add_responses(mock_jukebox_control_get)
    add_responses(mock_jukebox_control_add)

    response: Jukebox = subsonic.jukebox.status()
    response = response.add(song["id"])

    assert type(response) is Jukebox
    # Ignore the error as in normal conditions it should exist
    assert response.playlist[0].id == song["id"]
