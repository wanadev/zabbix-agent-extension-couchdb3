import argparse


def make_cli():
    cli = argparse.ArgumentParser()

    # Connexion info

    cli.add_argument(
            "--host",
            help="The CouchDB server host (default: localhost)",
            type=str,
            default="localhost")

    cli.add_argument(
            "--port",
            help="The CouchDB server port (default: 5984)",
            type=int,
            default=5984)

    cli.add_argument(
            "--user",
            help="The username to use for the connexion (default: admin)",
            type=str,
            default="admin")

    cli.add_argument(
            "--password",
            help="The password to use for the connexion (mandatory)",
            type=str,
            required=True)

    cli.add_argument(
            "--proto",
            help="The protocol to use (default: http)",
            type=str,
            default="http")

    # Extra

    cli.add_argument(
            "--show-json",
            help="Display the raw JSON stats from CouchDB and exit (no stats will be sent to Zabbix)",  # noqa
            action="store_true")

    cli.add_argument(
            "--show-stats",
            help="Display the available stats with their values and description and exit (no stats will be sent to Zabbix)",  # noqa
            action="store_true")

    return cli
