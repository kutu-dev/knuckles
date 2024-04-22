from typing import TYPE_CHECKING

# Avoid circular import error
from .artist import Artist
from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Contributor(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        role: str,
        artist: Artist,
        subRole: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.role = role
        self.subrole = subRole
        self.artist = artist
