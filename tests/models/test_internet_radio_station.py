from typing import Any

import responses
from knuckles.models.internet_radio_station import InternetRadioStation
from knuckles.subsonic import Subsonic
from responses import Response


@responses.activate
def test_generate(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)

    requested_station = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    requested_station.name = "Foo"
    requested_station = requested_station.generate()

    assert requested_station.name == internet_radio_station["name"]


@responses.activate
def test_create(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    mock_create_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)
    responses.add(mock_create_internet_radio_station)

    requested_station = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    requested_station = requested_station.create()

    assert type(requested_station) is InternetRadioStation


@responses.activate
def test_update(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    mock_update_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)
    responses.add(mock_update_internet_radio_station)

    requested_station = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    requested_station = requested_station.update()

    assert type(requested_station) is InternetRadioStation


@responses.activate
def test_delete(
    subsonic: Subsonic,
    mock_get_internet_radio_stations: Response,
    mock_delete_internet_radio_station: Response,
    internet_radio_station: dict[str, Any],
) -> None:
    responses.add(mock_get_internet_radio_stations)
    responses.add(mock_delete_internet_radio_station)

    requested_station = subsonic.internet_radio.get_internet_radio_station(
        internet_radio_station["id"]
    )
    requested_station = requested_station.delete()

    assert type(requested_station) is InternetRadioStation
