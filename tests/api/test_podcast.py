from typing import Any

import responses
from dateutil import parser
from responses import Response

from knuckles import Subsonic


def test_get_podcasts_default():
    ...


def test_get_podcasts_with_episodes() -> None:
    ...


def test_get_podcasts_without_episodes():
    ...


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


#! ADD NEWEST EPISODES AND MODEL TESTS
def test_get_podcast_with_episodes():
    ...


def test_get_podcast_without_episodes():
    ...


def test_refresh_podcasts():
    ...


def test_create_podcast_channel():
    ...


def test_delete_podcast_channel():
    ...


def test_download_podcast_episode():
    ...


def test_delete_podcast_episode():
    ...
