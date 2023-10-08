from typing import Any

import responses
from dateutil import parser
from knuckles import CoverArt, Subsonic
from responses import Response


@responses.activate
def test_get_music_folders(
    subsonic: Subsonic,
    mock_get_music_folders: Response,
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_get_music_folders)

    response = subsonic.browsing.get_music_folders()

    assert response[0].id == music_folders[0]["id"]
    assert response[0].name == music_folders[0]["name"]


@responses.activate
def test_get_music_folder(
    subsonic: Subsonic,
    mock_get_music_folders: Response,
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_get_music_folders)

    response = subsonic.browsing.get_music_folder(music_folders[0]["id"])

    assert response.id == music_folders[0]["id"]
    assert response.name == music_folders[0]["name"]


@responses.activate
def test_get_genres(
    subsonic: Subsonic, mock_get_genres: Response, genre: dict[str, Any]
) -> None:
    responses.add(mock_get_genres)

    response = subsonic.browsing.get_genres()

    assert response[0].value == genre["value"]
    assert response[0].song_count == genre["songCount"]
    assert response[0].album_count == genre["albumCount"]


@responses.activate
def test_get_genre(
    subsonic: Subsonic, mock_get_genres: Response, genre: dict[str, Any]
) -> None:
    responses.add(mock_get_genres)

    response = subsonic.browsing.get_genre(genre["value"])

    assert response.value == genre["value"]
    assert response.song_count == genre["songCount"]
    assert response.album_count == genre["albumCount"]


@responses.activate
def test_get_artists(
    subsonic: Subsonic,
    mock_get_artists: Response,
    artist: dict[str, Any],
    music_folders: list[dict[str, Any]],
) -> None:
    responses.add(mock_get_artists)

    response = subsonic.browsing.get_artists(music_folders[0]["id"])

    assert response[0].id == artist["id"]


@responses.activate
def test_get_artist(
    subsonic: Subsonic,
    mock_get_artist: Response,
    artist: dict[str, Any],
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_artist)

    response = subsonic.browsing.get_artist(artist["id"])

    assert response.id == artist["id"]
    assert response.name == artist["name"]
    assert response.artist_image_url == artist["artistImageUrl"]
    assert response.starred == parser.parse(artist["starred"])
    assert response.user_rating == artist["userRating"]
    assert response.average_rating == artist["averageRating"]
    assert response.average_rating == artist["averageRating"]
    assert response.album_count == artist["albumCount"]
    assert type(response.albums) is list
    assert type(response.albums[0].songs) is list
    assert response.albums[0].songs[0].title == song["title"]
    assert response.cover_art.id == artist["coverArt"]


@responses.activate
def test_get_album(
    subsonic: Subsonic,
    mock_get_album: Response,
    album: dict[str, Any],
    song: dict[str, Any],
) -> None:
    responses.add(mock_get_album)

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
    assert type(response.songs) is list
    assert response.songs[0].id == song["id"]
    assert response.played == parser.parse(album["played"])
    assert response.user_rating == album["userRating"]


@responses.activate
def test_get_song(
    subsonic: Subsonic, mock_get_song: Response, song: dict[str, Any]
) -> None:
    responses.add(mock_get_song)

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


@responses.activate
def test_get_album_info(
    subsonic: Subsonic,
    mock_get_album_info: Response,
    album: dict[str, Any],
    album_info: dict[str, Any],
) -> None:
    responses.add(mock_get_album_info)

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
    subsonic: Subsonic,
    mock_get_artist_info_with_all_optional_params: Response,
    artist: dict[str, Any],
    artist_info: dict[str, Any],
) -> None:
    responses.add(mock_get_artist_info_with_all_optional_params)

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
