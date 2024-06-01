from typing import TYPE_CHECKING

# Avoid circular import error
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class ReplayGain(Model):
    """Object that holds all the info about the gain of the playback
    of a media.

    Attributes:
        track_gain (str | None): The track replay gain in dB.
        album_gain (str | None): The album replay gain in dB.
        track_peak (int | None): The track peak value.
        album_peak (int | None): The album peak value.
        base_gain (int | None): The base replay gain in dB.
        fallback_gain (int | None): Fallback gain in dB used when
            the desired one is missing.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        trackGain: str | None = None,
        albumGain: str | None = None,
        trackPeak: str | None = None,
        albumPeak: str | None = None,
        baseGain: str | None = None,
        fallbackGain: int | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.track_gain = trackGain
        self.album_gain = albumGain
        self.track_peak = trackPeak
        self.album_peak = albumPeak
        self.base_gain = baseGain
        self.fallback_gain = fallbackGain
