from typing import TYPE_CHECKING

from knuckles.models._model import Model

from ._album import Album
from ._artist import Artist
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class SearchResult(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        songs: list[Song] | None = None,
        albums: list[Album] | None = None,
        artists: list[Artist] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.songs = songs
        self.albums = albums
        self.artists = artists
