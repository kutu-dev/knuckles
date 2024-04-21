from typing import TYPE_CHECKING

from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class CoverArt(Model):
    """Representation of all the data related to a cover art in Subsonic."""

    def __init__(self, subsonic: "Subsonic", id: str) -> None:
        """Representation of all the data related to a cover art in Subsonic.

        :param id: The ID of the cover art.
        :type id: str
        """

        super().__init__(subsonic)

        self.id: str = id
