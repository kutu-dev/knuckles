from typing import TYPE_CHECKING

from .api import Api
from .models.playlist import Playlist

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Playlists:
    """Class that contains all the methods needed to interact
    with the playlists calls and actions in the Subsonic API. <https://opensubsonic.netlify.app/categories/playlists/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_playlists(self, username: str | None = None) -> list[Playlist]:
        response = self.api.request(
            "getPlaylists",
            {"username": username} if username else {},
        )["playlists"]["playlist"]

        playlists = [Playlist(self.subsonic, **playlist) for playlist in response]

        return playlists

    def get_playlist(self, id: str) -> Playlist:
        response = self.api.request("getPlaylist", {"id": id})["playlist"]

        return Playlist(self.subsonic, **response)

    def create_playlist(self, name: str, song_ids: list[str]) -> Playlist:
        response = self.api.request(
            "createPlaylist", {"name": name, "songId": song_ids}
        )["playlist"]

        return Playlist(self.subsonic, **response)

    def update_playlist(
        self,
        id: str,
        name: str | None = None,
        comment: str | None = None,
        public: bool = False,
        song_ids_to_add: list[str] | None = None,
        song_indexes_to_remove: list[int] | None = None,
    ) -> Playlist:
        self.api.request(
            "updatePlaylist",
            {
                "playlistId": id,
                "name": name,
                "comment": comment,
                "public": public,
                "songIdToAdd": song_ids_to_add,
                "songIndexToRemove": song_indexes_to_remove,
            },
        )

        return Playlist(self.subsonic, id=id, name=name, comment=comment, public=public)

    def delete_playlist(self, id: str) -> "Subsonic":
        self.api.request("deletePlaylist", {"id": id})

        return self.subsonic
