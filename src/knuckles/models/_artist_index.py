from typing import TYPE_CHECKING, Any

from ._artist import Artist
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class ArtistIndex(Model):
    """Object that holds all the info about an artist index.

    Attributes:
        ignored_articles (list[str]): Ignored articles in the index.
        index (dict[str, list[Artist]] | None): Dictionary that holds
            the index, where the key is the index letter and the value
            a list of objects that holds all the info related with the
            artists in that are in the given index.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        ignoredArticles: str,
        index: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.ignored_articles = ignoredArticles

        self.index: dict[str, list[Artist]] | None

        if index is None:
            self.index = None
            return

        self.index = {}

        for entry in index:
            self.index[entry["name"]] = [
                Artist(subsonic=self._subsonic, **artist) for artist in entry["artist"]
            ]
