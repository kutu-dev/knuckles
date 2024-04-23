from typing import TYPE_CHECKING, Any, Self

from dateutil import parser

from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class PlayQueue(Model):
    """Representation of all the data related to a play queue in Subsonic."""

    def __init__(
        self,
        subsonic: "Subsonic",
        entry: list[dict[str, Any]],
        current: str | None = None,
        position: int | None = None,
        username: str | None = None,
        changed: str | None = None,
        changedBy: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.current = Song(self._subsonic, current) if current else None
        self.position = position
        self.user = User(self._subsonic, username) if username else None
        self.changed = parser.parse(changed) if changed else None
        self.changed_by = changedBy
        self.songs = [Song(self._subsonic, **song) for song in entry] if entry else None

    def generate(self) -> "PlayQueue":
        """Return a new play queue with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new share object with all the data updated.
        :rtype: PlayQueue
        """

        get_play_queue = self._subsonic.bookmarks.get_play_queue()

        return get_play_queue

    def save(self) -> Self:
        """Calls the "savePlayQueue" endpoint of the API.

        Saves the play queue using the parameters in the object.

        :return: _description_
        :rtype: Self
        """

        song_ids: list[str] = [song.id for song in self.songs] if self.songs else []

        self._subsonic.bookmarks.save_play_queue(
            song_ids, self.current.id if self.current else None, self.position
        )

        return self
