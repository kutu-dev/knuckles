from typing import TYPE_CHECKING

from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic


class MusicFolder(Model):
    """Object that holds all the info about a music folder

    Attributes:
        id: The ID of the music folder.
        name: The name of the music folder.
    """

    def __init__(self, subsonic: "Subsonic", id: str, name: str | None = None) -> None:
        super().__init__(subsonic)

        self.id = id
        self.name = name

    def generate(self) -> "MusicFolder":
        """Return a new music folder object with all the data updated from the
        API, using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        music_folders = self._subsonic.browsing.get_music_folders()

        # Get the first element with the same ID
        music_folder = next(
            music_folder for music_folder in music_folders if music_folder.id == self.id
        )

        return music_folder
