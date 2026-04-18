"""Unit tests for core_security — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_security import CoreSecurity


def _make_instance():
    """Create a CoreSecurity instance with mocked auth/session."""
    with patch('synology_api.core_security.base_api.BaseApi.__init__', return_value=None):
        instance = CoreSecurity.__new__(CoreSecurity)

    api_list = {
        'SYNO.Core.Security.AutoBlock.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM.Embed': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DSM.Proxy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.DoS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Adapter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Geoip': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Profile.Apply': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Rules': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Security.Firewall.Rules.Serv': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreSecurity(unittest.TestCase):
    """Tests for CoreSecurity methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_autoblock_rules_delete(self):
        self.instance.autoblock_rules_delete(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_get(self):
        self.instance.autoblock_rules_get()
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_list(self):
        self.instance.autoblock_rules_list()
        self.instance.request_data.assert_called_once()

    def test_autoblock_rules_set(self):
        self.instance.autoblock_rules_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_firewall_adapter_get(self):
        self.instance.firewall_adapter_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_adapter_list(self):
        self.instance.firewall_adapter_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_conf_get(self):
        self.instance.firewall_conf_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_conf_set(self):
        self.instance.firewall_conf_set()
        self.instance.request_data.assert_called_once()

    def test_firewall_geoip_get(self):
        self.instance.firewall_geoip_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_geoip_set(self):
        self.instance.firewall_geoip_set()
        self.instance.request_data.assert_called_once()

    def test_firewall_get(self):
        self.instance.firewall_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_profile_apply(self):
        self.instance.firewall_profile_apply(profile_name='test')
        self.instance.request_data.assert_called_once()

    def test_firewall_profile_apply_status(self):
        self.instance.firewall_profile_apply_status()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_delete(self):
        self.instance.firewall_rules_delete(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_get(self):
        self.instance.firewall_rules_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_list(self):
        self.instance.firewall_rules_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_serv_get(self):
        self.instance.firewall_rules_serv_get()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_serv_list(self):
        self.instance.firewall_rules_serv_list()
        self.instance.request_data.assert_called_once()

    def test_firewall_rules_set(self):
        self.instance.firewall_rules_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_firewall_set(self):
        self.instance.firewall_set()
        self.instance.request_data.assert_called_once()

    def test_security_dos_get(self):
        self.instance.security_dos_get()
        self.instance.request_data.assert_called_once()

    def test_security_dos_set(self):
        self.instance.security_dos_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_embed_get(self):
        self.instance.security_dsm_embed_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_embed_set(self):
        self.instance.security_dsm_embed_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_get(self):
        self.instance.security_dsm_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_proxy_get(self):
        self.instance.security_dsm_proxy_get()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_proxy_set(self):
        self.instance.security_dsm_proxy_set()
        self.instance.request_data.assert_called_once()

    def test_security_dsm_set(self):
        self.instance.security_dsm_set()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
