from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_music_folders: list[Response],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_music_folders)

    response = subsonic.browsing.get_music_folders()[0]
    response.name = "Foo"
    response = response.generate()

    assert response.name == music_folders[0]["name"]
