from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_artist: Response,
    artist: dict[str, Any],
) -> None:
    responses.add(mock_get_artist)

    requested_artist = subsonic.browsing.get_artist(artist["id"])
    requested_artist.name = "Foo"
    requested_artist = requested_artist.generate()

    assert requested_artist.name == artist["name"]
