from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Model:
    def __init__(self, subsonic: "Subsonic") -> None:
        self._subsonic = subsonic
