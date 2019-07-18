# -*- coding: utf-8 -*-

"""Tests for FPL API Integrations."""
from pprint import pprint as pp
from fpl_exporter.fpl_exporter import get_metrics, parse_metrics

import responses
import requests
import json


def test_api_response_fixture(bootstrap_fixture):

    bootstrap_fixture_elements = [
        "events",
        "game_settings",
        "phases",
        "teams",
        "total_players",
        "elements",
        "element_stats",
        "element_types",
    ]

    new_elements_in_api_response = set(bootstrap_fixture.keys()) - set(
        bootstrap_fixture_elements
    )
    print(new_elements_in_api_response)

    for element in bootstrap_fixture_elements:
        assert element in bootstrap_fixture.keys()
        # pp(bootstrap_fixture[element])

def test_get_metrics(api_client_fixture, bootstrap_fixture):
    r = api_client_fixture.get("/", response_body=bootstrap_fixture)
    assert r.status_code == 200
    result = r.json()


def test_parse_metrics(bootstrap_fixture):

    team_metrics = {}
    metrics = parse_metrics(bootstrap_fixture)
    pp(metrics.keys())
    events = metrics["events"]
    game_settings = metrics["game_settings"]
    phases = metrics["phases"]
    teams = metrics["teams"]

    for team in teams:
        ticker = team["short_name"]
        team_metrics[ticker] = {}
        for metric in team:
            team_metrics[ticker][metric] = team[metric]
            pp(metric)
        team_metrics[ticker]["strength"] = team["strength"]

    pp(team_metrics)


@responses.activate
def test_total_players(bootstrap_fixture):

    url = "https://foobar.fpl.bar/foobar/api/bootstrap-static/"
    mock_response = json.dumps(bootstrap_fixture)
    responses.add(responses.GET, url, status=200, json=mock_response)
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(bootstrap_fixture["total_players"], int)


