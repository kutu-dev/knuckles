from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._subsonic import Subsonic

from knuckles.models._model import Model


class ChatMessage(Model):
    """Representation of all the data related to a chat message in Subsonic."""

    def __init__(
        self, subsonic: "Subsonic", username: str, time: int, message: str
    ) -> None:
        """Representation of all the data related to a chat message in Subsonic.

        :param username: The username of the creator of the message
        :type username: str
        :param time: Time when the message was created.
        :type time: int
        :param message: The message content.
        :type message: str
        """

        super().__init__(subsonic)

        self.username: str = username
        self.message: str = message

        # Divide by 1000 as the Subsonic API return in milliseconds instead of seconds
        self.time: datetime = datetime.fromtimestamp(time / 1000)
