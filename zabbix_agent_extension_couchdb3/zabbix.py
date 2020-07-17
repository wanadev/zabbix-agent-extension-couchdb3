import os
import re


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


def flatten_stats(data, prefix="couchdb3"):
    for key in data:
        if "value" in data[key]:
            if type(data[key]["value"]) is dict:
                continue  # FIXME skip complex values
            yield (
                    "%s.%s" % (prefix, key),
                    data[key]["value"],
                    data[key]["desc"])
        else:
            for item in flatten_stats(data[key], "%s.%s" % (prefix, key)):
                yield item
