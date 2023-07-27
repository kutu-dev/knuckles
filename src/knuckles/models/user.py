from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class User:
    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        username: str,
        email: str,
        scrobblingEnabled: bool = False,
        adminRole: bool = False,
        settingsRole: bool = False,
        downloadRole: bool = False,
        uploadRole: bool = False,
        playlistRole: bool = False,
        coverArtRole: bool = False,
        commentRole: bool = False,
        podcastRole: bool = False,
        streamRole: bool = False,
        jukeboxRole: bool = False,
        shareRole: bool = False,
        videoConversionRole: bool = False,
    ) -> None:
        self.__subsonic = subsonic
        self.username = username
        self.email = email
        self.scrobbling_enabled = scrobblingEnabled
        self.admin_role = adminRole
        self.settings_role = settingsRole
        self.download_role = downloadRole
        self.upload_role = uploadRole
        self.playlist_role = playlistRole
        self.cover_art_role = coverArtRole
        self.comment_role = commentRole
        self.podcast_role = podcastRole
        self.stream_role = streamRole
        self.jukebox_role = jukeboxRole
        self.share_role = shareRole
        self.video_conversion_role = videoConversionRole

    def generate(self) -> "User":
        """Returns the function to the the same user with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new user object with all the data updated.
        :rtype: User
        """

        return self.__subsonic.user_management.get_user(self.username)

    def create(self) -> Self:
        """Calls the "createUser" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.user_management.create_user(self)

        return self

    def update(self) -> Self:
        """Calls the "updateUser" endpoint of the API.

        The user will be updated with
        the data stored in the properties of the object itself.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.user_management.update_user(self)

        return self

    def delete(self) -> Self:
        """Calls the "deleteUser" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.user_management.delete_user(self.username)

        return self

    def change_password(self, new_password: str) -> Self:
        """Calls the "changePassword" endpoint of the API.

        The password is changed with the user corresponding
        to the username property of the object.

        :param new_password: The new password for the user.
        :type new_password: str
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.user_management.change_password(self.username, new_password)

        return self
