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
        response = self.api.request("getInternetRadioStations")[
            "internetRadioStations"
        ]["internetRadioStation"]

        return [InternetRadioStation(self.subsonic, **station) for station in response]

    def get_internet_radio_station(self, id: str) -> InternetRadioStation | None:
        stations = self.get_internet_radio_stations()

        for station in stations:
            if station.id == id:
                return station

        return None

    def create_internet_radio_station(
        self, stream_url: str, name: str, homepage_url: str | None = None
    ) -> "Subsonic":
        self.api.request(
            "createInternetRadioStation",
            {"streamUrl": stream_url, "name": name, "homepageUrl": homepage_url},
        )

        return self.subsonic

    def update_internet_radio_station(
        self, id: str, stream_url: str, name: str, homepage_url: str | None = None
    ) -> "Subsonic":
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
        self.api.request("deleteInternetRadioStation", {"id": id})

        return self.subsonic
