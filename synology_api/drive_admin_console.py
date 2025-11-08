"""
Synology Drive Admin Console API wrapper.

This module provides a Python interface for managing Synology Drive Admin Console,
including status, configuration, connections, logs, shares, and settings.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class AdminConsole(base_api.BaseApi):
    """
    Synology Drive Admin Console API implementation.

    This class provides methods to retrieve and manage Synology Drive Admin Console status,
    configuration, connections, logs, shares, and settings.
    """

    def status_info(self) -> dict[str, object] | str:
        """
        Get Synology Drive status information.

        Returns
        -------
        dict[str, object] or str
            Status information.
        """
        api_name = 'SYNO.SynologyDrive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_status'}

        return self.request_data(api_name, api_path, req_param)

    def config_info(self) -> dict[str, object] | str:
        """
        Get Synology Drive configuration information.

        Returns
        -------
        dict[str, object] or str
            Configuration information.
        """
        api_name = 'SYNO.SynologyDrive.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def connections(self) -> dict[str, object] | str:
        """
        Get summary of Synology Drive connections.

        Returns
        -------
        dict[str, object] or str
            Connections summary.
        """
        api_name = 'SYNO.SynologyDrive.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'summary'}

        return self.request_data(api_name, api_path, req_param)

    def drive_check_user(self) -> dict[str, object] | str:
        """
        Check user status in Synology Drive.

        Returns
        -------
        dict[str, object] or str
            User check result.
        """
        api_name = 'SYNO.SynologyDrive'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check_user'}

        return self.request_data(api_name, api_path, req_param)

    def active_connections(self) -> dict[str, object] | str:
        """
        Get list of active Synology Drive connections.

        Returns
        -------
        dict[str, object] or str
            List of active connections.
        """
        api_name = 'SYNO.SynologyDrive.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def active_sync_connections(self) -> dict[str, object] | str:
        """
        Get list of active Synology Drive ShareSync connections.

        Returns
        -------
        dict[str, object] or str
            List of active ShareSync connections.
        """
        api_name = 'SYNO.SynologyDriveShareSync.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def share_active_list(self) -> dict[str, object] | str:
        """
        Get list of active shares in Synology Drive.

        Returns
        -------
        dict[str, object] or str
            List of active shares.
        """
        api_name = 'SYNO.SynologyDrive.Share'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_active'}

        return self.request_data(api_name, api_path, req_param)

    def log(
        self,
        share_type: str = 'all',
        get_all: bool = False,
        limit: int = 1000,
        keyword: str = '',
        date_from: int = 0,
        date_to: int = 0,
        username: str = '',
        target: str = 'user'
    ) -> dict[str, object] | str:
        """
        Get Synology Drive logs.

        Parameters
        ----------
        share_type : str, optional
            Type of share to filter logs (default is 'all').
        get_all : bool, optional
            Whether to get all logs (default is False).
        limit : int, optional
            Maximum number of logs to return (default is 1000).
        keyword : str, optional
            Keyword to filter logs (default is '').
        date_from : int, optional
            Start date in epoch format (default is 0).
        date_to : int, optional
            End date in epoch format (default is 0).
        username : str, optional
            Username to filter logs (default is '').
        target : str, optional
            Target type to filter logs (default is 'user').

        Returns
        -------
        dict[str, object] or str
            Log information.
        """
        api_name = 'SYNO.SynologyDrive.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        if get_all:
            get_all = 'true'
        elif not get_all:
            get_all = 'false'
        else:
            return 'get_all must be True or False'

        req_param = {'version': info['maxVersion'], 'method': 'list', 'share_type': share_type, 'get_all': get_all,
                     'limit': limit, 'keyword': keyword, 'datefrom': date_from, 'dateto': date_to, 'username': username,
                     'target': target}

        return self.request_data(api_name, api_path, req_param)

    def c2fs_share(self) -> dict[str, object] | str:
        """
        Get list of C2FS shares.

        Returns
        -------
        dict[str, object] or str
            List of C2FS shares.
        """
        api_name = 'SYNO.C2FS.Share'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def settings(self) -> dict[str, object] | str:
        """
        Get Synology Drive settings.

        Returns
        -------
        dict[str, object] or str
            Settings information.
        """
        api_name = 'SYNO.SynologyDrive.Settings'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def db_usage(self) -> dict[str, object] | str:
        """
        Get Synology Drive database usage.

        Returns
        -------
        dict[str, object] or str
            Database usage information.
        """
        api_name = 'SYNO.SynologyDrive.DBUsage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def delete_status(self) -> dict[str, object] | str:
        """
        Get status of deleted nodes in Synology Drive.

        Returns
        -------
        dict[str, object] or str
            Delete status information.
        """
        api_name = 'SYNO.SynologyDrive.Node.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def file_property_transfer_status(self) -> dict[str, object] | str:
        """
        Get file property transfer status for User Home migration.

        Returns
        -------
        dict[str, object] or str
            File property transfer status.
        """
        api_name = 'SYNO.SynologyDrive.Migration.UserHome'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def user_sync_profile(self, user: str = '', start: int = 0, limit: str | int = 'null') -> dict[str, object] | str:
        """
        Get user sync profile(s).

        Parameters
        ----------
        user : str, optional
            Username to filter profiles (default is '').
        start : int, optional
            Start index for pagination (default is 0).
        limit : str or int, optional
            Maximum number of profiles to return (default is 'null').

        Returns
        -------
        dict[str, object] or str
            User sync profile information.
        """
        api_name = 'SYNO.SynologyDrive.Profiles'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'start': start, 'limit': limit, 'user': user}

        return self.request_data(api_name, api_path, req_param)

    def index_pause(self, time_pause: int = 60) -> dict[str, object] | str:
        """
        Pause native client index for a specified duration.

        Parameters
        ----------
        time_pause : int, optional
            Pause duration in seconds (default is 60).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.SynologyDrive.Index'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_native_client_index_pause',
                     'pause_duration': time_pause}

        return self.request_data(api_name, api_path, req_param)
