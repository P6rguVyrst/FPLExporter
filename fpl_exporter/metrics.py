# -*- coding: utf-8 -*-

from prometheus_client import Gauge
import logging

LOGGER = logging.getLogger(__name__)


class FPLMetrics:

    players = Gauge("fpl_players_total", "Number of FPL players.")
    fpl_assets = Gauge(
        "fpl_assets_total", "Number of football players in Premier League."
    )
