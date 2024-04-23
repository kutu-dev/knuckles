from typing import Any

import responses
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_album_list_random_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_random_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_random_non_id3)

    response = subsonic.lists.get_album_list_random_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_newest_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_newest_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_newest_non_id3)

    response = subsonic.lists.get_album_list_newest_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_highest_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_highest_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_highest_non_id3)

    response = subsonic.lists.get_album_list_highest_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_frequent_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_frequent_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_frequent_non_id3)

    response = subsonic.lists.get_album_list_frequent_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_recent_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_recent_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_recent_non_id3)

    response = subsonic.lists.get_album_list_recent_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_name_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_name_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_name_non_id3)

    response = subsonic.lists.get_album_list_alphabetical_by_name_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_artist_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_artist_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_artist_non_id3)

    response = subsonic.lists.get_album_list_alphabetical_by_artist_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_starred_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_starred_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_starred_non_id3)

    response = subsonic.lists.get_album_list_starred_non_id3(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_year_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_year_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    from_year: int,
    to_year: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_year_non_id3)

    response = subsonic.lists.get_album_list_by_year_non_id3(
        from_year, to_year, num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_genre_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_genre_non_id3: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    genre: dict[str, Any],
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_genre_non_id3)

    response = subsonic.lists.get_album_list_by_genre_non_id3(
        genre["value"], num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_random(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_random: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_random)

    response = subsonic.lists.get_album_list_random(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_newest(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_newest: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_newest)

    response = subsonic.lists.get_album_list_newest(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_highest(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_highest: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_highest)

    response = subsonic.lists.get_album_list_highest(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_frequent(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_frequent: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_frequent)

    response = subsonic.lists.get_album_list_frequent(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_recent(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_recent: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_recent)

    response = subsonic.lists.get_album_list_recent(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_name(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_name: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_name)

    response = subsonic.lists.get_album_list_alphabetical_by_name(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_alphabetical_by_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_alphabetical_by_artist: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_alphabetical_by_artist)

    response = subsonic.lists.get_album_list_alphabetical_by_artist(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_starred(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_starred: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_starred)

    response = subsonic.lists.get_album_list_starred(
        num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_year(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_year: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    from_year: int,
    to_year: int,
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_year)

    response = subsonic.lists.get_album_list_by_year(
        from_year, to_year, num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_album_list_by_genre(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_list_by_genre: list[Response],
    album: dict[str, Any],
    num_of_album: int,
    genre: dict[str, Any],
    album_list_offset: int,
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_album_list_by_genre)

    response = subsonic.lists.get_album_list_by_genre(
        genre["value"], num_of_album, album_list_offset, music_folders[0]["id"]
    )

    assert response[0].id == album["id"]


@responses.activate
def test_get_random_songs(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_random_songs: list[Response],
    num_of_songs: int,
    genre: dict[str, Any],
    from_year: int,
    to_year: int,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_random_songs)

    response = subsonic.lists.get_random_songs(
        num_of_songs, genre["value"], from_year, to_year, music_folders[0]["id"]
    )

    assert isinstance(response, list)
    assert response[0].id == song["id"]


@responses.activate
def test_get_songs_by_genre(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_songs_by_genre: list[Response],
    genre: dict[str, Any],
    songs_count: int,
    song_list_offset: int,
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_songs_by_genre)

    response = subsonic.lists.get_songs_by_genre(
        genre["value"], songs_count, song_list_offset, music_folders[0]["id"]
    )

    assert isinstance(response, list)
    assert response[0].id == song["id"]


@responses.activate
def test_get_now_playing(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_now_playing: list[Response],
    now_playing_entry: dict[str, Any],
) -> None:
    add_responses(mock_get_now_playing)

    response = subsonic.lists.get_now_playing()

    assert isinstance(response, list)
    assert response[0].user.username == now_playing_entry["username"]
    assert response[0].minutes_ago == now_playing_entry["minutesAgo"]
    assert response[0].player_id == now_playing_entry["playerId"]
    assert response[0].player_name == now_playing_entry["playerName"]
    assert response[0].song.id == now_playing_entry["id"]


@responses.activate
def test_get_starred_non_id3(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_starred_non_id3: list[Response],
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
    album: dict[str, Any],
    artist: dict[str, Any],
) -> None:
    add_responses(mock_get_starred_non_id3)

    response = subsonic.lists.get_starred_non_id3(music_folders[0]["id"])

    assert isinstance(response.songs, list)
    assert response.songs[0].id == song["id"]
    assert isinstance(response.albums, list)
    assert response.albums[0].id == album["id"]
    assert isinstance(response.artists, list)
    assert response.artists[0].id == artist["id"]


@responses.activate
def test_get_starred(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_starred: list[Response],
    music_folders: list[dict[str, Any]],
    song: dict[str, Any],
    album: dict[str, Any],
    artist: dict[str, Any],
) -> None:
    add_responses(mock_get_starred)

    response = subsonic.lists.get_starred(music_folders[0]["id"])

    assert isinstance(response.songs, list)
    assert response.songs[0].id == song["id"]
    assert isinstance(response.albums, list)
    assert response.albums[0].id == album["id"]
    assert isinstance(response.artists, list)
    assert response.artists[0].id == artist["id"]
