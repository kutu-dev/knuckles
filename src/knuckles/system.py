from typing import NamedTuple

from .api import Api
from .models.system import License, SubsonicResponse


class OpenSubsonicExtension(NamedTuple):
    name: str
    versions: list[int]


class System:
    """Class that contains all the methods needed to interact
    with the systems calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/system/>
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def ping(self) -> SubsonicResponse:
        """Calls to the "ping" endpoint of the API.

        Useful to test the status of the server.

        :return: An object with all the data received from the server.
        :rtype: SubsonicResponse
        """

        response = self.api.json_request("ping")

        return SubsonicResponse(**response)

    def get_license(self) -> License:
        """Calls to the "getLicense" endpoint of the API.

        :return: An object with all the information about the status of the license.
        :rtype: License
        """

        response = self.api.json_request("getLicense")["license"]

        return License(**response)

    def get_open_subsonic_extensions(self) -> list[OpenSubsonicExtension]:
        response = self.api.json_request("getOpenSubsonicExtensions")[
            "openSubsonicExtensions"
        ]
        return [
            OpenSubsonicExtension(name, versions) for name, versions in response.items()
        ]
