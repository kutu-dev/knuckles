from typing import Any

import responses
from knuckles.subsonic import Subsonic
from responses import Response


@responses.activate
def test_get_internet_radio_stations(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)

    response = subsonic.internet_radio.get_internet_radio_stations()

    assert response[0].id == internet_radio_station["id"]


@responses.activate
def test_get_internet_radio_station(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)

    response = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )

    assert response.id == internet_radio_station["id"]
    assert response.name == internet_radio_station["name"]
    assert response.stream_url == internet_radio_station["streamUrl"]
    assert response.homepage_url == internet_radio_station["homepageUrl"]


@responses.activate
def test_create_internet_radio_station(
    subsonic: Subsonic,
    mock_create_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_create_internet_radio_station)

    response = subsonic.internet_radio.create_internet_radio_station(
        internet_radio_station["streamUrl"],
        internet_radio_station["name"],
        internet_radio_station["homepageUrl"],
    )

    assert type(response) == Subsonic


@responses.activate
def test_update_internet_radio_station(
    subsonic: Subsonic,
    mock_update_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_update_internet_radio_station)

    response = subsonic.internet_radio.update_internet_radio_station(
        internet_radio_station["id"],
        internet_radio_station["streamUrl"],
        internet_radio_station["name"],
        internet_radio_station["homepageUrl"],
    )

    assert type(response) == Subsonic


@responses.activate
def test_delete_internet_radio_station(
    subsonic: Subsonic,
    mock_delete_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_delete_internet_radio_station)

    response = subsonic.internet_radio.delete_internet_radio_station(
        internet_radio_station["id"],
    )

    assert type(response) == Subsonic
