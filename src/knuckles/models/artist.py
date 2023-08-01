# TODO Unfinished
from typing import Any, TYPE_CHECKING

import knuckles.models.album as album_model
from knuckles.models.cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic
from dateutil import parser


class Artist:
    """Representation of all the data related to an artist in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        name: str | None = None,
        coverArt: str | None = None,
        albumCount: int | None = None,
        artistImageUrl: str | None = None,
        starred: str | None = None,
        userRating: int | None = None,
        averageRating: float | None = None,
        album: list[dict[str, Any]] | None = None,
    ) -> None:
        """Representation of all the data related to an artist in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The ID of the artist.
        :type id: str
        :param name: The name of the artist.
        :type name: str
        :param coverArt: The ID of the cover art of the artist.
        :type coverArt: str
        :param albumCount: The number of albums that the artist has.
        :type albumCount: int
        :param artistImageUrl: A URL to an image of the artist.
        :type artistImageUrl: str
        :param starred: The time when the artist was starred.
        :type starred: str
        :param userRating: The rating of the authenticated user.
        :type userRating: int
        :param averageRating: The average rating of all the users.
        :type averageRating: float
        :param album: A list with all the albums made by the artist.
        :type album: list[dict[str, Any]]
        """

        self.__subsonic = subsonic
        self.id = id
        self.name = name
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.album_count = albumCount
        self.artist_image_url = artistImageUrl
        self.starred = parser.parse(starred) if starred else None
        self.user_rating = userRating
        self.average_rating = averageRating
        self.albums = (
            [album_model.Album(self.__subsonic, **album_data) for album_data in album]
            if album
            else None
        )

    def generate(self) -> "Artist":
        """Return a new artist with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: Artist
        """

        new_artist = self.__subsonic.browsing.get_artist(self.id)

        return new_artist
