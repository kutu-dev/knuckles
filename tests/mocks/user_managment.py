from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def user(username: str) -> dict[str, Any]:
    return {
        "username": username,
        "email": f"{username}@example.com",
        "scrobblingEnabled": True,
        "adminRole": False,
        "settingsRole": False,
        "downloadRole": True,
        "uploadRole": False,
        "playlistRole": False,
        "coverArtRole": False,
        "commentRole": False,
        "podcastRole": False,
        "streamRole": True,
        "jukeboxRole": False,
        "shareRole": True,
        "videoConversionRole": False,
    }


@pytest.fixture
def mock_get_user(
    mock_generator: MockGenerator, username: str, user: dict[str, Any]
) -> Response:
    return mock_generator("getUser", {"username": username}, {"user": user})


@pytest.fixture
def mock_get_users(mock_generator: MockGenerator, user: dict[str, Any]) -> Response:
    return mock_generator("getUsers", {}, {"users": {"user": [user]}})


@pytest.fixture
def mock_create_user(mock_generator: MockGenerator, user: dict[str, Any]) -> Response:
    return mock_generator("createUser", {**user})


@pytest.fixture
def mock_update_user(mock_generator: MockGenerator, user: dict[str, Any]) -> Response:
    return mock_generator("updateUser", {**user})


@pytest.fixture
def mock_delete_user(mock_generator: MockGenerator, username: str) -> Response:
    return mock_generator("deleteUser", {"username": username})


@pytest.fixture
def mock_change_password(
    mock_generator: MockGenerator, username: str, password: str
) -> Response:
    return mock_generator(
        "changePassword", {"username": username, "password": password}
    )
