from typing import Type


class NoApiAccess(Exception):
    pass


class InvalidRatingNumber(ValueError):
    pass


class VideoArgumentsInSong(ValueError):
    pass


class MissingPlaylistName(ValueError):
    pass


class ResourceNotFound(Exception):
    pass


class AlbumOrArtistArgumentsInSong(ValueError):
    pass


class ShareInvalidSongList(ValueError):
    pass


class CodeError0(Exception):
    pass


class CodeError10(Exception):
    pass


class CodeError20(Exception):
    pass


class CodeError30(Exception):
    pass


class CodeError40(Exception):
    pass


class CodeError41(Exception):
    pass


class CodeError50(Exception):
    pass


class CodeError60(Exception):
    pass


class CodeError70(Exception):
    pass


class UnknownErrorCode(Exception):
    pass


CODE_ERROR_EXCEPTIONS = Type[
    CodeError0
    | CodeError10
    | CodeError20
    | CodeError30
    | CodeError40
    | CodeError41
    | CodeError50
    | CodeError60
    | CodeError70
    | UnknownErrorCode
]


def get_code_error_exception(
    error_code: int,
) -> CODE_ERROR_EXCEPTIONS:
    """With a given code error returns the corresponding exception.

    :param error_code: The error code.
    :type error_code: int
    :return: The associated exception with the error code.
    :rtype: CODE_ERROR_EXCEPTIONS
    """

    match error_code:
        case 0:
            return CodeError0
        case 10:
            return CodeError10
        case 20:
            return CodeError20
        case 30:
            return CodeError30
        case 40:
            return CodeError40
        case 41:
            return CodeError41
        case 50:
            return CodeError50
        case 60:
            return CodeError60
        case 70:
            return CodeError70
        case _:
            return UnknownErrorCode
            return UnknownErrorCode
