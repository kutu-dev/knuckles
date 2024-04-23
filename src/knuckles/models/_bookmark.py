from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound
from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class Bookmark(Model):
    """Representation of all the data related to a bookmark in Subsonic."""

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
        """Return a new bookmark with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new album info object with all the data updated.
        :rtype: Bookmark
        """

        get_bookmark = self._subsonic.bookmarks.get_bookmark(self.song.id)

        if get_bookmark is None:
            raise ResourceNotFound()

        return get_bookmark

    def create(self) -> Self:
        """Calls the "createBookmark" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.bookmarks.create_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def update(self) -> Self:
        """Calls the "createBookmark" endpoint of the API, as creating and updating
        a bookmark uses the same endpoint. Useful for having more self-descriptive code.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.bookmarks.update_bookmark(
            self.song.id, self.position, self.comment
        )

        return self

    def delete(self) -> Self:
        """Calls the "deleteBookmark" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.bookmarks.delete_bookmark(self.song.id)

        return self
