from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def mock_ping(mock_generator: MockGenerator) -> list[Response]:
    return mock_generator("ping")


@pytest.fixture
def license() -> dict[str, Any]:
    return {
        "valid": True,
        "email": "user@example.com",
        "licenseExpires": "2017-04-11T10:42:50.842Z",
        "trialExpires": "2015-03-11T12:36:38.753Z",
    }


@pytest.fixture
def mock_get_license(
    mock_generator: MockGenerator, license: dict[str, Any]
) -> list[Response]:
    return mock_generator("getLicense", {}, {"license": license})


@pytest.fixture
def mock_auth_without_token(
    mock_generator: MockGenerator, password: str
) -> list[Response]:
    return mock_generator("ping", {"p": password})


@pytest.fixture
def open_subsonic_extension_name() -> str:
    return "extensionName"


@pytest.fixture
def open_subsonic_extension_versions() -> list[int]:
    return [1, 2]


@pytest.fixture
def open_subsonic_extensions(
    open_subsonic_extension_name: str, open_subsonic_extension_versions: list[int]
) -> dict[str, Any]:
    return {open_subsonic_extension_name: open_subsonic_extension_versions}


@pytest.fixture
def mock_get_open_subsonic_extensions(
    mock_generator: MockGenerator, open_subsonic_extensions: dict[str, Any]
) -> list[Response]:
    return mock_generator(
        "getOpenSubsonicExtensions",
        {},
        {"openSubsonicExtensions": open_subsonic_extensions},
    )
