from typing import TYPE_CHECKING, Any, Self

from ..exceptions import MissingChannelUrl, ResourceNotFound
from .cover_art import CoverArt

if TYPE_CHECKING:
    from ..subsonic import Subsonic

from dateutil import parser


class Episode:
    """Representation of all the data related to a podcast episode in Subsonic."""

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
        """Representation of all the data related to a podcast episode in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The ID of the episode.
        :type id: str
        :param streamId: The ID to stream the episode, defaults to None.
        :type streamId: str | None, optional
        :param channelId: The ID of the channel where the episode comes from,
            defaults to None.
        :type channelId: str | None, optional
        :param title: The title of the episode, defaults to None.
        :type title: str | None, optional
        :param description: The description of the episode, defaults to None.
        :type description: str | None, optional
        :param publishDate: The date of publish of the episode, defaults to None.
        :type publishDate: str | None, optional
        :param status: The status of the episode, defaults to None.
        :type status: str | None, optional
        :param parent: The ID of the parent folder of the episode, defaults to None.
        :type parent: str | None, optional
        :param isDir: If the episode is a dir, defaults to None.
        :type isDir: bool | None, optional
        :param year: The year of release of the episode, defaults to None.
        :type year: int | None, optional
        :param genre: The genre of the episode, defaults to None.
        :type genre: str | None, optional
        :param coverArt: The cover art ID of the episode, defaults to None.
        :type coverArt: str | None, optional
        :param size: The file size of the episode, defaults to None.
        :type size: int | None, optional
        :param contentType: The content type of the episode file, defaults to None.
        :type contentType: str | None, optional
        :param suffix: The suffix of the episode file, defaults to None.
        :type suffix: str | None, optional
        :param duration: The duration in seconds of the episode, defaults to None.
        :type duration: int | None, optional
        :param bitRate: The bit rate of the episode, defaults to None.
        :type bitRate: int | None, optional
        :param path: The path of the episode, defaults to None.
        :type path: str | None, optional
        """

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
        """Calls the "downloadPodcastEpisode" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.podcast.download_podcast_episode(self.id)

        return self

    def delete(self) -> Self:
        """Calls the "deletePodcastEpisode" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.podcast.delete_podcast_episode(self.id)

        return self


class Channel:
    """Representation of all the data related to a podcast channel in Subsonic."""

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
        """Representation of all the data related to a podcast channel in Subsonic.

        :param subsonic: The subsonic object to make all the internal requests with it.
        :type subsonic: Subsonic
        :param id: The ID of the channel.
        :type id: str
        :param url: The url to get the episodes from, defaults to None.
        :type url: str | None, optional
        :param title: The title of the channel, defaults to None.
        :type title: str | None, optional
        :param description: The description of the channel, defaults to None.
        :type description: str | None, optional
        :param coverArt: The cover art ID of the channel, defaults to None.
        :type coverArt: str | None, optional
        :param originalImageUrl: The url of the original image of the channel,
            defaults to None.
        :type originalImageUrl: str | None, optional
        :param status: The status of the channel, defaults to None.
        :type status: str | None, optional
        :param episode: A list will all the episodes of the podcast, defaults to None.
        :type episode: list[dict[str, Any]] | None, optional
        """

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
        """Calls the "createPodcastChannel" endpoint of the API.

        :raises MissingChannelUrl: Raised if the object where the method is called
        has a None value in the url parameter.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

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
        """Calls the "deletePodcastChannel" endpoint of the API.

        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__subsonic.podcast.delete_podcast_channel(self.id)

        return self
