"""Synology Core user/web/sharing service API (SYNO.Core.*)."""

from __future__ import annotations
import json
from typing import Optional
from . import base_api


class CoreServiceUser(base_api.BaseApi):
    """Core user/web services: Promotion, QuickConnect, Report, Share, Sharing, User, Web."""

    # SYNO.Core.Promotion
    # ------------------------------------------------------------------

    def promotion_info_get(self) -> dict[str, object] | str:
        """
        Get Synology promotion information.

        Returns
        -------
        dict[str, object] or str
            Result of the promotion info get operation.
        """
        api_name = 'SYNO.Core.Promotion.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def promotion_preinstall_get(self) -> dict[str, object] | str:
        """
        Get pre-install promotion information.

        Returns
        -------
        dict[str, object] or str
            Result of the promotion preinstall get operation.
        """
        api_name = 'SYNO.Core.Promotion.PreInstall'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.QuickConnect extras
    # ------------------------------------------------------------------

    def quickconnect_hostname_get(self) -> dict[str, object] | str:
        """
        Get QuickConnect hostname settings.

        Returns
        -------
        dict[str, object] or str
            Result of the quickconnect hostname get operation.
        """
        api_name = 'SYNO.Core.QuickConnect.Hostname'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_register_site_get(self) -> dict[str, object] | str:
        """
        Get QuickConnect registration site info.

        Returns
        -------
        dict[str, object] or str
            Result of the quickconnect register site get operation.
        """
        api_name = 'SYNO.Core.QuickConnect.RegisterSite'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_sni_get(self) -> dict[str, object] | str:
        """
        Get QuickConnect SNI settings.

        Returns
        -------
        dict[str, object] or str
            Result of the quickconnect sni get operation.
        """
        api_name = 'SYNO.Core.QuickConnect.SNI'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def quickconnect_upnp_get(self) -> dict[str, object] | str:
        """
        Get QuickConnect UPnP settings.

        Returns
        -------
        dict[str, object] or str
            Result of the quickconnect upnp get operation.
        """
        api_name = 'SYNO.Core.QuickConnect.Upnp'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.QuickStart
    # ------------------------------------------------------------------

    def quickstart_info_get(self) -> dict[str, object] | str:
        """
        Get quick start wizard information.

        Returns
        -------
        dict[str, object] or str
            Result of the quickstart info get operation.
        """
        api_name = 'SYNO.Core.QuickStart.Info'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def quickstart_install(self, **kwargs) -> dict[str, object] | str:
        """
        Run quick start installation.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the install operation.

        Returns
        -------
        dict[str, object] or str
            Result of the quickstart install operation.
        """
        api_name = 'SYNO.Core.QuickStart.Install'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'start'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Report
    # ------------------------------------------------------------------

    def report_get(self) -> dict[str, object] | str:
        """
        Get report settings.

        Returns
        -------
        dict[str, object] or str
            Result of the report get operation.
        """
        api_name = 'SYNO.Core.Report'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_get(self) -> dict[str, object] | str:
        """
        Get report analyzer settings.

        Returns
        -------
        dict[str, object] or str
            Result of the report analyzer get operation.
        """
        api_name = 'SYNO.Core.Report.Analyzer'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_file_get(self) -> dict[str, object] | str:
        """
        Get report analyzer file info.

        Returns
        -------
        dict[str, object] or str
            Result of the report analyzer file get operation.
        """
        api_name = 'SYNO.Core.Report.Analyzer.File'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_analyzer_share_get(self) -> dict[str, object] | str:
        """
        Get report analyzer share info.

        Returns
        -------
        dict[str, object] or str
            Result of the report analyzer share get operation.
        """
        api_name = 'SYNO.Core.Report.Analyzer.Share'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_config_get(self) -> dict[str, object] | str:
        """
        Get report configuration.

        Returns
        -------
        dict[str, object] or str
            Result of the report config get operation.
        """
        api_name = 'SYNO.Core.Report.Config'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_config_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set report configuration.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the report config set operation.
        """
        api_name = 'SYNO.Core.Report.Config'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def report_history_get(self) -> dict[str, object] | str:
        """
        Get report history.

        Returns
        -------
        dict[str, object] or str
            Result of the report history get operation.
        """
        api_name = 'SYNO.Core.Report.History'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_redirect_get(self) -> dict[str, object] | str:
        """
        Get report redirect settings.

        Returns
        -------
        dict[str, object] or str
            Result of the report redirect get operation.
        """
        api_name = 'SYNO.Core.Report.Redirect'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def report_util_get(self) -> dict[str, object] | str:
        """
        Get report utility information.

        Returns
        -------
        dict[str, object] or str
            Result of the report util get operation.
        """
        api_name = 'SYNO.Core.Report.Util'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.ResetAdmin
    # ------------------------------------------------------------------

    def reset_admin_get(self) -> dict[str, object] | str:
        """
        Get admin reset status.

        Returns
        -------
        dict[str, object] or str
            Result of the reset admin get operation.
        """
        api_name = 'SYNO.Core.ResetAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SecurityScan.Operation
    # ------------------------------------------------------------------

    def security_scan_operation_start(self) -> dict[str, object] | str:
        """
        Start a security scan.

        Returns
        -------
        dict[str, object] or str
            Result of the security scan operation start operation.
        """
        api_name = 'SYNO.Core.SecurityScan.Operation'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'start'})

    def security_scan_operation_get(self) -> dict[str, object] | str:
        """
        Get security scan operation status.

        Returns
        -------
        dict[str, object] or str
            Result of the security scan operation get operation.
        """
        api_name = 'SYNO.Core.SecurityScan.Operation'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Service extras
    # ------------------------------------------------------------------

    def service_conf_get(self) -> dict[str, object] | str:
        """
        Get service configuration.

        Returns
        -------
        dict[str, object] or str
            Result of the service conf get operation.
        """
        api_name = 'SYNO.Core.Service.Conf'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def service_conf_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set service configuration.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the service conf set operation.
        """
        api_name = 'SYNO.Core.Service.Conf'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def service_port_info_get(self) -> dict[str, object] | str:
        """
        Get service port information.

        Returns
        -------
        dict[str, object] or str
            Result of the service port info get operation.
        """
        api_name = 'SYNO.Core.Service.PortInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Share extras (Crypto, KeyManager, Migration, Permission)
    # ------------------------------------------------------------------

    def share_crypto_get(self) -> dict[str, object] | str:
        """
        Get shared folder encryption settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share crypto get operation.
        """
        api_name = 'SYNO.Core.Share.Crypto'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_crypto_key_get(self) -> dict[str, object] | str:
        """
        Get shared folder encryption key info.

        Returns
        -------
        dict[str, object] or str
            Result of the share crypto key get operation.
        """
        api_name = 'SYNO.Core.Share.Crypto.Key'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_crypto_file_get(self) -> dict[str, object] | str:
        """
        Get encrypted shared folder file settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share crypto file get operation.
        """
        api_name = 'SYNO.Core.Share.CryptoFile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_auto_key_get(self) -> dict[str, object] | str:
        """
        Get key manager auto-key settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share key manager auto key get operation.
        """
        api_name = 'SYNO.Core.Share.KeyManager.AutoKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_key_get(self) -> dict[str, object] | str:
        """
        Get key manager key settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share key manager key get operation.
        """
        api_name = 'SYNO.Core.Share.KeyManager.Key'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_machine_key_get(self) -> dict[str, object] | str:
        """
        Get key manager machine key settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share key manager machine key get operation.
        """
        api_name = 'SYNO.Core.Share.KeyManager.MachineKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_key_manager_store_get(self) -> dict[str, object] | str:
        """
        Get key manager store settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share key manager store get operation.
        """
        api_name = 'SYNO.Core.Share.KeyManager.Store'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_migration_get(self) -> dict[str, object] | str:
        """
        Get shared folder migration status.

        Returns
        -------
        dict[str, object] or str
            Result of the share migration get operation.
        """
        api_name = 'SYNO.Core.Share.Migration'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_migration_task_get(self) -> dict[str, object] | str:
        """
        Get shared folder migration task status.

        Returns
        -------
        dict[str, object] or str
            Result of the share migration task get operation.
        """
        api_name = 'SYNO.Core.Share.Migration.Task'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_permission_get(self, name: str) -> dict[str, object] | str:
        """
        Get permissions for a shared folder.

        Parameters
        ----------
        name : str
            The name value.

        Returns
        -------
        dict[str, object] or str
            Result of the share permission get operation.
        """
        api_name = 'SYNO.Core.Share.Permission'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'name': name})

    def share_permission_set(self, name: str, permissions: dict) -> dict[str, object] | str:
        """
        Set permissions for a shared folder.

        Parameters
        ----------
        name : str
            The name value.
        permissions : dict
            The permissions value.

        Returns
        -------
        dict[str, object] or str
            Result of the share permission set operation.
        """
        api_name = 'SYNO.Core.Share.Permission'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'name': name, 'user_group_type_list': json.dumps(permissions)})

    def share_permission_report_get(self) -> dict[str, object] | str:
        """
        Get shared folder permission report.

        Returns
        -------
        dict[str, object] or str
            Result of the share permission report get operation.
        """
        api_name = 'SYNO.Core.Share.PermissionReport'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def share_shell_file_get(self) -> dict[str, object] | str:
        """
        Get shared folder shell file settings.

        Returns
        -------
        dict[str, object] or str
            Result of the share shell file get operation.
        """
        api_name = 'SYNO.Core.Share.ShellFile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Sharing
    # ------------------------------------------------------------------

    def sharing_get(self) -> dict[str, object] | str:
        """
        Get file sharing settings.

        Returns
        -------
        dict[str, object] or str
            Result of the sharing get operation.
        """
        api_name = 'SYNO.Core.Sharing'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def sharing_initdata_get(self) -> dict[str, object] | str:
        """
        Get sharing initialization data.

        Returns
        -------
        dict[str, object] or str
            Result of the sharing initdata get operation.
        """
        api_name = 'SYNO.Core.Sharing.Initdata'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def sharing_login(self, sharing_id: str, password: Optional[str] = None) -> dict[str, object] | str:
        """
        Login to a file sharing link.

        Parameters
        ----------
        sharing_id : str
            The sharing id value.
        password : str, optional
            The password value.

        Returns
        -------
        dict[str, object] or str
            Result of the sharing login operation.
        """
        api_name = 'SYNO.Core.Sharing.Login'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'login',
                     'sharing_id': sharing_id}
        if password:
            req_param['password'] = password
        return self.request_data(api_name, info['path'], req_param)

    def sharing_session_get(self) -> dict[str, object] | str:
        """
        Get sharing session information.

        Returns
        -------
        dict[str, object] or str
            Result of the sharing session get operation.
        """
        api_name = 'SYNO.Core.Sharing.Session'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SupportForm
    # ------------------------------------------------------------------

    def support_form_get(self) -> dict[str, object] | str:
        """
        Get support form configuration.

        Returns
        -------
        dict[str, object] or str
            Result of the support form get operation.
        """
        api_name = 'SYNO.Core.SupportForm.Form'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def support_form_log_get(self) -> dict[str, object] | str:
        """
        Get support form submission log.

        Returns
        -------
        dict[str, object] or str
            Result of the support form log get operation.
        """
        api_name = 'SYNO.Core.SupportForm.Log'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def support_form_service_get(self) -> dict[str, object] | str:
        """
        Get support form service status.

        Returns
        -------
        dict[str, object] or str
            Result of the support form service get operation.
        """
        api_name = 'SYNO.Core.SupportForm.Service'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Synohdpack
    # ------------------------------------------------------------------

    def synohdpack_get(self) -> dict[str, object] | str:
        """
        Get Synology HD pack information.

        Returns
        -------
        dict[str, object] or str
            Result of the synohdpack get operation.
        """
        api_name = 'SYNO.Core.Synohdpack'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.SyslogClient.PersonalActivity
    # ------------------------------------------------------------------

    def syslog_personal_activity_get(self) -> dict[str, object] | str:
        """
        Get personal activity syslog settings.

        Returns
        -------
        dict[str, object] or str
            Result of the syslog personal activity get operation.
        """
        api_name = 'SYNO.Core.SyslogClient.PersonalActivity'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Tuned
    # ------------------------------------------------------------------

    def tuned_get(self) -> dict[str, object] | str:
        """
        Get system tuning (tuned) settings.

        Returns
        -------
        dict[str, object] or str
            Result of the tuned get operation.
        """
        api_name = 'SYNO.Core.Tuned'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def tuned_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set system tuning settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the tuned set operation.
        """
        api_name = 'SYNO.Core.Tuned'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.User extras
    # ------------------------------------------------------------------

    def user_group_get(self, user: str) -> dict[str, object] | str:
        """
        Get groups a user belongs to.

        Parameters
        ----------
        user : str
            The user value.

        Returns
        -------
        dict[str, object] or str
            Result of the user group get operation.
        """
        api_name = 'SYNO.Core.User.Group'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'name': user})

    def user_password_expiry_get(self) -> dict[str, object] | str:
        """
        Get password expiry settings.

        Returns
        -------
        dict[str, object] or str
            Result of the user password expiry get operation.
        """
        api_name = 'SYNO.Core.User.PasswordExpiry'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def user_password_meter_get(self, password: str) -> dict[str, object] | str:
        """
        Check password strength.

        Parameters
        ----------
        password : str
            The password value.

        Returns
        -------
        dict[str, object] or str
            Result of the user password meter get operation.
        """
        api_name = 'SYNO.Core.User.PasswordMeter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get',
                                  'password': password}, method='post')

    def user_password_policy_get(self) -> dict[str, object] | str:
        """
        Get password policy settings.

        Returns
        -------
        dict[str, object] or str
            Result of the user password policy get operation.
        """
        api_name = 'SYNO.Core.User.PasswordPolicy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def user_password_policy_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set password policy settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the user password policy set operation.
        """
        api_name = 'SYNO.Core.User.PasswordPolicy'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def user_username_policy_get(self) -> dict[str, object] | str:
        """
        Get username policy settings.

        Returns
        -------
        dict[str, object] or str
            Result of the user username policy get operation.
        """
        api_name = 'SYNO.Core.User.UsernamePolicy'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Virtualization.Host.Capability
    # ------------------------------------------------------------------

    def virtualization_host_capability_get(self) -> dict[str, object] | str:
        """
        Get virtualization host capability information.

        Returns
        -------
        dict[str, object] or str
            Result of the virtualization host capability get operation.
        """
        api_name = 'SYNO.Core.Virtualization.Host.Capability'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.VolEncKeepKey
    # ------------------------------------------------------------------

    def vol_enc_keep_key_get(self) -> dict[str, object] | str:
        """
        Get volume encryption keep-key settings.

        Returns
        -------
        dict[str, object] or str
            Result of the vol enc keep key get operation.
        """
        api_name = 'SYNO.Core.VolEncKeepKey'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def vol_enc_keep_key_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set volume encryption keep-key settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the vol enc keep key set operation.
        """
        api_name = 'SYNO.Core.VolEncKeepKey'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Web extras
    # ------------------------------------------------------------------

    def web_dsm_external_get(self) -> dict[str, object] | str:
        """
        Get DSM external web access settings.

        Returns
        -------
        dict[str, object] or str
            Result of the web dsm external get operation.
        """
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def web_dsm_external_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set DSM external web access settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the web dsm external set operation.
        """
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def web_security_http_compression_get(self) -> dict[str, object] | str:
        """
        Get HTTP compression settings.

        Returns
        -------
        dict[str, object] or str
            Result of the web security http compression get operation.
        """
        api_name = 'SYNO.Core.Web.Security.HTTPCompression'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def web_security_http_compression_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set HTTP compression settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the web security http compression set operation.
        """
        api_name = 'SYNO.Core.Web.Security.HTTPCompression'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def web_security_tls_profile_get(self) -> dict[str, object] | str:
        """
        Get TLS profile settings.

        Returns
        -------
        dict[str, object] or str
            Result of the web security tls profile get operation.
        """
        api_name = 'SYNO.Core.Web.Security.TLSProfile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def web_security_tls_profile_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set TLS profile settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the web security tls profile set operation.
        """
        api_name = 'SYNO.Core.Web.Security.TLSProfile'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)
