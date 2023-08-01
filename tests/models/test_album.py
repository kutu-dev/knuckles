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

    requested_album = subsonic.browsing.get_album(album["id"])
    requested_album.title = "Foo"
    requested_album = requested_album.generate()

    assert requested_album.title == album["title"]
    assert requested_album.info.notes == album_info["notes"]


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

    requested_album = subsonic.browsing.get_album(album["id"])
    get_album_info = requested_album.get_album_info()

    assert get_album_info.notes == album_info["notes"]
    assert requested_album.info.notes == album_info["notes"]
