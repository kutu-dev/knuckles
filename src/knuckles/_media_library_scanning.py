from typing import TYPE_CHECKING

from ._api import Api
from .models._scan_status import ScanStatus

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class MediaLibraryScanning:
    """Class that contains all the methods needed to interact with the
    [media library scanning endpoints](https://opensubsonic.netlify.app/
    categories/media-library-scanning/)
    in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_scan_status(self) -> ScanStatus:
        """Get the status of the scanning of the library.

        Returns:
            An object that holds all the info about the
                current state of the scanning of the library.
        """

        response = self.api.json_request("getScanStatus")["scanStatus"]

        return ScanStatus(self.subsonic, **response)

    def start_scan(self) -> ScanStatus:
        """Request to the server to start a scanning of the library.

        Returns:
            An object that holds all the info about the
                current state of the scanning of the library.
        """

        response = self.api.json_request("startScan")["scanStatus"]

        return ScanStatus(self.subsonic, **response)
