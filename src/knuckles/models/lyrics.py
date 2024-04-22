from typing import TYPE_CHECKING

from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Lyrics(Model):
    def __init__(
        self, subsonic: "Subsonic", artist: str, title: str, value: str
    ) -> None:
        super().__init__(subsonic)

        self.artist_name = artist
        self.song_title = title
        self.lyrics = value
