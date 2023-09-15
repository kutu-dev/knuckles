from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_ping(subsonic: Subsonic, subsonic_response, mock_ping: Response) -> None:
    responses.add(mock_ping)

    response = subsonic.system.ping()

    assert bool(response) is True
    assert response.status == subsonic_response["status"]
    assert response.version == subsonic_response["version"]
    assert response.type == subsonic_response["type"]
    assert response.server_version == subsonic_response["serverVersion"]
    assert response.open_subsonic == subsonic_response["openSubsonic"]


@responses.activate
def test_get_license(
    subsonic: Subsonic, license: dict[str, Any], mock_get_license: Response
) -> None:
    responses.add(mock_get_license)

    response = subsonic.system.get_license()

    assert bool(response) is True
    assert response.valid is license["valid"]
    assert response.email == license["email"]
    assert response.license_expires == parser.parse(license["licenseExpires"])
    assert response.trial_expires == parser.parse(license["trialExpires"])


@responses.activate
def test_auth_without_token(
    subsonic: Subsonic, mock_auth_without_token: Response
) -> None:
    responses.add(mock_auth_without_token)

    subsonic.api.use_token = False
    assert subsonic.system.ping().status == "ok"


@responses.activate
def test_get_open_subsonic_extensions(
    subsonic: Subsonic,
    mock_get_open_subsonic_extensions: Response,
    open_subsonic_extensions: dict[str, Any],
) -> None:
    responses.add(mock_get_open_subsonic_extensions)

    response = subsonic.system.get_open_subsonic_extensions()

    assert response == open_subsonic_extensions
