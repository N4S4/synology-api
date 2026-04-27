"""
Synology Core miscellaneous services API wrapper.

Covers the remaining SYNO.Core.* sub-namespaces not handled by the
dedicated core_security, core_network, core_notification, core_directory,
core_storage, core_upgrade, core_system, or core_external_device modules.
"""

from __future__ import annotations
import json
from typing import Optional, Sequence
from . import base_api


class CoreServiceApps(base_api.BaseApi):
    """Core app/file services: ACL, AppPortal, CMS, FileServ, Findhost, and more."""

    # ------------------------------------------------------------------
    # SYNO.Core.ACL
    # ------------------------------------------------------------------

    def acl_get(self, path: str) -> dict[str, object] | str:
        """
        Get ACL for a given path.

        Parameters
        ----------
        path : str
            The path value.

        Returns
        -------
        dict[str, object] or str
            Result of the acl get operation.
        """
        api_name = 'SYNO.Core.ACL'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'path': path})

    def acl_set(self, path: str, acl: dict) -> dict[str, object] | str:
        """
        Set ACL for a given path.

        Parameters
        ----------
        path : str
            The path value.
        acl : dict
            The acl value.

        Returns
        -------
        dict[str, object] or str
            Result of the acl set operation.
        """
        api_name = 'SYNO.Core.ACL'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'path': path, 'acl': json.dumps(acl)})

    # ------------------------------------------------------------------
    # SYNO.Core.ActionPriv / SYNO.Core.ActionPriv.Role
    # ------------------------------------------------------------------

    def action_priv_get(self) -> dict[str, object] | str:
        """
        Get action privilege settings.

        Returns
        -------
        dict[str, object] or str
            Result of the action priv get operation.
        """
        api_name = 'SYNO.Core.ActionPriv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def action_priv_role_get(self) -> dict[str, object] | str:
        """
        Get action privilege roles.

        Returns
        -------
        dict[str, object] or str
            Result of the action priv role get operation.
        """
        api_name = 'SYNO.Core.ActionPriv.Role'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def action_priv_role_set(self, roles: dict) -> dict[str, object] | str:
        """
        Set action privilege roles.

        Parameters
        ----------
        roles : dict
            The roles value.

        Returns
        -------
        dict[str, object] or str
            Result of the action priv role set operation.
        """
        api_name = 'SYNO.Core.ActionPriv.Role'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'roles': json.dumps(roles)})

    # ------------------------------------------------------------------
    # SYNO.Core.AppNotify
    # ------------------------------------------------------------------

    def app_notify_get(self) -> dict[str, object] | str:
        """
        Get application notification settings.

        Returns
        -------
        dict[str, object] or str
            Result of the app notify get operation.
        """
        api_name = 'SYNO.Core.AppNotify'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.AppPortal / AccessControl / Config / ReverseProxy
    # ------------------------------------------------------------------

    def app_portal_get(self) -> dict[str, object] | str:
        """
        Get application portal settings.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal get operation.
        """
        api_name = 'SYNO.Core.AppPortal'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set application portal settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal set operation.
        """
        api_name = 'SYNO.Core.AppPortal'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def app_portal_access_control_get(self) -> dict[str, object] | str:
        """
        Get application portal access control settings.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal access control get operation.
        """
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_access_control_list(self) -> dict[str, object] | str:
        """
        List application portal access control entries.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal access control list operation.
        """
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'list'})

    def app_portal_access_control_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set application portal access control settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal access control set operation.
        """
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def app_portal_access_control_update(self, entry: dict[str, object] | str) -> dict[str, object] | str:
        """
        Update an application portal access control entry.

        Parameters
        ----------
        entry : dict[str, object] or str
            Access control entry to update. Dict values are JSON encoded before
            they are sent to DSM.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal access control update operation.
        """
        api_name = 'SYNO.Core.AppPortal.AccessControl'
        info = self.gen_list[api_name]
        req_param = {
            'version': info['maxVersion'],
            'method': 'update',
            'entry': self._format_app_portal_entry(entry),
        }
        return self.request_data(api_name, info['path'], req_param)

    @staticmethod
    def _format_app_portal_entry(entry: dict[str, object] | str) -> str:
        """
        Format an AppPortal entry payload for DSM.

        Parameters
        ----------
        entry : dict[str, object] or str
            Entry payload as a Python dictionary or pre-encoded JSON string.

        Returns
        -------
        str
            JSON string to send to DSM.
        """
        if isinstance(entry, str):
            return entry
        return json.dumps(entry, separators=(',', ':'))

    def app_portal_config_get(self) -> dict[str, object] | str:
        """
        Get application portal configuration.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal config get operation.
        """
        api_name = 'SYNO.Core.AppPortal.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_portal_reverse_proxy_get(self) -> dict[str, object] | str:
        """
        List reverse proxy rules for app portal.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy list operation.
        """
        return self.app_portal_reverse_proxy_list()

    def app_portal_reverse_proxy_list(self) -> dict[str, object] | str:
        """
        List reverse proxy rules for app portal.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy list operation.
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'list'})

    def app_portal_reverse_proxy_create(self, entry: dict[str, object] | str) -> dict[str, object] | str:
        """
        Create an app portal reverse proxy rule.

        Parameters
        ----------
        entry : dict[str, object] or str
            Reverse proxy entry to create. Dict values are JSON encoded before
            they are sent to DSM.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy create operation.
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'], {
            'version': info['maxVersion'],
            'method': 'create',
            'entry': self._format_app_portal_entry(entry),
        })

    def app_portal_reverse_proxy_update(self, entry: dict[str, object] | str) -> dict[str, object] | str:
        """
        Update an app portal reverse proxy rule.

        Parameters
        ----------
        entry : dict[str, object] or str
            Reverse proxy entry to update. Dict values are JSON encoded before
            they are sent to DSM.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy update operation.
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'], {
            'version': info['maxVersion'],
            'method': 'update',
            'entry': self._format_app_portal_entry(entry),
        })

    def app_portal_reverse_proxy_delete(self, uuids: str | Sequence[str]) -> dict[str, object] | str:
        """
        Delete app portal reverse proxy rules.

        Parameters
        ----------
        uuids : str or Sequence[str]
            Reverse proxy UUID or UUIDs to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy delete operation.
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        if isinstance(uuids, str):
            if uuids.lstrip().startswith('['):
                uuids_payload = uuids
            else:
                uuids_payload = json.dumps([uuids], separators=(',', ':'))
        else:
            uuids_payload = json.dumps(list(uuids), separators=(',', ':'))
        return self.request_data(api_name, info['path'], {
            'version': info['maxVersion'],
            'method': 'delete',
            'uuids': uuids_payload,
        })

    def app_portal_reverse_proxy_set(self, **kwargs) -> dict[str, object] | str:
        """
        Update reverse proxy rules for app portal.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the update operation.

        Returns
        -------
        dict[str, object] or str
            Result of the app portal reverse proxy update operation.
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'update'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.AppPriv / App / Rule
    # ------------------------------------------------------------------

    def app_priv_get(self) -> dict[str, object] | str:
        """
        Get application privilege settings.

        Returns
        -------
        dict[str, object] or str
            Result of the app priv get operation.
        """
        api_name = 'SYNO.Core.AppPriv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_app_get(self) -> dict[str, object] | str:
        """
        Get per-application privilege settings.

        Returns
        -------
        dict[str, object] or str
            Result of the app priv app get operation.
        """
        api_name = 'SYNO.Core.AppPriv.App'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_rule_get(self) -> dict[str, object] | str:
        """
        Get application privilege rules.

        Returns
        -------
        dict[str, object] or str
            Result of the app priv rule get operation.
        """
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def app_priv_rule_set(self, rules: dict) -> dict[str, object] | str:
        """
        Set application privilege rules.

        Parameters
        ----------
        rules : dict
            The rules value.

        Returns
        -------
        dict[str, object] or str
            Result of the app priv rule set operation.
        """
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'rules': json.dumps(rules)})

    # ------------------------------------------------------------------
    # SYNO.Core.BackgroundTask
    # ------------------------------------------------------------------

    def background_task_list(self) -> dict[str, object] | str:
        """
        List all background tasks.

        Returns
        -------
        dict[str, object] or str
            Result of the background task list operation.
        """
        api_name = 'SYNO.Core.BackgroundTask'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'list'})

    def background_task_get(self, task_id: str) -> dict[str, object] | str:
        """
        Get a specific background task status.

        Parameters
        ----------
        task_id : str
            The task id value.

        Returns
        -------
        dict[str, object] or str
            Result of the background task get operation.
        """
        api_name = 'SYNO.Core.BackgroundTask'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'taskid': task_id})

    # ------------------------------------------------------------------
    # SYNO.Core.Backup.ED
    # ------------------------------------------------------------------

    def backup_ed_get(self) -> dict[str, object] | str:
        """
        Get encrypted data backup settings.

        Returns
        -------
        dict[str, object] or str
            Result of the backup ed get operation.
        """
        api_name = 'SYNO.Core.Backup.ED'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.BandwidthControl
    # ------------------------------------------------------------------

    def bandwidth_control_get(self) -> dict[str, object] | str:
        """
        Get bandwidth control settings.

        Returns
        -------
        dict[str, object] or str
            Result of the bandwidth control get operation.
        """
        api_name = 'SYNO.Core.BandwidthControl'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def bandwidth_control_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set bandwidth control settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the bandwidth control set operation.
        """
        api_name = 'SYNO.Core.BandwidthControl'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.CMS (Central Management System)
    # ------------------------------------------------------------------

    def cms_get(self) -> dict[str, object] | str:
        """
        Get CMS settings.

        Returns
        -------
        dict[str, object] or str
            Result of the cms get operation.
        """
        api_name = 'SYNO.Core.CMS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_cache_get(self) -> dict[str, object] | str:
        """
        Get CMS cache information.

        Returns
        -------
        dict[str, object] or str
            Result of the cms cache get operation.
        """
        api_name = 'SYNO.Core.CMS.Cache'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_identity_get(self) -> dict[str, object] | str:
        """
        Get CMS identity information.

        Returns
        -------
        dict[str, object] or str
            Result of the cms identity get operation.
        """
        api_name = 'SYNO.Core.CMS.Identity'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_policy_get(self) -> dict[str, object] | str:
        """
        Get CMS policy settings.

        Returns
        -------
        dict[str, object] or str
            Result of the cms policy get operation.
        """
        api_name = 'SYNO.Core.CMS.Policy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_policy_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set CMS policy.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the cms policy set operation.
        """
        api_name = 'SYNO.Core.CMS.Policy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def cms_server_info_get(self) -> dict[str, object] | str:
        """
        Get CMS server information.

        Returns
        -------
        dict[str, object] or str
            Result of the cms server info get operation.
        """
        api_name = 'SYNO.Core.CMS.ServerInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_task_get(self) -> dict[str, object] | str:
        """
        Get CMS task status.

        Returns
        -------
        dict[str, object] or str
            Result of the cms task get operation.
        """
        api_name = 'SYNO.Core.CMS.Task'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def cms_token_get(self) -> dict[str, object] | str:
        """
        Get CMS authentication token.

        Returns
        -------
        dict[str, object] or str
            Result of the cms token get operation.
        """
        api_name = 'SYNO.Core.CMS.Token'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Certificate extras (CSR, LetsEncrypt, Tencent)
    # ------------------------------------------------------------------

    def certificate_csr_get(self) -> dict[str, object] | str:
        """
        Get certificate signing request settings.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate csr get operation.
        """
        api_name = 'SYNO.Core.Certificate.CSR'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def certificate_csr_create(self, **kwargs) -> dict[str, object] | str:
        """
        Create a certificate signing request.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the create operation.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate csr create operation.
        """
        api_name = 'SYNO.Core.Certificate.CSR'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'create'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def certificate_letsencrypt_get(self) -> dict[str, object] | str:
        """
        Get Let's Encrypt certificate settings.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate letsencrypt get operation.
        """
        api_name = 'SYNO.Core.Certificate.LetsEncrypt'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def certificate_letsencrypt_create(self, **kwargs) -> dict[str, object] | str:
        """
        Create/renew a Let's Encrypt certificate.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the create operation.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate letsencrypt create operation.
        """
        api_name = 'SYNO.Core.Certificate.LetsEncrypt'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'create'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def certificate_letsencrypt_account_get(self) -> dict[str, object] | str:
        """
        Get Let's Encrypt account information.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate letsencrypt account get operation.
        """
        api_name = 'SYNO.Core.Certificate.LetsEncrypt.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def certificate_tencent_get(self) -> dict[str, object] | str:
        """
        Get Tencent SSL certificate settings.

        Returns
        -------
        dict[str, object] or str
            Result of the certificate tencent get operation.
        """
        api_name = 'SYNO.Core.Certificate.Tencent'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DDNS extras (Ethernet, TWNIC)
    # ------------------------------------------------------------------

    def ddns_ethernet_get(self) -> dict[str, object] | str:
        """
        Get DDNS ethernet interface settings.

        Returns
        -------
        dict[str, object] or str
            Result of the ddns ethernet get operation.
        """
        api_name = 'SYNO.Core.DDNS.Ethernet'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def ddns_twnic_get(self) -> dict[str, object] | str:
        """
        Get TWNIC DDNS settings.

        Returns
        -------
        dict[str, object] or str
            Result of the ddns twnic get operation.
        """
        api_name = 'SYNO.Core.DDNS.TWNIC'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DSMNotify extras
    # ------------------------------------------------------------------

    def dsm_notify_mail_content_get(self) -> dict[str, object] | str:
        """
        Get DSM notification mail content templates.

        Returns
        -------
        dict[str, object] or str
            Result of the dsm notify mail content get operation.
        """
        api_name = 'SYNO.Core.DSMNotify.MailContent'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def dsm_notify_strings_get(self) -> dict[str, object] | str:
        """
        Get DSM notification strings.

        Returns
        -------
        dict[str, object] or str
            Result of the dsm notify strings get operation.
        """
        api_name = 'SYNO.Core.DSMNotify.Strings'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.DataCollect / Application
    # ------------------------------------------------------------------

    def data_collect_get(self) -> dict[str, object] | str:
        """
        Get data collection settings.

        Returns
        -------
        dict[str, object] or str
            Result of the data collect get operation.
        """
        api_name = 'SYNO.Core.DataCollect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def data_collect_set(self, enabled: bool = True) -> dict[str, object] | str:
        """
        Set data collection settings.

        Parameters
        ----------
        enabled : bool, optional
            The enabled value.

        Returns
        -------
        dict[str, object] or str
            Result of the data collect set operation.
        """
        api_name = 'SYNO.Core.DataCollect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'enabled': json.dumps(enabled)})

    def data_collect_application_get(self) -> dict[str, object] | str:
        """
        Get per-application data collection settings.

        Returns
        -------
        dict[str, object] or str
            Result of the data collect application get operation.
        """
        api_name = 'SYNO.Core.DataCollect.Application'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.EW.Info
    # ------------------------------------------------------------------

    def ew_info_get(self) -> dict[str, object] | str:
        """
        Get extended warranty information.

        Returns
        -------
        dict[str, object] or str
            Result of the ew info get operation.
        """
        api_name = 'SYNO.Core.EW.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Factory
    # ------------------------------------------------------------------

    def factory_config_get(self) -> dict[str, object] | str:
        """
        Get factory configuration.

        Returns
        -------
        dict[str, object] or str
            Result of the factory config get operation.
        """
        api_name = 'SYNO.Core.Factory.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def factory_manutild_get(self) -> dict[str, object] | str:
        """
        Get factory manufacturing settings.

        Returns
        -------
        dict[str, object] or str
            Result of the factory manutild get operation.
        """
        api_name = 'SYNO.Core.Factory.Manutild'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.File / Thumbnail
    # ------------------------------------------------------------------

    def file_get(self, path: str) -> dict[str, object] | str:
        """
        Get file information.

        Parameters
        ----------
        path : str
            The path value.

        Returns
        -------
        dict[str, object] or str
            Result of the file get operation.
        """
        api_name = 'SYNO.Core.File'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'path': path})

    def file_thumbnail_get(self, path: str, size: str = 'small') -> dict[str, object] | str:
        """
        Get file thumbnail.

        Parameters
        ----------
        path : str
            The path value.
        size : str, optional
            The size value.

        Returns
        -------
        dict[str, object] or str
            Result of the file thumbnail get operation.
        """
        api_name = 'SYNO.Core.File.Thumbnail'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get',
                                  'path': path, 'size': size})

    # ------------------------------------------------------------------
    # SYNO.Core.FileServ NFS/Rsync/SMB extras
    # ------------------------------------------------------------------

    def fileserv_nfs_advanced_get(self) -> dict[str, object] | str:
        """
        Get NFS advanced settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs advanced get operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.AdvancedSetting'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_advanced_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set NFS advanced settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs advanced set operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.AdvancedSetting'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def fileserv_nfs_conf_backup_get(self) -> dict[str, object] | str:
        """
        Get NFS configuration backup.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs conf backup get operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.ConfBackup'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_idmap_get(self) -> dict[str, object] | str:
        """
        Get NFS ID mapping settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs idmap get operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.IDMap'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_kerberos_get(self) -> dict[str, object] | str:
        """
        Get NFS Kerberos settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs kerberos get operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.Kerberos'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_nfs_share_privilege_get(self) -> dict[str, object] | str:
        """
        Get NFS share privileges.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv nfs share privilege get operation.
        """
        api_name = 'SYNO.Core.FileServ.NFS.SharePrivilege'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_rsync_account_get(self) -> dict[str, object] | str:
        """
        Get rsync account settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv rsync account get operation.
        """
        api_name = 'SYNO.Core.FileServ.Rsync.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_rsync_account_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set rsync account settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv rsync account set operation.
        """
        api_name = 'SYNO.Core.FileServ.Rsync.Account'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def fileserv_smb_conf_backup_get(self) -> dict[str, object] | str:
        """
        Get SMB configuration backup.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv smb conf backup get operation.
        """
        api_name = 'SYNO.Core.FileServ.SMB.ConfBackup'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_smb_control_get(self) -> dict[str, object] | str:
        """
        Get SMB control settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv smb control get operation.
        """
        api_name = 'SYNO.Core.FileServ.SMB.Control'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def fileserv_smb_msdfs_get(self) -> dict[str, object] | str:
        """
        Get SMB MS-DFS settings.

        Returns
        -------
        dict[str, object] or str
            Result of the fileserv smb msdfs get operation.
        """
        api_name = 'SYNO.Core.FileServ.SMB.MSDFS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Findhost
    # ------------------------------------------------------------------

    def findhost_get(self) -> dict[str, object] | str:
        """
        Get find-host settings.

        Returns
        -------
        dict[str, object] or str
            Result of the findhost get operation.
        """
        api_name = 'SYNO.Core.Findhost'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
