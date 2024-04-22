from typing import Any

import responses
from dateutil import parser
from knuckles import CoverArt, Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_music_folders(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_music_folders: list[Response],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_music_folders)

    response = subsonic.browsing.get_music_folders()

    assert response[0].id == music_folders[0]["id"]
    assert response[0].name == music_folders[0]["name"]


@responses.activate
def test_get_indexes(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_indexes: list[Response],
    music_folders: list[dict[str, Any]],
    modified_date: int,
    indexes: dict[str, Any],
) -> None:
    add_responses(mock_get_indexes)

    response = subsonic.browsing.get_indexes(music_folders[0]["id"], modified_date)

    print(response.index)

    assert response.ignored_articles == indexes["ignoredArticles"]
    assert isinstance(response.index, dict)
    assert (
        response.index[indexes["index"][0]["name"]][0].name
        == indexes["index"][0]["artist"][0]["name"]
    )


@responses.activate
def test_get_music_directory(
    add_responses: AddResponses,
    mock_get_music_directory: list[Response],
    subsonic: Subsonic,
    music_directory: dict[str, Any],
) -> None:
    add_responses(mock_get_music_directory)

    response = subsonic.browsing.get_music_directory(music_directory["id"])

    assert response.id == music_directory["id"]
    assert response.parent == music_directory["parent"]
    assert response.name == music_directory["name"]
    assert response.starred == parser.parse(music_directory["starred"])
    assert response.user_rating == music_directory["userRating"]
    assert response.average_rating == music_directory["averageRating"]
    assert response.play_count == music_directory["playCount"]
    assert isinstance(response.songs, list)
    assert response.songs[0].id == music_directory["child"][0]["id"]


@responses.activate
def test_get_music_folder(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_music_folders: list[Response],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_music_folders)

    response = subsonic.browsing.get_music_folder(music_folders[0]["id"])

    assert response.id == music_folders[0]["id"]
    assert response.name == music_folders[0]["name"]


@responses.activate
def test_get_genres(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_genres: list[Response],
    genre: dict[str, Any],
) -> None:
    add_responses(mock_get_genres)

    response = subsonic.browsing.get_genres()

    assert response[0].value == genre["value"]
    assert response[0].song_count == genre["songCount"]
    assert response[0].album_count == genre["albumCount"]


@responses.activate
def test_get_genre(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_genres: list[Response],
    genre: dict[str, Any],
) -> None:
    add_responses(mock_get_genres)

    response = subsonic.browsing.get_genre(genre["value"])

    assert response.value == genre["value"]
    assert response.song_count == genre["songCount"]
    assert response.album_count == genre["albumCount"]


@responses.activate
def test_get_artists(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artists: list[Response],
    artist: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    add_responses(mock_get_artists)

    response = subsonic.browsing.get_artists(music_folders[0]["id"])

    assert response[0].id == artist["id"]


@responses.activate
def test_get_artist(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artist: list[Response],
    artist: dict[str, Any],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_artist)

    response = subsonic.browsing.get_artist(artist["id"])

    assert response.id == artist["id"]
    assert response.name == artist["name"]
    assert response.artist_image_url == artist["artistImageUrl"]
    assert response.starred == parser.parse(artist["starred"])
    assert response.user_rating == artist["userRating"]
    assert response.average_rating == artist["averageRating"]
    assert response.average_rating == artist["averageRating"]
    assert response.album_count == artist["albumCount"]
    assert isinstance(response.albums, list)
    assert isinstance(response.albums[0].songs, list)
    assert response.albums[0].songs[0].title == song["title"]
    assert response.cover_art.id == artist["coverArt"]
    assert response.music_brainz_id == artist["musicBrainzId"]
    assert response.sort_name == artist["sortName"]
    assert response.roles == artist["roles"]


@responses.activate
def test_get_album(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album: list[Response],
    album: dict[str, Any],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_album)

    response = subsonic.browsing.get_album(album["id"])

    assert response.id == album["id"]
    assert response.parent == album["parent"]
    assert response.album == album["album"]
    assert response.title == album["title"]
    assert response.name == album["name"]
    assert response.is_dir == album["isDir"]
    assert response.cover_art.id == album["coverArt"]
    assert response.song_count == album["songCount"]
    assert response.created == parser.parse(album["created"])
    assert response.duration == album["duration"]
    assert response.play_count == album["playCount"]
    assert response.artist.id == album["artistId"]
    assert response.artist.name == album["artist"]
    assert response.year == album["year"]
    assert response.genre == album["genre"]
    assert isinstance(response.songs, list)
    assert response.songs[0].id == song["id"]
    assert response.played == parser.parse(album["played"])
    assert response.user_rating == album["userRating"]
    assert isinstance(response.record_labels, list)
    assert response.record_labels[0].name == album["recordLabels"][0]["name"]
    assert response.music_brainz_id == album["musicBrainzId"]
    assert isinstance(response.genres, list)
    assert response.genres[0].name == album["genres"][0]["name"]
    assert isinstance(response.artists, list)
    assert response.artists[0].id == album["artists"][0]["id"]
    assert response.display_artist == album["displayArtist"]
    assert response.release_types == album["releaseTypes"]
    assert response.moods == album["moods"]
    assert response.sort_name == album["sortName"]
    assert response.original_release_date.year == album["originalReleaseDate"]["year"]
    assert response.release_date.year == album["releaseDate"]["year"]
    assert response.is_compilation == album["isCompilation"]
    assert isinstance(response.discs, list)
    assert response.discs[0].disc_number == album["discTitles"][0]["disc"]


@responses.activate
def test_get_song(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_song: list[Response],
    song: dict[str, Any],
) -> None:
    add_responses(mock_get_song)

    response = subsonic.browsing.get_song(song["id"])

    assert response.id == song["id"]
    assert response.parent == song["parent"]
    assert response.title == song["title"]
    assert response.album.id == song["albumId"]
    assert response.album.name == song["album"]
    assert response.artist.id == song["artistId"]
    assert response.artist.name == song["artist"]
    assert response.track == song["track"]
    assert response.year == song["year"]
    assert response.genre.value == song["genre"]
    assert isinstance(response.cover_art, CoverArt)
    assert response.cover_art.id == song["coverArt"]
    assert response.size == song["size"]
    assert response.content_type == song["contentType"]
    assert response.suffix == song["suffix"]
    assert response.transcoded_content_type is None
    assert response.transcoded_suffix is None
    assert response.duration == song["duration"]
    assert response.bit_rate == song["bitRate"]
    assert isinstance(response.path, str)
    assert response.user_rating == song["userRating"]
    assert response.average_rating == song["averageRating"]
    assert response.play_count == song["playCount"]
    assert response.disc_number == song["discNumber"]
    assert response.created == parser.parse(song["created"])
    assert response.starred == parser.parse(song["starred"])
    assert response.type == "music"
    assert response.bookmark_position is None
    assert response.played == parser.parse(song["played"])
    assert response.bpm == song["bpm"]
    assert response.comment == song["comment"]
    assert response.sort_name == song["sortName"]
    assert response.music_brainz_id == song["musicBrainzId"]
    assert isinstance(response.genres, list)
    assert response.genres[0].name == song["genres"][0]["name"]
    assert isinstance(response.artists, list)
    assert response.artists[0].id == song["artists"][0]["id"]
    assert response.display_artist == song["displayArtist"]
    assert isinstance(response.album_artists, list)
    assert response.album_artists[0].name == song["albumArtists"][0]["name"]
    assert response.display_album_artist == song["displayAlbumArtist"]
    assert isinstance(response.contributors, list)
    assert response.contributors[0].role == song["contributors"][0]["role"]
    assert response.display_composer == song["displayComposer"]
    assert isinstance(response.moods, list)
    assert response.moods[0] == song["moods"][0]
    assert response.replay_gain.track_gain == song["replayGain"]["trackGain"]


@responses.activate
def test_get_album_info(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_album_info: list[Response],
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    add_responses(mock_get_album_info)

    response = subsonic.browsing.get_album_info(album["id"])

    assert response.notes == album_info["notes"]
    assert response.music_brainz_id == album_info["musicBrainzId"]
    assert response.last_fm_url == album_info["lastFmUrl"]
    assert response.small_image_url == album_info["smallImageUrl"]
    assert response.medium_image_url == album_info["mediumImageUrl"]
    assert response.large_image_url == album_info["largeImageUrl"]
    assert response.large_image_url == album_info["largeImageUrl"]


@responses.activate
def test_get_artist_info(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_artist_info_with_all_optional_params: list[Response],
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    add_responses(mock_get_artist_info_with_all_optional_params)

    response = subsonic.browsing.get_artist_info(
        artist["id"], len(artist_info["similarArtist"]), False
    )

    assert response.biography == artist_info["biography"]
    assert response.music_brainz_id == artist_info["musicBrainzId"]
    assert response.last_fm_url == artist_info["lastFmUrl"]
    assert response.small_image_url == artist_info["smallImageUrl"]
    assert response.medium_image_url == artist_info["mediumImageUrl"]
    assert response.large_image_url == artist_info["largeImageUrl"]
    assert response.large_image_url == artist_info["largeImageUrl"]
    assert response.similar_artists is not None
    assert len(response.similar_artists) == len(artist_info["similarArtist"])
    assert response.similar_artists[0].name == artist["name"]


@responses.activate
def test_get_similar_songs(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_similar_songs: list[Response],
    song: dict[str, Any],
    songs_count: int,
) -> None:
    add_responses(mock_get_similar_songs)

    response = subsonic.browsing.get_similar_songs(song["id"], songs_count)

    assert response[0].id == song["id"]


@responses.activate
def test_get_top_songs(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_top_songs: list[Response],
    song: dict[str, Any],
    artist: dict[str, Any],
    songs_count: int,
) -> None:
    add_responses(mock_get_top_songs)

    response = subsonic.browsing.get_top_songs(artist["name"], songs_count)

    assert response[0].id == song["id"]
