from datetime import datetime
from typing import TYPE_CHECKING

from ._api import Api
from .exceptions import InvalidRatingNumber

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class MediaAnnotation:
    """Class that contains all the methods needed to interact with the
    [media annotations endpoints](https://opensubsonic.netlify.app/
    categories/media-annotation/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def star_song(self, song_id: str) -> "Subsonic":
        """Star a song from the server.

        Args:
            song_id: The ID of the song to star.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("star", {"id": song_id})

        return self.subsonic

    def star_album(self, album_id: str) -> "Subsonic":
        """Star an album from the server.

        Args:
            album_id: The ID of the album to star.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("star", {"albumId": album_id})

        return self.subsonic

    def star_artist(self, artist_id: str) -> "Subsonic":
        """Star an artist from the server.

        Args:
            artist_id: The ID of the artist to star.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("star", {"artistId": artist_id})

        return self.subsonic

    def unstar_song(self, song_id: str) -> "Subsonic":
        """Unstar a song from the server.

        Args:
            song_id: The ID of the song to unstar.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("unstar", {"id": song_id})

        return self.subsonic

    def unstar_album(self, album_id: str) -> "Subsonic":
        """Unstar an album from the server.

        Args:
            album_id: The ID of the album to unstar.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("unstar", {"albumId": album_id})

        return self.subsonic

    def unstar_artist(self, artist_id: str) -> "Subsonic":
        """Unstar an artist from the server.

        Args:
            artist_id: The ID of the artist to unstar.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("unstar", {"artistId": artist_id})

        return self.subsonic

    def set_rating(self, song_id: str, rating: int) -> "Subsonic":
        """The the rating of a song.

        Args:
            song_id: The ID of the song to set its rating.
            rating: The rating between 1 and 5 (inclusive) to set
                the rating of the song to.

        Raises:
            InvalidRatingNumber: Raised when a number that is not
                between 1 and 5 (inclusive) has been pass in into
                the `rating` parameter.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        if rating not in range(1, 6):
            raise InvalidRatingNumber(
                (
                    "Invalid rating number, "
                    + "only numbers between 1 and 5 (inclusive) are allowed"
                )
            )

        self.api.json_request("setRating", {"id": song_id, "rating": rating})

        return self.subsonic

    def remove_rating(self, song_id: str) -> "Subsonic":
        """Remove the rating entry of a song.

        Args:
            song_id: The ID of the song which entry should
                be removed.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("setRating", {"id": song_id, "rating": 0})

        return self.subsonic

    def scrobble(
        self, song_id: list[str], time: list[datetime], submission: bool = True
    ) -> "Subsonic":
        """Scrobble (register) that some song have been locally played or
        is being played.

        Args:
            song_id: The ID of the song to scrobble.
            time: How many times in second the song has been listened.
            submission: If true it will be registered that the song **was
                played**, if false the song will be scrobble as
                **now playing**.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """
        self.api.json_request(
            "scrobble",
            # Multiply by 1000 because the API uses
            # milliseconds instead of seconds for UNIX time
            {
                "id": song_id,
                "time": [int(seconds.timestamp()) * 1000 for seconds in time],
                "submission": submission,
            },
        )

        return self.subsonic
