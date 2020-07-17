Zabbix Agent extension to monitor CouchDB 3
===========================================

This is an extension for the Zabbix Agent to enable it to monitor CouchDB
3 servers.


Requirements
------------

* Python 3.5+
* `py-zabbix <https://github.com/adubkov/py-zabbix>`_


Installation (agent side)
-------------------------

You first have to install the extension on the server that runs the Zabbix
Agent.


From PIPY
~~~~~~~~~

Run the following command (as root):

    pip3 install zabbix-agent-extension-couchdb3

Then copy the ``zabbix-agent-extension-couchdb3.conf`` file from this
repository to the ``/etc/zabbix/zabbix_agentd.conf.d/`` folder on the server.

And finally, restart the Zabbix Agent (with systemd: ``systemctl restart
zabbix-agent``).


Installation (zabbix side)
--------------------------

TODO (import template)


CLI Usage
---------

This extension also provides a CLI to simplify debugging.

::

    usage: zabbix-agent-extension-couchdb3 [-h] [--host HOST] [--port PORT] [--user USER]
                        --password PASSWORD [--proto PROTO] [--show-json] [--show-stats]

    optional arguments:
      -h, --help           show this help message and exit
      --host HOST          The CouchDB server host (default: localhost)
      --port PORT          The CouchDB server port (default: 5984)
      --user USER          The username to use for the connexion (default: admin)
      --password PASSWORD  The password to use for the connexion (mandatory)
      --proto PROTO        The protocol to use (default: http)
      --show-json          Display the raw JSON stats from CouchDB and exit (no stats will be
                           sent to Zabbix)
      --show-stats         Display the available stats with their values and description and exit
                           (no stats will be sent to Zabbix)

Example: dumping CouchDB stats as JSON::

    zabbix-agent-extension-couchdb3 --password=XXXXX --show-json

Example: displaying CouchDB stats in a more friendly format::

    zabbix-agent-extension-couchdb3 --password=XXXXX --show-stats


Changelog
---------

* **v0.1.0:** Initial release
