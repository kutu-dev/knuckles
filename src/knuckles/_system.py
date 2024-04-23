from typing import TYPE_CHECKING, NamedTuple

from ._api import Api
from .models._system import License, SubsonicResponse

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class OpenSubsonicExtension(NamedTuple):
    name: str
    versions: list[int]


class System:
    """Class that contains all the methods needed to interact
    with the systems calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/system/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def ping(self) -> SubsonicResponse:
        """Calls to the "ping" endpoint of the API.

        Useful to test the status of the server.

        :return: An object with all the data received from the server.
        :rtype: SubsonicResponse
        """

        response = self.api.json_request("ping")

        return SubsonicResponse(self.subsonic, **response)

    def get_license(self) -> License:
        """Calls to the "getLicense" endpoint of the API.

        :return: An object with all the information about the status of the license.
        :rtype: License
        """

        response = self.api.json_request("getLicense")["license"]

        return License(self.subsonic, **response)

    def get_open_subsonic_extensions(self) -> list[OpenSubsonicExtension]:
        response = self.api.json_request("getOpenSubsonicExtensions")[
            "openSubsonicExtensions"
        ]
        return [
            OpenSubsonicExtension(name, versions) for name, versions in response.items()
        ]

    def check_open_subsonic_extension(
        self, extension_name: str, extension_version: int
    ) -> bool:
        extensions = self.get_open_subsonic_extensions()

        for extension in extensions:
            if extension.name != extension_name:
                continue

            if extension_version in extension.versions:
                return True

        return False
