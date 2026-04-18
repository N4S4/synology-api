"""Unit tests for CoreExternalDevice request construction."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_external_device import CoreExternalDevice


API_LIST = {
    'SYNO.Core.ExternalDevice.Bluetooth': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Core.ExternalDevice.Bluetooth.Device': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Core.ExternalDevice.Bluetooth.Settings': {'path': 'entry.cgi', 'maxVersion': 3},
    'SYNO.Core.ExternalDevice.DefaultPermission': {'path': 'entry.cgi', 'maxVersion': 4},
    'SYNO.Core.ExternalDevice.Printer': {'path': 'entry.cgi', 'maxVersion': 5},
    'SYNO.Core.ExternalDevice.Printer.Driver': {'path': 'entry.cgi', 'maxVersion': 6},
    'SYNO.Core.ExternalDevice.Printer.Network': {'path': 'entry.cgi', 'maxVersion': 7},
    'SYNO.Core.ExternalDevice.Printer.Network.Host': {'path': 'entry.cgi', 'maxVersion': 8},
    'SYNO.Core.ExternalDevice.Printer.OAuth': {'path': 'entry.cgi', 'maxVersion': 9},
    'SYNO.Core.ExternalDevice.Printer.USB': {'path': 'entry.cgi', 'maxVersion': 10},
    'SYNO.Core.ExternalDevice.Storage.EUnit': {'path': 'entry.cgi', 'maxVersion': 11},
    'SYNO.Core.ExternalDevice.Storage.Setting': {'path': 'entry.cgi', 'maxVersion': 12},
}


def _make_instance():
    """Create a CoreExternalDevice instance with mocked auth/session."""
    with patch('synology_api.core_external_device.base_api.BaseApi.__init__', return_value=None):
        instance = CoreExternalDevice.__new__(CoreExternalDevice)

    instance.core_list = API_LIST
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreExternalDevice(unittest.TestCase):
    """Tests for CoreExternalDevice request contracts."""

    def setUp(self):
        self.instance = _make_instance()

    def assert_request(self, api_name, params):
        self.instance.request_data.assert_called_once_with(
            api_name,
            API_LIST[api_name]['path'],
            {'version': API_LIST[api_name]['maxVersion'], **params},
        )

    def test_bluetooth_get_request_contract(self):
        self.instance.bluetooth_get()
        self.assert_request(
            'SYNO.Core.ExternalDevice.Bluetooth',
            {'method': 'get'},
        )

    def test_bluetooth_set_converts_boolean(self):
        self.instance.bluetooth_set(enable=False)
        self.assert_request(
            'SYNO.Core.ExternalDevice.Bluetooth',
            {'method': 'set', 'enable': 'false'},
        )

    def test_bluetooth_device_connect_request_contract(self):
        self.instance.bluetooth_device_connect(device_id='dev-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Bluetooth.Device',
            {'method': 'connect', 'id': 'dev-1'},
        )

    def test_bluetooth_settings_set_omits_none_values(self):
        self.instance.bluetooth_settings_set(discoverable=True)
        self.assert_request(
            'SYNO.Core.ExternalDevice.Bluetooth.Settings',
            {'method': 'set', 'discoverable': 'true'},
        )

    def test_default_permission_set_request_contract(self):
        self.instance.default_permission_set(permission='rw')
        self.assert_request(
            'SYNO.Core.ExternalDevice.DefaultPermission',
            {'method': 'set', 'permission': 'rw'},
        )

    def test_printer_list_request_contract(self):
        self.instance.printer_list()
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer',
            {'method': 'list'},
        )

    def test_printer_driver_get_request_contract(self):
        self.instance.printer_driver_get(driver_id='driver-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.Driver',
            {'method': 'get', 'id': 'driver-1'},
        )

    def test_printer_network_create_includes_optional_driver(self):
        self.instance.printer_network_create(
            host='printer.local', port=9101, driver_id='driver-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.Network',
            {
                'method': 'create',
                'host': 'printer.local',
                'port': 9101,
                'driver_id': 'driver-1',
            },
        )

    def test_printer_network_create_omits_missing_driver(self):
        self.instance.printer_network_create(host='printer.local')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.Network',
            {'method': 'create', 'host': 'printer.local', 'port': 9100},
        )

    def test_printer_network_host_list_request_contract(self):
        self.instance.printer_network_host_list()
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.Network.Host',
            {'method': 'list'},
        )

    def test_printer_oauth_set_request_contract(self):
        self.instance.printer_oauth_set(token='token-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.OAuth',
            {'method': 'set', 'token': 'token-1'},
        )

    def test_printer_usb_release_request_contract(self):
        self.instance.printer_usb_release(printer_id='printer-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Printer.USB',
            {'method': 'release', 'id': 'printer-1'},
        )

    def test_storage_eunit_get_request_contract(self):
        self.instance.storage_eunit_get(unit_id='unit-1')
        self.assert_request(
            'SYNO.Core.ExternalDevice.Storage.EUnit',
            {'method': 'get', 'id': 'unit-1'},
        )

    def test_storage_setting_set_converts_booleans_and_omits_none(self):
        self.instance.storage_setting_set(auto_mount=False)
        self.assert_request(
            'SYNO.Core.ExternalDevice.Storage.Setting',
            {'method': 'set', 'auto_mount': 'false'},
        )


class TestCoreExternalDeviceCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreExternalDevice)
        for namespace in API_LIST:
            with self.subTest(namespace=namespace):
                self.assertIn(f"'{namespace}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreExternalDevice)
                  if not m.startswith('_') and callable(getattr(CoreExternalDevice, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 28,
                                f"Expected 28+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
