from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_user(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_get_user)

    response = subsonic.user_management.get_user(user["username"])

    assert response.username == user["username"]
    assert response.password == user["password"]
    assert response.email == user["email"]
    assert response.ldap_authenticated == user["ldapAuthenticated"]
    assert response.admin_role == user["adminRole"]
    assert response.settings_role == user["settingsRole"]
    assert response.stream_role == user["streamRole"]
    assert response.jukebox_role == user["jukeboxRole"]
    assert response.download_role == user["downloadRole"]
    assert response.upload_role == user["uploadRole"]
    assert response.playlist_role == user["playlistRole"]
    assert response.cover_art_role == user["coverArtRole"]
    assert response.comment_role == user["commentRole"]
    assert response.podcast_role == user["podcastRole"]
    assert response.share_role == user["shareRole"]
    assert response.video_conversion_role == user["videoConversionRole"]
    assert response.music_folder_id == user["musicFolderId"]
    assert response.max_bit_rate == user["maxBitRate"]


@responses.activate
def test_get_users(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_users: list[Response],
    username: str,
) -> None:
    add_responses(mock_get_users)

    response = subsonic.user_management.get_users()

    assert response[0].username == username


@responses.activate
def test_create_user(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_create_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_create_user)

    response = subsonic.user_management.create_user(
        user["username"],
        user["password"],
        user["email"],
        user["ldapAuthenticated"],
        user["adminRole"],
        user["settingsRole"],
        user["streamRole"],
        user["jukeboxRole"],
        user["downloadRole"],
        user["uploadRole"],
        user["playlistRole"],
        user["coverArtRole"],
        user["commentRole"],
        user["podcastRole"],
        user["shareRole"],
        user["videoConversionRole"],
        user["musicFolderId"],
        user["maxBitRate"],
    )

    assert response.username == user["username"]


@responses.activate
def test_update_user(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_update_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_update_user)

    response = subsonic.user_management.update_user(
        user["username"],
        user["password"],
        user["email"],
        user["ldapAuthenticated"],
        user["adminRole"],
        user["settingsRole"],
        user["streamRole"],
        user["jukeboxRole"],
        user["downloadRole"],
        user["uploadRole"],
        user["playlistRole"],
        user["coverArtRole"],
        user["commentRole"],
        user["podcastRole"],
        user["shareRole"],
        user["videoConversionRole"],
        user["musicFolderId"],
        user["maxBitRate"],
    )

    assert response.username == user["username"]


@responses.activate
def test_delete_user(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_user: list[Response],
    username: str,
) -> None:
    add_responses(mock_delete_user)

    response = subsonic.user_management.delete_user(username)

    assert type(response) is Subsonic


@responses.activate
def test_change_password(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_change_password: list[Response],
    username: str,
    new_password: str,
) -> None:
    add_responses(mock_change_password)

    response = subsonic.user_management.change_password(username, new_password)

    assert type(response) is Subsonic
