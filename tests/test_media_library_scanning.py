from typing import Any

import responses
from knuckles import Subsonic
from knuckles.models import ScanStatus
from responses import matchers


@responses.activate
def test_start_scan(
    subsonic: Subsonic, params: dict[str, str], subsonic_response: dict[str, Any]
) -> None:
    subsonic_response["subsonic-response"]["scanStatus"] = {
        "scanning": True,
        "count": 25,
    }

    responses.add(
        responses.GET,
        url="https://example.com/rest/startScan",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: ScanStatus = subsonic.start_scan()

    assert response.scanning is True
    assert response.count == 25


@responses.activate
def test_get_scan_status(
    subsonic: Subsonic, params: dict[str, str], subsonic_response: dict[str, Any]
) -> None:
    subsonic_response["subsonic-response"]["scanStatus"] = {
        "scanning": True,
        "count": 25,
    }

    responses.add(
        responses.GET,
        url="https://example.com/rest/getScanStatus",
        match=[matchers.query_param_matcher(params, strict_match=False)],
        json=subsonic_response,
        status=200,
    )

    response: ScanStatus = subsonic.get_scan_status()

    assert response.scanning is True
    assert response.count == 25
