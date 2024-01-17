from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_info: list[Response],
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    add_responses(mock_get_album_info)

    response = subsonic.browsing.get_album_info(album["id"])
    response.notes = ""
    response = response.generate()

    assert response.notes == album_info["notes"]
