from typing import TYPE_CHECKING

from ..exceptions import ResourceNotFound

if TYPE_CHECKING:
    from ..subsonic import Subsonic


class Genre:
    """Representation of all the data related to genres in Subsonic."""

    def __init__(
        self,
        subsonic: "Subsonic",
        value: str,
        songCount: int | None = None,
        albumCount: int | None = None,
    ) -> None:
        """Representation of all the data related to genres in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param value: The name of the genre.
        :type value: str
        :param songCount: The number of songs with this genre, defaults to None.
        :type songCount: int | None, optional
        :param albumCount: The number of albums with this genre, defaults to None.
        :type albumCount: int | None, optional
        """

        self.__subsonic = subsonic
        self.value = value
        self.song_count = songCount
        self.album_count = albumCount

    def generate(self) -> "Genre | None":
        """Return a new genre with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new genre object with all the data updated.
        :rtype: Genre
        """
        getted_genre = self.__subsonic.browsing.get_genre(self.value)

        if getted_genre is None:
            raise ResourceNotFound(
                "Unable to generate gender as it does not exist in the server"
            )

        return getted_genre
