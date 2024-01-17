from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artist: list[Response],
    mock_get_artist_info: list[Response],
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    add_responses(mock_get_artist)
    add_responses(mock_get_artist_info)

    response = subsonic.browsing.get_artist(artist["id"])
    response.name = "Foo"
    response = response.generate()

    assert response.name == artist["name"]
    assert response.info.biography == artist_info["biography"]


@responses.activate
def test_get_artist_info(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artist: list[Response],
    mock_get_artist_info: list[Response],
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    add_responses(mock_get_artist)
    add_responses(mock_get_artist_info)

    response = subsonic.browsing.get_artist(artist["id"])
    get_artist_info = response.get_artist_info()

    assert get_artist_info.biography == artist_info["biography"]
    assert response.info.biography == artist_info["biography"]
