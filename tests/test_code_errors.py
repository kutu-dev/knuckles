import pytest
import knuckles
from knuckles import Subsonic, SubsonicResponse, Song, License
from responses import matchers
import responses


@responses.activate
def test_code_error_0(subsonic: Subsonic, params: dict[str, str]) -> None:
    responses.add(
        responses.GET,
        url="https://example.com/rest/ping",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {"code": 0, "message": "A generic error."},
            }
        },
        status=200,
    )

    with pytest.raises(knuckles.exceptions.CodeError0, match="A generic error."):
        subsonic.ping()


@responses.activate
def test_code_error_10(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {"code": 10, "message": "Required parameter is missing."},
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError10, match="Required parameter is missing."
    ):
        subsonic.ping()


@responses.activate
def test_code_error_20(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 20,
                    "message": "Incompatible Subsonic REST protocol version. Client must upgrade.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError20,
        match="Incompatible Subsonic REST protocol version. Client must upgrade.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_30(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 30,
                    "message": "Incompatible Subsonic REST protocol version. Server must upgrade.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError30,
        match="Incompatible Subsonic REST protocol version. Server must upgrade.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_40(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 40,
                    "message": "Wrong username or password.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError40,
        match="Wrong username or password.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_41(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 41,
                    "message": "Token authentication not supported for LDAP users.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError41,
        match="Token authentication not supported for LDAP users.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_50(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 50,
                    "message": "User is not authorized for the given operation.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError50,
        match="User is not authorized for the given operation.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_60(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 60,
                    "message": "The trial period for the Subsonic server is over. Please upgrade to Subsonic Premium. Visit subsonic.org for details.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError60,
        match="The trial period for the Subsonic server is over. Please upgrade to Subsonic Premium. Visit subsonic.org for details.",
    ):
        subsonic.ping()


@responses.activate
def test_code_error_70(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 70,
                    "message": "The requested data was not found.",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.CodeError70,
        match="The requested data was not found.",
    ):
        subsonic.ping()


@responses.activate
def test_unknown_code_error(subsonic: Subsonic) -> None:
    responses.add(
        responses.GET,
        "https://example.com/rest/ping",
        json={
            "subsonic-response": {
                "status": "failed",
                "version": "1.16.1",
                "type": "knuckles",
                "serverVersion": "0.1.3 (tag)",
                "openSubsonic": True,
                "error": {
                    "code": 80,
                    "message": "The cake is a lie!",
                },
            }
        },
        status=200,
    )

    with pytest.raises(
        knuckles.exceptions.UnknownErrorCode,
        match="The cake is a lie!",
    ):
        subsonic.ping()
