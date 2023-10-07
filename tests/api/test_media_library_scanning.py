from typing import Any

import responses
from knuckles import Subsonic
from responses import Response


@responses.activate
def test_start_scan(
    subsonic: Subsonic, scan_status: dict[str, Any], mock_start_scan: Response
) -> None:
    responses.add(mock_start_scan)

    response = subsonic.media_library_scanning.start_scan()

    assert response.scanning == scan_status["scanning"]
    assert response.count == scan_status["count"]


@responses.activate
def test_get_scan_status(
    subsonic: Subsonic, scan_status: dict[str, Any], mock_get_scan_status: Response
) -> None:
    responses.add(mock_get_scan_status)

    response = subsonic.media_library_scanning.get_scan_status()

    assert response.scanning == scan_status["scanning"]
    assert response.count == scan_status["count"]
