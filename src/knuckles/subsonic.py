from __future__ import annotations

from .api import Api
from .browsing import Browsing
from .chat import Chat
from .jukebox import JukeboxControl
from .media_annotation import MediaAnnotation
from .media_library_scanning import MediaLibraryScanning
from .system import System


class Subsonic:
    """The main class of the package, is used to interact with a Subsonic API."""

    def __init__(
        self,
        url: str,
        user: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
    ) -> None:
        """The main class of the package, is used to interact with a Subsonic API.

        :param url: The url of the Subsonic server.
        :type url: str
        :param user: The user to authenticate with
        :type user: str
        :param password: The password to authenticate with
        :type password: str
        :param client: A unique string identifying the client application.
        :type client: str
        :param use_https: If the requests should be sended using HTTPS,
            defaults to True
        :type use_https: bool, optional
        :param use_token: If the connection should send to the server the clean password
            or encode it in a token with a random salt, defaults to True
        :type use_token: bool, optional
        """

        self.api = Api(url, user, password, client, use_https, use_token)
        self.system = System(self.api)
        self.browsing = Browsing(self.api, self)
        self.lists = None  #! ?
        self.searching = None  #! ?
        self.playlists = None
        self.media_retrieval = None
        self.media_annotation = MediaAnnotation(self.api, self)
        self.sharing = None
        self.podcast = None
        self.jukebox = JukeboxControl(self.api, self)
        self.internet_radio = None
        self.chat = Chat(self.api, self)
        self.user_management = None
        self.bookmarks = None
        self.media_library_scanning = MediaLibraryScanning(self.api)
