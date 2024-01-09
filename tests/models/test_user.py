from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.user import User
from responses import Response


@responses.activate
def test_user_generate(subsonic: Subsonic, mock_get_user, user: dict[str, Any]) -> None:
    responses.add(mock_get_user)

    response = subsonic.user_management.get_user(user["username"])
    response.admin_role = not user["adminRole"]
    response = response.generate()

    assert response.admin_role == user["adminRole"]


@responses.activate
def test_user_create(
    subsonic: Subsonic, mock_get_user, mock_create_user, user: dict[str, Any]
) -> None:
    responses.add(mock_get_user)
    responses.add(mock_create_user)

    response = subsonic.user_management.get_user(user["username"])
    response = response.create()

    assert type(response) is User


@responses.activate
def test_user_update(
    subsonic: Subsonic, mock_get_user, mock_update_user, user: dict[str, Any]
) -> None:
    responses.add(mock_get_user)
    responses.add(mock_update_user)

    response = subsonic.user_management.get_user(user["username"])
    response.update()

    assert type(response) is User


@responses.activate
def test_user_delete(
    subsonic: Subsonic, mock_get_user, mock_delete_user, user: dict[str, Any]
) -> None:
    responses.add(mock_get_user)
    responses.add(mock_delete_user)

    response = subsonic.user_management.get_user(user["username"])
    response.delete()

    assert type(response) is User


@responses.activate
def test_user_change_password(
    subsonic: Subsonic,
    mock_get_user,
    mock_change_password: Response,
    user: dict[str, Any],
    new_password: str,
) -> None:
    responses.add(mock_get_user)
    responses.add(mock_change_password)

    response = subsonic.user_management.get_user(user["username"])
    response = response.change_password(new_password)

    assert type(response) is User
