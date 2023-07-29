from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


def test_generate(
    subsonic: Subsonic, mock_get_genres: Response, genre: dict[str, Any]
) -> None:
    responses.add(mock_get_genres)

    response = subsonic.browsing.get_genre(genre["value"])
    response.value = "Foo"
    response = response.generate()

    assert response.value == genre["value"]
