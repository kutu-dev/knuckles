from typing import TYPE_CHECKING

from .api import Api
from .models.album import Album
from .models.artist import Artist
from .models.search_result import SearchResult
from .models.song import Song

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Searching:
    """Class that contains all the methods needed to interact
    with the searching calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/searching/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def _generic_search(
        self,
        query: str = "",
        song_count: int | None = None,
        song_offset: int | None = None,
        album_count: int | None = None,
        album_offset: int | None = None,
        artist_count: int | None = None,
        artist_offset: int | None = None,
        music_folder_id: str | None = None,
        id3: bool = True,
    ) -> SearchResult:
        response = self.api.json_request(
            "search3" if id3 else "search2",
            {
                "query": query,
                "songCount": song_count,
                "songOffset": song_offset,
                "albumCount": album_count,
                "albumOffset": album_offset,
                "artistCount": artist_count,
                "artistOffset": artist_offset,
                "musicFolderId": music_folder_id,
            },
        )["searchResult3" if id3 else "searchResult2"]

        search_result_songs = (
            [Song(self.subsonic, **song) for song in response["song"]]
            if "song" in response
            else None
        )
        search_result_albums = (
            [Album(self.subsonic, **album) for album in response["album"]]
            if "album" in response
            else None
        )
        search_result_artists = (
            [Artist(self.subsonic, **artist) for artist in response["artist"]]
            if "artist" in response
            else None
        )

        return SearchResult(
            self.subsonic,
            search_result_songs,
            search_result_albums,
            search_result_artists,
        )

    def search(
        self,
        query: str = "",
        song_count: int | None = None,
        song_offset: int | None = None,
        album_count: int | None = None,
        album_offset: int | None = None,
        artist_count: int | None = None,
        artist_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> SearchResult:
        return self._generic_search(
            query,
            song_count,
            song_offset,
            album_count,
            album_offset,
            artist_count,
            artist_offset,
        )

    def search_non_id3(
        self,
        query: str,
        song_count: int | None = None,
        song_offset: int | None = None,
        album_count: int | None = None,
        album_offset: int | None = None,
        artist_count: int | None = None,
        artist_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> SearchResult:
        return self._generic_search(
            query,
            song_count,
            song_offset,
            album_count,
            album_offset,
            artist_count,
            artist_offset,
            music_folder_id,
            False,
        )
