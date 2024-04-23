from typing import Any

import pytest
import responses
from knuckles import Episode, Subsonic
from knuckles.exceptions import ResourceNotFound
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_episode(episode["id"])
    response.title = "Foo"
    response = response.generate()

    assert response.title == episode["title"]


@responses.activate
def test_generate_nonexistent_episode(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)

    response = Episode(subsonic, "Foo")

    with pytest.raises(
        ResourceNotFound,
        match="Unable to generate episode as it does not exist in the server",
    ):
        response.generate()


@responses.activate
def test_download(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    mock_download_podcast_episode: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)
    add_responses(mock_download_podcast_episode)

    response = subsonic.podcast.get_episode(episode["id"])
    response = response.download()

    assert type(response) is Episode


@responses.activate
def test_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    mock_delete_podcast_episode: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)
    add_responses(mock_delete_podcast_episode)

    requested_episode = subsonic.podcast.get_episode(episode["id"])
    requested_episode = requested_episode.delete()

    assert type(requested_episode) is Episode
