from typing import TYPE_CHECKING, Any, Self

# Avoid circular import error
import knuckles.models._album as album_model_module
from knuckles.models._genre import Genre, ItemGenre

from ._artist import Artist
from ._contributor import Contributor
from ._cover_art import CoverArt
from ._model import Model
from ._replay_gain import ReplayGain

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from datetime import datetime

from dateutil import parser


class Song(Model):
    """Object that holds all the info about a song.

    Attributes:
        id (str): The ID of the song.
        title (str | None): The title of the song.
        parent (str | None): The ID of the parent of the song.
        track (int | None): The track
        year (int | None): The year when the song was released.
        genre (Genre | None): All the info related with the genre
            of the song.
        size (int | None): The size of the file of the song.
        content_type (str | None): The HTTP ContentType of the
            file of the song.
        suffix (str | None): The suffix of the filename of the
            file of the song.
        transcoded_content_type (str | None): The HTTP ContentType
            of the transcoded file of the song.
        transcoded_suffix (str | None): The suffix of the filename
            of the transcoded file of the song.
        duration (int | None): The duration in seconds of the song.
        bit_rate (int | None): The bit rate of the song.
        path (str | None): The path of the song.
        user_rating (int | None): The rating given to the song by
            the user.
        average_rating (float | None): The average rating of all the
            user for the song.
        play_count (int | None): The number of the times the song
            has been played.
        disc_number (int | None): The disc number of the song.
        type (str |  None): The type of media.
        bookmark_position (int | None): The position in seconds
            where the song is bookmarked for the authenticated user.
        album (Album | None): All the info related with the album
            of the song.
        artist (Artist | None): All the info related with the main
            artist of the song.
        cover_art (CoverArt | None): All the info related
            with the cover art of the song.
        created (datetime | None): The timestamp when the song
            was created.
        starred (datetime | None): The timestamp when the song
            was starred by the authenticated user if they have.
        played (datetime | None): The timestamp when the song
            was last played.
        bpm (int | None): The bpm of the song.
        comment (str | None): The comment of the song.
        sort_name (str | None): The sort name of the song.
        music_brainz_id (str | None): The ID of the MusicBrainz entry
            of the song.
        genres (list[ItemGenre | None): List that holds all the info
            about all the genres of the song.
        artists (list[Artist] | None): List that holds all the info
            about all the artists that made the song.
        display_artist (str | None): The display name of the artist
            of the song.
        album_artists (list[Artist] | None): List that holds all the info
            about all the artists that made the album where the song
            is from.
        display_album_artist (str | None): THe display name of the artist
            of the album of the song.
        contributors (list[Contributor] | None): List that holds all the
            info about all the contributors of the song.
        display_composer (str | None): The display name of the composer
            of the song.
        moods (list[str] | None): List off all the moods of the song.
        replay_gain (ReplayGain | None): All the info about the replay
            gain of the song.
        media_type (str | None): The type of media of the song.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        title: str | None = None,
        parent: str | None = None,
        isDir: bool | None = None,
        isVideo: bool | None = None,
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
        mediaType: str | None = None,
        **kwargs,
    ) -> None:
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
        self.media_type = mediaType

    def generate(self) -> "Song":
        """Return a new song object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.browsing.get_song(self.id)

    def star(self) -> Self:
        """Star the song for the authenticated user.

        Returns:
            The object itself.
        """

        self._subsonic.media_annotation.star_song(self.id)

        return self

    def unstar(self) -> Self:
        """Unstar the song for the authenticated user.

        Returns:
            The object itself.
        """

        self._subsonic.media_annotation.unstar_song(self.id)

        return self

    def set_rating(self, rating: int) -> Self:
        """Set the rating of the song.

        Args:
            rating: The new rating for the song.

        Returns:
            The object itself.
        """

        self._subsonic.media_annotation.set_rating(self.id, rating)

        return self

    def remove_rating(self) -> Self:
        """Remove the rating for the song.

        Returns:
            The object itself.
        """

        self._subsonic.media_annotation.remove_rating(self.id)

        return self

    def scrobble(self, time: datetime, submission: bool = True) -> Self:
        """Scrobble the song.

        Args:
            time: The timestamp when the song was scrobble:
            submission: If the scrobble is a request to a submission or
                it is a now playing entry.

        Returns:
            The object itself.
        """

        self._subsonic.media_annotation.scrobble([self.id], [time], submission)

        return self
