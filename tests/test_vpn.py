"""Unit tests for VPN API request construction."""

import unittest
from unittest.mock import MagicMock, patch

from synology_api.vpn import VPN


def _make_instance():
    """Create a VPN instance with mocked auth/session."""
    with patch('synology_api.vpn.base_api.BaseApi.__init__', return_value=None):
        instance = VPN.__new__(VPN)

    instance.core_list = {
        'SYNO.Core.Network.VPN': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPN.CA': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPNWithConf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.VPN.OpenVPNWithConf.Certs': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestVPNCoreNetwork(unittest.TestCase):
    """Tests for DSM Core Network VPN methods on the VPN wrapper."""

    def setUp(self):
        self.instance = _make_instance()

    def test_core_network_vpn_get(self):
        self.instance.core_network_vpn_get()

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN',
            'entry.cgi',
            {'version': 1, 'method': 'get'},
        )

    def test_core_network_vpn_set(self):
        self.instance.core_network_vpn_set(reconnect=False, interval=45)

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN',
            'entry.cgi',
            {
                'version': 1,
                'method': 'set',
                'reconnect': 'false',
                'interval': 45,
            },
        )

    def test_core_network_openvpn_ca_get(self):
        self.instance.core_network_openvpn_ca_get()

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPN.CA',
            'entry.cgi',
            {'version': 1, 'method': 'get'},
        )

    def test_core_network_openvpn_ca_set(self):
        self.instance.core_network_openvpn_ca_set(ca_path='/tmp/ca.pem')

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPN.CA',
            'entry.cgi',
            {'version': 1, 'method': 'set', 'ca_path': '/tmp/ca.pem'},
        )

    def test_core_network_openvpn_with_conf_get(self):
        self.instance.core_network_openvpn_with_conf_get()

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPNWithConf',
            'entry.cgi',
            {'version': 1, 'method': 'get'},
        )

    def test_core_network_openvpn_with_conf_set(self):
        self.instance.core_network_openvpn_with_conf_set(
            conf_path='/tmp/client.ovpn',
            username='alice',
            password='secret',
        )

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPNWithConf',
            'entry.cgi',
            {
                'version': 1,
                'method': 'set',
                'conf_path': '/tmp/client.ovpn',
                'username': 'alice',
                'password': 'secret',
            },
        )

    def test_core_network_openvpn_with_conf_certs_get(self):
        self.instance.core_network_openvpn_with_conf_certs_get()

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPNWithConf.Certs',
            'entry.cgi',
            {'version': 1, 'method': 'get'},
        )

    def test_core_network_openvpn_with_conf_certs_set(self):
        self.instance.core_network_openvpn_with_conf_certs_set(
            cert_path='/tmp/client.pem',
            key_path='/tmp/client.key',
            ca_path='/tmp/ca.pem',
        )

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.Network.VPN.OpenVPNWithConf.Certs',
            'entry.cgi',
            {
                'version': 1,
                'method': 'set',
                'cert_path': '/tmp/client.pem',
                'key_path': '/tmp/client.key',
                'ca_path': '/tmp/ca.pem',
            },
        )


if __name__ == '__main__':
    unittest.main()
