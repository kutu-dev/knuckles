from typing import Any

import pytest
import responses
from dateutil import parser
from responses import matchers

from knuckles import CoverArt, Song, Subsonic


@responses.activate
def test_get_song(
    subsonic: Subsonic,
    params: dict[str, str],
    song: dict[str, Any],
    subsonic_response: dict[str, Any],
) -> None:
    params["id"] = song["id"]
    subsonic_response["subsonic-response"]["song"] = song

    responses.add(
        responses.GET,
        url="https://example.com/rest/getSong",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Song = subsonic.get_song(song["id"])

    assert response.id == song["id"]
    assert response.parent == song["parent"]
    assert response.is_dir == song["isDir"]
    assert response.title == song["title"]

    # Album asserts
    assert response.album_id == song["albumId"]
    assert response.album == song["album"]
    assert response.get_album().id == song["albumId"]
    assert response.get_album().name == song["album"]

    # Artist asserts
    assert response.artist_id == song["artistId"]
    assert response.artist == song["artist"]
    assert response.get_artist().id == song["artistId"]
    assert response.get_artist().name == song["artist"]

    assert response.track == song["track"]
    assert response.year == song["year"]
    assert response.genre == song["genre"]
    assert type(response.cover_art) is CoverArt
    assert response.cover_art.id == song["coverArt"]
    assert response.size == song["size"]
    assert response.content_type == song["contentType"]
    assert response.suffix == song["suffix"]
    assert response.transcoded_content_type is None
    assert response.transcoded_suffix is None
    assert response.duration == song["duration"]
    assert response.bit_rate == song["bitRate"]
    assert type(response.path) is not None
    assert response.user_rating == song["userRating"]
    assert response.average_rating == song["averageRating"]
    assert response.play_count == song["playCount"]
    assert response.disc_number == song["discNumber"]
    assert response.created == parser.parse(song["created"])
    assert response.starred == parser.parse(song["starred"])
    assert response.type == "music"
    assert response.bookmark_position is None
    assert response.played == parser.parse(song["played"])


@pytest.mark.parametrize("key", ["artistId", "artist"])
@responses.activate
def test_song_without_artist(
    subsonic: Subsonic,
    params: dict[str, str],
    song: dict[str, Any],
    subsonic_response: dict[str, Any],
    key: str,
) -> None:
    # Remove any of the two keys related with the artist in the response
    # and see if it returns None
    del song[key]

    subsonic_response["subsonic-response"]["song"] = song

    responses.add(
        responses.GET,
        url="https://example.com/rest/getSong",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Song = subsonic.get_song(song["id"])
    assert response.get_artist() is None


@pytest.mark.parametrize("key", ["albumId", "album"])
@responses.activate
def test_song_without_album(
    subsonic: Subsonic,
    params: dict[str, str],
    song: dict[str, Any],
    subsonic_response: dict[str, Any],
    key: str,
) -> None:
    # Remove any of the two keys related with the artist in the response
    # and see if it returns None
    del song[key]

    subsonic_response["subsonic-response"]["song"] = song

    responses.add(
        responses.GET,
        url="https://example.com/rest/getSong",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: Song = subsonic.get_song(song["id"])
    assert response.get_album() is None


@responses.activate
def test_song_generate(
    subsonic: Subsonic,
    params: dict[str, Any],
    song: dict[str, Any],
    subsonic_response: dict[str, Any],
) -> None:
    params["id"] = song["id"]
    subsonic_response["subsonic-response"]["song"] = song

    responses.add(
        responses.GET,
        url="https://example.com/rest/getSong",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    requested_song: Song = subsonic.get_song(song["id"])
    requested_song.title = "Foo"
    requested_song = requested_song.generate(subsonic)()
    assert requested_song.title == song["title"]
