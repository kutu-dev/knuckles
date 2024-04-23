from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artist_info_minimal: list[Response],
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    add_responses(mock_get_artist_info_minimal)

    response = subsonic.browsing.get_artist_info(artist["id"])
    response.biography = ""
    response = response.generate()

    assert response.biography == artist_info["biography"]
