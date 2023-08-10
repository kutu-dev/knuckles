from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound
from .song import Song
from .user import User

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from dateutil import parser


class Bookmark:
    """Representation of all the data related to a bookmark in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        entry: dict[str, Any],
        position: int,
        username: str | None = None,
        created: str | None = None,
        changed: str | None = None,
        comment: str | None = None,
    ) -> None:
        self.__subsonic = subsonic
        self.song = Song(self.__subsonic, **entry)
        self.position = position
        self.user = (
            User(subsonic=self.__subsonic, username=username) if username else None
        )
        self.comment = comment
        self.created = parser.parse(created) if created else None
        self.changed = parser.parse(changed) if changed else None

    def generate(self) -> "Bookmark":
        """Return a new bookmark with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: Bookmark
        """

        get_bookmark = self.__subsonic.bookmarks.get_bookmark(self.song.id)

        if get_bookmark is None:
            raise ResourceNotFound(
                "Unable to generate episode as it does not exist in the server"
            )

        return get_bookmark

    def create(self) -> Self:
        self.__subsonic.bookmarks.create_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def update(self) -> Self:
        self.__subsonic.bookmarks.update_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def delete(self) -> Self:
        self.__subsonic.bookmarks.delete_bookmark(self.song.id)

        return self
