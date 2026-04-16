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
