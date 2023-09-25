from pathlib import Path
from typing import Any

import responses
from knuckles import Subsonic
from responses import matchers


def test_stream() -> None:
    ...


@responses.activate
def test_download(
    tmp_path: Path, params: dict[str, Any], subsonic: Subsonic, song: dict[str, Any]
) -> None:
    placeholder_text = "Lorem Ipsum"

    # Create a temporally fake audio file
    fake_song = tmp_path / "test.wav"
    fake_song.touch()

    with open(fake_song, "w") as file:
        file.write(placeholder_text)

    # Mock the fake file into a request
    with open(fake_song, "rb") as file:
        responses.add(
            responses.GET,
            "https://example.com/rest/download",
            body=file.read(),
            content_type="audio/opus",
            match=[
                matchers.query_param_matcher(
                    {**params, "id": song["id"]}, strict_match=False
                )
            ],
            status=200,
        )

    subsonic.media_retrieval.download(song["id"], tmp_path / "output.wav")

    # Check if the file data has been unaltered
    with open(tmp_path / "output.wav", "r") as file:
        assert placeholder_text == file.read()
