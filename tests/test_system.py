from typing import Any

import responses
from responses import Response, matchers

from knuckles import License, Subsonic


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

    response: License = subsonic.system.get_license()

    assert bool(response) is True
    assert response.valid is license["valid"]
    assert response.email == license["email"]
    assert response.license_expires.timestamp() == license["licenseExpires"]
    assert response.trial_expires.timestamp() == license["trialExpires"]


@responses.activate
def test_auth_without_token(
    subsonic: Subsonic,
    params: dict[str, str],
    password: str,
    subsonic_response: dict[str, Any],
) -> None:
    params["p"] = password

    responses.add(
        responses.GET,
        url="https://example.com/rest/ping",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    subsonic.api.use_token = False
    assert subsonic.system.ping().status == "ok"
    assert subsonic.system.ping().status == "ok"
