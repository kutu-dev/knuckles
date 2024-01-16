from typing import Any

import pytest
import responses
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_jukebox_get(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_playlist: dict[str, Any],
    mock_jukebox_control_get: list[Response],
) -> None:
    add_responses(mock_jukebox_control_get)

    response = subsonic.jukebox.get()

    assert response.current_index == jukebox_playlist["currentIndex"]
    assert response.playing == jukebox_playlist["playing"]
    assert response.gain == jukebox_playlist["gain"]
    assert response.position == jukebox_playlist["position"]
    assert type(response.playlist) is list
    assert response.playlist[0].id == jukebox_playlist["entry"][0]["id"]


@responses.activate
def test_jukebox_status(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_status: list[Response],
) -> None:
    add_responses(mock_jukebox_control_status)

    response = subsonic.jukebox.status()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set(
    add_responses: AddResponses,
    subsonic: Subsonic,
    song: dict[str, Any],
    jukebox_status: dict[str, Any],
    mock_jukebox_control_set: list[Response],
) -> None:
    add_responses(mock_jukebox_control_set)

    response = subsonic.jukebox.set(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert type(response.playlist) is list
    assert response.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_start(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_start: list[Response],
) -> None:
    add_responses(mock_jukebox_control_start)

    response = subsonic.jukebox.start()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_stop(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_stop: list[Response],
) -> None:
    add_responses(mock_jukebox_control_stop)

    response = subsonic.jukebox.stop()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_without_offset(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_skip_without_offset: list[Response],
) -> None:
    add_responses(mock_jukebox_control_skip_without_offset)

    response = subsonic.jukebox.skip(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_with_offset(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_skip_with_offset: list[Response],
    offset_time: int,
) -> None:
    add_responses(mock_jukebox_control_skip_with_offset)

    response = subsonic.jukebox.skip(0, offset_time)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_add(
    add_responses: AddResponses,
    subsonic: Subsonic,
    song: dict[str, Any],
    jukebox_status: dict[str, Any],
    mock_jukebox_control_add: list[Response],
) -> None:
    add_responses(mock_jukebox_control_add)

    response = subsonic.jukebox.add(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_clear(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_clear: list[Response],
) -> None:
    add_responses(mock_jukebox_control_clear)

    response = subsonic.jukebox.clear()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_remove(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_remove: list[Response],
) -> None:
    add_responses(mock_jukebox_control_remove)

    response = subsonic.jukebox.remove(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_shuffle(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_shuffle: list[Response],
) -> None:
    add_responses(mock_jukebox_control_shuffle)

    response = subsonic.jukebox.shuffle()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set_gain(
    add_responses: AddResponses,
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_set_gain: list[Response],
) -> None:
    add_responses(mock_jukebox_control_set_gain)

    response = subsonic.jukebox.set_gain(jukebox_status["gain"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set_invalid_gain(
    subsonic: Subsonic,
) -> None:
    with pytest.raises(
        ValueError,
        match="The gain should be between 0 and 1 \(inclusive\)",
    ):
        subsonic.jukebox.set_gain(2)
