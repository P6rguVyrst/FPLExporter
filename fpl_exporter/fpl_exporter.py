# -*- coding: utf-8 -*-

"""Main module."""
import time
import requests
import logging
from pprint import pprint as pp


LOGGER = logging.getLogger(__name__)


class APIClient:
    def __init__(self, api):
        self.api = api

    def __request(self, method: str, endpoint: str):
        url = self.api + endpoint
        LOGGER.debug(f"{method}::{url}")
        return requests.request(method, url)

    def get(self, endpoint):
        return self.__request("GET", endpoint)


def prometheus_exporter(api_client):
    metrics = get_metrics(api_client)
    parse_metrics(metrics)
    #while True:
    #    # Need a way to inject dummy URL to api_client
    #    metrics = get_metrics(api_client)
    #    parse_metrics(metrics)
    #    time.sleep(60)


def parse_metrics(bootstrap_dictionary):
    pp(bootstrap_dictionary)


def get_metrics(api_client):
    "Return response object."
    return api_client.get("bootstrap-static/")
