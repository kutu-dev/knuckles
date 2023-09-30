from mimetypes import guess_extension
from pathlib import Path
from typing import Any

from requests.models import PreparedRequest

from .api import Api


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
        response.raise_for_status()

        if file_or_directory_path.is_dir():
            filename = (
                response.headers["Content-Disposition"].split("filename=")[1].strip()
            )

            # Remove leading quote char
            if filename[0] == '"':
                filename = filename[1:]

            # Remove trailing quote char
            if filename[-1] == '"':
                filename = filename[:-1]

            download_path = Path(
                file_or_directory_path,
                filename,
            )
        else:
            download_path = file_or_directory_path

        with open(download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return download_path

    def hls(self, id: str) -> str:
        """Returns a valid url for streaming the requested song with hls.m3u8

        :param id: The id of the song to stream.
        :type id: str
        :return A url that points to the given song in the hls.m3u8 endpoint
        :rtype str
        """

        return self._generate_url("hls.m3u8", {"id": id})

    def get_captions(self) -> None:
        ...

    def get_cover_art(self) -> None:
        ...

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

        if file_or_directory_path.is_dir():
            file_extension = guess_extension(
                response.headers["content-type"].partition(";")[0].strip()
            )

            filename = username + file_extension if file_extension else username

            download_path = Path(
                file_or_directory_path,
                filename,
            )
        else:
            download_path = file_or_directory_path

        with open(download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return download_path
