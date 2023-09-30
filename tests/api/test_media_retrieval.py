from urllib import parse
from pathlib import Path
from typing import Any

from responses import Response
import responses
from knuckles import Subsonic

from tests.mocks.media_retrieval import FileMetadata


def test_stream(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.stream(song["id"]))

    assert stream_url.path == "/rest/stream"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


@responses.activate
def test_download_with_a_given_filename(
    subsonic: Subsonic,
    mock_download: Response,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    download_metadata: FileMetadata,
) -> None:
    responses.add(mock_download)

    download_path = subsonic.media_retrieval.download(
        song["id"], tmp_path / download_metadata.output_filename
    )

    # Check if the file data has been unaltered
    with open(tmp_path / download_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / download_metadata.output_filename


@responses.activate
def test_download_without_a_given_filename(
    subsonic: Subsonic,
    mock_download: Response,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    download_metadata: FileMetadata,
) -> None:
    responses.add(mock_download)

    download_path = subsonic.media_retrieval.download(song["id"], tmp_path)

    # Check if the file data has been unaltered
    with open(tmp_path / download_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / download_metadata.default_filename


def test_hls(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.hls(song["id"]))

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


@responses.activate
def test_get_cover_art_with_a_given_filename(
    subsonic: Subsonic,
    mock_cover_art: Response,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    cover_art_metadata: FileMetadata,
    cover_art_size: int,
) -> None:
    responses.add(mock_cover_art)

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path / cover_art_metadata.output_filename, cover_art_size
    )

    # Check if the file data has been unaltered
    with open(tmp_path / cover_art_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / cover_art_metadata.output_filename


@responses.activate
def test_get_cover_art_without_a_given_filename(
    subsonic: Subsonic,
    mock_cover_art: Response,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    cover_art_size: int,
    cover_art_metadata: FileMetadata,
) -> None:
    responses.add(mock_cover_art)

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path, cover_art_size
    )

    # Check if the file data has been unaltered
    with open(tmp_path / cover_art_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / cover_art_metadata.default_filename


@responses.activate
def test_get_avatar_with_a_given_filename(
    subsonic: Subsonic,
    mock_avatar: Response,
    tmp_path: Path,
    placeholder_data: str,
    username: str,
    avatar_metadata: FileMetadata,
) -> None:
    responses.add(mock_avatar)

    download_path = subsonic.media_retrieval.get_avatar(
        username, tmp_path / avatar_metadata.output_filename
    )

    # Check if the file data has been unaltered
    with open(tmp_path / avatar_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / avatar_metadata.output_filename


@responses.activate
def test_get_avatar_without_a_given_filename(
    subsonic: Subsonic,
    mock_avatar: Response,
    tmp_path: Path,
    placeholder_data: str,
    username: str,
    avatar_metadata: FileMetadata,
) -> None:
    responses.add(mock_avatar)

    download_path = subsonic.media_retrieval.get_avatar(username, tmp_path)

    # Check if the file data has been unaltered
    with open(tmp_path / avatar_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / avatar_metadata.default_filename
