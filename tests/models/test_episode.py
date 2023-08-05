from typing import Any

import responses
from responses import Response

from knuckles import Subsonic


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)

    requested_episode = subsonic.podcast.get_episode(episode["id"])
    requested_episode.title = "Foo"
    requested_episode = requested_episode.generate()

    assert requested_episode.title == episode["title"]


@responses.activate
def test_download(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    mock_download_podcast_episode: Response,
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)
    responses.add(mock_download_podcast_episode)

    requested_episode = subsonic.podcast.get_episode(episode["id"])
    requested_episode = requested_episode.download()

    # assert type(requested_channel) == Episode


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    mock_delete_podcast_episode: Response,
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)
    responses.add(mock_delete_podcast_episode)

    requested_episode = subsonic.podcast.get_episode(episode["id"])
    requested_episode = requested_episode.delete()

    # assert type(requested_channel) == Episode
