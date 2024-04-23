from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound, ShareInvalidSongList
from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class Share(Model):
    """Representation of all the data related to a share in Subsonic."""

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
        """Representation of all the data related to a share in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The id of the share.
        :type id: str
        :param url: The url of the share, defaults to None.
        :type url: str | None, optional
        :param description: The description of the share, defaults to None.
        :type description: str | None, optional
        :param username: The username of the creator of the share, defaults to None.
        :type username: str | None, optional
        :param created: The time when the share was created, defaults to None.
        :type created: str | None, optional
        :param expires: The time when the share expires, defaults to None.
        :type expires: str | None, optional
        :param lastVisited: The last tim the share was used, defaults to None.
        :type lastVisited: str | None, optional
        :param visitCount: The number of times the share has been used,
            defaults to None.
        :type visitCount: int | None, optional
        :param entry: A list with all the songs that the share gives access,
            defaults to None.
        :type entry: list[dict[str, Any]] | None, optional
        """

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
        """Return a new share with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new share object with all the data updated.
        :rtype: Share
        """

        get_share = self._subsonic.sharing.get_share(self.id)

        if get_share is None:
            raise ResourceNotFound

        return get_share

    def create(self) -> "Share":
        """Calls the "createShare" endpoint of the API.

        Creates a new playlist with the same data of the object
        where the method is called.

        :raises ShareInvalidSongList: Raised if the list of songs
            in the share is empty of None.
        :return: The new created share.
        :rtype: Share
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
        """Calls the "updateShare" endpoint of the API.

        Updates the description and expire date of the share with the ones
        in the parameters of the object.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.sharing.update_share(self.id, self.description, self.expires)

        return self

    def delete(self) -> Self:
        """Calls the "deleteShare" endpoint of the API.

        Delete the share with the same ID as the id parameter in the object.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.sharing.delete_share(self.id)

        return self
