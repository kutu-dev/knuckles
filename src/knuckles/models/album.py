from typing import TYPE_CHECKING, Any

from dateutil import parser

import knuckles.models.song as song_object

from ..models.artist import Artist
from ..models.cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic


# TODO Unfinished
class Album:
    """Representation of all the data related to an album in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        parent: str | None = None,
        album: str | None = None,
        title: str | None = None,
        name: str | None = None,
        isDir: bool | None = None,
        artist: str | None = None,
        artistId: str | None = None,
        coverArt: str | None = None,
        songCount: int | None = None,
        duration: int | None = None,
        playCount: int | None = None,
        created: str | None = None,
        starred: str | None = None,
        year: int | None = None,
        genre: str | None = None,
        played: str | None = None,
        userRating: int | None = None,
        song: list[dict[str, Any]] | None = None,
    ) -> None:
        self.__subsonic = subsonic
        self.id = id
        self.parent = parent
        self.album = album
        self.name = name
        self.is_dir = isDir
        self.title = title
        self.artist = Artist(artistId, artist) if artistId else None
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.song_count = songCount
        self.duration = duration
        self.play_count = playCount
        self.created = parser.parse(created) if created else None
        self.starred = parser.parse(starred) if starred else None
        self.year = year
        self.genre = genre
        self.played = parser.parse(played) if played else None
        self.user_rating = userRating
        self.songs = (
            [song_object.Song(self.__subsonic, **song_data) for song_data in song]
            if song
            else None
        )
