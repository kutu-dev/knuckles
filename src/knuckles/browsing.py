from typing import TYPE_CHECKING

from .models.genre import Genre

from .api import Api
from .models.album import Album, AlbumInfo
from .models.artist import Artist
from .models.song import Song

if TYPE_CHECKING:
    from .subsonic import Subsonic


# TODO Unfinished
class Browsing:
    """Class that contains all the methods needed to interact
    with the browsing calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/browsing/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_genres(self) -> list[Genre]:
        """Calls the "getGenres" endpoint of the API.

        :return: A list will all the registered genres.
        :rtype: list[Genre]
        """

        response = self.api.request("getGenres")["genres"]["genre"]

        return [Genre(self.subsonic, **genre) for genre in response]

    def get_genre(self, name: str) -> Genre | None:
        """Get a desired genre.

        :param name: The name of the genre to get.
        :type name: str
        :return: A genre object that correspond with the given name.
        :rtype: Genre | None
        """

        genres = self.get_genres()

        for genre in genres:
            if genre.value == name:
                return genre

        return None

    def get_artists(self, music_folder_id: str | None = None) -> list[Artist]:
        response = self.api.request("getArtists", {"musicFolderId": music_folder_id})[
            "artists"
        ]["index"]

        artists: list[Artist] = []

        for index in response:
            for artist_data in index["artist"]:
                artist = Artist(self.subsonic, **artist_data)
                artists.append(artist)

        return artists

    def get_artist(self, id: str) -> Artist:
        response = self.api.request("getArtist", {"id": id})["artist"]

        return Artist(self.subsonic, **response)

    def get_album(self, id: str) -> Album:
        response = self.api.request("getAlbum", {"id": id})["album"]

        return Album(self.subsonic, **response)

    def get_album_info(self, id: str) -> AlbumInfo:
        """Calls to the "getAlbumInfo2" endpoint of the API.

        :param id: The ID of the album to get its info.
        :type id: str
        :return: An object with all the extra info given by the server about the album.
        :rtype: AlbumInfo
        """

        response = self.api.request("getAlbumInfo2", {"id": id})["albumInfo"]

        return AlbumInfo(self.subsonic, id, **response)

    def get_song(self, id: str) -> Song:
        """Calls to the "getSong" endpoint of the API.

        :param id: The ID of the song to get.
        :type id: str
        :return: An object with all the information
            that the server has given about the song.
        :rtype: Song
        """

        response = self.api.request("getSong", {"id": id})["song"]

        return Song(self.subsonic, **response)
