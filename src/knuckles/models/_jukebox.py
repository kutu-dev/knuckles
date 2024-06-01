from typing import TYPE_CHECKING, Any, Self

from ._model import Model
from ._song import Song

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class Jukebox(Model):
    """Object that holds all the info about a jukebox.

    Attributes:
        current_index (int): The index in the playlist of the
            current playing song in the jukebox.
        playing (bool): If the jukebox is playing a song
            or not.
        gain (float): The gain of the playback of the jukebox.
        position (int): How many seconds the song has been already player.
        playlist (list[Song] | None): A list that holds all the info about
            all the songs that are in the playlist of the jukebox.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        currentIndex: int,
        playing: bool,
        gain: float,
        position: int,
        entry: list[dict[str, Any]] | None = None,
    ) -> None:
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
        """Return a new jukebox object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.jukebox.get()

    def start(self) -> Self:
        """Start the playback of the next song in the playlist.

        Returns:
            The object itself.
        """

        self._subsonic.jukebox.start()

        return self

    def stop(self) -> Self:
        """Stop the playback of the jukebox.

        Returns:
            The object itself.
        """
        self._subsonic.jukebox.stop()

        return self

    def skip(self, index: int, offset: float = 0) -> Self:
        """Skips the current playing song of the jukebox to another one.

        Args:
            index: The index of the song to skip to.
            offset: An offset in seconds where the playback of the song
                should start at.

        Returns:
            The object itself.
        """

        self._subsonic.jukebox.skip(index, offset)

        return self

    def shuffle(self) -> Self:
        """Shuffle the playlist of the jukebox.

        Returns:
            The object itself.
        """

        self._subsonic.jukebox.shuffle()

        # The shuffle is server side so a call to the API is necessary
        # to get the new order of the playlist
        self.playlist = self._subsonic.jukebox.get().playlist

        return self

    def set_gain(self, gain: float) -> Self:
        """Set the gain of the jukebox.

        Args:
            gain: The new gain of the jukebox.

        Returns:
            The object itself.
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
        """Set the songs of the playlist of the jukebox.

        Args:
            songs_ids: The IDs of the songs to be set the playlist to.

        Returns:
            The object itself.
        """

        self._subsonic.jukebox.set(songs_ids)

        self.playlist = [
            Song(subsonic=self._subsonic, id=song_id) for song_id in songs_ids
        ]

        return self

    def add(self, songs_ids: list[str]) -> Self:
        """Add songs to the playlist of the jukebox.

        Args:
            songs_ids: The IDs of the songs to add.

        Returns:
            The object itself.
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
        """Remove a song from the playlist of the jukebox.

        Args:
            index: The index of the song in the playlist to remove.

        Returns:
            The object itself.
        """

        self._subsonic.jukebox.remove(index)

        if self.playlist is not None:
            del self.playlist[index]
            return self

        # If the playlist is None the real value of it is unknown,
        # so a call the API is necessary to get a correct representation of the jukebox
        self.playlist = self.generate().playlist
        return self
