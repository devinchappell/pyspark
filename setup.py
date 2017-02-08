#!/usr/bin/env/python

from setuptools import setup, find_packages

setup(
    name="PySpark",
    version="0.9.0",

    description="An SDK for interacting with Cisco Spark",
    author="Devin Chappell",
    author_email='devin.chappell@live.ca',
    keywords='python',
    install_requires=["requests"],
    packages=find_packages(),
    include_pacjkage_data=True
)