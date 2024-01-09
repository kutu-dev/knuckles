from typing import TYPE_CHECKING, Any

from .api import Api
from .models.user import User

if TYPE_CHECKING:
    from .subsonic import Subsonic


class UserManagement:
    """Class that contains all the methods needed to interact
    with the user management calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/user-management/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_user(self, username: str) -> User:
        """Calls the "getUser" endpoint of the API.

        :param username: The username of the user to get.
        :type username: str
        :return: A User object will all the data of the requested user.
        :rtype: User
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
        """Calls the "getUsers" endpoint of the API.

        :return: A list of User objects.
        :rtype: list[User]
        """

        request = self.api.json_request("getUsers")["users"]["user"]

        users: list[User] = []
        for user in request:
            users.append(User(
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
            ))

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
        """Calls the "updateUser" endpoint of the API.

        The user to update with the new data will be
        selected with the username property of the User object.

        :param updated_data_user: A user object with the updated data.
        :type updated_data_user: User
        :return: The object itself to allow method chaining.
        :rtype: User
        """

        self.api.json_request("updateUser", {
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
            })

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
        """Calls the "deleteUser" endpoint of the API.

        :param username: The username of the user to delete.
        :type username: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("deleteUser", {"username": username})

        return self.subsonic

    def change_password(self, username: str, new_password: str) -> "Subsonic":
        """Calls the "changePassword" endpoint of the API.

        :param username: The username of the user to change its password.
        :type username: str
        :param new_password: The new password of the user
        :type new_password: str
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.api.json_request(
            "changePassword", {"username": username, "password": new_password}
        )

        return self.subsonic
