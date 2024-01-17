from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def internet_radio_station() -> dict[str, Any]:
    return {
        "id": "1",
        "name": "HBR1.com - Dream Factory",
        "streamUrl": "https://ubuntu.hbr1.com:19800/ambient.aac",
        "homepageUrl": "https://www.hbr1.com/",
    }


@pytest.fixture
def mock_get_internet_radio_stations(
    mock_generator: MockGenerator, internet_radio_station
) -> list[Response]:
    return mock_generator(
        "getInternetRadioStations",
        {},
        {"internetRadioStations": {"internetRadioStation": [internet_radio_station]}},
    )


@pytest.fixture
def mock_create_internet_radio_station(
    mock_generator: MockGenerator, internet_radio_station
) -> list[Response]:
    return mock_generator(
        "createInternetRadioStation",
        {
            "streamUrl": internet_radio_station["streamUrl"],
            "name": internet_radio_station["name"],
            "homepageUrl": internet_radio_station["homepageUrl"],
        },
    )


@pytest.fixture
def mock_update_internet_radio_station(
    mock_generator: MockGenerator, internet_radio_station
) -> list[Response]:
    return mock_generator(
        "updateInternetRadioStation",
        {
            "id": internet_radio_station["id"],
            "streamUrl": internet_radio_station["streamUrl"],
            "name": internet_radio_station["name"],
            "homepageUrl": internet_radio_station["homepageUrl"],
        },
    )


@pytest.fixture
def mock_delete_internet_radio_station(
    mock_generator: MockGenerator, internet_radio_station
) -> list[Response]:
    return mock_generator(
        "deleteInternetRadioStation",
        {
            "id": internet_radio_station["id"],
        },
    )
