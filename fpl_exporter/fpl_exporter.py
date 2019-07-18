# -*- coding: utf-8 -*-

"""Main module."""
import time
import requests
import logging
import responses
import prometheus_client
from pprint import pprint as pp
from .metrics import FPLMetrics


MONITOR = FPLMetrics()



LOGGER = logging.getLogger(__name__)


class APIClient:

    def __init__(self, api_url):
        self.api = api_url

    def __request(self, method: str, endpoint: str):
        url = self.api + endpoint
        LOGGER.debug(f"{method}::{url}")
        return requests.request(method, url)

    def get(self, endpoint):
        return self.__request("GET", endpoint)


class APIFixture:

    def __init__(self, api_url):
        self.api = api_url

    @responses.activate
    def get(self, endpoint, response_status=200, response_body=None):
        url = self.api + endpoint
        responses.add(
            responses.GET,
            url,
            status=response_status,
            json=response_body,
        )
        response = requests.get(url)
        return response


class APIClientFactory:

    @staticmethod
    def get_api(api_url, mode="generic"):
        flavours = {
            "generic": APIClient,
            "fixture": APIFixture,
        }
        return flavours[mode](api_url)


def prometheus_exporter(api_client):
    prometheus_client.start_http_server(5000)
    while True:
        metrics = get_metrics(api_client).json()
        parse_metrics(metrics)
        time.sleep(240)


def get_metrics(api_client):
    "Return response object."

    start = time.time()
    api_response = api_client.get("bootstrap-static/")
    end = time.time()
    elapsed = end - start
    MONITOR.monitor_api_response_time.set(elapsed)

    return api_response


def parse_metrics(metrics):

    start = time.time()

    MONITOR.players.set(metrics["total_players"])
    MONITOR.fpl_assets.set(len(metrics["elements"]))
    parse_teams(metrics["teams"])

    end = time.time()
    elapsed = end - start

    MONITOR.monitor_working_time.set(elapsed)
    return metrics

def parse_teams(teams):
    for team in teams:
        key = team["short_name"]
        MONITOR.availability.state(team_availability(str(team["unavailable"])))
        MONITOR.strength_attack_home.labels(key).set(team["strength_attack_home"])
        MONITOR.strength_attack_away.labels(key).set(team["strength_attack_away"])
        MONITOR.strength_defence_home.labels(key).set(team["strength_defence_home"])
        MONITOR.strength_defence_away.labels(key).set(team["strength_defence_away"])
        MONITOR.strength_overall_home.labels(key).set(team["strength_overall_home"])
        MONITOR.strength_overall_away.labels(key).set(team["strength_overall_away"])
        #MONITOR.form.labels(key).set(team["form"])
        MONITOR.strength.labels(key).set(team["strength"])
        MONITOR.position.labels(key).set(team["position"])
        MONITOR.points.labels(key).set(team["points"])
        MONITOR.played.labels(key).set(team["played"])
        MONITOR.win.labels(key).set(team["win"])
        MONITOR.loss.labels(key).set(team["loss"])
        MONITOR.draw.labels(key).set(team["draw"])


def team_availability(availability):
    router = {
        "True": "unavailable",
        "False": "available",
    }
    return router.get(availability, "unknown")
