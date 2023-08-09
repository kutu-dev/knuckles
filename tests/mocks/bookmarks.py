from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def bookmark(song: dict[str, Any], username: str) -> dict[str, Any]:
    return {
        "entry": song,
        "position": 129000,
        "username": username,
        "comment": "Test comment",
        "created": "2023-03-13T16:30:35Z",
        "changed": "2023-03-13T16:30:35Z",
    }


@pytest.fixture
def mock_get_bookmarks(
    mock_generator: MockGenerator, bookmark: dict[str, Any]
) -> Response:
    return mock_generator("getBookmarks", {}, {"bookmarks": {"bookmark": [bookmark]}})


@pytest.fixture
def mock_create_bookmark(
    mock_generator: MockGenerator, song: dict[str, Any], bookmark: dict[str, Any]
) -> Response:
    return mock_generator(
        "createBookmark",
        {
            "id": song["id"],
            "position": bookmark["position"],
            "comment": bookmark["comment"],
        },
    )


@pytest.fixture
def mock_delete_bookmark(
    mock_generator: MockGenerator, song: dict[str, Any], bookmark: dict[str, Any]
) -> Response:
    return mock_generator("deleteBookmark", {"id": song["id"]})
