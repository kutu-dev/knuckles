from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.user import User
from responses import Response


@responses.activate
def test_get_user(
    subsonic: Subsonic, mock_get_user: Response, user: dict[str, Any]
) -> None:
    responses.add(mock_get_user)

    response = subsonic.user_management.get_user(user["username"])

    assert response.username == user["username"]
    assert response.email == user["email"]
    assert response.scrobbling_enabled == user["scrobblingEnabled"]
    assert response.admin_role == user["adminRole"]
    assert response.settings_role == user["settingsRole"]
    assert response.download_role == user["downloadRole"]
    assert response.upload_role == user["uploadRole"]
    assert response.playlist_role == user["playlistRole"]
    assert response.cover_art_role == user["coverArtRole"]
    assert response.comment_role == user["commentRole"]
    assert response.podcast_role == user["podcastRole"]
    assert response.stream_role == user["streamRole"]
    assert response.jukebox_role == user["jukeboxRole"]
    assert response.share_role == user["shareRole"]
    assert response.video_conversion_role == user["videoConversionRole"]


@responses.activate
def test_get_users(subsonic: Subsonic, mock_get_users: Response, username: str) -> None:
    responses.add(mock_get_users)

    response = subsonic.user_management.get_users()

    assert response[0].username == username


@responses.activate
def test_create_user(
    subsonic: Subsonic, mock_create_user: Response, user: dict[str, Any]
) -> None:
    responses.add(mock_create_user)

    response = subsonic.user_management.create_user(User(**user))

    assert response.username == user["username"]


@responses.activate
def test_update_user(
    subsonic: Subsonic, mock_update_user: Response, user: dict[str, Any]
) -> None:
    responses.add(mock_update_user)

    response = subsonic.user_management.update_user(User(**user))

    assert response.username == user["username"]


@responses.activate
def test_delete_user(
    subsonic: Subsonic, mock_delete_user: Response, username: str
) -> None:
    responses.add(mock_delete_user)

    response = subsonic.user_management.delete_user(username)

    assert type(response) == Subsonic


@responses.activate
def test_change_password(
    subsonic: Subsonic, mock_change_password: Response, username: str, new_password: str
) -> None:
    responses.add(mock_change_password)

    response = subsonic.user_management.change_password(username, new_password)

    assert type(response) == Subsonic
