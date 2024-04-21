from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Model:
    def __init__(self, subsonic: "Subsonic") -> None:
        self._subsonic = subsonic
