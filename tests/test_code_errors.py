from typing import Any, Type

import pytest
import responses
from responses import matchers

import knuckles.exceptions
from knuckles import Subsonic

code_errors = [
    (0, "A generic error.", knuckles.exceptions.CodeError0),
    (10, "Required parameter is missing.", knuckles.exceptions.CodeError10),
    (
        20,
        "Incompatible Subsonic REST protocol version. Client must upgrade.",
        knuckles.exceptions.CodeError20,
    ),
    (
        30,
        "Incompatible Subsonic REST protocol version. Server must upgrade.",
        knuckles.exceptions.CodeError30,
    ),
    (40, "Wrong username or password.", knuckles.exceptions.CodeError40),
    (
        41,
        "Token authentication not supported for LDAP users.",
        knuckles.exceptions.CodeError41,
    ),
    (
        50,
        "User is not authorized for the given operation.",
        knuckles.exceptions.CodeError50,
    ),
    (
        60,
        (
            "The trial period for the Subsonic server is over."
            + "Please upgrade to Subsonic Premium. Visit subsonic.org for details."
        ),
        knuckles.exceptions.CodeError60,
    ),
    (70, "The requested data was not found.", knuckles.exceptions.CodeError70),
    (80, "The cake is a lie!", knuckles.exceptions.UnknownErrorCode),
]


@pytest.mark.parametrize("code, message, exception", code_errors)
@responses.activate
def test_code_errors(
    subsonic: Subsonic,
    params: dict[str, str],
    subsonic_response: dict[str, Any],
    code: int,
    message: str,
    exception: Type[Exception],
) -> None:
    subsonic_response["subsonic-response"]["status"] = "failed"
    subsonic_response["subsonic-response"]["error"] = {"code": code, "message": message}

    responses.add(
        responses.GET,
        url="https://example.com/rest/ping",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    with pytest.raises(exception, match=message):
        subsonic.ping()
