from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import ResourceNotFound, ShareInvalidSongList
from knuckles.models.share import Share
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)

    response = subsonic.sharing.get_share(share["id"])
    response.description = "Foo"
    response = response.generate()

    assert response.description == share["description"]


@responses.activate
def test_generate_nonexistent_genre(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
) -> None:
    add_responses(mock_get_shares)

    nonexistent_share = Share(subsonic, "Foo")

    with pytest.raises(
        ResourceNotFound,
        match="Unable to generate share as it does not exist in the server",
    ):
        nonexistent_share.generate()


@responses.activate
def test_create(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    mock_create_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)
    add_responses(mock_create_share)

    response = subsonic.sharing.get_share(share["id"])
    response = response.create()

    assert type(response) is Share


@responses.activate
def test_create_none_song_list(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    mock_create_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)
    add_responses(mock_create_share)

    response = subsonic.sharing.get_share(share["id"])
    response.songs = None

    with pytest.raises(
        ShareInvalidSongList,
        match=(
            "A list with at least one song model object in the songs parameter"
            + "is necessary to create a share"
        ),
    ):
        response.create()


@responses.activate
def test_create_empty_song_list(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    mock_create_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)
    add_responses(mock_create_share)

    response = subsonic.sharing.get_share(share["id"])
    response.songs = []

    with pytest.raises(
        ShareInvalidSongList,
        match=(
            "A list with at least one song model object in the songs parameter"
            + "is necessary to create a share"
        ),
    ):
        response.create()


@responses.activate
def test_update(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    mock_update_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)
    add_responses(mock_update_share)

    response = subsonic.sharing.get_share(share["id"])
    response.update()

    assert type(response) is Share


@responses.activate
def test_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    mock_delete_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)
    add_responses(mock_delete_share)

    response = subsonic.sharing.get_share(share["id"])
    response.delete()

    assert type(response) is Share
