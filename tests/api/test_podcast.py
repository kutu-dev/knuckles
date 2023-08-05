from typing import Any

import responses
from dateutil import parser
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_get_podcasts_default(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_podcasts()

    assert response[0].id == channel["id"]
    assert response[0].episodes[0].id == episode["id"]


@responses.activate
def test_get_podcasts_with_episodes(
    subsonic: Subsonic,
    mock_get_podcasts_with_episodes: Response,
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_with_episodes)

    response = subsonic.podcast.get_podcasts(True)

    assert response[0].id == channel["id"]
    assert response[0].episodes[0].id == episode["id"]


@responses.activate
def test_get_podcasts_without_episodes(
    subsonic: Subsonic,
    mock_get_podcasts_without_episodes,
    channel: dict[str, Any],
) -> None:
    responses.add(mock_get_podcasts_without_episodes)

    response = subsonic.podcast.get_podcasts(False)

    assert response[0].id == channel["id"]
    assert response[0].episodes is None


@responses.activate
def test_get_podcast_default(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_with_episodes)

    response = subsonic.podcast.get_podcast(channel["id"])

    assert response.id == channel["id"]
    assert response.url == channel["url"]
    assert response.title == channel["title"]
    assert response.description == channel["description"]
    assert response.cover_art.id == channel["coverArt"]
    assert response.original_image_url == channel["originalImageUrl"]
    assert response.status == channel["status"]
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
def test_get_podcast_with_episodes(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_with_episodes)

    response = subsonic.podcast.get_podcast(channel["id"], True)

    assert response.id == channel["id"]
    assert response.episodes[0].id == episode["id"]


@responses.activate
def test_get_podcast_without_episodes(
    subsonic: Subsonic,
    mock_get_podcast_without_episodes: Response,
    channel: dict[str, Any],
    episode: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_without_episodes)

    response = subsonic.podcast.get_podcast(channel["id"], False)

    assert response.id == channel["id"]
    assert response.episodes[0].id == episode["id"]


@responses.activate
def test_get_newest_podcasts(
    subsonic: Subsonic, mock_get_newest_podcasts: Response, episode: dict[str, Any]
) -> None:
    responses.add(mock_get_newest_podcasts)

    response = subsonic.podcast.get_newest_podcasts()

    assert response[0].id == episode["id"]


@responses.activate
def test_refresh_podcasts(subsonic: Subsonic, mock_refresh_podcasts: Response) -> None:
    responses.add(mock_refresh_podcasts)

    response = subsonic.podcast.refresh_podcasts()

    assert type(response) == Subsonic


@responses.activate
def test_create_podcast_channel(
    subsonic: Subsonic, mock_create_podcast_channel: Response, channel: dict[str, Any]
) -> None:
    responses.add(mock_create_podcast_channel)

    response = subsonic.podcast.create_podcast_channel(channel["url"])

    assert type(response) == Subsonic


@responses.activate
def test_delete_podcast_channel(
    subsonic: Subsonic, mock_delete_podcast_channel: Response, channel: dict[str, Any]
) -> None:
    responses.add(mock_delete_podcast_channel)

    response = subsonic.podcast.delete_podcast_channel(channel["id"])

    assert type(response) == Subsonic


@responses.activate
def test_download_podcast_episode(
    subsonic: Subsonic, mock_download_podcast_episode: Response, episode: dict[str, Any]
) -> None:
    responses.add(mock_download_podcast_episode)

    response = subsonic.podcast.download_podcast_episode(episode["id"])

    assert type(response) == Subsonic


@responses.activate
def test_delete_podcast_episode(
    subsonic: Subsonic, mock_delete_podcast_episode: Response, episode: dict[str, Any]
) -> None:
    responses.add(mock_delete_podcast_episode)

    response = subsonic.podcast.delete_podcast_episode(episode["id"])

    assert type(response) == Subsonic
