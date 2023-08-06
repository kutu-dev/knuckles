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
        response = self.api.request("getPodcasts", {"includeEpisodes": with_episodes})[
            "podcasts"
        ]

        return [Channel(self.subsonic, **channel) for channel in response]

    def get_podcast(self, id: str, with_episodes: bool = True) -> Channel:
        response = self.api.request(
            "getPodcasts", {"id": id, "includeEpisodes": with_episodes}
        )["podcasts"][0]

        return Channel(self.subsonic, **response)

    def get_newest_podcasts(self, number_max_episodes: int) -> list[Episode]:
        response = self.api.request(
            "getNewestPodcasts", {"count": number_max_episodes}
        )["newestPodcasts"]["episode"]

        return [Episode(self.subsonic, **episode) for episode in response]

    def get_episode(self, id: str) -> Episode | None:
        channels = self.get_podcasts()

        # Flatten the list of episodes inside the list of channels
        list_of_episodes = [
            episode
            for channel in channels
            if channel.episodes is not None
            for episode in channel.episodes
        ]

        for episode in list_of_episodes:
            if episode.id == id:
                return episode

        return None

    def refresh_podcasts(self) -> "Subsonic":
        self.api.request("refreshPodcasts")

        return self.subsonic

    def create_podcast_channel(self, url: str) -> "Subsonic":
        self.api.request("createPodcastChannel", {"url": url})

        return self.subsonic

    def delete_podcast_channel(self, id: str) -> "Subsonic":
        self.api.request("deletePodcastChannel", {"id": id})

        return self.subsonic

    def download_podcast_episode(self, id: str) -> "Subsonic":
        self.api.request("downloadPodcastEpisode", {"id": id})

        return self.subsonic

    def delete_podcast_episode(self, id: str) -> "Subsonic":
        self.api.request("deletePodcastEpisode", {"id": id})

        return self.subsonic
