from typing import Any

import responses
from knuckles import Subsonic
from responses import Response

from tests.conftest import AddResponses


@responses.activate
def test_start_scan(
    add_responses: AddResponses,
    subsonic: Subsonic,
    scan_status: dict[str, Any],
    mock_start_scan: list[Response],
) -> None:
    add_responses(mock_start_scan)

    response = subsonic.media_library_scanning.start_scan()

    assert response.scanning == scan_status["scanning"]
    assert response.count == scan_status["count"]


@responses.activate
def test_get_scan_status(
    add_responses: AddResponses,
    subsonic: Subsonic,
    scan_status: dict[str, Any],
    mock_get_scan_status: list[Response],
) -> None:
    add_responses(mock_get_scan_status)

    response = subsonic.media_library_scanning.get_scan_status()

    assert response.scanning == scan_status["scanning"]
    assert response.count == scan_status["count"]
