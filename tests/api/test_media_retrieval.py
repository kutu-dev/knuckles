from pathlib import Path
from typing import Any
from urllib import parse

import knuckles
import pytest
import responses
from _pytest.fixtures import FixtureRequest
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses
from tests.mocks.media_retrieval import FileMetadata


def test_stream_song(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(
        subsonic.media_retrieval.stream(
            song["id"], 0, song["suffix"], estimate_content_length=True
        )
    )

    assert stream_url.path == "/rest/stream"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]
    assert parse.parse_qs(stream_url.query)["maxBitRate"][0] == "0"
    assert parse.parse_qs(stream_url.query)["format"][0] == song["suffix"]
    assert parse.parse_qs(stream_url.query)["estimateContentLength"][0] == "True"


def test_stream_video(subsonic: Subsonic, video: dict[str, Any]) -> None:
    stream_url = parse.urlparse(
        subsonic.media_retrieval.stream(
            video["id"], 0, video["suffix"], 809, "640x480", True, True
        )
    )

    assert stream_url.path == "/rest/stream"

    parsed_query = parse.parse_qs(stream_url.query)

    assert parsed_query["id"][0] == video["id"]
    assert parsed_query["maxBitRate"][0] == "0"
    assert parsed_query["format"][0] == video["suffix"]
    assert parsed_query["timeOffset"][0] == "809"
    assert parsed_query["size"][0] == "640x480"
    assert parsed_query["estimateContentLength"][0] == "True"
    assert parsed_query["converted"][0] == "True"


@responses.activate
def test_download_with_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_download: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    download_metadata: FileMetadata,
) -> None:
    add_responses(mock_download)

    response = subsonic.media_retrieval.download(
        song["id"], tmp_path / download_metadata.output_filename
    )

    # Check if the file data has been altered
    with open(tmp_path / download_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert response == tmp_path / download_metadata.output_filename


@responses.activate
def test_download_without_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_download: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    download_metadata: FileMetadata,
) -> None:
    add_responses(mock_download)

    response = subsonic.media_retrieval.download(song["id"], tmp_path)

    # Check if the file data has been altered
    with open(tmp_path / download_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert response == tmp_path / download_metadata.default_filename


def test_hls_song(subsonic: Subsonic, song: dict[str, Any]) -> None:
    stream_url = parse.urlparse(subsonic.media_retrieval.hls(song["id"]))

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == song["id"]


def test_hls_video(
    subsonic: Subsonic, video: dict[str, Any], video_info: dict[str, Any]
) -> None:
    custom_bitrates = ["1000@480x360", "820@1920x1080"]

    stream_url = parse.urlparse(
        subsonic.media_retrieval.hls(
            video["id"], custom_bitrates, video_info["audioTrack"][0]["id"]
        )
    )

    assert stream_url.path == "/rest/hls.m3u8"
    assert parse.parse_qs(stream_url.query)["id"][0] == video["id"]
    assert custom_bitrates[0] in parse.parse_qs(stream_url.query)["bitRate"]
    assert custom_bitrates[1] in parse.parse_qs(stream_url.query)["bitRate"]
    assert (
        parse.parse_qs(stream_url.query)["audioTrack"][0]
        == video_info["audioTrack"][0]["id"]
    )


@responses.activate
def test_get_captions_with_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_captions_vtt: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    video: dict[str, Any],
    vtt_metadata: FileMetadata,
) -> None:
    add_responses(mock_get_captions_vtt)

    response = subsonic.media_retrieval.get_captions(
        video["id"], tmp_path / vtt_metadata.output_filename
    )

    # Check if the file data has been altered
    with open(tmp_path / vtt_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert response == tmp_path / vtt_metadata.output_filename


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
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock: str,
    tmp_path: Path,
    placeholder_data: str,
    video: dict[str, Any],
    metadata: str,
) -> None:
    # Retrieve the mocks dynamically as their tests are equal
    get_mock: list[Response] = request.getfixturevalue(mock)
    get_metadata: FileMetadata = request.getfixturevalue(metadata)

    add_responses(get_mock)

    if metadata == "vtt_metadata":
        subtitle_format = knuckles.SubtitlesFileFormat.VTT
    else:
        subtitle_format = knuckles.SubtitlesFileFormat.SRT

    download_path = subsonic.media_retrieval.get_captions(
        video["id"], tmp_path, subtitle_format
    )

    # Check if the file data has been altered
    with open(tmp_path / get_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / get_metadata.default_filename


@responses.activate
@pytest.mark.parametrize(
    "mock, metadata",
    [
        ("mock_get_captions_prefer_vtt", "vtt_metadata"),
        ("mock_get_captions_prefer_srt", "srt_metadata"),
    ],
)
def test_get_captions_with_a_preferred_file_format(
    request: FixtureRequest,
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock: str,
    tmp_path: Path,
    placeholder_data: str,
    video: dict[str, Any],
    metadata: str,
) -> None:
    # Retrieve the mocks dynamically as their tests are equal
    get_mock: list[Response] = request.getfixturevalue(mock)
    get_metadata: FileMetadata = request.getfixturevalue(metadata)

    add_responses(get_mock)

    if metadata == "vtt_metadata":
        subtitle_format = knuckles.SubtitlesFileFormat.VTT
    else:
        subtitle_format = knuckles.SubtitlesFileFormat.SRT

    download_path = subsonic.media_retrieval.get_captions(
        video["id"], tmp_path, subtitle_format
    )

    # Check if the file data has been altered
    with open(tmp_path / get_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / get_metadata.default_filename


@responses.activate
def test_get_cover_art_with_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_cover_art: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    cover_art_metadata: FileMetadata,
    cover_art_size: int,
) -> None:
    add_responses(mock_cover_art)

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path / cover_art_metadata.output_filename, cover_art_size
    )

    # Check if the file data has been altered
    with open(tmp_path / cover_art_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / cover_art_metadata.output_filename


@responses.activate
def test_get_cover_art_without_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_cover_art: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    song: dict[str, Any],
    cover_art_size: int,
    cover_art_metadata: FileMetadata,
) -> None:
    add_responses(mock_cover_art)

    download_path = subsonic.media_retrieval.get_cover_art(
        song["coverArt"], tmp_path, cover_art_size
    )

    # Check if the file data has been altered
    with open(tmp_path / cover_art_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / cover_art_metadata.default_filename


@responses.activate
def test_get_lyrics(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_lyrics: list[Response],
    lyrics: dict[str, Any],
) -> None:
    add_responses(mock_get_lyrics)

    response = subsonic.media_retrieval.get_lyrics(lyrics["artist"], lyrics["title"])

    assert response.artist_name == lyrics["artist"]
    assert response.song_title == lyrics["title"]
    assert response.lyrics == lyrics["value"]


@responses.activate
def test_get_avatar_with_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_avatar: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    username: str,
    avatar_metadata: FileMetadata,
) -> None:
    add_responses(mock_avatar)

    download_path = subsonic.media_retrieval.get_avatar(
        username, tmp_path / avatar_metadata.output_filename
    )

    # Check if the file data has been altered
    with open(tmp_path / avatar_metadata.output_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / avatar_metadata.output_filename


@responses.activate
def test_get_avatar_without_a_given_filename(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_avatar: list[Response],
    tmp_path: Path,
    placeholder_data: str,
    username: str,
    avatar_metadata: FileMetadata,
) -> None:
    add_responses(mock_avatar)

    download_path = subsonic.media_retrieval.get_avatar(username, tmp_path)

    # Check if the file data has been altered
    with open(tmp_path / avatar_metadata.default_filename, "r") as file:
        assert placeholder_data == file.read()

    assert download_path == tmp_path / avatar_metadata.default_filename
