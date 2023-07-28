# TODO Unfinished
class Artist:
    """Representation of all the data related to an artist in Subsonic."""

    def __init__(self, id: str, name: str | None = None) -> None:
        self.id: str = id
        self.name: str | None = name
