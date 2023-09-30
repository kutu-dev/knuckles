from enum import Enum
from mimetypes import guess_extension
from pathlib import Path
from typing import Any

from requests import Response
from requests.models import PreparedRequest

from .api import Api


class SubtitlesFileFormat(Enum):
    VTT = "vtt"
    SRT = "srt"


class MediaRetrieval:
    """Class that contains all the methods needed to interact
    with the media retrieval calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/media-retrieval/>
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def _generate_url(self, endpoint: str, params: dict[str, Any]) -> str:
        prepared_request = PreparedRequest()
        prepared_request.prepare_url(
            f"{self.api.url}/rest/{endpoint}", {**self.api.generate_params(), **params}
        )

        # Ignore the error caused by the url parameter of prepared_request
        # as the prepare_url method always set it to a string.
        return prepared_request.url  # type: ignore [return-value]

    def _download_file(
        self, response: Response, file_or_directory_path: Path, directory_filename: str
    ) -> Path:
        response.raise_for_status()

        if file_or_directory_path.is_dir():
            download_path = Path(
                file_or_directory_path,
                directory_filename,
            )
        else:
            download_path = file_or_directory_path

        with open(download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return download_path

    def stream(self, id: str) -> str:
        """Returns a valid url for streaming the requested song

        :param id: The id of the song to stream
        :type id: str
        :return A url that points to the given song in the stream endpoint
        :rtype str
        """

        return self._generate_url("stream", {"id": id})

    def download(self, id: str, file_or_directory_path: Path) -> Path:
        """Calls the "download" endpoint of the API.

        :param id: The id of the song or video to download.
        :type id: str
        :param file_or_directory_path: If a directory path is passed the file will be
        inside of it with the default filename given by the API,
        if not the file will be saved directly in the given path.
        :type file_or_directory_path: Path
        :return Returns the given path
        :rtype Path
        """

        response = self.api.raw_request("download", {"id": id})

        filename = response.headers["Content-Disposition"].split("filename=")[1].strip()

        # Remove leading quote char
        if filename[0] == '"':
            filename = filename[1:]

        # Remove trailing quote char
        if filename[-1] == '"':
            filename = filename[:-1]

        return self._download_file(response, file_or_directory_path, filename)

    def hls(self, id: str) -> str:
        """Returns a valid url for streaming the requested song with hls.m3u8

        :param id: The id of the song to stream.
        :type id: str
        :return A url that points to the given song in the hls.m3u8 endpoint
        :rtype str
        """

        return self._generate_url("hls.m3u8", {"id": id})

    def get_captions(
        self,
        id: str,
        file_or_directory_path: Path,
        subtitles_file_format: SubtitlesFileFormat = SubtitlesFileFormat.VTT,
    ) -> Path:
        # Check if the given file format is a valid one
        SubtitlesFileFormat(subtitles_file_format.value)

        response = self.api.raw_request(
            "getCaptions",
            {"id": id, "format": subtitles_file_format.value},
        )

        mime_type = response.headers["content-type"].partition(";")[0].strip()

        # As application/x-subrip is not a valid MIME TYPE a manual check is done
        file_extension: str | None
        if mime_type == "application/x-subrip":
            file_extension = ".srt"
        else:
            file_extension = guess_extension(mime_type)

        filename = id + file_extension if file_extension else id

        return self._download_file(response, file_or_directory_path, filename)

    def get_cover_art(
        self, id: str, file_or_directory_path: Path, size: int | None = None
    ) -> Path:
        """Calls the "getCoverArt" endpoint of the API.

        :param id: The id of the cover art to download.
        :type id: str
        :param file_or_directory_path: If a directory path is passed the file will be
        inside of it with the filename being the name of the user and
        a guessed file extension, if not the file will be saved
        directly in the given path.
        :type file_or_directory_path: Path
        :param size: The size of the image to be scale to in a square.
        :type size: int
        :return Returns the given path
        :rtype Path
        """

        response = self.api.raw_request("getCoverArt", {"id": id, "size": size})

        file_extension = guess_extension(
            response.headers["content-type"].partition(";")[0].strip()
        )

        filename = id + file_extension if file_extension else id

        return self._download_file(response, file_or_directory_path, filename)

    def get_lyrics(self) -> None:
        ...

    def get_avatar(self, username: str, file_or_directory_path: Path) -> Path:
        """Calls the "getAvatar" endpoint of the API.

        :param username: The username of the profile picture to download.
        :type username: str
        :param file_or_directory_path: If a directory path is passed the file will be
        inside of it with the filename being the name of the user and
        a guessed file extension, if not the file will be saved
        directly in the given path.
        :type file_or_directory_path: Path
        :return Returns the given path
        :rtype Path
        """

        response = self.api.raw_request("getAvatar", {"username": username})
        response.raise_for_status()

        file_extension = guess_extension(
            response.headers["content-type"].partition(";")[0].strip()
        )

        filename = username + file_extension if file_extension else username

        return self._download_file(response, file_or_directory_path, filename)
