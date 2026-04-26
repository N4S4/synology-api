"""Unit tests for core_security — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_security_auth import CoreSecurityAuth


def _make_instance():
    """Create a CoreSecurityAuth instance with mocked auth/session."""
    with patch('synology_api.core_security_auth.base_api.BaseApi.__init__', return_value=None):
        instance = CoreSecurityAuth.__new__(CoreSecurityAuth)

    api_list = {
        'SYNO.Core.SmartBlock': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Device': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Trusted': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.Untrusted': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SmartBlock.User': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Admin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.EnforcePolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Ex': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.OTP.Mail': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.TrustDevice': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DisableAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreSecurityAuth(unittest.TestCase):
    """Tests for CoreSecurityAuth methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_disable_admin_get(self):
        self.instance.disable_admin_get()
        self.instance.request_data.assert_called_once()

    def test_disable_admin_set(self):
        self.instance.disable_admin_set()
        self.instance.request_data.assert_called_once()

    def test_otp_admin_get(self):
        self.instance.otp_admin_get()
        self.instance.request_data.assert_called_once()

    def test_otp_admin_set(self):
        self.instance.otp_admin_set()
        self.instance.request_data.assert_called_once()

    def test_otp_enforce_policy_get(self):
        self.instance.otp_enforce_policy_get()
        self.instance.request_data.assert_called_once()

    def test_otp_enforce_policy_set(self):
        self.instance.otp_enforce_policy_set()
        self.instance.request_data.assert_called_once()

    def test_otp_ex_get(self):
        self.instance.otp_ex_get()
        self.instance.request_data.assert_called_once()

    def test_otp_ex_set(self):
        self.instance.otp_ex_set()
        self.instance.request_data.assert_called_once()

    def test_otp_get(self):
        self.instance.otp_get()
        self.instance.request_data.assert_called_once()

    def test_otp_mail_get(self):
        self.instance.otp_mail_get()
        self.instance.request_data.assert_called_once()

    def test_otp_mail_set(self):
        self.instance.otp_mail_set()
        self.instance.request_data.assert_called_once()

    def test_otp_set(self):
        self.instance.otp_set()
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_delete(self):
        self.instance.smartblock_device_delete(devices='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_get(self):
        self.instance.smartblock_device_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_device_list(self):
        self.instance.smartblock_device_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_get(self):
        self.instance.smartblock_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_set(self):
        self.instance.smartblock_set()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_delete(self):
        self.instance.smartblock_trusted_delete(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_get(self):
        self.instance.smartblock_trusted_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_list(self):
        self.instance.smartblock_trusted_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_trusted_set(self):
        self.instance.smartblock_trusted_set(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_delete(self):
        self.instance.smartblock_untrusted_delete(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_get(self):
        self.instance.smartblock_untrusted_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_list(self):
        self.instance.smartblock_untrusted_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_untrusted_set(self):
        self.instance.smartblock_untrusted_set(entries='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_delete(self):
        self.instance.smartblock_user_delete(users='test')
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_get(self):
        self.instance.smartblock_user_get()
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_list(self):
        self.instance.smartblock_user_list()
        self.instance.request_data.assert_called_once()

    def test_smartblock_user_set(self):
        self.instance.smartblock_user_set(users='test')
        self.instance.request_data.assert_called_once()

    def test_trust_device_delete(self):
        self.instance.trust_device_delete(devices='test')
        self.instance.request_data.assert_called_once()

    def test_trust_device_get(self):
        self.instance.trust_device_get()
        self.instance.request_data.assert_called_once()

    def test_trust_device_list(self):
        self.instance.trust_device_list()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
