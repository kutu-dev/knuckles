from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import ResourceNotFound
from knuckles.models.podcast import Episode
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_episode(episode["id"])
    response.title = "Foo"
    response = response.generate()

    assert response.title == episode["title"]


@responses.activate
def test_generate_nonexistent_episode(
    subsonic: Subsonic, mock_get_podcasts_with_episodes: Response
) -> None:
    responses.add(mock_get_podcasts_with_episodes)

    response = Episode(subsonic, "Foo")

    with pytest.raises(
        ResourceNotFound,
        match="Unable to generate episode as it does not exist in the server",
    ):
        response.generate()


@responses.activate
def test_download(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    mock_download_podcast_episode: Response,
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)
    responses.add(mock_download_podcast_episode)

    response = subsonic.podcast.get_episode(episode["id"])
    response = response.download()

    assert type(response) is Episode


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

    assert type(requested_episode) is Episode
