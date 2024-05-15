from typing import TYPE_CHECKING, NamedTuple

from ._api import Api
from .models._system import License, SubsonicResponse

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class OpenSubsonicExtension(NamedTuple):
    name: str
    versions: list[int]


class System:
    """Class that contains all the methods needed to interact with the
    [system endpoints](https://opensubsonic.netlify.app/
    categories/system/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def ping(self) -> SubsonicResponse:
        """Make a ping to the server.

        Returns:
            An object that holds all the info returned by the server.
        """

        response = self.api.json_request("ping")

        return SubsonicResponse(self.subsonic, **response)

    def get_license(self) -> License:
        """Get the current status of the license of the server.

        Returns:
            An object that contains all the info about the status
                of the license of the server.
        """

        response = self.api.json_request("getLicense")["license"]

        return License(self.subsonic, **response)

    def get_open_subsonic_extensions(self) -> list[OpenSubsonicExtension]:
        """Get all the available OpenSubsonic REST API extensions for the
        connected server.

        Returns:
            A list that contains all the info about all the available
                extensions in the connected server.
        """

        response = self.api.json_request("getOpenSubsonicExtensions")[
            "openSubsonicExtensions"
        ]
        return [
            OpenSubsonicExtension(name, versions) for name, versions in response.items()
        ]

    def check_open_subsonic_extension(
        self, extension_name: str, extension_version: int
    ) -> bool:
        """Check if a OpenSubonic REST API extension is available on the
        connected server.

        Args:
            extension_name: The name of the extension to check if its
                available.
            extension_version: The version of the extension to check if
                its available.

        Returns:
            If the given extension at the given version is available on
                the connected server or not.
        """

        extensions = self.get_open_subsonic_extensions()

        for extension in extensions:
            if extension.name != extension_name:
                continue

            if extension_version in extension.versions:
                return True

        return False
