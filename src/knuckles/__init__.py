from importlib.metadata import version

from ._api import RequestMethod
from ._media_retrieval import SubtitlesFileFormat
from ._subsonic import Subsonic
from .models._album import Album, AlbumInfo, Disc, RecordLabel, ReleaseDate
from .models._artist import Artist, ArtistInfo
from .models._artist_index import ArtistIndex
from .models._bookmark import Bookmark
from .models._chat_message import ChatMessage
from .models._contributor import Contributor
from .models._cover_art import CoverArt
from .models._genre import Genre, ItemGenre
from .models._internet_radio_station import InternetRadioStation
from .models._jukebox import Jukebox
from .models._lyrics import Lyrics
from .models._music_directory import MusicDirectory
from .models._music_folder import MusicFolder
from .models._now_playing_entry import NowPlayingEntry
from .models._play_queue import PlayQueue
from .models._playlist import Playlist
from .models._podcast import Channel, Episode
from .models._replay_gain import ReplayGain
from .models._scan_status import ScanStatus
from .models._search_result import SearchResult
from .models._share import Share
from .models._song import Song
from .models._starred_content import StarredContent
from .models._system import License, SubsonicResponse
from .models._user import User
from .models._video import AudioTrack, Captions, Video, VideoInfo

__version__ = version("knuckles")

__all__ = [
    "__version__",
    "Subsonic",
    "RequestMethod",
    "SubtitlesFileFormat",
    "RecordLabel",
    "Disc",
    "ReleaseDate",
    "AlbumInfo",
    "Album",
    "ArtistInfo",
    "Artist",
    "Bookmark",
    "ChatMessage",
    "Contributor",
    "CoverArt",
    "ItemGenre",
    "Genre",
    "ArtistIndex",
    "InternetRadioStation",
    "Jukebox",
    "Lyrics",
    "MusicDirectory",
    "MusicFolder",
    "NowPlayingEntry",
    "PlayQueue",
    "Playlist",
    "Episode",
    "Channel",
    "ReplayGain",
    "ScanStatus",
    "SearchResult",
    "Share",
    "Song",
    "StarredContent",
    "SubsonicResponse",
    "License",
    "User",
    "AudioTrack",
    "Captions",
    "VideoInfo",
    "Video",
]
