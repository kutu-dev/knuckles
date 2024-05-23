from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Model:
    """Generic parent class for all the models.
    Have an internal attribute to hold a Subsonic object to
    access the OpenSubsonic REST API.
    """

    def __init__(self, subsonic: "Subsonic") -> None:
        self._subsonic = subsonic
