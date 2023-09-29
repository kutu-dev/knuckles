import knuckles
import pytest
from knuckles.subsonic import Subsonic


@pytest.fixture
def username() -> str:
    return "user"


@pytest.fixture
def password() -> str:
    return "password"


@pytest.fixture
def client() -> str:
    return "client"


@pytest.fixture
def base_url() -> str:
    return "https://example.com"


@pytest.fixture
def subsonic(base_url: str, username: str, password: str, client: str) -> Subsonic:
    return knuckles.Subsonic(
        url=base_url,
        user=username,
        password=password,
        client=client,
    )


@pytest.fixture
def params(username: str, client: str) -> dict[str, str]:
    return {
        "u": username,
        "v": "1.16.1",
        "c": client,
        "f": "json",
    }
