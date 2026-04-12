"""Unit tests for core_network — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_network import CoreNetwork


def _make_instance():
    """Create a CoreNetwork instance with mocked auth/session."""
    with patch('synology_api.core_network.base_api.BaseApi.__init__', return_value=None):
        instance = CoreNetwork.__new__(CoreNetwork)

    api_list = {
        'SYNO.Core.Network.Authentication': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Authentication.Cert': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Ethernet.External': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6.Router': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.IPv6.Router.Prefix': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.MACClone': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.OVS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.PPPoE.Relay': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.Router.Static.Route': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.TrafficControl.RouterRules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.TrafficControl.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.UPnPServer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Network.WOL': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreNetwork(unittest.TestCase):
    """Tests for CoreNetwork methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_ethernet_external_get(self):
        self.instance.ethernet_external_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_get(self):
        self.instance.ipv6_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_get(self):
        self.instance.ipv6_router_get()
        self.instance.request_data.assert_called_once()

    def test_ipv6_router_prefix_get(self):
        self.instance.ipv6_router_prefix_get()
        self.instance.request_data.assert_called_once()

    def test_mac_clone_get(self):
        self.instance.mac_clone_get()
        self.instance.request_data.assert_called_once()

    def test_network_auth_cert_delete(self):
        self.instance.network_auth_cert_delete()
        self.instance.request_data.assert_called_once()

    def test_network_auth_cert_get(self):
        self.instance.network_auth_cert_get()
        self.instance.request_data.assert_called_once()

    def test_network_auth_get(self):
        self.instance.network_auth_get()
        self.instance.request_data.assert_called_once()

    def test_ovs_get(self):
        self.instance.ovs_get()
        self.instance.request_data.assert_called_once()

    def test_ovs_set(self):
        self.instance.ovs_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_pppoe_relay_get(self):
        self.instance.pppoe_relay_get()
        self.instance.request_data.assert_called_once()

    def test_static_route_delete(self):
        self.instance.static_route_delete(route_id='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_get(self):
        self.instance.static_route_get(route_id='test')
        self.instance.request_data.assert_called_once()

    def test_static_route_list(self):
        self.instance.static_route_list()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_router_rules_get(self):
        self.instance.traffic_control_router_rules_get()
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_delete(self):
        self.instance.traffic_control_rules_delete(rule_id='test')
        self.instance.request_data.assert_called_once()

    def test_traffic_control_rules_get(self):
        self.instance.traffic_control_rules_get()
        self.instance.request_data.assert_called_once()

    def test_upnp_server_get(self):
        self.instance.upnp_server_get()
        self.instance.request_data.assert_called_once()

    def test_wol_get(self):
        self.instance.wol_get()
        self.instance.request_data.assert_called_once()

    def test_wol_wake(self):
        self.instance.wol_wake(mac='00:11:22:33:44:55')
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
