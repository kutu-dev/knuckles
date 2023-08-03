from typing import Any

import pytest
from dateutil import parser
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def share(song: dict[str, Any], username: str) -> dict[str, Any]:
    return {
        "id": "12",
        "url": "http://example.com/share/1",
        "description": "Forget and Remember (Comfort Fit)",
        "username": username,
        "created": "2020-04-16T04:12:09+00:00",
        "expires": "2024-05-21T04:13:10+00:00",
        "lastVisited": "2023-03-17T04:10:09+00:00",
        "visitCount": 0,
        "entry": [song],
    }


@pytest.fixture
def mock_get_shares(mock_generator: MockGenerator, share: dict[str, Any]) -> Response:
    return mock_generator("getShares", {}, {"shares": {"share": [share]}})


@pytest.fixture
def mock_create_share(
    mock_generator: MockGenerator, share: dict[str, Any], song: dict[str, Any]
) -> Response:
    return mock_generator(
        "createShare",
        {
            "id": song["id"],
            "description": share["description"],
            "expires": parser.parse(share["expires"]).timestamp() * 1000,
        },
        {"shares": {"share": [share]}},
    )


@pytest.fixture
def mock_update_share(mock_generator: MockGenerator, share: dict[str, Any]) -> Response:
    return mock_generator(
        "updateShare",
        {
            "id": share["id"],
            "description": share["description"],
            "expires": parser.parse(share["expires"]).timestamp() * 1000,
        },
    )


@pytest.fixture
def mock_delete_share(mock_generator: MockGenerator, share: dict[str, Any]) -> Response:
    return mock_generator("deleteShare", {"id": share["id"]})
