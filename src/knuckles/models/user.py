from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from ..exceptions import NoApiAccess


class User:
    """Representation of all the data related to a user in Subsonic."""

    def __init__(
        self,
        # Subsonic fields
        username: str,
        email: str | None = None,
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
        """Representation of all the data related to a user in Subsonic.

        :param username: The username of the user
        :type username: str
        :param email: The email of the user
        :type email: str
        :param scrobblingEnabled: If the user can do scrobbling,
            defaults to False.
        :type scrobblingEnabled: bool, optional
        :param adminRole: If the user has admin privileges,
            overrides all the rest of roles,defaults to False.
        :type adminRole: bool, optional
        :param settingsRole: If the user can modify global settings,
            defaults to False.
        :type settingsRole: bool, optional
        :param downloadRole: If the user can download songs, defaults to False.
        :type downloadRole: bool, optional
        :param uploadRole: If the user can upload data to the server,
            defaults to False.
        :type uploadRole: bool, optional
        :param playlistRole: If the user can use playlist, defaults to False.
        :type playlistRole: bool, optional
        :param coverArtRole: If the user can access cover arts,
            defaults to False.
        :type coverArtRole: bool, optional
        :param commentRole: If the user can do comments, defaults to False.
        :type commentRole: bool, optional
        :param podcastRole: If the user can listen to podcasts,
            defaults to False.
        :type podcastRole: bool, optional
        :param streamRole: If the user can listen media with streaming,
            defaults to False.
        :type streamRole: bool, optional
        :param jukeboxRole: If the user can use the jukebox, defaults to False
        :type jukeboxRole: bool, optional
        :param shareRole: If the user can use sharing capabilities,
            defaults to False
        :type shareRole: bool, optional
        :param videoConversionRole: If the user can do video conversion,
            defaults to False
        :type videoConversionRole: bool, optional
        :param subsonic: The subsonic object to make all the internal requests with it,
            defaults to None
        :type subsonic: Subsonic | None, optional
        """

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
