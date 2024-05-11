from typing import TYPE_CHECKING, Any, Self

from ._model import Model
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Jukebox(Model):
    """Representation of all the data related to the jukebox in Subsonic."""

    def __init__(
        self,
        subsonic: "Subsonic",
        currentIndex: int,
        playing: bool,
        gain: float,
        position: int,
        entry: list[dict[str, Any]] | None = None,
    ) -> None:
        """Representation of all the data related to the jukebox in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param currentIndex: The current index of the jukebox.
        :type currentIndex: int
        :param playing: If the jukebox is playing a song.
        :type playing: bool
        :param gain: The gain of the jukebox.
        :type gain: float
        :param position: The position of the jukebox.
        :type position: int
        :param entry: A list with all the songs inside the jukebox, defaults to None.
        :type entry: list[dict[str, Any]] | None, optional
        """

        super().__init__(subsonic)

        self.current_index: int = currentIndex
        self.playing: bool = playing
        self.gain: float = gain
        self.position: int = position

        self.playlist: list[Song] | None = None
        if entry is None:
            return

        self.playlist = []

        for song in entry:
            self.playlist.append(Song(subsonic=self._subsonic, **song))

    def generate(self) -> "Jukebox":
        """Return a new jukebox with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new jukebox object with all the data updated.
        :rtype: Jukebox
        """

        return self._subsonic.jukebox.get()

    def start(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "start".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.start()

        return self

    def stop(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "stop".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.stop()

        return self

    def skip(self, index: int, offset: float = 0) -> Self:
        """_summary_

        :param index: The index in the jukebox playlist to skip to.
        :type index: int
        :param offset: Start playing this many seconds into the track, defaults to 0.
        :type offset: float, optional
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.skip(index, offset)

        return self

    def shuffle(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "shuffle".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.shuffle()

        # The shuffle is server side so a call to the API is necessary
        # to get the new order of the playlist
        self.playlist = self._subsonic.jukebox.get().playlist

        return self

    def set_gain(self, gain: float) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "setGain"

        :param gain: A number between 0 and 1 (inclusive) to set the gain.
        :type gain: float
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.set_gain(gain)
        self.gain = gain

        return self

    def clear(self) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "clear".

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.clear()
        self.playlist = []

        return self

    def set(self, songs_ids: list[str]) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "set".

        :param id: The ID of a song to set it in the jukebox.
        :type id: str
        :raises ValueError: Raised if the gain argument isn't between the valid range.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.set(songs_ids)

        self.playlist = [
            Song(subsonic=self._subsonic, id=song_id) for song_id in songs_ids
        ]

        return self

    def add(self, songs_ids: list[str]) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "add".

        :param id: The ID of a song to add it in the jukebox.
        :type id: str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.add(songs_ids)

        songs_to_add = [
            Song(subsonic=self._subsonic, id=song_id) for song_id in songs_ids
        ]
        if self.playlist is not None:
            self.playlist += songs_to_add
            return self

        # If the playlist is None then the real value of it is unknown,
        # so a call the API is necessary to get a correct representation
        # of the jukebox
        self.playlist = self.generate().playlist
        return self

    def remove(self, index: int) -> Self:
        """Calls the "jukeboxControl" endpoint of the API with the action "remove".

        :param index: The index in the jukebox playlist for the song to remove.
        :type index: int
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self._subsonic.jukebox.remove(index)

        if self.playlist is not None:
            del self.playlist[index]
            return self

        # If the playlist is None the real value of it is unknown,
        # so a call the API is necessary to get a correct representation of the jukebox
        self.playlist = self.generate().playlist
        return self
