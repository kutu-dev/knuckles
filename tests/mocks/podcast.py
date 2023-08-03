from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def episode() -> dict[str, Any]:
    return {
        "id": "34",
        "streamId": "523",
        "channelId": "1",
        "title": "Title",
        "description": "Description",
        "publishDate": "2011-02-03T14:46:43",
        "status": "completed",
        "parent": "11",
        "isDir": "false",
        "year": 2011,
        "genre": "Podcast",
        "coverArt": "coverArtId",
        "size": 78421341,
        "contentType": "audio/mpeg",
        "suffix": "mp3",
        "duration": 3146,
        "bitRate": 128,
        "path": "Podcast/foo/bar.mp3",
    }


@pytest.fixture
def channel(episode: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": "1",
        "url": "https://downloads.domain.com/podcasts/rss.xml",
        "title": "Title",
        "description": "Description",
        "coverArt": "coverArtId",
        "originalImageUrl": "https://downloads.domain.com/podcasts/drkarl.jpg",
        "status": "completed",
        "episode": [episode],
    }


@pytest.fixture
def mock_get_podcasts_with_episodes(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator(
        "getPlaylists", {"includeEpisodes": True}, {"podcasts": [channel]}
    )


@pytest.fixture
def mock_get_podcasts_without_episodes(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator(
        "getPlaylists", {"includeEpisodes": False}, {"podcasts": [channel]}
    )


@pytest.fixture
def mock_get_podcast_with_episodes(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator(
        "getPlaylists",
        {"id": channel["id"], "includeEpisodes": True},
        {"podcasts": [channel]},
    )


@pytest.fixture
def mock_get_podcast_without_episodes(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator(
        "getPlaylists",
        {"id": channel["id"], "includeEpisodes": False},
        {"podcasts": [channel]},
    )


@pytest.fixture
def mock_refresh_podcasts(mock_generator: MockGenerator) -> Response:
    return mock_generator("refreshPodcasts")


@pytest.fixture
def mock_create_podcast_channel(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator("createPodcastChannel", {"url": channel["url"]})


@pytest.fixture
def mock_delete_podcast_channel(
    mock_generator: MockGenerator, channel: dict[str, Any]
) -> Response:
    return mock_generator("deletePodcastChannel", {"id": channel["id"]})


@pytest.fixture
def mock_download_podcast_episode(
    mock_generator: MockGenerator, episode: dict[str, Any]
) -> Response:
    return mock_generator("downloadPodcastEpisode", {"id": episode["id"]})


@pytest.fixture
def mock_delete_podcast_episode(
    mock_generator: MockGenerator, episode: dict[str, Any]
) -> Response:
    return mock_generator("deletePodcastEpisode", {"id": episode["id"]})
