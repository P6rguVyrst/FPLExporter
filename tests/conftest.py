import json
import pytest
import responses
from fpl_exporter.api import APIClientFactory


@pytest.fixture
def bootstrap_fixture(scope="session"):
    with open("tests/data/bootstrap-static.json") as data:
        res = json.load(data)
    return res


@pytest.fixture
def api_client_fixture(scope="session"):

    fpl_api_url = "https://foobar.fpl.bar/foobar/api/bootstrap-static/"
    mock_api_client = APIClientFactory().get_api(fpl_api_url, mode="fixture")
    return mock_api_client
