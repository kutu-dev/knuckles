from typing import TYPE_CHECKING

from .api import Api
from .models.internet_radio_station import InternetRadioStation

if TYPE_CHECKING:
    from .subsonic import Subsonic


class InternetRadio:
    """Class that contains all the methods needed to interact
    with the internet radio calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/internet-radio/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_internet_radio_stations(
        self,
    ) -> list[InternetRadioStation]:
        """Calls the "getInternetRadioStation" endpoint of the API.

        :return: A list with all the internet radio stations.
        :rtype: list[InternetRadioStation]
        """

        response = self.api.request("getInternetRadioStations")[
            "internetRadioStations"
        ]["internetRadioStation"]

        return [InternetRadioStation(self.subsonic, **station) for station in response]

    def get_internet_radio_station(self, id: str) -> InternetRadioStation | None:
        """Using the "getInternetRadioStation" endpoint iterates over all the stations
        and find the one with the same ID.

        :param id: The ID of the station to find.
        :type id: str
        :return: The found internet radio station or None if no one is found.
        :rtype: InternetRadioStation | None
        """

        stations = self.get_internet_radio_stations()

        for station in stations:
            if station.id == id:
                return station

        return None

    def create_internet_radio_station(
        self, stream_url: str, name: str, homepage_url: str | None = None
    ) -> "Subsonic":
        """Calls the "createInternetRadioStation" endpoint of the API.

        :param stream_url: The stream url of the station.
        :type stream_url: str
        :param name: The name of the station.
        :type name: str
        :param homepage_url: The url of the homepage of the station, defaults to None.
        :type homepage_url: str | None, optional
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request(
            "createInternetRadioStation",
            {"streamUrl": stream_url, "name": name, "homepageUrl": homepage_url},
        )

        return self.subsonic

    def update_internet_radio_station(
        self, id: str, stream_url: str, name: str, homepage_url: str | None = None
    ) -> "Subsonic":
        """Calls the "updateInternetRadioStation" endpoint ot the API.

        :param id: The ID of the station to update.
        :type id: str
        :param stream_url: The new steam url of the station.
        :type stream_url: str
        :param name: The new name of the station.
        :type name: str
        :param homepage_url: The new url of the homepage of the station,
            defaults to None.
        :type homepage_url: str | None, optional
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request(
            "updateInternetRadioStation",
            {
                "id": id,
                "streamUrl": stream_url,
                "name": name,
                "homepageUrl": homepage_url,
            },
        )

        return self.subsonic

    def delete_internet_radio_station(self, id: str) -> "Subsonic":
        """Calls the "deleteInternetRadioStation" endpoint of the API.

        :param id: The ID of the station to delete
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("deleteInternetRadioStation", {"id": id})

        return self.subsonic
