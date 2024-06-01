from typing import TYPE_CHECKING, Any

from ._api import Api
from .models._album import Album
from .models._now_playing_entry import NowPlayingEntry
from .models._song import Song
from .models._starred_content import StarredContent

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Lists:
    """Class that contains all the methods needed to interact with the
    [lists endpoints](https://opensubsonic.netlify.app/categories/lists)
    in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def _get_album_list_generic(
        self,
        list_type: str,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
        id3: bool = True,
        **extra_params: Any,
    ) -> list[Album]:
        """Make a GET requests to the "getAlbumList", used because this
        endpoint can generate a lot of different types of list.

        Args:
            list_type: The name of the type of list to request to the server.
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.
            id3: If the request should be send to the ID3 or non-ID3 version
                of the endpoint.

        Returns:
            A list with all the info about the received albums.
        """

        response = self.api.json_request(
            "getAlbumList2" if id3 else "getAlbumList",
            {
                "type": list_type,
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
        """Get a random list of albums from the server. Not organized
        according ID3 tags.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about random albums.
        """

        return self._get_album_list_generic(
            "random", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_newest_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the newest added to the oldest. Not organized according ID3 tags.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from newest to oldest.
        """

        return self._get_album_list_generic(
            "newest", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_highest_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the highest rated to the lowest ones. Not organized according ID3 tags.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the highest rated to the lowest ones.
        """

        return self._get_album_list_generic(
            "highest", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_frequent_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the most frequent listened to the least.
        Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the most frequent listened to the least.
        """

        return self._get_album_list_generic(
            "frequent", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_recent_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the most recent listened to the least.
        not organized according id3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the most recent listened to the least.
        """

        return self._get_album_list_generic(
            "recent", num_of_albums, album_list_offset, music_folder_id, False
        )

    def get_album_list_alphabetical_by_name_non_id3(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized alphabetically
        by their names. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized alphabetically by their names.
        """

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
        """Get a list of albums from the server organized alphabetically
        by their artist name. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized alphabetically by their artist name.
        """

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
        """Get a list of the albums that have been starred by
        the authenticated user. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                starred by the user.
        """

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
        """Get all the album registered by the server that were created between
        the given year range.

        Args:
            from_year: The minimum year of the range where the albums
                were created.
            to_year: The maximum year of the range where the albums
                were created.
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                that where released in the given year range.
        """

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
        """Get all the albums that are tagged with the given genre.
        Not organized according ID3 tags.

        Args:
            genre_name: The name of the genre that all the albums
                must be tagged with.
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                that are tagged with the given album.
        """

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
        """Get a random list of albums from the server.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about random albums.
        """

        return self._get_album_list_generic(
            "random", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_newest(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the newest added to the oldest. Not organized according ID3 tags.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from newest to oldest.
        """

        return self._get_album_list_generic(
            "newest", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_highest(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the highest rated to the lowest ones. Not organized according ID3 tags.

        Args:
            num_of_albums: The number of albums to be in the list.
            album_list_offset: The number of album to offset in the list,
                useful for pagination.
            music_folder_id: The ID of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the highest rated to the lowest ones.
        """

        return self._get_album_list_generic(
            "highest", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_frequent(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the most frequent listened to the least.
        Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the most frequent listened to the least.
        """

        return self._get_album_list_generic(
            "frequent", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_recent(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized from
        the most recent listened to the least.
        not organized according id3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized from the most recent listened to the least.
        """

        return self._get_album_list_generic(
            "recent", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_alphabetical_by_name(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized alphabetically
        by their names. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized alphabetically by their names.
        """

        return self._get_album_list_generic(
            "alphabeticalByName", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_alphabetical_by_artist(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of albums from the server organized alphabetically
        by their artist name. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                organized alphabetically by their artist name.
        """

        return self._get_album_list_generic(
            "alphabeticalByArtist", num_of_albums, album_list_offset, music_folder_id
        )

    def get_album_list_starred(
        self,
        num_of_albums: int | None = None,
        album_list_offset: int | None = None,
        music_folder_id: str | None = None,
    ) -> list[Album]:
        """Get a list of the albums that have been starred by
        the authenticated user. Not organized according ID3 tags.

        args:
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                starred by the user.
        """

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
        """Get all the album registered by the server that were created between
        the given year range.

        Args:
            from_year: The minimum year of the range where the albums
                were created.
            to_year: The maximum year of the range where the albums
                were created.
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                that where released in the given year range.
        """

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
        """Get all the albums that are tagged with the given genre. Not organized
        according ID3 tags.

        Args:
            genre_name: The name of the genre that all the albums must be tagged
                with.
            num_of_albums: the number of albums to be in the list.
            album_list_offset: the number of album to offset in the list,
                useful for pagination.
            music_folder_id: the id of a music folder to list where the album
                are from.

        Returns:
            A list that contains the info about the albums
                that are tagged with the given album.
        """

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
        """Get random songs registered in the server.

        Args:
            num_of_songs: The number of songs to return.
            genre_name: The genre that the songs must
                have it tagged on them.
            from_year: The minimum year where the songs
                were released.
            to_year: The maximum year where the songs
                were released.
            music_folder_id: An ID of a music folder
                to limit where the songs should be from.

        Returns:
            A list that contains all the info about
                that were randomly selected by the server.
        """

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
        """Get all the songs tagged with the given genre.

        Args:
            genre_name: The name of the genre that all the songs
                must be tagged with.
            num_of_songs: The number of songs that the list
                should have.
            song_list_offset: the number of songs to offset in the list,
                useful for pagination.
            music_folder_id: An ID of a music folder where all the songs
                should be from.

        Returns:
            A list that contains all the info about
                that are tagged with the given genre.
        """

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
        """Get the songs that are currently playing by all the users.

        Returns:
            A list that holds all the info about all the
                song that are current playing by all the users.
        """

        response = self.api.json_request("getNowPlaying")["nowPlaying"]["entry"]

        return [NowPlayingEntry(subsonic=self.subsonic, **entry) for entry in response]

    def get_starred_non_id3(self, music_folder_id: str | None = None) -> StarredContent:
        """Get all the songs, albums and artists starred by the authenticated
        user. Not organized according ID3 tags.

        Args:
            music_folder_id: An ID of a music folder where all the songs
                albums, and artists should be from.

        Returns:
            An object that holds all the info about all the starred
                songs, albums and artists by the user.
        """

        response = self.api.json_request(
            "getStarred", {"musicFolderId": music_folder_id}
        )["starred"]

        return StarredContent(subsonic=self.subsonic, **response)

    def get_starred(self, music_folder_id: str | None = None) -> StarredContent:
        """Get all the songs, albums and artists starred by the authenticated
        user.

        Args:
            music_folder_id: An ID of a music folder where all the songs
                albums, and artists should be from.

        Returns:
            An object that holds all the info about all the starred
                songs, albums and artists by the user.
        """

        response = self.api.json_request(
            "getStarred2", {"musicFolderId": music_folder_id}
        )["starred2"]

        return StarredContent(subsonic=self.subsonic, **response)
