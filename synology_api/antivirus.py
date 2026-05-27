"""
Synology Antivirus Essential API wrapper.

Wraps the SYNO.AntiVirus.* APIs for managing
Antivirus Essential on DSM 7.x+.

Requires Antivirus Essential package installed
on the target NAS.

API endpoints
~~~~~~~~~~~~~
- SYNO.AntiVirus.Config      -- Antivirus configuration
- SYNO.AntiVirus.Schedule    -- Scan schedules
- SYNO.AntiVirus.Quarantine  -- Quarantined items
- SYNO.AntiVirus.General     -- System info & definitions
- SYNO.AntiVirus.Log         -- Scan logs (needs prior scans)
"""

from __future__ import annotations

from typing import Any

from synology_api.base_api import BaseApi


class Antivirus(BaseApi):
    """
    Synology Antivirus Essential API client.

    Manages antivirus configuration, scan schedules,
    quarantine, and system information via the
    SYNO.AntiVirus.* WebAPI endpoints.

    Requires Antivirus Essential installed on the target NAS.
    """

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.AntiVirus.Config — Configuration
    # ═══════════════════════════════════════════════════════════════════════

    def config_get(self) -> dict[str, object] | str:
        """
        Get antivirus configuration.

        Retrieves current antivirus settings including whitelist,
        scan behaviour, and virus action policy.

        Returns
        -------
        dict[str, object] or str
            Configuration dictionary with keys like ``enableWhitelist``,
            ``scanExtensionOnly``, ``smartScan``, ``updateBeforeScan``,
            and ``virusAction`` (e.g. ``"do_nothing"``, ``"clean"``,
            ``"quarantine"``, ``"delete"``).

        Examples
        --------
            >>> av.config_get()
        """
        api_name = "SYNO.AntiVirus.Config"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.AntiVirus.Schedule — Scan Schedules
    # ═══════════════════════════════════════════════════════════════════════

    def schedule_load(self) -> dict[str, object] | str:
        """
        Get all scheduled scan jobs.

        Returns the list of configured scan schedules
        with their activation status, trigger times,
        and scan types.

        Returns
        -------
        dict[str, object] or str
            Dictionary with ``jobCount`` (int) and
            ``scheduleScanJobs`` (list of schedule objects),
            each with keys ``activated``, ``triggerTime``,
            ``scanType``, and ``scanTarget``.

        Examples
        --------
            >>> av.schedule_load()
        """
        api_name = "SYNO.AntiVirus.Schedule"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "load"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.AntiVirus.Quarantine — Quarantined Items
    # ═══════════════════════════════════════════════════════════════════════

    def quarantine_load(
        self, start: int = 0, limit: int = 200
    ) -> dict[str, object] | str:
        """
        Get quarantined files with pagination.

        Lists files currently held in quarantine.

        Parameters
        ----------
        start : int, optional
            Starting offset for pagination (default 0).
        limit : int, optional
            Maximum items to return (default 200).

        Returns
        -------
        dict[str, object] or str
            Dictionary with ``quarantineCount`` (int) and
            ``quarantineArray`` (list of quarantined file objects).

        Examples
        --------
            >>> av.quarantine_load()
            >>> av.quarantine_load(start=200, limit=200)
        """
        api_name = "SYNO.AntiVirus.Quarantine"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {
                "version": info["maxVersion"],
                "method": "load",
                "start": start,
                "limit": limit,
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.AntiVirus.General — System Info & Definitions
    # ═══════════════════════════════════════════════════════════════════════

    def general_sys_info(self) -> dict[str, object] | str:
        """
        Get antivirus system and definition information.

        Returns virus definition status, download progress,
        licence expiration, and overall protection status.

        Returns
        -------
        dict[str, object] or str
            Dictionary with keys like ``downloadSizeNow``,
            ``downloadSizeTotal``, ``licenceExpire``,
            ``button`` (UI status flags), and ``errormsg``.

        Examples
        --------
            >>> av.general_sys_info()
        """
        api_name = "SYNO.AntiVirus.General"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name,
            info["path"],
            {"version": info["maxVersion"], "method": "get_sys_info"},
        )
