from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound, ShareInvalidSongList
from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class Share(Model):
    """Object that holds all the info about a share.

    Attributes:
        id (str): The ID of the share.
        url (str | None): The URL to access the shared media.
        description (str | None): The description of the share.
        user (User | None): All the info related with the user creator
            of the share.
        created (datetime | None): The timestamp when the share
            was created.
        expires (datetime | None): The timestamp when the share
            will expire.
        last_visited (datetime | None): The timestamp when the
            share was last visited.
        visit_count (int | None): Number of times the share has
            been visited.
        songs (list[Song] | None): List that holds all the info about
            all the songs available to access with the share.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        url: str | None = None,
        description: str | None = None,
        username: str | None = None,
        created: str | None = None,
        expires: str | None = None,
        lastVisited: str | None = None,
        visitCount: int | None = None,
        entry: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.url = url
        self.description = description
        self.user = User(self._subsonic, username) if username else None
        self.created = parser.parse(created) if created else None
        self.expires = parser.parse(expires) if expires else None
        self.last_visited = parser.parse(lastVisited) if lastVisited else None
        self.visit_count = visitCount
        self.songs = [Song(self._subsonic, **song) for song in entry] if entry else None

    def generate(self) -> "Share | None":
        """Return a new share object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        get_share = self._subsonic.sharing.get_share(self.id)

        if get_share is None:
            raise ResourceNotFound

        return get_share

    def create(self) -> "Share":
        """Create a new share with the same info of the current one.

        Raises:
            ShareInvalidSongList: Raised if the song list contained in
                the share is empty.

        Returns:
            The new created share.
        """

        if self.songs is None or self.songs == []:
            raise ShareInvalidSongList(
                (
                    "A list with at least one song model object in the songs parameter"
                    + "is necessary to create a share"
                )
            )

        songs_ids = [song.id for song in self.songs]

        new_share = self._subsonic.sharing.create_share(
            songs_ids, self.description, self.expires
        )

        return new_share

    def update(self) -> Self:
        """Update the info of the share with the one in the model.

        Returns:
            The object itself.
        """

        self._subsonic.sharing.update_share(self.id, self.description, self.expires)

        return self

    def delete(self) -> Self:
        """Delete the share from the server.

        Returns:
            The object itself.
        """

        self._subsonic.sharing.delete_share(self.id)

        return self
