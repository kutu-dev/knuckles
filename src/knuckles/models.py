# Not fancy but does the job
from typing import TYPE_CHECKING, Any, Self

from knuckles.exceptions import AlbumOrArtistArgumentsInSong, VideoArgumentsInSong

if TYPE_CHECKING:
    from .subsonic import Subsonic

from datetime import datetime

from dateutil import parser


class SubsonicResponse:
    """Representation of the generic successful response data
    in a request to the API.
    """

    def __init__(
        self,
        status: str,
        version: str,
        type: str | None = None,
        serverVersion: str | None = None,
        openSubsonic: bool = False,
    ) -> None:
        """Representation of the generic successful response data
        in a request to the API.

        Transform all the data in camelCase to snake_case.

        :param status: The command result. It can be "ok" or "failed".
        :type status: str
        :param version: The server supported Subsonic API version.
        :type version: str
        :param type: The server actual name (OpenSubsonic), defaults to None
        :type type: str | None, optional
        :param serverVersion: The server actual version (OpenSubsonic), defaults to None
        :type serverVersion: str | None, optional
        :param openSubsonic: The support of the OpenSubsonic v1 specifications,
            defaults to False
        :type openSubsonic: bool, optional
        """

        self.status: str = status
        self.version: str = version
        self.type: str | None = type
        self.server_version: str | None = serverVersion
        self.open_subsonic: bool = openSubsonic


class License:
    """Representation of the license related data in Subsonic."""

    def __init__(
        self,
        valid: bool,
        email: str | None = None,
        licenseExpires: str | None = None,
        trialExpires: str | None = None,
    ) -> None:
        """Representation of the license related data in Subsonic.

        :param valid: The status of the license
        :type valid: bool
        :param email: The email of the user which the request was made, defaults to None
        :type email: str | None, optional
        :param licenseExpires: End of license date, defaults to None
        :type licenseExpires: str | None, optional
        :param trialExpires: End of trial date., defaults to None
        :type trialExpires: str | None, optional
        """

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


#! Unfinished
class CoverArt:
    """Representation of all the data related to cover arts in Subsonic."""

    def __init__(self, id: str) -> None:
        """Representation of all the data related to cover arts in Subsonic.

        :param id: The ID of the cover art.
        :type id: str
        """

        self.id: str = id


#! Unfinished
class Album:
    """Representation of all the data related to albums in Subsonic."""

    def __init__(self, id: str, name: str | None = None) -> None:
        self.id: str = id
        self.name: str | None = name


#! Unfinisehd
class Artist:
    """Representation of all the data related to artist in Subsonic."""

    def __init__(self, id: str, name: str | None = None) -> None:
        self.id: str = id
        self.name: str | None = name


class Song:
    """Representation of all the data related to song in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
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
        # OpenSubsonic fields
        played: str | None = None,
    ) -> None:
        """Representation of all the data related to song in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The id of the media.
        :type id: str
        :param title:  The song name., defaults to None.
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
        self.title: str | None = title
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
        with immutability, e.g., foo = foo.generate().

        :return: A new song object with all the data updated.
        :rtype: Song
        """

        return self.__subsonic.get_song(self.id)

    def star(self) -> Self:
        """Calls the "star" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.star_song(self.id)

        return self

    def unstar(self) -> Self:
        """Calls the "unstar" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.unstar_song(self.id)

        return self

    def set_rating(self, rating: int) -> Self:
        """Calls the "setRating" endpoint of the API.

        :param rating: The rating between 1 and 5 (inclusive).
        :type rating: int
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.set_rating(self.id, rating)

        return self

    def remove_rating(self) -> Self:
        """Calls the "setRating" endpoint of the API with a rating of 0.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.remove_rating(self.id)

        return self

    def scrobble(self, time: datetime, submission: bool = True) -> Self:
        """Calls the "scrobble" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.scrobble(self.id, time, submission)

        return self


class ScanStatus:
    """Representation of all the data related to the status
    of a library scan in Subsonic.
    """

    def __init__(self, scanning: bool, count: int) -> None:
        """Representation of all the data related to the status
        of a library scan in Subsonic.

        :param scanning: The status of the scan.
        :type scanning: bool
        :param count: Scanned item count.
        :type count: int
        """

        self.scanning: bool = scanning
        self.count: int = count


class ChatMessage:
    """Representation of all the data related to a chat message in Subsonic."""

    def __init__(self, username: str, time: int, message: str) -> None:
        """Representation of all the data related to a chat message in Subsonic.

        :param username: The username of the creator of the message
        :type username: str
        :param time: Time when the message was created.
        :type time: int
        :param message: The message content.
        :type message: str
        """

        self.username: str = username

        # Divide by 1000 as the Subsonic API return in milliseconds instead of seconds
        self.time: datetime = datetime.fromtimestamp(time / 1000)
        self.message: str = message


class Jukebox:
    """Representation of all the data related to the jukebox in Subsonic."""

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
        """Representation of all the data related to the jukebox in Subsonic.

        :param subsonic: _description_
        :type subsonic: Subsonic
        :param currentIndex: _description_
        :type currentIndex: int
        :param playing: _description_
        :type playing: bool
        :param gain: _description_
        :type gain: float
        :param position: _description_
        :type position: int
        :param entry: _description_, defaults to None
        :type entry: list[dict[str, Any]] | None, optional
        """

        self.__subsonic: "Subsonic" = subsonic
        self.current_index: int = currentIndex
        self.playing: bool = playing
        self.gain: float = gain
        self.position: int = position

        self.playlist: list[Song] | None = None
        if entry is None:
            return

        self.playlist = []

        for song in entry:
            self.playlist.append(Song(subsonic=self.__subsonic, **song))

    def generate(self) -> "Jukebox":
        """Returns the function to the the same song with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new song object with all the data updated.
        :rtype: Jukebox
        """

        return self.__subsonic.jukebox_get()

    def start(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "start".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_start()

        return self

    def stop(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "stop".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_stop()

        return self

    def skip(self, index: int, offset: float = 0) -> Self:
        """_summary_

        :param index: The index in the jukebox playlist to skip to.
        :type index: int
        :param offset: Start playing this many seconds into the track, defaults to 0.
        :type offset: float, optional
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_skip(index, offset)

        return self

    def shuffle(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "shuffle".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_shuffle()

        # The shuffle is server side so a call to the API is necessary
        # to get the new order of the playlist
        self.playlist = self.__subsonic.jukebox_get().playlist

        return self

    def set_gain(self, gain: float) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "setGain"

        :param gain: A number between 0 and 1 (inclusive) to set the gain.
        :type gain: float
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_set_gain(gain)
        self.gain = gain

        return self

    def clear(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "clear".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_clear()
        self.playlist = []

        return self

    def set(self, song: Song | str) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "set".

        :param song: Either a Song object or the ID of a song to set it in the jukebox.
        :type song: Song | str
        :raises ValueError: Raised if the gain argument isn't between the valid range.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        if type(song) is str:
            song_to_set: Song = Song(self.__subsonic, song)

        self.__subsonic.jukebox_set(song_to_set)
        self.playlist = [song_to_set]

        return self

    def add(self, song: Song | str) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "add".

        :param song: Either a Song object or the ID of a song to add it in the jukebox.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        if type(song) is str:
            song_to_add: Song = Song(self.__subsonic, song)

        self.__subsonic.jukebox_add(song_to_add)

        if self.playlist is not None:
            self.playlist.append(song_to_add)
            return self

        # If the playlist is None the real value of it is unknown,
        # so a call the API is necessary to get a correct representation of the jukebox
        self.playlist = self.generate().playlist
        return self

    def remove(self, index: int) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "remove".

        :param index: The index in the jukebox playlist for the song to remove.
        :type index: int
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.jukebox_remove(index)

        if self.playlist is not None:
            del self.playlist[index]
            return self

        # If the playlist is None the real value of it is unknown,
        # so a call the API is necessary to get a correct representation of the jukebox
        self.playlist = self.generate().playlist
        return self
