from typing import TYPE_CHECKING, Any, Self

from dateutil import parser

from ..models.song import CoverArt, Song
from ..models.user import User

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Playlist:
    """Representation of all the data related to a playlist in Subsonic."""

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
        """Return a new playlist with all the data updated from the API,
        using the endpoint that return the most information possible.

        :return: A new playlist object with all the data updated.
        :rtype: Playlist
        """

        return self.__subsonic.playlists.get_playlist(self.id)

    def create(self) -> "Playlist":
        """Calls the "createPlaylist" endpoint of the API.

        Creates a new playlist with the same data of the object
        where the method is called.

        :return: The new created playlist.
        :rtype: Playlist
        """
        # Create a list of Song IDs if songs is not None
        songs_ids = [song.id for song in self.songs] if self.songs else None

        new_playlist = self.__subsonic.playlists.create_playlist(
            # Ignore the None type error as the server
            # should return a Error Code 10 in response
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

        :return: The object itself to allow method chaining.
        :rtype: Self
        """
        self.__subsonic.playlists.update_playlist(
            self.id, self.name, self.comment, self.public
        )

        return self

    def delete(self) -> Self:
        """Calls the "deletePlaylist" endpoint of the API.

        Delete the playlist with the same ID as the id parameter in the object.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """
        self.__subsonic.playlists.delete_playlist(self.id)

        return self
