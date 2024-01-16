from typing import Any

import responses
from knuckles.subsonic import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_get_internet_radio_stations(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)

    response = subsonic.internet_radio.get_internet_radio_stations()

    assert response[0].id == internet_radio_station["id"]


@responses.activate
def test_get_internet_radio_station(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_get_internet_radio_stations: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_get_internet_radio_stations)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )

    assert response.id == internet_radio_station["id"]
    assert response.name == internet_radio_station["name"]
    assert response.stream_url == internet_radio_station["streamUrl"]
    assert response.homepage_url == internet_radio_station["homepageUrl"]


@responses.activate
def test_create_internet_radio_station(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_create_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_create_internet_radio_station)

    response = subsonic.internet_radio.create_internet_radio_station(
        internet_radio_station["streamUrl"],
        internet_radio_station["name"],
        internet_radio_station["homepageUrl"],
    )

    assert type(response) is Subsonic


@responses.activate
def test_update_internet_radio_station(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_update_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_update_internet_radio_station)

    response = subsonic.internet_radio.update_internet_radio_station(
        internet_radio_station["id"],
        internet_radio_station["streamUrl"],
        internet_radio_station["name"],
        internet_radio_station["homepageUrl"],
    )

    assert type(response) is Subsonic


@responses.activate
def test_delete_internet_radio_station(
    add_responses: AddResponses,
    subsonic: Subsonic,
    mock_delete_internet_radio_station: list[Response],
    internet_radio_station: dict[str, Any],
) -> None:
    add_responses(mock_delete_internet_radio_station)

    response = subsonic.internet_radio.delete_internet_radio_station(
        internet_radio_station["id"],
    )

    assert type(response) is Subsonic
