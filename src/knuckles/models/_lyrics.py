from typing import TYPE_CHECKING

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Lyrics(Model):
    """Object that holds all the info about the lyrics of a song.

    Attributes:
        artist_name (str): The name of the artist of the song.
        song_title (str): The title of the song.
        lyrics (str): The lyrics text of the song.
    """

    def __init__(
        self, subsonic: "Subsonic", artist: str, title: str, value: str
    ) -> None:
        super().__init__(subsonic)

        self.artist_name = artist
        self.song_title = title
        self.lyrics = value
