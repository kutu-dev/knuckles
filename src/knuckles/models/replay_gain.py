from typing import TYPE_CHECKING

# Avoid circular import error
from .model import Model

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class ReplayGain(Model):
    def __init__(
        self,
        subsonic: "Subsonic",
        trackGain: str | None = None,
        albumGain: str | None = None,
        trackPeak: str | None = None,
        albumPeak: str | None = None,
        baseGain: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.track_gain = trackGain
        self.album_gain = albumGain
        self.track_peak = trackPeak
        self.album_peak = albumPeak
        self.base_gain = baseGain
