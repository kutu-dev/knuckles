from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_artist_info: Response,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    responses.add(mock_get_artist_info)

    response = subsonic.browsing.get_artist_info(artist["id"])
    response.biography = ""
    response = response.generate()

    assert response.biography == artist_info["biography"]
