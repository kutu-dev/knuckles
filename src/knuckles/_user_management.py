from typing import TYPE_CHECKING

from ._api import Api
from .models._user import User

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class UserManagement:
    """Class that contains all the methods needed to interact with the
    [user management endpoints](https://opensubsonic.netlify.app/
    categories/user-management/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_user(self, username: str) -> User:
        """Get all the info about a user.

        Args:
            username: The username of the user to get its info.

        Returns:
            An object that holds all the info about the requested user.
        """
        request = self.api.json_request("getUser", {"username": username})["user"]

        return User(
            self.subsonic,
            request["username"],
            request["password"],
            request["email"],
            request["ldapAuthenticated"],
            request["adminRole"],
            request["settingsRole"],
            request["streamRole"],
            request["jukeboxRole"],
            request["downloadRole"],
            request["uploadRole"],
            request["playlistRole"],
            request["coverArtRole"],
            request["commentRole"],
            request["podcastRole"],
            request["shareRole"],
            request["videoConversionRole"],
            request["musicFolderId"],
            request["maxBitRate"],
        )

    def get_users(self) -> list[User]:
        """Get all the users registered in the server.

        Returns:
            A list that holds all the info about all the available
                users in the server.
        """

        request = self.api.json_request("getUsers")["users"]["user"]

        users: list[User] = []
        for user in request:
            users.append(
                User(
                    self.subsonic,
                    user["username"],
                    user["password"],
                    user["email"],
                    user["ldapAuthenticated"],
                    user["adminRole"],
                    user["settingsRole"],
                    user["streamRole"],
                    user["jukeboxRole"],
                    user["downloadRole"],
                    user["uploadRole"],
                    user["playlistRole"],
                    user["coverArtRole"],
                    user["commentRole"],
                    user["podcastRole"],
                    user["shareRole"],
                    user["videoConversionRole"],
                    user["musicFolderId"],
                    user["maxBitRate"],
                )
            )

        return users

    def create_user(
        self,
        username: str,
        password: str,
        email: str,
        ldap_authenticated: bool | None = None,
        admin_role: bool | None = None,
        settings_role: bool | None = None,
        stream_role: bool | None = None,
        jukebox_role: bool | None = None,
        download_role: bool | None = None,
        upload_role: bool | None = None,
        playlist_role: bool | None = None,
        cover_art_role: bool | None = None,
        comment_role: bool | None = None,
        podcast_role: bool | None = None,
        share_role: bool | None = None,
        video_conversion_role: bool | None = None,
        music_folder_id: list[str] | None = None,
        max_bit_rate: int | None = None,
    ) -> User:
        """Create a new user in the server.

        Args:
            username: The username of the user to create.
            password: The password of the user to create.
            email: The email of the user to create.
            ldap_authenticated: If the user is authenticated in a LDAP server.
            admin_role: If the user should be an administrator.
            settings_role: If the user is allowed to change its
                personal settings and password.
            stream_role: If the user should be allowed to stream songs and
                videos.
            jukebox_role: If the user should be able to play songs in the
                jukebox.
            download_role: If the user should be able to download files from
                the server.
            upload_role: If the user should be allowed to upload files to
                the server.
            playlist_role: If the user should be able to create and delete
                playlists.
            cover_art_role: If the user should be allowed to change cover
                art and tags of songs.
            comment_role: If the user is allowed to create and edit
                comments and ratings.
            podcast_role: If the user should be allowed to administrate
                podcasts.
            share_role: If the user should be able to create share links.
            video_conversion_role: If the use should be allowed to
                start video conversion in the server.
            music_folder_id: A list of IDs where the used should have access
                to. If no one is specified all of them will be accessible.
            max_bit_rate: The max bitrate that the user should be able to
                stream.

        Returns:
            An object that holds all the info about the new created user.
        """

        self.api.json_request(
            "createUser",
            {
                "username": username,
                "password": password,
                "email": email,
                "ldapAuthenticated": ldap_authenticated,
                "adminRole": admin_role,
                "settingsRole": settings_role,
                "streamRole": stream_role,
                "jukeboxRole": jukebox_role,
                "downloadRole": download_role,
                "uploadRole": upload_role,
                "playlistRole": playlist_role,
                "coverArtRole": cover_art_role,
                "commentRole": comment_role,
                "podcastRole": podcast_role,
                "shareRole": share_role,
                "videoConversionRole": video_conversion_role,
                "musicFolderId": music_folder_id,
                "maxBitRate": max_bit_rate,
            },
        )

        # Attach the Subsonic object
        new_user = User(
            self.subsonic,
            username,
            password,
            email,
            ldap_authenticated,
            admin_role,
            settings_role,
            stream_role,
            jukebox_role,
            download_role,
            upload_role,
            playlist_role,
            cover_art_role,
            comment_role,
            podcast_role,
            share_role,
            video_conversion_role,
            music_folder_id,
            max_bit_rate,
        )

        return new_user

    def update_user(
        self,
        username: str,
        password: str | None = None,
        email: str | None = None,
        ldap_authenticated: bool | None = None,
        admin_role: bool | None = None,
        settings_role: bool | None = None,
        stream_role: bool | None = None,
        jukebox_role: bool | None = None,
        download_role: bool | None = None,
        upload_role: bool | None = None,
        playlist_role: bool | None = None,
        cover_art_role: bool | None = None,
        comment_role: bool | None = None,
        podcast_role: bool | None = None,
        share_role: bool | None = None,
        video_conversion_role: bool | None = None,
        music_folder_id: list[str] | None = None,
        max_bit_rate: int | None = None,
    ) -> User:
        """Update the info of a user.

        Args:
            username: The username of the user to update.
            password: The password of the user to update.
            email: The email of the user to update.
            ldap_authenticated: If the user is authenticated in a LDAP server.
            admin_role: If the user should be an administrator.
            settings_role: If the user is allowed to change its
                personal settings and password.
            stream_role: If the user should be allowed to stream songs and
                videos.
            jukebox_role: If the user should be able to play songs in the
                jukebox.
            download_role: If the user should be able to download files from
                the server.
            upload_role: If the user should be allowed to upload files to
                the server.
            playlist_role: If the user should be able to create and delete
                playlists.
            cover_art_role: If the user should be allowed to change cover
                art and tags of songs.
            comment_role: If the user is allowed to create and edit
                comments and ratings.
            podcast_role: If the user should be allowed to administrate
                podcasts.
            share_role: If the user should be able to create share links.
            video_conversion_role: If the use should be allowed to
                start video conversion in the server.
            music_folder_id: A list of IDs where the used should have access
                to. If no one is specified all of them will be accessible.
            max_bit_rate: The max bitrate that the user should be able to
                stream.

        Returns:
            An object that holds all the info about the update user.
        """

        self.api.json_request(
            "updateUser",
            {
                "username": username,
                "password": password,
                "email": email,
                "ldapAuthenticated": ldap_authenticated,
                "adminRole": admin_role,
                "settingsRole": settings_role,
                "streamRole": stream_role,
                "jukeboxRole": jukebox_role,
                "downloadRole": download_role,
                "uploadRole": upload_role,
                "playlistRole": playlist_role,
                "coverArtRole": cover_art_role,
                "commentRole": comment_role,
                "podcastRole": podcast_role,
                "shareRole": share_role,
                "videoConversionRole": video_conversion_role,
                "musicFolderId": music_folder_id,
                "maxBitRate": max_bit_rate,
            },
        )

        updated_user = User(
            self.subsonic,
            username,
            password,
            email,
            ldap_authenticated,
            admin_role,
            settings_role,
            stream_role,
            jukebox_role,
            download_role,
            upload_role,
            playlist_role,
            cover_art_role,
            comment_role,
            podcast_role,
            share_role,
            video_conversion_role,
            music_folder_id,
            max_bit_rate,
        )

        return updated_user

    def delete_user(self, username: str) -> "Subsonic":
        """Delete a user from the server.

        Args:
            username: The username of the user to delete.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("deleteUser", {"username": username})

        return self.subsonic

    def change_password(self, username: str, new_password: str) -> "Subsonic":
        """Change the password of a user.

        Args:
            username: The username of the user to change its password.
            new_password: The new password for the user.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request(
            "changePassword", {"username": username, "password": new_password}
        )

        return self.subsonic
