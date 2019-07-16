import json
import pytest


@pytest.fixture
def bootstrap_fixture(scope="session"):
    with open("tests/data/bootstrap-static.json") as data:
        res = json.load(data)
    return res
