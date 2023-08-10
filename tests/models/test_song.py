from datetime import datetime
from typing import Any

import pytest
import responses
from responses import Response

from knuckles import Song, Subsonic
from tests.conftest import MockGenerator


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_song: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)

    requested_song = subsonic.browsing.get_song(song["id"])
    requested_song.title = "Foo"
    requested_song = requested_song.generate()

    assert requested_song.title == song["title"]


@responses.activate
def test_song_star(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_star_song: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_star_song)

    requested_song = subsonic.browsing.get_song(song["id"])

    assert type(requested_song.star()) is Song


@responses.activate
def test_song_unstar(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_unstar_song: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_unstar_song)

    requested_song: Song = subsonic.browsing.get_song(song["id"])

    assert type(requested_song.unstar()) is Song


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

    requested_song: Song = subsonic.browsing.get_song(song["id"])

    assert type(requested_song.set_rating(rating)) is Song


@responses.activate
def test_song_remove_rating(
    subsonic: Subsonic,
    mock_get_song: Response,
    mock_set_rating_zero: Response,
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_song)
    responses.add(mock_set_rating_zero)

    requested_song: Song = subsonic.browsing.get_song(song["id"])

    assert type(requested_song.remove_rating()) is Song


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

    requested_song: Song = subsonic.browsing.get_song(song["id"])
    datetime_time: datetime = datetime.fromtimestamp(scrobble_time / 1000)

    scrobble_response: Song = requested_song.scrobble(datetime_time)

    assert type(scrobble_response) is Song


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

    requested_song: Song = subsonic.browsing.get_song(song["id"])
    datetime_time: datetime = datetime.fromtimestamp(scrobble_time / 1000)

    scrobble_response: Song = requested_song.scrobble(datetime_time, True)

    assert type(scrobble_response) is Song


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

    requested_song: Song = subsonic.browsing.get_song(song["id"])
    datetime_time: datetime = datetime.fromtimestamp(scrobble_time / 1000)

    scrobble_response: Song = requested_song.scrobble(datetime_time, False)

    assert type(scrobble_response) is Song
