from typing import TYPE_CHECKING, Any

from ._model import Model
from ._song import Song
from ._user import User

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class NowPlayingEntry(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        username: str,
        minutesAgo: int | None = None,
        playerId: int | None = None,
        playerName: str | None = None,
        **song_data: Any,
    ) -> None:
        super().__init__(subsonic)

        self.user = User(self._subsonic, username)
        self.minutes_ago = minutesAgo
        self.player_id = playerId
        self.player_name = playerName
        self.song = Song(subsonic=self._subsonic, **song_data)
