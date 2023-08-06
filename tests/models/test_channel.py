from typing import Any

import pytest
import responses
from knuckles import Subsonic
from knuckles.exceptions import MissingChannelUrl
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

    assert type(requested_channel) == Channel


@responses.activate
def test_create_none_url_value(
    subsonic: Subsonic,
    mock_get_podcast_with_episodes: Response,
    channel: dict[str, Any],
):
    responses.add(mock_get_podcast_with_episodes)

    response = subsonic.podcast.get_podcast(channel["id"])
    response.url = None

    with pytest.raises(
        MissingChannelUrl,
        match=(
            "A non None value in the url parameter" + "is necessary to create a channel"
        ),
    ):
        response.create()


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

    assert type(requested_channel) == Channel
