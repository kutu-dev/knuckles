from typing import TYPE_CHECKING, Any

from dateutil import parser

# Avoid circular import error
import knuckles.models._song as song_model_module

from ._artist import Artist
from ._cover_art import CoverArt
from ._genre import ItemGenre
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class RecordLabel(Model):
    """Object that holds all the info about a record label.

    Attributes:
        name (str): The name of the record label.
    """

    def __init__(self, subsonic: "Subsonic", name: str) -> None:
        super().__init__(subsonic)

        self.name = name


class Disc(Model):
    """Object that holds all the info about a disc.

    Attributes:
        disc_number (int): The number of the disc.
        title (str): The title of the disc.
    """

    def __init__(self, subsonic: "Subsonic", disc: int, title: str) -> None:
        super().__init__(subsonic)

        self.disc_number = disc
        self.title = title


class ReleaseDate(Model):
    """Object that holds all the info about the release date of a media.

    Attributes:
        year (int): The year when it was released.
        month (int): The month when it was released.
        day (int): The day when it was released.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.year = year
        self.month = month
        self.day = day


class AlbumInfo(Model):
    """Object that holds all the info about the extra info of an album.

    Attributes:
        album_id (str): The ID of the album where the extra info is from.
        notes (str): Notes of the album.
        music_brainz_id (str | None): The music brainz ID of the album.
        last_fm_url (str | None): The last.fm URL of the album
        small_image_user (str | None): The URL of the small sized image of the album.
        medium_image_user (str | None): The URL of the medium sized image of the album.
        large_image_user (str | None): The URL of the large sized image of the album.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        album_id: str,
        notes: str | None = None,
        musicBrainzId: str | None = None,
        lastFmUrl: str | None = None,
        smallImageUrl: str | None = None,
        mediumImageUrl: str | None = None,
        largeImageUrl: str | None = None,
        **kargs,
    ) -> None:
        super().__init__(subsonic)

        self.album_id = album_id
        self.notes = notes
        self.music_brainz_id = musicBrainzId
        self.last_fm_url = lastFmUrl
        self.small_image_url = smallImageUrl
        self.medium_image_url = mediumImageUrl
        self.large_image_url = largeImageUrl

    def generate(self) -> "AlbumInfo":
        """Return a new album info object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.browsing.get_album_info(self.album_id)


class Album(Model):
    """Object that holds all the info of an album.

    Attributes:
        id (str): The ID of the album.
        parent (str | None): The ID of the parent media of the album.
        name (str | None): The name of the album.
        album (str | None): The name of the album (Can differ the `name` and
            `title` attributes, **not documented in the [OpenSubsonic Spec](ht
            tps://opensubsonic.netlify.app/docs/responses/albumid3/)).
        is_dir (bool | None): If the album is a directory.
        title (str | None): The name of the album (Can differ the `name` and
            `album` attributes, **not documented in the [OpenSubsonic Spec](ht
            tps://opensubsonic.netlify.app/docs/responses/albumid3/)).
        artist (Artist | None): The artist of the album.
        cover_art (CoverArt): All the info about the cover art of the album.
        song_count (int | None): The number of songs inside the album.
        duration (int | None): The total duration of the album in seconds.
        play_count (int | None): The times the album has been played.
        created (datetime | None): The timestamp when the album was created.
        starred (datetime | None): The timestamp when the album was starred if
            it is.
        year (int | None): The year when the album was released.
        genre (str | None): The genre of the album.
        played (datetime | None): The timestamp when the album was played.
        user_rating (int | None): The rating from 0 to 5 (inclusive) that the
            used has given to the album if it is rated.
        songs (list[Song] | None): The list of songs that the album contains.
        info (AlbumInfo | None): Extra info about the album.
        record_labels (list[RecordLabel] | None): List of all the record labels
            that have licensed the album.
        music_brainz_id (str | None): The ID of the MusicBrainz database entry
            of the album.
        genres (list[ItemGenre] | None): List of all the genres that the album
            has.
        artists (list[Artist] | None): List of all the artists involved with
            the album.
        display_artist (str | None): String that condense all the artists
            involved with the album.
        release_types (list[str] | None): The types of album that the
            album is.
        moods (list[str] | None): List of all the moods that the album
            has.
        sort_name (str | None): The name of the album used for sorting.
        original_release_date (ReleaseDate | None): The original release date
            of the album.
        release_date (ReleaseDate | None): The release date of the album.
        is_compilation (bool | None): If the album is a compilation or not.
        discs (list[Disc] | None):
    """

    def __init__(
        self,
        subsonic: "Subsonic",
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
        recordLabels: list[dict[str, Any]] | None = None,
        musicBrainzId: str | None = None,
        genres: list[dict[str, Any]] | None = None,
        artists: list[dict[str, Any]] | None = None,
        displayArtist: str | None = None,
        releaseTypes: list[str] | None = None,
        moods: list[str] | None = None,
        sortName: str | None = None,
        originalReleaseDate: dict[str, Any] | None = None,
        releaseDate: dict[str, Any] | None = None,
        isCompilation: bool | None = None,
        discTitles: list[dict[str, Any]] | None = None,
        **kargs,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.parent = parent
        self.album = album
        self.name = name
        self.is_dir = isDir
        self.title = title
        self.artist = Artist(self._subsonic, artistId, artist) if artistId else None
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
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
            [song_model_module.Song(self._subsonic, **song_data) for song_data in song]
            if song
            else None
        )
        self.info: AlbumInfo | None = None
        self.record_labels = (
            [
                RecordLabel(self._subsonic, **record_label)
                for record_label in recordLabels
            ]
            if recordLabels
            else None
        )
        self.music_brainz_id = musicBrainzId
        self.genres = (
            [ItemGenre(self._subsonic, **genre) for genre in genres] if genres else None
        )
        self.artists = (
            [Artist(self._subsonic, **artist) for artist in artists]
            if artists
            else None
        )
        self.display_artist = displayArtist
        self.release_types = releaseTypes
        self.moods = moods
        self.sort_name = sortName
        self.original_release_date = (
            ReleaseDate(self._subsonic, **originalReleaseDate)
            if originalReleaseDate
            else None
        )
        self.release_date = (
            ReleaseDate(self._subsonic, **releaseDate) if releaseDate else None
        )
        self.is_compilation = isCompilation
        self.discs = (
            [Disc(self._subsonic, **disc) for disc in discTitles]
            if discTitles
            else None
        )

    def generate(self) -> "Album":
        """Return a new album object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        new_album = self._subsonic.browsing.get_album(self.id)
        new_album.get_album_info()

        return new_album

    def get_album_info(self) -> AlbumInfo:
        """Get all the extra info about the album, it's
        set to the `info` attribute of the object.

        Returns:
            The extra info returned by the server.
        """

        self.info = self._subsonic.browsing.get_album_info(self.id)

        return self.info
