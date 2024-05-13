from typing import TYPE_CHECKING

from ._api import Api
from .models._playlist import Playlist

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Playlists:
    """Class that contains all the methods needed to interact with the
    [playlists endpoints](https://opensubsonic.netlify.app/
    categories/playlists/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_playlists(self, username: str | None = None) -> list[Playlist]:
        """Get all the playlists available to the authenticated user.

        Args:
            username: The username of another user if is wanted to get the
                playlists they can access.

        Returns:
            A list that holds all the info about all the playlist
                that the user can play.
        """

        response = self.api.json_request(
            "getPlaylists",
            {"username": username} if username else {},
        )["playlists"]["playlist"]

        playlists = [Playlist(self.subsonic, **playlist) for playlist in response]

        return playlists

    def get_playlist(self, playlist_id: str) -> Playlist:
        """Get all the info about a playlist available for the authenticated
        user.

        Args:
            playlist_id: The ID of the playlist to get its info.

        Returns:
            An object that holds all the info about the requested playlist.
        """

        response = self.api.json_request("getPlaylist", {"id": playlist_id})["playlist"]

        return Playlist(self.subsonic, **response)

    def create_playlist(
        self,
        name: str,
        comment: str | None = None,
        public: bool | None = None,
        song_ids: list[str] | None = None,
    ) -> Playlist:
        """Create a new playlist for the authenticated user.

        Args:
            name: The name of the playlist to be created.
            comment: A comment to be added to the new created playlist.
            public: If the song should be public or not.
            song_ids: A list of ID of the songs that should be included
                with the playlist.

        Returns:
            An object that holds all the info about the new created playlist.
        """

        response = self.api.json_request(
            "createPlaylist", {"name": name, "songId": song_ids}
        )["playlist"]

        new_playlist = Playlist(self.subsonic, **response)

        # Allow to modify comment and public
        # with a workaround using the updatePlaylist endpoint

        if comment or public:
            self.update_playlist(new_playlist.id, comment=comment, public=public)
            new_playlist.comment = comment
            new_playlist.public = public

        return new_playlist

    def update_playlist(
        self,
        playlist_id: str,
        name: str | None = None,
        comment: str | None = None,
        public: bool | None = None,
        song_ids_to_add: list[str] | None = None,
        song_indexes_to_remove: list[int] | None = None,
    ) -> Playlist:
        """Update the info of a playlist.

        Args:
            playlist_id: The ID of the playlist to update its info.
            name: A new name for the playlist.
            comment: A new comment for the playlist.
            public: Change if the playlist should be public or private.
            song_ids_to_add: A list of IDs of new songs to be added to the
                playlist.
            song_indexes_to_remove: A list in indexes of songs that should
                be removed from the playlist.

        Returns:
            An object that holds all the info about the updated playlist.
        """

        self.api.json_request(
            "updatePlaylist",
            {
                "playlistId": playlist_id,
                "name": name,
                "comment": comment,
                "public": public,
                "songIdToAdd": song_ids_to_add,
                "songIndexToRemove": song_indexes_to_remove,
            },
        )

        return Playlist(
            self.subsonic, id=playlist_id, name=name, comment=comment, public=public
        )

    def delete_playlist(self, playlist_id: str) -> "Subsonic":
        """Delete a playlist.

        Args:
            playlist_id: The ID of the playlist to remove.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("deletePlaylist", {"id": playlist_id})

        return self.subsonic
