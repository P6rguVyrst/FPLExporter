# -*- coding: utf-8 -*-

"""Console script for fpl_exporter."""
from .exceptions import UndefinedAPIPathException
from .fpl_exporter import APIClient, prometheus_exporter
import os
import sys
import click
import logging


@click.command()
@click.option("-p", "--path", help="Must be defined if using debug mode.")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.option(
    "-d", "--debug-mode", is_flag=True, help="Run ad hoc api commands against the API."
)
def main(path, verbose, debug_mode):
    """Console script for prometheus_artifactory_exporter."""
    if verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    fpl_api_url = os.getenv("FPL_API_URL", "https://fantasy.premierleague.com/api/")
    api_client = APIClient(fpl_api_url)
    if debug_mode:
        if not path:
            raise UndefinedAPIPathException(
                "Debug mode is for exploring Artifactory API endpoints."
            )
        print(api_client.get(path).text)
    else:
        prometheus_exporter(api_client)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
