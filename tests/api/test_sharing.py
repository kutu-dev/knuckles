from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_get_shares(
    subsonic: Subsonic,
    mock_get_shares: Response,
    share: dict[str, Any],
    song: dict[str, Any],
    username: str,
) -> None:
    responses.add(mock_get_shares)

    response = subsonic.sharing.get_shares()

    assert response[0].id == share["id"]
    assert response[0].url == share["url"]
    assert response[0].description == share["description"]
    assert response[0].username == username
    assert response[0].created == parser.parse(share["created"])
    assert response[0].expires == parser.parse(share["expires"])
    assert response[0].last_visited == share["lastVisited"]
    assert response[0].visit_count == share["visitCount"]
    assert response[0].songs[0].title == song["title"]


@responses.activate
def test_create_share(
    subsonic: Subsonic,
    mock_create_share: Response,
    share: dict[str, Any],
    song: dict[str, Any],
) -> None:
    responses.add(mock_create_share)

    response = subsonic.sharing.create_share(
        [song["id"]], share["description"], parser.parse(share["expires"])
    )

    assert response.id == share["id"]


@responses.activate
def test_update_share(
    subsonic: Subsonic, mock_update_share: Response, share: dict[str, Any]
) -> None:
    responses.add(mock_update_share)

    response = subsonic.sharing.update_share(
        share["id"], share["description"], parser.parse(share["expires"])
    )

    assert response.id == share["id"]


@responses.activate
def test_delete_share(
    subsonic: Subsonic, mock_delete_share: Response, share: dict[str, Any]
) -> None:
    responses.add(mock_delete_share)

    response = subsonic.sharing.delete_share(share["id"])

    assert type(response) == Subsonic
