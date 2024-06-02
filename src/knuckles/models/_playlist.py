from typing import TYPE_CHECKING, Any, Self

from dateutil import parser

from ._cover_art import CoverArt
from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Playlist(Model):
    """Object that holds all the info about a playlist.

    Attributes:
        id (str): The ID of the playlist.
        name (str | None): The name of the playlist.
        song_count (int | None): The number of songs in the playlist.
        duration (int | None): The total durations of all the songs in the
            playlist.
        created (datetime | None): The timestamp when the playlist was created.
        changed (datetime | None): The timestamp when the playlist was last
            edited.
        comment (str | None): A comment attach with the playlist.
        owner (User | None): All the info related with the user creator of
            the playlist.
        public (bool | None): If the playlist is public or not.
        cover_art (CoverArt | None): All the info related with the cover art
            of the playlist.
        allowed_users (list[User] | None): List that holds all the info
            related with all the users allowed to see the playlist.
        songs (list[Song] | None): List that holds all the info about
            all the songs in the playlist.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
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
        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.song_count = songCount
        self.duration = duration
        self.created = parser.parse(created) if created else None
        self.changed = parser.parse(changed) if changed else None
        self.comment = comment
        self.owner = User(self._subsonic, owner) if owner else None
        self.public = public
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
        self.allowed_users = (
            [User(self._subsonic, username) for username in allowedUser]
            if allowedUser
            else None
        )
        self.songs = [Song(self._subsonic, **song) for song in entry] if entry else None

    def generate(self) -> "Playlist":
        """Return a new playlist object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.playlists.get_playlist(self.id)

    def create(self) -> "Playlist":
        """Create a playlist with the same info of the object.

        Returns:
            The new created playlist.
        """

        # Create a list of Song IDs if songs is not None
        songs_ids = [song.id for song in self.songs] if self.songs else None

        new_playlist = self._subsonic.playlists.create_playlist(
            # Ignore the None type error as the server
            # should return an Error Code 10 in response
            self.name,  # type: ignore[arg-type]
            self.comment,
            self.public,
            songs_ids,
        )

        return new_playlist

    def update(self) -> Self:
        """Updates changed info between the model and the server.

        Warning:
            It doesn't change the list of songs in the playlist. For do
            it use the `add_songs` and `remove_songs` methods.

        Returns:
            The object itself.
        """

        self._subsonic.playlists.update_playlist(
            self.id, comment=self.comment, public=self.public
        )

        return self

    def delete(self) -> Self:
        """Delete the playlist from the server.

        Returns:
            The object itself.
        """

        self._subsonic.playlists.delete_playlist(self.id)

        return self

    def add_songs(self, song_ids: list[str]) -> Self:
        """Add songs to the playlist.

        Args:
            song_ids: The ID of songs to add.

        Returns:
            The object itself.
        """

        self._subsonic.playlists.update_playlist(self.id, song_ids_to_add=song_ids)

        if not self.songs:
            self.songs = []

        for id_ in song_ids:
            self.songs.append(Song(self._subsonic, id_))

        if not self.song_count:
            self.song_count = 0

        self.song_count += len(song_ids)

        return self

    def remove_songs(self, songs_indexes: list[int]) -> Self:
        """Remove songs from the playlist.

        Args:
            songs_indexes: The indexes of the songs to remove.

        Returns:
            The object itself.
        """

        self._subsonic.playlists.update_playlist(
            self.id, song_indexes_to_remove=songs_indexes
        )

        if not self.songs:
            self.songs = []

        for index in songs_indexes:
            del self.songs[index]

        if not self.song_count:
            self.song_count = 0

        self.song_count -= len(songs_indexes)

        return self
