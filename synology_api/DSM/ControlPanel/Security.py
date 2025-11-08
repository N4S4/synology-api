"""
Security class for Synology DSM.
"""
from synology_api import base_api
import json


class Security(base_api.BaseApi):
    """
    Security class for Synology DSM.
    """

    def get_security_settings(self) -> dict:
        """
        Get security settings, Security tab: General, Login Settings.

        Returns
        -------
        dict
            Security settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "allow_stay_signed_in_option": true,
                "allow_trust_device_2fa_option": true,
                "csp_header_option": true,
                "enable_csrf_protection": true,
                "restart_clean_session": true,
                "skip_ip_checking": true,
                "timeout": 15
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Security.DSM'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_dsm_embedded_settings(self) -> dict:
        """
        Get DSM embedded settings.

        Returns
        -------
        dict
            DSM embedded settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_block": true,
                "whitelist": [
                    "find.synology.com/",
                    "gofile.me/"
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Security.DSM.Embed'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_2fa_settings(self) -> dict:
        """
        Get 2-factor authentication settings, Account tab: 2-factor authentication.

        Returns
        -------
        dict
            2-factor authentication settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "otp_enforce_option": "custom"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.OTP.EnforcePolicy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_amfa_settings(self) -> dict:
        """
        Get AMFA (Adaptive Multi-Factor Authentication) settings, Account tab: Adaptive multi-factor authentication.

        Returns
        -------
        dict
            AMFA settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "group_list": "",
                "type": "admin",
                "user_list": ""
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.SecureSignIn.AMFA.Policy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_smartblock_settings(self) -> dict:
        """
        Get Smart Block settings, Login Settings tab: Smart Block.

        Returns
        -------
        dict
            Smart Block settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "enabled": true,
                "trust_lock": 30,
                "trust_minute": 1,
                "trust_try": 10,
                "untrust_lock": 30,
                "untrust_minute": 1,
                "untrust_try": 5
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.SmartBlock'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_firewall_status(self) -> dict:
        """
        Get firewall status, Firewall tab: Enable firewall.

        Returns
        -------
        dict
            Firewall status information.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_firewall": true,
                "profile_name": "default"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Security.Firewall'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_firewall_notifications_settings(self) -> dict:
        """
        Get firewall notifications settings, Firewall tab: Enable firewall notifications.

        Returns
        -------
        dict
            Firewall notifications settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_port_check": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Security.Firewall.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_auto_block_settings(self) -> dict:
        """
        Get auto block settings, Auto Block tab: Enable auto block.

        Returns
        -------
        dict
            Auto block settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "attempts": 10,
                "enable": true,
                "expire_day": 0,
                "within_mins": 5
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Security.AutoBlock'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_dos_settings(self, adapter_list: list[str]) -> dict:
        """
        Get DoS settings, Protect tab: Denial-of-Service (DoS) Protection.

        Parameters
        ----------
        adapter_list : list[str]
            List of network interfaces to get DoS settings for. Can be obtained via `Network.get_network_interface()` and get `ifname` from the response.

        Returns
        -------
        dict
            DoS settings information.

        Examples
        --------
        ```json
        {
            "data": [
                {
                    "adapter": "ovs_eth0",
                    "dos_protect_enable": true
                },
                {
                    "adapter": "ovs_eth1",
                    "dos_protect_enable": false
                },
                {
                    "adapter": "pppoe",
                    "dos_protect_enable": false
                }
            ],
            "success": true
        }
        ```
        """
        configs = [{"adapter": adapter} for adapter in adapter_list]

        api_name = 'SYNO.Core.Security.DoS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'configs': json.dumps(configs)
        }

        return self.request_data(api_name, api_path, req_param)

    def get_http_compression_settings(self) -> dict:
        """
        Get HTTP compression settings, Advanced tab: HTTP compression.

        Returns
        -------
        dict
            HTTP compression settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "http_compression": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Web.Security.HTTPCompression'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_tls_profile_settings(self) -> dict:
        """
        Get TLS profile settings, Advanced tab: TLS / SSL Profile level.

        Returns
        -------
        dict
            TLS profile settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "default-level": 1,
                "services": {
                    "LogCenter": {
                        "current-level": 0,
                        "display-name": "Log Receiving",
                        "display-name-i18n": "helptoc:logcenter_server"
                    },
                    "WebStation_4437801d-caf5-45d6-afbd-99fc2f9f91dc": {
                        "current-level": 0,
                        "display-name": "*:8080"
                    },
                    "dsm": {
                        "current-level": 0,
                        "display-name": "DSM Desktop Service",
                        "display-name-i18n": "common:web_desktop"
                    },
                    "openldap": {
                        "current-level": 0,
                        "display-name": "LDAP Server"
                    },
                    "smbftpd": {
                        "current-level": 0,
                        "display-name": "FTPS",
                        "display-name-i18n": "tree:leaf_ftpes"
                    },
                    "system_quickconnect": {
                        "current-level": 0,
                        "display-name": "QuickConnect",
                        "display-name-i18n": "helptoc:quickconnect"
                    }
                }
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Web.Security.TLSProfile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_spectre_meldown_settings(self) -> dict:
        """
        Get Spectre/Meltdown settings, Advanced tab: Spectre/Meltdown Protection.

        Returns
        -------
        dict
            Spectre/Meltdown settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_spectre_meltdown_mitigation": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.SpectreMeltdown'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_kmip_settings(self) -> dict:
        """
        Get KMIP settings, KMIP tab.

        Returns
        -------
        dict
            KMIP settings information.

        Examples
        --------
        ```json
        {
            "data": {
                "client_cert_info": null,
                "client_enable": false,
                "conn_success": false,
                "conn_time": "",
                "kmip_conn_server_desc": "",
                "kmip_conn_server_port": "5696",
                "kmip_db_loc": "",
                "kmip_enabled": "",
                "kmip_mode": "",
                "kmip_server": "",
                "kmip_server_port": "5696",
                "server_cert_info": null,
                "server_enable": false,
                "support_kmip": "yes"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Storage.CGI.KMIP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
