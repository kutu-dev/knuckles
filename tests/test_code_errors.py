import knuckles.exceptions
import pytest
import responses
from knuckles import Subsonic
from responses import matchers

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
    code: int,
    message: str,
    exception,
) -> None:
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
                "error": {"code": code, "message": message},
            }
        },
        status=200,
    )

    with pytest.raises(exception, match=message):
        subsonic.ping()
