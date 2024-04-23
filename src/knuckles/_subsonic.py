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
    """Container of all the methods to interact with the OpenSubsonic API"""

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
        """FF

        Args:
            url: The URL of the Subsonic server to connect to.
            user: The name of the user
            password: asd
            client: sad
            use_https: d a
            use_token: as
            request_method: as
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
