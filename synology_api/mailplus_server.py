"""
Synology MailPlus Server API wrapper.

Wraps the SYNO.MailPlusServer.* APIs for managing the
MailPlus Server package on DSM 7.x+.

Requires MailPlus Server installed on the target NAS.
Most read-only methods work without mail server configuration;
domain/account methods require a configured mail domain.

API endpoints
~~~~~~~~~~~~~
- SYNO.MailPlusServer.MailPlus     -- Core server settings
- SYNO.MailPlusServer.ServerList   -- Cluster/server list
- SYNO.MailPlusServer.SMTP.*       -- SMTP configuration
- SYNO.MailPlusServer.IMAP_POP3    -- IMAP/POP3 settings
- SYNO.MailPlusServer.Security     -- Flow limits & quotas
- SYNO.MailPlusServer.Report       -- Report configuration
- SYNO.MailPlusServer.Audit.*      -- Admin & transaction logs
- SYNO.MailPlusServer.Queue        -- Mail queue
"""

from __future__ import annotations

from typing import Any

from synology_api.base_api import BaseApi


class MailPlusServer(BaseApi):
    """
    Synology MailPlus Server API client.

    Manages MailPlus Server configuration, SMTP/IMAP settings,
    security policies, audit logs, and mail queue monitoring
    via the SYNO.MailPlusServer.* WebAPI endpoints.

    Requires MailPlus Server installed on the target NAS.

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
    # SYNO.MailPlusServer.MailPlus — Core Settings
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_info(self) -> dict[str, object] | str:
        """
        Get core MailPlus Server settings.

        Returns
        -------
        dict[str, object] or str
            Settings including SMTP sender name, DSM access,
            mail export, PGP, and POP3 toggles.

        Examples
        --------
            >>> mp.mailplus_info()
        """
        api_name = "SYNO.MailPlusServer.MailPlus"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.ServerList — Server List
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_server_list(self) -> dict[str, object] | str:
        """
        List MailPlus servers in the cluster.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"server_list": [...], "balancer_enabled": ...,
            "cluster_syncing": ...}, "success": true}``.

        Examples
        --------
            >>> mp.mailplus_server_list()
        """
        api_name = "SYNO.MailPlusServer.ServerList"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.SMTP.General — SMTP Configuration
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_smtp_general(self) -> dict[str, object] | str:
        """
        Get SMTP general configuration.

        Returns
        -------
        dict[str, object] or str
            SMTP settings including banner, hostname,
            max hops, recipients, and auth settings.

        Examples
        --------
            >>> mp.mailplus_smtp_general()
        """
        api_name = "SYNO.MailPlusServer.SMTP.General"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.SMTP.Security — SMTP Security
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_smtp_security(self) -> dict[str, object] | str:
        """
        Get SMTP security configuration.

        Returns
        -------
        dict[str, object] or str
            Security limits including max connections per minute,
            max mails per minute, parallel connections, and
            junk command thresholds.

        Examples
        --------
            >>> mp.mailplus_smtp_security()
        """
        api_name = "SYNO.MailPlusServer.SMTP.Security"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.IMAP_POP3 — IMAP/POP3 Settings
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_imap_pop3(self) -> dict[str, object] | str:
        """
        Get IMAP/POP3 configuration.

        Returns
        -------
        dict[str, object] or str
            IMAP, IMAPS, POP3, POP3S enable/disable toggles
            and authentication security settings.

        Examples
        --------
            >>> mp.mailplus_imap_pop3()
        """
        api_name = "SYNO.MailPlusServer.IMAP_POP3"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.Security — Flow Limits
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_security(self) -> dict[str, object] | str:
        """
        Get mail flow limit and sender quota settings.

        Returns
        -------
        dict[str, object] or str
            Flow limit (mails per time period) and sender
            quota configuration.

        Examples
        --------
            >>> mp.mailplus_security()
        """
        api_name = "SYNO.MailPlusServer.Security"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.Report — Report Settings
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_report(self) -> dict[str, object] | str:
        """
        Get mail report configuration.

        Returns
        -------
        dict[str, object] or str
            Report settings including enable toggle,
            recipient, and scheduled hours/minutes.

        Examples
        --------
            >>> mp.mailplus_report()
        """
        api_name = "SYNO.MailPlusServer.Report"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.MailPlusServer.Audit.AdminLog — Admin Audit Log
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_admin_log(
        self, offset: int = 0, limit: int = 50
    ) -> dict[str, object] | str:
        """
        List MailPlus admin audit log entries.

        Parameters
        ----------
        offset : int, optional
            Pagination offset (default 0).
        limit : int, optional
            Maximum results per page (default 50).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"log_list": [...], "offset": N,
            "total": N}, "success": true}``.

        Examples
        --------
            >>> mp.mailplus_admin_log()
        """
        api_name = "SYNO.MailPlusServer.Audit.AdminLog"
        info = self.gen_list[api_name]
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
    # SYNO.MailPlusServer.Audit.TransactionLog — Transaction Log
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_transaction_log(
        self, offset: int = 0, limit: int = 50
    ) -> dict[str, object] | str:
        """
        List MailPlus mail transaction log entries.

        Parameters
        ----------
        offset : int, optional
            Pagination offset (default 0).
        limit : int, optional
            Maximum results per page (default 50).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"items": [...], "offset": N,
            "total": N, "is_migrating": bool}, "success": true}``.

        Examples
        --------
            >>> mp.mailplus_transaction_log()
        """
        api_name = "SYNO.MailPlusServer.Audit.TransactionLog"
        info = self.gen_list[api_name]
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
    # SYNO.MailPlusServer.Queue — Mail Queue
    # ═══════════════════════════════════════════════════════════════════════

    def mailplus_queue(
        self, offset: int = 0, limit: int = 50
    ) -> dict[str, object] | str:
        """
        List messages in the mail queue.

        Parameters
        ----------
        offset : int, optional
            Pagination offset (default 0).
        limit : int, optional
            Maximum results per page (default 50).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"items": [...], "total": N}, "success": true}``.

        Examples
        --------
            >>> mp.mailplus_queue()
        """
        api_name = "SYNO.MailPlusServer.Queue"
        info = self.gen_list[api_name]
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
