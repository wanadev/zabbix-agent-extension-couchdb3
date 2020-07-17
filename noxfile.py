import nox


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "zabbix_agent_extension_couchdb3", "noxfile.py")
