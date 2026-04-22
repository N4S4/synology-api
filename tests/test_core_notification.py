"""Unit tests for CoreNotification request construction."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_notification import CoreNotification


API_LIST = {
    'SYNO.Core.Notification.Advance.CustomizedData': {'path': 'entry.cgi', 'maxVersion': 1},
    'SYNO.Core.Notification.Advance.FilterSettings': {'path': 'entry.cgi', 'maxVersion': 2},
    'SYNO.Core.Notification.Advance.FilterSettings.Profile': {'path': 'entry.cgi', 'maxVersion': 3},
    'SYNO.Core.Notification.Advance.FilterSettings.Template': {'path': 'entry.cgi', 'maxVersion': 4},
    'SYNO.Core.Notification.Advance.Variables': {'path': 'entry.cgi', 'maxVersion': 5},
    'SYNO.Core.Notification.Advance.WarningPercentage': {'path': 'entry.cgi', 'maxVersion': 6},
    'SYNO.Core.Notification.CMS': {'path': 'entry.cgi', 'maxVersion': 7},
    'SYNO.Core.Notification.CMS.Conf': {'path': 'entry.cgi', 'maxVersion': 8},
    'SYNO.Core.Notification.Line': {'path': 'entry.cgi', 'maxVersion': 9},
    'SYNO.Core.Notification.Mail': {'path': 'entry.cgi', 'maxVersion': 10},
    'SYNO.Core.Notification.Mail.Auth': {'path': 'entry.cgi', 'maxVersion': 11},
    'SYNO.Core.Notification.Mail.Oauth': {'path': 'entry.cgi', 'maxVersion': 12},
    'SYNO.Core.Notification.Mail.Profile.Conf': {'path': 'entry.cgi', 'maxVersion': 13},
    'SYNO.Core.Notification.Push': {'path': 'entry.cgi', 'maxVersion': 14},
    'SYNO.Core.Notification.Push.AuthToken': {'path': 'entry.cgi', 'maxVersion': 15},
    'SYNO.Core.Notification.Push.Mobile': {'path': 'entry.cgi', 'maxVersion': 16},
    'SYNO.Core.Notification.Push.Webhook.Provider': {'path': 'entry.cgi', 'maxVersion': 17},
    'SYNO.Core.Notification.SMS': {'path': 'entry.cgi', 'maxVersion': 18},
    'SYNO.Core.Notification.SMS.Provider': {'path': 'entry.cgi', 'maxVersion': 19},
    'SYNO.Core.Notification.Sysnotify': {'path': 'entry.cgi', 'maxVersion': 20},
}


def _make_instance():
    """Create a CoreNotification instance with mocked auth/session."""
    with patch('synology_api.core_notification.base_api.BaseApi.__init__', return_value=None):
        instance = CoreNotification.__new__(CoreNotification)

    instance.gen_list = API_LIST
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreNotification(unittest.TestCase):
    """Tests for CoreNotification request contracts."""

    def setUp(self):
        self.instance = _make_instance()

    def assert_request(self, api_name, params):
        self.instance.request_data.assert_called_once_with(
            api_name,
            API_LIST[api_name]['path'],
            {'version': API_LIST[api_name]['maxVersion'], **params},
        )

    def test_customized_data_get_request_contract(self):
        self.instance.notification_advance_customized_data_get()
        self.assert_request(
            'SYNO.Core.Notification.Advance.CustomizedData',
            {'method': 'get'},
        )

    def test_filter_settings_set_omits_none_values(self):
        self.instance.notification_advance_filter_settings_set()
        self.assert_request(
            'SYNO.Core.Notification.Advance.FilterSettings',
            {'method': 'set'},
        )

    def test_filter_profile_set_includes_profile(self):
        self.instance.notification_advance_filter_profile_set(
            profile='profile-json')
        self.assert_request(
            'SYNO.Core.Notification.Advance.FilterSettings.Profile',
            {'method': 'set', 'profile': 'profile-json'},
        )

    def test_filter_template_get_request_contract(self):
        self.instance.notification_advance_filter_template_get()
        self.assert_request(
            'SYNO.Core.Notification.Advance.FilterSettings.Template',
            {'method': 'get'},
        )

    def test_variables_set_includes_payload(self):
        self.instance.notification_advance_variables_set(variables='vars-json')
        self.assert_request(
            'SYNO.Core.Notification.Advance.Variables',
            {'method': 'set', 'variables': 'vars-json'},
        )

    def test_warning_percentage_set_preserves_integer(self):
        self.instance.notification_advance_warning_percentage_set(
            percentage=85)
        self.assert_request(
            'SYNO.Core.Notification.Advance.WarningPercentage',
            {'method': 'set', 'percentage': 85},
        )

    def test_cms_get_request_contract(self):
        self.instance.notification_cms_get()
        self.assert_request(
            'SYNO.Core.Notification.CMS',
            {'method': 'get'},
        )

    def test_cms_conf_set_includes_conf(self):
        self.instance.notification_cms_conf_set(conf='conf-json')
        self.assert_request(
            'SYNO.Core.Notification.CMS.Conf',
            {'method': 'set', 'conf': 'conf-json'},
        )

    def test_line_set_converts_boolean_and_includes_token(self):
        self.instance.notification_line_set(token='line-token', enable=False)
        self.assert_request(
            'SYNO.Core.Notification.Line',
            {'method': 'set', 'token': 'line-token', 'enable': 'false'},
        )

    def test_mail_set_includes_settings(self):
        self.instance.notification_mail_set(settings='mail-json')
        self.assert_request(
            'SYNO.Core.Notification.Mail',
            {'method': 'set', 'settings': 'mail-json'},
        )

    def test_mail_auth_set_omits_missing_password(self):
        self.instance.notification_mail_auth_set(
            auth_type='login', username='notify')
        self.assert_request(
            'SYNO.Core.Notification.Mail.Auth',
            {'method': 'set', 'auth_type': 'login', 'username': 'notify'},
        )

    def test_mail_oauth_set_includes_credentials(self):
        self.instance.notification_mail_oauth_set(
            client_id='cid', client_secret='secret', refresh_token='refresh')
        self.assert_request(
            'SYNO.Core.Notification.Mail.Oauth',
            {
                'method': 'set',
                'client_id': 'cid',
                'client_secret': 'secret',
                'refresh_token': 'refresh',
            },
        )

    def test_mail_profile_conf_get_request_contract(self):
        self.instance.notification_mail_profile_conf_get()
        self.assert_request(
            'SYNO.Core.Notification.Mail.Profile.Conf',
            {'method': 'get'},
        )

    def test_push_set_converts_boolean(self):
        self.instance.notification_push_set(enable=True)
        self.assert_request(
            'SYNO.Core.Notification.Push',
            {'method': 'set', 'enable': 'true'},
        )

    def test_push_auth_token_set_includes_token(self):
        self.instance.notification_push_auth_token_set(token='push-token')
        self.assert_request(
            'SYNO.Core.Notification.Push.AuthToken',
            {'method': 'set', 'token': 'push-token'},
        )

    def test_push_mobile_get_request_contract(self):
        self.instance.notification_push_mobile_get()
        self.assert_request(
            'SYNO.Core.Notification.Push.Mobile',
            {'method': 'get'},
        )

    def test_webhook_provider_set_omits_missing_token(self):
        self.instance.notification_push_webhook_provider_set(
            provider='slack', url='https://example.invalid/hook')
        self.assert_request(
            'SYNO.Core.Notification.Push.Webhook.Provider',
            {
                'method': 'set',
                'provider': 'slack',
                'url': 'https://example.invalid/hook',
            },
        )

    def test_sms_set_includes_settings(self):
        self.instance.notification_sms_set(settings='sms-json')
        self.assert_request(
            'SYNO.Core.Notification.SMS',
            {'method': 'set', 'settings': 'sms-json'},
        )

    def test_sms_provider_set_omits_missing_api_key(self):
        self.instance.notification_sms_provider_set(provider='twilio')
        self.assert_request(
            'SYNO.Core.Notification.SMS.Provider',
            {'method': 'set', 'provider': 'twilio'},
        )

    def test_sysnotify_get_request_contract(self):
        self.instance.notification_sysnotify_get()
        self.assert_request(
            'SYNO.Core.Notification.Sysnotify',
            {'method': 'get'},
        )


class TestCoreNotificationCoverage(unittest.TestCase):
    """Meta-tests for API namespace coverage."""

    def test_all_namespaces_covered(self):
        """Every API namespace must be referenced in at least one method."""
        source = inspect.getsource(CoreNotification)
        for namespace in API_LIST:
            with self.subTest(namespace=namespace):
                self.assertIn(f"'{namespace}'", source)

    def test_method_count(self):
        """Verify expected number of public methods."""
        public = [m for m in dir(CoreNotification)
                  if not m.startswith('_') and callable(getattr(CoreNotification, m))
                  and m != 'logout']
        self.assertGreaterEqual(len(public), 40,
                                f"Expected 40+ methods, found {len(public)}")


if __name__ == '__main__':
    unittest.main()
