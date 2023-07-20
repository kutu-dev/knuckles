from knuckles import Subsonic, SubsonicResponse, Song, License
from datetime import datetime
from pathlib import Path
import knuckles
import pytest


SUBSONIC_URL = "http://demo.navidrome.org"
USER = "demo"
PASSWORD = "demo"
SONG_ID = "44942f3661c50b698f7b6ee595f390d8"
SONG_TITLE = "A Fine Way To Start"


@pytest.fixture(scope="session")
def subsonic() -> Subsonic:
    return knuckles.Subsonic(
        url=SUBSONIC_URL, user=USER, password=PASSWORD, client="KnucklesTests"
    )


def test_successful_ping(subsonic: Subsonic) -> None:
    response: SubsonicResponse = subsonic.ping()

    assert bool(response) == True
    assert response.status == "ok"
    assert response.version is not None
    assert response.type == "navidrome"
    assert response.server_version is not None
    assert response.open_subsonic == False


def test_unsuccessful_ping(subsonic: Subsonic) -> None:
    # Temporally change to an invalid user to test error response
    old_user: str = subsonic.user
    subsonic.user = "foo"

    with pytest.raises(
        knuckles.exceptions.CodeError40, match="Wrong username or password.?"
    ):
        subsonic.ping()

    subsonic.user = old_user


def test_get_license(subsonic: Subsonic):
    response: License = subsonic.get_license()

    assert bool(response) == True
    assert response.valid == True
    assert response.email == None
    assert response.license_expires == None
    assert response.trial_expires == None


def test_ping_without_token_auth(subsonic: Subsonic):
    # Temporally disable the authentication by token
    subsonic.use_token = False
    assert subsonic.ping()
    subsonic.use_token = True


def test_get_song(subsonic: Subsonic):
    response: Song = subsonic.get_song(SONG_ID)

    assert response.id == SONG_ID
    assert response.is_dir == False
    assert response.title == SONG_TITLE
    assert response.album_id == "6f041d520b69baa75166ad9b6ca5de4a"
    assert response.album_id == response.album.id
    assert response.album_name == "Red Eyes"
    assert response.album_name == response.album.name
    assert response.artist_id == "637e3b2295ab6d551afa4074ef1f7fae"
    assert response.artist_id == response.artist.id
    assert response.artist_name == "Carter Vail"
    assert response.artist_name == response.artist.name
    assert response.track == 1
    assert response.year == 2020
    assert response.genre is None
    assert response.cover_art.id == "mf-44942f3661c50b698f7b6ee595f390d8_640a9288"
    assert response.size == 2220457
    assert response.content_type == "audio/mpeg"
    assert response.suffix == "mp3"
    assert response.transcoded_content_type is None
    assert response.transcoded_suffix is None
    assert response.duration == 74
    assert response.bit_rate == 185
    assert type(response.path) is not None
    assert response.user_rating == 5
    assert response.average_rating is None
    assert response.play_count == 40
    assert response.disc_number == 1
    assert type(response.created) is datetime
    assert type(response.starred) is datetime
    assert response.type == "music"
    assert response.bookmark_position is None
    assert type(response.played) is datetime


def test_song_generate(subsonic: Subsonic):
    song: Song = subsonic.get_song(SONG_ID)
    song.title = "Foo"
    song = song.generate(subsonic)()

    assert song.title == SONG_TITLE
