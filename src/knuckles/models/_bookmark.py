from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound
from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class Bookmark(Model):
    """Object that holds all the info about a bookmark.

    Attributes:
        song (Song): All the info about the bookmarked song.
        position (int): The position in seconds of the playback
            of the song when it was bookmarked.
        user (User | None): All the info about the user that
            created the bookmark.
        comment (str | None): A comment attached to the bookmark.
        created (datetime | None): The timestamp when the bookmark
            was created.
        changed (datetime | None): The timestamp when the bookmark
            was updated.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        entry: dict[str, Any],
        position: int,
        username: str | None = None,
        created: str | None = None,
        changed: str | None = None,
        comment: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.song = Song(self._subsonic, **entry)
        self.position = position
        self.user = (
            User(subsonic=self._subsonic, username=username) if username else None
        )
        self.comment = comment
        self.created = parser.parse(created) if created else None
        self.changed = parser.parse(changed) if changed else None

    def generate(self) -> "Bookmark":
        """Return a new album object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        get_bookmark = self._subsonic.bookmarks.get_bookmark(self.song.id)

        if get_bookmark is None:
            raise ResourceNotFound()

        return get_bookmark

    def create(self) -> Self:
        """Create a new bookmark for the authenticated user
        with the same data of the object where this method is
        called.

        Returns:
            The object itself.
        """

        self._subsonic.bookmarks.create_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def update(self) -> Self:
        """Update the info about the bookmark of this song using the
        current data of the object.

        Returns:
            The object itself.
        """

        self._subsonic.bookmarks.update_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def delete(self) -> Self:
        """Delete the bookmark entry from the server.

        Returns:
            The object itself.
        """

        self._subsonic.bookmarks.delete_bookmark(self.song.id)

        return self
