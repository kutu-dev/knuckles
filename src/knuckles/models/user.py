from typing import TYPE_CHECKING, Self

from ..exceptions import NoApiAccess

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class User:
    def __init__(
        self,
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
        # Internal
        subsonic: "Subsonic | None" = None,
    ) -> None:
        self.subsonic = subsonic
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

    def __check_api_access(self) -> None:
        """Check if the object has a valid subsonic property

        :raises NoApiAccess: _description_
        """

        if self.subsonic is None:
            raise NoApiAccess(
                (
                    "This user isn't associated with a Subsonic object."
                    + "A non None value in the subsonic property is required"
                )
            )

    def generate(self) -> "User":
        """Returns the function to the the same user with the maximum possible
        information from the Subsonic API.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: A new user object with all the data updated.
        :rtype: User
        """

        self.__check_api_access()

        return self.subsonic.user_management.get_user(  # type: ignore[union-attr]
            self.username
        )

    def create(self) -> Self:
        """Calls the "createUser" endpoint of the API.

        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__check_api_access()

        self.subsonic.user_management.create_user(self)  # type: ignore[union-attr]

        return self

    def update(self) -> Self:
        """Calls the "updateUser" endpoint of the API.

        The user will be updated with
        the data stored in the properties of the object itself.

        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__check_api_access()

        self.subsonic.user_management.update_user(self)  # type: ignore[union-attr]

        return self

    def delete(self) -> Self:
        """Calls the "deleteUser" endpoint of the API.

        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.subsonic.user_management.delete_user(  # type: ignore[union-attr]
            self.username
        )

        return self

    def change_password(self, new_password: str) -> Self:
        """Calls the "changePassword" endpoint of the API.

        The password is changed with the user corresponding
        to the username property of the object.

        :param new_password: The new password for the user.
        :type new_password: str
        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__check_api_access()

        self.subsonic.user_management.change_password(  # type: ignore[union-attr]
            self.username, new_password
        )

        return self
