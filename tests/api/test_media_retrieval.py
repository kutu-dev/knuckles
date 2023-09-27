from pathlib import Path
from typing import Any


import responses
from knuckles import Subsonic

from tests.mocks.media_retrieval import MockDownload


def test_stream() -> None:
    ...


@responses.activate
def test_download_with_a_given_filename(
    tmp_path: Path,
    output_filename: str,
    placeholder_text: str,
    mock_download: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
) -> None:
    responses.add(mock_download(song["id"], tmp_path))

    subsonic.media_retrieval.download(song["id"], tmp_path / output_filename)

    # Check if the file data has been unaltered
    with open(tmp_path / output_filename, "r") as file:
        assert placeholder_text == file.read()


@responses.activate
def test_download_without_a_given_filename(
    tmp_path: Path,
    input_filename: str,
    placeholder_text: str,
    mock_download: MockDownload,
    subsonic: Subsonic,
    song: dict[str, Any],
) -> None:
    responses.add(
        mock_download(
            song["id"],
            tmp_path,
            headers={"Content-Disposition": f'attachment; filename="{input_filename}"'},
        )
    )

    subsonic.media_retrieval.download(song["id"], tmp_path)

    # Check if the file data has been unaltered
    with open(tmp_path / input_filename, "r") as file:
        assert placeholder_text == file.read()
