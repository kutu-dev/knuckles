from typing import TYPE_CHECKING, Any

from .api import Api
from .models.album import Album
from .models.now_playing_entry import NowPlayingEntry
from .models.song import Song
from .models.starred_content import StarredContent

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
        id3: bool = True,
        **extra_params: Any,
    ) -> list[Album]:
        response = self.api.json_request(
            "getAlbumList2" if id3 else "getAlbumList",
            {
                "type": type,
                "size": num_of_albums,
                "offset": album_list_offset,
                "musicFolderId": music_folder_id,
                **extra_params,
            },
        )["albumList2" if id3 else "albumList"]["album"]

        return [Album(subsonic=self.subsonic, **album) for album in response]

    def get_album_list_random_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "random", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_newest_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "newest", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_highest_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "highest", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_frequent_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "frequent", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_recent_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "recent", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_alphabetical_by_name_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "alphabeticalByName",
            num_of_albums,
            album_list_offset,
            music_folder_id,
            False,
        )

    def get_album_list_alphabetical_by_artist_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "alphabeticalByArtist",
            num_of_albums,
            album_list_offset,
            music_folder_id,
            False,
        )

    def get_album_list_starred_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        return self._get_album_list_generic(
            "starred", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_by_year_non_id3(
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
            False,
            fromYear=from_year,
            toYear=to_year,
        )

    def get_album_list_by_genre_non_id3(
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
            False,
            genre=genre_name,
        )

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

    def get_random_songs(
        self,
        num_of_songs: int | None = None,
        genre_name: str | None = None,
        from_year: int | None = None,
        to_year: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Song]:
        response = self.api.json_request(
            "getRandomSongs",
            {
                "size": num_of_songs,
                "genre": genre_name,
                "fromYear": from_year,
                "toYear": to_year,
                "musicFolderId": music_folder_id,
            },
        )["randomSongs"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]

    def get_songs_by_genre(
        self,
        genre_name: str,
        num_of_songs: int | None = None,
        song_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Song]:
        response = self.api.json_request(
            "getSongsByGenre",
            {
                "genre": genre_name,
                "count": num_of_songs,
                "offset": song_list_offset,
                "musicFolderId": music_folder_id,
            },
        )["songsByGenre"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]

    def get_now_playing(self) -> list[NowPlayingEntry]:
        response = self.api.json_request("getNowPlaying")["nowPlaying"]["entry"]

        return [NowPlayingEntry(subsonic=self.subsonic, **entry) for entry in response]

    def get_starred_non_id3(self, music_folder_id: str | None = None) -> StarredContent:
        response = self.api.json_request(
            "getStarred", {"musicFolderId": music_folder_id}
        )["starred"]

        return StarredContent(subsonic=self.subsonic, **response)

    def get_starred(self, music_folder_id: str | None = None) -> StarredContent:
        response = self.api.json_request(
            "getStarred2", {"musicFolderId": music_folder_id}
        )["starred2"]

        return StarredContent(subsonic=self.subsonic, **response)
