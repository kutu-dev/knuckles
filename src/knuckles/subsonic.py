import hashlib
import secrets
from datetime import datetime
from typing import Any, Self
from urllib.parse import ParseResult, urlparse

import requests
from requests import Response

from .exceptions import (
    CODE_ERROR_EXCEPTIONS,
    CodeError0,
    CodeError10,
    CodeError20,
    CodeError30,
    CodeError40,
    CodeError41,
    CodeError50,
    CodeError60,
    CodeError70,
    InvalidRatingNumber,
    UnknownErrorCode,
)
from .models import (
    Album,
    Artist,
    ChatMessage,
    Jukebox,
    License,
    ScanStatus,
    Song,
    SubsonicResponse,
)


class Subsonic:
    """The main class of the package.

    Allow easy interactions with the Subsonic API with the given authentication values.
    """

    def __init__(
        self,
        url: str,
        user: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
    ) -> None:
        """The main class of the package.

        Allow easy interactions with the Subsonic API
        with the given authentication values.

        :param url: The url of the Subsonic server.
        :type url: str
        :param user: The user to authenticate with
        :type user: str
        :param password: The password to authenticate with
        :type password: str
        :param client: A unique string identifying the client application.
        :type client: str
        :param use_https: If the requests should be sended using HTTPS,
            defaults to True
        :type use_https: bool, optional
        :param use_token: If the connection should send to the server the clean password
            or encode it in a token with a random salt, defaults to True
        :type use_token: bool, optional
        """

        self.user = user
        self.password = password
        self.client = client
        self.use_token = use_token

        # Sanitize url and ensure the correct protocol is used
        parsed_url: ParseResult = urlparse(url)

        # If the user accidentally specifies a protocol the url goes to netloc instead
        base_url: str = parsed_url.path if parsed_url.path != "" else parsed_url.netloc

        if use_https:
            self.url = f"https://{base_url}"
        else:
            self.url = f"http://{base_url}"

    def __generate_params(self, extra_params: dict[str, Any] = {}) -> dict[str, Any]:
        """Generate the parameters for any request to the API.

        This allow the user to change any variable in any time without issues.
        If it's enabled (True by default) it will generate a diferent token and salt
        for each call.

        :param extra_params: Extra parameters to be attached to the generated ones,
            defaults to {}.
        :type extra_params: dict[str, Any], optional
        :return: All the parameters needed by the Subsonic API to authenticate
            with the extra ones attached to them.
        :rtype: dict[str, Any]
        """

        params: dict[str, Any] = {
            "u": self.user,
            "v": "1.16.1",
            "c": self.client,
            "f": "json",
            **extra_params,
        }

        # Add authentication based in the method selected by the user
        if not self.use_token:
            return {
                **params,
                "p": self.password,
            }

        salt: str = secrets.token_hex(16)
        token: str = hashlib.md5(
            self.password.encode("utf-8") + salt.encode("utf-8")
        ).hexdigest()

        return {**params, "t": token, "s": salt}

    def __request_to_the_api(
        self, endpoint: str, extra_params: dict[str, Any] = {}
    ) -> dict[str, Any]:
        """Make a request to the Subsonic API.

        :param endpoint: The endpoint where the request should be made,
            only specifies the route name, without slashes.
            E.g. "ping", "getLicense", etc.
        :type endpoint: str
        :param extra_params: The extra parameters required by the endpoint,
            defaults to {}.
        :type extra_params: dict[str, Any], optional
        :raises code_error: Raises an exception with the format CodeErrorXX or
            UnknownCodeError if the request fails.
        :return: The JSON data inside the "subsonic-response" object.
        :rtype: dict[str, Any]
        """

        response: Response = requests.get(
            url=f"{self.url}/rest/{endpoint}",
            params=self.__generate_params(extra_params),
        )

        json_response: dict[str, Any] = response.json()["subsonic-response"]

        if json_response["status"] == "failed":
            code_error: CODE_ERROR_EXCEPTIONS = (
                self.__get_subsonic_code_error_exception(json_response["error"]["code"])
            )

            raise code_error(json_response["error"]["message"])

        return json_response

    @staticmethod
    def __get_subsonic_code_error_exception(
        error_code: int,
    ) -> CODE_ERROR_EXCEPTIONS:
        """With a given code error returns the corresponding exception.

        :param error_code: The error code.
        :type error_code: int
        :return: The associated exception with the error code.
        :rtype: CODE_ERROR_EXCEPTIONS
        """

        match error_code:
            case 0:
                return CodeError0
            case 10:
                return CodeError10
            case 20:
                return CodeError20
            case 30:
                return CodeError30
            case 40:
                return CodeError40
            case 41:
                return CodeError41
            case 50:
                return CodeError50
            case 60:
                return CodeError60
            case 70:
                return CodeError70
            case _:
                return UnknownErrorCode

    def ping(self) -> SubsonicResponse:
        """Calls to the "ping" endpoint of the API.

        Useful to test the status of the server.

        :return: An object with all the data received from the server.
        :rtype: SubsonicResponse
        """

        response: dict[str, Any] = self.__request_to_the_api("ping")

        return SubsonicResponse(**response)

    def get_license(self) -> License:
        """Calls to the "getLicense" endpoint of the API.

        :return: An object with all the information about the status of the license.
        :rtype: License
        """

        response: dict[str, Any] = self.__request_to_the_api("getLicense")["license"]

        return License(**response)

    def get_song(self, id: str) -> Song:
        """Calls to the "getSong" endpoint of the API.

        :param id: The ID of the song to get.
        :type id: str
        :return: An object with all the information
            that the server has given about the song.
        :rtype: Song
        """

        response: dict[str, Any] = self.__request_to_the_api("getSong", {"id": id})[
            "song"
        ]

        return Song(self, **response)

    def get_scan_status(self) -> ScanStatus:
        """Calls to the "getScanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response: dict[str, Any] = self.__request_to_the_api("getScanStatus")[
            "scanStatus"
        ]

        return ScanStatus(**response)

    def start_scan(self) -> ScanStatus:
        """Calls to the "scanStatus" endpoint of the API.

        :return: An object with the information about the status of the scan.
        :rtype: ScanStatus
        """

        response: dict[str, Any] = self.__request_to_the_api("startScan")["scanStatus"]

        return ScanStatus(**response)

    def add_chat_message(self, message: str) -> Self:
        """Calls to the "addChatMessage" endpoint of the API:

        :param message: The message to send.
        :type message: str
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.__request_to_the_api("addChatMessage", {"message": message})

        return self

    def get_chat_messages(self) -> list[ChatMessage]:
        """Calls to the "getChatMessages" endpoint of the API.

        :return: A list with objects containing
            each one all the information given about each message.
        :rtype: list[ChatMessage]
        """

        response: list[dict[str, Any]] = self.__request_to_the_api("getChatMessages")[
            "chatMessages"
        ]["chatMessage"]

        messages: list[ChatMessage] = [ChatMessage(**message) for message in response]

        return messages

    def star_song(self, song: Song | str) -> Self:
        """Calls the "star" endpoint of the API.

        :param song: Either a Song object or the ID of a song to star.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        self.__request_to_the_api("star", {"id": id})

        return self

    def star_album(self, album: Album | str) -> Self:
        """Calls the "star" endpoint of the API.

        :param album: Either a Album object or the ID of a album to star.
        :type album: Album | str
        :raises TypeError: Raised if the passed value to song isn't a Album object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(album) is Album:
            id = album.id
        elif type(album) is str:
            id = album
        else:
            raise TypeError("The type of the album parameter is invalid")

        self.__request_to_the_api("star", {"albumId": id})

        return self

    def star_artist(self, artist: Artist | str) -> Self:
        """Calls the "star" endpoint of the API.

        :param artist: Either a Artist object or the ID of a artist to star.
        :type artist: Artist | str
        :raises TypeError: Raised if the passed value to artist isn't a Artist object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(artist) is Artist:
            id = artist.id
        elif type(artist) is str:
            id = artist
        else:
            raise TypeError("The type of the artist parameter is invalid")

        self.__request_to_the_api("star", {"artistId": id})

        return self

    def unstar_song(self, song: Song | str) -> Self:
        """Calls the "unstar" endpoint of the API.

        :param song: Either a Song object or the ID of a song to unstar.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        self.__request_to_the_api("unstar", {"id": id})

        return self

    def unstar_album(self, album: Album | str) -> Self:
        """Calls the "unstar" endpoint of the API.

        :param album: Either a Album object or the ID of a album to unstar.
        :type album: Album | str
        :raises TypeError: Raised if the passed value to song isn't a Album object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(album) is Album:
            id = album.id
        elif type(album) is str:
            id = album
        else:
            raise TypeError("The type of the album parameter is invalid")

        self.__request_to_the_api("unstar", {"albumId": id})

        return self

    def unstar_artist(self, artist: Artist | str) -> Self:
        """Calls the "unstar" endpoint of the API.

        :param artist: Either a Artist object or the ID of a artist to unstar.
        :type artist: Artist | str
        :raises TypeError: Raised if the passed value to artist isn't a Artist object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(artist) is Artist:
            id = artist.id
        elif type(artist) is str:
            id = artist
        else:
            raise TypeError("The type of the artist parameter is invalid")

        self.__request_to_the_api("unstar", {"artistId": id})

        return self

    def set_rating(self, song: Song | str, rating: int) -> Self:
        """Calls to the "setRating" endpoint of the API.

        :param song: Either a Song object or the ID of a song to set its rating.
        :type song: Song | str
        :param rating: The rating to set. It should be a number
            between 1 and 5 (inclusive).
        :type rating: int
        :raises InvalidRatingNumber: Raised if the given rating number
            isn't in the valid range.
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        if rating not in range(1, 6):
            raise InvalidRatingNumber(
                (
                    "Invalid rating number, "
                    + "only numbers between 1 and 5 (inclusive) are allowed"
                )
            )

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        self.__request_to_the_api("setRating", {"id": id, "rating": rating})

        return self

    def remove_rating(self, song: Song | str) -> Self:
        """Calls the "setRating" endpoint of the API with a rating of 0.

        :param song: Either a Song object or the ID of a song to set its rating.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        self.__request_to_the_api("setRating", {"id": id, "rating": 0})

        return self

    def scrobble(
        self, song: Song | str, time: datetime, submission: bool = True
    ) -> Self:
        """Calls to the "scrobble" endpoint of the API

        :param song: Either a Song object or the ID of a song to set its rating.
        :type song: Song | str
        :param time: The time at which the song was listened to.
        :type time: datetime
        :param submission: If the scrobble is a submission
            or a "now playing" notification, defaults to True.
        :type submission: bool, optional
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        self.__request_to_the_api(
            "scrobble", {"id": id, "time": time.timestamp(), "submission": submission}
        )

        return self

    def jukebox_get(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "get".

        :return: An object with all the given information about the jukebox.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "get"}
        )["jukeboxPlaylist"]

        return Jukebox(self, **response)

    def jukebox_status(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "get".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "status"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_set(self, song: Song | str) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "set".

        :param song: Either a Song object or the ID of a song to set it in the jukebox.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "set", "id": id}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_start(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "start".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "start"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_stop(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "stop".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "stop"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_skip(self, index: int, offset: float = 0) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "skip".

        :param index: The index in the jukebox playlist to skip to.
        :type index: int
        :param offset: Start playing this many seconds into the track, defaults to 0
        :type offset: float, optional
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "skip", "index": index, "offset": offset}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_add(self, song: Song | str) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "add".

        :param song: Either a Song object or the ID of a song to add it in the jukebox.
        :type song: Song | str
        :raises TypeError: Raised if the passed value to song isn't a Song object
             or an ID.
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        id: str
        if type(song) is Song:
            id = song.id
        elif type(song) is str:
            id = song
        else:
            raise TypeError("The type of the song parameter is invalid")

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "add", "id": id}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_clear(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "clear".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "clear"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_remove(self, index: int) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "remove".

        :param index: The index in the jukebox playlist for the song to remove.
        :type index: int
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "remove", "index": index}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_shuffle(self) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "shuffle".

        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "shuffle"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_set_gain(self, gain: float) -> Jukebox:
        """Calls the "jukeboxControl" endpoint of the API with the action "setGain"

        :param gain: A number between 0 and 1 (inclusive) to set the gain.
        :type gain: float
        :raises ValueError: Raised if the gain argument isn't between the valid range.
        :return: An object with all the given information about the jukebox.
        Except the jukebox playlist.
        :rtype: Jukebox
        """

        if not 1 > gain > 0:
            raise ValueError("The gain should be between 0 and 1 (inclusive)")

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "setGain", "gain": gain}
        )["jukeboxStatus"]

        return Jukebox(self, **response)
