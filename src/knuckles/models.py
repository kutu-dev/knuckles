# Not fancy but does the job
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subsonic import Subsonic

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable

from dateutil import parser


@dataclass()
class SubsonicResponse:
    status: str
    version: str

    # Open Subsonic extensions
    type: str | None = None
    server_version: str | None = None
    open_subsonic: bool = False

    def __bool__(self) -> bool:
        return self.status == "ok"


@dataclass()
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


@dataclass()
class CoverArt:
    id: str


#! TODO
@dataclass()
class Album:
    id: str
    name: str


#! TODO
@dataclass()
class Artist:
    id: str
    name: str


@dataclass()
class Song:
    id: str
    is_dir: bool
    title: str

    parent: str | None = None
    album: Album = field(init=False)
    album_id: str | None = None
    album_name: str | None = None
    artist: Artist = field(init=False)
    artist_id: str | None = None
    artist_name: str | None = None
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

    # Open Subsonic extensions
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

        if self.album_id is not None and self.album_name is not None:
            self.album = Album(self.album_id, self.album_name)

        if self.artist_id is not None and self.artist_name is not None:
            self.artist = Artist(self.artist_id, self.artist_name)

    def generate(self, subsonic_instance: "Subsonic") -> Callable:
        """Returns the function to the the same song with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the instance itself
        with immutability, e.g., `foo = foo.generate(bar)()`.

        Args:
            subsonic_instance (Subsonic): A Subsonic object to make the call to the API

        Returns:
            Callable: _description_
        """

        return lambda: subsonic_instance.get_song(self.id)
