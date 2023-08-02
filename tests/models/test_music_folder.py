from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_music_folders: Response,
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_get_music_folders)

    requested_folder = subsonic.browsing.get_music_folders()[0]
    requested_folder.name = "Foo"
    requested_folder = requested_folder.generate()

    assert requested_folder.name == music_folders[0]["name"]
