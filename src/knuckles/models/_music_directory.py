from typing import TYPE_CHECKING, Any

from dateutil import parser

from ._model import Model
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class MusicDirectory(Model):
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
