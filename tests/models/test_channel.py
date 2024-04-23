from typing import Any

import responses
from knuckles import Channel, Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_default: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_default)

    response = subsonic.podcast.get_podcast(channel["id"])
    response.title = "Foo"
    response = response.generate()

    assert response.title == channel["title"]


@responses.activate
def test_create(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_default: list[Response],
    mock_create_podcast_channel: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_default)
    add_responses(mock_create_podcast_channel)

    response = subsonic.podcast.get_podcast(channel["id"])
    response = response.create()

    assert type(response) is Channel


@responses.activate
def test_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_podcast_default: list[Response],
    mock_delete_podcast_channel: list[Response],
    channel: dict[str, Any],
) -> None:
    add_responses(mock_get_podcast_default)
    add_responses(mock_delete_podcast_channel)

    response = subsonic.podcast.get_podcast(channel["id"])
    response = response.delete()

    assert type(response) is Channel
