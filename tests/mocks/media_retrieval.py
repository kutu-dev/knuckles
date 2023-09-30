from pathlib import Path
from typing import Protocol, Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


class MockDownload(Protocol):
    def __call__(
        self,
        endpoint: str,
        extra_params: dict[str, Any],
        temp_dir_path: Path,
        content_type: str,
        headers: dict[str, str] = {},
    ) -> Response:
        ...


@pytest.fixture()
def placeholder_data() -> str:
    return "Lorem Ipsum"


@pytest.fixture
def default_song_filename() -> str:
    return "default.wav"


@pytest.fixture
def output_song_filename() -> str:
    return "output.wav"


@pytest.fixture
def song_content_type() -> str:
    return "audio/wav"


@pytest.fixture
def default_avatar_filename(username: str) -> str:
    return f"{username}.png"


@pytest.fixture
def output_avatar_filename() -> str:
    return "output.png"


@pytest.fixture
def avatar_content_type() -> str:
    return "image/png"


@pytest.fixture
def default_cover_art_filename(song: dict[str, Any]) -> str:
    return f"{song['coverArt']}.png"


@pytest.fixture
def output_cover_art_filename() -> str:
    return "output.png"


@pytest.fixture
def cover_art_content_type() -> str:
    return "image/png"


@pytest.fixture
def cover_art_size() -> int:
    return 512


@pytest.fixture
def mock_download_file(
    placeholder_data: str,
    mock_generator: MockGenerator,
) -> MockDownload:
    def inner(
        endpoint: str,
        extra_params: dict[str, Any],
        temp_dir_path: Path,
        content_type: str,
        headers: dict[str, str] = {},
    ):
        fake_file = temp_dir_path / "file.mock"
        fake_file.touch()

        with open(fake_file, "w") as file:
            file.write(placeholder_data)

        with open(fake_file, "r") as file:
            return mock_generator(
                endpoint,
                extra_params,
                headers=headers,
                content_type=content_type,
                body=file.read(),
            )

    return inner
