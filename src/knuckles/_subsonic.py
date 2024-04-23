from ._api import Api, RequestMethod
from ._bookmarks import Bookmarks
from ._browsing import Browsing
from ._chat import Chat
from ._internet_radio import InternetRadio
from ._jukebox import JukeboxControl
from ._lists import Lists
from ._media_annotation import MediaAnnotation
from ._media_library_scanning import MediaLibraryScanning
from ._media_retrieval import MediaRetrieval
from ._playlists import Playlists
from ._podcast import Podcast
from ._searching import Searching
from ._sharing import Sharing
from ._system import System
from ._user_management import UserManagement


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
        request_method: RequestMethod = RequestMethod.POST,
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
        :param use_https: If the requests should be sent using HTTPS,
            defaults to True
        :type use_https: bool, optional
        :param use_token: If the connection should send to the server the clean password
            or encode it in a token with a random salt, defaults to True
        :type use_token: bool, optional
        """

        self.api = Api(
            url, user, password, client, use_https, use_token, request_method
        )
        self.system = System(self.api, self)
        self.browsing = Browsing(self.api, self)
        self.lists = Lists(self.api, self)
        self.searching = Searching(self.api, self)
        self.playlists = Playlists(self.api, self)
        self.media_retrieval = MediaRetrieval(self.api, self)
        self.media_annotation = MediaAnnotation(self.api, self)
        self.sharing = Sharing(self.api, self)
        self.podcast = Podcast(self.api, self)
        self.jukebox = JukeboxControl(self.api, self)
        self.internet_radio = InternetRadio(self.api, self)
        self.chat = Chat(self.api, self)
        self.user_management = UserManagement(self.api, self)
        self.bookmarks = Bookmarks(self.api, self)
        self.media_library_scanning = MediaLibraryScanning(self.api, self)
