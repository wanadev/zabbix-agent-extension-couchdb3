import datetime


_VALUE_TYPES = {
    float: 0,
    int: 3,
}


_TPL_HEAD = """<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>4.0</version>
    <date>%s</date>
    <groups>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template CouchDB 3</template>
            <name>Template CouchDB 3</name>
            <description/>
            <groups>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>CouchDB3</name>
                </application>
            </applications>
            <items>
"""

_TPL_ITEM = """
                <item>
                    <name>CouchDB 3: %s</name>
                    <type>2</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>%s</key>
                    <delay>0</delay>
                    <history>90d</history>
                    <trends>365d</trends>
                    <status>0</status>
                    <value_type>%i</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>%s</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>CouchDB3</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
"""

_TPL_TAIL = """
                <item>
                    <name>CouchDB 3 stats</name>
                    <type>0</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>couchdb3.stats[{$COUCHDB_HOST},{$COUCHDB_PORT},{$COUCHDB_USER},{$COUCHDB_PASSWORD},{$COUCHDB_PROTO}]</key>
                    <delay>30s</delay>
                    <history>90d</history>
                    <trends>0</trends>
                    <status>0</status>
                    <value_type>4</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>CouchDB3</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
            </items>
            <discovery_rules/>
            <httptests/>
            <macros>
                <macro>
                    <macro>{$COUCHDB_HOST}</macro>
                    <value>localhost</value>
                </macro>
                <macro>
                    <macro>{$COUCHDB_PASSWORD}</macro>
                    <value/>
                </macro>
                <macro>
                    <macro>{$COUCHDB_PORT}</macro>
                    <value>5984</value>
                </macro>
                <macro>
                    <macro>{$COUCHDB_PROTO}</macro>
                    <value>http</value>
                </macro>
                <macro>
                    <macro>{$COUCHDB_USER}</macro>
                    <value>admin</value>
                </macro>
            </macros>
            <templates/>
            <screens/>
        </template>
    </templates>
</zabbix_export>
"""


def _get_current_date():
    date = datetime.datetime.utcnow().isoformat()
    date = "%sZ" % date.split(".")[0]
    return date


def generate_zabbix4_template(stats):
    date = _get_current_date()

    tpl = _TPL_HEAD % date

    for key, value, desc in stats:
        value_type = _VALUE_TYPES[type(value)]
        tpl += _TPL_ITEM % (key, key, value_type, desc)

    tpl += _TPL_TAIL

    return tpl
