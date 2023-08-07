# TODO Unfinished
class CoverArt:
    """Representation of all the data related to a cover art in Subsonic."""

    def __init__(self, id: str) -> None:
        """Representation of all the data related a to cover art in Subsonic.

        :param id: The ID of the cover art.
        :type id: str
        """

        self.id: str = id
