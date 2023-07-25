import hashlib
import secrets
from datetime import datetime
from typing import Any, Self
from urllib.parse import ParseResult, urlparse

import requests
from requests import Response

from .exceptions import (
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
from .models import ChatMessage, Jukebox, License, ScanStatus, Song, SubsonicResponse


class Subsonic:
    def __init__(
        self,
        url: str,
        user: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
    ) -> None:
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

        This allow the user to change any variable without issues.

        Returns:
            dict[str, str]: Dictionary containing only the parameters necessary
            for authenticating in the API.
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
        self, subroute: str, extra_params: dict[str, Any] = {}
    ) -> dict[str, Any]:
        """Make a request to the Subsonic API

        Args:
            subroute (str): The subroute inside the API to call.
            E.g., "ping", "getLicense", etc.

            extra_params (dict[str, str], optional): Extra parameters to be added
            to the request. E.g., "id", "query", etc. Defaults to {}.

        Returns:
            dict[str, Any]: Return the subsonic response of the server
        """

        response: Response = requests.get(
            url=f"{self.url}/rest/{subroute}",
            params=self.__generate_params(extra_params),
        )

        json_response: dict[str, Any] = response.json()["subsonic-response"]

        if json_response["status"] == "failed":
            raise self.__get_code_error(json_response["error"]["code"])(
                json_response["error"]["message"]
            )

        return json_response

    @staticmethod
    def __get_code_error(
        error_code: int,
    ) -> type[
        CodeError0
        | CodeError10
        | CodeError20
        | CodeError30
        | CodeError40
        | CodeError41
        | CodeError50
        | CodeError60
        | CodeError70
        | UnknownErrorCode
    ]:
        """Get the exception associated to the given Subsonic error code

        Args:
            error_code (int): The Subsonic error code

        Returns:
            type[ CodeError0 | CodeError10 | CodeError20 | CodeError30 | CodeError40 |
            CodeError41 | CodeError50 | CodeError60 | CodeError70 | UnknownErrorCode ]:
            The exception associated with the provided error code
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
        response: dict[str, Any] = self.__request_to_the_api("ping")

        return SubsonicResponse(**response)

    def get_license(self) -> License:
        response: dict[str, Any] = self.__request_to_the_api("getLicense")["license"]

        return License(**response)

    def get_song(self, id: str) -> Song:
        response: dict[str, Any] = self.__request_to_the_api("getSong", {"id": id})[
            "song"
        ]

        return Song(self, **response)

    def get_scan_status(self) -> ScanStatus:
        response: dict[str, Any] = self.__request_to_the_api("getScanStatus")

        return ScanStatus(**response["scanStatus"])

    def start_scan(self) -> ScanStatus:
        response: dict[str, Any] = self.__request_to_the_api("startScan")["scanStatus"]

        return ScanStatus(**response)

    def add_chat_message(self, message: str) -> Self:
        self.__request_to_the_api("addChatMessage", {"message": message})

        return self

    def get_chat_messages(self) -> list[ChatMessage]:
        response: list[dict[str, Any]] = self.__request_to_the_api("getChatMessages")[
            "chatMessages"
        ]["chatMessage"]

        messages: list[ChatMessage] = [ChatMessage(**message) for message in response]

        return messages

    def star_song(self, id: str) -> Self:
        self.__request_to_the_api("star", {"id": id})

        return self

    def star_album(self, id: str) -> Self:
        self.__request_to_the_api("star", {"albumId": id})

        return self

    def star_artist(self, id: str) -> Self:
        self.__request_to_the_api("star", {"artistId": id})

        return self

    def unstar_song(self, id: str) -> Self:
        self.__request_to_the_api("unstar", {"id": id})

        return self

    def unstar_album(self, id: str) -> Self:
        self.__request_to_the_api("unstar", {"albumId": id})

        return self

    def unstar_artist(self, id: str) -> Self:
        self.__request_to_the_api("unstar", {"artistId": id})

        return self

    def set_rating(self, id: str, rating: int) -> Self:
        if rating not in range(1, 6):
            raise InvalidRatingNumber(
                (
                    "Invalid rating number, "
                    + "only numbers between 1 and 5 (inclusive) are allowed"
                )
            )

        self.__request_to_the_api("setRating", {"id": id, "rating": rating})

        return self

    def remove_rating(self, id: str) -> Self:
        self.__request_to_the_api("setRating", {"id": id, "rating": 0})

        return self

    def scrobble(self, id: str, time: datetime, submission: bool = True) -> Self:
        self.__request_to_the_api(
            "scrobble", {"id": id, "time": time.timestamp(), "submission": submission}
        )

        return self

    def jukebox_get(self) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "get"}
        )["jukeboxPlaylist"]

        return Jukebox(self, **response)

    def jukebox_status(self) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "status"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_set(self, song: Song | str) -> Jukebox:
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
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "start"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_stop(self) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "stop"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_skip(self, index: int, offset: float = 0) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "skip", "index": index, "offset": offset}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_add(self, song: Song | str) -> Jukebox:
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
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "clear"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_remove(self, index: int) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "remove", "index": index}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_shuffle(self) -> Jukebox:
        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "shuffle"}
        )["jukeboxStatus"]

        return Jukebox(self, **response)

    def jukebox_set_gain(self, gain: float) -> Jukebox:
        if not 1 > gain > 0:
            raise ValueError("The gain should be between 0 and 1 (inclusive)")

        response: dict[str, Any] = self.__request_to_the_api(
            "jukeboxControl", {"action": "setGain", "gain": gain}
        )["jukeboxStatus"]

        return Jukebox(self, **response)
