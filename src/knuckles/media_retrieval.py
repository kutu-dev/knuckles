from enum import Enum
from mimetypes import guess_extension
from pathlib import Path
from typing import Any, Callable

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
        """Using the PreparedRequest object of the Requests request package generates a
        valid URL for any endpoint with a valid authentication parameter.

        :param endpoint: The endpoint of the API to be used.
        :type endpoint: str
        :param params: Extra parameters to be added to the URL.
        :type params: dict[str, Any]
        :return: The generated url.
        :rtype: str
        """

        prepared_request = PreparedRequest()
        prepared_request.prepare_url(
            f"{self.api.url}/rest/{endpoint}", {**self.api.generate_params(), **params}
        )

        # Ignore the type error caused by the url parameter of prepared_request
        # as the prepare_url method always set it to a string.
        return prepared_request.url  # type: ignore [return-value]

    @staticmethod
    def _download_file(response: Response, downloaded_file_path: Path) -> Path:
        """Downloads a file attached to a Response object.

        :param response: The response to get the download binary data.
        :type response: Response
        :param downloaded_file_path: The file path to save the downloaded file.
        :type downloaded_file_path: Path
        :return: The same path given in downloaded_file_path.
        :rtype: Path
        """

        response.raise_for_status()

        with open(downloaded_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return downloaded_file_path

    @classmethod
    def _handle_download(
        cls,
        response: Response,
        file_or_directory_path: Path,
        determinate_filename: Callable[[Response], str],
    ) -> Path:
        if not file_or_directory_path.is_dir():
            return cls._download_file(response, file_or_directory_path)

        filename = determinate_filename(response)

        return cls._download_file(response, file_or_directory_path / filename)

    def stream(
        self,
        id_: str,
        max_bitrate_rate: int | None = None,
        format_: str | None = None,
        time_offset: int | None = None,
        size: str | None = None,
        estimate_content_length: bool | None = None,
        converted: bool | None = None,
    ) -> str:
        """Returns a valid url for streaming the requested song or video

        :param id_: The id of the song or video to stream
        :type id_: str
        :param max_bitrate_rate: A limit for the stream bitrate
        :type max_bitrate_rate: int | None
        :param format_: The file format of preference to be used in the stream.
        :type format_: str | None
        :param time_offset: Only applicable to video streaming.
            An offset in seconds from where the video should start.
        :type time_offset: int | None
        :param size: Only applicable to video streaming.
            The resolution for the streamed video, in the format of "WIDTHHxHEIGHT".
        :type size: str | None
        :param estimate_content_length: If the response should set a
            Content-Length HTTP header with an estimation of the duration of the media.
        :type estimate_content_length: bool | None
        :param converted: Only applicable to video streaming.
            Try to retrieve from the server an optimize video in MP4 if it's available.
        :type converted: bool | None
        :return A url that points to the given song in the stream endpoint
        :rtype str
        """

        return self._generate_url(
            "stream",
            {
                "id": id_,
                "maxBitRate": max_bitrate_rate,
                "format": format_,
                "timeOffset": time_offset,
                "size": size,
                "estimateContentLength": estimate_content_length,
                "converted": converted,
            },
        )

    def download(self, id_: str, file_or_directory_path: Path) -> Path:
        """Calls the "download" endpoint of the API.

        :param id_: The id of the song or video to download.
        :type id_: str
        :param file_or_directory_path: If a directory path is passed the file will be
            inside of it with the default filename given by the API,
            if not the file will be saved directly in the given path.
        :type file_or_directory_path: Path
        :return The path of the downloaded file
        :rtype Path
        """

        response = self.api.raw_request("download", {"id": id_})

        def determinate_filename(file_response: Response) -> str:
            filename = (
                file_response.headers["Content-Disposition"]
                .split("filename=")[1]
                .strip()
            )

            # Remove leading quote char
            if filename[0] == '"':
                filename = filename[1:]

            # Remove trailing quote char
            if filename[-1] == '"':
                filename = filename[:-1]

            return filename

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )

    def hls(
        self,
        id_: str,
        custom_bitrates: list[str] | None = None,
        audio_track_id: str | None = None,
    ) -> str:
        """Returns a valid url for streaming the requested song with hls.m3u8

        :param id_: The id of the song to stream.
        :type id_: str
        :param custom_bitrates: A list of bitrates to be added to the hls playlist
            for video streaming, the resolution can also be specified with
            this format: "BITRATE@WIDTHxHEIGHT".
        :type custom_bitrates: list[str] | None
        :param audio_track_id: The id of the audio track to be used
            if the playlist is for a video.
        :type audio_track_id: str | None
        :return A url that points to the given song in the hls.m3u8 endpoint
        :rtype str
        """

        return self._generate_url(
            "hls.m3u8",
            {"id": id_, "bitRate": custom_bitrates, "audioTrack": audio_track_id},
        )

    def get_captions(
        self,
        id_: str,
        file_or_directory_path: Path,
        subtitles_file_format: SubtitlesFileFormat = SubtitlesFileFormat.VTT,
    ) -> Path:
        """Calls the "getCaptions" endpoint of the API.

        :param id_: The ID of the video to get the captions
        :type id_: str
        :param file_or_directory_path: If a directory path is passed the file will be
            inside of it with the default filename given by the API,
            if not the file will be saved directly in the given path.
        :type file_or_directory_path: Path
        :param subtitles_file_format: The preferred captions file format.
        :type subtitles_file_format: SubtitlesFileFormat
        :return: The path of the downloaded captions file.
        :rtype:
        """

        # Check if the given file format is a valid one
        SubtitlesFileFormat(subtitles_file_format.value)

        response = self.api.raw_request(
            "getCaptions",
            {"id": id_, "format": subtitles_file_format.value},
        )

        def determinate_filename(file_response: Response) -> str:
            mime_type = file_response.headers["content-type"].partition(";")[0].strip()

            # application/x-subrip is not a valid MIME TYPE so a manual check is needed
            file_extension: str | None = None
            if mime_type == "application/x-subrip":
                file_extension = ".srt"
            else:
                file_extension = guess_extension(mime_type)

            return id_ + file_extension if file_extension else id_

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )

    def get_cover_art(
        self, id_: str, file_or_directory_path: Path, size: int | None = None
    ) -> Path:
        """Calls the "getCoverArt" endpoint of the API.

        :param id_: The id of the cover art to download.
        :type id_: str
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

        response = self.api.raw_request("getCoverArt", {"id": id_, "size": size})

        def determinate_filename(file_response: Response) -> str:
            file_extension = guess_extension(
                file_response.headers["content-type"].partition(";")[0].strip()
            )

            return id_ + file_extension if file_extension else id_

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )

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

        def determinate_filename(file_response: Response) -> str:
            file_extension = guess_extension(
                file_response.headers["content-type"].partition(";")[0].strip()
            )

            return username + file_extension if file_extension else username

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )
