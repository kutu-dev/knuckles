from typing import TYPE_CHECKING

# Avoid circular import error
from ._artist import Artist
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Contributor(Model):
    """Object that holds all the info about a contributor.

    Attributes:
        role (str): The role of the contributor.
        artist (Artist): All the artist info associated with the
            contributor.
        subrole (str | None): The subrole of the contributor.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        role: str,
        artist: Artist,
        subRole: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.role = role
        self.artist = artist
        self.subrole = subRole
