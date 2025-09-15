"""
Login portal class for Synology DSM.
"""
from synology_api import base_api
import json


class LoginPortal(base_api.BaseApi):
    """
    Login portal class for Synology DSM.
    """

    def get_dsm_web_service_info(self) -> dict:
        """
        Get the web status of the login portal.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_avahi": true,
                "enable_custom_domain": false,
                "enable_hsts": false,
                "enable_https_redirect": false,
                "enable_max_connections": false,
                "enable_reuseport": false,
                "enable_server_header": true,
                "enable_spdy": true,
                "enable_ssdp": true,
                "fqdn": null,
                "http_port": 5000,
                "https_port": 5001,
                "main_app": "DSM",
                "max_connections": 2048,
                "max_connections_limit": {
                    "lower": 2048,
                    "upper": 131070
                },
                "server_header": "nginx",
                "support_reuseport": true
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Web.DSM"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "get",
        }
        return self.request_data(api_name, api_path, req_param)

    def list_app_portal(self, additionnal: list = []) -> dict:
        """
        List application portals.

        Parameters
        ----------
        additionnal : list, optional
            Additional fields to include in the response, by default []. Possible values are "default_setting".

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "portal": [
                {
                    "display_name": "Active Backup for Microsoft 365 Portal",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.ActiveBackupOffice365.Portal.Instance"
                },
                {
                    "display_name": "Synology Calendar",
                    "enable_redirect": false,
                    "id": "SYNO.Cal.Application"
                },
                {
                    "display_name": "Synology Contacts",
                    "enable_redirect": false,
                    "id": "SYNO.Contacts.AppInstance"
                },
                {
                    "display_name": "Download Station",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.DownloadStation.Application"
                },
                {
                    "display_name": "File Station",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.App.FileStation3.Instance"
                },
                {
                    "display_name": "Note Station",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.NoteStation.Application"
                },
                {
                    "acl": null,
                    "alias": "cam",
                    "display_name": "Surveillance Station",
                    "enable_redirect": false,
                    "fqdn": null,
                    "hsts": false,
                    "http_port": 9900,
                    "id": "SYNO.SDS.SurveillanceStation"
                },
                {
                    "display_name": "Synology Drive",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.SheetStation.Application"
                },
                {
                    "display_name": "Virtual Machine Manager",
                    "enable_redirect": false,
                    "id": "SYNO.SDS.Virtualization.Application"
                }
                ]
            },
            "success": true
            }
            ```
        """
        api_name = "SYNO.Core.AppPortal"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "list",
            "additional": json.dumps(additionnal),
        }
        return self.request_data(api_name, api_path, req_param)

    def list_reverse_proxy(self) -> dict:
        """
        List reverse proxy rules.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "entries": []
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.ReverseProxy"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "list",
        }
        return self.request_data(api_name, api_path, req_param)

    def list_access_control(self) -> dict:
        """
        List access control rules.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "entries": [
                {
                    "UUID": "4d0b7d3d-d8a5-4b91-a160-efd45703005f",
                    "name": "test",
                    "rules": [
                    {
                        "access": true,
                        "address": "127.0.0.1"
                    }
                    ]
                }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.AccessControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "list",
        }
        return self.request_data(api_name, api_path, req_param)

    def get_login_theme(self) -> dict:
        """
        Get the current login theme.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "background_color": "#FFFFFF",
                "background_position": "fill",
                "background_seq": 0,
                "enable_background_customize": false,
                "enable_logo_customize": false,
                "login_footer_enable_html": false,
                "login_title": "",
                "login_version_logo": false,
                "logo_position": "center",
                "logo_seq": 0,
                "only_background_color": false,
                "weather_info": "display"
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Theme.Login"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "get",
        }
        return self.request_data(api_name, api_path, req_param)

    def get_app_theme(self, app_id: str) -> dict:
        """
        Get the theme for a specific application.

        Parameters
        ----------
        app_id : str
            The ID of the application. The app_id can be found in the `list_app_portal()` returns.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "background_color": "#FFFFFF",
            "background_position": "fill",
            "background_seq": 0,
            "enable_background_customize": false,
            "enable_logo_customize": false,
            "from_dsm": true,
            "login_footer_enable_html": false,
            "login_title": "",
            "login_version_logo": false,
            "logo_position": "center",
            "logo_seq": 0,
            "only_background_color": false,
            "weather_info": "display"
        }
        ```
        """
        api_name = "SYNO.Core.Theme.AppPortalLogin"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "get",
            "app": app_id,
        }
        return self.request_data(api_name, api_path, req_param)

    def set_dsm_web_service_info(self,
                                 enable_custom_domain: bool, enable_avahi: bool, enable_hsts: bool, enable_https_redirect: bool,
                                 enable_max_connections: bool, enable_reuseport: bool, enable_server_header: bool, enable_spdy: bool,
                                 enable_ssdp: bool, fqdn: str = "", http_port: int = 5000, https_port: int = 5001, main_app: str = "DSM", max_connections: int = 2048,
                                 max_connections_limit: dict = {"lower": 2048, "upper": 131070}, server_header: str = "nginx", support_reuseport: bool = True
                                 ) -> dict:
        """
        Set the web service information for DSM. Note that this will likely restart the web service.

        Parameters
        ----------
        enable_custom_domain : bool
            Enable custom domain.
        enable_avahi : bool
            Enable Avahi (mDNS) support.
        enable_hsts : bool
            Enable HTTP Strict Transport Security (HSTS).
        enable_https_redirect : bool
            Enable HTTPS redirection.
        enable_max_connections : bool
            Enable maximum connections limit.
        enable_reuseport : bool
            Enable SO_REUSEPORT option.
        enable_server_header : bool
            Enable server header in responses.
        enable_spdy : bool
            Enable SPDY protocol support.
        enable_ssdp : bool
            Enable SSDP support.
        fqdn : str, optional
            Fully qualified domain name, by default "".
        http_port : int, optional
            HTTP port number, by default 5000.
        https_port : int, optional
            HTTPS port number, by default 5001.
        main_app : str, optional
            Main application to launch on login, by default "DSM".
        max_connections : int, optional
            Maximum number of connections, by default 2048.
        max_connections_limit : dict, optional
            Dictionary with 'lower' and 'upper' keys for max connections limit, by default {"lower": 2048, "upper": 131070}.
        server_header : str, optional
            Server header string, by default "nginx".
        support_reuseport : bool, optional
            Whether SO_REUSEPORT is supported, by default True.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Web.DSM"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "set",
            "enable_custom_domain": enable_custom_domain,
            "enable_avahi": enable_avahi,
            "enable_hsts": enable_hsts,
            "enable_https_redirect": enable_https_redirect,
            "enable_max_connections": enable_max_connections,
            "enable_reuseport": enable_reuseport,
            "enable_server_header": enable_server_header,
            "enable_spdy": enable_spdy,
            "enable_ssdp": enable_ssdp,
            "fqdn": fqdn,
            "http_port": http_port,
            "https_port": https_port,
            "main_app": main_app,
            "max_connections": max_connections,
            "max_connections_limit": json.dumps(max_connections_limit),
            "server_header": server_header,
            "support_reuseport": support_reuseport
        }
        return self.request_data(api_name, api_path, req_param)

    def set_login_theme(self,
                        background_color: str = "#FFFFFF", background_position: str = "fill", background_seq: int = 0,
                        enable_background_customize: bool = False, enable_logo_customize: bool = False,
                        login_footer_enable_html: bool = False, login_title: str = "", login_version_logo: bool = False,
                        logo_position: str = "center", logo_seq: int = 0, only_background_color: bool = False,
                        weather_info: str = "display"
                        ) -> dict:
        """
        Set the login theme for DSM.

        Parameters
        ----------
        background_color : str, optional
            Background color in HEX format, by default "#FFFFFF".
        background_position : str, optional
            Background image position, by default "fill". Possible values are "fill", "fit", "stretch", "center", "tile".
        background_seq : int, optional
            Background image sequence number, by default 0.
        enable_background_customize : bool, optional
            Enable custom background image, by default False.
        enable_logo_customize : bool, optional
            Enable custom logo image, by default False.
        login_footer_enable_html : bool, optional
            Enable HTML in the login footer, by default False.
        login_title : str, optional
            Custom login title text, by default "".
        login_version_logo : bool, optional
            Show DSM version logo on the login page, by default False.
        logo_position : str, optional
            Logo image position, by default "center". Possible values are "left", "center", "right".
        logo_seq : int, optional
            Logo image sequence number, by default 0.
        only_background_color : bool, optional
            Use only background color without image, by default False.
        weather_info : str, optional
            Weather information display option, by default "display". Possible values are "display", "hide".

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Theme.Login"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "set",
            "background_color": background_color,
            "background_position": background_position,
            "background_seq": background_seq,
            "enable_background_customize": enable_background_customize,
            "enable_logo_customize": enable_logo_customize,
            "login_footer_enable_html": login_footer_enable_html,
            "login_title": login_title,
            "login_version_logo": login_version_logo,
            "logo_position": logo_position,
            "logo_seq": logo_seq,
            "only_background_color": only_background_color,
            "weather_info": weather_info
        }
        return self.request_data(api_name, api_path, req_param)

    def get_config(self) -> dict:
        """
        Get the login portal configuration.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "data": {
                "show_titlebar": true
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.Config"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "get",
        }
        return self.request_data(api_name, api_path, req_param)

    def set_config(self, show_titlebar: bool) -> dict:
        """
        Set the login portal configuration.

        Parameters
        ----------
        show_titlebar : bool
            Whether to show the title bar on the login portal.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.Config"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "set",
            "show_titlebar": show_titlebar
        }
        return self.request_data(api_name, api_path, req_param)

    def create_access_control_profile(self, name: str, rules: list) -> dict:
        """
        Create an access control profile.

        Parameters
        ----------
        name : str
            Name of the access control profile.
        rules : list
            List of rules for the access control profile. Each rule is a dictionary with keys:
            - action: "allow" or "deny"
            - source: source IP or subnet in CIDR notation
            - protocol: "http", "https", or "both"
            - port: port number or range (e.g., "80", "443", "8000-9000")

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.AccessControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "create",
            "name": name,
            "rules": json.dumps(rules)
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_access_control_profile(self, uuid: str, name: str, rules: list) -> dict:
        """
        Edit an existing access control profile.

        Parameters
        ----------
        uuid : str
            UUID of the access control profile to edit. The UUID can be found in the `list_access_control()` returns.
        name : str
            New name for the access control profile.
        rules : list
            New list of rules for the access control profile. Each rule is a dictionary with keys:
            - address : str (source IP or subnet in CIDR notation)
            - access : bool (True for allow, False for deny)

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.AccessControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "edit",
            "uuid": uuid,
            "name": name,
            "rules": json.dumps(rules)
        }
        return self.request_data(api_name, api_path, req_param)

    def delete_access_control_profile(self, uuids: list) -> dict:
        """
        Delete one or more access control profiles.

        Parameters
        ----------
        uuids : list
            List of UUIDs of the access control profiles to delete.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.AccessControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "delete",
            "uuids": json.dumps(uuids)
        }
        return self.request_data(api_name, api_path, req_param)

    def create_reverse_proxy_rule(self, entry: dict) -> dict:
        """
        Create a reverse proxy rule.

        Parameters
        ----------
        entry : dict
            The reverse proxy rule configuration. Example:
            {
                "description": "yrdy",
                "proxy_connect_timeout": 60,
                "proxy_read_timeout": 60,
                "proxy_send_timeout": 60,
                "proxy_http_version": 1,
                "proxy_intercept_errors": False,
                "frontend": {
                    "acl": None,
                    "fqdn": None,
                    "port": 8000,
                    "protocol": 0,
                    "https": {"hsts": False}
                },
                "backend": {
                    "fqdn": "localhost",
                    "port": 8080,
                    "protocol": 0
                },
                "customize_headers": [
                    {"name": "yoyo", "value": "test"}
                ]
            }

        Returns
        -------
        dict
            Success response from the API.

        Examples
        --------
        ```json
        {
            'success': True
        }
        ```
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1,
            'method': 'create',
            'entry': json.dumps(entry)
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_reverse_proxy_rule(self, entry: dict) -> dict:
        """
        Edit a reverse proxy rule.

        Parameters
        ----------
        entry : dict
            The reverse proxy rule configuration, including UUID and _key. Example:
            {
                "description": "yrdy",
                "proxy_connect_timeout": 60,
                "proxy_read_timeout": 60,
                "proxy_send_timeout": 60,
                "proxy_http_version": 1,
                "proxy_intercept_errors": False,
                "UUID": "91dbcc5b-2467-4047-996c-2b5beb4fbefa",
                "backend": {
                    "fqdn": "localhost",
                    "port": 8080,
                    "protocol": 0
                },
                "customize_headers": [
                    {"name": "yoyo", "value": "test"}
                ],
                "frontend": {
                    "acl": None,
                    "fqdn": None,
                    "port": 8000,
                    "protocol": 0,
                    "https": {"hsts": False}
                }
            }

        Returns
        -------
        dict
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        ```
        """
        api_name = 'SYNO.Core.AppPortal.ReverseProxy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1,
            'method': 'update',
            'entry': json.dumps(entry)
        }
        return self.request_data(api_name, api_path, req_param)

    def delete_reverse_proxy_rule(self, uuids: list) -> dict:
        """
        Delete one or more reverse proxy rules.

        Parameters
        ----------
        uuids : list
            List of UUIDs of the reverse proxy rules to delete.

        Returns
        -------
        dict
            The response from the API call.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.AppPortal.ReverseProxy"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "delete",
            "uuids": json.dumps(uuids)
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_app_portal(self, id: str, display_name: str, additional: dict, enable_custom_domain: bool = False,
                        acl: str = None, fqdn: str = None, enable_redirect: bool = False) -> dict:
        """
        Edit (set) an app portal.

        Parameters
        ----------
        id : str
            The app portal instance ID.
        display_name : str
            The display name for the portal.
        additional : dict
            Additional settings, e.g.:
            {
                "default_setting": {
                    "alias": "microsoft365",
                    "fqdn": "",
                    "hsts": False,
                    "http_port": 28003,
                    "https_port": 28004
                }
            }
        enable_custom_domain : bool, optional
            Enable custom domain. Default is False.
        acl : str, optional
            Access control profile uuid. Default is None.
        fqdn : str, optional
            Fully qualified domain name. Default is None.
        enable_redirect : bool, optional
            Enable redirect. Default is False.

        Returns
        -------
        dict
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        ```
        """
        api_name = 'SYNO.Core.AppPortal'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 2,
            'method': 'set',
            'id': id,
            'display_name': display_name,
            'additional': json.dumps(additional),
            'enable_custom_domain': enable_custom_domain,
            'acl': acl,
            'fqdn': fqdn,
            'enable_redirect': enable_redirect
        }
        return self.request_data(api_name, api_path, req_param)
