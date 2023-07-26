from typing import Any

import responses
from dateutil import parser
from knuckles import CoverArt, Song, Subsonic
from responses import Response


@responses.activate
def test_get_song(
    subsonic: Subsonic, mock_get_song: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_get_song)

    response: Song = subsonic.browsing.get_song(song["id"])

    assert response.id == song["id"]
    assert response.parent == song["parent"]
    assert response.title == song["title"]
    assert response.album.id == song["albumId"]
    assert response.album.name == song["album"]
    assert response.artist.id == song["artistId"]
    assert response.artist.name == song["artist"]
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
