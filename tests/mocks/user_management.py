from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def user(username: str) -> dict[str, Any]:
    return {
        "username": username,
        "password": "password",
        "email": f"{username}@example.com",
        "ldapAuthenticated": False,
        "adminRole": False,
        "settingsRole": False,
        "streamRole": True,
        "jukeboxRole": False,
        "downloadRole": True,
        "uploadRole": False,
        "playlistRole": False,
        "coverArtRole": False,
        "commentRole": False,
        "podcastRole": False,
        "shareRole": True,
        "videoConversionRole": False,
        "musicFolderId": ["0", "1"],
        "maxBitRate": 0,
    }


@pytest.fixture
def mock_get_user(
    mock_generator: MockGenerator, username: str, user: dict[str, Any]
) -> list[Response]:
    return mock_generator("getUser", {"username": username}, {"user": user})


@pytest.fixture
def mock_get_users(
    mock_generator: MockGenerator, user: dict[str, Any]
) -> list[Response]:
    return mock_generator("getUsers", {}, {"users": {"user": [user]}})


@pytest.fixture
def mock_create_user(
    mock_generator: MockGenerator, user: dict[str, Any]
) -> list[Response]:
    return mock_generator("createUser", {**user})


@pytest.fixture
def mock_update_user(
    mock_generator: MockGenerator, user: dict[str, Any]
) -> list[Response]:
    return mock_generator("updateUser", {**user})


@pytest.fixture
def mock_delete_user(mock_generator: MockGenerator, username: str) -> list[Response]:
    return mock_generator("deleteUser", {"username": username})


@pytest.fixture
def new_password() -> str:
    return "MoreSecureThanPHP"


@pytest.fixture
def mock_change_password(
    mock_generator: MockGenerator, username: str, new_password: str
) -> list[Response]:
    return mock_generator(
        "changePassword", {"username": username, "password": new_password}
    )
