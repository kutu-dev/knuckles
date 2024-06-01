from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from knuckles.models._model import Model
from knuckles.models._user import User


class ChatMessage(Model):
    """Object that holds all the info about a chat message.

    Attributes:
        user (User): The user author of the chat message.
        message: The message send by the user.
        time (datetime): The timestamp when the chat message was send.
    """

    def __init__(
        self, subsonic: "Subsonic", username: str, time: int, message: str
    ) -> None:
        super().__init__(subsonic)

        self.user = User(self._subsonic, username)
        self.message = message

        # Divide by 1000 as the Subsonic API return in milliseconds instead of seconds
        self.time: datetime = datetime.fromtimestamp(time / 1000)
