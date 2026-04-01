"""Unit tests for core_system — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_system import CoreSystem


def _make_instance():
    """Create a CoreSystem instance with mocked auth/session."""
    with patch('synology_api.core_system.base_api.BaseApi.__init__', return_value=None):
        instance = CoreSystem.__new__(CoreSystem)

    api_list = {
        'SYNO.Core.Desktop.Defs': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.Initdata': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.JSUIString': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.PersonalUpdater': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.SessionData': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.Timeout': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.UIString': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Desktop.Upgrade': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.GroupSettings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Help': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.PersonalSettings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Region.Language': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Region.NTP': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Region.NTP.DateTimeFormat': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Region.NTP.Server': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.System.ResetButton': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Theme.AppPortalLogin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Theme.Desktop': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Theme.FileSharingLogin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Theme.Image': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Theme.Login': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.UISearch': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.UserSettings': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.core_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreSystem(unittest.TestCase):
    """Tests for CoreSystem methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_desktop_defs_get(self):
        self.instance.desktop_defs_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_initdata_get(self):
        self.instance.desktop_initdata_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_jsui_string_get(self):
        self.instance.desktop_jsui_string_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_personal_updater_get(self):
        self.instance.desktop_personal_updater_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_personal_updater_set(self):
        self.instance.desktop_personal_updater_set()
        self.instance.request_data.assert_called_once()

    def test_desktop_session_data_get(self):
        self.instance.desktop_session_data_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_timeout_get(self):
        self.instance.desktop_timeout_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_timeout_set(self):
        self.instance.desktop_timeout_set(timeout_minutes='test')
        self.instance.request_data.assert_called_once()

    def test_desktop_ui_string_get(self):
        self.instance.desktop_ui_string_get()
        self.instance.request_data.assert_called_once()

    def test_desktop_upgrade_get(self):
        self.instance.desktop_upgrade_get()
        self.instance.request_data.assert_called_once()

    def test_group_settings_get(self):
        self.instance.group_settings_get(group='test')
        self.instance.request_data.assert_called_once()

    def test_group_settings_set(self):
        self.instance.group_settings_set(group='test')
        self.instance.request_data.assert_called_once()

    def test_help_get(self):
        self.instance.help_get(topic='test')
        self.instance.request_data.assert_called_once()

    def test_help_list(self):
        self.instance.help_list()
        self.instance.request_data.assert_called_once()

    def test_ntp_datetime_format_get(self):
        self.instance.ntp_datetime_format_get()
        self.instance.request_data.assert_called_once()

    def test_ntp_datetime_format_set(self):
        self.instance.ntp_datetime_format_set(date_format='test', time_format='test')
        self.instance.request_data.assert_called_once()

    def test_ntp_server_get(self):
        self.instance.ntp_server_get()
        self.instance.request_data.assert_called_once()

    def test_ntp_server_set(self):
        self.instance.ntp_server_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_personal_settings_get(self):
        self.instance.personal_settings_get()
        self.instance.request_data.assert_called_once()

    def test_personal_settings_set(self):
        self.instance.personal_settings_set()
        self.instance.request_data.assert_called_once()

    def test_region_language_get(self):
        self.instance.region_language_get()
        self.instance.request_data.assert_called_once()

    def test_region_language_set(self):
        self.instance.region_language_set(language='test')
        self.instance.request_data.assert_called_once()

    def test_region_ntp_get(self):
        self.instance.region_ntp_get()
        self.instance.request_data.assert_called_once()

    def test_region_ntp_set(self):
        self.instance.region_ntp_set(enabled=True, server='test')
        self.instance.request_data.assert_called_once()

    def test_reset_button_get(self):
        self.instance.reset_button_get()
        self.instance.request_data.assert_called_once()

    def test_reset_button_set(self):
        self.instance.reset_button_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_theme_app_portal_login_get(self):
        self.instance.theme_app_portal_login_get()
        self.instance.request_data.assert_called_once()

    def test_theme_app_portal_login_set(self):
        self.instance.theme_app_portal_login_set()
        self.instance.request_data.assert_called_once()

    def test_theme_desktop_get(self):
        self.instance.theme_desktop_get()
        self.instance.request_data.assert_called_once()

    def test_theme_desktop_set(self):
        self.instance.theme_desktop_set()
        self.instance.request_data.assert_called_once()

    def test_theme_file_sharing_login_get(self):
        self.instance.theme_file_sharing_login_get()
        self.instance.request_data.assert_called_once()

    def test_theme_file_sharing_login_set(self):
        self.instance.theme_file_sharing_login_set()
        self.instance.request_data.assert_called_once()

    def test_theme_image_get(self):
        self.instance.theme_image_get()
        self.instance.request_data.assert_called_once()

    def test_theme_image_list(self):
        self.instance.theme_image_list()
        self.instance.request_data.assert_called_once()

    def test_theme_login_get(self):
        self.instance.theme_login_get()
        self.instance.request_data.assert_called_once()

    def test_theme_login_set(self):
        self.instance.theme_login_set()
        self.instance.request_data.assert_called_once()

    def test_ui_search_get(self):
        self.instance.ui_search_get(query='test')
        self.instance.request_data.assert_called_once()

    def test_ui_search_list(self):
        self.instance.ui_search_list()
        self.instance.request_data.assert_called_once()

    def test_user_settings_get(self):
        self.instance.user_settings_get(user='test')
        self.instance.request_data.assert_called_once()

    def test_user_settings_set(self):
        self.instance.user_settings_set()
        self.instance.request_data.assert_called_once()


class TestCoreSystemCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreSystem)
        required = {
        'SYNO.Core.Desktop.Defs',
        'SYNO.Core.Desktop.Initdata',
        'SYNO.Core.Desktop.JSUIString',
        'SYNO.Core.Desktop.PersonalUpdater',
        'SYNO.Core.Desktop.SessionData',
        'SYNO.Core.Desktop.Timeout',
        'SYNO.Core.Desktop.UIString',
        'SYNO.Core.Desktop.Upgrade',
        'SYNO.Core.GroupSettings',
        'SYNO.Core.Help',
        'SYNO.Core.PersonalSettings',
        'SYNO.Core.Region.Language',
        'SYNO.Core.Region.NTP',
        'SYNO.Core.Region.NTP.DateTimeFormat',
        'SYNO.Core.Region.NTP.Server',
        'SYNO.Core.System.ResetButton',
        'SYNO.Core.Theme.AppPortalLogin',
        'SYNO.Core.Theme.Desktop',
        'SYNO.Core.Theme.FileSharingLogin',
        'SYNO.Core.Theme.Image',
        'SYNO.Core.Theme.Login',
        'SYNO.Core.UISearch',
        'SYNO.Core.UserSettings'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreSystem)
                  if not m.startswith('_') and callable(getattr(CoreSystem, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 40,
                                f"Expected 40+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
