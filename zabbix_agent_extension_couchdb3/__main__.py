import sys
import json

from .cli import make_cli
from . import couchdb
from . import zabbix


def print_json(stats_json):
    print(json.dumps(stats_json, indent=4))


def print_stats(stats_json):
    stats = zabbix.flatten_stats(stats_json)
    for key, value, desc in stats:
        print("# %s" % desc)
        print("%s %s" % (key, str(value)))
        print()


def send_stats_to_zabbix(stats_json, hostname):
    stats = zabbix.flatten_stats(stats_json)
    return zabbix.send_stats(stats, hostname)


def main(args):
    cli = make_cli()
    options = cli.parse_args(args)

    stats_json = couchdb.get_stats(
            host=options.host,
            port=options.port,
            user=options.user,
            password=options.password,
            proto=options.proto)

    if options.show_json:
        print_json(stats_json)
    elif options.show_stats:
        print_stats(stats_json)
    else:
        hostname = zabbix.get_hostname()
        resp = send_stats_to_zabbix(stats_json, hostname)
        print(resp)


if __name__ == "__main__":
    main(sys.argv[1:])
