from typing import TYPE_CHECKING, Any

from .artist import Artist
from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Index(Model):
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
