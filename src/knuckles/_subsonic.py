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
    """Object that holds all the other helper objects to interact
    with the OpenSubsonic REST API.

    Inside this object there are helper object that holds all the methods
    used to access the REST API. The methods are split following the
    [categories listed in the OpenSubsonic REST API Spec](https://opensubsonic.
    netlify.app/categories/).

    Attributes:
        api: Helper object used to directly access the REST API of the given
            server.
        system: Helper object used to access all system related endpoints.
        browsing: Helper object used to access all system related endpoints.
        lists: Helper object used to access all lists related endpoints.
        searching: Helper object used to access all searching related
            endpoints.
        playlists: Helper object used to access playlists related endpoints.
        media_retrieval: Helper object used to access all media retrieval
            related endpoints.
        media_annotation: Helper object used to access all media
            annotation related endpoints.
        sharing: Helper object used to access all sharing related endpoints.
        podcast: Helper object used to access all podcast related endpoints.
        jukebox: Helper object used to access all jukebox related endpoints.
        internet_radio: Helper object used to access all internet radio
            related endpoints.
        chat: Helper object used to access all chat related endpoints.
        user_management: Helper object used to access all user management
            related endpoints.
        bookmarks: Helper object used to access all bookmarks related
            endpoints.
        media_library_scanning: Helper object used to access all media
            library scanning related endpoints.
    """

    def __init__(
        self,
        url: str,
        user: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
        request_method: RequestMethod = RequestMethod.GET,
    ) -> None:
        """Construction method of the Subsonic object used to
        interact with the OpenSubsonic REST API.

        Args:
            url: The URL of the Subsonic server to connect to.
            user: The name of the user to authenticate.
            password: The password of the user to authenticate.
            client: A unique name of the client to report to the
                server.
            use_https: If the requests should be use of HTTPS.
            use_token: If the authentication should be made
                using a salted token or in plain text.
            request_method: If the requests should be made
                using a GET verb or a POST verb.
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
