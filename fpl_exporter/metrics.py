# -*- coding: utf-8 -*-

from prometheus_client import Gauge, Enum
import logging

LOGGER = logging.getLogger(__name__)


class FPLMetrics:

    monitor_working_time = Gauge(
        "prometheus_exporter_fpl_work_time", "Exporter working time."
    )
    monitor_api_response_time = Gauge(
        "prometheus_exporter_fpl_api_response_time", "Exporter FPL API response time."
    )


    players = Gauge("fpl_players_total", "Number of FPL players.")
    fpl_assets = Gauge(
        "fpl_assets_total", "Number of football players in Premier League."
    )
    # TEAMS
    strength_attack_home = Gauge(
        "fpl_team_strength_attack_home", "Team offensive strength on home games.", ["team"]
    )
    strength_attack_away = Gauge(
        "fpl_team_strength_attack_away", "Team offensive strength on away games.", ["team"]
    )
    strength_defence_home = Gauge(
        "fpl_team_strength_defence_home", "Team defensive strength on home games.", ["team"]
    )
    strength_defence_away = Gauge(
        "fpl_team_strength_defence_away", "Team defensive strength on away games.", ["team"]
    )
    strength_overall_home = Gauge(
        "fpl_team_strength_overal_home", "Team overall strength on home games.", ["team"]
    )
    strength_overall_away = Gauge(
        "fpl_team_strength_overal_away", "Team overall strength on away games.", ["team"]
    )
    #form = Gauge(
    #    "fpl_team_form", "Team overal form.", ["team"]
    #)
    strength = Gauge(
        "fpl_team_strength", "Team strength.", ["team"]
    )
    #
    availability = Enum(
        "fpl_team_unavailable", "Team availability in current gameweek.", ["team"], states=["unknown", "available", "unavailable"]
    )
    position = Gauge(
        "fpl_team_table_position", "Team position in Premier League table.", ["team"]
    )
    points = Gauge(
        "fpl_team_table_points", "Team points accumulated in Premier League table.", ["team"]
    )
    played = Gauge(
        "fpl_team_games_played", "Games won.", ["team"]
    )
    win = Gauge(
        "fpl_team_games_won", "Games won.", ["team"]
    )
    loss = Gauge(
        "fpl_team_games_lost", "Games lost.", ["team"]
    )
    draw = Gauge(
        "fpl_team_games_drawn", "Games drawn.", ["team"]
    )
