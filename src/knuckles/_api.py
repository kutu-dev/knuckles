import hashlib
import secrets
from enum import Enum
from typing import Any
from urllib.parse import ParseResult, urlparse

import requests
from requests import Response
from requests.models import PreparedRequest

from .exceptions import ERROR_CODE_EXCEPTION, get_error_code_exception


class RequestMethod(Enum):
    GET = "get"
    POST = "post"


class Api:
    """Class in charge of managing the access to the REST API
    of the OpenSubsonic server.
    """

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        client: str,
        use_https: bool = True,
        use_token: bool = True,
        request_method: RequestMethod = RequestMethod.GET,
    ) -> None:
        """Class in charge of managing the access to the REST API of
        the OpenSubsonic server.

        Args:
            url: The base URL that points to the server,
                **without** the `/rest/` path.
            username: The name of the user to login as in the API.
            password: The password of the user to login as in the API.
            client: The name of the client to report to the API.
            use_https:  If HTTPS should be used.
            use_token: If the modern token based authentication should be used.
            request_method: If the requests should send the data as
                GET parameters or POST form data.
        """
        pass

        self.username = username
        self.password = password
        self.client = client
        self.use_token = use_token
        self.request_method = request_method

        # Sanitize url and ensure the correct protocol is used
        parsed_url: ParseResult = urlparse(url)

        # If the user accidentally specifies a protocol the url goes to netloc instead
        base_url: str = parsed_url.path if parsed_url.path != "" else parsed_url.netloc

        if use_https:
            self.url = f"https://{base_url}"
        else:
            self.url = f"http://{base_url}"

    def _generate_params(
        self, extra_params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Generates the parameters needed for a request to the API.

        Args:
            extra_params: Extra parameters to be added to the request.

        Returns:
            All the parameters with a randomly generated salt.
        """
        params: dict[str, Any] = {
            "u": self.username,
            "v": "1.16.1",
            "c": self.client,
            "f": "json",
        }

        if extra_params is not None:
            params.update(extra_params)

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

    def generate_url(self, endpoint: str, extra_params: dict[str, Any]) -> str:
        """Using the PreparedRequest object of the Requests request package
        generates a valid URL for any endpoint with
        a valid authentication parameter.


        Args:
            endpoint: The endpoint to be appended in the URL, **without** the
                leading `/rest/`.
            extra_params: The extra parameters to be added to the URL.

        Returns:
            A valid URL pointing to the desired endpoint and with the
                requested parameters, including the ones needed
                for authentication.
        """

        prepared_request = PreparedRequest()
        prepared_request.prepare_url(
            f"{self.url}/rest/{endpoint}", {**self._generate_params(extra_params)}
        )

        # Ignore the type error caused by the url parameter of prepared_request
        # as the prepare_url method always set it to a string.
        return prepared_request.url  # type: ignore [return-value]

    def raw_request(
        self, endpoint: str, extra_params: dict[str, Any] | None = None
    ) -> Response:
        """Makes a request to the OpenSubsonic server REST API.

        Args:
            endpoint: The endpoint to be appended in the URL, **without** the
                leading `/rest/`.
            extra_params: Extra parameters to the added to the request.

        Returns:
            The
                [`requests`](https://docs.python-requests.org/en/latest/index.html)
                `response` object of the executed request.
        """

        match self.request_method:
            case RequestMethod.POST:
                return requests.post(
                    url=f"{self.url}/rest/{endpoint}",
                    data=self._generate_params(extra_params),
                )

            case RequestMethod.GET | _:
                return requests.get(
                    url=f"{self.url}/rest/{endpoint}",
                    params=self._generate_params(extra_params),
                )

    def json_request(
        self, endpoint: str, extra_params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Makes a request to the OpenSubsonic server REST API and returns the
        data from the `subsonic_response` property. Should **never** be used
        with non-json compatible endpoints.

        Args:
            endpoint: The endpoint to be appended in the URL, **without** the
                leading `/rest/`.
            extra_params: Extra parameters to the added to the request.

        Raises:
            code_error: Raise an error if the server reports and issue with the
                request in the form of a code error, the raised follows
                the form `CodeErrorXX` where `XX` is the raised code error.
                `UnknownCodeError` is raised if the error code
                is not part of the standard.

        Returns:
            The data contained in the `subsonic_response` property.
        """

        response = self.raw_request(endpoint, extra_params)

        json_response: dict[str, Any] = response.json()["subsonic-response"]

        if json_response["status"] == "failed":
            code_error: ERROR_CODE_EXCEPTION = get_error_code_exception(
                json_response["error"]["code"]
            )

            raise code_error(json_response["error"]["message"])

        return json_response
