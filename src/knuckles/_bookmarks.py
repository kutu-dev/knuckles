from typing import TYPE_CHECKING

from ._api import Api
from .models._bookmark import Bookmark
from .models._play_queue import PlayQueue

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Bookmarks:
    """Class that contains all the methods needed to interact with the
    [bookmark endpoints](https://opensubsonic.netlify.app/
    categories/bookmarks/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_bookmarks(self) -> list[Bookmark]:
        """Get all the bookmarks created by the authenticated user.

        Returns:
            A list containing all the bookmarks for the authenticated user.
        """

        response = self.api.json_request("getBookmarks")["bookmarks"]["bookmark"]

        return [Bookmark(self.subsonic, **bookmark) for bookmark in response]

    def get_bookmark(self, bookmark_id: str) -> Bookmark | None:
        """Get all the info of a bookmark given its ID.

        Args:
            bookmark_id: The id of the bookmark to get.

        Returns:
            A object that contains all the info of the requested bookmark.
        """

        bookmarks = self.get_bookmarks()

        for bookmark in bookmarks:
            if bookmark.song.id == bookmark_id:
                return bookmark

        return None

    def create_bookmark(
        self, song_or_video_id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Creates a new bookmark for the authenticated user.

        Args:
            song_or_video_id: The ID of the song or video to bookmark.
            position: A position in milliseconds to be indicated with the song
                or video.
            comment: A comment to be attached with the song or video.

        Returns:
            An object that contains all the info of the new created
                bookmark.
        """

        self.api.json_request(
            "createBookmark",
            {"id": song_or_video_id, "position": position, "comment": comment},
        )

        # Fake the song structure given by in the API.
        return Bookmark(
            self.subsonic, {"id": song_or_video_id}, position=position, comment=comment
        )

    def update_bookmark(
        self, song_or_video_id: str, position: int, comment: str | None = None
    ) -> Bookmark:
        """Updates a bookmark for the authenticated user.

        Args:
            song_or_video_id: The ID of the song or video to update its
                bookmark.
            position: A position in milliseconds to be indicated with the song
                or video.
            comment: A comment to be attached with the song or video.
        Returns:
            An object that contains all the info of the new created
                bookmark.
        """

        return self.create_bookmark(song_or_video_id, position, comment)

    def delete_bookmark(self, song_or_video_id: str) -> "Subsonic":
        """Deletes a bookmark for the authenticated user.

        Args:
            song_or_video_id: The ID of the song or video to delete its
                bookmark.
        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """
        self.api.json_request("deleteBookmark", {"id": song_or_video_id})

        return self.subsonic

    def get_play_queue(self) -> PlayQueue:
        """Get the play queue of the authenticated user.

        Returns:
            An object that contains all the info of the
                play queue of the user.
        """

        response = self.api.json_request("getPlayQueue")["playQueue"]

        return PlayQueue(self.subsonic, **response)

    def save_play_queue(
        self,
        song_ids: list[str],
        current_song_id: str | None = None,
        position: int | None = None,
    ) -> PlayQueue:
        """Saves a new play queue for the authenticated user.

        Args:
            song_ids: A list with all the songs to add to the queue.
            current_song_id: The ID of the current playing song.
            position: A position in milliseconds of where the current song
                playback it at.

        Returns:
            An object that contains all the info of the new
                saved play queue.
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
