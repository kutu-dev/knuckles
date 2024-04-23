from typing import TYPE_CHECKING, Self

from ..exceptions import ResourceNotFound
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class InternetRadioStation(Model):
    """Representation of all the data related to
    an internet radio station in Subsonic.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        name: str,
        streamUrl: str,
        homepageUrl: str,
    ) -> None:
        """Representation of all the data related to
        an internet radio station in Subsonic.

        :param id: The id of the radio station.
        :type streamUrl: str
        :param name: The name of the radio station.
        :type name: str
        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param streamUrl: The stream url of the radio station.
        :type streamUrl: str
        :param homepageUrl: The url of the homepage of the radio station.
        :type homepageUrl: str
        """

        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.stream_url = streamUrl
        self.homepage_url = homepageUrl

    def generate(self) -> "InternetRadioStation | None":
        """Return a new internet radio station with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new internet radio station object with all the data updated.
        :rtype: InternetRadioStation
        """

        get_station = self._subsonic.internet_radio.get_internet_radio_station(self.id)

        if get_station is None:
            raise ResourceNotFound(
                (
                    "Unable to generate internet radio station"
                    + "as it does not exist in the server"
                )
            )

        return get_station

    def create(self) -> Self:
        """Calls the "createInternetRadioStation" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.internet_radio.create_internet_radio_station(
            self.stream_url, self.name, self.homepage_url
        )

        return self

    def update(self) -> Self:
        """Calls the "updateInternetRadioStation" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.internet_radio.update_internet_radio_station(
            self.id, self.stream_url, self.name, self.homepage_url
        )

        return self

    def delete(self) -> Self:
        """Calls the "deleteInternetRadioStation" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.internet_radio.delete_internet_radio_station(self.id)

        return self
