import typing

from .api import Api
from .models.song import Song

if typing.TYPE_CHECKING:
    from .subsonic import Subsonic


# TODO Unfinished
class Browsing:
    """Class that contains all the methods needed to interact
    with the browsing calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/browsing/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def get_song(self, id: str) -> Song:
        """Calls to the "getSong" endpoint of the API.

        :param id: The ID of the song to get.
        :type id: str
        :return: An object with all the information
            that the server has given about the song.
        :rtype: Song
        """

        response = self.api.request("getSong", {"id": id})["song"]

        return Song(self.subsonic, **response)
