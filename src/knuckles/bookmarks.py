from typing import TYPE_CHECKING

from .api import Api
from .models.bookmark import Bookmark
from .models.play_queue import PlayQueue

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

        response = self.api.json_request("getBookmarks")["bookmarks"]["bookmark"]

        return [Bookmark(self.subsonic, **bookmark) for bookmark in response]

    def get_bookmark(self, id_: str) -> Bookmark | None:
        """Using the "getBookmarks" endpoint iterates over all the bookmarks
        and find the one with the same ID.

        :param id_: The ID of the song of the bookmark to find.
        :type id_: str
        :return: The found bookmark or None if no one is found.
        :rtype: Bookmark | None
        """

        bookmarks = self.get_bookmarks()

        for bookmark in bookmarks:
            if bookmark.song.id == id_:
                return bookmark

        return None

    def create_bookmark(
        self, id_: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Calls the "createBookmark" endpoint of the API.

        :param id_: The ID of the song of the bookmark.
        :type id_: str
        :param position: The position in seconds of the bookmark.
        :type position: int
        :param comment: The comment of the bookmark, defaults to None.
        :type comment: str | None, optional
        :return: The new created share.
        :rtype: Bookmark
        """

        self.api.json_request(
            "createBookmark", {"id": id_, "position": position, "comment": comment}
        )

        # Fake the song structure given by in the API.
        return Bookmark(self.subsonic, {"id": id_}, position=position, comment=comment)

    def update_bookmark(
        self, id_: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Method that internally calls the create_bookmark method
        as creating and updating a bookmark uses the same endpoint. Useful for having
        more self-descriptive code.

        :param id_: The ID of the song of the bookmark.
        :type id_: str
        :param position: The position in seconds of the bookmark.
        :type position: int
        :param comment: The comment of the bookmark, defaults to None.
        :type comment: str | None, optional
        :return: A Bookmark object with all the updated info.
        :rtype: Bookmark
        """

        return self.create_bookmark(id_, position, comment)

    def delete_bookmark(self, id_: str) -> "Subsonic":
        """Calls the "deleteBookmark" endpoint of the API.

        :param id_: The ID of the song of the bookmark to delete.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("deleteBookmark", {"id": id_})

        return self.subsonic

    def get_play_queue(self) -> PlayQueue:
        """Calls the "getPlayQueue" endpoint of the API.

        :return: The play queue of the authenticated user.
        :rtype: PlayQueue
        """

        response = self.api.json_request("getPlayQueue")["playQueue"]

        return PlayQueue(self.subsonic, **response)

    def save_play_queue(
        self,
        song_ids: list[str],
        current_song_id: str | None = None,
        position: int | None = None,
    ) -> PlayQueue:
        """Calls the "savePlayQueue" endpoint of the API.

        :param song_ids: A list with all the IDs of the songs to add.
        :type song_ids: list[str]
        :param current_song_id: The ID of the current song in the queue,
            defaults to None.
        :type current_song_id: str | None, optional
        :param position: The position in seconds of the current song,
            defaults to None.
        :type position: int | None, optional
        :return: The new saved play queue.
        :rtype: PlayQueue
        """

        self.api.json_request(
            "savePlayQueue",
            {"id": song_ids, "current": current_song_id, "position": position},
        )

        # Fake the song structure given by in the API.
        songs = []
        for song_id in song_ids:
            songs.append({"id": song_id})

        return PlayQueue(self.subsonic, songs, current_song_id, position)
