from typing import TYPE_CHECKING

from ._api import Api
from .models._jukebox import Jukebox

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class JukeboxControl:
    """Class that contains all the methods needed to interact with the
    [jukebox control endpoint](https://opensubsonic.netlify.app/
    categories/jukebox) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get(self) -> Jukebox:
        """Get all the info related with the current playlist of
        the jukebox.

        Returns:
            An object that holds all the info related with
                the playlist of the jukebox.
        """

        response = self.api.json_request("jukeboxControl", {"action": "get"})[
            "jukeboxPlaylist"
        ]

        return Jukebox(self.subsonic, **response)

    def status(self) -> Jukebox:
        """Get all the info related with the current state of
        the jukebox.

        Returns:
            An object that holds all the info related with
                the scate of the jukebox.
        """

        response = self.api.json_request("jukeboxControl", {"action": "status"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def set(self, songs_ids: list[str]) -> Jukebox:
        """Set the song playlist for the jukebox.

        Args:
            songs_ids: A list of song IDs to set the jukebox playlist.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request(
            "jukeboxControl", {"action": "set", "id": songs_ids}
        )["jukeboxStatus"]

        # Preset the song list as this call changes it in a predictable way
        return Jukebox(
            self.subsonic, **response, entry=[{"id": song_id} for song_id in songs_ids]
        )

    def start(self) -> Jukebox:
        """Start the playback of the current song in the jukebox playlist.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request("jukeboxControl", {"action": "start"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def stop(self) -> Jukebox:
        """Stop the playback of the current song in the jukebox playlist.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request("jukeboxControl", {"action": "stop"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def skip(self, index: int, offset: float = 0) -> Jukebox:
        """Skip the playback of the current song in the jukebox playlist.

        Args:
            index: The index of the song to skip to.
            offset: The offset of seconds to start playing the next song.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request(
            "jukeboxControl", {"action": "skip", "index": index, "offset": offset}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)

    def add(self, songs_ids: list[str]) -> Jukebox:
        """Add songs to the jukebox playlist.

        Args:
            songs_ids: A list of song IDs to add to the jukebox playlist.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request(
            "jukeboxControl", {"action": "add", "id": songs_ids}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)

    def clear(self) -> Jukebox:
        """Clear the playlist of the jukebox.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """
        response = self.api.json_request("jukeboxControl", {"action": "clear"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def remove(self, index: int) -> Jukebox:
        """Remove a song from the playlist of the jukebox.

        Args:
            index: The index of the song to remove from the playlist.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request(
            "jukeboxControl", {"action": "remove", "index": index}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)

    def shuffle(self) -> Jukebox:
        """Shuffle all the songs in the playlist of the jukebox.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        response = self.api.json_request("jukeboxControl", {"action": "shuffle"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def set_gain(self, gain: float) -> Jukebox:
        """Set the gain of the playback of the jukebox.

        Args:
            gain: A number between 0 and 1 (inclusive) to be set as the gain.

        Raises:
            ValueError: Raised if the given gain is not between 0 and 1.

        Returns:
            An object that contains the updated jukebox status
                and playlist.
        """

        if not 1 > gain > 0:
            raise ValueError("The gain should be between 0 and 1 (inclusive)")

        response = self.api.json_request(
            "jukeboxControl", {"action": "setGain", "gain": gain}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)
