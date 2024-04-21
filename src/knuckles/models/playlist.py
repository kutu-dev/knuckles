from typing import TYPE_CHECKING, Any, Self

from dateutil import parser

from .cover_art import CoverArt
from .model import Model
from .song import Song
from .user import User

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Playlist(Model):
    """Representation of all the data related to a playlist in Subsonic."""

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
        """Representation of all the data related to a user in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The ID of the playlist.
        :type id: str
        :param name: The name of the playlist, defaults to None.
        :type name: str | None, optional
        :param songCount: The numbers of songs inside the playlist, defaults to None.
        :type songCount: int | None, optional
        :param duration: The total duration of the playlist, defaults to None.
        :type duration: int | None, optional
        :param created: The time when the playlist was created, defaults to None.
        :type created: str | None, optional
        :param changed: The last time the playlist was changed, defaults to None.
        :type changed: str | None, optional
        :param comment: The comment of the playlist, defaults to None.
        :type comment: str | None, optional
        :param owner: The owner of the playlist, defaults to None.
        :type owner: str | None, optional
        :param public: If the playlist is public, defaults to None.
        :type public: bool | None, optional
        :param coverArt: The ID of the cover art of the playlist, defaults to None.
        :type coverArt: str | None, optional
        :param allowedUser: The list of users allowed to reproduce the playlist,
            defaults to None.
        :type allowedUser: list[str] | None, optional
        :param entry: A list with all the songs inside the playlist, defaults to None.
        :type entry: list[dict[str, Any]] | None, optional
        """

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
        """Return a new playlist with all the data updated from the API,
        using the endpoint that return the most information possible.

        :return: A new playlist object with all the data updated.
        :rtype: Playlist
        """

        return self._subsonic.playlists.get_playlist(self.id)

    def create(self) -> "Playlist":
        """Calls the "createPlaylist" endpoint of the API.

        Creates a new playlist with the same data of the object
        where the method is called.

        :return: The new created playlist.
        :rtype: Playlist
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
        """Calls the "updatePlaylist" endpoint of the API.

        Updates the name, comment and public state of the playlist with the ones
        in the parameters of the object.

        NOT the playlist list, please use TODO (add_songs)
        and TODO (remove_songs) to reflect it in the model.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """
        self._subsonic.playlists.update_playlist(
            self.id, self.name, self.comment, self.public
        )

        return self

    def delete(self) -> Self:
        """Calls the "deletePlaylist" endpoint of the API.

        Delete the playlist with the same ID as the id parameter in the object.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """
        self._subsonic.playlists.delete_playlist(self.id)

        return self

    def add_songs(self, song_ids: list[str]) -> Self:
        """Add any number of new songs to the playlist
        It's reflected in the songs list in the model.

        :param song_ids: A list with the IDs of the songs to add.

        :return: The object itself to allow method chaining.
        :rtype: Self
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
        """Remove any number of new songs to the playlist
        It's reflected in the songs list in the model.

        :param song_indexes: A list with the indexes of the songs to remove.

        :return: The object itself to allow method chaining.
        :rtype: Self
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
