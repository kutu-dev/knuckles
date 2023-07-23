from typing import Any

import responses
from responses import matchers

from knuckles import Subsonic


@responses.activate
def test_star_song(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["id"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/star",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.star_song("testId")

    assert type(response) is Subsonic


@responses.activate
def test_star_album(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["albumId"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/star",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.star_album("testId")

    assert type(response) is Subsonic


@responses.activate
def test_star_artist(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["artistId"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/star",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.star_artist("testId")

    assert type(response) is Subsonic


@responses.activate
def test_unstar_song(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["id"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/unstar",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.unstar_song("testId")

    assert type(response) is Subsonic


@responses.activate
def test_unstar_album(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["albumId"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/unstar",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.unstar_album("testId")

    assert type(response) is Subsonic


@responses.activate
def test_unstar_artist(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
) -> None:
    params["artistId"] = "testId"
    responses.add(
        responses.GET,
        url="https://example.com/rest/unstar",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.unstar_artist("testId")

    assert type(response) is Subsonic
