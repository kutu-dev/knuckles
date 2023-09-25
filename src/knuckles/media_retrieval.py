from pathlib import Path

from .api import Api


class MediaRetrieval:
    """Class that contains all the methods needed to interact
    with the media retrieval calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/media-retrieval/>
    """

    def __init__(self, api: Api) -> None:
        self.api = api

    def stream(self) -> None:
        ...

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

        response = self.api.request_raw("download", {"id": id})
        response.raise_for_status()

        if file_or_directory_path.is_dir():
            filename = response.headers["Content-Disposition"].split("filename=")[1]

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

    def hls(self) -> None:
        ...

    def get_captions(self) -> None:
        ...

    def get_cover_art(self) -> None:
        ...

    def get_lyrics(self) -> None:
        ...

    def get_avatar(self) -> None:
        ...
