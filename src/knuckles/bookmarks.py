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
        response = self.api.request("getBookmarks")["bookmarks"]["bookmark"]

        return [Bookmark(self.subsonic, **bookmark) for bookmark in response]

    def get_bookmark(self, id: str) -> Bookmark | None:
        bookmarks = self.get_bookmarks()

        for bookmark in bookmarks:
            if bookmark.song.id == id:
                return bookmark

        return None

    def create_bookmark(
        self, id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        self.api.request(
            "createBookmark", {"id": id, "position": position, "comment": comment}
        )

        # Fake the structure given by the songs in the API.
        return Bookmark(self.subsonic, {"id": id}, position=position, comment=comment)

    def update_bookmark(
        self, id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        return self.create_bookmark(id, position, comment)

    def delete_bookmark(self, id: str) -> "Subsonic":
        self.api.request("deleteBookmark", {"id": id})

        return self.subsonic
