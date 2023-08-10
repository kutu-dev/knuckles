from typing import TYPE_CHECKING

from .api import Api
from .models.bookmark import Bookmark

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Bookmarks:
    """Class that contains all the methods needed to interact
    with the browsing calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/bookmarks/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_bookmarks(self) -> list[Bookmark]:
        """Calls the "getBookmarks" endpoints of the API.

        :return: A list with all the bookmarks given by the server.
        :rtype: list[Bookmark]
        """

        response = self.api.request("getBookmarks")["bookmarks"]["bookmark"]

        return [Bookmark(self.subsonic, **bookmark) for bookmark in response]

    def get_bookmark(self, id: str) -> Bookmark | None:
        """Using the "getBookmarks" endpoint iterates over all the bookmarks
        and find the one with the same ID.

        :param id: The ID of the song of the bookmark to find.
        :type id: str
        :return: The found bookmark or None if no one is found.
        :rtype: Bookmark | None
        """

        bookmarks = self.get_bookmarks()

        for bookmark in bookmarks:
            if bookmark.song.id == id:
                return bookmark

        return None

    def create_bookmark(
        self, id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Calls the "createBookmark" endpoint of the API.

        :param id: The ID of the song of the bookmark.
        :type id: str
        :param position: The position in seconds of the bookmark.
        :type position: int
        :param comment: The comment of the bookmark, defaults to None.
        :type comment: str | None, optional
        :return: The new created share.
        :rtype: Bookmark
        """

        self.api.request(
            "createBookmark", {"id": id, "position": position, "comment": comment}
        )

        # Fake the structure given by the songs in the API.
        return Bookmark(self.subsonic, {"id": id}, position=position, comment=comment)

    def update_bookmark(
        self, id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Method that internally calls the create_bookmark method
        as creating and updating a bookmark uses the same endpoint. Useful for having
        more self descriptive code.

        :param id: The ID of the song of the bookmark.
        :type id: str
        :param position: The position in seconds of the bookmark.
        :type position: int
        :param comment: The comment of the bookmark, defaults to None.
        :type comment: str | None, optional
        :return: A Bookmark object with all the updated info.
        :rtype: Bookmark
        """

        return self.create_bookmark(id, position, comment)

    def delete_bookmark(self, id: str) -> "Subsonic":
        """Calls the "deleteBookmark" endpoint of the API.

        :param id: The ID of the song of the bookmark to delete.
        :type id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("deleteBookmark", {"id": id})

        return self.subsonic
