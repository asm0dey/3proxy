import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_runs(host):
    proxy = host.service("3proxy")
    assert proxy.is_running
    assert proxy.is_enabled


def test_ports_open(host):
    assert host.socket("tcp://0.0.0.0:3128").is_listening
    assert host.socket("tcp://0.0.0.0:1080").is_listening


def test_users_lines(host):
    cfg_path = ""
    if host.system_info.distribution == "ubuntu":
        cfg_path = "/etc/3proxy/3proxy.cfg"
    else:
        cfg_path = "/etc/3proxy.cfg"
    cfg = host.file(cfg_path)
    assert cfg.contains('users "asm0dey:CR:$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/' +
                        '6/" "asm0dey2:CR:$1$pL3Ho94u$2.wCxrLfacj82UMPJSy/6/"')
    assert cfg.contains("auth strong")
