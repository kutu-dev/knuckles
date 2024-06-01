from typing import TYPE_CHECKING, Any, Self

from ..exceptions import ResourceNotFound
from ._cover_art import CoverArt
from ._model import Model

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from dateutil import parser


class Episode(Model):
    """Object that holds all the info about a episode

    Attributes:
        id: (str) The ID of the episode
        stream_id (str | None): The ID of the stream of the
            episode.
        channel (Channel | None): The channel where the episode is
            from.
        title (str | None): The title of the episode.
        description (str | None): The description of the episode.
        publish_date (datetime | None): The timestamp when the episode
            was publised.
        status (str | None): The status of the episode.
        parent (str | None): The ID of the parent of the episode.
        is_dir (bool | None): If the episode is a directory.
        year (int | None): The year when the episode was released.
        genre (str | None): The name of the genre of the episode.
        cover_art (CoverArt | None): All the info related with the
            cover art of the episode.
        size (int | None): The size of the episode.
        content_type (str | None): The HTTP Content-Type of the file
            of the episode.
        suffix (str | None): The suffix of the filename of the file
            of the episode.
        duration (int | None): The duration in seconds of the episode.
        bit_rate (int | None): The bit rate of the episode.
        path (str | None): The path of the episode.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        streamId: str | None = None,
        channelId: str | None = None,
        title: str | None = None,
        description: str | None = None,
        publishDate: str | None = None,
        status: str | None = None,
        parent: str | None = None,
        isDir: bool | None = None,
        year: int | None = None,
        genre: str | None = None,
        coverArt: str | None = None,
        size: int | None = None,
        contentType: str | None = None,
        suffix: str | None = None,
        duration: int | None = None,
        bitRate: int | None = None,
        path: str | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.stream_id = streamId
        self.channel = Channel(self._subsonic, channelId) if channelId else None
        self.title = title
        self.description = description
        self.publish_date = parser.parse(publishDate) if publishDate else None
        self.status = status
        self.parent = parent
        self.is_dir = isDir
        self.year = year
        self.genre = genre
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
        self.size = size
        self.content_type = contentType
        self.suffix = suffix
        self.duration = duration
        self.bit_rate = bitRate
        self.path = path

    def generate(self) -> "Episode":
        """Return a new episode object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        get_episode = self._subsonic.podcast.get_podcast_episode(self.id)

        if get_episode is None:
            raise ResourceNotFound(
                "Unable to generate episode as it does not exist in the server"
            )

        return get_episode

    def download(self) -> Self:
        """Request the server to download the episode.

        Returns:
            The object itself.
        """

        self._subsonic.podcast.download_podcast_episode(self.id)

        return self

    def delete(self) -> Self:
        """Delete the episode from the server.

        Returns:
            The object itself.
        """

        self._subsonic.podcast.delete_podcast_episode(self.id)

        return self


class Channel(Model):
    """Object that holds all the info about a channel.

    Attributes:
        id (str): The ID of the channel.
        url (str | None): The URL of the channel.
        title (str | None): The title of the channel.
        description (str | None): The description of the channel.
        cover_art (CoverArt | None): All the info related with the
            cover art of the channel.
        original_image_url (str | None): The URL of the original image
            of the channel.
        status (str | None): The status of the channel.
        episodes (list[Episode] | None): List that holds all the info about
            all the episodes of the channel.
    """

    def __init__(
        self,
        subsonic: "Subsonic",
        id: str,
        url: str | None = None,
        title: str | None = None,
        description: str | None = None,
        coverArt: str | None = None,
        originalImageUrl: str | None = None,
        status: str | None = None,
        episode: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(subsonic)

        self.id = id
        self.url = url
        self.title = title
        self.description = description
        self.cover_art = CoverArt(self._subsonic, coverArt) if coverArt else None
        self.original_image_url = originalImageUrl
        self.status = status
        self.episodes = (
            [Episode(self._subsonic, **episode_data) for episode_data in episode]
            if episode
            else None
        )

    def generate(self) -> "Channel":
        """Return a new channel object with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object
        itself with immutability, e.g., `foo = foo.generate()`.

        Returns:
            A new object with all the updated info.
        """

        return self._subsonic.podcast.get_podcast_channel(self.id)

    def create(self) -> Self:
        """Create a new podcast with the info of the current one.

        Returns:
            The object itself.
        """

        # Ignore the None type error as the server
        # should return an Error Code 10 in response
        self._subsonic.podcast.create_podcast_channel(
            self.url  # type: ignore[arg-type]
        )

        return self

    def delete(self) -> Self:
        """Delete the podcast from the server.

        Returns:
            The object itself.
        """

        self._subsonic.podcast.delete_podcast_channel(self.id)

        return self
