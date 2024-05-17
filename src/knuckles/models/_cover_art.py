from typing import TYPE_CHECKING

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class CoverArt(Model):
    """Object that holds all the info of a cover art.

    Attributes:
        id: The ID of the cover art.
    """

    def __init__(self, subsonic: "Subsonic", id: str) -> None:
        super().__init__(subsonic)

        self.id: str = id
