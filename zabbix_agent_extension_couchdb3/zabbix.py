import os
import re

from pyzabbix import ZabbixMetric, ZabbixSender


_HOSTNAME_REGEXP = re.compile(r"^Hostname=(.+)\s*$")
_ZABBIX_CONFIG = "/etc/zabbix/zabbix_agentd.conf"


def get_hostname():
    if not os.path.isfile(_ZABBIX_CONFIG):
        print("Unable to read the hostname from the Zabbix Agent config")
        return "localhost"

    with open(_ZABBIX_CONFIG) as file_:
        for line in file_:
            if not _HOSTNAME_REGEXP.match(line):
                continue
            return _HOSTNAME_REGEXP.match(line).group(1)


def flatten_stats(stats_json, prefix="couchdb3"):
    for key in stats_json:
        if "value" in stats_json[key]:
            if type(stats_json[key]["value"]) is dict:
                continue  # FIXME skip complex values
            yield (
                    "%s.%s" % (prefix, key),
                    stats_json[key]["value"],
                    stats_json[key]["desc"])
        else:
            for item in flatten_stats(stats_json[key], "%s.%s" % (prefix, key)):  # noqa: E501
                yield item


def send_stats(stats, hostname="localhost"):
    packet = []
    for key, value, desc in stats:
        packet.append(ZabbixMetric(hostname, key, value))
    return ZabbixSender(use_config=True).send(packet)
