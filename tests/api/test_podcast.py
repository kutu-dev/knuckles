from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_podcasts_default(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_podcasts()

    assert response[0].id == channel["id"]
    assert type(response[0].episodes) is list
    assert response[0].episodes[0].id == episode["id"]


@responses.activate
def test_get_podcasts_with_episodes(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_podcasts(True)

    assert response[0].id == channel["id"]
    assert type(response[0].episodes) is list
    assert response[0].episodes[0].id == episode["id"]


@responses.activate
def test_get_podcasts_without_episodes(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_without_episodes: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_without_episodes)

    response = subsonic.podcast.get_podcasts(False)

    assert response[0].id == channel["id"]
    assert response[0].episodes is None


@responses.activate
def test_get_podcast_default(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_default: list[Response],
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_default)

    response = subsonic.podcast.get_podcast(channel["id"])

    assert response.id == channel["id"]
    assert response.url == channel["url"]
    assert response.title == channel["title"]
    assert response.description == channel["description"]
    assert response.cover_art.id == channel["coverArt"]
    assert response.original_image_url == channel["originalImageUrl"]
    assert response.status == channel["status"]


@responses.activate
def test_get_podcast_with_episodes(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: list[Response],
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_with_episodes)

    response = subsonic.podcast.get_podcast(channel["id"], True)

    assert response.id == channel["id"]
    assert type(response.episodes) is list
    assert response.episodes[0].id == episode["id"]
    assert response.episodes[0].stream_id == episode["streamId"]
    assert response.episodes[0].channel.id == episode["channelId"]
    assert response.episodes[0].title == episode["title"]
    assert response.episodes[0].description == episode["description"]
    assert response.episodes[0].publish_date == parser.parse(episode["publishDate"])
    assert response.episodes[0].status == episode["status"]
    assert response.episodes[0].parent == episode["parent"]
    assert response.episodes[0].year == episode["year"]
    assert response.episodes[0].genre == episode["genre"]
    assert response.episodes[0].cover_art.id == episode["coverArt"]
    assert response.episodes[0].size == episode["size"]
    assert response.episodes[0].content_type == episode["contentType"]
    assert response.episodes[0].suffix == episode["suffix"]
    assert response.episodes[0].duration == episode["duration"]
    assert response.episodes[0].bit_rate == episode["bitRate"]
    assert response.episodes[0].path == episode["path"]


@responses.activate
def test_get_podcast_without_episodes(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_without_episodes: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_without_episodes)

    response = subsonic.podcast.get_podcast(channel["id"], False)

    assert response.id == channel["id"]
    assert response.episodes is None


@responses.activate
def test_get_newest_podcasts(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_newest_podcasts: list[Response],
    number_of_new_episodes: int,
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_newest_podcasts)

    response = subsonic.podcast.get_newest_podcasts(number_of_new_episodes)

    assert response[0].id == episode["id"]


@responses.activate
def test_get_episode(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_episode(episode["id"])

    assert response.id == episode["id"]


@responses.activate
def test_refresh_podcasts(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_refresh_podcasts: list[Response],
) -> None:
    add_responses(mock_refresh_podcasts)

    response = subsonic.podcast.refresh_podcasts()

    assert type(response) is Subsonic


@responses.activate
def test_create_podcast_channel(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_create_podcast_channel: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_create_podcast_channel)

    response = subsonic.podcast.create_podcast_channel(channel["url"])

    assert type(response) is Subsonic


@responses.activate
def test_delete_podcast_channel(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_podcast_channel: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_delete_podcast_channel)

    response = subsonic.podcast.delete_podcast_channel(channel["id"])

    assert type(response) is Subsonic


@responses.activate
def test_download_podcast_episode(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_download_podcast_episode: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_download_podcast_episode)

    response = subsonic.podcast.download_podcast_episode(episode["id"])

    assert type(response) is Subsonic


@responses.activate
def test_delete_podcast_episode(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_podcast_episode: list[Response],
    episode: dict[str, Any],
) -> None:
    add_responses(mock_delete_podcast_episode)

    response = subsonic.podcast.delete_podcast_episode(episode["id"])

    assert type(response) is Subsonic
