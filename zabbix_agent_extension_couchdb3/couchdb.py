import json
import urllib.request


_ZABBIX_STATS_ROUTE = "/_node/_local/_stats"


def get_stats(host="localhost", port=5984, user="admin", password=None, proto="http"):  # noqa: E501
    if not password:
        raise Exception("The password parameter is mandatory")

    url = urllib.request.urlunparse((
        proto, "%s:%i" % (host, port), _ZABBIX_STATS_ROUTE, None, None, None))

    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(
            realm="server",
            uri=url,
            user=user,
            passwd=password)

    opener = urllib.request.build_opener(auth_handler)

    urllib.request.install_opener(opener)

    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))
