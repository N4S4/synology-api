"""Synology Core hardware/media/package service API (SYNO.Core.*)."""

from __future__ import annotations
import json
from typing import Optional
from . import base_api


class CoreServiceHW(base_api.BaseApi):
    """Core hardware/media/package: Group, Hardware, ISCSI, Media, OAuth, Package, PortFwd."""

    # SYNO.Core.Group extras
    # ------------------------------------------------------------------

    def group_extra_admin_get(self) -> dict[str, object] | str:
        """
        Get extra admin group settings.

        Returns
        -------
        dict[str, object] or str
            Result of the group extra admin get operation.
        """
        api_name = 'SYNO.Core.Group.ExtraAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def group_member_list(self, group: str) -> dict[str, object] | str:
        """
        List members of a group.

        Parameters
        ----------
        group : str
            The group value.

        Returns
        -------
        dict[str, object] or str
            Result of the group member list operation.
        """
        api_name = 'SYNO.Core.Group.Member'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'list', 'group': group})

    def group_valid_local_admin_get(self) -> dict[str, object] | str:
        """
        Get valid local admin information.

        Returns
        -------
        dict[str, object] or str
            Result of the group valid local admin get operation.
        """
        api_name = 'SYNO.Core.Group.ValidLocalAdmin'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.Hardware extras
    # ------------------------------------------------------------------

    def hardware_lcm_get(self) -> dict[str, object] | str:
        """
        Get LCD monitor panel settings.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware lcm get operation.
        """
        api_name = 'SYNO.Core.Hardware.LCM'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_led_brightness_get(self) -> dict[str, object] | str:
        """
        Get LED brightness settings.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware led brightness get operation.
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_led_brightness_set(self, brightness: int) -> dict[str, object] | str:
        """
        Set LED brightness level.

        Parameters
        ----------
        brightness : int
            The brightness value.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware led brightness set operation.
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'set',
                                  'brightness': brightness})

    def hardware_memory_layout_get(self) -> dict[str, object] | str:
        """
        Get memory layout information.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware memory layout get operation.
        """
        api_name = 'SYNO.Core.Hardware.MemoryLayout'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_need_reboot_get(self) -> dict[str, object] | str:
        """
        Check if a reboot is required.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware need reboot get operation.
        """
        api_name = 'SYNO.Core.Hardware.NeedReboot'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_oob_management_get(self) -> dict[str, object] | str:
        """
        Get out-of-band management (IPMI/BMC) settings.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware oob management get operation.
        """
        api_name = 'SYNO.Core.Hardware.OOBManagement'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_remote_fan_status_get(self) -> dict[str, object] | str:
        """
        Get remote fan status.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware remote fan status get operation.
        """
        api_name = 'SYNO.Core.Hardware.RemoteFanStatus'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_spectre_meltdown_get(self) -> dict[str, object] | str:
        """
        Get Spectre/Meltdown mitigation status.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware spectre meltdown get operation.
        """
        api_name = 'SYNO.Core.Hardware.SpectreMeltdown'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def hardware_video_transcoding_get(self) -> dict[str, object] | str:
        """
        Get hardware video transcoding capability.

        Returns
        -------
        dict[str, object] or str
            Result of the hardware video transcoding get operation.
        """
        api_name = 'SYNO.Core.Hardware.VideoTranscoding'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.ISCSI extras
    # ------------------------------------------------------------------

    def iscsi_fc_target_get(self) -> dict[str, object] | str:
        """
        Get Fibre Channel target settings.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi fc target get operation.
        """
        api_name = 'SYNO.Core.ISCSI.FCTarget'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_host_get(self) -> dict[str, object] | str:
        """
        Get iSCSI host settings.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi host get operation.
        """
        api_name = 'SYNO.Core.ISCSI.Host'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_lunbkp_get(self) -> dict[str, object] | str:
        """
        Get iSCSI LUN backup settings.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi lunbkp get operation.
        """
        api_name = 'SYNO.Core.ISCSI.Lunbkp'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_node_get(self) -> dict[str, object] | str:
        """
        Get iSCSI node information.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi node get operation.
        """
        api_name = 'SYNO.Core.ISCSI.Node'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_replication_get(self) -> dict[str, object] | str:
        """
        Get iSCSI replication settings.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi replication get operation.
        """
        api_name = 'SYNO.Core.ISCSI.Replication'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def iscsi_vmware_get(self) -> dict[str, object] | str:
        """
        Get iSCSI VMware integration settings.

        Returns
        -------
        dict[str, object] or str
            Result of the iscsi vmware get operation.
        """
        api_name = 'SYNO.Core.ISCSI.VMware'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.MediaIndexing
    # ------------------------------------------------------------------

    def media_indexing_get(self) -> dict[str, object] | str:
        """
        Get media indexing settings.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing get operation.
        """
        api_name = 'SYNO.Core.MediaIndexing'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set media indexing settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing set operation.
        """
        api_name = 'SYNO.Core.MediaIndexing'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def media_indexing_index_folder_get(self) -> dict[str, object] | str:
        """
        Get indexed folder list.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing index folder get operation.
        """
        api_name = 'SYNO.Core.MediaIndexing.IndexFolder'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_media_converter_get(self) -> dict[str, object] | str:
        """
        Get media converter settings.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing media converter get operation.
        """
        api_name = 'SYNO.Core.MediaIndexing.MediaConverter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_scheduler_get(self) -> dict[str, object] | str:
        """
        Get media indexing scheduler settings.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing scheduler get operation.
        """
        api_name = 'SYNO.Core.MediaIndexing.Scheduler'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def media_indexing_thumbnail_quality_get(self) -> dict[str, object] | str:
        """
        Get thumbnail quality settings.

        Returns
        -------
        dict[str, object] or str
            Result of the media indexing thumbnail quality get operation.
        """
        api_name = 'SYNO.Core.MediaIndexing.ThumbnailQuality'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.MyDSCenter
    # ------------------------------------------------------------------

    def mydscenter_get(self) -> dict[str, object] | str:
        """
        Get MyDS Center settings.

        Returns
        -------
        dict[str, object] or str
            Result of the mydscenter get operation.
        """
        api_name = 'SYNO.Core.MyDSCenter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def mydscenter_account_get(self) -> dict[str, object] | str:
        """
        Get MyDS Center account information.

        Returns
        -------
        dict[str, object] or str
            Result of the mydscenter account get operation.
        """
        api_name = 'SYNO.Core.MyDSCenter.Account'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def mydscenter_login(self, username: str, password: str) -> dict[str, object] | str:
        """
        Login to MyDS Center.

        Parameters
        ----------
        username : str
            The username value.
        password : str
            The password value.

        Returns
        -------
        dict[str, object] or str
            Result of the mydscenter login operation.
        """
        api_name = 'SYNO.Core.MyDSCenter.Login'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'login',
                                  'username': username, 'password': password}, method='post')

    def mydscenter_logout(self) -> dict[str, object] | str:
        """
        Logout from MyDS Center.

        Returns
        -------
        dict[str, object] or str
            Result of the mydscenter logout operation.
        """
        api_name = 'SYNO.Core.MyDSCenter.Logout'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'logout'})

    def mydscenter_purchase_get(self) -> dict[str, object] | str:
        """
        Get MyDS Center purchase information.

        Returns
        -------
        dict[str, object] or str
            Result of the mydscenter purchase get operation.
        """
        api_name = 'SYNO.Core.MyDSCenter.Purchase'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.NormalUser
    # ------------------------------------------------------------------

    def normal_user_get(self) -> dict[str, object] | str:
        """
        Get normal user settings.

        Returns
        -------
        dict[str, object] or str
            Result of the normal user get operation.
        """
        api_name = 'SYNO.Core.NormalUser'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def normal_user_login_notify_get(self) -> dict[str, object] | str:
        """
        Get normal user login notification settings.

        Returns
        -------
        dict[str, object] or str
            Result of the normal user login notify get operation.
        """
        api_name = 'SYNO.Core.NormalUser.LoginNotify'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.OAuth
    # ------------------------------------------------------------------

    def oauth_scope_get(self) -> dict[str, object] | str:
        """
        Get OAuth scope settings.

        Returns
        -------
        dict[str, object] or str
            Result of the oauth scope get operation.
        """
        api_name = 'SYNO.Core.OAuth.Scope'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def oauth_server_get(self) -> dict[str, object] | str:
        """
        Get OAuth server settings.

        Returns
        -------
        dict[str, object] or str
            Result of the oauth server get operation.
        """
        api_name = 'SYNO.Core.OAuth.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def oauth_server_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set OAuth server settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the oauth server set operation.
        """
        api_name = 'SYNO.Core.OAuth.Server'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Package extras
    # ------------------------------------------------------------------

    def package_auto_upgrade_progress_get(self) -> dict[str, object] | str:
        """
        Get package auto-upgrade progress.

        Returns
        -------
        dict[str, object] or str
            Result of the package auto upgrade progress get operation.
        """
        api_name = 'SYNO.Core.Package.AutoUpgrade.Progress'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_control(self, package_id: str, action: str) -> dict[str, object] | str:
        """
        Control a package (start/stop).

        Parameters
        ----------
        package_id : str
            The package id value.
        action : str
            The action value.

        Returns
        -------
        dict[str, object] or str
            Result of the package control operation.
        """
        api_name = 'SYNO.Core.Package.Control'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': action, 'id': package_id})

    def package_fake_iframe_get(self) -> dict[str, object] | str:
        """
        Get package fake iframe info.

        Returns
        -------
        dict[str, object] or str
            Result of the package fake iframe get operation.
        """
        api_name = 'SYNO.Core.Package.FakeIFrame'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_feed_list(self) -> dict[str, object] | str:
        """
        List package feeds.

        Returns
        -------
        dict[str, object] or str
            Result of the package feed list operation.
        """
        api_name = 'SYNO.Core.Package.Feed'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'list'})

    def package_feed_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set package feed settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the package feed set operation.
        """
        api_name = 'SYNO.Core.Package.Feed'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def package_legal_prerelease_get(self) -> dict[str, object] | str:
        """
        Get package pre-release legal agreement status.

        Returns
        -------
        dict[str, object] or str
            Result of the package legal prerelease get operation.
        """
        api_name = 'SYNO.Core.Package.Legal.PreRelease'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_log_get(self, package_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Get package log entries.

        Parameters
        ----------
        package_id : str, optional
            The package id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package log get operation.
        """
        api_name = 'SYNO.Core.Package.Log'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if package_id:
            req_param['id'] = package_id
        return self.request_data(api_name, info['path'], req_param)

    def package_myds_get(self) -> dict[str, object] | str:
        """
        Get MyDS package info.

        Returns
        -------
        dict[str, object] or str
            Result of the package myds get operation.
        """
        api_name = 'SYNO.Core.Package.MyDS'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_myds_purchase_get(self) -> dict[str, object] | str:
        """
        Get MyDS package purchase info.

        Returns
        -------
        dict[str, object] or str
            Result of the package myds purchase get operation.
        """
        api_name = 'SYNO.Core.Package.MyDS.Purchase'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_progress_get(self, task_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Get package installation/upgrade progress.

        Parameters
        ----------
        task_id : str, optional
            The task id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package progress get operation.
        """
        api_name = 'SYNO.Core.Package.Progress'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if task_id:
            req_param['taskid'] = task_id
        return self.request_data(api_name, info['path'], req_param)

    def package_screenshot_get(self, package_id: str) -> dict[str, object] | str:
        """
        Get package screenshots.

        Parameters
        ----------
        package_id : str
            The package id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package screenshot get operation.
        """
        api_name = 'SYNO.Core.Package.Screenshot'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_screenshot_server_get(self, package_id: str) -> dict[str, object] | str:
        """
        Get package screenshot from server.

        Parameters
        ----------
        package_id : str
            The package id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package screenshot server get operation.
        """
        api_name = 'SYNO.Core.Package.Screenshot.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_setting_update_get(self) -> dict[str, object] | str:
        """
        Get package update settings.

        Returns
        -------
        dict[str, object] or str
            Result of the package setting update get operation.
        """
        api_name = 'SYNO.Core.Package.Setting.Update'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def package_thumb_get(self, package_id: str) -> dict[str, object] | str:
        """
        Get package thumbnail.

        Parameters
        ----------
        package_id : str
            The package id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package thumb get operation.
        """
        api_name = 'SYNO.Core.Package.Thumb'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    def package_thumb_server_get(self, package_id: str) -> dict[str, object] | str:
        """
        Get package thumbnail from server.

        Parameters
        ----------
        package_id : str
            The package id value.

        Returns
        -------
        dict[str, object] or str
            Result of the package thumb server get operation.
        """
        api_name = 'SYNO.Core.Package.Thumb.Server'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get', 'id': package_id})

    # ------------------------------------------------------------------
    # SYNO.Core.PersonalNotification
    # ------------------------------------------------------------------

    def personal_notification_device_get(self) -> dict[str, object] | str:
        """
        Get personal notification device settings.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification device get operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Device'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_event_get(self) -> dict[str, object] | str:
        """
        Get personal notification events.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification event get operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Event'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_filter_get(self) -> dict[str, object] | str:
        """
        Get personal notification filter settings.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification filter get operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Filter'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_filter_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set personal notification filter settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification filter set operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Filter'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    def personal_notification_mobile_get(self) -> dict[str, object] | str:
        """
        Get personal notification mobile settings.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification mobile get operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Mobile'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_settings_get(self) -> dict[str, object] | str:
        """
        Get personal notification settings.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification settings get operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Settings'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def personal_notification_settings_set(self, **kwargs) -> dict[str, object] | str:
        """
        Set personal notification settings.

        Parameters
        ----------
        **kwargs : object
            Additional DSM API parameters for the set operation.

        Returns
        -------
        dict[str, object] or str
            Result of the personal notification settings set operation.
        """
        api_name = 'SYNO.Core.PersonalNotification.Settings'
        info = self.gen_list[api_name]
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)
        return self.request_data(api_name, info['path'], req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.PhotoViewer
    # ------------------------------------------------------------------

    def photo_viewer_get(self) -> dict[str, object] | str:
        """
        Get photo viewer settings.

        Returns
        -------
        dict[str, object] or str
            Result of the photo viewer get operation.
        """
        api_name = 'SYNO.Core.PhotoViewer'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
    # SYNO.Core.PortForwarding extras
    # ------------------------------------------------------------------

    def port_forwarding_get(self) -> dict[str, object] | str:
        """
        Get port forwarding settings.

        Returns
        -------
        dict[str, object] or str
            Result of the port forwarding get operation.
        """
        api_name = 'SYNO.Core.PortForwarding'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_compatibility_get(self) -> dict[str, object] | str:
        """
        Get port forwarding compatibility status.

        Returns
        -------
        dict[str, object] or str
            Result of the port forwarding compatibility get operation.
        """
        api_name = 'SYNO.Core.PortForwarding.Compatibility'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_router_info_get(self) -> dict[str, object] | str:
        """
        Get router information for port forwarding.

        Returns
        -------
        dict[str, object] or str
            Result of the port forwarding router info get operation.
        """
        api_name = 'SYNO.Core.PortForwarding.RouterInfo'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_router_list(self) -> dict[str, object] | str:
        """
        List detected routers.

        Returns
        -------
        dict[str, object] or str
            Result of the port forwarding router list operation.
        """
        api_name = 'SYNO.Core.PortForwarding.RouterList'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    def port_forwarding_rules_serv_get(self) -> dict[str, object] | str:
        """
        Get service-based port forwarding rules.

        Returns
        -------
        dict[str, object] or str
            Result of the port forwarding rules serv get operation.
        """
        api_name = 'SYNO.Core.PortForwarding.Rules.Serv'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info['path'],
                                 {'version': info['maxVersion'], 'method': 'get'})

    # ------------------------------------------------------------------
