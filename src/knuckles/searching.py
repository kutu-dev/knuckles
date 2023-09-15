from dataclasses import dataclass
from typing import TYPE_CHECKING

from .api import Api
from .models.album import Album
from .models.artist import Artist
from .models.song import Song

if TYPE_CHECKING:
    from .subsonic import Subsonic


# Use a plain dataclass as it only stores lists
# and doesn't have any sort of method to be generated


@dataclass
class SearchResult:
    songs: list[Song] | None = None
    albums: list[Album] | None = None
    artists: list[Artist] | None = None


class Searching:
    """Class that contains all the methods needed to interact
    with the searching calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/searching/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

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
        """Calls the "search3" endpoint of the API.

        :param query: The query
        :type query: str
        :param song_count: Maximum number of songs to return
        :type song_count: int
        :param song_offset: Offset the results for songs
        :type song_offset: int
        :param album_count: Maximum number of albums to return
        :type album_count: int
        :param album_offset: Offset the results for albums
        :type album_offset: int
        :param artist_count: Maximum number of artists to return
        :type artist_count: int
        :param artist_offset: Offset the results for artists
        :type artist_offset: int
        :param music_folder_id: The id of the music folder to search results
        :type music_folder_id: str
        :return:
        :rtype:
        """
        response = self.api.request(
            "search3",
            {
                "query": query,
                "songCount": song_count,
                "songOffset": song_offset,
                "albumCount": album_count,
                "albumOffset": album_offset,
                "artistCount": artist_count,
                "artistOffset": artist_offset,
            },
        )["searchResult3"]

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
            songs=search_result_songs,
            albums=search_result_albums,
            artists=search_result_artists,
        )
