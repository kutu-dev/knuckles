from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from ..exceptions import NoApiAccess


class User:
    """Representation of all the data related to a user in Subsonic."""

    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
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
    ) -> None:
        self.subsonic = subsonic
        self.username = username
        self.password = password
        self.email = email
        self.ldap_authenticated = ldap_authenticated
        self.admin_role = admin_role
        self.settings_role = settings_role
        self.stream_role = stream_role
        self.jukebox_role = jukebox_role
        self.download_role = download_role
        self.upload_role = upload_role
        self.playlist_role = playlist_role
        self.cover_art_role = cover_art_role
        self.comment_role = comment_role
        self.podcast_role = podcast_role
        self.share_role = share_role
        self.video_conversion_role = video_conversion_role
        self.music_folder_id = music_folder_id
        self.max_bit_rate = max_bit_rate

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
        """Returns the function to the same user with the maximum possible
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

        #! TODO This is bad
        if not self.password or not self.email:
            raise NoApiAccess()

        self.subsonic.user_management.create_user(
            self.username,
            self.password,
            self.email,
            self.ldap_authenticated,
            self.admin_role,
            self.settings_role,
            self.stream_role,
            self.jukebox_role,
            self.download_role,
            self.upload_role,
            self.playlist_role,
            self.cover_art_role,
            self.comment_role,
            self.podcast_role,
            self.share_role,
            self.video_conversion_role,
            self.music_folder_id,
            self.max_bit_rate,
        )  # type: ignore[union-attr]

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

        self.subsonic.user_management.update_user(
            self.username,
            self.password,
            self.email,
            self.ldap_authenticated,
            self.admin_role,
            self.settings_role,
            self.stream_role,
            self.jukebox_role,
            self.download_role,
            self.upload_role,
            self.playlist_role,
            self.cover_art_role,
            self.comment_role,
            self.podcast_role,
            self.share_role,
            self.video_conversion_role,
            self.music_folder_id,
            self.max_bit_rate,
        )  # type: ignore[union-attr]

        return self

    def delete(self) -> Self:
        """Calls the "deleteUser" endpoint of the API.

        :raises NoApiAccess: Raised if the subsonic property is None.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__check_api_access()

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
