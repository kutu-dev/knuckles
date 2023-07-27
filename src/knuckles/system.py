from .api import Api
from .models.system import License, SubsonicResponse


class System:
    """Class that contains all the methods needed to interact
    with the systems calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/system/>
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def ping(self) -> SubsonicResponse:
        """Calls to the "ping" endpoint of the API.

        Useful to test the status of the server.

        :return: An object with all the data received from the server.
        :rtype: SubsonicResponse
        """

        response = self.api.request("ping")

        return SubsonicResponse(**response)

    def get_license(self) -> License:
        """Calls to the "getLicense" endpoint of the API.

        :return: An object with all the information about the status of the license.
        :rtype: License
        """

        response = self.api.request("getLicense")["license"]

        return License(**response)
