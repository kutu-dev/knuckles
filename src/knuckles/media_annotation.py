from datetime import datetime
from typing import TYPE_CHECKING

from .api import Api
from .exceptions import InvalidRatingNumber

if TYPE_CHECKING:
    from .subsonic import Subsonic


class MediaAnnotation:
    """Class that contains all the methods needed to interact
    with the media annotation calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/media-annotation/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def star_song(self, id_: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id_: The ID of a song to star.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("star", {"id": id_})

        return self.subsonic

    def star_album(self, id_: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id_: The ID of an album to star.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("star", {"albumId": id_})

        return self.subsonic

    def star_artist(self, id_: str) -> "Subsonic":
        """Calls the "star" endpoint of the API.

        :param id_: The ID of an artist to star.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("star", {"artistId": id_})

        return self.subsonic

    def unstar_song(self, id_: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id_: The ID of a song to unstar.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("unstar", {"id": id_})

        return self.subsonic

    def unstar_album(self, id_: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id_: The ID of an album to unstar.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("unstar", {"albumId": id_})

        return self.subsonic

    def unstar_artist(self, id_: str) -> "Subsonic":
        """Calls the "unstar" endpoint of the API.

        :param id_: The ID of an artist to unstar.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("unstar", {"artistId": id_})

        return self.subsonic

    def set_rating(self, id_: str, rating: int) -> "Subsonic":
        """Calls to the "setRating" endpoint of the API.

        :param id_: The ID of a song to set its rating.
        :type id_: str
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

        self.api.json_request("setRating", {"id": id_, "rating": rating})

        return self.subsonic

    def remove_rating(self, id_: str) -> "Subsonic":
        """Calls the "setRating" endpoint of the API with a rating of 0.

        :param id_: The ID of a song to set its rating.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("setRating", {"id": id_, "rating": 0})

        return self.subsonic

    def scrobble(
        self, id_: list[str], time: list[datetime], submission: bool = True
    ) -> "Subsonic":
        """Calls to the "scrobble" endpoint of the API

        :param id_: The list of song IDs to scrobble.
        :type id_: list[str]
        :param time: The time at which the song was listened to.
        :type time: datetime
        :param submission: If the scrobble is a submission
            or a "now playing" notification, defaults to True.
        :type submission: bool, optional
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request(
            "scrobble",
            # Multiply by 1000 because the API uses
            # milliseconds instead of seconds for UNIX time
            {
                "id": id_,
                "time": [int(seconds.timestamp()) * 1000 for seconds in time],
                "submission": submission,
            },
        )

        return self.subsonic
