from typing import Any

import pytest
import responses
from responses import Response

from knuckles import Subsonic
from knuckles.exceptions import ResourceNotFound
from knuckles.models.genre import Genre


@responses.activate
def test_generate(
    subsonic: Subsonic, mock_get_genres: Response, genre: dict[str, Any]
) -> None:
    responses.add(mock_get_genres)

    response = subsonic.browsing.get_genre(genre["value"])
    response.song_count = 20
    response = response.generate()

    assert response.song_count == genre["songCount"]


@responses.activate
def test_generate_nonexistent_genre(
    subsonic: Subsonic, mock_get_genres: Response, genre: dict[str, Any]
) -> None:
    responses.add(mock_get_genres)

    nonexistent_genre = Genre(subsonic, "Foo")

    with pytest.raises(
        ResourceNotFound,
        match="Unable to generate gender as it does not exist in the server",
    ):
        nonexistent_genre.generate()
