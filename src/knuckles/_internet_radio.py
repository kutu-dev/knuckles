from typing import TYPE_CHECKING

from ._api import Api
from .models._internet_radio_station import InternetRadioStation

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class InternetRadio:
    """Class that contains all the methods needed to interact with the
    [internet radio endpoints](https://opensubsonic.netlify.app/
    categories/internet-radio) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_internet_radio_stations(
        self,
    ) -> list[InternetRadioStation]:
        """Get all the internet radio stations available in the server.

        Returns:
            A list with all the reported internet radio stations.
        """

        response = self.api.json_request("getInternetRadioStations")[
            "internetRadioStations"
        ]["internetRadioStation"]

        return [InternetRadioStation(self.subsonic, **station) for station in response]

    def get_internet_radio_station(
        self, internet_radio_station_id: str
    ) -> InternetRadioStation | None:
        """Get all the info related with a internet radio station.

        Args:
            internet_radio_station_id: The ID of the internet radio station
                to get its info.

        Returns:
            An object that contains all the info about the requested
                internet radio station.
        """

        stations = self.get_internet_radio_stations()

        for station in stations:
            if station.id == internet_radio_station_id:
                return station

        return None

    def create_internet_radio_station(
        self, stream_url: str, name: str, homepage_url: str | None = None
    ) -> "Subsonic":
        """Create a new internet radio station.

        Args:
            stream_url: The URL of the stream to be added to the
                internet radio station.
            name: The name of the new created internet radio station.
            homepage_url: An URL for the homepage of the internet
                radio station.

        Returns:
            An object that holds all the data about the new created
                internet radio station.
        """

        self.api.json_request(
            "createInternetRadioStation",
            {"streamUrl": stream_url, "name": name, "homepageUrl": homepage_url},
        )

        return self.subsonic

    def update_internet_radio_station(
        self,
        internet_radio_station_id: str,
        stream_url: str,
        name: str,
        homepage_url: str | None = None,
    ) -> "Subsonic":
        """Update the data of an internet radio station.

        Args:
            internet_radio_station_id: The ID of the internet radio station
                to edit its data.
            stream_url: A new stream URL for the internet radio station.
            name: a new name for the internet radio station.
            homepage_url: A new homepage URL for the internet radio
                station.

        Returns:
            An object that holds all the data about the new updated
                internet radio station.
        """
        self.api.json_request(
            "updateInternetRadioStation",
            {
                "id": internet_radio_station_id,
                "streamUrl": stream_url,
                "name": name,
                "homepageUrl": homepage_url,
            },
        )

        return self.subsonic

    def delete_internet_radio_station(
        self, internet_radio_station_id: str
    ) -> "Subsonic":
        """Delete an internet radio station.

        Args:
            internet_radio_station_id: The ID of the internet radio station
                to delete.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """
        self.api.json_request(
            "deleteInternetRadioStation", {"id": internet_radio_station_id}
        )

        return self.subsonic
