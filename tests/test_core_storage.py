"""Unit tests for core_storage — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_storage import CoreStorage


def _make_instance():
    """Create a CoreStorage instance with mocked auth/session."""
    with patch('synology_api.core_storage.base_api.BaseApi.__init__', return_value=None):
        instance = CoreStorage.__new__(CoreStorage)

    api_list = {
        'SYNO.Core.Quota': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.RecycleBin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.RecycleBin.User': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Storage.Disk': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Storage.Disk.FWUpgrade': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Storage.Pool': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Storage.Volume': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Storage.iSCSILUN': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreStorage(unittest.TestCase):
    """Tests for CoreStorage methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_iscsi_lun_get(self):
        self.instance.iscsi_lun_get(lun_id='test')
        self.instance.request_data.assert_called_once()

    def test_iscsi_lun_list(self):
        self.instance.iscsi_lun_list()
        self.instance.request_data.assert_called_once()

    def test_iscsi_lun_set(self):
        self.instance.iscsi_lun_set(
            lun_id='test', name='test', description='test')
        self.instance.request_data.assert_called_once()

    def test_quota_get(self):
        self.instance.quota_get(volume_path='test')
        self.instance.request_data.assert_called_once()

    def test_quota_list(self):
        self.instance.quota_list()
        self.instance.request_data.assert_called_once()

    def test_quota_set(self):
        self.instance.quota_set(
            volume_path='test', enabled=True, quota_mb='test')
        self.instance.request_data.assert_called_once()

    def test_recycle_bin_clean(self):
        self.instance.recycle_bin_clean(share_name='test')
        self.instance.request_data.assert_called_once()

    def test_recycle_bin_get(self):
        self.instance.recycle_bin_get()
        self.instance.request_data.assert_called_once()

    def test_recycle_bin_set(self):
        self.instance.recycle_bin_set(enabled=True, retention_days='test')
        self.instance.request_data.assert_called_once()

    def test_recycle_bin_user_get(self):
        self.instance.recycle_bin_user_get(user='test')
        self.instance.request_data.assert_called_once()

    def test_recycle_bin_user_set(self):
        self.instance.recycle_bin_user_set(user='test', enabled=True)
        self.instance.request_data.assert_called_once()

    def test_storage_disk_fw_upgrade_get(self):
        self.instance.storage_disk_fw_upgrade_get()
        self.instance.request_data.assert_called_once()

    def test_storage_disk_fw_upgrade_start(self):
        self.instance.storage_disk_fw_upgrade_start(disk_id='test')
        self.instance.request_data.assert_called_once()

    def test_storage_disk_get(self):
        self.instance.storage_disk_get(disk_id='test')
        self.instance.request_data.assert_called_once()

    def test_storage_disk_list(self):
        self.instance.storage_disk_list()
        self.instance.request_data.assert_called_once()

    def test_storage_pool_get(self):
        self.instance.storage_pool_get(pool_id='test')
        self.instance.request_data.assert_called_once()

    def test_storage_pool_list(self):
        self.instance.storage_pool_list()
        self.instance.request_data.assert_called_once()

    def test_storage_pool_set(self):
        self.instance.storage_pool_set(pool_id='test', description='test')
        self.instance.request_data.assert_called_once()

    def test_storage_volume_get(self):
        self.instance.storage_volume_get(volume_path='test')
        self.instance.request_data.assert_called_once()

    def test_storage_volume_list(self):
        self.instance.storage_volume_list()
        self.instance.request_data.assert_called_once()

    def test_storage_volume_set(self):
        self.instance.storage_volume_set(
            volume_path='test', description='test')
        self.instance.request_data.assert_called_once()


class TestCoreStorageCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreStorage)
        required = {
            'SYNO.Core.Quota',
            'SYNO.Core.RecycleBin',
            'SYNO.Core.RecycleBin.User',
            'SYNO.Core.Storage.Disk',
            'SYNO.Core.Storage.Disk.FWUpgrade',
            'SYNO.Core.Storage.Pool',
            'SYNO.Core.Storage.Volume',
            'SYNO.Core.Storage.iSCSILUN'
        }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreStorage)
                  if not m.startswith('_') and callable(getattr(CoreStorage, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 21,
                                f"Expected 21+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
