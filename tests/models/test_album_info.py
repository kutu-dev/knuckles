from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_album_info: Response,
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    responses.add(mock_get_album_info)

    response = subsonic.browsing.get_album_info(album["id"])
    response.notes = ""
    response = response.generate()

    assert response.notes == album_info["notes"]
