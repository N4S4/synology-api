"""Unit tests for core_service — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_service_user import CoreServiceUser


def _make_instance():
    """Create a CoreServiceUser instance with mocked auth/session."""
    with patch('synology_api.core_service_user.base_api.BaseApi.__init__', return_value=None):
        instance = CoreServiceUser.__new__(CoreServiceUser)

    api_list = {
        'SYNO.Core.Promotion.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Promotion.PreInstall': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.Hostname': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.RegisterSite': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.SNI': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickConnect.Upnp': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickStart.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.QuickStart.Install': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer.File': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Analyzer.Share': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.History': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Redirect': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Report.Util': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ResetAdmin': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SecurityScan.Operation': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Service.Conf': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Service.PortInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Crypto': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Crypto.Key': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.CryptoFile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.AutoKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.Key': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.MachineKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.KeyManager.Store': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Migration': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Migration.Task': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.Permission': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.PermissionReport': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Share.ShellFile': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Initdata': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Login': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Sharing.Session': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Form': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Log': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SupportForm.Service': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Synohdpack': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.SyslogClient.PersonalActivity': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Tuned': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.Group': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordExpiry': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordMeter': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.PasswordPolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.User.UsernamePolicy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Virtualization.Host.Capability': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.VolEncKeepKey': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.DSM.External': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.Security.HTTPCompression': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Web.Security.TLSProfile': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreServiceUser(unittest.TestCase):
    """Tests for CoreServiceUser methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_promotion_info_get(self):
        self.instance.promotion_info_get()
        self.instance.request_data.assert_called_once()

    def test_promotion_preinstall_get(self):
        self.instance.promotion_preinstall_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_hostname_get(self):
        self.instance.quickconnect_hostname_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_register_site_get(self):
        self.instance.quickconnect_register_site_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_sni_get(self):
        self.instance.quickconnect_sni_get()
        self.instance.request_data.assert_called_once()

    def test_quickconnect_upnp_get(self):
        self.instance.quickconnect_upnp_get()
        self.instance.request_data.assert_called_once()

    def test_quickstart_info_get(self):
        self.instance.quickstart_info_get()
        self.instance.request_data.assert_called_once()

    def test_quickstart_install(self):
        self.instance.quickstart_install()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_file_get(self):
        self.instance.report_analyzer_file_get()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_get(self):
        self.instance.report_analyzer_get()
        self.instance.request_data.assert_called_once()

    def test_report_analyzer_share_get(self):
        self.instance.report_analyzer_share_get()
        self.instance.request_data.assert_called_once()

    def test_report_config_get(self):
        self.instance.report_config_get()
        self.instance.request_data.assert_called_once()

    def test_report_config_set(self):
        self.instance.report_config_set()
        self.instance.request_data.assert_called_once()

    def test_report_get(self):
        self.instance.report_get()
        self.instance.request_data.assert_called_once()

    def test_report_history_get(self):
        self.instance.report_history_get()
        self.instance.request_data.assert_called_once()

    def test_report_redirect_get(self):
        self.instance.report_redirect_get()
        self.instance.request_data.assert_called_once()

    def test_report_util_get(self):
        self.instance.report_util_get()
        self.instance.request_data.assert_called_once()

    def test_reset_admin_get(self):
        self.instance.reset_admin_get()
        self.instance.request_data.assert_called_once()

    def test_security_scan_operation_get(self):
        self.instance.security_scan_operation_get()
        self.instance.request_data.assert_called_once()

    def test_security_scan_operation_start(self):
        self.instance.security_scan_operation_start()
        self.instance.request_data.assert_called_once()

    def test_service_conf_get(self):
        self.instance.service_conf_get()
        self.instance.request_data.assert_called_once()

    def test_service_conf_set(self):
        self.instance.service_conf_set()
        self.instance.request_data.assert_called_once()

    def test_service_port_info_get(self):
        self.instance.service_port_info_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_file_get(self):
        self.instance.share_crypto_file_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_get(self):
        self.instance.share_crypto_get()
        self.instance.request_data.assert_called_once()

    def test_share_crypto_key_get(self):
        self.instance.share_crypto_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_auto_key_get(self):
        self.instance.share_key_manager_auto_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_key_get(self):
        self.instance.share_key_manager_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_machine_key_get(self):
        self.instance.share_key_manager_machine_key_get()
        self.instance.request_data.assert_called_once()

    def test_share_key_manager_store_get(self):
        self.instance.share_key_manager_store_get()
        self.instance.request_data.assert_called_once()

    def test_share_migration_get(self):
        self.instance.share_migration_get()
        self.instance.request_data.assert_called_once()

    def test_share_migration_task_get(self):
        self.instance.share_migration_task_get()
        self.instance.request_data.assert_called_once()

    def test_share_permission_get(self):
        self.instance.share_permission_get(name='test')
        self.instance.request_data.assert_called_once()

    def test_share_permission_report_get(self):
        self.instance.share_permission_report_get()
        self.instance.request_data.assert_called_once()

    def test_share_permission_set(self):
        self.instance.share_permission_set(
            name='test', permissions={"test": True})
        self.instance.request_data.assert_called_once()

    def test_share_shell_file_get(self):
        self.instance.share_shell_file_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_get(self):
        self.instance.sharing_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_initdata_get(self):
        self.instance.sharing_initdata_get()
        self.instance.request_data.assert_called_once()

    def test_sharing_login(self):
        self.instance.sharing_login(sharing_id='test', password='test')
        self.instance.request_data.assert_called_once()

    def test_sharing_session_get(self):
        self.instance.sharing_session_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_get(self):
        self.instance.support_form_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_log_get(self):
        self.instance.support_form_log_get()
        self.instance.request_data.assert_called_once()

    def test_support_form_service_get(self):
        self.instance.support_form_service_get()
        self.instance.request_data.assert_called_once()

    def test_synohdpack_get(self):
        self.instance.synohdpack_get()
        self.instance.request_data.assert_called_once()

    def test_syslog_personal_activity_get(self):
        self.instance.syslog_personal_activity_get()
        self.instance.request_data.assert_called_once()

    def test_tuned_get(self):
        self.instance.tuned_get()
        self.instance.request_data.assert_called_once()

    def test_tuned_set(self):
        self.instance.tuned_set()
        self.instance.request_data.assert_called_once()

    def test_user_group_get(self):
        self.instance.user_group_get(user='test')
        self.instance.request_data.assert_called_once()

    def test_user_password_expiry_get(self):
        self.instance.user_password_expiry_get()
        self.instance.request_data.assert_called_once()

    def test_user_password_meter_get(self):
        self.instance.user_password_meter_get(password='test')
        self.instance.request_data.assert_called_once()

    def test_user_password_policy_get(self):
        self.instance.user_password_policy_get()
        self.instance.request_data.assert_called_once()

    def test_user_password_policy_set(self):
        self.instance.user_password_policy_set()
        self.instance.request_data.assert_called_once()

    def test_user_username_policy_get(self):
        self.instance.user_username_policy_get()
        self.instance.request_data.assert_called_once()

    def test_virtualization_host_capability_get(self):
        self.instance.virtualization_host_capability_get()
        self.instance.request_data.assert_called_once()

    def test_vol_enc_keep_key_get(self):
        self.instance.vol_enc_keep_key_get()
        self.instance.request_data.assert_called_once()

    def test_vol_enc_keep_key_set(self):
        self.instance.vol_enc_keep_key_set()
        self.instance.request_data.assert_called_once()

    def test_web_dsm_external_get(self):
        self.instance.web_dsm_external_get()
        self.instance.request_data.assert_called_once()

    def test_web_dsm_external_set(self):
        self.instance.web_dsm_external_set()
        self.instance.request_data.assert_called_once()

    def test_web_security_http_compression_get(self):
        self.instance.web_security_http_compression_get()
        self.instance.request_data.assert_called_once()

    def test_web_security_http_compression_set(self):
        self.instance.web_security_http_compression_set()
        self.instance.request_data.assert_called_once()

    def test_web_security_tls_profile_get(self):
        self.instance.web_security_tls_profile_get()
        self.instance.request_data.assert_called_once()

    def test_web_security_tls_profile_set(self):
        self.instance.web_security_tls_profile_set()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
