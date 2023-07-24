from .models import (
    Album,
    Artist,
    ChatMessage,
    CoverArt,
    License,
    ScanStatus,
    Song,
    SubsonicResponse,
)
from .subsonic import Subsonic

__all__ = [
    "Subsonic",
    "Album",
    "Artist",
    "ChatMessage",
    "CoverArt",
    "License",
    "ScanStatus",
    "Song",
    "SubsonicResponse",
]

# TODO to implement
# * - setRating -> Album(Non ID3), Artist(Non ID3)
# * - scrobble -> Song, Video -> (Multiple files at the same time? ambiguous docs)

#! Not implemented
# * - Audio transcoding
# * - Video
# * - Open Subsonic Extensions
# * - CA Certs
# * - Non ID3
