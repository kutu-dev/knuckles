from typing import TYPE_CHECKING

from ._api import Api
from .models._playlist import Playlist

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Playlists:
    """Class that contains all the methods needed to interact
    with the playlists calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/playlists/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_playlists(self, username: str | None = None) -> list[Playlist]:
        """Calls to the "getPlaylists" endpoint of the API.

        :param username: The user to get its playlist,
            if None gets the playlist of the authenticated user, defaults to None.
        :type username: str | None, optional
        :return: A list with all the playlist of the desired user.
        :rtype: list[Playlist]
        """
        response = self.api.json_request(
            "getPlaylists",
            {"username": username} if username else {},
        )["playlists"]["playlist"]

        playlists = [Playlist(self.subsonic, **playlist) for playlist in response]

        return playlists

    def get_playlist(self, id_: str) -> Playlist:
        """Calls to the "getPlaylist" endpoint of the API.

        :param id_: The ID of the playlist to get.
        :type id_: str
        :return: The requested playlist.
        :rtype: Playlist
        """
        response = self.api.json_request("getPlaylist", {"id": id_})["playlist"]

        return Playlist(self.subsonic, **response)

    def create_playlist(
        self,
        name: str,
        comment: str | None = None,
        public: bool | None = None,
        song_ids: list[str] | None = None,
    ) -> Playlist:
        """Calls the "createPlaylist" endpoint of the API.

        The Subsonic API only allows to set a name and a list of songs when creating
        a playlist. To allow more initial customization (comment and public)
        this method calls the "updatePlaylist" endpoint internally.

        :param name: The name of the new playlist.
        :type name: str
        :param comment: A comment to append to the playlist, defaults to None.
        :type comment: str | None, optional
        :param public: If the playlist should be public of private, defaults to None.
        :type public: bool | None, optional
        :param song_ids: A list of songs to add to the playlist, defaults to None.
        :type song_ids: list[str] | None, optional
        :return: The new created playlist.
        :rtype: Playlist
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
        id_: str,
        name: str | None = None,
        comment: str | None = None,
        public: bool | None = None,
        song_ids_to_add: list[str] | None = None,
        song_indexes_to_remove: list[int] | None = None,
    ) -> Playlist:
        """Calls the "updatePlaylist" endpoint of the API.

        :param id_: The ID of the playlist to update.
        :type id_: str
        :param name: A new name for the playlist, defaults to None.
        :type name: str | None, optional
        :param comment: A new comment for the playlist, defaults to None.
        :type comment: str | None, optional
        :param public: A new public state for the playlist, defaults to None.
        :type public: bool | None, optional
        :param song_ids_to_add: A list of IDs of songs to add to the playlist,
            defaults to None.
        :type song_ids_to_add: list[str] | None, optional
        :param song_indexes_to_remove: A list of indexes of songs to remove
            in the playlist, defaults to None.
        :type song_indexes_to_remove: list[int] | None, optional
        :return: The updated version of the playlist.
        :rtype: Playlist
        """
        self.api.json_request(
            "updatePlaylist",
            {
                "playlistId": id_,
                "name": name,
                "comment": comment,
                "public": public,
                "songIdToAdd": song_ids_to_add,
                "songIndexToRemove": song_indexes_to_remove,
            },
        )

        return Playlist(
            self.subsonic, id=id_, name=name, comment=comment, public=public
        )

    def delete_playlist(self, id_: str) -> "Subsonic":
        """Calls the "deletePlaylist" endpoint of the API.

        :param id_: The ID of the song to remove.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """
        self.api.json_request("deletePlaylist", {"id": id_})

        return self.subsonic
