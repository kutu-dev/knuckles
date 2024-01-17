from typing import Any

import responses
from knuckles.models.internet_radio_station import InternetRadioStation
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_generate(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    response.name = "Foo"
    response = response.generate()

    assert response.name == internet_radio_station["name"]


@responses.activate
def test_create(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    mock_create_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)
    add_responses(mock_create_internet_radio_station)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    response = response.create()

    assert type(response) is InternetRadioStation


@responses.activate
def test_update(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    mock_update_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)
    add_responses(mock_update_internet_radio_station)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    response = response.update()

    assert type(response) is InternetRadioStation


@responses.activate
def test_delete(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    mock_delete_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)
    add_responses(mock_delete_internet_radio_station)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    response = response.delete()

    assert type(response) is InternetRadioStation
