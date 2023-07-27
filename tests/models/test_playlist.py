from typing import Any

import responses
from responses import Response

from knuckles import Subsonic


def test_playlist_generate(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)

    response = subsonic.playlist.get(playlist["id"])
    response.name = "Foo"
    response = response.generate()

    # assert type(response) ==
    assert response.name == playlist["name"]


def test_playlist_create(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_create_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_create_playlist)

    response = subsonic.playlist.get(playlist["id"])
    response = response.create()

    # assert type(response) ==


def test_playlist_update(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_update_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_update_playlist)

    response = subsonic.playlist.get(playlist["id"])
    response = response.update()

    # assert type(response) ==


def test_playlist_delete(
    subsonic: Subsonic,
    mock_get_playlist: Response,
    mock_delete_playlist: Response,
    playlist: dict[str, Any],
) -> None:
    responses.add(mock_get_playlist)
    responses.add(mock_delete_playlist)

    response = subsonic.playlist.get(playlist["id"])
    response = response.delete()

    # assert type(response) ==
