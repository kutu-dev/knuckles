from typing import Any

import pytest
from responses import Response

from tests.conftest import MockGenerator


@pytest.fixture()
def mock_stream():
    ...


@pytest.fixture()
def mock_download(
    mock_generator_without_response: MockGenerator, song: dict[str, Any]
) -> Response:
    return mock_generator_without_response("download", {"id": song["id"]})
