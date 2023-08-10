from .api import Api
from .bookmarks import Bookmarks
from .browsing import Browsing
from .chat import Chat
from .internet_radio import InternetRadio
from .jukebox import JukeboxControl
from .media_annotation import MediaAnnotation
from .media_library_scanning import MediaLibraryScanning
from .playlists import Playlists
from .podcast import Podcast
from .sharing import Sharing
from .system import System
from .user_management import UserManagement


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
        self.playlists = Playlists(self.api, self)
        self.media_retrieval = None
        self.media_annotation = MediaAnnotation(self.api, self)
        self.sharing = Sharing(self.api, self)
        self.podcast = Podcast(self.api, self)
        self.jukebox = JukeboxControl(self.api, self)
        self.internet_radio = InternetRadio(self.api, self)
        self.chat = Chat(self.api, self)
        self.user_management = UserManagement(self.api, self)
        self.bookmarks = Bookmarks(self.api, self)
        self.media_library_scanning = MediaLibraryScanning(self.api)
        self.media_library_scanning = MediaLibraryScanning(self.api)
