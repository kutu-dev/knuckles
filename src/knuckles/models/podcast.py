from typing import TYPE_CHECKING, Any, Self

from ..exceptions import MissingChannelUrl, ResourceNotFound
from .cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic


from dateutil import parser


class Episode:
    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
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
        self.__subsonic = subsonic
        self.id = id
        self.stream_id = streamId
        self.channel = Channel(self.__subsonic, channelId) if channelId else None
        self.title = title
        self.description = description
        self.publish_date = parser.parse(publishDate) if publishDate else None
        self.status = status
        self.parent = parent
        self.is_dir = isDir
        self.year = year
        self.genre = genre
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.size = size
        self.content_type = contentType
        self.suffix = suffix
        self.duration = duration
        self.bit_rate = bitRate
        self.path = path

    def generate(self) -> "Episode":
        """Return a new episode with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new episode object with all the data updated.
        :rtype: Episode
        """

        getted_episode = self.__subsonic.podcast.get_episode(self.id)

        if getted_episode is None:
            raise ResourceNotFound(
                "Unable to generate episode as it does not exist in the server"
            )

        return getted_episode

    def download(self) -> Self:
        self.__subsonic.podcast.download_podcast_episode(self.id)

        return self

    def delete(self) -> Self:
        self.__subsonic.podcast.delete_podcast_episode(self.id)

        return self


class Channel:
    def __init__(
        self,
        # Internal
        subsonic: "Subsonic",
        # Subsonic fields
        id: str,
        url: str | None = None,
        title: str | None = None,
        description: str | None = None,
        coverArt: str | None = None,
        originalImageUrl: str | None = None,
        status: str | None = None,
        episode: list[dict[str, Any]] | None = None,
    ) -> None:
        self.__subsonic = subsonic
        self.id = id
        self.url = url
        self.title = title
        self.description = description
        self.cover_art = CoverArt(coverArt) if coverArt else None
        self.original_image_url = originalImageUrl
        self.status = status
        self.episodes = (
            [Episode(self.__subsonic, **episode_data) for episode_data in episode]
            if episode
            else None
        )

    def generate(self) -> "Channel":
        """Return a new channel with all the data updated from the API,
        using the endpoint that return the most information possible.

        Useful for making copies with updated data or updating the object itself
        with immutability, e.g., foo = foo.generate().

        :return: A new channel object with all the data updated.
        :rtype: Channel
        """

        return self.__subsonic.podcast.get_podcast(self.id)

    def create(self) -> Self:
        if self.url is None:
            raise MissingChannelUrl(
                (
                    "A non None value in the url parameter"
                    + "is necessary to create a channel"
                )
            )

        self.__subsonic.podcast.create_podcast_channel(self.url)

        return self

    def delete(self) -> Self:
        self.__subsonic.podcast.delete_podcast_channel(self.id)

        return self
