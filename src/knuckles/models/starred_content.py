from typing import TYPE_CHECKING, Any

from knuckles.models.model import Model

from .album import Album
from .artist import Artist
from .song import Song

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class StarredContent(Model):
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
