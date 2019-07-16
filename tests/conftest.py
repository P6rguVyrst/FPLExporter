import json
import pytest
import responses
from fpl_exporter.fpl_exporter import APIClient


@pytest.fixture
def bootstrap_fixture(scope="session"):
    with open("tests/data/bootstrap-static.json") as data:
        res = json.load(data)
    return res


@pytest.fixture
def api_client_fixture(scope="session"):

    fpl_api_url = "https://foobar.fpl.bar/foobar/api/bootstrap-static/"
    mock_api_client = APIClient(fpl_api_url) # APIClientFactory? Returns an API client - mock or real.
    return mock_api_client
