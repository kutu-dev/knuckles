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

    @staticmethod
    def __user_properties_to_json(user: User) -> dict[str, Any]:
        """Converts the data in a User object to a dictionary
        with the keys used in all the user related calls to the API.

        :param user: The user to convert to a dictionary
        :type user: User
        :return: The dictionary with the data and valid keys to the API.
        :rtype: dict[str, Any]"""

        return {
            "username": user.username,
            "email": user.email,
            "scrobblingEnabled": user.scrobbling_enabled,
            "adminRole": user.admin_role,
            "settingsRole": user.settings_role,
            "downloadRole": user.download_role,
            "uploadRole": user.upload_role,
            "playlistRole": user.playlist_role,
            "coverArtRole": user.cover_art_role,
            "commentRole": user.comment_role,
            "podcastRole": user.podcast_role,
            "streamRole": user.stream_role,
            "jukeboxRole": user.jukebox_role,
            "shareRole": user.share_role,
            "videoConversionRole": user.video_conversion_role,
        }

    def get_user(self, username: str) -> User:
        """Calls the "getUser" endpoint of the API.

        :param username: The username of the user to get.
        :type username: str
        :return: A User object will all the data of the requested user.
        :rtype: User
        """

        request = self.api.json_request("getUser", {"username": username})["user"]

        return User(subsonic=self.subsonic, **request)

    def get_users(self) -> list[User]:
        """Calls the "getUsers" endpoint of the API.

        :return: A list of User objects.
        :rtype: list[User]
        """

        request = self.api.json_request("getUsers")["users"]["user"]

        users = [User(subsonic=self.subsonic, **user) for user in request]

        return users

    def create_user(self, new_user: User) -> User:
        """Calls the "createUser" endpoint of the API.

        :param new_user: A user object with all the data for the new user.
        :type new_user: User
        :return: The object itself to allow method chaining.
        :rtype: User
        """

        user_json_data = self.__user_properties_to_json(new_user)

        self.api.json_request("createUser", {**user_json_data})

        # Attach the Subsonic object
        new_user.subsonic = self.subsonic

        return new_user

    def update_user(self, updated_data_user: User) -> User:
        """Calls the "updateUser" endpoint of the API.

        The user to update with the new data will be
        selected with the username property of the User object.

        :param updated_data_user: A user object with the updated data.
        :type updated_data_user: User
        :return: The object itself to allow method chaining.
        :rtype: User
        """

        user_json_data = self.__user_properties_to_json(updated_data_user)

        self.api.json_request("updateUser", {**user_json_data})

        # Attach the Subsonic object
        updated_data_user.subsonic = self.subsonic

        return updated_data_user

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
