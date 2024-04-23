from typing import TYPE_CHECKING

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class ScanStatus(Model):
    """Representation of all the data related to the status
    of a library scan in Subsonic.
    """

    def __init__(self, subsonic: "Subsonic", scanning: bool, count: int) -> None:
        """Representation of all the data related to the status
        of a library scan in Subsonic.

        :param scanning: The status of the scan.
        :type scanning: bool
        :param count: Scanned item count.
        :type count: int
        """

        super().__init__(subsonic)

        self.scanning: bool = scanning
        self.count: int = count
