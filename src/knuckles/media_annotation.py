from datetime import datetime
from typing import TYPE_CHECKING

from .api import Api
from .exceptions import InvalidRatingNumber

if TYPE_CHECKING:
    from .subsonic import Subsonic


class MediaAnnotation:
    """Class that contains all the methods needed to interact
    with the media annotation calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/media-annotation/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def star_song(self, id: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id: The ID of a song to star.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("star", {"id": id})

        return self.subsonic

    def star_album(self, id: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id: The ID of a album to star.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("star", {"albumId": id})

        return self.subsonic

    def star_artist(self, id: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id: The ID of a artist to star.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("star", {"artistId": id})

        return self.subsonic

    def unstar_song(self, id: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id: The ID of a song to unstar.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("unstar", {"id": id})

        return self.subsonic

    def unstar_album(self, id: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id: The ID of a album to unstar.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("unstar", {"albumId": id})

        return self.subsonic

    def unstar_artist(self, id: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id: The ID of a artist to unstar.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("unstar", {"artistId": id})

        return self.subsonic

    def set_rating(self, id: str, rating: int) -> "Subsonic":
        """Calls to the "setRating" endpoint of the API.

        :param id: The ID of a song to set its rating.
        :type id: str
        :param rating: The rating to set. It should be a number
            between 1 and 5 (inclusive).
        :type rating: int
        :raises InvalidRatingNumber: Raised if the given rating number
            isn't in the valid range.
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        if rating not in range(1, 6):
            raise InvalidRatingNumber(
                (
                    "Invalid rating number, "
                    + "only numbers between 1 and 5 (inclusive) are allowed"
                )
            )

        self.api.request("setRating", {"id": id, "rating": rating})

        return self.subsonic

    def remove_rating(self, id: str) -> "Subsonic":
        """Calls the "setRating" endpoint of the API with a rating of 0.

        :param id: The ID of a song to set its rating.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("setRating", {"id": id, "rating": 0})

        return self.subsonic

    def scrobble(
        self, id: list[str], time: datetime, submission: bool = True
    ) -> "Subsonic":
        """Calls to the "scrobble" endpoint of the API

        :param id: The list of song IDs to scrobble.
        :type id: list[str]
        :param time: The time at which the song was listened to.
        :type time: datetime
        :param submission: If the scrobble is a submission
            or a "now playing" notification, defaults to True.
        :type submission: bool, optional
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request(
            "scrobble",
            # Multiply by 1000 because the API uses
            # milliseconds instead of seconds for UNIX time
            {"id": id, "time": int(time.timestamp() * 1000), "submission": submission},
        )

        return self.subsonic
