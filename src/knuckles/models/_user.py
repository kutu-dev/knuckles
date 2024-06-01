from typing import TYPE_CHECKING, Self

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from ..exceptions import MissingRequiredProperty


class User(Model):
    """Object that holds all the info about a user.

    Attributes:
        username (str): The username of the user.
        password (str | None): The password of the user.
        email (str | None): The email of the user.
        ldap_authenticated (bool | None): If the user is has been
            authenticated using LDAP.
        admin_role (bool | None): If the user has access to admin functionalities.
        settings_role (bool | None): If the user has access to change the settings
            of the server.
        stream_role (bool | None): If the user has access to stream media.
        jukebox_role (bool | None): If the user has access to control the jukebox.
        download_role (bool | None): If the user has access to download media.
        upload_role (bool | None): If the user has access to upload media.
        playlist_role (bool | None): If the user has access to create, edit and
            delete playlists.
        cover_art_role (bool | None): If the user has access to manipulate
            cover arts of media.
        comment_role (bool | None): If the user has access to manipulate
            comments.
        podcast_role (bool | None): If the user has access to manipulate podcasts.
        share_role (bool | None): If the user has access to create, modify and
            delete shares.
        video_conversion_role (bool | None): If the user is able to trigger
            video conversions.
        music_folder_id (list[str] | None): The IDs of the music folders
            where the user is able to access content from.
        max_bit_rate (int | None): The max bit rate the user can stream.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
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
        super().__init__(subsonic)

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

    def generate(self) -> "User":
        """Return a new user object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.user_management.get_user(self.username)

    def create(self) -> Self:
        """Create a new user with the attributes of the model.

        Raises:
            MissingRequiredProperty: Raised if a required property to create
                the user is missing.
        Returns:
            The object itself.
        """

        if not self.email:
            raise MissingRequiredProperty(
                "You must provide an email in the email property of the model"
            )

        if not self.password:
            raise MissingRequiredProperty(
                "You must provide an password in the password property of the model"
            )

        self._subsonic.user_management.create_user(
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
        )

        return self

    def update(self) -> Self:
        """Updates the info about the user in the server with
        the one in the model.

        Returns:
            The object itself.
        """

        self._subsonic.user_management.update_user(
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
        )

        return self

    def delete(self) -> Self:
        """Delete the user from the server.

        Returns:
            The object itself.
        """

        self._subsonic.user_management.delete_user(self.username)

        return self

    def change_password(self, new_password: str) -> Self:
        """Change the password of the user.

        Args:
            new_password: The new password for the user

        Returns:
            The object itself.
        """

        self._subsonic.user_management.change_password(self.username, new_password)

        return self
