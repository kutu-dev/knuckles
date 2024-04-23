from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_video_info: list[Response],
    video: dict[str, Any],
    video_info: dict[str, Any],
) -> None:
    add_responses(mock_get_video_info)

    response = subsonic.browsing.get_video_info(video["id"])
    response.id = ""
    response = response.generate()

    assert response.id == video_info["id"]
