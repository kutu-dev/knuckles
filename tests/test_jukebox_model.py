from typing import Any

import responses
from responses import matchers

from knuckles.subsonic import Subsonic


@responses.activate
def test_jukebox_non_partial_generate(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()

    assert response.playlist is None

    jukebox_with_playlist = response.generate()

    assert jukebox_with_playlist.playlist[0].id == song["id"]


@responses.activate
def test_jukebox_partial_generate(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.playing = False

    response = response.generate(True)

    assert response.playing is True


@responses.activate
def test_jukebox_start(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    start_params: dict[str, Any] = {**params}
    start_params["action"] = "start"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(start_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    response = subsonic.jukebox_status()
    response.start()


@responses.activate
def test_jukebox_stop(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    stop_params: dict[str, Any] = {**params}
    stop_params["action"] = "stop"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(stop_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    response = subsonic.jukebox_status()
    response.stop()


@responses.activate
def test_jukebox_skip_without_offset(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    skip_params: dict[str, Any] = {**params}
    skip_params["action"] = "skip"
    skip_params["index"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(skip_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.skip(0)


@responses.activate
def test_jukebox_skip_with_offset(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    skip_params: dict[str, Any] = {**params}
    skip_params["action"] = "skip"
    skip_params["index"] = 0
    skip_params["offset"] = 10
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(skip_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.skip(0, 10)


@responses.activate
def test_jukebox_shuffle(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    shuffle_params: dict[str, Any] = {**params}
    shuffle_params["action"] = "shuffle"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(shuffle_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.shuffle()


@responses.activate
def test_jukebox_set_gain(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    set_gain_params: dict[str, Any] = {**params}
    set_gain_params["action"] = "setGain"
    set_gain_params["gain"] = 75
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(set_gain_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.set_gain(75)


@responses.activate
def test_jukebox_clear(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    clear_params: dict[str, Any] = {**params}
    clear_params["action"] = "clear"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(clear_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.clear()


@responses.activate
def test_jukebox_remove_with_populated_playlist(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    remove_params: dict[str, Any] = {**params}
    remove_params["action"] = "remove"
    remove_params["index"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(remove_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_get()
    response.remove(0)

    assert response.playlist == []


@responses.activate
def test_jukebox_add_with_populated_playlist(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    add_params: dict[str, Any] = {**params}
    add_params["action"] = "add"
    add_params["id"] = song["id"]
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(add_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_get()
    response.add("secondSongId")

    assert response.playlist[1].id == "secondSongId"


@responses.activate
def test_jukebox_set(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    add_params: dict[str, Any] = {**params}
    add_params["action"] = "set"
    add_params["id"] = song["id"]
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(add_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_get()
    response.set("secondSongId")

    assert response.playlist[0].id == "secondSongId"


@responses.activate
def test_jukebox_remove_without_populated_playlist(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    remove_params: dict[str, Any] = {**params}
    remove_params["action"] = "remove"
    remove_params["index"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(remove_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_get()
    response.remove(0)

    assert response.playlist == []


@responses.activate
def test_jukebox_add_without_populated_playlist(
    subsonic: Subsonic,
    params: dict[str, str | int | float],
    song: dict[str, Any],
    jukebox_status_response: dict[str, Any],
    jukebox_playlist_response: dict[str, Any],
) -> None:
    status_params: dict[str, Any] = {**params}
    status_params["action"] = "status"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(status_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    get_params: dict[str, Any] = {**params}
    get_params["action"] = "get"
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(get_params, strict_match=False)],
        json=jukebox_playlist_response,
        status=200,
    )

    add_params: dict[str, Any] = {**params}
    add_params["action"] = "add"
    add_params["id"] = song["id"]
    responses.add(
        responses.GET,
        url="https://example.com/rest/jukebox",
        match=[matchers.query_param_matcher(add_params, strict_match=False)],
        json=jukebox_status_response,
        status=200,
    )

    #!TYPES
    response = subsonic.jukebox_status()
    response.add("secondSongId")

    assert response.playlist[1].id == "secondSongId"
