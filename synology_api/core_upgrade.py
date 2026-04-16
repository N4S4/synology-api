"""
Synology Core Upgrade API wrapper (extended endpoints).

This module covers SYNO.Core.Upgrade endpoints that are NOT already
provided by core_sys_info.SysInfo, including cluster patches, group
upgrades, junior-mode data, pre-checks, and remote actions.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class CoreUpgrade(base_api.BaseApi):
    """
    Extended Core Upgrade API implementation for Synology NAS.

    This class provides methods for cluster-level upgrades, group upgrades,
    patch management, pre-checks, and remote upgrade actions.
    """

    # ─── SYNO.Core.Upgrade.AutoUpgrade.Security ────────────────────────

    def auto_upgrade_security_get(self) -> dict[str, object] | str:
        """
        Get auto-upgrade security settings.

        Returns
        -------
        dict[str, object] or str
            Security auto-upgrade configuration.
        """
        api_name = 'SYNO.Core.Upgrade.AutoUpgrade.Security'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def auto_upgrade_security_set(self,
                                  enabled: bool = True) -> dict[str, object] | str:
        """
        Set auto-upgrade security settings.

        Parameters
        ----------
        enabled : bool, optional
            Enable or disable security auto-upgrade. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.AutoUpgrade.Security'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enabled': str(enabled).lower()}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Cluster.Patch ───────────────────────────────

    def cluster_patch_get(self) -> dict[str, object] | str:
        """
        Get cluster patch information.

        Returns
        -------
        dict[str, object] or str
            Cluster patch status.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Patch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def cluster_patch_list(self) -> dict[str, object] | str:
        """
        List available cluster patches.

        Returns
        -------
        dict[str, object] or str
            List of cluster patches.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Patch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Cluster.Server ──────────────────────────────

    def cluster_server_get(self) -> dict[str, object] | str:
        """
        Get cluster upgrade server information.

        Returns
        -------
        dict[str, object] or str
            Cluster upgrade server status.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def cluster_server_list(self) -> dict[str, object] | str:
        """
        List cluster upgrade servers.

        Returns
        -------
        dict[str, object] or str
            List of cluster upgrade servers.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Cluster.Server.Download ─────────────────────

    def cluster_server_download_get(self) -> dict[str, object] | str:
        """
        Get cluster server download status.

        Returns
        -------
        dict[str, object] or str
            Download status for cluster server upgrade.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Server.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def cluster_server_download_start(self) -> dict[str, object] | str:
        """
        Start cluster server upgrade download.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.Cluster.Server.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Group ───────────────────────────────────────

    def upgrade_group_get(self) -> dict[str, object] | str:
        """
        Get upgrade group information.

        Returns
        -------
        dict[str, object] or str
            Upgrade group status.
        """
        api_name = 'SYNO.Core.Upgrade.Group'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_group_list(self) -> dict[str, object] | str:
        """
        List upgrade groups.

        Returns
        -------
        dict[str, object] or str
            List of upgrade groups.
        """
        api_name = 'SYNO.Core.Upgrade.Group'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Group.Download ──────────────────────────────

    def upgrade_group_download_get(self) -> dict[str, object] | str:
        """
        Get group download status.

        Returns
        -------
        dict[str, object] or str
            Group upgrade download status.
        """
        api_name = 'SYNO.Core.Upgrade.Group.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_group_download_start(self) -> dict[str, object] | str:
        """
        Start group upgrade download.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.Group.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Group.Setting ───────────────────────────────

    def upgrade_group_setting_get(self) -> dict[str, object] | str:
        """
        Get group upgrade settings.

        Returns
        -------
        dict[str, object] or str
            Group upgrade settings.
        """
        api_name = 'SYNO.Core.Upgrade.Group.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_group_setting_set(self,
                                  enabled: bool = True) -> dict[str, object] | str:
        """
        Set group upgrade settings.

        Parameters
        ----------
        enabled : bool, optional
            Enable or disable group upgrade. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.Group.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enabled': str(enabled).lower()}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.GroupInstall ────────────────────────────────

    def group_install_get(self) -> dict[str, object] | str:
        """
        Get group install status.

        Returns
        -------
        dict[str, object] or str
            Group install status.
        """
        api_name = 'SYNO.Core.Upgrade.GroupInstall'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def group_install_start(self) -> dict[str, object] | str:
        """
        Start a group install.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.GroupInstall'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.GroupInstall.Network ────────────────────────

    def group_install_network_get(self) -> dict[str, object] | str:
        """
        Get group install network status.

        Returns
        -------
        dict[str, object] or str
            Network status for group install.
        """
        api_name = 'SYNO.Core.Upgrade.GroupInstall.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def group_install_network_set(self,
                                  **kwargs: object) -> dict[str, object] | str:
        """
        Set group install network configuration.

        Parameters
        ----------
        **kwargs : object
            Network configuration key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.GroupInstall.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.JuniorModeData ──────────────────────────────

    def junior_mode_data_get(self) -> dict[str, object] | str:
        """
        Get junior mode data.

        Returns
        -------
        dict[str, object] or str
            Junior mode data.
        """
        api_name = 'SYNO.Core.Upgrade.JuniorModeData'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def junior_mode_data_set(self,
                             **kwargs: object) -> dict[str, object] | str:
        """
        Set junior mode data.

        Parameters
        ----------
        **kwargs : object
            Junior mode configuration key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.JuniorModeData'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.Patch ───────────────────────────────────────

    def upgrade_patch_get(self) -> dict[str, object] | str:
        """
        Get upgrade patch information.

        Returns
        -------
        dict[str, object] or str
            Upgrade patch status.
        """
        api_name = 'SYNO.Core.Upgrade.Patch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_patch_list(self) -> dict[str, object] | str:
        """
        List available upgrade patches.

        Returns
        -------
        dict[str, object] or str
            List of upgrade patches.
        """
        api_name = 'SYNO.Core.Upgrade.Patch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.PreCheck ────────────────────────────────────

    def upgrade_precheck_get(self) -> dict[str, object] | str:
        """
        Get upgrade pre-check status.

        Returns
        -------
        dict[str, object] or str
            Pre-check results for pending upgrade.
        """
        api_name = 'SYNO.Core.Upgrade.PreCheck'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_precheck_start(self) -> dict[str, object] | str:
        """
        Start an upgrade pre-check.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.PreCheck'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Upgrade.RemoteAction ────────────────────────────────

    def remote_action_get(self) -> dict[str, object] | str:
        """
        Get remote upgrade action status.

        Returns
        -------
        dict[str, object] or str
            Remote action status.
        """
        api_name = 'SYNO.Core.Upgrade.RemoteAction'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def remote_action_set(self,
                          action: str,
                          **kwargs: object) -> dict[str, object] | str:
        """
        Set a remote upgrade action.

        Parameters
        ----------
        action : str
            The remote action to perform (e.g., 'install', 'cancel').
        **kwargs : object
            Additional action parameters.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Upgrade.RemoteAction'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'action': action}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)
