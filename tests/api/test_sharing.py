from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_shares(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_get_shares)

    response = subsonic.sharing.get_shares()

    assert response[0].id == share["id"]


@responses.activate
def test_get_share(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_shares: list[Response],
    share: dict[str, Any],
    song: dict[str, Any],
    username: str,
) -> None:
    add_responses(mock_get_shares)

    response = subsonic.sharing.get_share(share["id"])

    assert response.id == share["id"]
    assert response.url == share["url"]
    assert response.description == share["description"]
    assert response.user.username == username
    assert response.created == parser.parse(share["created"])
    assert response.expires == parser.parse(share["expires"])
    assert response.last_visited == parser.parse(share["lastVisited"])
    assert response.visit_count == share["visitCount"]
    assert isinstance(response.songs, list)
    assert response.songs[0].title == song["title"]


@responses.activate
def test_create_share(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_create_share: list[Response],
    share: dict[str, Any],
    song: dict[str, Any],
) -> None:
    add_responses(mock_create_share)

    response = subsonic.sharing.create_share(
        [song["id"]], share["description"], parser.parse(share["expires"])
    )

    assert response.id == share["id"]


@responses.activate
def test_update_share(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_update_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_update_share)

    response = subsonic.sharing.update_share(
        share["id"], share["description"], parser.parse(share["expires"])
    )

    assert response.id == share["id"]


@responses.activate
def test_delete_share(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_share: list[Response],
    share: dict[str, Any],
) -> None:
    add_responses(mock_delete_share)

    response = subsonic.sharing.delete_share(share["id"])

    assert isinstance(response, Subsonic)
