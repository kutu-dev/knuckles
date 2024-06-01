from typing import TYPE_CHECKING

from knuckles.models._model import Model

from ._album import Album
from ._artist import Artist
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class SearchResult(Model):
    """Object that holds all the info about a search result.

    Attributes:
        songs (list[Song] | None): List that holds all the info about
            all the songs returned in the search result.-
        albums (list[Album] | None): List that holds all the info about
            all the albums returned in the search result.
        artists (list[Artist] | None): List that holds all the info about
            all the artists returned in the search result.
    """

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
