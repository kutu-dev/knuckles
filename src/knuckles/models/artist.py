from typing import TYPE_CHECKING, Any

# Avoid circular import error
import knuckles.models.album as album_model_module

from .cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from dateutil import parser


class ArtistInfo:
    """Representation of all the data related to an artist info in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        artist_id: str,
        # Subsonic fields
        biography: str,
        musicBrainzId: str | None,
        lastFmUrl: str | None,
        smallImageUrl: str | None,
        mediumImageUrl: str | None,
        largeImageUrl: str | None,
        similarArtist: list[dict[str, Any]] | None = None,
    ) -> None:
        """Representation of all the data related to an album info in Subsonic.
        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param artist_id: The ID3 of the artist associated with the info.
        :type artist_id: str
        :param biography: A biography for the album.
        :type biography: str
        :param musicBrainzId:The ID in music Brainz of the album.
        :type musicBrainzId: str
        :param smallImageUrl: An URL to the small size cover image of the artist.
        :type smallImageUrl: str
        :param mediumImageUrl: An URL to the medium size cover image of the artist.
        :type mediumImageUrl: str
        :param largeImageUrl: An URL to the large size cover image of the artist.
        :type largeImageUrl: str
        :param similarArtist: A list with all the similar artists.
        :type similarArtist: list[str, Any]
        """

        self.__subsonic = subsonic
        self.artist_id = artist_id
        self.biography = biography
        self.music_brainz_id = musicBrainzId
        self.last_fm_url = lastFmUrl
        self.small_image_url = smallImageUrl
        self.medium_image_url = mediumImageUrl
        self.large_image_url = largeImageUrl
        self.similar_artists = (
            [Artist(self.__subsonic, **artist) for artist in similarArtist]
            if similarArtist
            else None
        )

    def generate(self) -> "ArtistInfo":
        """Return a new artist info with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: ArtistInfo
        """

        return self.__subsonic.browsing.get_artist_info(self.artist_id)


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
        self.artist_image_url = artistImageUrl
        self.album_count = albumCount
        self.starred = parser.parse(starred) if starred else None
        self.user_rating = userRating
        self.average_rating = averageRating
        self.albums = (
            [
                album_model_module.Album(self.__subsonic, **album_data)
                for album_data in album
            ]
            if album
            else None
        )
        self.info: ArtistInfo | None = None

    def generate(self) -> "Artist":
        """Return a new artist with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: Artist
        """

        new_artist = self.__subsonic.browsing.get_artist(self.id)
        new_artist.get_artist_info()

        return new_artist

    def get_artist_info(self) -> ArtistInfo:
        """Returns the extra info given by the "getAlbumInfo2" endpoint,
        also sets it in the info property of the model.

        :return: An AlbumInfo object with all the extra info given by the API.
        :rtype: AlbumInfo
        """

        self.info = self.__subsonic.browsing.get_artist_info(self.id)

        return self.info
