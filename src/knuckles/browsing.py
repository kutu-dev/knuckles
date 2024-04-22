from typing import TYPE_CHECKING

from .api import Api
from .models.album import Album, AlbumInfo
from .models.artist import Artist, ArtistInfo
from .models.genre import Genre
from .models.index import Index
from .models.music_directory import MusicDirectory
from .models.music_folder import MusicFolder
from .models.song import Song
from .models.video import Video, VideoInfo

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Browsing:
    """Class that contains all the methods needed to interact
    with the browsing calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/browsing/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_music_folders(self) -> list[MusicFolder]:
        """Calls the "getMusicFolders" endpoint of the API.

        :return: A list with all the received music folders.
        :rtype: list[MusicFolder]
        """

        response = self.api.json_request("getMusicFolders")["musicFolders"][
            "musicFolder"
        ]

        return [MusicFolder(self.subsonic, **music_folder) for music_folder in response]

    def get_music_folder(self, id_: str) -> MusicFolder | None:
        """Get a desired music folder.

        :param id_: The id of the music folder to get.
        :type id_: str
        :return: A music folder object that correspond with the given id
            or None if is no music folder is found.
        :rtype: Genre | None
        """

        music_folders = self.get_music_folders()

        for music_folder in music_folders:
            if music_folder.id == id_:
                return music_folder

        return None

    def get_indexes(self, music_folder_id: str, modified_since: int) -> Index:
        response = self.api.json_request(
            "getIndexes",
            {"musicFolderId": music_folder_id, "ifModifiedSince": modified_since},
        )["indexes"]

        return Index(subsonic=self.subsonic, **response)

    def get_music_directory(self, music_directory_id: str) -> MusicDirectory:
        response = self.api.json_request(
            "getMusicDirectory", {"id": music_directory_id}
        )["directory"]

        return MusicDirectory(subsonic=self.subsonic, **response)

    def get_genres(self) -> list[Genre]:
        """Calls the "getGenres" endpoint of the API.

        :return: A list will all the registered genres.
        :rtype: list[Genre]
        """

        response = self.api.json_request("getGenres")["genres"]["genre"]

        return [Genre(self.subsonic, **genre) for genre in response]

    def get_genre(self, name: str) -> Genre | None:
        """Get a desired genre.

        :param name: The name of the genre to get.
        :type name: str
        :return: A genre object that correspond with the given name
            or None if is no genre is found.
        :rtype: Genre | None
        """

        genres = self.get_genres()

        for genre in genres:
            if genre.value == name:
                return genre

        return None

    def get_artists(self, music_folder_id: str | None = None) -> list[Artist]:
        """Calls the "getArtists" endpoint of the API.

        :param music_folder_id: Only return artists in the music folder
            with the given ID.
        :type music_folder_id: str | None
        :return: A list with all the artists.
        :rtype: list[Artist]
        """

        response = self.api.json_request(
            "getArtists", {"musicFolderId": music_folder_id}
        )["artists"]["index"]

        artists: list[Artist] = []

        for index in response:
            for artist_data in index["artist"]:
                artist = Artist(self.subsonic, **artist_data)
                artists.append(artist)

        return artists

    def get_artist(self, id_: str) -> Artist:
        """Calls the "getArtist" endpoint of the API.

        :param id_: The ID of the artist to get.
        :type id_: str
        :return: An object with all the information
            that the server has given about the album.
        :rtype: Artist
        """

        response = self.api.json_request("getArtist", {"id": id_})["artist"]

        return Artist(self.subsonic, **response)

    def get_album(self, id_: str) -> Album:
        """Calls the "getAlbum" endpoint of the API.

        :param id_: The ID of the album to get.
        :type id_: str
        :return: An object with all the information
            that the server has given about the album.
        :rtype: Album
        """

        response = self.api.json_request("getAlbum", {"id": id_})["album"]

        return Album(self.subsonic, **response)

    def get_album_info(self, id_: str) -> AlbumInfo:
        """Calls to the "getAlbumInfo2" endpoint of the API.

        :param id_: The ID of the album to get its info.
        :type id_: str
        :return: An object with all the extra info given by the server about the album.
        :rtype: AlbumInfo
        """

        response = self.api.json_request("getAlbumInfo2", {"id": id_})["albumInfo"]

        return AlbumInfo(self.subsonic, id_, **response)

    def get_song(self, id_: str) -> Song:
        """Calls to the "getSong" endpoint of the API.

        :param id_: The ID of the song to get.
        :type id_: str
        :return: An object with all the information
            that the server has given about the song.
        :rtype: Song
        """

        response = self.api.json_request("getSong", {"id": id_})["song"]

        return Song(self.subsonic, **response)

    def get_videos(self) -> list[Video]:
        response = self.api.json_request("getVideos")["videos"]["video"]

        return [Video(self.subsonic, **video) for video in response]

    def get_video(self, video_id: str) -> Video | None:
        videos = self.get_videos()

        for video in videos:
            if video.id == video_id:
                return video

        return None

    def get_video_info(self, video_id: str) -> VideoInfo:
        response = self.api.json_request("getVideoInfo", {"id": video_id})["videoInfo"]

        return VideoInfo(self.subsonic, **response)

    def get_artist_info(
        self,
        id_: str,
        count: int | None = None,
        include_not_present: bool | None = None,
    ) -> ArtistInfo:
        """Calls the "getArtistInfo" endpoint of the API.

        :param id_: The id of the artist to get its info
        :type id_:
        :param count:
        :type count:
        :param include_not_present:
        :type include_not_present:
        :return:
        :rtype:
        """

        response = self.api.json_request(
            "getArtistInfo2",
            {"id": id_, "count": count, "includeNotPresent": include_not_present},
        )["artistInfo2"]

        return ArtistInfo(self.subsonic, id_, **response)

    def get_similar_songs(self, song_id: str, count: int | None = None) -> list[Song]:
        response = self.api.json_request(
            "getSimilarSongs2", {"id": song_id, "count": count}
        )["similarSongs2"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]

    def get_top_songs(self, artist_name: str, max_num_of_songs: int) -> list[Song]:
        response = self.api.json_request(
            "getTopSongs", {"artist": artist_name, "count": max_num_of_songs}
        )["topSongs"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]
