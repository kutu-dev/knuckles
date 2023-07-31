import hashlib
import secrets
from typing import Any
from urllib.parse import ParseResult, urlparse

import requests
from requests import Response

from .exceptions import CODE_ERROR_EXCEPTIONS, get_code_error_exception


class Api:
    """Class used to internally access and requests to the Subsonic API.

    Allow easy interactions with the Subsonic API
    with the given authentication values.
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
        """Class used to internally access and interacts with the Subsonic API.

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

        pass

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

    def generate_params(self, extra_params: dict[str, Any] = {}) -> dict[str, Any]:
        """Generate the parameters for any request to the API.

        This allows the user to change any variable in any time without issues.
        If it's enabled (True by default) it will generate a different token and salt
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

    def request(
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
            params=self.generate_params(extra_params),
        )

        json_response: dict[str, Any] = response.json()["subsonic-response"]

        if json_response["status"] == "failed":
            code_error: CODE_ERROR_EXCEPTIONS = get_code_error_exception(
                json_response["error"]["code"]
            )

            raise code_error(json_response["error"]["message"])

        return json_response
