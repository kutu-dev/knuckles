from typing import TYPE_CHECKING, Any

from knuckles.models._model import Model

from ._album import Album
from ._artist import Artist
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class StarredContent(Model):
    """Object that holds all the info about starred content.

    Attributes:
        songs (list[Song] | None): List that holds all the info
            about all the starred songs.
        albums (list[Album] | None): List that holds all the info
            about all the starred albums.
        artists (list[Artist] | None): List that holds all the info
            about all the starred artists.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        song: list[dict[str, Any]] | None = None,
        album: list[dict[str, Any]] | None = None,
        artist: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.songs = (
            [Song(subsonic=self._subsonic, **song) for song in song] if song else None
        )
        self.albums = (
            [Album(subsonic=self._subsonic, **album) for album in album]
            if album
            else None
        )
        self.artists = (
            [Artist(subsonic=self._subsonic, **artist) for artist in artist]
            if artist
            else None
        )
