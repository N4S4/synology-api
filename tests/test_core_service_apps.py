"""Unit tests for core_service — verifies all API namespaces are covered."""

import inspect
import unittest
from unittest.mock import MagicMock, patch

from synology_api.core_service_apps import CoreServiceApps


def _make_instance():
    """Create a CoreServiceApps instance with mocked auth/session."""
    with patch('synology_api.core_service_apps.base_api.BaseApi.__init__', return_value=None):
        instance = CoreServiceApps.__new__(CoreServiceApps)

    api_list = {
        'SYNO.Core.ACL': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ActionPriv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.ActionPriv.Role': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppNotify': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.AccessControl': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPortal.ReverseProxy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv.App': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.AppPriv.Rule': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.BackgroundTask': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Backup.ED': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.BandwidthControl': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Cache': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Identity': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Policy': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.ServerInfo': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Task': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.CMS.Token': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.CSR': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.LetsEncrypt': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.LetsEncrypt.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Certificate.Tencent': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DDNS.Ethernet': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DDNS.TWNIC': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DSMNotify.MailContent': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DSMNotify.Strings': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DataCollect': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.DataCollect.Application': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.EW.Info': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Factory.Config': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Factory.Manutild': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.File': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.File.Thumbnail': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.AdvancedSetting': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.ConfBackup': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.IDMap': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.Kerberos': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.NFS.SharePrivilege': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.Rsync.Account': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.ConfBackup': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.Control': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.FileServ.SMB.MSDFS': {'path': 'entry.cgi', 'maxVersion': 1},
        'SYNO.Core.Findhost': {'path': 'entry.cgi', 'maxVersion': 1},
    }
    instance.gen_list = api_list
    instance.request_data = MagicMock(
        return_value={'success': True, 'data': {}})
    return instance


class TestCoreServiceApps(unittest.TestCase):
    """Tests for CoreServiceApps methods."""

    def setUp(self):
        self.instance = _make_instance()

    def test_acl_get(self):
        self.instance.acl_get(path='test')
        self.instance.request_data.assert_called_once()

    def test_acl_set(self):
        self.instance.acl_set(path='test', acl={"test": True})
        self.instance.request_data.assert_called_once()

    def test_action_priv_get(self):
        self.instance.action_priv_get()
        self.instance.request_data.assert_called_once()

    def test_action_priv_role_get(self):
        self.instance.action_priv_role_get()
        self.instance.request_data.assert_called_once()

    def test_action_priv_role_set(self):
        self.instance.action_priv_role_set(roles={"test": True})
        self.instance.request_data.assert_called_once()

    def test_app_notify_get(self):
        self.instance.app_notify_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_access_control_get(self):
        self.instance.app_portal_access_control_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_access_control_list_request_contract(self):
        self.instance.app_portal_access_control_list()
        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.AccessControl',
            'entry.cgi',
            {'version': 1, 'method': 'list'},
        )

    def test_app_portal_access_control_set(self):
        self.instance.app_portal_access_control_set()
        self.instance.request_data.assert_called_once()

    def test_app_portal_access_control_update_serializes_entry(self):
        entry = {
            'UUID': 'rule-uuid',
            '_key': 'rule-key',
            'name': 'block',
            'rules': [
                {'access': True, 'address': '192.0.2.1'},
                {'access': False, 'address': '198.51.100.2'},
            ],
        }
        expected_entry = (
            '{"UUID":"rule-uuid","_key":"rule-key","name":"block",'
            '"rules":[{"access":true,"address":"192.0.2.1"},'
            '{"access":false,"address":"198.51.100.2"}]}'
        )

        self.instance.app_portal_access_control_update(entry)

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.AccessControl',
            'entry.cgi',
            {'version': 1, 'method': 'update', 'entry': expected_entry},
        )

    def test_app_portal_access_control_update_accepts_preencoded_entry(self):
        entry = '{"UUID":"rule-uuid","rules":[]}'

        self.instance.app_portal_access_control_update(entry)

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.AccessControl',
            'entry.cgi',
            {'version': 1, 'method': 'update', 'entry': entry},
        )

    def test_app_portal_config_get(self):
        self.instance.app_portal_config_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_get(self):
        self.instance.app_portal_get()
        self.instance.request_data.assert_called_once()

    def test_app_portal_reverse_proxy_get(self):
        self.instance.app_portal_reverse_proxy_get()
        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {'version': 1, 'method': 'list'},
        )

    def test_app_portal_reverse_proxy_list_request_contract(self):
        self.instance.app_portal_reverse_proxy_list()
        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {'version': 1, 'method': 'list'},
        )

    def test_app_portal_reverse_proxy_create_serializes_entry(self):
        entry = {
            'description': 'test',
            'frontend': {'fqdn': 'test.local', 'port': 18080, 'protocol': 0, 'acl': None},
            'backend': {'fqdn': '127.0.0.1', 'port': 80, 'protocol': 0},
            'proxy_intercept_errors': False,
        }
        expected_entry = (
            '{"description":"test","frontend":{"fqdn":"test.local",'
            '"port":18080,"protocol":0,"acl":null},"backend":'
            '{"fqdn":"127.0.0.1","port":80,"protocol":0},'
            '"proxy_intercept_errors":false}'
        )

        self.instance.app_portal_reverse_proxy_create(entry)

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {'version': 1, 'method': 'create', 'entry': expected_entry},
        )

    def test_app_portal_reverse_proxy_update_accepts_preencoded_entry(self):
        entry = '{"UUID":"rule-uuid","description":"test"}'

        self.instance.app_portal_reverse_proxy_update(entry)

        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {'version': 1, 'method': 'update', 'entry': entry},
        )

    def test_app_portal_reverse_proxy_delete_serializes_uuid_list(self):
        self.instance.app_portal_reverse_proxy_delete(
            ['rule-uuid-1', 'rule-uuid-2'])
        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {
                'version': 1,
                'method': 'delete',
                'uuids': '["rule-uuid-1","rule-uuid-2"]',
            },
        )

    def test_app_portal_reverse_proxy_set(self):
        self.instance.app_portal_reverse_proxy_set(
            entry='{"UUID":"rule-uuid"}')
        self.instance.request_data.assert_called_once_with(
            'SYNO.Core.AppPortal.ReverseProxy',
            'entry.cgi',
            {
                'version': 1,
                'method': 'update',
                'entry': '{"UUID":"rule-uuid"}',
            },
        )

    def test_app_portal_set(self):
        self.instance.app_portal_set()
        self.instance.request_data.assert_called_once()

    def test_app_priv_app_get(self):
        self.instance.app_priv_app_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_get(self):
        self.instance.app_priv_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_rule_get(self):
        self.instance.app_priv_rule_get()
        self.instance.request_data.assert_called_once()

    def test_app_priv_rule_set(self):
        self.instance.app_priv_rule_set(rules={"test": True})
        self.instance.request_data.assert_called_once()

    def test_background_task_get(self):
        self.instance.background_task_get(task_id='test')
        self.instance.request_data.assert_called_once()

    def test_background_task_list(self):
        self.instance.background_task_list()
        self.instance.request_data.assert_called_once()

    def test_backup_ed_get(self):
        self.instance.backup_ed_get()
        self.instance.request_data.assert_called_once()

    def test_bandwidth_control_get(self):
        self.instance.bandwidth_control_get()
        self.instance.request_data.assert_called_once()

    def test_bandwidth_control_set(self):
        self.instance.bandwidth_control_set()
        self.instance.request_data.assert_called_once()

    def test_certificate_csr_create(self):
        self.instance.certificate_csr_create()
        self.instance.request_data.assert_called_once()

    def test_certificate_csr_get(self):
        self.instance.certificate_csr_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_account_get(self):
        self.instance.certificate_letsencrypt_account_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_create(self):
        self.instance.certificate_letsencrypt_create()
        self.instance.request_data.assert_called_once()

    def test_certificate_letsencrypt_get(self):
        self.instance.certificate_letsencrypt_get()
        self.instance.request_data.assert_called_once()

    def test_certificate_tencent_get(self):
        self.instance.certificate_tencent_get()
        self.instance.request_data.assert_called_once()

    def test_cms_cache_get(self):
        self.instance.cms_cache_get()
        self.instance.request_data.assert_called_once()

    def test_cms_get(self):
        self.instance.cms_get()
        self.instance.request_data.assert_called_once()

    def test_cms_identity_get(self):
        self.instance.cms_identity_get()
        self.instance.request_data.assert_called_once()

    def test_cms_policy_get(self):
        self.instance.cms_policy_get()
        self.instance.request_data.assert_called_once()

    def test_cms_policy_set(self):
        self.instance.cms_policy_set()
        self.instance.request_data.assert_called_once()

    def test_cms_server_info_get(self):
        self.instance.cms_server_info_get()
        self.instance.request_data.assert_called_once()

    def test_cms_task_get(self):
        self.instance.cms_task_get()
        self.instance.request_data.assert_called_once()

    def test_cms_token_get(self):
        self.instance.cms_token_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_application_get(self):
        self.instance.data_collect_application_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_get(self):
        self.instance.data_collect_get()
        self.instance.request_data.assert_called_once()

    def test_data_collect_set(self):
        self.instance.data_collect_set(enabled=True)
        self.instance.request_data.assert_called_once()

    def test_ddns_ethernet_get(self):
        self.instance.ddns_ethernet_get()
        self.instance.request_data.assert_called_once()

    def test_ddns_twnic_get(self):
        self.instance.ddns_twnic_get()
        self.instance.request_data.assert_called_once()

    def test_dsm_notify_mail_content_get(self):
        self.instance.dsm_notify_mail_content_get()
        self.instance.request_data.assert_called_once()

    def test_dsm_notify_strings_get(self):
        self.instance.dsm_notify_strings_get()
        self.instance.request_data.assert_called_once()

    def test_ew_info_get(self):
        self.instance.ew_info_get()
        self.instance.request_data.assert_called_once()

    def test_factory_config_get(self):
        self.instance.factory_config_get()
        self.instance.request_data.assert_called_once()

    def test_factory_manutild_get(self):
        self.instance.factory_manutild_get()
        self.instance.request_data.assert_called_once()

    def test_file_get(self):
        self.instance.file_get(path='test')
        self.instance.request_data.assert_called_once()

    def test_file_thumbnail_get(self):
        self.instance.file_thumbnail_get(path='test', size='test')
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_advanced_get(self):
        self.instance.fileserv_nfs_advanced_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_advanced_set(self):
        self.instance.fileserv_nfs_advanced_set()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_conf_backup_get(self):
        self.instance.fileserv_nfs_conf_backup_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_idmap_get(self):
        self.instance.fileserv_nfs_idmap_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_kerberos_get(self):
        self.instance.fileserv_nfs_kerberos_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_nfs_share_privilege_get(self):
        self.instance.fileserv_nfs_share_privilege_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_rsync_account_get(self):
        self.instance.fileserv_rsync_account_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_rsync_account_set(self):
        self.instance.fileserv_rsync_account_set()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_conf_backup_get(self):
        self.instance.fileserv_smb_conf_backup_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_control_get(self):
        self.instance.fileserv_smb_control_get()
        self.instance.request_data.assert_called_once()

    def test_fileserv_smb_msdfs_get(self):
        self.instance.fileserv_smb_msdfs_get()
        self.instance.request_data.assert_called_once()

    def test_findhost_get(self):
        self.instance.findhost_get()
        self.instance.request_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()
