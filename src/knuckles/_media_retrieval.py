from enum import Enum
from mimetypes import guess_extension
from pathlib import Path
from typing import TYPE_CHECKING, Callable

from requests import Response

if TYPE_CHECKING:
    from ._subsonic import Subsonic

from ._api import Api
from .models._lyrics import Lyrics


class SubtitlesFileFormat(Enum):
    VTT = "vtt"
    SRT = "srt"


class MediaRetrieval:
    """Class that contains all the methods needed to interact with the
    [media retrieval endpoints](https://opensubsonic.netlify.app/
    categories/media-retrieval/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    @staticmethod
    def _download_file(response: Response, downloaded_file_path: Path) -> Path:
        """Download to the local filesystem the binary file data attached to a
        `requests` Response object.
        Doesn't check if the Response object is valid for file downloading.

        Args:
            response: The response object to get the file from.
            downloaded_file_path: A path where the file to download should
                be saved.

        Returns:
            The path where the file was finally saved.
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
        """Download the file attached with the given `requests` Response
        object, if the given path is a directory then the file will be
        downloaded inside of it, if its a valid file path it will be downloaded
        using this exact filename.

        In case of not being a directory then a custom callback to determine
        the name of the file to be created.


        Args:
            response: The response object to get the file from.
            file_or_directory_path: The directory or filename where the file
                should be saved to.
            determinate_filename: The callback to be used to determine the
                filename in case the given path points to a directory.

        Returns:
            The path where the file was finally saved.
        """

        if not file_or_directory_path.is_dir():
            return cls._download_file(response, file_or_directory_path)

        filename = determinate_filename(response)

        return cls._download_file(response, file_or_directory_path / filename)

    def stream(
        self,
        song_or_video_id: str,
        max_bitrate_rate: int | None = None,
        stream_format: str | None = None,
        time_offset: int | None = None,
        size: str | None = None,
        estimate_content_length: bool | None = None,
        converted: bool | None = None,
    ) -> str:
        """Get the URL required to stream a song or video.

        Args:
            song_or_video_id: The ID of the song or video to get its
                steam URL
            max_bitrate_rate: The max bitrate the stream should have.
            stream_format: The format the song or video should be.
                **Warning**: The available formats are dependant of the
                server implementation. The only secure format is "raw",
                which disabled transcoding at all.
            time_offset: An offset where the stream should start. It may
                not work with video, depending of the server configuration.
            size: The maximum resolution of the streaming in the format `WxH`,
                only works with video streaming.
            estimate_content_length: When set to true the response with have
                the `Content-Length` HTTP header set to a estimated duration
                for the streamed song or video.
            converted: If set to true the server will try to stream a
                transcoded version in `MP4`. Only works with video
                streaming.

        Returns:
            An URL with all the needed parameters to start a streaming
                using a GET request.
        """

        return self.subsonic.api.generate_url(
            "stream",
            {
                "id": song_or_video_id,
                "maxBitRate": max_bitrate_rate,
                "format": stream_format,
                "timeOffset": time_offset,
                "size": size,
                "estimateContentLength": estimate_content_length,
                "converted": converted,
            },
        )

    def download(self, song_or_video_id: str, file_or_directory_path: Path) -> Path:
        """Download a song or video from the server.

        Args:
            song_or_video_id: The ID of the song or video to download.
            file_or_directory_path: The path where the downloaded file should
                be saved. If the given path is a directory then the file will
                be downloaded inside of it, if its a valid file path it will be
                downloaded using this exact filename.

        Returns:
            The path where the song or video was finally saved.
        """

        response = self.api.raw_request("download", {"id": song_or_video_id})

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
        song_or_video_id: str,
        custom_bitrates: list[str] | None = None,
        audio_track_id: str | None = None,
    ) -> str:
        """Get the URL required to stream a song or video with hls.m3u8.

        Args:
            song_or_video_id: The ID of the song or video to stream.
            custom_bitrates: The bitrate that the server should try to
                limit the stream to. If more that one is specified the
                server will create a `variant playlist`, suitable for adaptive
                bitrate streaming.
            audio_track_id: The ID of an audio track to be added to the stream
                if video is being streamed.

        Returns:
            An URL with all the needed parameters to start a streaming
                with hls.m3u8 using a GET request.
        """

        return self.subsonic.api.generate_url(
            "hls.m3u8",
            {
                "id": song_or_video_id,
                "bitRate": custom_bitrates,
                "audioTrack": audio_track_id,
            },
        )

    def get_captions(
        self,
        caption_id: str,
        file_or_directory_path: Path,
        subtitles_file_format: SubtitlesFileFormat = SubtitlesFileFormat.VTT,
    ) -> Path:
        """Download a video caption file from the server.

        Args:
            caption_id: The ID of the caption to download.
            file_or_directory_path: The path where the downloaded file should
                be saved. If the given path is a directory then the file will
                be downloaded inside of it, if its a valid file path it will be
                downloaded using this exact filename.
            subtitles_file_format: The format that the subtitle file should
                have.

        Returns:
            The path where the captions was finally saved.
        """

        # Check if the given file format is a valid one
        SubtitlesFileFormat(subtitles_file_format.value)

        response = self.api.raw_request(
            "getCaptions",
            {"id": caption_id, "format": subtitles_file_format.value},
        )

        def determinate_filename(file_response: Response) -> str:
            mime_type = file_response.headers["content-type"].partition(";")[0].strip()

            # application/x-subrip is not a valid MIME TYPE so a manual check is needed
            file_extension: str | None = None
            if mime_type == "application/x-subrip":
                file_extension = ".srt"
            else:
                file_extension = guess_extension(mime_type)

            return caption_id + file_extension if file_extension else caption_id

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )

    def get_cover_art(
        self, cover_art_id: str, file_or_directory_path: Path, size: int | None = None
    ) -> Path:
        """Download the cover art from the server.

        Args:
            cover_art_id: The ID of the cover art to download.
            file_or_directory_path: The path where the downloaded file should
                be saved. If the given path is a directory then the file will
                be downloaded inside of it, if its a valid file path it will be
                downloaded using this exact filename.
            size: The width in pixels that the image should have,
                the cover arts are always squares.

        Returns:
            The path where the captions was finally saved.
        """

        response = self.api.raw_request(
            "getCoverArt", {"id": cover_art_id, "size": size}
        )

        def determinate_filename(file_response: Response) -> str:
            file_extension = guess_extension(
                file_response.headers["content-type"].partition(";")[0].strip()
            )

            return cover_art_id + file_extension if file_extension else cover_art_id

        return self._handle_download(
            response, file_or_directory_path, determinate_filename
        )

    def get_lyrics(
        self, artist_name: str | None = None, song_title: str | None = None
    ) -> Lyrics:
        """Get the lyrics of a song.

        Args:
            artist_name: The name of the artist that made the song to get its
                lyrics from.
            song_title: The title of the song to get its lyrics from.

        Returns:
            An object that contains all the info about the requested
                lyrics.
        """

        response = self.api.json_request(
            "getLyrics", {"artist": artist_name, "title": song_title}
        )["lyrics"]

        return Lyrics(subsonic=self.subsonic, **response)

    def get_avatar(self, username: str, file_or_directory_path: Path) -> Path:
        """Download the avatar image of a user from the server.

        Args:
            username: The username of the user to get its avatar from.
            file_or_directory_path: The path where the downloaded file should
                be saved. If the given path is a directory then the file will
                be downloaded inside of it, if its a valid file path it will be
                downloaded using this exact filename.

        Returns:
            The path where the avatar image was finally saved.
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
