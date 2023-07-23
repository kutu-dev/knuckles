# Not fancy but does the job
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from .subsonic import Subsonic

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

from dateutil import parser


@dataclass
class SubsonicResponse:
    status: str
    version: str

    # Open Subsonic extensions
    type: str | None = None
    server_version: str | None = None
    open_subsonic: bool = False

    def __bool__(self) -> bool:
        return self.status == "ok"


@dataclass
class License:
    valid: bool
    email: str | None = None
    license_expires: datetime | str | None = None
    trial_expires: datetime | str | None = None

    def __bool__(self) -> bool:
        return self.valid

    def __post_init__(self) -> None:
        if type(self.license_expires) is str:
            self.license_expires = parser.parse(self.license_expires)

        if type(self.trial_expires) is str:
            self.trial_expires = parser.parse(self.trial_expires)


@dataclass
class CoverArt:
    id: str


#! TODO
@dataclass
class Album:
    id: str
    name: str


#! TODO
@dataclass
class Artist:
    id: str
    name: str


@dataclass
class Song:
    _subsonic: "Subsonic"
    id: str
    title: str

    parent: str | None = None
    album: str | None = None
    album_id: str | None = None
    artist: str | None = None
    artist_id: str | None = None
    track: int | None = None
    year: int | None = None
    genre: str | None = None
    cover_art: CoverArt | str | None = None
    size: int | None = None
    content_type: str | None = None
    suffix: str | None = None
    transcoded_content_type: str | None = None
    transcoded_suffix: str | None = None
    duration: int | None = None
    bit_rate: int | None = None
    path: Path | str | None = None
    user_rating: int | None = None
    average_rating: float | None = None
    play_count: int | None = None
    disc_number: int | None = None
    created: datetime | str | None = None
    starred: datetime | str | None = None
    type: str | None = None
    bookmark_position: int | None = None

    # OpenSubsonic extensions
    played: datetime | str | None = None

    def __post_init__(self) -> None:
        if self.path is not None:
            self.path = Path(self.path)

        if type(self.created) is str:
            self.created = parser.parse(self.created)

        if type(self.starred) is str:
            self.starred = parser.parse(self.starred)

        if type(self.played) is str:
            self.played = parser.parse(self.played)

        if type(self.cover_art) is str:
            self.cover_art = CoverArt(self.cover_art)

    def generate(self) -> Callable:
        """Returns the function to the the same song with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the instance itself
        with immutability, e.g., `foo = foo.generate(bar)()`.

        Returns:
            Callable: _description_
        """

        return lambda: self._subsonic.get_song(self.id)

    def get_album(self) -> Album | None:
        """Return an Album dataclass that correspond with the song.

        Returns:
            Album | None: The album of the song or
            None if the song doesn't have artist data attached (album and album_id).
        """

        if self.album_id is None or self.album is None:
            return None

        return Album(self.album_id, self.album)

    def get_artist(self) -> Album | None:
        """Return an Artist dataclass that correspond with the song.

        Returns:
            Artist | None: The album of the song or
            None if the song doesn't have artist data attached (artist and artist_id).
        """

        if self.artist_id is None or self.artist is None:
            return None

        return Album(self.artist_id, self.artist)

    def star(self) -> Self:
        self._subsonic.star_song(self.id)

        return self

    def unstar(self) -> Self:
        self._subsonic.unstar_song(self.id)

        return self


@dataclass
class ScanStatus:
    scanning: bool
    count: int


@dataclass
class ChatMessage:
    username: str
    time: int
    message: str
