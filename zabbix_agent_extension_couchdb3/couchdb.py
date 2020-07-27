import json
import urllib.request


_ZABBIX_STATS_ROUTE = "/_node/_local/_stats"


def get_stats(host="localhost", port=5984, user="admin", password=None, proto="http"):  # noqa: E501
    if not password:
        raise Exception("The password parameter is mandatory")

    url = urllib.request.urlunparse((
        proto, "%s:%i" % (host, port), _ZABBIX_STATS_ROUTE, None, None, None))

    password_manager = urllib.request.HTTPPasswordMgrWithPriorAuth()
    password_manager.add_password(
            realm=None,
            uri=url,
            user=user,
            passwd=password,
            is_authenticated=True)

    auth_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    opener = urllib.request.build_opener(auth_handler)

    urllib.request.install_opener(opener)

    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def flatten_stats(stats_json, prefix="couchdb3"):
    for key in stats_json:
        if "value" in stats_json[key]:
            value = stats_json[key]["value"]
            desc = stats_json[key]["desc"]
            if type(stats_json[key]["value"]) is dict:
                if "min" in value:
                    yield (
                        "%s.%s.min" % (prefix, key),
                        value["min"],
                        desc)
                if "max" in value:
                    yield (
                        "%s.%s.max" % (prefix, key),
                        value["max"],
                        desc)
                if "median" in value:
                    yield (
                        "%s.%s.median" % (prefix, key),
                        value["median"],
                        desc)
                if "percentile" in value:
                    for perc, count in value["percentile"]:
                        yield (
                            "%s.%s.percentile[%i]" % (prefix, key, perc),
                            count,
                            desc)
            else:
                yield ("%s.%s" % (prefix, key), value, desc)
        else:
            for item in flatten_stats(stats_json[key], "%s.%s" % (prefix, key)):  # noqa: E501
                yield item
