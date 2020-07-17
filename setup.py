#!/usr/bin/env python
# encoding: UTF-8

import os

from setuptools import setup, find_packages


long_description = ""
if os.path.isfile("README.rst"):
    long_description = open("README.rst", "r").read()


setup(
    name="zabbix-agent-extension-couchdb3",
    version="0.1.0",
    description="Zabbix Agent extension to monitor CouchDB 3",
    url="https://github.com/wanadev/zabbix-agent-extension-couchdb3",
    license="BSD-3-Clause",

    long_description=long_description,
    keywords="zabbix monitoring couchdb couchdb3",

    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON",

    packages=find_packages(),

    install_requires=[
        "py-zabbix>=1.1.7",
        ],
    extras_require={
        "dev": [
            "nox",
            "flake8",
        ]},

    entry_points={
        "console_scripts": [
            "zabbix-agent-extension-couchdb3 = zabbix_agent_extension_couchdb3.__main__:main"  # noqa
        ]},

    )
