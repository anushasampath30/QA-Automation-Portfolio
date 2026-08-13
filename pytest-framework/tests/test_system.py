import pytest
import re
@pytest.mark.smoke
def test_system_connected(system_connection):
    assert system_connection.connected is True
@pytest.mark.regression
def test_system_version(system_connection):
    assert system_connection.get_version() == "25.8.1"
@pytest.mark.smoke
def test_system_status(system_connection):
    assert system_connection.get_status() == "ACTIVE"
@pytest.mark.regression

def test_system_format(system_connection):
    version = system_connection.get_version()
    print(version)
    assert re.fullmatch("\d+\.\d+\.\d+",version)
