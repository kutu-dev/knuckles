from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture
def scan_status() -> dict[str, Any]:
    return {"scanning": True, "count": 69}


@pytest.fixture
def mock_start_scan(
    mock_generator: MockGenerator, scan_status: dict[str, Any]
) -> Response:
    return mock_generator("startScan", {}, {"scanStatus": scan_status})


@pytest.fixture
def mock_get_scan_status(
    mock_generator: MockGenerator, scan_status: dict[str, Any]
) -> Response:
    return mock_generator("getScanStatus", {}, {"scanStatus": scan_status})
