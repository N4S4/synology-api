"""
Synology LDAP Server API wrapper.

Wraps the SYNO.Core.Directory.LDAP.* APIs for managing
the LDAP Server package on DSM 7.x+.

Requires LDAP Server package installed and configured
on the target NAS.

.. note::
   The LDAP Server API uses the ``SYNO.Core.Directory.LDAP``
   namespace, not ``SYNO.DirectoryServer`` (which is a separate
   Directory Server package API).

API endpoints
~~~~~~~~~~~~~
- SYNO.Core.Directory.LDAP           -- LDAP server configuration
- SYNO.Core.Directory.LDAP.BaseDN    -- Base DN management
- SYNO.Core.Directory.LDAP.Profile   -- LDAP profiles
- SYNO.Core.Directory.LDAP.User      -- LDAP user management
- SYNO.Core.Directory.LDAP.Refresh   -- LDAP refresh triggers
- SYNO.Core.Directory.LDAP.Login.Notify -- Login notification settings
"""

from __future__ import annotations

from typing import Any

from synology_api.base_api import BaseApi


class LdapServer(BaseApi):
    """
    Synology LDAP Server API client.

    Manages LDAP Server configuration, users, profiles,
    and base DNs on DSM 7.x+.

    Requires the LDAP Server package installed and at least
    one LDAP directory configured on the target NAS.

    Parameters
    ----------
    ip_address : str
        NAS IP address (e.g. ``"192.168.1.x"``).
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
    # SYNO.Core.Directory.LDAP — Server Configuration
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_config(self) -> dict[str, object] | str:
        """
        Get LDAP Server configuration.

        Returns the current LDAP client/server settings including
        base DN, server address, encryption, schema type, and
        connection status.

        Returns
        -------
        dict[str, object] or str
            LDAP configuration dictionary. When LDAP is not
            configured, ``base_dn`` is empty and ``error``
            contains a status code (e.g. 2703).

        Examples
        --------
            >>> ldap.ldap_config()
        """
        api_name = "SYNO.Core.Directory.LDAP"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Core.Directory.LDAP.BaseDN — Base DN Management
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_basedn_list(self) -> dict[str, object] | str:
        """
        List LDAP Base DNs.

        .. note::
           This method requires an active LDAP configuration.
           Returns error 2701 if LDAP is not configured.

        Returns
        -------
        dict[str, object] or str
            List of configured Base DNs.

        Examples
        --------
            >>> ldap.ldap_basedn_list()
        """
        api_name = "SYNO.Core.Directory.LDAP.BaseDN"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Core.Directory.LDAP.Profile — LDAP Profiles
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_profile_list(self) -> dict[str, object] | str:
        """
        List LDAP client profiles.

        .. note::
           Requires an active LDAP configuration.

        Returns
        -------
        dict[str, object] or str
            List of LDAP profiles.

        Examples
        --------
            >>> ldap.ldap_profile_list()
        """
        api_name = "SYNO.Core.Directory.LDAP.Profile"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Core.Directory.LDAP.User — User Management
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_user_list(
        self, offset: int = 0, limit: int = 100
    ) -> dict[str, object] | str:
        """
        List LDAP users.

        .. note::
           Requires an active LDAP configuration.

        Parameters
        ----------
        offset : int, optional
            Pagination offset (default 0).
        limit : int, optional
            Maximum results per page (default 100).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"items": [...], "total": N}, "success": true}``.

        Examples
        --------
            >>> ldap.ldap_user_list()
        """
        api_name = "SYNO.Core.Directory.LDAP.User"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {
                "version": info["maxVersion"],
                "method": "list",
                "offset": offset,
                "limit": limit,
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Core.Directory.LDAP.Refresh — Cache Refresh
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_refresh(self) -> dict[str, object] | str:
        """
        Refresh LDAP user/group cache.

        Triggers a re-sync of local LDAP cache with the
        LDAP server.

        .. note::
           Requires an active LDAP configuration.

        Returns
        -------
        dict[str, object] or str
            API response.

        Examples
        --------
            >>> ldap.ldap_refresh()
        """
        api_name = "SYNO.Core.Directory.LDAP.Refresh"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "set"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Core.Directory.LDAP.Login.Notify — Login Notifications
    # ═══════════════════════════════════════════════════════════════════════

    def ldap_login_notify_get(self) -> dict[str, object] | str:
        """
        Get LDAP login notification settings.

        .. note::
           Requires an active LDAP configuration.

        Returns
        -------
        dict[str, object] or str
            Login notification configuration.

        Examples
        --------
            >>> ldap.ldap_login_notify_get()
        """
        api_name = "SYNO.Core.Directory.LDAP.Login.Notify"
        info = self.core_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )
