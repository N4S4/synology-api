"""Unit tests for CoreNetwork request construction."""

import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_network import CoreNetwork


API_LIST = {
    'SYNO.Core.Network.Authentication': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Core.Network.Authentication.Cert': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Core.Network.Ethernet.External': {'path': 'entry.cgi', 'maxVersion': 3},
    'SYNO.Core.Network.IPv6': {'path': 'entry.cgi', 'maxVersion': 4},
    'SYNO.Core.Network.IPv6.Router': {'path': 'entry.cgi', 'maxVersion': 5},
    'SYNO.Core.Network.IPv6.Router.Prefix': {'path': 'entry.cgi', 'maxVersion': 6},
    'SYNO.Core.Network.MACClone': {'path': 'entry.cgi', 'maxVersion': 7},
    'SYNO.Core.Network.OVS': {'path': 'entry.cgi', 'maxVersion': 8},
    'SYNO.Core.Network.PPPoE.Relay': {'path': 'entry.cgi', 'maxVersion': 9},
    'SYNO.Core.Network.Router.Static.Route': {'path': 'entry.cgi', 'maxVersion': 10},
    'SYNO.Core.Network.TrafficControl.RouterRules': {'path': 'entry.cgi', 'maxVersion': 11},
    'SYNO.Core.Network.TrafficControl.Rules': {'path': 'entry.cgi', 'maxVersion': 12},
    'SYNO.Core.Network.UPnPServer': {'path': 'entry.cgi', 'maxVersion': 13},
    'SYNO.Core.Network.WOL': {'path': 'entry.cgi', 'maxVersion': 14},
}


def _make_instance():
    """Create a CoreNetwork instance with mocked auth/session."""
    with patch('synology_api.core_network.base_api.BaseApi.__init__', return_value=None):
        instance = CoreNetwork.__new__(CoreNetwork)

    instance.core_list = API_LIST
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreNetwork(unittest.TestCase):
    """Tests for CoreNetwork request contracts."""

    def setUp(self):
        self.instance = _make_instance()

    def assert_request(self, api_name, params):
        self.instance.request_data.assert_called_once_with(
            api_name,
            API_LIST[api_name]['path'],
            {'version': API_LIST[api_name]['maxVersion'], **params},
        )

    def test_network_auth_get_request_contract(self):
        self.instance.network_auth_get()
        self.assert_request(
            'SYNO.Core.Network.Authentication',
            {'method': 'get'},
        )

    def test_network_auth_set_converts_boolean_and_includes_profile(self):
        self.instance.network_auth_set(enable=True, profile='corp-wifi')
        self.assert_request(
            'SYNO.Core.Network.Authentication',
            {'method': 'set', 'enable': 'true', 'profile': 'corp-wifi'},
        )

    def test_network_auth_cert_set_omits_none_values(self):
        self.instance.network_auth_cert_set(cert_path='/cert.pem')
        self.assert_request(
            'SYNO.Core.Network.Authentication.Cert',
            {'method': 'set', 'cert_path': '/cert.pem'},
        )

    def test_ethernet_external_get_request_contract(self):
        self.instance.ethernet_external_get()
        self.assert_request(
            'SYNO.Core.Network.Ethernet.External',
            {'method': 'get'},
        )

    def test_ipv6_set_converts_boolean_and_includes_type(self):
        self.instance.ipv6_set(enable=False, type='dhcpv6')
        self.assert_request(
            'SYNO.Core.Network.IPv6',
            {'method': 'set', 'enable': 'false', 'type': 'dhcpv6'},
        )

    def test_ipv6_router_prefix_get_request_contract(self):
        self.instance.ipv6_router_prefix_get()
        self.assert_request(
            'SYNO.Core.Network.IPv6.Router.Prefix',
            {'method': 'get'},
        )

    def test_mac_clone_get_request_contract(self):
        self.instance.mac_clone_get()
        self.assert_request(
            'SYNO.Core.Network.MACClone',
            {'method': 'get'},
        )

    def test_ovs_set_converts_boolean(self):
        self.instance.ovs_set(enable=True)
        self.assert_request(
            'SYNO.Core.Network.OVS',
            {'method': 'set', 'enable': 'true'},
        )

    def test_pppoe_relay_get_request_contract(self):
        self.instance.pppoe_relay_get()
        self.assert_request(
            'SYNO.Core.Network.PPPoE.Relay',
            {'method': 'get'},
        )

    def test_static_route_delete_request_contract(self):
        self.instance.static_route_delete(route_id='route-1')
        self.assert_request(
            'SYNO.Core.Network.Router.Static.Route',
            {'method': 'delete', 'id': 'route-1'},
        )

    def test_traffic_control_router_rules_get_request_contract(self):
        self.instance.traffic_control_router_rules_get()
        self.assert_request(
            'SYNO.Core.Network.TrafficControl.RouterRules',
            {'method': 'get'},
        )

    def test_traffic_control_rules_delete_request_contract(self):
        self.instance.traffic_control_rules_delete(rule_id='rule-1')
        self.assert_request(
            'SYNO.Core.Network.TrafficControl.Rules',
            {'method': 'delete', 'id': 'rule-1'},
        )

    def test_upnp_server_set_converts_boolean(self):
        self.instance.upnp_server_set(enable=True)
        self.assert_request(
            'SYNO.Core.Network.UPnPServer',
            {'method': 'set', 'enable': 'true'},
        )

    def test_wol_wake_includes_optional_interface(self):
        self.instance.wol_wake(mac='00:11:22:33:44:55', ifname='eth0')
        self.assert_request(
            'SYNO.Core.Network.WOL',
            {'method': 'wake', 'mac': '00:11:22:33:44:55', 'ifname': 'eth0'},
        )


if __name__ == '__main__':
    unittest.main()
