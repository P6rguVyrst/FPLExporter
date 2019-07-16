# -*- coding: utf-8 -*-

"""Tests for Prometheus Metrics for fpl_exporter."""

from fpl_exporter.metrics import FPLMetrics


MONITOR = FPLMetrics()


def test_players():
    total_players = 123
    MONITOR.players.set(total_players)
    collector = MONITOR.players.collect()[0]
    samples = collector.samples[0]
    assert int(samples.value) == total_players


def test_fpl_assets():

    elements = [1, 2, 3, 4]
    MONITOR.fpl_assets.set(len(elements))
    collector = MONITOR.fpl_assets.collect()[0]
    samples = collector.samples[0]
    assert int(samples.value) == len(elements)
