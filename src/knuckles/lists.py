from typing import TYPE_CHECKING, Any

from .api import Api
from .models.album import Album

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Lists:
    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def _get_album_list_generic(
        self,
        type: str,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
        **extra_params: Any,
    ) -> list[Album]:
        response = self.api.json_request(
            "getAlbumList2",
            {
                "type": type,
                "size": num_of_albums,
                "offset": album_list_offset,
                "musicFolderId": music_folder_id,
                **extra_params,
            },
        )["albumList2"]["album"]

        return [Album(subsonic=self.subsonic, **album) for album in response]

    def get_album_list_random(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "random", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_newest(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "newest", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_highest(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "highest", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_frequent(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "frequent", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_recent(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "recent", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_alphabetical_by_name(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "alphabeticalByName", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_alphabetical_by_artist(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "alphabeticalByArtist", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_starred(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "starred", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_by_year(
        self,
        from_year: int,
        to_year: int,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "byYear",
            num_of_albums,
            album_list_offset,
            music_folder_id,
            fromYear=from_year,
            toYear=to_year,
        )

    def get_album_list_by_genre(
        self,
        genre_name: str,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "byGenre",
            num_of_albums,
            album_list_offset,
            music_folder_id,
            genre=genre_name,
        )
