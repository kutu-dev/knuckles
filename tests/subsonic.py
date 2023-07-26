import knuckles
import pytest
from knuckles.subsonic import Subsonic


@pytest.fixture
def user() -> str:
    return "user"


@pytest.fixture
def password() -> str:
    return "password"


@pytest.fixture
def client() -> str:
    return "client"


@pytest.fixture
def subsonic(user: str, password: str, client: str) -> Subsonic:
    return knuckles.Subsonic(
        url="http://example.com",
        user=user,
        password=password,
        client=client,
    )


@pytest.fixture
def params(user: str, client: str) -> dict[str, str]:
    return {
        "u": user,
        "v": "1.16.1",
        "c": client,
        "f": "json",
    }
