from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic, __version__
from responses import Response
from importlib.metadata import version
from tests.conftest import AddResponses


def test_version() -> None:
    assert __version__ == version("knuckles")


@responses.activate
def test_ping(
    add_responses: AddResponses,
    subsonic: Subsonic,
    subsonic_response: dict[str, Any],
    mock_ping: list[Response],
) -> None:
    add_responses(mock_ping)
    response = subsonic.system.ping()

    assert bool(response) is True
    assert response.status == subsonic_response["status"]
    assert response.version == subsonic_response["version"]
    assert response.type == subsonic_response["type"]
    assert response.server_version == subsonic_response["serverVersion"]
    assert response.open_subsonic == subsonic_response["openSubsonic"]


@responses.activate
def test_get_license(
    add_responses: AddResponses,
    subsonic: Subsonic,
    license: dict[str, Any],
    mock_get_license: list[Response],
) -> None:
    add_responses(mock_get_license)
    response = subsonic.system.get_license()

    assert bool(response) is True
    assert response.valid is license["valid"]
    assert response.email == license["email"]
    assert response.license_expires == parser.parse(license["licenseExpires"])
    assert response.trial_expires == parser.parse(license["trialExpires"])


@responses.activate
def test_auth_without_token(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_auth_without_token: list[Response],
) -> None:
    add_responses(mock_auth_without_token)
    subsonic.api.use_token = False
    assert subsonic.system.ping().status == "ok"


@responses.activate
def test_get_open_subsonic_extensions(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_open_subsonic_extensions: list[Response],
    open_subsonic_extension_name: str,
    open_subsonic_extension_versions: list[int],
) -> None:
    add_responses(mock_get_open_subsonic_extensions)
    response = subsonic.system.get_open_subsonic_extensions()

    assert response[0].name == open_subsonic_extension_name
    assert response[0].versions == open_subsonic_extension_versions


@responses.activate
def test_check_open_subsonic_extension_available(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_open_subsonic_extensions: list[Response],
    open_subsonic_extension_name: str,
    open_subsonic_extension_versions: list[int],
) -> None:
    add_responses(mock_get_open_subsonic_extensions)
    response = subsonic.system.check_open_subsonic_extension(
        open_subsonic_extension_name, open_subsonic_extension_versions[0]
    )

    assert response


@responses.activate
def test_check_open_subsonic_extension_unavailable_extension(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_open_subsonic_extensions: list[Response],
    open_subsonic_extension_name: str,
    open_subsonic_extension_versions: list[int],
) -> None:
    add_responses(mock_get_open_subsonic_extensions)
    response = subsonic.system.check_open_subsonic_extension(
        "unavailableExtension", open_subsonic_extension_versions[0]
    )

    assert not response


@responses.activate
def test_check_open_subsonic_extension_unavailable_version(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_open_subsonic_extensions: list[Response],
    open_subsonic_extension_name: str,
    open_subsonic_extension_versions: list[int],
) -> None:
    add_responses(mock_get_open_subsonic_extensions)
    response = subsonic.system.check_open_subsonic_extension(
        open_subsonic_extension_name, 72
    )

    assert not response
