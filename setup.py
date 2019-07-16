#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=6.0", "requests", "prometheus_client"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest", "responses"]

setup(
    author="Toomas Ormisson",
    author_email="contact@verypythonproblems.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Prometheus Exporter for Fantasy Premier League.",
    entry_points={"console_scripts": ["fpl-exporter=fpl_exporter.cli:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fpl_exporter",
    name="fpl_exporter",
    packages=find_packages(include=["fpl_exporter"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/P6rguvyrst/fpl_exporter",
    version="0.0.1",
    zip_safe=False,
)
