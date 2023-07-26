from typing import Any

import pytest
import responses
from knuckles.subsonic import Subsonic
from responses import Response


@responses.activate
def test_jukebox_get(
    subsonic: Subsonic,
    jukebox_playlist: dict[str, Any],
    mock_jukebox_control_get: Response,
) -> None:
    responses.add(mock_jukebox_control_get)

    response = subsonic.jukebox.get()

    assert response.current_index == jukebox_playlist["currentIndex"]
    assert response.playing == jukebox_playlist["playing"]
    assert response.gain == jukebox_playlist["gain"]
    assert response.position == jukebox_playlist["position"]
    assert type(response.playlist) == list
    assert response.playlist[0].id == jukebox_playlist["entry"][0]["id"]


@responses.activate
def test_jukebox_status(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_status: Response,
) -> None:
    responses.add(mock_jukebox_control_status)

    response = subsonic.jukebox.status()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set(
    subsonic: Subsonic,
    song: dict[str, Any],
    jukebox_status: dict[str, Any],
    mock_jukebox_control_set: Response,
) -> None:
    responses.add(mock_jukebox_control_set)

    response = subsonic.jukebox.set(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert type(response.playlist) == list
    assert response.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_start(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_start: Response,
) -> None:
    responses.add(mock_jukebox_control_start)

    response = subsonic.jukebox.start()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_stop(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_stop: Response,
) -> None:
    responses.add(mock_jukebox_control_stop)

    response = subsonic.jukebox.stop()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_without_offset(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_skip_without_offset: Response,
) -> None:
    responses.add(mock_jukebox_control_skip_without_offset)

    response = subsonic.jukebox.skip(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_with_offset(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_skip_with_offset: Response,
    offset_time: int,
) -> None:
    responses.add(mock_jukebox_control_skip_with_offset)

    response = subsonic.jukebox.skip(0, offset_time)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_add(
    subsonic: Subsonic,
    song: dict[str, Any],
    jukebox_status: dict[str, Any],
    mock_jukebox_control_add: Response,
) -> None:
    responses.add(mock_jukebox_control_add)

    response = subsonic.jukebox.add(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_clear(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_clear: Response,
) -> None:
    responses.add(mock_jukebox_control_clear)

    response = subsonic.jukebox.clear()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_remove(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_remove: Response,
) -> None:
    responses.add(mock_jukebox_control_remove)

    response = subsonic.jukebox.remove(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_shuffle(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_shuffle: Response,
) -> None:
    responses.add(mock_jukebox_control_shuffle)

    response = subsonic.jukebox.shuffle()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set_gain(
    subsonic: Subsonic,
    jukebox_status: dict[str, Any],
    mock_jukebox_control_set_gain: Response,
) -> None:
    responses.add(mock_jukebox_control_set_gain)

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
