from urllib import parse
from pathlib import Path
from typing import Any

import pytest
from _pytest.fixtures import FixtureRequest
from responses import Response
import responses
from knuckles import Subsonic

from knuckles.media_retrieval import SubtitlesFileFormat
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

    # Check if the file data has been altered
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

    # Check if the file data has been altered
    with open(tmp_path / download_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / download_metadata.default_filename


def test_hls_song(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.hls(song["id"]))

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


def test_hls_video(
    subsonic: Subsonic, video: dict[str, Any], video_details: dict[str, Any]
) -> None:
    custom_bitrates = ["1000@480x360", "820@1920x1080"]

    stream_url = parse.urlparse(
        subsonic.media_retrieval.hls(
            video["id"], custom_bitrates, video_details["audioTrack"][0]["id"]
        )
    )

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == video["id"]
    assert custom_bitrates[0] in parse.parse_qs(stream_url.query)["bitRate"]
    assert custom_bitrates[1] in parse.parse_qs(stream_url.query)["bitRate"]
    assert (
        parse.parse_qs(stream_url.query)["audioTrack"][0]
        == video_details["audioTrack"][0]["id"]
    )


@responses.activate
def test_get_captions_with_a_given_filename(
    subsonic: Subsonic,
    mock_get_captions_vtt: Response,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    vtt_metadata: FileMetadata,
):
    responses.add(mock_get_captions_vtt)

    download_path = subsonic.media_retrieval.get_captions(
        song["id"], tmp_path / vtt_metadata.output_filename
    )

    # Check if the file data has been altered
    with open(tmp_path / vtt_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / vtt_metadata.output_filename


@responses.activate
@pytest.mark.parametrize(
    "mock, metadata",
    [
        ("mock_get_captions_vtt", "vtt_metadata"),
        ("mock_get_captions_srt", "srt_metadata"),
    ],
)
def test_get_captions_without_a_given_filename(
    request: FixtureRequest,
    subsonic: Subsonic,
    mock: str,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    metadata: str,
):
    # Retrieve the mocks dynamically as their tests are equal
    get_mock: Response = request.getfixturevalue(mock)
    get_metadata: FileMetadata = request.getfixturevalue(metadata)

    responses.add(get_mock)

    download_path = subsonic.media_retrieval.get_captions(song["id"], tmp_path)

    # Check if the file data has been altered
    with open(tmp_path / get_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / get_metadata.default_filename


@responses.activate
@pytest.mark.parametrize(
    "mock, metadata, file_format",
    [
        ("mock_get_captions_prefer_vtt", "vtt_metadata", SubtitlesFileFormat.VTT),
        ("mock_get_captions_prefer_srt", "srt_metadata", SubtitlesFileFormat.SRT),
    ],
)
def test_get_captions_with_a_preferred_file_format(
    request: FixtureRequest,
    subsonic: Subsonic,
    mock: str,
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    metadata: str,
    file_format: SubtitlesFileFormat,
):
    # Retrieve the mocks dynamically as their tests are equal
    get_mock: Response = request.getfixturevalue(mock)
    get_metadata: FileMetadata = request.getfixturevalue(metadata)

    responses.add(get_mock)

    download_path = subsonic.media_retrieval.get_captions(
        song["id"], tmp_path, file_format
    )

    # Check if the file data has been altered
    with open(tmp_path / get_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / get_metadata.default_filename


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

    # Check if the file data has been altered
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

    # Check if the file data has been altered
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

    # Check if the file data has been altered
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

    # Check if the file data has been altered
    with open(tmp_path / avatar_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / avatar_metadata.default_filename
