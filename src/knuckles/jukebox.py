from typing import TYPE_CHECKING

from .api import Api
from .models.jukebox import Jukebox

if TYPE_CHECKING:
    from .subsonic import Subsonic


class JukeboxControl:
    """Class that contains all the methods needed to interact
    with the jukebox calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/docs/endpoints/jukeboxcontrol/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "get".

        :return: An object with all the given information about the jukebox.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "get"})[
            "jukeboxPlaylist"
        ]

        return Jukebox(self.subsonic, **response)

    def status(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "status".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "status"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def set(self, id: str) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "set".

        :param id: The ID of a song to set it in the jukebox.
        :type id: str
        :return: An object with all the given information about the jukebox.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "set", "id": id})[
            "jukeboxStatus"
        ]

        # Preset the song list as this call changes it in a predictable way
        return Jukebox(self.subsonic, **response, entry=[{"id": id}])

    def start(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "start".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "start"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def stop(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "stop".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "stop"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def skip(self, index: int, offset: float = 0) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "skip".

        :param index: The index in the jukebox playlist to skip to.
        :type index: int
        :param offset: Start playing this many seconds into the track, defaults to 0
        :type offset: float, optional
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request(
            "jukeboxControl", {"action": "skip", "index": index, "offset": offset}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)

    def add(self, id: str) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "add".

        :param id: The ID of a song to add it in the jukebox.
        :type id: str
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "add", "id": id})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def clear(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "clear".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "clear"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def remove(self, index: int) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "remove".

        :param index: The index in the jukebox playlist for the song to remove.
        :type index: int
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request(
            "jukeboxControl", {"action": "remove", "index": index}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)

    def shuffle(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "shuffle".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response = self.api.request("jukeboxControl", {"action": "shuffle"})[
            "jukeboxStatus"
        ]

        return Jukebox(self.subsonic, **response)

    def set_gain(self, gain: float) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "setGain".

        :param gain: A number between 0 and 1 (inclusive) to set the gain.
        :type gain: float
        :raises ValueError: Raised if the gain argument isn't between the valid range.
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        if not 1 > gain > 0:
            raise ValueError("The gain should be between 0 and 1 (inclusive)")

        response = self.api.request(
            "jukeboxControl", {"action": "setGain", "gain": gain}
        )["jukeboxStatus"]

        return Jukebox(self.subsonic, **response)
