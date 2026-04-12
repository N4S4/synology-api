"""Unit tests for core_upgrade — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_upgrade import CoreUpgrade


def _make_instance():
    """Create a CoreUpgrade instance with mocked auth/session."""
    with patch('synology_api.core_upgrade.base_api.BaseApi.__init__', return_value=None):
        instance = CoreUpgrade.__new__(CoreUpgrade)

    api_list = {
        'SYNO.Core.Upgrade.AutoUpgrade.Security': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Cluster.Patch': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Cluster.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Cluster.Server.Download': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Group': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Group.Download': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Group.Setting': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.GroupInstall': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.GroupInstall.Network': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.JuniorModeData': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.Patch': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.PreCheck': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Upgrade.RemoteAction': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreUpgrade(unittest.TestCase):
    """Tests for CoreUpgrade methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_auto_upgrade_security_get(self):
        self.instance.auto_upgrade_security_get()
        self.instance.request_data.assert_called_once()

    def test_auto_upgrade_security_set(self):
        self.instance.auto_upgrade_security_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_cluster_patch_get(self):
        self.instance.cluster_patch_get()
        self.instance.request_data.assert_called_once()

    def test_cluster_patch_list(self):
        self.instance.cluster_patch_list()
        self.instance.request_data.assert_called_once()

    def test_cluster_server_download_get(self):
        self.instance.cluster_server_download_get()
        self.instance.request_data.assert_called_once()

    def test_cluster_server_download_start(self):
        self.instance.cluster_server_download_start()
        self.instance.request_data.assert_called_once()

    def test_cluster_server_get(self):
        self.instance.cluster_server_get()
        self.instance.request_data.assert_called_once()

    def test_cluster_server_list(self):
        self.instance.cluster_server_list()
        self.instance.request_data.assert_called_once()

    def test_group_install_get(self):
        self.instance.group_install_get()
        self.instance.request_data.assert_called_once()

    def test_group_install_network_get(self):
        self.instance.group_install_network_get()
        self.instance.request_data.assert_called_once()

    def test_group_install_network_set(self):
        self.instance.group_install_network_set()
        self.instance.request_data.assert_called_once()

    def test_group_install_start(self):
        self.instance.group_install_start()
        self.instance.request_data.assert_called_once()

    def test_junior_mode_data_get(self):
        self.instance.junior_mode_data_get()
        self.instance.request_data.assert_called_once()

    def test_junior_mode_data_set(self):
        self.instance.junior_mode_data_set()
        self.instance.request_data.assert_called_once()

    def test_remote_action_get(self):
        self.instance.remote_action_get()
        self.instance.request_data.assert_called_once()

    def test_remote_action_set(self):
        self.instance.remote_action_set(action='test')
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_download_get(self):
        self.instance.upgrade_group_download_get()
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_download_start(self):
        self.instance.upgrade_group_download_start()
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_get(self):
        self.instance.upgrade_group_get()
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_list(self):
        self.instance.upgrade_group_list()
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_setting_get(self):
        self.instance.upgrade_group_setting_get()
        self.instance.request_data.assert_called_once()

    def test_upgrade_group_setting_set(self):
        self.instance.upgrade_group_setting_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_upgrade_patch_get(self):
        self.instance.upgrade_patch_get()
        self.instance.request_data.assert_called_once()

    def test_upgrade_patch_list(self):
        self.instance.upgrade_patch_list()
        self.instance.request_data.assert_called_once()

    def test_upgrade_precheck_get(self):
        self.instance.upgrade_precheck_get()
        self.instance.request_data.assert_called_once()

    def test_upgrade_precheck_start(self):
        self.instance.upgrade_precheck_start()
        self.instance.request_data.assert_called_once()


class TestCoreUpgradeCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreUpgrade)
        required = {
        'SYNO.Core.Upgrade.AutoUpgrade.Security',
        'SYNO.Core.Upgrade.Cluster.Patch',
        'SYNO.Core.Upgrade.Cluster.Server',
        'SYNO.Core.Upgrade.Cluster.Server.Download',
        'SYNO.Core.Upgrade.Group',
        'SYNO.Core.Upgrade.Group.Download',
        'SYNO.Core.Upgrade.Group.Setting',
        'SYNO.Core.Upgrade.GroupInstall',
        'SYNO.Core.Upgrade.GroupInstall.Network',
        'SYNO.Core.Upgrade.JuniorModeData',
        'SYNO.Core.Upgrade.Patch',
        'SYNO.Core.Upgrade.PreCheck',
        'SYNO.Core.Upgrade.RemoteAction'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreUpgrade)
                  if not m.startswith('_') and callable(getattr(CoreUpgrade, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 26,
                                f"Expected 26+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
