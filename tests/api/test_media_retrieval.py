from urllib import parse
from pathlib import Path
from typing import Any


import responses
from knuckles import Subsonic

from tests.mocks.media_retrieval import MockDownload


def test_stream(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.stream(song["id"]))

    assert stream_url.path == "/rest/stream"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


@responses.activate
def test_download_with_a_given_filename(
    tmp_path: Path,
    output_song_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
    song_content_type: str,
) -> None:
    responses.add(
        mock_download_file("download", {"id": song["id"]}, tmp_path, song_content_type)
    )

    download_path = subsonic.media_retrieval.download(
        song["id"], tmp_path / output_song_filename
    )

    # Check if the file data has been unaltered
    with open(tmp_path / output_song_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / output_song_filename


@responses.activate
def test_download_without_a_given_filename(
    tmp_path: Path,
    default_song_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
    song_content_type: str,
) -> None:
    responses.add(
        mock_download_file(
            "download",
            {"id": song["id"]},
            tmp_path,
            song_content_type,
            headers={
                "Content-Disposition": f'attachment; filename="{default_song_filename}"'
            },
        )
    )

    download_path = subsonic.media_retrieval.download(song["id"], tmp_path)

    # Check if the file data has been unaltered
    with open(tmp_path / default_song_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / default_song_filename


def test_hls(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.hls(song["id"]))

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


@responses.activate
def test_get_cover_art_with_a_given_filename(
    tmp_path: Path,
    output_cover_art_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
    cover_art_content_type: str,
    cover_art_size: int,
) -> None:
    responses.add(
        mock_download_file(
            "getCoverArt",
            {"id": song["coverArt"], "size": cover_art_size},
            tmp_path,
            cover_art_content_type,
        )
    )

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path / output_cover_art_filename, cover_art_size
    )

    # Check if the file data has been unaltered
    with open(tmp_path / output_cover_art_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / output_cover_art_filename


@responses.activate
def test_get_cover_art_without_a_given_filename(
    tmp_path: Path,
    default_cover_art_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
    cover_art_content_type: str,
    cover_art_size: int,
) -> None:
    responses.add(
        mock_download_file(
            "getCoverArt",
            {"id": song["coverArt"], "size": cover_art_size},
            tmp_path,
            cover_art_content_type,
        )
    )

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path, cover_art_size
    )

    # Check if the file data has been unaltered
    with open(tmp_path / default_cover_art_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / default_cover_art_filename


@responses.activate
def test_get_avatar_with_a_given_filename(
    tmp_path: Path,
    output_avatar_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    username: str,
    avatar_content_type: str,
) -> None:
    responses.add(
        mock_download_file(
            "getAvatar", {"username": username}, tmp_path, avatar_content_type
        )
    )

    download_path = subsonic.media_retrieval.get_avatar(
        username, tmp_path / output_avatar_filename
    )

    # Check if the file data has been unaltered
    with open(tmp_path / output_avatar_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / output_avatar_filename


@responses.activate
def test_get_avatar_without_a_given_filename(
    tmp_path: Path,
    default_avatar_filename: str,
    placeholder_data: str,
    mock_download_file: MockDownload,
    subsonic: Subsonic,
    username: str,
    avatar_content_type: str,
) -> None:
    responses.add(
        mock_download_file(
            "getAvatar", {"username": username}, tmp_path, avatar_content_type
        )
    )

    download_path = subsonic.media_retrieval.get_avatar(username, tmp_path)

    # Check if the file data has been unaltered
    with open(tmp_path / default_avatar_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / default_avatar_filename
