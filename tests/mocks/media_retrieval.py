from pathlib import Path
from typing import Protocol

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture()
def mock_stream():
    ...


class MockDownload(Protocol):
    def __call__(
        self,
        song_id: str,
        temp_dir_path: Path,
        headers: dict[str, str] = {},
    ) -> Response:
        ...


@pytest.fixture()
def placeholder_text() -> str:
    return "Lorem Ipsum"


@pytest.fixture
def input_filename() -> str:
    return "input.wav"


@pytest.fixture
def output_filename() -> str:
    return "output.wav"


@pytest.fixture
def content_type() -> str:
    return "audio/wav"


@pytest.fixture
def mock_download(
    input_filename: str,
    placeholder_text: str,
    content_type: str,
    mock_generator: MockGenerator,
) -> MockDownload:
    def inner(
        song_id: str,
        temp_dir_path: Path,
        headers: dict[str, str] = {},
    ):
        fake_song = temp_dir_path / input_filename
        fake_song.touch()

        with open(fake_song, "w") as file:
            file.write(placeholder_text)

        with open(fake_song, "r") as file:
            return mock_generator(
                "download",
                {"id": song_id},
                headers=headers,
                content_type=content_type,
                body=file.read(),
            )

    return inner
