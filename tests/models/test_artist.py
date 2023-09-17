from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_artist: Response,
    mock_get_artist_info: Response,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    responses.add(mock_get_artist)
    responses.add(mock_get_artist_info)

    requested_artist = subsonic.browsing.get_artist(artist["id"])
    requested_artist.name = "Foo"
    requested_artist = requested_artist.generate()

    assert requested_artist.name == artist["name"]
    assert requested_artist.info.biography == artist_info["biography"]


@responses.activate
def test_get_artist_info(
    subsonic: Subsonic,
    mock_get_artist: Response,
    mock_get_artist_info: Response,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    responses.add(mock_get_artist)
    responses.add(mock_get_artist_info)

    requested_artist = subsonic.browsing.get_artist(artist["id"])
    get_artist_info = requested_artist.get_artist_info()

    assert get_artist_info.biography == artist_info["biography"]
    assert requested_artist.info.biography == artist_info["biography"]
