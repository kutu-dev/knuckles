from typing import TYPE_CHECKING, Any, Self

from dateutil import parser

from ..exceptions import MissingPlaylistName
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
        public: bool | None = None,
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

    def generate(self) -> "Playlist":
        return self.__subsonic.playlists.get_playlist(self.id)

    def create(self) -> "Playlist":
        if self.name is None:
            raise MissingPlaylistName(
                (
                    "A not None value in the name parameter"
                    + "is necessary to create a playlist"
                )
            )

        # Create a list of Song IDs if songs is not None
        songs_ids = [song.id for song in self.songs] if self.songs else None

        # As the createPlaylist endpoint is very limited
        # a call to the updatePlaylist endpoint is used to extend it
        new_playlist = self.__subsonic.playlists.create_playlist(
            self.name, self.comment, self.public, songs_ids
        )

        return new_playlist

    def update(self) -> Self:
        self.__subsonic.playlists.update_playlist(
            self.id, self.name, self.comment, self.public
        )

        return self

    def delete(self) -> Self:
        self.__subsonic.playlists.delete_playlist(self.id)

        return self
