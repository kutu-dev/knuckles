from typing import TYPE_CHECKING, Any

from dateutil import parser

from ._model import Model
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class MusicDirectory(Model):
    """Object that holds all the info about a music directory.

    Attributes:
        id (str): The ID of the music directory.
        name (str):
        parent (str | None):
        starred (datetime | None): The timestamp when the music directory
            was starred by the authenticated user if it was.
        user_rating (int): The rating given by the authenticated user
            if they rated it.
        average_rating (float | None): The average rating given to the music
            directory.
        play_count (int | None): The number of times songs have been played
            that are in the music directory.
        songs (list[Song] | None): List that holds all the info about all
            the songs that are part of the music directory.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        name: str,
        parent: str | None = None,
        starred: str | None = None,
        userRating: int | None = None,
        averageRating: float | None = None,
        playCount: int | None = None,
        child: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.parent = parent
        self.starred = parser.parse(starred) if starred else None
        self.user_rating = userRating
        self.average_rating = averageRating
        self.play_count = playCount
        self.songs = (
            [Song(subsonic=self._subsonic, **song) for song in child] if child else None
        )
