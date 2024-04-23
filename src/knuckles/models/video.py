from typing import TYPE_CHECKING, Any

# Avoid circular import error
import knuckles.models.album as album_model_module
from knuckles.models.genre import Genre, ItemGenre

from ..exceptions import ResourceNotFound
from .artist import Artist
from .contributor import Contributor
from .cover_art import CoverArt
from .model import Model
from .replay_gain import ReplayGain

if TYPE_CHECKING:
    from ..subsonic import Subsonic


from dateutil import parser


class AudioTrack(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        name: str | None = None,
        languageCode: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name
        self.language_code = languageCode


class Captions(Model):
    def __init__(self, subsonic: "Subsonic", id: str, name: str | None = None) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name


class VideoInfo(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        video_id: str,
        id: str,
        captions: dict[str, Any] | None = None,
        audioTrack: list[dict[str, Any]] | None = None,
        conversion: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.video_id = video_id
        self.id = id
        self.captions = (
            Captions(subsonic=self._subsonic, **captions) if captions else None
        )
        self.conversion = (
            Video(subsonic=self._subsonic, **conversion) if conversion else None
        )

        self.audio_tracks: dict[str, AudioTrack] | None
        if not audioTrack:
            self.audio_track = None
            return

        self.audio_tracks = {}
        for track in audioTrack:
            language_code = track["languageCode"]

            del track["languageCode"]
            self.audio_tracks[language_code] = AudioTrack(
                subsonic=self._subsonic, **track
            )

    def generate(self) -> "VideoInfo":
        return self._subsonic.browsing.get_video_info(self.video_id)


class Video(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        title: str | None = None,
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

        self.info: VideoInfo | None = None

    def generate(self) -> "Video":
        """Return a new song with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new song object with all the data updated.
        :rtype: Song
        """

        video = self._subsonic.browsing.get_video(self.id)

        if video is None:
            raise ResourceNotFound()

        return video

    def get_video_info(self) -> VideoInfo:
        self.info = self._subsonic.browsing.get_video_info(self.id)

        return self.info
