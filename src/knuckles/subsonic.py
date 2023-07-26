from __future__ import annotations

from knuckles.browsing import Browsing
from knuckles.chat import Chat
from knuckles.jukebox import JukeboxControl
from knuckles.media_annotation import MediaAnnotation
from knuckles.media_library_scanning import MediaLibraryScanning
from knuckles.system import System

from .api import Api


class Subsonic:
    """The main class of the package, is used to interact with a Subsonic API"""

    def __init__(
        self,
        url: str,
        user: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
    ) -> None:
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
