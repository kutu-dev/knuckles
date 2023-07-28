from typing import TYPE_CHECKING, Any

from dateutil import parser

from ..models.song import CoverArt, Song
from ..models.user import User

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Playlist:
    """Representation of all the data related to a user in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        name: str | None = None,
        songCount: int | None = None,
        duration: int | None = None,
        created: str | None = None,
        changed: str | None = None,
        comment: str | None = None,
        owner: str | None = None,
        public: bool = False,
        coverArt: str | None = None,
        allowedUser: list[str] | None = None,
        entry: list[dict[str, Any]] | None = None,
    ) -> None:
        self.__subsonic = subsonic
        self.id = id
        self.name = name
        self.song_count = songCount
        self.duration = duration
        self.created = parser.parse(created) if created else None
        self.changed = parser.parse(changed) if changed else None
        self.comment = comment
        self.owner = User(owner, subsonic=self.__subsonic) if owner else None
        self.public = public
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.allowed_users = (
            [User(username) for username in allowedUser] if allowedUser else None
        )
        self.songs = (
            [Song(self.__subsonic, **song) for song in entry] if entry else None
        )
