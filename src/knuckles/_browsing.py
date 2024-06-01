from typing import TYPE_CHECKING

from ._api import Api
from .models._album import Album, AlbumInfo
from .models._artist import Artist, ArtistInfo
from .models._artist_index import ArtistIndex
from .models._genre import Genre
from .models._music_directory import MusicDirectory
from .models._music_folder import MusicFolder
from .models._song import Song
from .models._video import Video, VideoInfo

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Browsing:
    """Class that contains all the methods needed to interact with the
    [browsing endpoints](https://opensubsonic.netlify.app/categories/browsing)
    in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_music_folders(self) -> list[MusicFolder]:
        """Get all the top level music folders.

        Returns:
            A list that contains all the info about all the available
                music folders.
        """

        response = self.api.json_request("getMusicFolders")["musicFolders"][
            "musicFolder"
        ]

        return [MusicFolder(self.subsonic, **music_folder) for music_folder in response]

    def get_music_folder(self, music_folder_id: str) -> MusicFolder | None:
        """Get the info of a music folder.

        Args:
            music_folder_id: The ID of the music folder to get.

        Returns:
            An object that contains all the info about the
                requested music folder, or None if it wasn't found.
        """

        music_folders = self.get_music_folders()

        for music_folder in music_folders:
            if music_folder.id == music_folder_id:
                return music_folder

        return None

    def get_music_directory(self, music_directory_id: str) -> MusicDirectory:
        """Get the info of a music directory.

        Args:
            music_directory_id: The ID of the music directory to get its info.

        Returns:
            An object that holds all the info about the requested music
                directory.
        """

        response = self.api.json_request(
            "getMusicDirectory", {"id": music_directory_id}
        )["directory"]

        return MusicDirectory(subsonic=self.subsonic, **response)

    def get_genres(self) -> list[Genre]:
        """Get all the available genres in the server.

        Returns:
            A list with all the registered genres in the server.
        """

        response = self.api.json_request("getGenres")["genres"]["genre"]

        return [Genre(self.subsonic, **genre) for genre in response]

    def get_genre(self, genre_name: str) -> Genre | None:
        """Get all the info of a genre.

        Args:
            genre_name: The name of the genre to get its info.

        Returns:
            An object that contains all the info
                about the requested genre.
        """

        genres = self.get_genres()

        for genre in genres:
            if genre.value == genre_name:
                return genre

        return None

    def get_artists(self, music_folder_id: str | None = None) -> list[Artist]:
        """Get all the registered artists in the server.

        Args:
            music_folder_id: A music folder ID to reduce the scope of the
                artists to return.

        Returns:
            A list with all the info about all the received artists.
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

    def get_artist(self, artist_id: str) -> Artist:
        """Get all the info about an artist.

        Args:
            artist_id: The ID of the artist to get its info.

        Returns:
            An object that contains all the info about
                the requested artist.
        """

        response = self.api.json_request("getArtist", {"id": artist_id})["artist"]

        return Artist(self.subsonic, **response)

    def get_artists_indexed(
        self, music_folder_id: str, modified_since: int
    ) -> ArtistIndex:
        """Get all the registered artist indexed alphabetically.

        Args:
            music_folder_id: A music folder ID to reduce the scope
                where the artist should be from.
            modified_since: Time in milliseconds since the artist have changed
                its collection.

        Returns:
            An object containt all the artist alphabetically indexed.
        """

        response = self.api.json_request(
            "getIndexes",
            {"musicFolderId": music_folder_id, "ifModifiedSince": modified_since},
        )["indexes"]

        return ArtistIndex(subsonic=self.subsonic, **response)

    def get_album(self, album_id: str) -> Album:
        """Get all the info about an album.

        Args:
            album_id: The ID of the album to get its info.

        Returns:
            An object that contains all the info about
                the requested album.
        """

        response = self.api.json_request("getAlbum", {"id": album_id})["album"]

        return Album(self.subsonic, **response)

    def get_album_info_non_id3(self, album_id: str) -> AlbumInfo:
        """Get all the extra info about an album. Not organized according
        ID3 tags.

        Args:
            album_id: The ID of the album to get its extra info.

        Returns:
            An object that contains all the extra info about
                the requested album.
        """

        response = self.api.json_request("getAlbumInfo", {"id": album_id})["albumInfo"]

        return AlbumInfo(self.subsonic, album_id, **response)

    def get_album_info(self, album_id: str) -> AlbumInfo:
        """Get all the extra info about an album.

        Args:
            album_id: The ID of the album to get its extra info.

        Returns:
            An object that contains all the extra info about
                the requested album.
        """

        response = self.api.json_request("getAlbumInfo2", {"id": album_id})["albumInfo"]

        return AlbumInfo(self.subsonic, album_id, **response)

    def get_song(self, song_id: str) -> Song:
        """Get all the info about a song.

        Args:
            song_id: The ID of the song to get its info.

        Returns:
            An object that contains all the info
                about the requested song.
        """

        response = self.api.json_request("getSong", {"id": song_id})["song"]

        return Song(self.subsonic, **response)

    def get_videos(self) -> list[Video]:
        """Get all the registered videos in the server.

        Returns:
            A list with all the info about al the videos
                available in the server.
        """

        response = self.api.json_request("getVideos")["videos"]["video"]

        return [Video(self.subsonic, **video) for video in response]

    def get_video(self, video_id: str) -> Video | None:
        """Get all the info about a video.

        Args:
            video_id: The ID of the video to get its info.

        Returns:
            An object that contains all the info about
                the requested video.
        """

        videos = self.get_videos()

        for video in videos:
            if video.id == video_id:
                return video

        return None

    def get_video_info(self, video_id: str) -> VideoInfo:
        """Get all the extra info about a video.

        Args:
            video_id: The ID of the video to get its extra info.

        Returns:
            An object that holds all the extra info about
                the requested video.
        """

        response = self.api.json_request("getVideoInfo", {"id": video_id})["videoInfo"]

        return VideoInfo(self.subsonic, video_id=video_id, **response)

    def get_artist_info_non_id3(
        self,
        artist_id: str,
        max_similar_artists: int | None = None,
        include_similar_artists_not_present: bool | None = None,
    ) -> ArtistInfo:
        """Get all the extra info about an artist. Not organized according
        ID3 tags.

        Args:
            artist_id: The ID of the artist to get its extra info.
            max_similar_artists: The max number of similar artists to
                return.
            include_similar_artists_not_present: Include similar artists
                that are not present in any the media library.

        Returns:
            An object that contains all the extra info about
                the requested artist.
        """

        response = self.api.json_request(
            "getArtistInfo",
            {
                "id": artist_id,
                "count": max_similar_artists,
                "includeNotPresent": include_similar_artists_not_present,
            },
        )["artistInfo"]

        return ArtistInfo(self.subsonic, artist_id, **response)

    def get_artist_info(
        self,
        artist_id: str,
        max_similar_artists: int | None = None,
        include_similar_artists_not_present: bool | None = None,
    ) -> ArtistInfo:
        """Get all the extra info about an artist.

        Args:
            artist_id: The ID of the artist to get its extra info.
            max_similar_artists: The max number of similar artists to
                return.
            include_similar_artists_not_present: Include similar artists
                that are not present in any the media library.

        Returns:
            An object that contains all the extra info about
                the requested artist.
        """

        response = self.api.json_request(
            "getArtistInfo2",
            {
                "id": artist_id,
                "count": max_similar_artists,
                "includeNotPresent": include_similar_artists_not_present,
            },
        )["artistInfo2"]

        return ArtistInfo(self.subsonic, artist_id, **response)

    def get_similar_songs_non_id3(
        self, song_id: str, song_count: int | None = None
    ) -> list[Song]:
        """Get similar songs to the given one. Not organized according
        ID3 tags.

        Args:
            song_id: The ID of the song to get similar songs.
            song_count: The number of songs to return.

        Returns:
            A list that contains all the songs that are similar
                to the given one.
        """

        response = self.api.json_request(
            "getSimilarSongs", {"id": song_id, "count": song_count}
        )["similarSongs"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]

    def get_similar_songs(
        self, song_id: str, song_count: int | None = None
    ) -> list[Song]:
        """Get similar songs to the given one.

        Args:
            song_id: The ID of the song to get similar songs.
            song_count: The number of songs to return.

        Returns:
            A list that contains all the songs that are similar
                to the given one.
        """

        response = self.api.json_request(
            "getSimilarSongs2", {"id": song_id, "count": song_count}
        )["similarSongs2"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]

    def get_top_songs(self, artist_name: str, max_num_of_songs: int) -> list[Song]:
        """Get the top rated songs in the server.

        Args:
            artist_name: Limit the ranked songs to the ones created by the
                given artist.
            max_num_of_songs: The max number of songs to return.

        Returns:
            A list that contains the top rated songs of the server.
        """

        response = self.api.json_request(
            "getTopSongs", {"artist": artist_name, "count": max_num_of_songs}
        )["topSongs"]["song"]

        return [Song(subsonic=self.subsonic, **song) for song in response]
