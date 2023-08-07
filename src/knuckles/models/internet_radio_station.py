from typing import TYPE_CHECKING, Self

from ..exceptions import ResourceNotFound

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class InternetRadioStation:
    """Representation of all the data related to
    a internet radio station in Subsonic.
    """

    def __init__(
        self, subsonic: "Subsonic", id: str, name: str, streamUrl: str, homepageUrl: str
    ) -> None:
        """Representation of all the data related to
        a internet radio station in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param streamUrl: The id of the radio station.
        :type streamUrl: str
        :param streamUrl: The stream url of the radio station.
        :type streamUrl: str
        :param name: The name of the radio station.
        :type name: str
        :param homepageUrl: The url of the homepage of the radio station.
        :type homepageUrl: str
        """

        self.__subsonic = subsonic
        self.id = id
        self.name = name
        self.stream_url = streamUrl
        self.homepage_url = homepageUrl

    def generate(self) -> "InternetRadioStation | None":
        get_station = self.__subsonic.internet_radio.get_internet_radio_station(self.id)

        if get_station is None:
            raise ResourceNotFound(
                (
                    "Unable to generate internet radio station"
                    + "as it does not exist in the server"
                )
            )

        return get_station

    def create(self) -> Self:
        self.__subsonic.internet_radio.create_internet_radio_station(
            self.stream_url, self.name, self.homepage_url
        )

        return self

    def update(self) -> Self:
        self.__subsonic.internet_radio.update_internet_radio_station(
            self.id, self.stream_url, self.name, self.homepage_url
        )

        return self

    def delete(self) -> Self:
        self.__subsonic.internet_radio.delete_internet_radio_station(self.id)

        return self
