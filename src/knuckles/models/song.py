from typing import TYPE_CHECKING, Any, Self

# Avoid circular import error
import knuckles.models.album as album_model_module
from knuckles.models.genre import Genre, ItemGenre

from .artist import Artist
from .cover_art import CoverArt
from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from datetime import datetime

from dateutil import parser


class Contributor(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        role: str,
        artist: Artist,
        subRole: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.role = role
        self.subrole = subRole
        self.artist = artist


class ReplayGain(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        trackGain: str | None = None,
        albumGain: str | None = None,
        trackPeak: str | None = None,
        albumPeak: str | None = None,
        baseGain: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.track_gain = trackGain
        self.album_gain = albumGain
        self.track_peak = trackPeak
        self.album_peak = albumPeak
        self.base_gain = baseGain


class Song(Model):
    """Representation of all the data related to a song in Subsonic."""

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        title: str | None = None,
        isDir: bool = False,
        parent: str | None = None,
        album: str | None = None,
        artist: str | None = None,
        track: int | None = None,
        year: int | None = None,
        genre: str | None = None,
        coverArt: str | None = None,
        size: int | None = None,
        contentType: str | None = None,
        suffix: str | None = None,
        transcodedContentType: str | None = None,
        transcodedSuffix: str | None = None,
        duration: int | None = None,
        bitRate: int | None = None,
        path: str | None = None,
        isVideo: bool = False,
        userRating: int | None = None,
        averageRating: float | None = None,
        playCount: int | None = None,
        discNumber: int | None = None,
        created: str | None = None,
        starred: str | None = None,
        albumId: str | None = None,
        artistId: str | None = None,
        type: str | None = None,
        bookmarkPosition: int | None = None,
        originalWidth: None = None,
        originalHeight: None = None,
        played: str | None = None,
        bpm: int | None = None,
        comment: str | None = None,
        sortName: str | None = None,
        musicBrainzId: str | None = None,
        genres: list[dict[str, Any]] | None = None,
        artists: list[dict[str, Any]] | None = None,
        displayArtist: str | None = None,
        albumArtists: list[dict[str, Any]] | None = None,
        displayAlbumArtist: str | None = None,
        contributors: list[dict[str, Any]] | None = None,
        displayComposer: str | None = None,
        moods: list[str] | None = None,
        replayGain: dict[str, Any] | None = None,
    ) -> None:
        """Representation of all the data related to song in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The id of the media.
        :type id: str
        :param title:  The song name, defaults to None.
        :type title: str | None, optional
        :param isDir: If the media is a dir (should always be False), defaults to False.
        :type isDir: bool, optional
        :param parent: The ID of the parent folder, defaults to None.
        :type parent: str | None, optional
        :param album: The album name, defaults to None.
        :type album: str | None, optional
        :param artist: The artist name, defaults to None.
        :type artist: str | None, optional
        :param track: The track number, defaults to None.
        :type track: int | None, optional
        :param year: The media year, defaults to None.
        :type year: int | None, optional
        :param genre: The media genre, defaults to None.
        :type genre: str | None, optional
        :param coverArt: A covertArt id, defaults to None.
        :type coverArt: str | None, optional
        :param size: A file size of the media, defaults to None.
        :type size: int | None, optional
        :param contentType: The mimeType of the media, defaults to None.
        :type contentType: str | None, optional
        :param suffix: The file suffix of the media, defaults to None.
        :type suffix: str | None, optional
        :param transcodedContentType: The transcoded mediaType
            if transcoding should happen, defaults to None.
        :type transcodedContentType: str | None, optional
        :param transcodedSuffix: The file suffix of the transcoded media,
            defaults to None.
        :type transcodedSuffix: str | None, optional
        :param duration: The duration of the media in seconds, defaults to None.
        :type duration: int | None, optional
        :param bitRate: The bitrate of the media, defaults to None.
        :type bitRate: int | None, optional
        :param path: The full path of the media, defaults to None.
        :type path: str | None, optional
        :param isVideo: If the media is a video (should always be false),
            defaults to False.
        :type isVideo: bool, optional
        :param userRating: The user rating of the media (between 1 and 5, inclusive),
            defaults to None.
        :type userRating: int | None, optional
        :param averageRating: The average rating of the media
            (between 1.0 and 5.0 inclusive), defaults to None.
        :type averageRating: float | None, optional
        :param playCount: The play count, defaults to None.
        :type playCount: int | None, optional
        :param discNumber: The disc number, defaults to None.
        :type discNumber: int | None, optional
        :param created: Date the media was created, defaults to None.
        :type created: str | None, optional
        :param starred: Date the media was starred, defaults to None.
        :type starred: str | None, optional
        :param albumId: The corresponding album id, defaults to None.
        :type albumId: str | None, optional
        :param artistId: The corresponding artist id, defaults to None.
        :type artistId: str | None, optional
        :param type: The media type, defaults to None.
        :type type: str | None, optional
        :param bookmarkPosition: The bookmark position in seconds, defaults to None.
        :type bookmarkPosition: int | None, optional
        :param originalWidth: The video original Width, defaults to None.
        :type originalWidth: None, optional
        :param originalHeight: The video original Height, defaults to None.
        :type originalHeight: None, optional
        :param played: Date the album was last played (OpenSubsonic), defaults to None.
        :type played: str | None, optional
        :raises VideoArgumentsInSong: Raised if arguments only valid
            for videos are passed in.
        :raises AlbumOrArtistArgumentsInSong: Raised if arguments only valid
            for albums or artists are passed in.
        """

        super().__init__(subsonic)

        self.id: str = id
        self.title: str | None = title
        self.parent: str | None = parent
        self.track: int | None = track
        self.year: int | None = year
        self.genre = Genre(self._subsonic, genre) if genre else None
        self.size: int | None = size
        self.content_type: str | None = contentType
        self.suffix: str | None = suffix
        self.transcoded_content_type: str | None = transcodedContentType
        self.transcoded_suffix: str | None = transcodedSuffix
        self.duration: int | None = duration
        self.bit_rate: int | None = bitRate
        self.path: str | None = path
        self.user_rating: int | None = userRating
        self.average_rating: float | None = averageRating
        self.play_count: int | None = playCount
        self.disc_number: int | None = discNumber
        self.type: str | None = type
        self.bookmark_position: int | None = bookmarkPosition
        self.album = (
            album_model_module.Album(self._subsonic, albumId, name=album)
            if albumId
            else None
        )
        self.artist = Artist(self._subsonic, artistId, artist) if artistId else None
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
        self.created = parser.parse(created) if created else None
        self.starred = parser.parse(starred) if starred else None
        self.played = parser.parse(played) if played else None
        self.bpm = bpm
        self.comment = comment
        self.sort_name = sortName
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
        self.album_artists = (
            [Artist(self._subsonic, **artist) for artist in albumArtists]
            if albumArtists
            else None
        )
        self.display_album_artist = displayAlbumArtist
        self.contributors = (
            [Contributor(self._subsonic, **contributor) for contributor in contributors]
            if contributors
            else None
        )
        self.display_composer = displayComposer
        self.moods = moods
        self.replay_gain = (
            ReplayGain(self._subsonic, **replayGain) if replayGain else None
        )

    def generate(self) -> "Song":
        """Return a new song with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new song object with all the data updated.
        :rtype: Song
        """

        return self._subsonic.browsing.get_song(self.id)

    def star(self) -> Self:
        """Calls the "star" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.media_annotation.star_song(self.id)

        return self

    def unstar(self) -> Self:
        """Calls the "unstar" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.media_annotation.unstar_song(self.id)

        return self

    def set_rating(self, rating: int) -> Self:
        """Calls the "setRating" endpoint of the API.

        :param rating: The rating between 1 and 5 (inclusive).
        :type rating: int
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.media_annotation.set_rating(self.id, rating)

        return self

    def remove_rating(self) -> Self:
        """Calls the "setRating" endpoint of the API with a rating of 0.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.media_annotation.remove_rating(self.id)

        return self

    def scrobble(self, time: datetime, submission: bool = True) -> Self:
        """Calls the "scrobble" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.media_annotation.scrobble([self.id], [time], submission)

        return self
