from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture()
def placeholder_data() -> str:
    return "Lorem Ipsum"


class MockDownload(Protocol):
    def __call__(
        self,
        endpoint: str,
        extra_params: dict[str, Any],
        content_type: str,
        headers: dict[str, str] = {},
    ) -> Response:
        ...


@pytest.fixture
def mock_download_file_generator(
    placeholder_data: str, mock_generator: MockGenerator, tmp_path: Path
) -> MockDownload:
    def inner(
        endpoint: str,
        extra_params: dict[str, Any],
        content_type: str,
        headers: dict[str, str] = {},
    ):
        fake_file = tmp_path / "file.mock"
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


@dataclass
class FileMetadata:
    # The default filename that Knuckles should use if no custom one is provided
    default_filename: str

    # The custom filename given to Knuckles
    output_filename: str

    content_type: str


@pytest.fixture
def download_metadata() -> FileMetadata:
    return FileMetadata("default.wav", "output.wav", "audio/wav")


@pytest.fixture
def mock_download(
    mock_download_file_generator: MockDownload,
    song: dict[str, Any],
    download_metadata: FileMetadata,
) -> Response:
    return mock_download_file_generator(
        "download",
        {"id": song["id"]},
        download_metadata.content_type,
        headers={
            "Content-Disposition": "attachment; "
            + f'filename="{download_metadata.default_filename}"'
        },
    )


@pytest.fixture
def cover_art_metadata(song: dict[str, Any]) -> FileMetadata:
    return FileMetadata(f"{song['coverArt']}.png", "output.png", "image/png")


@pytest.fixture
def cover_art_size() -> int:
    return 512


@pytest.fixture
def mock_cover_art(
    mock_download_file_generator: MockDownload,
    song: dict[str, Any],
    cover_art_metadata: FileMetadata,
    cover_art_size: int,
) -> Response:
    return mock_download_file_generator(
        "getCoverArt",
        {"id": song["coverArt"], "size": cover_art_size},
        cover_art_metadata.content_type,
    )


@pytest.fixture
def avatar_metadata(username: str) -> FileMetadata:
    return FileMetadata(f"{username}.png", "output.png", "image/png")


@pytest.fixture
def mock_avatar(
    mock_download_file_generator: MockDownload,
    username: str,
    avatar_metadata: FileMetadata,
) -> Response:
    return mock_download_file_generator(
        "getAvatar",
        {"username": username},
        avatar_metadata.content_type,
    )
