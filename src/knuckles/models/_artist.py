from typing import TYPE_CHECKING, Any

# Avoid circular import error
import knuckles.models._album as album_model_module

from ._cover_art import CoverArt
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class ArtistInfo(Model):
    """Object that holds all the extra info of an artist.

    Attributes:
        artist_id (str): The ID of the artist.
        biography (str): The biography of an artist.
        music_brainz_id (str | None): The ID of the MusicBrainz database
            entry of the artist.
        last_fm_url (str | None): The last.fm URL of the artist.
        small_image_url (str | None): The URL of the small sized image of
            the artist.
        medium_image_url (str | None): The URL of the medium sized image
            of the artist.
        large_image_url (str | None): The URL of the large sized image
            of the artist.
        similar_artists (list[Artist] | None): A list that contains the
            all the info about similar artists.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        artist_id: str,
        biography: str,
        musicBrainzId: str | None,
        lastFmUrl: str | None,
        smallImageUrl: str | None,
        mediumImageUrl: str | None,
        largeImageUrl: str | None,
        similarArtist: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(subsonic)

        self.artist_id = artist_id
        self.biography = biography
        self.music_brainz_id = musicBrainzId
        self.last_fm_url = lastFmUrl
        self.small_image_url = smallImageUrl
        self.medium_image_url = mediumImageUrl
        self.large_image_url = largeImageUrl
        self.similar_artists = (
            [Artist(self._subsonic, **artist) for artist in similarArtist]
            if similarArtist
            else None
        )

    def generate(self) -> "ArtistInfo":
        """Return a new artist info with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        Returns:
            A new object with the updated model.
        """

        return self._subsonic.browsing.get_artist_info(self.artist_id)


class Artist(Model):
    """Object that holds all the info of an artist.

    Attributes:
        id (str): The ID of the artist.
        name (str | None): The name of the artist.
        cover_art (CoverArt | None): The cover art associated with the artist.
        artist_image_url (str | None): The URL of the image of the artist.
        album_count (int | None): The number of albums created by the artist.
        starred (datetime | None): The timestamp when the artist was starred if
            it is.
        user_rating (int | None): The rating from 0 to 5 (inclusive) that the
            used has given to the artist if it is rated.
        average_rating (float | None): The average rating given by all the
            users.
        albums (list[Album] | None): A list that holds all the info about
            all the albums created by the artist.
        info (ArtistInfo | None): All the extra info about the artist.
        music_brainz_id (str | None): The ID of the MusicBrainz database entry
            of the artist.
        sort_name (str | None): The sort name of the artist.
        roles (list[str] | None): List with all the roles the artist has been
            in.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        name: str | None = None,
        coverArt: str | None = None,
        albumCount: int | None = None,
        artistImageUrl: str | None = None,
        starred: str | None = None,
        userRating: int | None = None,
        averageRating: float | None = None,
        album: list[dict[str, Any]] | None = None,
        musicBrainzId: str | None = None,
        sortName: str | None = None,
        roles: list[str] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
        self.artist_image_url = artistImageUrl
        self.album_count = albumCount
        self.starred = parser.parse(starred) if starred else None
        self.user_rating = userRating
        self.average_rating = averageRating
        self.albums = (
            [
                album_model_module.Album(self._subsonic, **album_data)
                for album_data in album
            ]
            if album
            else None
        )
        self.info: ArtistInfo | None = None
        self.music_brainz_id = musicBrainzId
        self.sort_name = sortName
        self.roles = roles

    def generate(self) -> "Artist":
        """Return a new artist info with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        Returns:
            A new object with the updated model.
        """

        new_artist = self._subsonic.browsing.get_artist(self.id)
        new_artist.get_artist_info()

        return new_artist

    def get_artist_info(self) -> ArtistInfo:
        """Get all the extra info about the artist, it's
        set to the `info` attribute of the object.

        Returns:
            The extra info returned by the server.
        """

        self.info = self._subsonic.browsing.get_artist_info(self.id)

        return self.info
