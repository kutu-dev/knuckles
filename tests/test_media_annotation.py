from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import InvalidRatingNumber
from responses import matchers


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


@pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
@responses.activate
def test_set_rating(
    subsonic: Subsonic,
    params: dict[str, str | int],
    subsonic_response: dict[str, Any],
    song: dict[str, Any],
    rating: int,
) -> None:
    params["id"] = song["id"]
    params["rating"] = rating
    responses.add(
        responses.GET,
        url="https://example.com/rest/setRating",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.set_rating(song["id"], rating)

    assert type(response) is Subsonic


@responses.activate
def test_remove_rating(
    subsonic: Subsonic,
    params: dict[str, str | int],
    subsonic_response: dict[str, Any],
    song: dict[str, Any],
) -> None:
    params["id"] = song["id"]
    params["rating"] = 0
    responses.add(
        responses.GET,
        url="https://example.com/rest/setRating",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Subsonic = subsonic.remove_rating(song["id"])

    assert type(response) is Subsonic


@pytest.mark.parametrize("rating", [-1, 0, 6])
@responses.activate
def test_set_invalid_rating(
    subsonic: Subsonic,
    params: dict[str, str | int],
    subsonic_response: dict[str, Any],
    song: dict[str, Any],
    rating: int,
) -> None:
    params["id"] = song["id"]
    params["rating"] = rating
    responses.add(
        responses.GET,
        url="https://example.com/rest/setRating",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    with pytest.raises(
        InvalidRatingNumber,
        match=(
            "Invalid rating number, "
            + "only numbers between 1 and 5 \(inclusive\) are allowed"
        ),
    ):
        subsonic.set_rating(song["id"], rating)
