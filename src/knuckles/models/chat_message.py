from datetime import datetime


class ChatMessage:
    """Representation of all the data related to a chat message in Subsonic."""

    def __init__(self, username: str, time: int, message: str) -> None:
        """Representation of all the data related to a chat message in Subsonic.

        :param username: The username of the creator of the message
        :type username: str
        :param time: Time when the message was created.
        :type time: int
        :param message: The message content.
        :type message: str
        """

        self.username: str = username

        # Divide by 1000 as the Subsonic API return in milliseconds instead of seconds
        self.time: datetime = datetime.fromtimestamp(time / 1000)
        self.message: str = message
