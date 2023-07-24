from datetime import datetime
from typing import Any

import responses
from responses import matchers

from knuckles import License, Subsonic, SubsonicResponse


@responses.activate
def test_ping(
    subsonic: Subsonic, params: dict[str, str], subsonic_response: dict[str, Any]
) -> None:
    responses.add(
        responses.GET,
        url="https://example.com/rest/ping",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: SubsonicResponse = subsonic.ping()

    assert bool(response) is True
    assert response.status == "ok"
    assert response.version == "1.16.1"
    assert response.type == "knuckles"
    assert response.server_version == "0.1.3 (tag)"
    assert response.open_subsonic is True


@responses.activate
def test_get_license(
    subsonic: Subsonic, params: dict[str, str], subsonic_response: dict[str, Any]
) -> None:
    subsonic_response["subsonic-response"]["license"] = {
        "valid": True,
        "email": "user@example.com",
        "licenseExpires": "2017-04-11T10:42:50.842Z",
        "trialExpires": "2015-03-11T12:36:38.753Z",
    }

    responses.add(
        responses.GET,
        url="https://example.com/rest/getLicense",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: License = subsonic.get_license()

    assert bool(response) is True
    assert response.valid is True
    assert response.email == "user@example.com"
    assert type(response.license_expires) is datetime
    assert response.license_expires.timestamp() == 1491907370.842
    assert type(response.trial_expires) is datetime
    assert response.trial_expires.timestamp() == 1426077398.753


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

    subsonic.use_token = False
    assert subsonic.ping().status == "ok"
    assert subsonic.ping().status == "ok"
