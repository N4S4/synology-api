"""Unit tests for core_external_device — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_external_device import CoreExternalDevice


def _make_instance():
    """Create a CoreExternalDevice instance with mocked auth/session."""
    with patch('synology_api.core_external_device.base_api.BaseApi.__init__', return_value=None):
        instance = CoreExternalDevice.__new__(CoreExternalDevice)

    api_list = {
        'SYNO.Core.ExternalDevice.Bluetooth': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Bluetooth.Device': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Bluetooth.Settings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.DefaultPermission': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer.Driver': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer.Network': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer.Network.Host': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer.OAuth': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Printer.USB': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Storage.EUnit': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ExternalDevice.Storage.Setting': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreExternalDevice(unittest.TestCase):
    """Tests for CoreExternalDevice methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_bluetooth_device_connect(self):
        self.instance.bluetooth_device_connect(device_id='test')
        self.instance.request_data.assert_called_once()

    def test_bluetooth_device_disconnect(self):
        self.instance.bluetooth_device_disconnect(device_id='test')
        self.instance.request_data.assert_called_once()

    def test_bluetooth_device_get(self):
        self.instance.bluetooth_device_get(device_id='test')
        self.instance.request_data.assert_called_once()

    def test_bluetooth_device_list(self):
        self.instance.bluetooth_device_list()
        self.instance.request_data.assert_called_once()

    def test_bluetooth_get(self):
        self.instance.bluetooth_get()
        self.instance.request_data.assert_called_once()

    def test_bluetooth_set(self):
        self.instance.bluetooth_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_bluetooth_settings_get(self):
        self.instance.bluetooth_settings_get()
        self.instance.request_data.assert_called_once()

    def test_bluetooth_settings_set(self):
        self.instance.bluetooth_settings_set(discoverable='test', name='test')
        self.instance.request_data.assert_called_once()

    def test_default_permission_get(self):
        self.instance.default_permission_get()
        self.instance.request_data.assert_called_once()

    def test_default_permission_set(self):
        self.instance.default_permission_set(permission='test')
        self.instance.request_data.assert_called_once()

    def test_printer_clean(self):
        self.instance.printer_clean(printer_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_driver_get(self):
        self.instance.printer_driver_get(driver_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_driver_list(self):
        self.instance.printer_driver_list()
        self.instance.request_data.assert_called_once()

    def test_printer_get(self):
        self.instance.printer_get(printer_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_list(self):
        self.instance.printer_list()
        self.instance.request_data.assert_called_once()

    def test_printer_network_create(self):
        self.instance.printer_network_create(
            host='test', port=1, driver_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_network_delete(self):
        self.instance.printer_network_delete(printer_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_network_host_list(self):
        self.instance.printer_network_host_list()
        self.instance.request_data.assert_called_once()

    def test_printer_network_list(self):
        self.instance.printer_network_list()
        self.instance.request_data.assert_called_once()

    def test_printer_oauth_get(self):
        self.instance.printer_oauth_get()
        self.instance.request_data.assert_called_once()

    def test_printer_oauth_set(self):
        self.instance.printer_oauth_set(token='test')
        self.instance.request_data.assert_called_once()

    def test_printer_usb_get(self):
        self.instance.printer_usb_get(printer_id='test')
        self.instance.request_data.assert_called_once()

    def test_printer_usb_list(self):
        self.instance.printer_usb_list()
        self.instance.request_data.assert_called_once()

    def test_printer_usb_release(self):
        self.instance.printer_usb_release(printer_id='test')
        self.instance.request_data.assert_called_once()

    def test_storage_eunit_get(self):
        self.instance.storage_eunit_get(unit_id='test')
        self.instance.request_data.assert_called_once()

    def test_storage_eunit_list(self):
        self.instance.storage_eunit_list()
        self.instance.request_data.assert_called_once()

    def test_storage_setting_get(self):
        self.instance.storage_setting_get()
        self.instance.request_data.assert_called_once()

    def test_storage_setting_set(self):
        self.instance.storage_setting_set(
            auto_format='test', auto_mount='test')
        self.instance.request_data.assert_called_once()


class TestCoreExternalDeviceCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreExternalDevice)
        required = {
            'SYNO.Core.ExternalDevice.Bluetooth',
            'SYNO.Core.ExternalDevice.Bluetooth.Device',
            'SYNO.Core.ExternalDevice.Bluetooth.Settings',
            'SYNO.Core.ExternalDevice.DefaultPermission',
            'SYNO.Core.ExternalDevice.Printer',
            'SYNO.Core.ExternalDevice.Printer.Driver',
            'SYNO.Core.ExternalDevice.Printer.Network',
            'SYNO.Core.ExternalDevice.Printer.Network.Host',
            'SYNO.Core.ExternalDevice.Printer.OAuth',
            'SYNO.Core.ExternalDevice.Printer.USB',
            'SYNO.Core.ExternalDevice.Storage.EUnit',
            'SYNO.Core.ExternalDevice.Storage.Setting'
        }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreExternalDevice)
                  if not m.startswith('_') and callable(getattr(CoreExternalDevice, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 28,
                                f"Expected 28+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
