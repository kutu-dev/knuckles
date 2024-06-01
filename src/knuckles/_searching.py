from typing import TYPE_CHECKING

from ._api import Api
from .models._album import Album
from .models._artist import Artist
from .models._search_result import SearchResult
from .models._song import Song

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Searching:
    """Class that contains all the methods needed to interact with the
    [bookmark endpoints](https://opensubsonic.netlify.app/
    categories/searching/) in the Subsonic API.
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
        """Direct method to call the "search2" and "search3" endpoints,
        abstracting all the parameters of them.

        Args:
            query: The query string to be send to the server.
            song_count: The numbers of songs that the server
                should return.
            song_offset: The number of songs to offset in the list,
                useful for pagination.
            album_count: The numbers of albums that the server
                should return.
            album_offset: The number of album to offset in the list,
                useful for pagination.
            artist_count: The numbers of artists that the server
                should return.
            artist_offset: The number of artists to offset in the list,
                useful for pagination.
            music_folder_id: An ID of a music folder to limit where the
                songs, albums and artists should come from.
            id3: If the ID3 organized endpoint should be called or not.

        Returns:
            An object that contains all the info about the found songs,
                albums and artists received with the given query.
        """

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
        """Search and find all the songs, albums and artists that
        whose title match the given query.

        Args:
            query: The query string to be send to the server.
            song_count: The numbers of songs that the server
                should return.
            song_offset: The number of songs to offset in the list,
                useful for pagination.
            album_count: The numbers of albums that the server
                should return.
            album_offset: The number of album to offset in the list,
                useful for pagination.
            artist_count: The numbers of artists that the server
                should return.
            artist_offset: The number of artists to offset in the list,
                useful for pagination.
            music_folder_id: An ID of a music folder to limit where the
                songs, albums and artists should come from.

        Returns:
            An object that contains all the info about the found songs,
                albums and artists received with the given query.
        """

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
        """Search and find all the songs, albums and artists that
        whose title match the given query. Not organized according
        ID3 tags.

        Args:
            query: The query string to be send to the server.
            song_count: The numbers of songs that the server
                should return.
            song_offset: The number of songs to offset in the list,
                useful for pagination.
            album_count: The numbers of albums that the server
                should return.
            album_offset: The number of album to offset in the list,
                useful for pagination.
            artist_count: The numbers of artists that the server
                should return.
            artist_offset: The number of artists to offset in the list,
                useful for pagination.
            music_folder_id: An ID of a music folder to limit where the
                songs, albums and artists should come from.

        Returns:
            An object that contains all the info about the found songs,
                albums and artists received with the given query.
        """

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
