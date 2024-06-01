from typing import TYPE_CHECKING

from ._api import Api
from .models._podcast import Channel, Episode

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Podcast:
    """Class that contains all the methods needed to interact with the
    [podcast endpoints](https://opensubsonic.netlify.app/
    categories/podcast/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_podcast_channels(self, with_episodes: bool = True) -> list[Channel]:
        """Get all the info about all the available podcasts channels in the
        server.

        Args:
            with_episodes: If the server should also return all the info
                about each episode of each podcast channel

        Returns:
            An list that hold all the info about all the available podcasts
                channels.
        """

        response = self.api.json_request(
            "getPodcasts", {"includeEpisodes": with_episodes}
        )["podcasts"]

        return [Channel(self.subsonic, **channel) for channel in response]

    def get_podcast_channel(
        self, podcast_channel_id: str, with_episodes: bool | None = None
    ) -> Channel:
        """Get all the info about a podcast channel.

        Args:
            podcast_channel_id: The ID of the podcast channel to get its info.
            with_episodes: If the server should also return all the info
                about each episode of the podcast channel.

        Returns:
            An object that hold all the info about the requested podcast
                channel.
        """

        response = self.api.json_request(
            "getPodcasts", {"id": podcast_channel_id, "includeEpisodes": with_episodes}
        )["podcasts"][0]

        return Channel(self.subsonic, **response)

    def get_newest_podcast_episodes(self, number_max_episodes: int) -> list[Episode]:
        """Get all the info about the newest released podcast episodes.

        Args:
            number_max_episodes: The max number of episodes that the server
                should return.

        Returns:
            A list that holds all the info about all the newest released
                episodes.
        """

        response = self.api.json_request(
            "getNewestPodcasts", {"count": number_max_episodes}
        )["newestPodcasts"]["episode"]

        return [Episode(self.subsonic, **episode) for episode in response]

    def get_podcast_episode(self, episode_id: str) -> Episode | None:
        """Get all the info about a podcast episode.

        Args:
            episode_id: The ID of the podcast episode to get its info.

        Returns:
            An object that holds all the info about the requested podcast
                episode.
        """

        channels = self.get_podcast_channels()

        # Flatten the list of episodes inside the list of channels
        list_of_episodes = [
            episode
            for channel in channels
            if channel.episodes is not None
            for episode in channel.episodes
        ]

        for episode in list_of_episodes:
            if episode.id == episode_id:
                return episode

        return None

    def refresh_podcasts(self) -> "Subsonic":
        """Request the server to search for new podcast episodes.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("refreshPodcasts")

        return self.subsonic

    def create_podcast_channel(self, url: str) -> "Subsonic":
        """Create a new podcast channel

        Args:
            url: The URL of the podcast to add.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("createPodcastChannel", {"url": url})

        return self.subsonic

    def delete_podcast_channel(self, podcast_channel_id: str) -> "Subsonic":
        """Delete a podcast channel.

        Args:
            podcast_channel_id: The ID of the podcast channel to delete.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("deletePodcastChannel", {"id": podcast_channel_id})

        return self.subsonic

    def download_podcast_episode(self, podcast_episode_id: str) -> "Subsonic":
        """Download a podcast episode to the server.

        Args:
            podcast_episode_id: The ID of the podcast episode to download to
                the server.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("downloadPodcastEpisode", {"id": podcast_episode_id})

        return self.subsonic

    def delete_podcast_episode(self, podcast_episode_id: str) -> "Subsonic":
        """Delete a podcast episode from the server.

        Args:
            podcast_episode_id: The ID of the podcast episode to delete.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("deletePodcastEpisode", {"id": podcast_episode_id})

        return self.subsonic
