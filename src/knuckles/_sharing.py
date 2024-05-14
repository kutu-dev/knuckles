from datetime import datetime
from typing import TYPE_CHECKING

from ._api import Api
from .models._share import Share

if TYPE_CHECKING:
    from ._subsonic import Subsonic


class Sharing:
    """Class that contains all the methods needed to interact with the
    [sharing endpoints](https://opensubsonic.netlify.app/
    categories/sharing/) in the Subsonic API.
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_shares(self) -> list[Share]:
        """Get all the shares manageable by the authenticated user.

        Returns:
            A list that holds all the info about all the shares
                manageable by the user.
        """

        response = self.api.json_request("getShares")["shares"]["share"]

        return [Share(self.subsonic, **share) for share in response]

    def get_share(self, share_id: str) -> Share | None:
        """Get all the info about a share.

        Args:
            share_id: The ID of the share to get its info.

        Returns:
            An object that holds all the info about the requested
                share.
        """

        shares = self.get_shares()

        for share in shares:
            if share.id == share_id:
                return share

        return None

    def create_share(
        self,
        songs_ids: list[str],
        description: str | None = None,
        expires: datetime | None = None,
    ) -> Share:
        """Create a new share.

        Args:
            songs_ids: A list that holds the IDs of all the songs
                that the share can give access to.
            description: A description to be added with the share.
            expires: A timestamp that marks when the share should
                be invalidated.

        Returns:
            An object that holds all the info about the requested share.
        """

        response = self.api.json_request(
            "createShare",
            {
                "id": songs_ids,
                "description": description,
                "expires": expires.timestamp() * 1000 if expires else None,
            },
        )["shares"]["share"][0]

        return Share(self.subsonic, **response)

    def update_share(
        self,
        share_id: str,
        new_description: str | None = None,
        new_expires: datetime | None = None,
    ) -> Share:
        """Update the info of a share.

        Args:
            share_id: The ID of the share to update.
            new_description: A new description to be added to the share.
            new_expires: A new expire timestamp for the share.

        Returns:
            An object that holds all the new updated info for the share.
        """

        self.api.json_request(
            "updateShare",
            {
                "id": share_id,
                "description": new_description,
                "expires": new_expires.timestamp() * 1000 if new_expires else None,
            },
        )

        updated_share = Share(self.subsonic, share_id, description=new_description)

        # Set it manually as the constructor expects ISO 6801 to convert it to datetime
        # Instead of a datetime directly
        updated_share.expires = new_expires

        return updated_share

    def delete_share(self, share_id: str) -> "Subsonic":
        """Delete a share from the server.

        Args:
            share_id: The ID of the server to delete.

        Returns:
            The Subsonic object where this method was called to allow
                method chaining.
        """

        self.api.json_request("deleteShare", {"id": share_id})

        return self.subsonic
