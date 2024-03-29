============
FPL Exporter
============


.. image:: https://img.shields.io/pypi/v/fpl_exporter.svg
        :target: https://pypi.python.org/pypi/fpl_exporter

.. image:: https://img.shields.io/travis/P6rguvyrst/fpl_exporter.svg
        :target: https://travis-ci.org/P6rguvyrst/fpl_exporter

.. image:: https://readthedocs.org/projects/fpl-exporter/badge/?version=latest
        :target: https://fpl-exporter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/P6rguvyrst/fpl_exporter/shield.svg
     :target: https://pyup.io/repos/github/P6rguvyrst/fpl_exporter/
     :alt: Updates



Prometheus Exporter for Fantasy Premier League.


* Free software: Apache Software License 2.0
* Documentation: https://fpl-exporter.readthedocs.io.

.. image:: static/images/fpl-1.png
   :scale: 50 %
   :align: left

.. image:: static/images/fpl-2.png
   :scale: 50 %
   :align: left


Installation & Upgrade
----------------------

helm upgrade fpl-exporter charts/incubator/prometheus-exporter --namespace exporter -f values.yaml --install



Internal Metrics
----------------

+--------------------------------------------+---------------------------------------------------+
| Metric                                     | Description                                       |
+============================================+===================================================+
| prometheus_exporter_fpl_work_time          | Time spent processing API response data           |
+--------------------------------------------+---------------------------------------------------+
| prometheus_exporter_fpl_api_response_time  | API response time                                 |
+--------------------------------------------+---------------------------------------------------+


Generic Metrics
---------------

+--------------------------------------------+---------------------------------------------------+
| Metric                                     | Description                                       |
+============================================+===================================================+
| fpl_players_total                          | Number of FPL players                             |
+--------------------------------------------+---------------------------------------------------+
| fpl_assets_total                           | Number of Premier League assets (players)         |
+--------------------------------------------+---------------------------------------------------+


Team Metrics
------------

+--------------------------------------------+---------------------------------------------------+
| Metric                                     | Description                                       |
+============================================+===================================================+
| fpl_team_availability                      | Team availability, current gameweek               |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_attack_home              | Team offensive strength on home games             |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_attack_away              | Team offensive strength on away games             |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_defence_home             | Team defensive strength on home games             |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_defence_away             | Team defensive strength on away games             |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_overal_home              | Team overall strength on home games               |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength_overal_away              | Team overall strength on away games               |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_strength                          | Team strength                                     |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_table_position                    | Team position in Premier League table             |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_table_points                      | Team points accumulated in Premier League table   |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_games_played                      | Games played                                      |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_games_won                         | Ganes won                                         |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_games_lost                        | Games lost                                        |
+--------------------------------------------+---------------------------------------------------+
| fpl_team_games_drawn                       | Games drawn                                       |
+--------------------------------------------+---------------------------------------------------+

Asset Metrics
-------------

+--------------------------------------------+---------------------------------------------------+
| Metric                                     | Description                                       |
+============================================+===================================================+
| fpl_asset_ict_index                        | Asset ICT Index                                   | 
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_influence                        | Asset Influence                                   | 
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_creatifity                       | Asset Creativity                                  | 
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_threat                           | Asset Threat                                      | 
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_selected_by_percent              | Asset Selected by people (percentage)             |
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_form                             | Asset Form                                        |
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_bonus                            | Asset Bonus                                       |
+--------------------------------------------+---------------------------------------------------+
| fpl_asset_bps                              | Asset Bonus Point Scores                          |
+--------------------------------------------+---------------------------------------------------+



**NB! There's more metrics instrumented, but since I haven't yet found use for them and don't want to overload exporter with useless functionality. Defined metrics can be found at fpl_exporter/metrics.py.**


Features
--------

  * HELP: fpl-exporter --help
  * DEBUG MODE: fpl-exporter -vd -p bootstrap-static


Endpoints
---------
https://fantasy.premierleague.com/api/entry/{teamId}/history
https://fantasy.premierleague.com/api/entry/{teamId}

https://fantasy.premierleague.com/api/fixtures
https://fantasy.premierleague.com/api/bootstrap-static
http://fantasy.premierleague.com/api/element-summary/{playerId}

http://fantasy.premierleague.com/api/leagues-classic-standings/{leagueId}
http://fantasy.premierleague.com/api/leagues-h2h-standings/{leagueId}


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
