from typing import Any

import pytest
import responses
from knuckles.models import Song
from knuckles.subsonic import Subsonic
from responses import matchers


@responses.activate
def test_jukebox_get(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_playlist: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_get()

    assert response.current_index == jukebox_playlist["currentIndex"]
    assert response.playing == jukebox_playlist["playing"]
    assert response.gain == jukebox_playlist["gain"]
    assert response.position == jukebox_playlist["position"]
    assert type(response.playlist) == list
    assert response.playlist[0] == Song
    assert response.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_status(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    song: dict[str, Any],
) -> None:
    params["action"] = "set"
    params["id"] = song["id"]
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_set(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_start(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "start"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_start()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_stop(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "stop"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_stop()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_without_offset(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "skip"
    params["index"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_skip(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_skip_with_offset(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "skip"
    params["index"] = 0
    params["offset"] = 10
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_skip(0, 10)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_add(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    song: dict[str, Any],
) -> None:
    params["action"] = "add"
    params["id"] = song["id"]
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_add(song["id"])

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_add_invalid_id(
    subsonic: Subsonic,
) -> None:
    #!TYPES

    with pytest.raises(
        TypeError,
        match="The type of the song parameter is invalid",
    ):
        subsonic.jukebox_add(True)  # type: ignore[arg-type]


@responses.activate
def test_jukebox_clear(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "clear"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_clear()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_remove(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "remove"
    params["index"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_remove(0)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_shuffle(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "shuffle"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_shuffle()

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set_gain(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    params["action"] = "setGain"
    params["gain"] = 0.75
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukeboxControl",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_set_gain(0.75)

    assert response.current_index == jukebox_status["currentIndex"]
    assert response.playing == jukebox_status["playing"]
    assert response.gain == jukebox_status["gain"]
    assert response.position == jukebox_status["position"]
    assert response.playlist is None


@responses.activate
def test_jukebox_set_invalid_gain(
    subsonic: Subsonic,
) -> None:
    #!TYPES

    with pytest.raises(
        ValueError,
        match="The gain should be between 0 and 1 \(inclusive\)",
    ):
        subsonic.jukebox_set_gain(2)
