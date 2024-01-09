from datetime import datetime
from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import InvalidRatingNumber
from responses import Response

from tests.conftest import MockGenerator


@responses.activate
def test_star_song(
    subsonic: Subsonic, mock_star_song: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_star_song)

    response = subsonic.media_annotation.star_song(song["id"])

    assert type(response) is Subsonic


@responses.activate
def test_star_album(
    subsonic: Subsonic, mock_star_album: Response, album: dict[str, Any]
) -> None:
    responses.add(mock_star_album)

    response = subsonic.media_annotation.star_album(album["id"])

    assert type(response) is Subsonic


@responses.activate
def test_star_artist(
    subsonic: Subsonic, mock_star_artist: Response, artist: dict[str, Any]
) -> None:
    responses.add(mock_star_artist)

    response = subsonic.media_annotation.star_artist(artist["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_song(
    subsonic: Subsonic, mock_unstar_song: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_unstar_song)

    response = subsonic.media_annotation.unstar_song(song["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_album(
    subsonic: Subsonic, mock_unstar_album: Response, album: dict[str, Any]
) -> None:
    responses.add(mock_unstar_album)

    response = subsonic.media_annotation.unstar_album(album["id"])

    assert type(response) is Subsonic


@responses.activate
def test_unstar_artist(
    subsonic: Subsonic, mock_unstar_artist: Response, artist: dict[str, Any]
) -> None:
    responses.add(mock_unstar_artist)

    response = subsonic.media_annotation.unstar_artist(artist["id"])

    assert type(response) is Subsonic


@pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
@responses.activate
def test_set_rating(
    subsonic: Subsonic,
    mock_generator: MockGenerator,
    song: dict[str, Any],
    rating: int,
) -> None:
    responses.add(mock_generator("setRating", {"id": song["id"], "rating": rating}))

    response = subsonic.media_annotation.set_rating(song["id"], rating)

    assert type(response) is Subsonic


@responses.activate
def test_remove_rating(
    subsonic: Subsonic,
    mock_set_rating_zero: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_set_rating_zero)

    response = subsonic.media_annotation.remove_rating(song["id"])

    assert type(response) is Subsonic


@pytest.mark.parametrize("rating", [-1, 0, 6])
@responses.activate
def test_set_invalid_rating(
    subsonic: Subsonic,
    song: dict[str, Any],
    rating: int,
) -> None:
    with pytest.raises(
        InvalidRatingNumber,
        match=(
            "Invalid rating number, "
            + "only numbers between 1 and 5 \(inclusive\) are allowed"
        ),
    ):
        subsonic.media_annotation.set_rating(song["id"], rating)


@responses.activate
def test_default_scrobble(
    subsonic: Subsonic,
    mock_scrobble_submission: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_scrobble_submission)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(1678935707000 / 1000)],
    )

    assert type(response) is Subsonic


@responses.activate
def test_submission_scrobble(
    subsonic: Subsonic,
    mock_scrobble_submission: Response,
    song: dict[str, Any],
    scrobble_time: int,
) -> None:
    responses.add(mock_scrobble_submission)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(scrobble_time / 1000)],
        True,
    )

    assert type(response) is Subsonic


@responses.activate
def test_now_playing_scrobble(
    subsonic: Subsonic,
    mock_scrobble_now_playing: Response,
    song: dict[str, Any],
    scrobble_time: int,
) -> None:
    responses.add(mock_scrobble_now_playing)

    response = subsonic.media_annotation.scrobble(
        [song["id"]],
        # Divide by 1000 because messages are saved in milliseconds instead of seconds
        [datetime.fromtimestamp(scrobble_time / 1000)],
        False,
    )

    assert type(response) is Subsonic
