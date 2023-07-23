import hashlib
import re
import secrets
from typing import Any, Self
from urllib.parse import ParseResult, urlparse

import requests

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
    UnknownErrorCode,
)
from .models import ChatMessage, License, ScanStatus, Song, SubsonicResponse


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

    def __generate_params(self, extra_params: dict[str, str] = {}) -> dict[str, str]:
        """Generate the parameters for any request to the API.

        This allow the user to change any variable without issues.

        Returns:
            dict[str, str]: Dictionary containing only the parameters necessary
            for authenticating in the API.
        """

        params: dict[str, str] = {
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
        self, subroute: str, extra_params: dict[str, str] = {}
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

        response = requests.get(
            url=f"{self.url}/rest/{subroute}",
            params=self.__generate_params(extra_params),
        )

        print(f"{self.url}/rest/{subroute}")
        json_response: dict[str, Any] = response.json()["subsonic-response"]

        if json_response["status"] == "failed":
            raise self.__get_code_error(json_response["error"]["code"])(
                json_response["error"]["message"]
            )

        # Convert all the keys to snake case for creating dataclasses easier
        return self.__dict_to_snake_case(json_response)

    @staticmethod
    def __string_to_snake_case(string: str) -> str:
        """Convert a camelCase or PascalCase string to a snake_case string

        Args:
            string (str): The string to convert

        Returns:
            str: The string converted to snake_case
        """

        return re.sub("([A-Z]\w+$)", "_\\1", string).lower()

    def __dict_to_snake_case(self, dict_to_transform: dict[str, Any]) -> dict[str, Any]:
        """Convert all the keys in a dictionary to snake case

        Args:
            dict (dict[str, Any]): The dictionary to convert

        Returns:
            dict[str, Any]: The dictionary with the keys converted
        """

        return {
            self.__string_to_snake_case(key): self.__dict_to_snake_case(value)
            if type(value) is dict
            else value
            for key, value in dict_to_transform.items()
        }

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

        # Remove unnecessary keys
        del response["is_dir"]

        if "is_video" in response:
            del response["is_video"]

        if "original_width" in response:
            del response["original_width"]

        if "original_height" in response:
            del response["original_height"]

        return Song(self, **response)

    def get_scan_status(self) -> ScanStatus:
        response: dict[str, Any] = self.__request_to_the_api("getScanStatus")

        return ScanStatus(**response["scan_status"])

    def start_scan(self) -> ScanStatus:
        response: dict[str, Any] = self.__request_to_the_api("startScan")["scan_status"]

        return ScanStatus(**response)

    def add_chat_message(self, message: str) -> Self:
        self.__request_to_the_api("addChatMessage", {"message": message})

        return self

    def get_chat_messages(self) -> list[ChatMessage]:
        response: list[dict[str, Any]] = self.__request_to_the_api("getChatMessages")[
            "chat_messages"
        ]["chat_message"]

        messages: list[ChatMessage] = [ChatMessage(**message) for message in response]

        return messages
