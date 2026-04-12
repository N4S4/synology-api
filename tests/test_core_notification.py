"""Unit tests for core_notification — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_notification import CoreNotification


def _make_instance():
    """Create a CoreNotification instance with mocked auth/session."""
    with patch('synology_api.core_notification.base_api.BaseApi.__init__', return_value=None):
        instance = CoreNotification.__new__(CoreNotification)

    api_list = {
        'SYNO.Core.Notification.Advance.CustomizedData': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Advance.FilterSettings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Advance.FilterSettings.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Advance.FilterSettings.Template': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Advance.Variables': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Advance.WarningPercentage': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.CMS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.CMS.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Line': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Mail': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Mail.Auth': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Mail.Oauth': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Mail.Profile.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Push': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Push.AuthToken': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Push.Mobile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Push.Webhook.Provider': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.SMS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.SMS.Provider': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Notification.Sysnotify': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(return_value={'success': True, 'data': {}})
    return instance


class TestCoreNotification(unittest.TestCase):
    """Tests for CoreNotification methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_notification_advance_customized_data_get(self):
        self.instance.notification_advance_customized_data_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_customized_data_set(self):
        self.instance.notification_advance_customized_data_set(data='test')
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_profile_get(self):
        self.instance.notification_advance_filter_profile_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_profile_set(self):
        self.instance.notification_advance_filter_profile_set(profile={"test": True})
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_settings_get(self):
        self.instance.notification_advance_filter_settings_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_settings_set(self):
        self.instance.notification_advance_filter_settings_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_template_get(self):
        self.instance.notification_advance_filter_template_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_filter_template_set(self):
        self.instance.notification_advance_filter_template_set(template='test')
        self.instance.request_data.assert_called_once()

    def test_notification_advance_variables_get(self):
        self.instance.notification_advance_variables_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_variables_set(self):
        self.instance.notification_advance_variables_set(variables='test')
        self.instance.request_data.assert_called_once()

    def test_notification_advance_warning_percentage_get(self):
        self.instance.notification_advance_warning_percentage_get()
        self.instance.request_data.assert_called_once()

    def test_notification_advance_warning_percentage_set(self):
        self.instance.notification_advance_warning_percentage_set(percentage='test')
        self.instance.request_data.assert_called_once()

    def test_notification_cms_conf_get(self):
        self.instance.notification_cms_conf_get()
        self.instance.request_data.assert_called_once()

    def test_notification_cms_conf_set(self):
        self.instance.notification_cms_conf_set(conf='test')
        self.instance.request_data.assert_called_once()

    def test_notification_cms_get(self):
        self.instance.notification_cms_get()
        self.instance.request_data.assert_called_once()

    def test_notification_cms_set(self):
        self.instance.notification_cms_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_notification_line_get(self):
        self.instance.notification_line_get()
        self.instance.request_data.assert_called_once()

    def test_notification_line_set(self):
        self.instance.notification_line_set(token='test', enable='test')
        self.instance.request_data.assert_called_once()

    def test_notification_mail_auth_get(self):
        self.instance.notification_mail_auth_get()
        self.instance.request_data.assert_called_once()

    def test_notification_mail_auth_set(self):
        self.instance.notification_mail_auth_set(auth_type='test', username='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_notification_mail_get(self):
        self.instance.notification_mail_get()
        self.instance.request_data.assert_called_once()

    def test_notification_mail_oauth_get(self):
        self.instance.notification_mail_oauth_get()
        self.instance.request_data.assert_called_once()

    def test_notification_mail_oauth_set(self):
        self.instance.notification_mail_oauth_set(client_id='test', client_secret='test', refresh_token='test')
        self.instance.request_data.assert_called_once()

    def test_notification_mail_profile_conf_get(self):
        self.instance.notification_mail_profile_conf_get()
        self.instance.request_data.assert_called_once()

    def test_notification_mail_profile_conf_set(self):
        self.instance.notification_mail_profile_conf_set(profile={"test": True})
        self.instance.request_data.assert_called_once()

    def test_notification_mail_set(self):
        self.instance.notification_mail_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_notification_push_auth_token_get(self):
        self.instance.notification_push_auth_token_get()
        self.instance.request_data.assert_called_once()

    def test_notification_push_auth_token_set(self):
        self.instance.notification_push_auth_token_set(token='test')
        self.instance.request_data.assert_called_once()

    def test_notification_push_get(self):
        self.instance.notification_push_get()
        self.instance.request_data.assert_called_once()

    def test_notification_push_mobile_get(self):
        self.instance.notification_push_mobile_get()
        self.instance.request_data.assert_called_once()

    def test_notification_push_mobile_set(self):
        self.instance.notification_push_mobile_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_notification_push_set(self):
        self.instance.notification_push_set(enable='test')
        self.instance.request_data.assert_called_once()

    def test_notification_push_webhook_provider_get(self):
        self.instance.notification_push_webhook_provider_get()
        self.instance.request_data.assert_called_once()

    def test_notification_push_webhook_provider_set(self):
        self.instance.notification_push_webhook_provider_set(provider='test', url='test', token='test')
        self.instance.request_data.assert_called_once()

    def test_notification_sms_get(self):
        self.instance.notification_sms_get()
        self.instance.request_data.assert_called_once()

    def test_notification_sms_provider_get(self):
        self.instance.notification_sms_provider_get()
        self.instance.request_data.assert_called_once()

    def test_notification_sms_provider_set(self):
        self.instance.notification_sms_provider_set(provider='test', api_key='test')
        self.instance.request_data.assert_called_once()

    def test_notification_sms_set(self):
        self.instance.notification_sms_set(settings='test')
        self.instance.request_data.assert_called_once()

    def test_notification_sysnotify_get(self):
        self.instance.notification_sysnotify_get()
        self.instance.request_data.assert_called_once()

    def test_notification_sysnotify_set(self):
        self.instance.notification_sysnotify_set(settings='test')
        self.instance.request_data.assert_called_once()


class TestCoreNotificationCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreNotification)
        required = {
        'SYNO.Core.Notification.Advance.CustomizedData',
        'SYNO.Core.Notification.Advance.FilterSettings',
        'SYNO.Core.Notification.Advance.FilterSettings.Profile',
        'SYNO.Core.Notification.Advance.FilterSettings.Template',
        'SYNO.Core.Notification.Advance.Variables',
        'SYNO.Core.Notification.Advance.WarningPercentage',
        'SYNO.Core.Notification.CMS',
        'SYNO.Core.Notification.CMS.Conf',
        'SYNO.Core.Notification.Line',
        'SYNO.Core.Notification.Mail',
        'SYNO.Core.Notification.Mail.Auth',
        'SYNO.Core.Notification.Mail.Oauth',
        'SYNO.Core.Notification.Mail.Profile.Conf',
        'SYNO.Core.Notification.Push',
        'SYNO.Core.Notification.Push.AuthToken',
        'SYNO.Core.Notification.Push.Mobile',
        'SYNO.Core.Notification.Push.Webhook.Provider',
        'SYNO.Core.Notification.SMS',
        'SYNO.Core.Notification.SMS.Provider',
        'SYNO.Core.Notification.Sysnotify'
    }
        for ns in required:
            with self.subTest(namespace=ns):
                self.assertIn(f"'{ns}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreNotification)
                  if not m.startswith('_') and callable(getattr(CoreNotification, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 40,
                                f"Expected 40+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
