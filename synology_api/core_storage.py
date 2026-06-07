"""
Synology Core Storage API wrapper.

This module provides a Python interface for managing storage resources
on Synology NAS devices, including disks, pools, volumes, iSCSI LUNs,
quotas, and recycle bins.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class CoreStorage(base_api.BaseApi):
    """
    Core Storage API implementation for Synology NAS.

    This class provides methods to manage storage disks, pools, volumes,
    iSCSI LUNs, quotas, and recycle bin operations.
    """

    # ─── SYNO.Core.Storage.Disk ─────────────────────────────────────────

    def storage_disk_list(self) -> dict[str, object] | str:
        """
        List all storage disks.

        Returns
        -------
        dict[str, object] or str
            List of storage disks and their status.
        """
        api_name = 'SYNO.Core.Storage.Disk'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_disk_get(self, disk_id: str) -> dict[str, object] | str:
        """
        Get information for a specific disk.

        Parameters
        ----------
        disk_id : str
            The disk identifier (e.g., 'sda').

        Returns
        -------
        dict[str, object] or str
            Disk information.
        """
        api_name = 'SYNO.Core.Storage.Disk'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': disk_id}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Storage.Disk.FWUpgrade ───────────────────────────────

    def storage_disk_fw_upgrade_get(self) -> dict[str, object] | str:
        """
        Get disk firmware upgrade status.

        Returns
        -------
        dict[str, object] or str
            Firmware upgrade availability and status.
        """
        api_name = 'SYNO.Core.Storage.Disk.FWUpgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def storage_disk_fw_upgrade_start(self, disk_id: str) -> dict[str, object] | str:
        """
        Start a disk firmware upgrade.

        Parameters
        ----------
        disk_id : str
            The disk identifier to upgrade.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Storage.Disk.FWUpgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start',
                     'id': disk_id}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Storage.Pool ─────────────────────────────────────────

    def storage_pool_list(self) -> dict[str, object] | str:
        """
        List all storage pools.

        Returns
        -------
        dict[str, object] or str
            List of storage pools.
        """
        api_name = 'SYNO.Core.Storage.Pool'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_pool_get(self, pool_id: str) -> dict[str, object] | str:
        """
        Get information for a specific storage pool.

        Parameters
        ----------
        pool_id : str
            The storage pool identifier.

        Returns
        -------
        dict[str, object] or str
            Storage pool information.
        """
        api_name = 'SYNO.Core.Storage.Pool'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': pool_id}

        return self.request_data(api_name, api_path, req_param)

    def storage_pool_set(self, pool_id: str,
                         description: Optional[str] = None) -> dict[str, object] | str:
        """
        Update storage pool settings.

        Parameters
        ----------
        pool_id : str
            The storage pool identifier.
        description : str, optional
            New description for the pool.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Storage.Pool'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'id': pool_id}
        if description is not None:
            req_param['description'] = description

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Storage.Volume ───────────────────────────────────────

    def storage_volume_list(self) -> dict[str, object] | str:
        """
        List all storage volumes.

        Returns
        -------
        dict[str, object] or str
            List of storage volumes.
        """
        api_name = 'SYNO.Core.Storage.Volume'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_volume_get(self, volume_path: str) -> dict[str, object] | str:
        """
        Get information for a specific volume.

        Parameters
        ----------
        volume_path : str
            The volume path (e.g., '/volume1').

        Returns
        -------
        dict[str, object] or str
            Volume information.
        """
        api_name = 'SYNO.Core.Storage.Volume'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'volume_path': volume_path}

        return self.request_data(api_name, api_path, req_param)

    def storage_volume_set(self, volume_path: str,
                           description: Optional[str] = None) -> dict[str, object] | str:
        """
        Update volume settings.

        Parameters
        ----------
        volume_path : str
            The volume path (e.g., '/volume1').
        description : str, optional
            New description for the volume.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Storage.Volume'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'volume_path': volume_path}
        if description is not None:
            req_param['description'] = description

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Storage.iSCSILUN ────────────────────────────────────

    def iscsi_lun_list(self) -> dict[str, object] | str:
        """
        List all iSCSI LUNs.

        Returns
        -------
        dict[str, object] or str
            List of iSCSI LUNs.
        """
        api_name = 'SYNO.Core.Storage.iSCSILUN'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def iscsi_lun_get(self, lun_id: str) -> dict[str, object] | str:
        """
        Get information for a specific iSCSI LUN.

        Parameters
        ----------
        lun_id : str
            The iSCSI LUN identifier.

        Returns
        -------
        dict[str, object] or str
            iSCSI LUN information.
        """
        api_name = 'SYNO.Core.Storage.iSCSILUN'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': lun_id}

        return self.request_data(api_name, api_path, req_param)

    def iscsi_lun_set(self, lun_id: str,
                      name: Optional[str] = None,
                      description: Optional[str] = None) -> dict[str, object] | str:
        """
        Update iSCSI LUN settings.

        Parameters
        ----------
        lun_id : str
            The iSCSI LUN identifier.
        name : str, optional
            New name for the LUN.
        description : str, optional
            New description for the LUN.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Storage.iSCSILUN'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'id': lun_id}
        if name is not None:
            req_param['name'] = name
        if description is not None:
            req_param['description'] = description

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Storage.CGI — Storage Manager (gen_list only) ──────────────

    def storage_load_info(self) -> dict[str, object] | str:
        """
        Get full Storage Manager overview.

        Returns disk, pool, volume, enclosure and port information
        in a single call. This is the primary endpoint used by the
        Storage Manager web UI.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"disks": [...], "detected_pools": [...],
            "overview_data": {...}, "ports": [...], ...}, "success": true}``.

        Examples
        --------
            >>> storage.storage_load_info()
        """
        api_name = 'SYNO.Storage.CGI.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load_info'}

        return self.request_data(api_name, api_path, req_param)

    def storage_smart_scheduler_list(self) -> dict[str, object] | str:
        """
        List S.M.A.R.T. test schedules.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"items": [...], "total": N}, "success": true}``.
            Each item includes schedule type, frequency, and target disks.

        Examples
        --------
            >>> storage.storage_smart_scheduler_list()
        """
        api_name = 'SYNO.Storage.CGI.Smart.Scheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_hdd_manager_get(self) -> dict[str, object] | str:
        """
        Get HDD health threshold settings.

        Returns S.M.A.R.T. warning thresholds for bad sectors,
        remaining life, and other disk health indicators.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"BadSctrThrEn": ..., "RemainLifeThrEn": ...,
            ...}, "success": true}``.

        Examples
        --------
            >>> storage.storage_hdd_manager_get()
        """
        api_name = 'SYNO.Storage.CGI.HddMan'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def storage_spare_list(self) -> dict[str, object] | str:
        """
        List hot spare disks.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"hotSpares": [...]}, "success": true}``.

        Examples
        --------
            >>> storage.storage_spare_list()
        """
        api_name = 'SYNO.Storage.CGI.Spare'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Quota ───────────────────────────────────────────────

    def quota_get(self, volume_path: str) -> dict[str, object] | str:
        """
        Get quota settings for a volume.

        Parameters
        ----------
        volume_path : str
            The volume path (e.g., '/volume1').

        Returns
        -------
        dict[str, object] or str
            Quota configuration.
        """
        api_name = 'SYNO.Core.Quota'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'volume_path': volume_path}

        return self.request_data(api_name, api_path, req_param)

    def quota_list(self) -> dict[str, object] | str:
        """
        List quota settings for all volumes.

        Returns
        -------
        dict[str, object] or str
            List of quota settings.
        """
        api_name = 'SYNO.Core.Quota'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def quota_set(self, volume_path: str,
                  enabled: bool = True,
                  quota_mb: Optional[int] = None) -> dict[str, object] | str:
        """
        Set quota for a volume.

        Parameters
        ----------
        volume_path : str
            The volume path (e.g., '/volume1').
        enabled : bool, optional
            Enable or disable quota. Defaults to True.
        quota_mb : int, optional
            Quota size in megabytes.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Quota'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'volume_path': volume_path,
                     'enabled': str(enabled).lower()}
        if quota_mb is not None:
            req_param['quota'] = quota_mb

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.RecycleBin ──────────────────────────────────────────

    def recycle_bin_get(self) -> dict[str, object] | str:
        """
        Get recycle bin settings.

        Returns
        -------
        dict[str, object] or str
            Recycle bin configuration.
        """
        api_name = 'SYNO.Core.RecycleBin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def recycle_bin_set(self, enabled: bool = True,
                        retention_days: Optional[int] = None) -> dict[str, object] | str:
        """
        Set recycle bin configuration.

        Parameters
        ----------
        enabled : bool, optional
            Enable or disable recycle bin. Defaults to True.
        retention_days : int, optional
            Number of days to retain deleted files.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.RecycleBin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enable': str(enabled).lower()}
        if retention_days is not None:
            req_param['retention_days'] = retention_days

        return self.request_data(api_name, api_path, req_param)

    def recycle_bin_clean(self, share_name: Optional[str] = None) -> dict[str, object] | str:
        """
        Empty the recycle bin.

        Parameters
        ----------
        share_name : str, optional
            Shared folder name to clean. If None, cleans all recycle bins.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.RecycleBin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clean'}
        if share_name is not None:
            req_param['share_name'] = share_name

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.RecycleBin.User ─────────────────────────────────────

    def recycle_bin_user_get(self, user: str) -> dict[str, object] | str:
        """
        Get per-user recycle bin settings.

        Parameters
        ----------
        user : str
            The username.

        Returns
        -------
        dict[str, object] or str
            Per-user recycle bin configuration.
        """
        api_name = 'SYNO.Core.RecycleBin.User'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'user': user}

        return self.request_data(api_name, api_path, req_param)

    def recycle_bin_user_set(self, user: str,
                             enabled: bool = True) -> dict[str, object] | str:
        """
        Set per-user recycle bin configuration.

        Parameters
        ----------
        user : str
            The username.
        enabled : bool, optional
            Enable or disable per-user recycle bin. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.RecycleBin.User'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'user': user, 'enable': str(enabled).lower()}

        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_check_quota(self) -> dict:
        """
        Check storage quota usage.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_quota",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_dry_run(self) -> dict:
        """
        Run a dry-run (simulation) operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "dry_run",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_get_schedule_plan(self) -> dict:
        """
        Get the current schedule plan.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_schedule_plan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_get_status(self) -> dict:
        """
        Get the current operational status.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_status",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_get_volume_info(self) -> dict:
        """
        Get volume information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_volume_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_manual_dedupe(self) -> dict:
        """
        Manually trigger data deduplication.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "manual_dedupe",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_rescan_quota_v2(self) -> dict:
        """
        Rescan storage quota (version 2).

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "rescan_quota_v2",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_set_reclaim_type(self) -> dict:
        """
        Set the space reclamation type.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_reclaim_type",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_set_schedule_plan(self) -> dict:
        """
        Set or update the schedule plan.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_schedule_plan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_set_volume_schedule_config(self) -> dict:
        """
        Configure the volume schedule.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_volume_schedule_config",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def btrfs_dedupe_stop(self) -> dict:
        """
        Stop the current operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.BtrfsDedupe``.
        """
        api_name = "SYNO.Storage.CGI.BtrfsDedupe"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "stop",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_disable_passive(self) -> dict:
        """
        Disable passive cache protection mode.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "disable_passive",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_enable_passive(self) -> dict:
        """
        Enable passive cache protection mode.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enable_passive",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_get_config(self) -> dict:
        """
        Get the current configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_config",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_get_status(self) -> dict:
        """
        Get the current operational status.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_status",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_get_status_all(self) -> dict:
        """
        Get the status of all items.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_status_all",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def cache_protection_update_config(self) -> dict:
        """
        Update the configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Cache.Protection``.
        """
        api_name = "SYNO.Storage.CGI.Cache.Protection"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "update_config",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_do_data_scrubbing(self) -> dict:
        """
        Start a data scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "do_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_do_disk_scan(self) -> dict:
        """
        Start a disk scan operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "do_disk_scan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_ignore_data_scrubbing(self) -> dict:
        """
        Ignore/skip a data scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "ignore_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_is_building(self) -> dict:
        """
        Check if the storage is currently building/rebuilding.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "is_building",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_is_data_scrubbing(self) -> dict:
        """
        Check if data scrubbing is currently running.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "is_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_reboot_after_rebuild(self) -> dict:
        """
        Get or configure auto-reboot after rebuild.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "reboot_after_rebuild",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_remove_ask_for_fsck(self) -> dict:
        """
        Clear the file-system check prompt.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_ask_for_fsck",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_remove_ask_for_fsck_scan(self) -> dict:
        """
        Clear the fsck scan prompt.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_ask_for_fsck_scan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_remove_ask_for_remap_scan(self) -> dict:
        """
        Clear the remap scan prompt.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_ask_for_remap_scan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_remove_ask_for_wcache_lost_data_scrubbing(self) -> dict:
        """
        Clear the write-cache lost data scrubbing prompt.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_ask_for_wcache_lost_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def storage_check_should_ask_for_fsck_scan(self) -> dict:
        """
        Check whether an fsck scan prompt should be shown.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Check``.
        """
        api_name = "SYNO.Storage.CGI.Check"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "should_ask_for_fsck_scan",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def detected_pool_assemble(self) -> dict:
        """
        Assemble/re-assemble a detected storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.DetectedPool``.
        """
        api_name = "SYNO.Storage.CGI.DetectedPool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "assemble",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def detected_pool_remove(self) -> dict:
        """
        Remove a component.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.DetectedPool``.
        """
        api_name = "SYNO.Storage.CGI.DetectedPool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dual_enclosure_load(self) -> dict:
        """
        Load/retrieve all entries.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.DualEnclosure``.
        """
        api_name = "SYNO.Storage.CGI.DualEnclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "load",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_exp_fw_fail_get(self) -> dict:
        """
        Get expansion unit firmware failure information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "exp_fw_fail_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_exp_fw_update(self) -> dict:
        """
        Update expansion unit firmware.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "exp_fw_update",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_exp_fw_update_cancel_notify(self) -> dict:
        """
        Cancel expansion unit firmware update notification.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "exp_fw_update_cancel_notify",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_exp_fw_update_list_get(self) -> dict:
        """
        Get the list of available expansion unit firmware updates.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "exp_fw_update_list_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_exp_fw_update_status_get(self) -> dict:
        """
        Get the status of expansion unit firmware update.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "exp_fw_update_status_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_is_exp_connected(self) -> dict:
        """
        Check if the expansion unit is connected.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "is_exp_connected",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_load(self) -> dict:
        """
        Load all enclosure information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "load",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_exp_fw_fail_get(self) -> dict:
        """
        Get SHA expansion unit firmware failure information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_exp_fw_fail_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_exp_fw_update(self) -> dict:
        """
        Update SHA expansion unit firmware.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_exp_fw_update",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_exp_fw_update_cancel_notify(self) -> dict:
        """
        Cancel SHA expansion unit firmware update notification.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_exp_fw_update_cancel_notify",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_exp_fw_update_list_get(self) -> dict:
        """
        List SHA expansion unit firmware updates available.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_exp_fw_update_list_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_exp_fw_update_status_get(self) -> dict:
        """
        Get SHA expansion unit firmware update status.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_exp_fw_update_status_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def enclosure_sha_is_exp_connected(self) -> dict:
        """
        Check if the SHA expansion unit is connected.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Enclosure``.
        """
        api_name = "SYNO.Storage.CGI.Enclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sha_is_exp_connected",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_disable(self) -> dict:
        """
        Disable offline volume operations.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "disable",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_enable(self) -> dict:
        """
        Enable the feature.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enable",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_get_info(self) -> dict:
        """
        Get flash cache information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_pack_for_ma(self) -> dict:
        """
        Package OAuth credentials for the mail account.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pack_for_ma",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_repair(self) -> dict:
        """
        Repair/recover the entity.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "repair",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_reset(self) -> dict:
        """
        Reset the Taipei enclosure.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "reset",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_set_autounlock_key(self) -> dict:
        """
        Set an auto-unlock key for the encryption vault.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_autounlock_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_set_for_ma(self) -> dict:
        """
        Set the person mail account for the Mail Account service.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_for_ma",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_sync_to_passive(self) -> dict:
        """
        Sync data to the passive enclosure.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "sync_to_passive",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_verify_passwd(self) -> dict:
        """
        Verify the encryption vault password.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "verify_passwd",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_unlock_enter_passwd(self) -> dict:
        """
        Enter passwd.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enter_passwd",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_unlock_get_passwd_wrong_record(self) -> dict:
        """
        Get passwd wrong record.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_passwd_wrong_record",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def encryption_vault_unlock_skip_passwd(self) -> dict:
        """
        Skip passwd.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.
        """
        api_name = "SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "skip_passwd",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_add_drive(self) -> dict:
        """
        Add an SSD drive to the flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "add_drive",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_advisor_history_get(self) -> dict:
        """
        Get the Security Advisor scan history.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "advisor_history_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_advisor_poll(self) -> dict:
        """
        Poll for Security Advisor scan progress.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "advisor_poll",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_advisor_start(self) -> dict:
        """
        Start a Security Advisor security scan.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "advisor_start",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_advisor_stop(self) -> dict:
        """
        Stop a running Security Advisor scan.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "advisor_stop",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_check_can_create(self) -> dict:
        """
        Check if a new user can be created.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_can_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_check_can_lock_space(self) -> dict:
        """
        Check if deduplication space can be locked.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_can_lock_space",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_check_pin_metadata_and_rec_size(self) -> dict:
        """
        Check pinned metadata and record size settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_pin_metadata_and_rec_size",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_check_system_raid(self) -> dict:
        """
        Check system RAID configuration on the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_system_raid",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_check_volume_abnormal_cant_create_cache(self) -> dict:
        """
        Check if a volume abnormality prevents cache creation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_volume_abnormal_cant_create_cache",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_configure(self) -> dict:
        """
        Configure DSM FindMe (QuickConnect) settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "configure",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_create_feasibility_hard_check(self) -> dict:
        """
        Run a feasibility check for pool creation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create_feasibility_hard_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_enable(self) -> dict:
        """
        Enable a flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enable",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_estimate_mem_size(self) -> dict:
        """
        Estimate memory requirements for pool operations.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "estimate_mem_size",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_estimate_raid_size(self) -> dict:
        """
        Estimate the RAID size for a pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "estimate_raid_size",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_is_redundancy_degraded(self) -> dict:
        """
        Check if pool redundancy is degraded.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "is_redundancy_degraded",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_remove(self) -> dict:
        """
        Remove SSDs from a flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_remove_cancel(self) -> dict:
        """
        Cancel a volume removal operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_cancel",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_repair(self) -> dict:
        """
        Repair a flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "repair",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_replace(self) -> dict:
        """
        Replace SSDs in a flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "replace",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_shared_cache_config_get(self) -> dict:
        """
        Get the shared SSD cache configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "shared_cache_config_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def flashcache_shared_cache_config_set(self) -> dict:
        """
        Set the shared SSD cache configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Flashcache``.
        """
        api_name = "SYNO.Storage.CGI.Flashcache"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "shared_cache_config_set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_check_loop(self) -> dict:
        """
        Check the deduplication background loop status.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_loop",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_delete_key(self) -> dict:
        """
        Delete an encryption key from the vault.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_erase_all_data(self) -> dict:
        """
        Erase all data on spare disks.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "erase_all_data",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_get(self) -> dict:
        """
        Get KMIP server configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_get_key_list(self) -> dict:
        """
        List all encryption keys in the vault.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_key_list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_get_server_hostname(self) -> dict:
        """
        Get the hostname of the storage server.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_server_hostname",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_get_version_info(self) -> dict:
        """
        Get HA license version information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_version_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_import_cert(self) -> dict:
        """
        Import a KMIP server certificate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "import_cert",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_import_server_ca(self) -> dict:
        """
        Import the KMIP server CA certificate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "import_server_ca",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_list_cert(self) -> dict:
        """
        List KMIP client certificates.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list_cert",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_remove_cert(self) -> dict:
        """
        Remove a KMIP certificate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_cert",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_renew_cert(self) -> dict:
        """
        Renew a KMIP certificate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "renew_cert",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_set(self) -> dict:
        """
        Configure KMIP server settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_set_cert(self) -> dict:
        """
        Set/configure a KMIP certificate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_cert",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_test_conn(self) -> dict:
        """
        Test the KMIP server connection.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_conn",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def kmip_transfer_data(self) -> dict:
        """
        Transfer volume data to another location.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.KMIP``.
        """
        api_name = "SYNO.Storage.CGI.KMIP"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "transfer_data",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_cancel_data_scrubbing(self) -> dict:
        """
        Cancel an ongoing data scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "cancel_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_check_fast_repair(self) -> dict:
        """
        Check if a fast repair is possible on the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_fast_repair",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_create(self) -> dict:
        """
        Create a new storage pool on the NAS.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_data_scrubbing(self) -> dict:
        """
        Get/set data scrubbing status for the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_data_scrubbing_plain(self) -> dict:
        """
        Run a plain data scrubbing operation (no dedupe).

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "data_scrubbing_plain",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_deactivate(self) -> dict:
        """
        Deactivate the flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "deactivate",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_delete(self) -> dict:
        """
        Delete an existing storage pool (destructive — all data lost).

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_edit_desc(self) -> dict:
        """
        Edit the description of a user account.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "edit_desc",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_enum_resource(self) -> dict:
        """
        Enumerate resources within a storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enum_resource",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_estimate_size(self) -> dict:
        """
        Estimate the resulting size after pool expansion.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "estimate_size",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_expand_by_add_disk(self) -> dict:
        """
        Expand a storage pool by adding new disks.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_by_add_disk",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_expand_unallocated(self) -> dict:
        """
        Expand a pool using unallocated space.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_unallocated",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_expand_unfinished_shr(self) -> dict:
        """
        Resume an interrupted SHR expansion.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_unfinished_shr",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_get_setting(self) -> dict:
        """
        Get the flash cache settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_setting",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_is_disk_detected_old_info(self) -> dict:
        """
        Check if a detected disk has old RAID information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "is_disk_detected_old_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_migrate(self) -> dict:
        """
        Migrate a storage pool to a different RAID type.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "migrate",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_pause_data_scrubbing(self) -> dict:
        """
        Pause an ongoing data scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pause_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_pre_delete_check(self) -> dict:
        """
        Check if a pool can be safely deleted.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pre_delete_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_reassemble(self) -> dict:
        """
        Re-assemble a pool from detected disks.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "reassemble",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_remove_missing_pool(self) -> dict:
        """
        Remove a missing storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_missing_pool",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_remove_raid_sb_cache(self) -> dict:
        """
        Remove RAID superblock cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "remove_raid_sb_cache",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_repair(self) -> dict:
        """
        Repair a degraded storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "repair",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_replace(self) -> dict:
        """
        Replace a failing disk in a storage pool with a new one.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "replace",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_set_setting(self) -> dict:
        """
        Configure advanced storage pool settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_setting",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def pool_update_raid_sb_cache(self) -> dict:
        """
        Update RAID superblock cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Pool``.
        """
        api_name = "SYNO.Storage.CGI.Pool"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "update_raid_sb_cache",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def scrubbing_get_state(self, space_id: str) -> dict:
        """
        SYNO.Storage.CGI.Scrubbing.get_state

        Parameters
        ----------
        space_id : str
            Storage space/volume identifier to query scrubbing state for.

        Returns
        -------
        dict
            Scrubbing state for the specified space.
        """
        api_name = "SYNO.Storage.CGI.Scrubbing"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_state",
            "version": 1,
            "space_id": space_id,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_get_health_info(self) -> dict:
        """
        Get storage health information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_health_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_get_latest_online_drive_db_info(self) -> dict:
        """
        Get the latest online drive database info.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_latest_online_drive_db_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_get_smart_info(self) -> dict:
        """
        Get S.M.A.R.T. information for all disks.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_smart_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_list(self) -> dict:
        """
        List all entries.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_secure_erase(self) -> dict:
        """
        Securely erase a disk in the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "secure_erase",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_smart_warning_get(self) -> dict:
        """
        Get S.M.A.R.T. warning settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "smart_warning_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_smart_warning_set(self) -> dict:
        """
        Configure S.M.A.R.T. warning settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "smart_warning_set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def smart_update_smartctl_db(self) -> dict:
        """
        Update the smartctl drive database.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Smart``.
        """
        api_name = "SYNO.Storage.CGI.Smart"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "update_smartctl_db",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def spare_conf_get(self) -> dict:
        """
        Get detailed information.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Spare.Conf``.
        """
        api_name = "SYNO.Storage.CGI.Spare.Conf"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def spare_conf_set(self) -> dict:
        """
        Set spare disk configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Spare.Conf``.
        """
        api_name = "SYNO.Storage.CGI.Spare.Conf"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def taipei_enclosure_load(self) -> dict:
        """
        Load/retrieve all entries.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.TaipeiEnclosure``.
        """
        api_name = "SYNO.Storage.CGI.TaipeiEnclosure"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "load",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_cancel_data_scrubbing(self) -> dict:
        """
        Cancel volume data scrubbing.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "cancel_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_cancel_defrag(self) -> dict:
        """
        Cancel an ongoing defragmentation operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "cancel_defrag",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_cancel_fs_scrubbing(self) -> dict:
        """
        Cancel an ongoing file-system scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "cancel_fs_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_change_recovery_key(self) -> dict:
        """
        Change the encryption key vault recovery key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "change_recovery_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_clean_dek(self) -> dict:
        """
        Clean DEK (Data Encryption Key) entries.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "clean_dek",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_convert_shr_to_pool(self) -> dict:
        """
        Convert SHR to a storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "convert_shr_to_pool",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_convert_shr_without_drive(self) -> dict:
        """
        Convert SHR to a pool without adding drives.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "convert_shr_without_drive",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_create(self) -> dict:
        """
        Create a new volume on the NAS.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_create_on_existing_pool(self) -> dict:
        """
        Create a volume on an existing pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create_on_existing_pool",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_data_scrubbing(self) -> dict:
        """
        Get/set data scrubbing status for the volume.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_defrag(self) -> dict:
        """
        Start a defragmentation operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "defrag",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_delete(self) -> dict:
        """
        Delete an existing volume (destructive).

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_deploy_unused(self) -> dict:
        """
        Deploy unused disk space to a volume.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "deploy_unused",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_disable_space_usage(self) -> dict:
        """
        Disable Btrfs space usage tracking.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "disable_space_usage",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_enable_space_usage(self) -> dict:
        """
        Enable Btrfs space usage tracking.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enable_space_usage",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_enum_resource(self) -> dict:
        """
        Enumerate resources in a volume.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "enum_resource",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_estimate_size(self) -> dict:
        """
        Estimate volume size after changes.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "estimate_size",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_expand_by_add_disk(self) -> dict:
        """
        Expand a volume by adding disks.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_by_add_disk",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_expand_pool_child(self) -> dict:
        """
        Expand a child of the storage pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_pool_child",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_expand_unallocated(self) -> dict:
        """
        Expand a volume using unallocated space.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_unallocated",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_expand_unfinished_shr(self) -> dict:
        """
        Resume interrupted SHR volume expansion.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "expand_unfinished_shr",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_export_recovery_key(self) -> dict:
        """
        Export the encryption vault recovery key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "export_recovery_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_failover_keep_rw(self) -> dict:
        """
        Fail over to secondary enclosure while keeping read-write.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "failover_keep_rw",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_fs_info_on_pool_meta_set(self) -> dict:
        """
        Set file-system info on pool metadata.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "fs_info_on_pool_meta_set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_fs_info_on_pool_meta_update(self) -> dict:
        """
        Update file-system info on pool metadata.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "fs_info_on_pool_meta_update",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_fs_scrubbing(self) -> dict:
        """
        Start a file-system scrubbing operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "fs_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_get_dump_volumes(self) -> dict:
        """
        Get dump/backup volume information for flash cache.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_dump_volumes",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_get_recovery_key(self) -> dict:
        """
        Get the encryption key vault recovery key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_recovery_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_get_recovery_key_info(self) -> dict:
        """
        Get information about the vault recovery key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_recovery_key_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_get_space_usage(self) -> dict:
        """
        Get Btrfs deduplication space usage statistics.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_space_usage",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_migrate(self) -> dict:
        """
        Migrate a volume to a different configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "migrate",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_next_trim_time_get(self) -> dict:
        """
        Get the next scheduled TRIM time for a volume.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "next_trim_time_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_pause_data_scrubbing(self) -> dict:
        """
        Pause volume data scrubbing.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pause_data_scrubbing",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_pre_delete_check(self) -> dict:
        """
        Check if a volume can be safely deleted.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pre_delete_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_repair(self) -> dict:
        """
        Repair a degraded volume.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "repair",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_set_dek(self) -> dict:
        """
        Set a DEK (Data Encryption Key) entry.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_dek",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_set_setting(self) -> dict:
        """
        Configure advanced volume settings.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_setting",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_ssd_trim_get(self) -> dict:
        """
        Get SSD TRIM configuration for the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "ssd_trim_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_ssd_trim_save(self) -> dict:
        """
        Save SSD TRIM configuration for the pool.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "ssd_trim_save",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_transfer_to_rw(self) -> dict:
        """
        Transfer volume to read-write mode.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "transfer_to_rw",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_unlock_by_recovery_key(self) -> dict:
        """
        Unlock the encryption vault using the recovery key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "unlock_by_recovery_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_unlock_by_vault(self) -> dict:
        """
        Unlock the encryption vault using a vault key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "unlock_by_vault",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_unlock_by_vault_password_key(self) -> dict:
        """
        Unlock the encryption vault using a vault password key.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "unlock_by_vault_password_key",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_vol_extent_size_get(self) -> dict:
        """
        Get volume extent size configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "vol_extent_size_get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_vol_extent_size_set(self) -> dict:
        """
        Set volume extent size configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume``.
        """
        api_name = "SYNO.Storage.CGI.Volume"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "vol_extent_size_set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_installer_quick_create(self) -> dict:
        """
        Quick create.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume.Installer``.
        """
        api_name = "SYNO.Storage.CGI.Volume.Installer"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "quick_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_installer_quick_create_precheck(self) -> dict:
        """
        Quick create precheck.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume.Installer``.
        """
        api_name = "SYNO.Storage.CGI.Volume.Installer"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "quick_create_precheck",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_offline_execute(self) -> dict:
        """
        Execute the pending offline volume operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.
        """
        api_name = "SYNO.Storage.CGI.Volume.OfflineOp"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "execute",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_offline_pre_estimate(self) -> dict:
        """
        Pre estimate.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.
        """
        api_name = "SYNO.Storage.CGI.Volume.OfflineOp"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "pre_estimate",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def volume_offline_stop(self) -> dict:
        """
        Stop the current operation.

        Returns
        -------
        dict
            API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.
        """
        api_name = "SYNO.Storage.CGI.Volume.OfflineOp"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "stop",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)
