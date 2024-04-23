from datetime import datetime
from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import InvalidRatingNumber
from responses import Response

from tests.conftest import AddResponses, MockGenerator


@responses.activate
def test_star_song(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_star_song: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_star_song)

    response = subsonic.media_annotation.star_song(song["id"])

    assert type(response) is Subsonic


@responses.activate
def test_star_album(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_star_album: list[Response],
    album: dict[str, Any],
) -> None:
    add_responses(mock_star_album)

    response = subsonic.media_annotation.star_album(album["id"])

    assert type(response) is Subsonic


@responses.activate
def test_star_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_star_artist: list[Response],
    artist: dict[str, Any],
) -> None:
    add_responses(mock_star_artist)

    response = subsonic.media_annotation.star_artist(artist["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_song(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_unstar_song: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_unstar_song)

    response = subsonic.media_annotation.unstar_song(song["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_album(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_unstar_album: list[Response],
    album: dict[str, Any],
) -> None:
    add_responses(mock_unstar_album)

    response = subsonic.media_annotation.unstar_album(album["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_unstar_artist: list[Response],
    artist: dict[str, Any],
) -> None:
    add_responses(mock_unstar_artist)

    response = subsonic.media_annotation.unstar_artist(artist["id"])

    assert type(response) is Subsonic


@pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
@responses.activate
def test_set_rating(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_generator: MockGenerator,
    song: dict[str, Any],
    rating: int,
) -> None:
    add_responses(mock_generator("setRating", {"id": song["id"], "rating": rating}))

    response = subsonic.media_annotation.set_rating(song["id"], rating)

    assert type(response) is Subsonic


@responses.activate
def test_remove_rating(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_set_rating_zero: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_set_rating_zero)

    response = subsonic.media_annotation.remove_rating(song["id"])

    assert type(response) is Subsonic


@pytest.mark.parametrize("rating", [-1, 0, 6])
@responses.activate
def test_set_invalid_rating(
    add_responses: AddResponses,
    subsonic: Subsonic,
    song: dict[str, Any],
    rating: int,
) -> None:
    with pytest.raises(
        InvalidRatingNumber,
        match=(
            "Invalid rating number, "
            + r"only numbers between 1 and 5 \(inclusive\) are allowed"
        ),
    ):
        subsonic.media_annotation.set_rating(song["id"], rating)


@responses.activate
def test_default_scrobble(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_scrobble_submission: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_scrobble_submission)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(1678935707000 / 1000)],
    )

    assert type(response) is Subsonic


@responses.activate
def test_submission_scrobble(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_scrobble_submission: list[Response],
    song: dict[str, Any],
    scrobble_time: int,
) -> None:
    add_responses(mock_scrobble_submission)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(scrobble_time / 1000)],
        True,
    )

    assert type(response) is Subsonic


@responses.activate
def test_now_playing_scrobble(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_scrobble_now_playing: list[Response],
    song: dict[str, Any],
    scrobble_time: int,
) -> None:
    add_responses(mock_scrobble_now_playing)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(scrobble_time / 1000)],
        False,
    )

    assert type(response) is Subsonic
