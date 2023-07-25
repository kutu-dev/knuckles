# Not fancy but does the job
from typing import TYPE_CHECKING, Any, Self

from knuckles.exceptions import AlbumOrArtistArgumentsInSong, VideoArgumentsInSong

if TYPE_CHECKING:
    from .subsonic import Subsonic

from datetime import datetime

from dateutil import parser


class SubsonicResponse:
    def __init__(
        self,
        status: str,
        version: str,
        type: str | None = None,
        serverVersion: str | None = None,
        openSubsonic: bool = False,
    ) -> None:
        self.status: str = status
        self.version: str = version
        self.type: str | None = type
        self.server_version: str | None = serverVersion
        self.open_subsonic: bool = openSubsonic


class License:
    def __init__(
        self,
        valid: bool,
        email: str | None = None,
        licenseExpires: str | None = None,
        trialExpires: str | None = None,
    ) -> None:
        self.valid: bool = valid
        self.email: str | None = email

        self.license_expires: datetime | None
        if licenseExpires is not None:
            self.license_expires = parser.parse(licenseExpires)
        else:
            self.license_expires = None

        self.trial_expires: datetime | None
        if trialExpires is not None:
            self.trial_expires = parser.parse(trialExpires)
        else:
            self.trial_expires = None

    def __bool__(self) -> bool:
        return self.valid


class CoverArt:
    def __init__(self, id: str) -> None:
        self.id: str = id


class Album:
    def __init__(self, id: str, name: str | None = None) -> None:
        self.id: str = id
        self.name: str | None = name


class Artist:
    def __init__(self, id: str, name: str | None = None) -> None:
        self.id: str = id
        self.name: str | None = name


class Song:
    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        title: str,
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
        # OpenSubsonic fields
        played: str | None = None,
    ) -> None:
        if isVideo or originalWidth is not None or originalHeight is not None:
            raise VideoArgumentsInSong(
                (
                    "A song shouldn't contain values valid for videos."
                    + "Did you mean: Video()?"
                )
            )

        if isDir:
            raise AlbumOrArtistArgumentsInSong(
                "'isDir' shouldn't be True. Did you mean: Album() or Artist()?"
            )

        self.__subsonic: "Subsonic" = subsonic
        self.id: str = id
        self.title: str = title
        self.parent: str | None = parent
        self.track: int | None = track
        self.year: int | None = year
        self.genre: str | None = genre
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

        self.album: Album | None = None
        if albumId is not None:
            self.album = Album(albumId, album)

        self.artist: Artist | None = None
        if artistId is not None:
            self.artist = Artist(artistId, artist)

        self.cover_art: CoverArt | None = None
        if coverArt is not None:
            self.cover_art = CoverArt(coverArt)

        self.created: datetime | None = None
        if created is not None:
            self.created = parser.parse(created)

        self.starred: datetime | None = None
        if starred is not None:
            self.starred = parser.parse(starred)

        self.played: datetime | None = None
        if played is not None:
            self.played = parser.parse(played)

    def generate(self) -> "Song":
        """Returns the function to the the same song with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., `foo = foo.generate()`.

        Returns:
            Song: The same object with updated data
        """

        return self.__subsonic.get_song(self.id)

    def star(self) -> Self:
        self.__subsonic.star_song(self.id)

        return self

    def unstar(self) -> Self:
        self.__subsonic.unstar_song(self.id)

        return self

    def set_rating(self, rating: int) -> Self:
        self.__subsonic.set_rating(self.id, rating)

        return self

    def remove_rating(self) -> Self:
        self.__subsonic.remove_rating(self.id)

        return self

    def scrobble(self, time: datetime, submission: bool = True) -> Self:
        self.__subsonic.scrobble(self.id, time, submission)

        return self


class ScanStatus:
    def __init__(self, scanning: bool, count: int) -> None:
        self.scanning: bool = scanning
        self.count: int = count


class ChatMessage:
    def __init__(self, username: str, time: int, message: str) -> None:
        self.username: str = username

        # Divide by 1000 as the Subsonic API return in milliseconds instead of seconds
        self.time: datetime = datetime.fromtimestamp(time / 1000)
        self.message: str = message


class Jukebox:
    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        currentIndex: int,
        playing: bool,
        gain: float,
        position: int,
        entry: list[dict[str, Any]] | None = None,
    ) -> None:
        self.current_index: int = currentIndex
        self.playing: bool = playing
        self.gain: float = gain
        self.position: int = position

        self.playlist: list[Song] | None = None
        if entry is None:
            return

        self.playlist = []

        for song in entry:
            self.playlist.append(Song(subsonic=subsonic, **song))
