from datetime import datetime

from dateutil import parser


class SubsonicResponse:
    """Representation of the generic successful response data
    in a request to the API.
    """

    def __init__(
        self,
        status: str,
        version: str,
        type: str | None = None,
        serverVersion: str | None = None,
        openSubsonic: bool = False,
    ) -> None:
        """Representation of the generic successful response data
        in a request to the API.

        Transform all the data in camelCase to snake_case.

        :param status: The command result. It can be "ok" or "failed".
        :type status: str
        :param version: The server supported Subsonic API version.
        :type version: str
        :param type: The server actual name (OpenSubsonic), defaults to None
        :type type: str | None, optional
        :param serverVersion: The server actual version (OpenSubsonic), defaults to None
        :type serverVersion: str | None, optional
        :param openSubsonic: The support of the OpenSubsonic v1 specifications,
            defaults to False
        :type openSubsonic: bool, optional
        """

        self.status: str = status
        self.version: str = version
        self.type: str | None = type
        self.server_version: str | None = serverVersion
        self.open_subsonic: bool = openSubsonic


class License:
    """Representation of the license related data in Subsonic."""

    def __init__(
        self,
        valid: bool,
        email: str | None = None,
        licenseExpires: str | None = None,
        trialExpires: str | None = None,
    ) -> None:
        """Representation of the license related data in Subsonic.

        :param valid: The status of the license
        :type valid: bool
        :param email: The email of the user which the request was made, defaults to None
        :type email: str | None, optional
        :param licenseExpires: End of license date, defaults to None
        :type licenseExpires: str | None, optional
        :param trialExpires: End of trial date., defaults to None
        :type trialExpires: str | None, optional
        """

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
