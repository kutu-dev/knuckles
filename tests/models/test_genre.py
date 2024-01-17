from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import ResourceNotFound
from knuckles.models.genre import Genre
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_genres: list[Response],
    genre: dict[str, Any],
) -> None:
    add_responses(mock_get_genres)

    response = subsonic.browsing.get_genre(genre["value"])
    response.song_count = 20
    response = response.generate()

    assert response.song_count == genre["songCount"]


@responses.activate
def test_generate_nonexistent_genre(
    add_responses: AddResponses, subsonic: Subsonic, mock_get_genres: list[Response]
) -> None:
    add_responses(mock_get_genres)

    nonexistent_genre = Genre(subsonic, "Foo")

    with pytest.raises(
        ResourceNotFound,
        match="Unable to generate genre as it does not exist in the server",
    ):
        nonexistent_genre.generate()
