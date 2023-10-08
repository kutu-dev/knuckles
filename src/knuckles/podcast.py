from typing import TYPE_CHECKING

from .api import Api
from .models.podcast import Channel, Episode

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Podcast:
    """Class that contains all the methods needed to interact
    with the podcast calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/podcast/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_podcasts(self, with_episodes: bool = True) -> list[Channel]:
        """Calls the "getPodcasts" endpoint of the API.

        :param with_episodes: If the channels should also have
            all the episodes inside of them, defaults to True.
        :type with_episodes: bool, optional
        :return: A list with all the podcast channels in the sever.
        :rtype: list[Channel]
        """

        response = self.api.json_request(
            "getPodcasts", {"includeEpisodes": with_episodes}
        )["podcasts"]

        return [Channel(self.subsonic, **channel) for channel in response]

    def get_podcast(self, id_: str, with_episodes: bool | None = None) -> Channel:
        """Calls the "getPodcasts" endpoint of the API with a specific ID
        to only return the desired podcast channel.

        :param id_: The ID of the channel to get.
        :type id_: str
        :param with_episodes: If the channels should also have
            all the episodes inside of them, defaults to True.
        :type with_episodes: bool, optional
        :return: The requested podcast channel.
        :rtype: Channel
        """

        response = self.api.json_request(
            "getPodcasts", {"id": id_, "includeEpisodes": with_episodes}
        )["podcasts"][0]

        return Channel(self.subsonic, **response)

    def get_newest_podcasts(self, number_max_episodes: int) -> list[Episode]:
        """Calls the "getNewestPodcasts" endpoint of the API.

        :param number_max_episodes: The max number of episodes to return.
        :type number_max_episodes: int
        :return: The list with the new episodes.
        :rtype: list[Episode]
        """

        response = self.api.json_request(
            "getNewestPodcasts", {"count": number_max_episodes}
        )["newestPodcasts"]["episode"]

        return [Episode(self.subsonic, **episode) for episode in response]

    def get_episode(self, id_: str) -> Episode | None:
        """Calls the "getPodcasts" endpoints of the API and search through
        all the episodes to find the one with the same ID of the provided ID.

        :param id_: The provided episode ID.
        :type id_: str
        :return: The episode with the same ID
            or None if no episode with the ID are found.
        :rtype: Episode | None
        """

        channels = self.get_podcasts()

        # Flatten the list of episodes inside the list of channels
        list_of_episodes = [
            episode
            for channel in channels
            if channel.episodes is not None
            for episode in channel.episodes
        ]

        for episode in list_of_episodes:
            if episode.id == id_:
                return episode

        return None

    def refresh_podcasts(self) -> "Subsonic":
        """Calls the "refreshPodcast" method of the API.

        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("refreshPodcasts")

        return self.subsonic

    def create_podcast_channel(self, url: str) -> "Subsonic":
        """Calls the "createPodcastChannel endpoint of the API."

        :param url: The url of the new podcast.
        :type url: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("createPodcastChannel", {"url": url})

        return self.subsonic

    def delete_podcast_channel(self, id_: str) -> "Subsonic":
        """Calls the "deletePodcastChannel" endpoint of the API.

        :param id_: The ID of the channel to delete.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("deletePodcastChannel", {"id": id_})

        return self.subsonic

    def download_podcast_episode(self, id_: str) -> "Subsonic":
        """Calls the "downloadPodcastEpisode" endpoint of the API.

        :param id_: The ID of the episode to download.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("downloadPodcastEpisode", {"id": id_})

        return self.subsonic

    def delete_podcast_episode(self, id_: str) -> "Subsonic":
        """Calls the "deletePodcastEpisode" endpoint of the API.

        :param id_: The ID of the episode to delete.
        :type id_: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.json_request("deletePodcastEpisode", {"id": id_})

        return self.subsonic
