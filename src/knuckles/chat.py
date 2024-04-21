from typing import TYPE_CHECKING, Any

from .api import Api
from .models.chat_message import ChatMessage

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Chat:
    """Class that contains all the methods needed to interact
    with the chat calls in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/chat/>
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

        self.api.json_request("addChatMessage", {"message": message})

        return self.subsonic

    def get_chat_messages(self) -> list[ChatMessage]:
        """Calls to the "getChatMessages" endpoint of the API.

        :return: A list of ChatMessage objects.
        :rtype: list[ChatMessage]
        """

        response: list[dict[str, Any]] = self.api.json_request("getChatMessages")[
            "chatMessages"
        ]["chatMessage"]

        messages = [ChatMessage(self.subsonic, **message) for message in response]

        return messages
