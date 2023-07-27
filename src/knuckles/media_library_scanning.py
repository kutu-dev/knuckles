from .api import Api
from .models.scan_status import ScanStatus


class MediaLibraryScanning:
    """Class that contains all the methods needed to interact
    with the media library scanning calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/media-library-scanning/>
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def get_scan_status(self) -> ScanStatus:
        """Calls to the "getScanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response = self.api.request("getScanStatus")["scanStatus"]

        return ScanStatus(**response)

    def start_scan(self) -> ScanStatus:
        """Calls to the "scanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response = self.api.request("startScan")["scanStatus"]

        return ScanStatus(**response)
