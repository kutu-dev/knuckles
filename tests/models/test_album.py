from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_album: Response,
    mock_get_album_info: Response,
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    responses.add(mock_get_album)
    responses.add(mock_get_album_info)

    response = subsonic.browsing.get_album(album["id"])
    response.title = "Foo"
    response = response.generate()

    assert response.title == album["title"]
    assert response.info.notes == album_info["notes"]


@responses.activate
def test_get_album_info(
    subsonic: Subsonic,
    mock_get_album: Response,
    mock_get_album_info: Response,
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    responses.add(mock_get_album)
    responses.add(mock_get_album_info)

    response = subsonic.browsing.get_album(album["id"])
    get_album_info = response.get_album_info()

    assert get_album_info.notes == album_info["notes"]
    assert response.info.notes == album_info["notes"]
