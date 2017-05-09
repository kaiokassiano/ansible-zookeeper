import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("name, version", [
    ('default-jre-headless', '2:1.8'),
])
def test_packages(Package, name, version):
    pkg = Package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_monasca_agent_installed(File):
    f = File('/opt/zookeeper/bin/zkCli.sh')

    assert f.exists


@pytest.mark.parametrize('service_name', [
    ('zookeeper'),
])
def test_monasca_agent_service_enabled(Service, service_name):
    s = Service(service_name)

    assert s.is_enabled
