from typing import TYPE_CHECKING

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class ScanStatus(Model):
    """Object that holds all the info about a scan status.

    Attributes:
        scanning (bool): If the server is scanning media or not.
        count (int): The number of media already scanned.
    """

    def __init__(self, subsonic: "Subsonic", scanning: bool, count: int) -> None:
        super().__init__(subsonic)

        self.scanning: bool = scanning
        self.count: int = count
