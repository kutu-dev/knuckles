from typing import TYPE_CHECKING

from .api import Api
from .models.scan_status import ScanStatus

if TYPE_CHECKING:
    from .subsonic import Subsonic


class MediaLibraryScanning:
    """Class that contains all the methods needed to interact
    with the media library scanning calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/media-library-scanning/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_scan_status(self) -> ScanStatus:
        """Calls to the "getScanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response = self.api.json_request("getScanStatus")["scanStatus"]

        return ScanStatus(self.subsonic, **response)

    def start_scan(self) -> ScanStatus:
        """Calls to the "scanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response = self.api.json_request("startScan")["scanStatus"]

        return ScanStatus(self.subsonic, **response)
