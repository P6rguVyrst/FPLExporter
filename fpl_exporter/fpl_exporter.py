# -*- coding: utf-8 -*-

"""Main module."""

import requests
import logging

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
    pass
