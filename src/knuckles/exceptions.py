from typing import Type


class MissingRequiredProperty(Exception):
    """Raised when a property required to call a method is missing."""

    pass


class InvalidRatingNumber(ValueError):
    """Raised when input an invalid rating weight in a method of the API."""

    pass


class ResourceNotFound(Exception):
    """Raised when a resource could not be retrieve to
    generate a model using a previous one."""

    def __init__(
        self,
        message: str = (
            "Unable to generate the model as it does not exist in the server"
        ),
        *args: str,
    ) -> None:
        super().__init__(message, *args)


class ShareInvalidSongList(ValueError):
    """Raised when a method in a share is called with an invalid song list."""

    pass


class ErrorCode0(Exception):
    """Raised when the server returns an error code 0,
    it being a generic error.
    """

    pass


class ErrorCode10(Exception):
    """Raised when the server returns an error code 10,
    meaning that a parameter for the requested endpoint is missing.
    Should never be raised because Knuckles takes care for enforcing mandatory
    parameters, if you have encountered this exception the server may have
    broke the OpenSubsonic API.

    If you suspect that this is an issue caused by Knuckles itself,
    please report it to upstream.
    """

    pass


class ErrorCode20(Exception):
    """Raised when the server returns an error code 20,
    meaning that the client has a lower RESP API version than the server.
    Should never be raised given that Knuckles supports up to the latest
    Subsonic REST API version.
    """

    pass


class ErrorCode30(Exception):
    """Raised when the server returns an error code 30,
    meaning that the server has a lower RESP API version than the client.
    """

    pass


class ErrorCode40(Exception):
    """Raised when the server returns an error code 40,
    meaning that the given user doesn't exists or the password is incorrect.
    """

    pass


class ErrorCode41(Exception):
    """Raised when the server returns an error code 42,
    meaning that token authentication is not available.
    """

    pass


class ErrorCode50(Exception):
    """Raised when the server returns an error code 50,
    meaning that the authenticated user is no authorized
    for the requested action.
    """

    pass


class ErrorCode60(Exception):
    """Raised when the server return an error code 60,
    meaning that the Subsonic trial period has ended.
    """

    pass


class ErrorCode70(Exception):
    """Raised when the server returns an error code 70,
    meaning that the requested data wasn't found.
    """

    pass


class UnknownErrorCode(Exception):
    """Raised when the server returns an error code that doesn't
    have a specific core error exception.
    """

    pass


ERROR_CODE_EXCEPTION = Type[
    ErrorCode0
    | ErrorCode10
    | ErrorCode20
    | ErrorCode30
    | ErrorCode40
    | ErrorCode41
    | ErrorCode50
    | ErrorCode60
    | ErrorCode70
    | UnknownErrorCode
]


def get_error_code_exception(
    error_code: int,
) -> ERROR_CODE_EXCEPTION:
    """Converts a numeric error code to its corresponding error code exception

    Args:
        error_code: The number of the error to get its exception.

    Returns: The exception of the given error code
    """
    match error_code:
        case 0:
            return ErrorCode0
        case 10:
            return ErrorCode10
        case 20:
            return ErrorCode20
        case 30:
            return ErrorCode30
        case 40:
            return ErrorCode40
        case 41:
            return ErrorCode41
        case 50:
            return ErrorCode50
        case 60:
            return ErrorCode60
        case 70:
            return ErrorCode70
        case _:
            return UnknownErrorCode
