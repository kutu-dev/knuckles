from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.podcast import Channel
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    channel: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_with_episodes)

    requested_channel = subsonic.podcast.get_podcast(channel["id"])
    requested_channel.title = "Foo"
    requested_channel = requested_channel.generate()

    assert requested_channel.title == channel["title"]


@responses.activate
def test_create(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    mock_create_podcast_channel: Response,
    channel: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_with_episodes)
    responses.add(mock_create_podcast_channel)

    requested_channel = subsonic.podcast.get_podcast(channel["id"])
    requested_channel = requested_channel.create()

    assert type(requested_channel) is Channel


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    mock_delete_podcast_channel: Response,
    channel: dict[str, Any],
) -> None:
    responses.add(mock_get_podcast_with_episodes)
    responses.add(mock_delete_podcast_channel)

    requested_channel = subsonic.podcast.get_podcast(channel["id"])
    requested_channel = requested_channel.delete()

    assert type(requested_channel) is Channel
