"""
Log Center API wrapper for Synology DSM.

This module provides a class to interact with the Synology Log Center API.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class LogCenter(base_api.BaseApi):
    """
    Interface for Synology Log Center API.

    Provides methods to interact with log center features such as retrieving logs,
    client status, remote archives, and storage settings.
    """

    def logcenter(self) -> dict[str, object] | str:
        """
        Retrieve the list of log center receive rules.

        Returns
        -------
        dict[str, object] or str
            The API response containing the receive rules or an error message.
        """
        api_name = 'SYNO.LogCenter.RecvRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_cnt(self) -> dict[str, object] | str:
        """
        Retrieve the count status from the syslog client.

        Returns
        -------
        dict[str, object] or str
            The API response containing the count status or an error message.
        """
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'cnt_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_eps(self) -> dict[str, object] | str:
        """
        Retrieve the EPS (events per second) status from the syslog client.

        Returns
        -------
        dict[str, object] or str
            The API response containing the EPS status or an error message.
        """
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'eps_get'}

        return self.request_data(api_name, api_path, req_param)

    def remote_log_archives(self) -> dict[str, object] | str:
        """
        Retrieve the list of remote log archive subfolders.

        Returns
        -------
        dict[str, object] or str
            The API response containing remote archive subfolders or an error message.
        """
        api_name = 'SYNO.LogCenter.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get_remotearch_subfolder'}

        return self.request_data(api_name, api_path, req_param)

    def display_logs(self) -> dict[str, object] | str:
        """
        Retrieve the list of logs from the syslog client.

        Returns
        -------
        dict[str, object] or str
            The API response containing the logs or an error message.
        """
        api_name = 'SYNO.Core.SyslogClient.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def setting_storage_list(self) -> dict[str, object] | str:
        """
        Retrieve the log center storage settings.

        Returns
        -------
        dict[str, object] or str
            The API response containing storage settings or an error message.
        """
        api_name = 'SYNO.LogCenter.Setting.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def registry_send_list(self) -> dict[str, object] | str:
        """
        Retrieve the list of log center client registry send settings.

        Returns
        -------
        dict[str, object] or str
            The API response containing registry send settings or an error message.
        """
        api_name = 'SYNO.LogCenter.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def history(self) -> dict[str, object] | str:
        """
        Retrieve the log center history.

        Returns
        -------
        dict[str, object] or str
            The API response containing the log center history or an error message.
        """
        api_name = 'SYNO.LogCenter.History'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
