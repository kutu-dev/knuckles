from datetime import datetime
from typing import TYPE_CHECKING

from .api import Api
from .models.share import Share

if TYPE_CHECKING:
    from .subsonic import Subsonic


class Sharing:
    """Class that contains all the methods needed to interact
    with the sharing calls and actions in the Subsonic API.
    <https://opensubsonic.netlify.app/categories/sharing/>
    """

    def __init__(self, api: Api, subsonic: "Subsonic") -> None:
        self.api = api

        # Only to pass it to the models
        self.subsonic = subsonic

    def get_shares(self) -> list[Share]:
        """Calls the "getShares" endpoint of the API.

        :return: A list with all the shares given by the server.
        :rtype: list[Share]
        """

        response = self.api.request("getShares")["shares"]["share"]

        return [Share(self.subsonic, **share) for share in response]

    def get_share(self, id: str) -> Share | None:
        """Using the "getShares" endpoint iterates over all the shares
        and find the one with the same ID.

        :param id: The ID of the share to find.
        :type id: str
        :return: The found share or None if no one is found.
        :rtype: Share | None
        """

        shares = self.get_shares()

        for share in shares:
            if share.id == id:
                return share

        return None

    def create_share(
        self,
        songs_ids: list[str],
        description: str | None = None,
        expires: datetime | None = None,
    ) -> Share:
        """Calls the "createShare" endpoint of the API.

        :param songs_ids: A list with IDs of songs to add to the new share.
        :type songs_ids: list[str]
        :param description: A description for the share, defaults to None.
        :type description: str | None, optional
        :param expires: The time when the share should expires, defaults to None.
        :type expires: datetime | None, optional
        :return: The new created share.
        :rtype: Share
        """

        response = self.api.request(
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
        """Calls the "updateShare" endpoint of the API.

        :param share_id: The ID of the share to update.
        :type share_id: str
        :param new_description: A new description for the share, defaults to None.
        :type new_description: str | None, optional
        :param new_expires: A new expire date fot the share, defaults to None.
        :type new_expires: datetime | None, optional
        :return: An object with a Share object with all the updated info.
        :rtype: Share
        """

        self.api.request(
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
        """Calls the "deleteShare" endpoint of the API.

        :param share_id: The ID of the share to delete.
        :type share_id: str
        :return: The object itself to allow method chaining.
        :rtype: Subsonic
        """

        self.api.request("deleteShare", {"id": share_id})

        return self.subsonic
