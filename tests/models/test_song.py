from datetime import datetime
from typing import Any

import pytest
import responses
from knuckles import Song, Subsonic
from responses import Response

from tests.conftest import AddResponses, MockGenerator


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_song: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_song)

    response = subsonic.browsing.get_song(song["id"])
    response.title = "Foo"
    response = response.generate()

    assert response.title == song["title"]


@responses.activate
def test_song_star(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_star_song: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_star_song)

    response = subsonic.browsing.get_song(song["id"]).star()

    assert type(response) is Song


@responses.activate
def test_song_unstar(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_unstar_song: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_unstar_song)

    response: Song = subsonic.browsing.get_song(song["id"]).unstar()

    assert type(response) is Song


@pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
@responses.activate
def test_song_set_rating(
    subsonic: Subsonic,
    mock_generator: MockGenerator,
    mock_get_song: Response,
    song: dict[str, Any],
    rating: int,
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_generator("setRating", {"id": song["id"], "rating": rating}))

    response: Song = subsonic.browsing.get_song(song["id"]).set_rating(rating)

    assert type(response) is Song


@responses.activate
def test_song_remove_rating(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_set_rating_zero: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_set_rating_zero)

    response: Song = subsonic.browsing.get_song(song["id"]).remove_rating()

    assert type(response) is Song


@responses.activate
def test_song_default_scrobble(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_scrobble_submission: Response,
    scrobble_time: int,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_scrobble_submission)

    scrobble_in_datetime = datetime.fromtimestamp(scrobble_time / 1000)
    response: Song = subsonic.browsing.get_song(song["id"]).scrobble(
        scrobble_in_datetime
    )

    assert type(response) is Song


@responses.activate
def test_song_submission_scrobble(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_scrobble_submission: Response,
    scrobble_time: int,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_scrobble_submission)

    scrobble_in_datetime = datetime.fromtimestamp(scrobble_time / 1000)
    response: Song = subsonic.browsing.get_song(song["id"]).scrobble(
        scrobble_in_datetime, True
    )

    assert type(response) is Song


@responses.activate
def test_song_now_playing_scrobble(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_scrobble_now_playing: Response,
    scrobble_time: int,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_scrobble_now_playing)

    scrobble_in_datetime = datetime.fromtimestamp(scrobble_time / 1000)
    response: Song = subsonic.browsing.get_song(song["id"]).scrobble(
        scrobble_in_datetime, False
    )

    assert type(response) is Song
