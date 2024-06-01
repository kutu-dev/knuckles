from typing import Type

import knuckles.exceptions
import pytest
import responses
from knuckles import Subsonic

from tests.conftest import AddResponses, MockGenerator

code_errors = [
    (0, "A generic error.", knuckles.exceptions.ErrorCode0),
    (10, "Required parameter is missing.", knuckles.exceptions.ErrorCode10),
    (
        20,
        "Incompatible Subsonic REST protocol version. Client must upgrade.",
        knuckles.exceptions.ErrorCode20,
    ),
    (
        30,
        "Incompatible Subsonic REST protocol version. Server must upgrade.",
        knuckles.exceptions.ErrorCode30,
    ),
    (40, "Wrong username or password.", knuckles.exceptions.ErrorCode40),
    (
        41,
        "Token authentication not supported for LDAP users.",
        knuckles.exceptions.ErrorCode41,
    ),
    (
        50,
        "User is not authorized for the given operation.",
        knuckles.exceptions.ErrorCode50,
    ),
    (
        60,
        (
            "The trial period for the Subsonic server is over. "
            + "Please upgrade to Subsonic Premium. Visit subsonic.org for details."
        ),
        knuckles.exceptions.ErrorCode60,
    ),
    (70, "The requested data was not found.", knuckles.exceptions.ErrorCode70),
    (80, "The cake is a lie!", knuckles.exceptions.UnknownErrorCode),
]


# Manually generate a mock for each error
@pytest.mark.parametrize("code, message, exception", code_errors)
@responses.activate
def test_code_errors(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_generator: MockGenerator,
    code: int,
    message: str,
    exception: Type[Exception],
) -> None:
    add_responses(
        mock_generator(
            "ping",
            {},
            {"status": "failed", "error": {"code": code, "message": message}},
        )
    )

    with pytest.raises(exception, match=message):
        subsonic.system.ping()
