from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import ShareInvalidSongList
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_shares: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.description = "Foo"
    requested_share = requested_share.generate()

    assert requested_share.description == share["description"]


@responses.activate
def test_create(
    subsonic: Subsonic,
    mock_get_shares: Response,
    mock_create_share: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)
    responses.add(mock_create_share)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.create()

    assert True is False
    # assert type(requested_share) ==


@responses.activate
def test_create_none_song_list(
    subsonic: Subsonic,
    mock_get_shares: Response,
    mock_create_share: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)
    responses.add(mock_create_share)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.songs = None

    with pytest.raises(
        ShareInvalidSongList,
        match=(
            "A list with at least one song model object in the songs parameter"
            + "is necessary to create a share"
        ),
    ):
        requested_share.create()


@responses.activate
def test_create_empty_song_list(
    subsonic: Subsonic,
    mock_get_shares: Response,
    mock_create_share: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)
    responses.add(mock_create_share)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.songs = []

    with pytest.raises(
        ShareInvalidSongList,
        match=(
            "A list with at least one song model object in the songs parameter"
            + "is necessary to create a share"
        ),
    ):
        requested_share.create()


@responses.activate
def test_update(
    subsonic: Subsonic,
    mock_get_shares: Response,
    mock_update_share: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)
    responses.add(mock_update_share)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.update()

    assert True is False
    # assert type(requested_share) ==


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_shares: Response,
    mock_delete_share: Response,
    share: dict[str, Any],
) -> None:
    responses.add(mock_get_shares)
    responses.add(mock_delete_share)

    requested_share = subsonic.sharing.get_share(share["id"])
    requested_share.delete()

    assert True is False
    # assert type(requested_share) ==
