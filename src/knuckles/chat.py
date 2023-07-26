import typing
from typing import Any

from knuckles.api import Api
from knuckles.models import ChatMessage

if typing.TYPE_CHECKING:
    from knuckles.subsonic import Subsonic


class Chat:
    """Class that contains all the methods needed to interact
    with the chat calls in the Subsonic API. <https://opensubsonic.netlify.app/categories/chat/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def add_chat_message(self, message: str) -> "Subsonic":
        """Calls to the "addChatMessage" endpoint of the API:

        :param message: The message to send.
        :type message: str
        :return: The object itself to allow method chaining.
        :rtype: Self
        """

        self.api.request("addChatMessage", {"message": message})

        return self.subsonic

    def get_chat_messages(self) -> list[ChatMessage]:
        """Calls to the "getChatMessages" endpoint of the API.

        :return: A list with objects containing
            each one all the information given about each message.
        :rtype: list[ChatMessage]
        """

        response: list[dict[str, Any]] = self.api.request("getChatMessages")[
            "chatMessages"
        ]["chatMessage"]

        messages: list[ChatMessage] = [ChatMessage(**message) for message in response]

        return messages
