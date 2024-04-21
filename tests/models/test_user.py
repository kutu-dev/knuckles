from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models.user import User
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_user_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_get_user)

    response = subsonic.user_management.get_user(user["username"])
    response.admin_role = not user["adminRole"]
    response = response.generate()

    assert response.admin_role == user["adminRole"]


@responses.activate
def test_user_create(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    mock_create_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_get_user)
    add_responses(mock_create_user)

    response = subsonic.user_management.get_user(user["username"])
    response = response.create()

    assert type(response) is User


@responses.activate
def test_user_update(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    mock_update_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_get_user)
    add_responses(mock_update_user)

    response = subsonic.user_management.get_user(user["username"])
    response.update()

    assert type(response) is User


@responses.activate
def test_user_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    mock_delete_user: list[Response],
    user: dict[str, Any],
) -> None:
    add_responses(mock_get_user)
    add_responses(mock_delete_user)

    response = subsonic.user_management.get_user(user["username"])
    response.delete()

    assert type(response) is User


@responses.activate
def test_user_change_password(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_user: list[Response],
    mock_change_password: list[Response],
    user: dict[str, Any],
    new_password: str,
) -> None:
    add_responses(mock_get_user)
    add_responses(mock_change_password)

    response = subsonic.user_management.get_user(user["username"])
    response = response.change_password(new_password)

    assert type(response) is User
