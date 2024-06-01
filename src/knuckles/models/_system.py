from datetime import datetime
from typing import TYPE_CHECKING

from dateutil import parser

from knuckles.models._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class SubsonicResponse(Model):
    """Object that holds all the generic info about a
    response in a OpenSubsonic REST API call.

    Attributes:
        status (str): The status of the response, can be "ok" or "failed".
        version (str): The server supported version of the OpenSubonic REST API.
        type (str | None): The name of the server reported by itself.
        server_version (str | None): The server actual version.
        open_subsonic (bool | None): If the server supports OpenSubsonic REST API
            extensions.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        status: str,
        version: str,
        type: str | None = None,
        serverVersion: str | None = None,
        openSubsonic: bool | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.status = status
        self.version = version
        self.type = type
        self.server_version = serverVersion
        self.open_subsonic = openSubsonic


class License(Model):
    """Object that holds all the info about the license status of the server.

    Attributes:
        valid (bool): If the license of the server is valid.
        email (str | None): The email of the authenticated user.
        license_expires (datetime | None): The timestamp when the
            license expires.
        trial_expires (datetime | None): The timestamp when the
            trial expires if it has not already.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        valid: bool,
        email: str | None = None,
        licenseExpires: str | None = None,
        trialExpires: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.valid: bool = valid
        self.email: str | None = email

        self.license_expires: datetime | None
        if licenseExpires is not None:
            self.license_expires = parser.parse(licenseExpires)
        else:
            self.license_expires = None

        self.trial_expires: datetime | None
        if trialExpires is not None:
            self.trial_expires = parser.parse(trialExpires)
        else:
            self.trial_expires = None

    def __bool__(self) -> bool:
        return self.valid
