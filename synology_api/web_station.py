"""
Synology Web Station API wrapper.

Wraps the SYNO.WebStation.* APIs for managing web server
virtual hosts, PHP/Python profiles, portals, and services
on DSM 7.x+.

Requires Web Station package installed on the target NAS.

API endpoints
~~~~~~~~~~~~~
- SYNO.WebStation.Status      -- Web Station status
- SYNO.WebStation.Default      -- Default server settings
- SYNO.WebStation.HTTP.VHost   -- Virtual host management
- SYNO.WebStation.PHP.*        -- PHP configuration & profiles
- SYNO.WebStation.Python.*     -- Python configuration & profiles
- SYNO.WebStation.ErrorPage    -- Custom error pages
- SYNO.WebStation.WebService.Portal -- Portal management
- SYNO.WebStation.WebService.Service -- Service management
- SYNO.WebStation.Package      -- Package web settings
- SYNO.WebStation.Shortcut     -- URL shortcuts
- SYNO.WebStation.Task         -- Background tasks
"""

from __future__ import annotations

from typing import Any

from synology_api.base_api import BaseApi


class WebStation(BaseApi):
    """
    Synology Web Station API client.

    Manages Web Station virtual hosts, PHP/Python runtimes,
    web service portals, error pages, URL shortcuts, and
    background tasks via the SYNO.WebStation.* WebAPI
    endpoints.

    Requires Web Station package installed on the target NAS.

    Parameters
    ----------
    ip_address : str
        NAS IP address (e.g. ``"192.168.1.2"``).
    port : str
        NAS web interface port (e.g. ``"5001"``).
    username : str
        DSM user account name.
    password : str
        DSM user account password.
    secure : bool, optional
        Use HTTPS instead of HTTP (default True).
    cert_verify : bool, optional
        Verify SSL certificates (default False).
    dsm_version : int, optional
        DSM major version (default 7).
    debug : bool, optional
        Enable debug output (default True).
    otp_code : str, optional
        One-time password for 2FA login.
    device_id : str, optional
        Device ID for login session binding.
    device_name : str, optional
        Device name for login session binding.
    interactive_output : bool, optional
        Format output for interactive terminal use (default False).
    """

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Status — Status
    # ═══════════════════════════════════════════════════════════════════════

    def ws_status(self) -> dict[str, object] | str:
        """
        Get Web Station status and backend information.

        Returns
        -------
        dict[str, object] or str
            Status including available backends (PHP, Python,
            server), current backend, home share, and
            web service configuration.

        Examples
        --------
            >>> ws.ws_status()
        """
        api_name = "SYNO.WebStation.Status"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Default — Default Server
    # ═══════════════════════════════════════════════════════════════════════

    def ws_default(self) -> dict[str, object] | str:
        """
        Get default web server configuration.

        Returns
        -------
        dict[str, object] or str
            Default backend server, PHP settings, and
            user directory configuration.

        Examples
        --------
            >>> ws.ws_default()
        """
        api_name = "SYNO.WebStation.Default"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.HTTP.VHost — Virtual Hosts
    # ═══════════════════════════════════════════════════════════════════════

    def ws_vhost_list(self) -> dict[str, object] | str:
        """
        List all virtual hosts.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"hosts": [...], "total": N}, "success": true}``.
            Each host includes name, document root, ports,
            and PHP backend.

        Examples
        --------
            >>> ws.ws_vhost_list()
        """
        api_name = "SYNO.WebStation.HTTP.VHost"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.PHP — PHP Configuration
    # ═══════════════════════════════════════════════════════════════════════

    def ws_php_info(self) -> dict[str, object] | str:
        """
        Get PHP configuration and available extensions.

        Returns
        -------
        dict[str, object] or str
            PHP metadata, default settings, and available
            PHP extensions list.

        Examples
        --------
            >>> ws.ws_php_info()
        """
        api_name = "SYNO.WebStation.PHP"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    def ws_php_profile_list(self) -> dict[str, object] | str:
        """
        List PHP profiles.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"profiles": [...], "total": N}, "success": true}``.
            Each profile includes version, extensions, and
            custom PHP settings.

        Examples
        --------
            >>> ws.ws_php_profile_list()
        """
        api_name = "SYNO.WebStation.PHP.Profile"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Python — Python Configuration
    # ═══════════════════════════════════════════════════════════════════════

    def ws_python_info(self) -> dict[str, object] | str:
        """
        Get Python configuration metadata.

        Returns
        -------
        dict[str, object] or str
            Python runtime metadata and available versions.

        Examples
        --------
            >>> ws.ws_python_info()
        """
        api_name = "SYNO.WebStation.Python"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    def ws_python_profile_list(self) -> dict[str, object] | str:
        """
        List Python profiles.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"profiles": [...], "total": N}, "success": true}``.
            Each profile includes Python version, virtualenv
            path, and WSGI configuration.

        Examples
        --------
            >>> ws.ws_python_profile_list()
        """
        api_name = "SYNO.WebStation.Python.Profile"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.ErrorPage — Custom Error Pages
    # ═══════════════════════════════════════════════════════════════════════

    def ws_error_page_list(self) -> dict[str, object] | str:
        """
        List custom error page profiles.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"profiles": [...]}, "success": true}``.

        Examples
        --------
            >>> ws.ws_error_page_list()
        """
        api_name = "SYNO.WebStation.ErrorPage"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.WebService.Portal — Portals
    # ═══════════════════════════════════════════════════════════════════════

    def ws_portal_list(self) -> dict[str, object] | str:
        """
        List web service portals.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"portals": [...]}, "success": true}``.
            Portals are the entry points that map hostnames
            and ports to web services.

        Examples
        --------
            >>> ws.ws_portal_list()
        """
        api_name = "SYNO.WebStation.WebService.Portal"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.WebService.Service — Services
    # ═══════════════════════════════════════════════════════════════════════

    def ws_service_list(self) -> dict[str, object] | str:
        """
        List web services.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"services": [...]}, "success": true}``.

        Examples
        --------
            >>> ws.ws_service_list()
        """
        api_name = "SYNO.WebStation.WebService.Service"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Package — Package Web Settings
    # ═══════════════════════════════════════════════════════════════════════

    def ws_package_list(self) -> dict[str, object] | str:
        """
        List packages with web service configuration.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"packages": [...]}, "success": true}``.

        Examples
        --------
            >>> ws.ws_package_list()
        """
        api_name = "SYNO.WebStation.Package"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Shortcut — URL Shortcuts
    # ═══════════════════════════════════════════════════════════════════════

    def ws_shortcut_list(self) -> dict[str, object] | str:
        """
        List URL shortcuts/redirects.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"shortcuts": [...]}, "success": true}``.

        Examples
        --------
            >>> ws.ws_shortcut_list()
        """
        api_name = "SYNO.WebStation.Shortcut"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.WebStation.Task — Background Tasks
    # ═══════════════════════════════════════════════════════════════════════

    def ws_task_list(self) -> dict[str, object] | str:
        """
        List Web Station background tasks.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"tasks": [...]}, "success": true}``.

        Examples
        --------
            >>> ws.ws_task_list()
        """
        api_name = "SYNO.WebStation.Task"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )
