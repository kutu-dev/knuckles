from typing import TYPE_CHECKING, Self

from ..exceptions import ResourceNotFound
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class InternetRadioStation(Model):
    """Object that holds all the info about a Internet radio station.

    Attributes:
        id (str): The ID of the Internet radio station.
        name (str): Then name of the Internet radio station.
        stream_url (str): The URL of the stream of the Internet radio station.
        homepage_url (str): The URl of the hompage of the Internet radio station.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        name: str,
        streamUrl: str,
        homepageUrl: str,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.stream_url = streamUrl
        self.homepage_url = homepageUrl

    def generate(self) -> "InternetRadioStation | None":
        """Return a new album object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
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
        """Create a new Internet radio station for the authenticated user
        with the same data of the object where this method is
        called.

        Returns:
            The object itself.
        """

        self._subsonic.internet_radio.create_internet_radio_station(
            self.stream_url, self.name, self.homepage_url
        )

        return self

    def update(self) -> Self:
        """Update the info about the Internet radio station using the
        current data of the object.

        Returns:
            The object itself.
        """

        self._subsonic.internet_radio.update_internet_radio_station(
            self.id, self.stream_url, self.name, self.homepage_url
        )

        return self

    def delete(self) -> Self:
        """Delete the Internet radio station entry from the server.

        Returns:
            The object itself.
        """

        self._subsonic.internet_radio.delete_internet_radio_station(self.id)

        return self
