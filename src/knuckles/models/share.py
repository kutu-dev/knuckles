from typing import TYPE_CHECKING, Any, Self

from ..exceptions import (
    ResourceNotFound,
    ShareInvalidSongList,
)
from .song import Song
from .user import User

if TYPE_CHECKING:
    from ..subsonic import Subsonic


from dateutil import parser


class Share:
    """Representation of all the data related to a share in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
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
        self.__subsonic = subsonic
        self.id = id
        self.url = url
        self.description = description
        self.user = User(username) if username else None
        self.created = parser.parse(created) if created else None
        self.expires = parser.parse(expires) if expires else None
        self.last_visited = parser.parse(lastVisited) if lastVisited else None
        self.visit_count = visitCount
        self.songs = (
            [Song(self.__subsonic, **song) for song in entry] if entry else None
        )

    def generate(self) -> "Share | None":
        """Return a new share with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new share object with all the data updated.
        :rtype: Share
        """

        getted_share = self.__subsonic.sharing.get_share(self.id)

        if getted_share is None:
            raise ResourceNotFound(
                "Unable to generate share as it does not exist in the server"
            )

        return getted_share

    def create(self) -> Self:
        if self.songs is None or self.songs == []:
            raise ShareInvalidSongList(
                (
                    "A list with at least one song model object in the songs parameter"
                    + "is necessary to create a share"
                )
            )

        songs_ids = [song.id for song in self.songs]

        self.__subsonic.sharing.create_share(songs_ids, self.description, self.expires)

        return self

    def update(self) -> Self:
        self.__subsonic.sharing.update_share(self.id, self.description, self.expires)

        return self

    def delete(self) -> Self:
        self.__subsonic.sharing.delete_share(self.id)

        return self
