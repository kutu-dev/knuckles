from typing import TYPE_CHECKING, Any

from ._api import Api
from .models._chat_message import ChatMessage

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Chat:
    """Class that contains all the methods needed to interact with the
    [chat endpoints](https://opensubsonic.netlify.app/categories/chat)
    in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api
        self.subsonic = subsonic

    def add_chat_message(self, message: str) -> "Subsonic":
        """Add chat message.

        Args:
            message: The message content to add.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """
        self.api.json_request("addChatMessage", {"message": message})

        return self.subsonic

    def get_chat_messages(self) -> list[ChatMessage]:
        """Get all send chat messages.

        Returns:
            A list with all the messages info.
        """

        response: list[dict[str, Any]] = self.api.json_request("getChatMessages")[
            "chatMessages"
        ]["chatMessage"]

        messages = [ChatMessage(self.subsonic, **message) for message in response]

        return messages
