from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_video_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_videos: list[Response],
    video: dict[str, Any],
) -> None:
    add_responses(mock_get_videos)

    response = subsonic.browsing.get_video(video["id"])

    response.suffix = ""
    response = response.generate()

    assert response.suffix == video["suffix"]


@responses.activate
def test_get_video_info(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_videos: list[Response],
    mock_get_video_info: list[Response],
    video: dict[str, Any],
    video_info: dict[str, Any],
) -> None:
    add_responses(mock_get_videos)
    add_responses(mock_get_video_info)

    response = subsonic.browsing.get_video(video["id"])
    get_video_info = response.get_video_info()

    assert get_video_info.id == video_info["id"]
    assert response.info.id == video_info["id"]
