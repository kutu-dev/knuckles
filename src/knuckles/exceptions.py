from typing import Type


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


class InvalidRatingNumber(Exception):
    pass


class VideoArgumentsInSong(ValueError):
    pass


class AlbumOrArtistArgumentsInSong(ValueError):
    pass
