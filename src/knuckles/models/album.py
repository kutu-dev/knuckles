from typing import TYPE_CHECKING, Any

from dateutil import parser

import knuckles.models.song as song_model

from ..models.artist import Artist
from ..models.cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class AlbumInfo:
    """Representation of all the data related to an album info in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        album_id: str,
        # Subsonic fields
        notes: str,
        musicBrainzId: str | None,
        lastFmUrl: str | None,
        smallImageUrl: str | None,
        mediumImageUrl: str | None,
        largeImageUrl: str | None,
    ) -> None:
        """Representation of all the data related to an album info in Subsonic.
        :param subsonic:The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param album_id: The ID3 of the album associated with the info.
        :type album_id: str
        :param notes: A note for the album.
        :type notes: str
        :param musicBrainzId:The ID in music Brainz of the album.
        :type musicBrainzId: str
        :param smallImageUrl: An URL to the small size cover image of the album.
        :type smallImageUrl: str
        :param mediumImageUrl: An URL to the medium size cover image of the album.
        :type mediumImageUrl: str
        :param largeImageUrl: An URL to the large size cover image of the album.
        :type largeImageUrl: str
        """

        self.__subsonic = subsonic
        self.album_id = album_id
        self.notes = notes
        self.music_brainz_id = musicBrainzId
        self.last_fm_url = lastFmUrl
        self.small_image_url = smallImageUrl
        self.medium_image_url = mediumImageUrl
        self.large_image_url = largeImageUrl

    def generate(self) -> "AlbumInfo":
        """Return a new album info with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: AlbumInfo
        """

        return self.__subsonic.browsing.get_album_info(self.album_id)


# TODO Unfinished
class Album:
    """Representation of all the data related to an album in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        parent: str | None = None,
        album: str | None = None,
        title: str | None = None,
        name: str | None = None,
        isDir: bool | None = None,
        artist: str | None = None,
        artistId: str | None = None,
        coverArt: str | None = None,
        songCount: int | None = None,
        duration: int | None = None,
        playCount: int | None = None,
        created: str | None = None,
        starred: str | None = None,
        year: int | None = None,
        genre: str | None = None,
        played: str | None = None,
        userRating: int | None = None,
        song: list[dict[str, Any]] | None = None,
    ) -> None:
        self.__subsonic = subsonic
        self.id = id
        self.parent = parent
        self.album = album
        self.name = name
        self.is_dir = isDir
        self.title = title
        self.artist = Artist(self.__subsonic, artistId, artist) if artistId else None
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.song_count = songCount
        self.duration = duration
        self.play_count = playCount
        self.created = parser.parse(created) if created else None
        self.starred = parser.parse(starred) if starred else None
        self.year = year
        self.genre = genre
        self.played = parser.parse(played) if played else None
        self.user_rating = userRating
        self.songs = (
            [song_model.Song(self.__subsonic, **song_data) for song_data in song]
            if song
            else None
        )
        self.info: AlbumInfo | None = None

    def generate(self) -> "Album":
        """Return a new album with all the data updated from the API,
        using the endpoints that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: Album
        """

        new_album = self.__subsonic.browsing.get_album(self.id)
        new_album.get_album_info()

        return new_album

    def get_album_info(self) -> AlbumInfo:
        """Returns the extra info given by the "getAlbumInfo2" endpoint,
        also sets it in the info property of the model.

        :return: An AlbumInfo object with all the extra info given by the API.
        :rtype: AlbumInfo
        """

        self.info = self.__subsonic.browsing.get_album_info(self.id)

        return self.info
