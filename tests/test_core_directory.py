"""Unit tests for core_directory — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_directory import CoreDirectory


def _make_instance():
    """Create a CoreDirectory instance with mocked auth/session."""
    with patch('synology_api.core_directory.base_api.BaseApi.__init__', return_value=None):
        instance = CoreDirectory.__new__(CoreDirectory)

    api_list = {
        'SYNO.Core.Directory.Azure.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.Domain.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.Domain.Trust': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.BaseDN': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Login.Notify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.Refresh': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.LDAP.User': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.OIDC.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.CAS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Profile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML.Metadata': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.SAML.Status': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Setting': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.Status': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.SSO.utils': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Directory.WebSphere.SSO': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreDirectory(unittest.TestCase):
    """Tests for CoreDirectory methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_directory_azure_sso_get(self):
        self.instance.directory_azure_sso_get()
        self.instance.request_data.assert_called_once()

    def test_directory_domain_conf_get(self):
        self.instance.directory_domain_conf_get()
        self.instance.request_data.assert_called_once()

    def test_directory_domain_trust_get(self):
        self.instance.directory_domain_trust_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_base_dn_get(self):
        self.instance.directory_ldap_base_dn_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_login_notify_get(self):
        self.instance.directory_ldap_login_notify_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_profile_get(self):
        self.instance.directory_ldap_profile_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_refresh_get(self):
        self.instance.directory_ldap_refresh_get()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_refresh_set(self):
        self.instance.directory_ldap_refresh_set()
        self.instance.request_data.assert_called_once()

    def test_directory_ldap_user_get(self):
        self.instance.directory_ldap_user_get()
        self.instance.request_data.assert_called_once()

    def test_directory_oidc_sso_get(self):
        self.instance.directory_oidc_sso_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_cas_get(self):
        self.instance.directory_sso_cas_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_profile_get(self):
        self.instance.directory_sso_profile_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_get(self):
        self.instance.directory_sso_saml_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_metadata_get(self):
        self.instance.directory_sso_saml_metadata_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_saml_status_get(self):
        self.instance.directory_sso_saml_status_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_setting_get(self):
        self.instance.directory_sso_setting_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_status_get(self):
        self.instance.directory_sso_status_get()
        self.instance.request_data.assert_called_once()

    def test_directory_sso_utils_get(self):
        self.instance.directory_sso_utils_get()
        self.instance.request_data.assert_called_once()

    def test_directory_websphere_sso_get(self):
        self.instance.directory_websphere_sso_get()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
