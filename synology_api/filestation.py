"""
FileStation API module.

This module provides the FileStation class for interacting with Synology NAS FileStation API,
allowing file management, search, upload, download, and background task operations.
"""

from __future__ import annotations

import json
from typing import Optional, Any
import os
import io
import time
from datetime import datetime
from urllib.parse import urljoin, urlencode

import requests
import tqdm
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import sys
import warnings
from urllib import parse
from treelib import Tree
from . import base_api
from .utils import validate_path, get_data_for_request_from_file


class FileStation(base_api.BaseApi):
    """
    FileStation API implementation.

    Provides methods to interact with Synology NAS FileStation API for file and folder operations,
    search, upload, download, and background task management.

    Supported methods:
        - Getters:
            - Get FileStation info
            - Get list of shared folders
            - Get file list in a folder
            - Get file information
            - Get search task results
            - Get mount point list
            - Get favorite list
            - Get directory size calculation status
            - Get MD5 calculation status
            - Check file/folder permissions
            - Get shared link information
            - Get shared link list
            - Get copy or move task status
            - Get delete task status
            - Get extract task status
            - Get file list of archive
            - Get compression task status
            - Get list of all background tasks
        - Setters:
            - Edit favorite name
            - Replace all favorites
            - Edit shared link
        - Actions:
            - Start search task
            - Stop search task
            - Stop all search tasks
            - Add a favorite
            - Delete a favorite
            - Clear broken favorites
            - Start directory size calculation
            - Stop directory size calculation
            - Start MD5 calculation
            - Stop MD5 calculation
            - Upload file
            - Create sharing link
            - Delete shared link
            - Clear invalid shared links
            - Create folder
            - Rename folder
            - Start copy or move task
            - Stop copy or move task
            - Start delete task
            - Stop delete task
            - Delete file or folder (blocking)
            - Start extract task
            - Stop extract task
            - Start file compression
            - Stop file compression
            - Download file
            - Generate file tree

    Parameters
    ----------
    ip_address : str
        IP address of the Synology NAS.
    port : str
        Port number for the connection.
    username : str
        Username for authentication.
    password : str
        Password for authentication.
    secure : bool, optional
        Use HTTPS if True, HTTP otherwise. Default is False.
    cert_verify : bool, optional
        Verify SSL certificates if True. Default is False.
    dsm_version : int, optional
        DSM version of the Synology NAS. Default is 7.
    debug : bool, optional
        Enable debug output if True. Default is True.
    otp_code : str, optional
        One-time password for 2-step verification. Default is None.
    device_id : str, optional
        Device ID for authentication. Default is None.
    device_name : str, optional
        Name of the device. Default is None.
    interactive_output : bool, optional
        If True, enables interactive output. Default is False.
    """

    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 device_id: Optional[str] = None,
                 device_name: Optional[str] = None,
                 interactive_output: bool = True
                 ) -> None:
        """
        Initialize FileStation API client.

        Parameters
        ----------
        ip_address : str
            IP address or hostname of the Synology NAS.
        port : str
            Port number for the API.
        username : str
            Username for authentication.
        password : str
            Password for authentication.
        secure : bool, optional
            Use HTTPS if True, HTTP if False. Default is False.
        cert_verify : bool, optional
            Verify SSL certificates if True. Default is False.
        dsm_version : int, optional
            DSM version. Default is 7.
        debug : bool, optional
            Enable debug output. Default is True.
        otp_code : str, optional
            One-time password for 2FA, if required.
        device_id : str, optional
            Device ID for authentication.
        device_name : str, optional
            Device name for authentication.
        interactive_output : bool, optional
            If True, outputs are formatted for interactive use. Default is True.
        """
        super(FileStation, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                          dsm_version, debug, otp_code, device_id, device_name, 'FileStation')

        self._dir_taskid: str = ''
        self._dir_taskid_list: list[str] = []
        self._md5_calc_taskid: str = ''
        self._md5_calc_taskid_list: list[str] = []
        self._search_taskid: str = ''
        self._search_taskid_list: list[str] = []
        self._copy_move_taskid: str = ''
        self._copy_move_taskid_list: list[str] = []
        self._delete_taskid: str = ''
        self._delete_taskid_list: list[str] = []
        self._extract_taskid: str = ''
        self._extract_taskid_list: list[str] = []
        self._compress_taskid: str = ''
        self._compress_taskid_list: list[str] = []

        self.session.get_api_list('FileStation')

        self.file_station_list: dict = self.session.app_api_list

        self.interactive_output: bool = interactive_output

    def get_info(self) -> dict[str, object] | str:
        """
        Get FileStation information.

        Returns
        -------
        dict[str, object] or str
            FileStation information or error message.
        """
        api_name = 'SYNO.FileStation.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_list_share(self,
                       additional: Optional[str | list[str]] = None,
                       offset: Optional[int] = None,
                       limit: Optional[int] = None,
                       sort_by: Optional[str] = None,
                       sort_direction: Optional[str] = None,
                       onlywritable: bool = False
                       ) -> dict[str, object] | str:
        """
        List shared folders.

        Parameters
        ----------
        additional : str or list of str, optional
            Additional attributes to include.
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        onlywritable : bool, optional
            If True, only writable shares are listed.

        Returns
        -------
        dict[str, object] or str
            List of shared folders or error message.
        """
        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_share'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def get_file_list(self,
                      folder_path: Optional[str] = None,
                      offset: Optional[int] = None,
                      limit: Optional[int] = None,
                      sort_by: Optional[str] = None,
                      sort_direction: Optional[str] = None,
                      pattern: Optional[str] = None,
                      filetype: Optional[str] = None,
                      goto_path: Optional[str] = None,
                      additional: Optional[str | list[str]] = None) -> dict[str, object]:
        """
        List files in a folder.

        Parameters
        ----------
        folder_path : str, optional
            Path to the folder.
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        pattern : str, optional
            Pattern to filter files.
        filetype : str, optional
            File type filter.
        goto_path : str, optional
            Path to go to.
        additional : str or list of str, optional
            Additional attributes to include.

        Returns
        -------
        dict[str, object]
            List of files or error message.
        """
        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        if not isinstance(folder_path, str):
            # break instead of return
            raise ValueError('Enter a valid folder_path')

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if filetype is not None:
            req_param['filetype'] = str(req_param['filetype']).lower()

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        # if type(additional) is list:
        #    additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def get_file_info(self,
                      path: str | list[str],
                      additional_param: Optional[str | list[str]] = None
                      ) -> dict[str, object] | str:
        """
        Get information about a file or files.

        Parameters
        ----------
        path : str or list of str
            Path(s) to the file(s).
        additional_param : str or list of str, optional
            Additional attributes to retrieve.

        Returns
        -------
        dict[str, object] or str
            File information or error message.
        """
        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'getinfo',
                     'path': json.dumps(path)}

        if additional_param is None:
            additional_param = ["real_path", "size",
                                "owner", "time", "perm", "type"]
        elif isinstance(additional_param, str):
            additional_param = [additional_param]
        elif isinstance(additional_param, list):
            if not all(isinstance(a, str) for a in additional_param):
                return "additional_param must be a string or a list of strings."
        else:
            return "additional_param must be a string or a list of strings."

        req_param['additional'] = json.dumps(additional_param)

        return self.request_data(api_name, api_path, req_param)

    # TODO  all working if specify extension check if correct [pattern, extension]
    #  it works if you put extension='...'

    def search_start(self,
                     folder_path: Optional[str] = None,
                     recursive: Optional[bool] = None,
                     pattern: Optional[str] = None,
                     extension: Optional[str] = None,
                     filetype: Optional[str] = None,
                     size_from: Optional[int] = None,
                     size_to: Optional[int] = None,
                     mtime_from: Optional[str | int] = None,
                     mtime_to: Optional[str | int] = None,
                     crtime_from: Optional[str | int] = None,
                     crtime_to: Optional[str | int] = None,
                     atime_from: Optional[str | int] = None,
                     atime_to: Optional[str | int] = None,
                     owner: Optional[str] = None,
                     group: Optional[str] = None
                     ) -> dict[str, object] | str:
        """
        Start a search task.

        Parameters
        ----------
        folder_path : str, optional
            Path to the folder where the search will start.
        recursive : bool, optional
            If True, the search will be recursive.
        pattern : str, optional
            Pattern to search for.
        extension : str, optional
            File extension to filter by.
        filetype : str, optional
            File type filter.
        size_from : int, optional
            Minimum file size.
        size_to : int, optional
            Maximum file size.
        mtime_from : str or int, optional
            Minimum modification time (Unix timestamp or formatted string).
        mtime_to : str or int, optional
            Maximum modification time (Unix timestamp or formatted string).
        crtime_from : str or int, optional
            Minimum creation time (Unix timestamp or formatted string).
        crtime_to : str or int, optional
            Maximum creation time (Unix timestamp or formatted string).
        atime_from : str or int, optional
            Minimum access time (Unix timestamp or formatted string).
        atime_to : str or int, optional
            Maximum access time (Unix timestamp or formatted string).
        owner : str, optional
            Owner filter.
        group : str, optional
            Group filter.

        Returns
        -------
        dict[str, object] or str
            Search task ID or error message.
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'start', 'folder_path': ''}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param'] and 'time' not in key:
                if val is not None:
                    req_param[str(key)] = val
            if 'time' in key:
                if val is not None:
                    try:
                        date = time.strptime(val, "%Y-%m-%d %H:%M:%S")
                        timestamp = time.mktime(date)
                        req_param[key] = '"' + str(timestamp) + '"'
                    except ValueError:
                        try:
                            datetime.fromtimestamp(int(val)).strftime(
                                '%Y-%m-%d %H:%M:%S')
                            req_param[key] = '"' + val + '"'
                        except ValueError:
                            return 'Enter the correct Date Time format "YYY-MM-DD HH:MM:SS" or Unix timestamp'

        if folder_path is None:
            return 'Enter a valid folder_path'
        else:
            req_param['folder_path'] = '"' + folder_path + '"'

        if filetype is not None:
            req_param['filetype'] = '"' + filetype + '"'

        response = self.request_data(api_name, api_path, req_param)

        taskid = response['data']['taskid']
        self._search_taskid = '"{}"'.format(taskid)
        self._search_taskid_list.append('"' + response['data']['taskid'] + '"')

        message = ('You can now check the status of request with '
                   'get_search_list() , your id is: ' + self._search_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": taskid}

        return output

    def get_search_list(self,
                        task_id: str,
                        filetype: Optional[str] = None,
                        limit: Optional[int] = None,
                        sort_by: Optional[str] = None,
                        sort_direction: Optional[str] = None,
                        offset: Optional[int] = None,
                        additional: Optional[str | list[str]] = None
                        ) -> dict[str, object] | str:
        """
        Get the results of a search task.

        Parameters
        ----------
        task_id : str
            Task ID of the search task.
        filetype : str, optional
            File type filter.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        offset : int, optional
            Offset for pagination.
        additional : str or list of str, optional
            Additional attributes to include.

        Returns
        -------
        dict[str, object] or str
            Search results or error message.
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'taskid': ''}

        if task_id is None:
            return 'Enter a correct taskid, choose one of the following: ' + str(self._search_taskid_list)
        else:
            req_param['taskid'] = task_id

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional', 'task_id']:
                if val is not None:
                    req_param[str(key)] = val

        if filetype is not None:
            req_param['filetype'] = str(filetype).lower()

        if additional is None:
            additional = ['size', 'owner', 'time']

        if type(additional) is list:
            additional = '","'.join(additional)

        req_param['additional'] = '["' + additional + '"]'

        return self.request_data(api_name, api_path, req_param)

    def stop_search_task(self, taskid: str) -> dict[str, object] | str:
        """
        Stop a search task.

        Parameters
        ----------
        taskid : str
            Task ID of the search task to stop.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'taskid': self._search_taskid}

        if taskid is None:  # NOTE this is unreachable
            return 'Enter a valid taskid, choose between ' + str(self._search_taskid_list)

        self._search_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_all_search_task(self) -> str:
        """
        Stop all running search tasks.

        Returns
        -------
        str
            Confirmation message.
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'taskid': ''}

        assert len(self._search_taskid_list), 'Task list is empty' +\
            str(self._search_taskid_list)

        for task_id in self._search_taskid_list:
            req_param['taskid'] = task_id
            self.request_data(api_name, api_path, req_param)

        self._search_taskid_list = []

        return 'All task are stopped'

    def get_mount_point_list(self,
                             mount_type: str,
                             offset: Optional[int] = None,
                             limit: Optional[int] = None,
                             sort_by: Optional[str] = None,
                             sort_direction: Optional[str] = None,
                             additional: Optional[str | list[str]] = [
                                 "real_path", "owner", "time", "perm", "mount_point_type"]
                             ) -> dict[str, object] | str:
        """
        List mount points.

        Parameters
        ----------
        mount_type : str
            Type of mount point to return.

            Posible values:
            - `"ftp"` = FTP and FTPS connections
            - `"davs"` = WebDAV connections
            - `"sharing"` = Public cloud connections
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.

            Posible values:
            - `"name"`
            - `"path"`
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        additional : str or list of str, optional
            Additional attributes to include. Defaults to `["real_path","owner","time","perm","mount_point_type"]`.

            Possible values (not exhaustive):
            - `"real_path"`
            - `"size"`
            - `"owner"`
            - `"time"`
            - `"mount_point_type"`
            - `"perm"`

        Returns
        -------
        dict[str, object] or str
            List of mount points or error message.
        """
        api_name = 'SYNO.FileStation.VirtualFolder'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'additional': additional,
            'type': mount_type
        }

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional', 'mount_type']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def get_favorite_list(self,
                          offset: Optional[int] = None,
                          limit: Optional[int] = None,
                          sort_by: Optional[str] = None,
                          status_filter: Optional[str] = None,
                          additional: Optional[str | list[str]] = None
                          ) -> dict[str, object] | str:
        """
        List favorite files and folders.

        Parameters
        ----------
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        status_filter : str, optional
            Status filter.
        additional : str or list of str, optional
            Additional attributes to include.

        Returns
        -------
        dict[str, object] or str
            List of favorites or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def add_a_favorite(self,
                       path: str,
                       name: Optional[str] = None,
                       index: Optional[int] = None
                       ) -> dict[str, object] | str:
        """
        Add a file or folder to favorites.

        Parameters
        ----------
        path : str
            Path to the file or folder.
        name : str, optional
            Name for the favorite.
        index : int, optional
            Index for the favorite.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'add'}

        if path is None:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_a_favorite(self, path: Optional[str] = None) -> dict[str, object] | str:
        """
        Delete a favorite.

        Parameters
        ----------
        path : str, optional
            Path to the favorite to delete.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_broken_favorite(self) -> dict[str, object] | str:
        """
        Clear broken favorites.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_broken'}

        return self.request_data(api_name, api_path, req_param)

    def edit_favorite_name(self, path: str, new_name: str) -> dict[str, object] | str:
        """
        Edit the name of a favorite.

        Parameters
        ----------
        path : str
            Path to the favorite.
        new_name : str
            New name for the favorite.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if path is None:
            return 'Enter a valid path'
        else:
            req_param['path'] = path

        if new_name is None:
            return 'Enter a valid new_name'
        else:
            req_param['new_name'] = new_name

        return self.request_data(api_name, api_path, req_param)

    def replace_all_favorite(self, path: str | list[str], name: str | list[str]):
        """
        Replace all favorites with new paths and names.

        Parameters
        ----------
        path : str or list of str
            New path or list of new paths for the favorites.
        name : str or list of str
            New name or list of new names for the favorites.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if type(path) is list:
            path = ','.join(path)
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        if type(name) is list:
            name = ','.join(name)
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = name
        else:
            return 'Enter a valid name'

        return self.request_data(api_name, api_path, req_param)

    def start_dir_size_calc(self, path: str) -> dict[str, object] | str:
        """
        Start a directory size calculation task.

        Parameters
        ----------
        path : str
            Path to the directory.

        Returns
        -------
        dict[str, object] or str
            Task ID or error message.
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        taskid = self.request_data(api_name, api_path, req_param)[
            'data']['taskid']

        response_id = '"{}"'.format(taskid)
        self._dir_taskid = response_id
        self._dir_taskid_list.append(response_id)

        message = ('You can now check the status of request '
                   'with get_dir_status() , your id is: '
                   + response_id)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": taskid}

        return output

    def stop_dir_size_calc(self, taskid: str) -> str:
        """
        Stop a directory size calculation task.

        Parameters
        ----------
        taskid : str
            Task ID of the size calculation task to stop.

        Returns
        -------
        str
            Confirmation message.
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'taskid': taskid}

        if taskid is None:
            return 'Enter a valid taskid choose between: ' + str(self._dir_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        self.request_data(api_name, api_path, req_param)
        self._dir_taskid_list.remove('"' + taskid + '"')

        return 'The task has been stopped'

    def get_dir_status(self, taskid: Optional[str] = None) -> dict[str, object] | str:
        """
        Get the status of a directory size calculation task.

        Parameters
        ----------
        taskid : str, optional
            Task ID of the size calculation task.

        Returns
        -------
        dict[str, object] or str
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'status', 'taskid': taskid}

        if taskid is None and self._dir_taskid != '':
            return 'Choose a taskid from this list: ' + str(self._dir_taskid)

        return self.request_data(api_name, api_path, req_param)

    def start_md5_calc(self, file_path: str) -> str | dict[str, object]:
        """
        Start an MD5 calculation task.

        Parameters
        ----------
        file_path : str
            Path to the file.

        Returns
        -------
        str or dict[str, object]
            Task ID or error message.
        """
        api_name = 'SYNO.FileStation.MD5'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if file_path is None:
            return 'Enter a correct file_path'
        else:
            req_param['file_path'] = file_path

        self._md5_calc_taskid = self.request_data(
            api_name, api_path, req_param)['data']['taskid']
        self._md5_calc_taskid_list.append(self._md5_calc_taskid)

        message = ('You can now check the status of request with '
                   'get_md5_status() , your id is: ' + self._md5_calc_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._md5_calc_taskid}

        return output

    def get_md5_status(self, taskid: Optional[str] = None) -> str | dict[str, object]:
        """
        Get the status of an MD5 calculation task.

        Parameters
        ----------
        taskid : str, optional
            Task ID of the MD5 calculation task.

        Returns
        -------
        str or dict[str, object]
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.MD5'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None and self._md5_calc_taskid != '':
            req_param['taskid'] = '"{taskid}"'.format(
                taskid=self._md5_calc_taskid)
        elif taskid is not None:
            req_param['taskid'] = '"{taskid}"'.format(taskid=taskid)
        else:
            return 'Did you run start_md5_calc() first? No task id found! ' + str(self._md5_calc_taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_md5_calc(self, taskid: str) -> str:
        """
        Stop an MD5 calculation task.

        Parameters
        ----------
        taskid : str
            Task ID of the MD5 calculation task to stop.

        Returns
        -------
        str
            Confirmation message.
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'taskid': taskid}

        if taskid is None:
            return 'Enter a valid taskid choose between: ' + str(self._md5_calc_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        self.request_data(api_name, api_path, req_param)
        self._md5_calc_taskid_list.remove(taskid)

        return 'The task has been stopped'

    def check_permissions(self,
                          path: str,
                          filename: str,
                          overwrite: Optional[bool] = None,
                          create_only: Optional[bool] = None
                          ) -> dict[str, object] | str:
        """
        Check permissions for a file or folder.

        Parameters
        ----------
        path : str
            Path to the file or folder.
        filename : str
            Name of the file.
        overwrite : bool, optional
            If True, overwriting is allowed.
        create_only : bool, optional
            If True, only creation is allowed.

        Returns
        -------
        dict[str, object] or str
            Permission check result or error message.
        """
        api_name = 'SYNO.FileStation.CheckPermission'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'write'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if path is None:
            return 'Enter a valid path'

        if filename is None:
            return 'Enter a valid name'

        return self.request_data(api_name, api_path, req_param)

    def upload_file(self,
                    dest_path: str,
                    file_path: str,
                    create_parents: bool = True,
                    overwrite: bool = True,
                    verify: bool = False,
                    progress_bar: bool = True
                    ) -> str | tuple[int, dict[str, object]]:
        """
        Upload a file to the server.

        Parameters
        ----------
        dest_path : str
            Destination path on the server.
        file_path : str
            Path to the file to upload.
        create_parents : bool, optional
            If True, parent folders will be created.
        overwrite : bool, optional
            If True, existing files will be overwritten.
        verify : bool, optional
            If True, SSL certificates will be verified.
        progress_bar : bool, optional
            If True, shows a progress bar during upload.

        Returns
        -------
        str or tuple[int, dict[str, object]]
            Upload result or error message.
        """
        api_name = 'SYNO.FileStation.Upload'
        info = self.file_station_list[api_name]
        api_path = info['path']

        session = requests.session()

        base = urljoin(self.base_url, api_path)
        url_params = {
            "api": api_name,
            "version": info["minVersion"],
            "method": "upload",
            "_sid": self._sid
        }

        url = f"{base}?{urlencode(url_params)}"
        encoder_params = {
            'path': dest_path,
            'create_parents': str(create_parents).lower(),
            'overwrite': str(overwrite).lower(),
        }
        data = get_data_for_request_from_file(
            file_path=file_path, fields=encoder_params, called_from='FileStation', progress_bar=True)
        r = session.post(
            url,
            data=data,
            verify=verify,
            headers={"X-SYNO-TOKEN": self.session._syno_token,
                     'Content-Type': data.content_type}
        )
        session.close()
        if r.status_code != 200 or not r.json()['success']:
            return r.status_code, r.json()

        return r.json()

    def get_shared_link_info(self, link_id: str) -> dict[str, object] | str:
        """
        Get information about a shared link.

        Parameters
        ----------
        link_id : str
            ID of the shared link.

        Returns
        -------
        dict[str, object] or str
            Shared link information or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def get_shared_link_list(self,
                             offset: Optional[int] = None,
                             limit: Optional[int] = None,
                             sort_by: Optional[str] = None,
                             sort_direction: Optional[str] = None,
                             force_clean: Optional[bool] = None
                             ) -> dict[str, object] | str:
        """
        List shared links.

        Parameters
        ----------
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        force_clean : bool, optional
            If True, forces a clean of the shared link list.

        Returns
        -------
        dict[str, object] or str
            List of shared links or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_sharing_link(self,
                            path: str,
                            password: Optional[str] = None,
                            date_expired: Optional[str | int] = None,
                            date_available: Optional[str | int] = None,
                            expire_times: int = 0
                            ) -> dict[str, object] | str:
        """
        Create a shared link.

        Parameters
        ----------
        path : str
            Path to the file or folder to share.
        password : str, optional
            Password for the shared link.
        date_expired : str or int, optional
            Expiration date for the shared link (Unix timestamp or formatted string).
        date_available : str or int, optional
            Availability date for the shared link (Unix timestamp or formatted string).
        expire_times : int, optional
            Number of times the link can be accessed before expiring.

        Returns
        -------
        dict[str, object] or str
            Shared link details or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create'}

        if date_expired:
            if str(date_expired)[0] != '"':
                date_expired = '"' + str(date_expired) + '"'
        if date_available:
            if str(date_available)[0] != '"':
                date_available = '"' + str(date_available) + '"'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if path is None:
            return 'Enter a valid path'

        return self.request_data(api_name, api_path, req_param)

    def delete_shared_link(self, link_id: str) -> dict[str, object] | str:
        """
        Delete a shared link.

        Parameters
        ----------
        link_id : str
            ID of the shared link to delete.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def clear_invalid_shared_link(self) -> dict[str, object] | str:
        """
        Clear invalid shared links.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_invalid'}

        return self.request_data(api_name, api_path, req_param)

    def edit_shared_link(self,
                         link_id: str,
                         password: Optional[str] = None,
                         date_expired: Optional[str | int] = None,
                         date_available: Optional[str | int] = None,
                         expire_times: int = 0
                         ) -> dict[str, object] | str:
        """
        Edit a shared link.

        Parameters
        ----------
        link_id : str
            ID of the shared link to edit.
        password : str, optional
            New password for the shared link.
        date_expired : str or int, optional
            New expiration date for the shared link (Unix timestamp or formatted string).
        date_available : str or int, optional
            New availability date for the shared link (Unix timestamp or formatted string).
        expire_times : int, optional
            New number of times the link can be accessed before expiring.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if date_expired:
            if str(date_expired)[0] != '"':
                date_expired = '"' + str(date_expired) + '"'
        if date_available:
            if str(date_available)[0] != '"':
                date_available = '"' + str(date_available) + '"'

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_folder(self,
                      folder_path: str | list[str],
                      name: str | list[str],
                      force_parent: Optional[bool] = None,
                      additional: Optional[str | list[str]] = None
                      ) -> str | dict[str, object]:
        """
        Create a new folder.

        Parameters
        ----------
        folder_path : str or list of str
            Path or list of paths where the folder should be created.
        name : str or list of str
            Name or list of names for the new folder.
        force_parent : bool, optional
            If True, parent folders will be created if they don't exist.
        additional : str or list of str, optional
            Additional attributes to include.

        Returns
        -------
        str or dict[str, object]
            Creation result or error message.
        """
        api_name = 'SYNO.FileStation.CreateFolder'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'folder_path', 'additional', 'name']:
                if val is not None:
                    req_param[str(key)] = val

        if type(folder_path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in folder_path]
            folder_path = new_path
            folder_path = '[' + ','.join(folder_path) + ']'
            req_param['folder_path'] = folder_path
        elif folder_path is not None:
            req_param['folder_path'] = folder_path
        else:
            return 'Enter a valid path'

        if type(name) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in name]
            name = new_path
            name = '[' + ','.join(name) + ']'
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = '"' + name + '"'
        else:
            return 'Enter a valid path'

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def rename_folder(self,
                      path: str | list[str],
                      name: str | list[str],
                      additional: Optional[str | list[str]] = None,
                      search_taskid: Optional[str] = None
                      ) -> dict[str, object] | str:
        """
        Rename a file or a folder.

        Parameters
        ----------
        path : str or list of str
            Current path or list of paths of the files or folder(s) to rename.
        name : str or list of str
            New name or list of new names for the file or folder(s).
        additional : str or list of str, optional
            Additional attributes to include.
        search_taskid : str, optional
            Task ID of a search task.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.

        Examples
        --------
        >>> rename_folder('/Downloads/script.log', 'script1.log')
        >>> rename_folder(['/Downloads/script.log','/Downloads/script.log'],['a.log', 'b.log'])
        >>> rename_folder('/Downloads/script', 'code')
        """
        api_name = 'SYNO.FileStation.Rename'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'rename'}

        if isinstance(path, list) and isinstance(name, list):
            if len(path) != len(name):
                raise ValueError("Path and name must have the same length.")
        elif isinstance(path, str) and isinstance(name, str):
            pass  # ok, both are strings
        else:
            raise TypeError(
                "Path and name must be both lists or both strings.")

        if validate_path(path) == False:
            return 'Enter a valid folder path or file path (ex. /Downloads/script.log)'

        req_param['path'] = json.dumps(path)
        req_param['name'] = json.dumps(name)

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        if search_taskid is not None:
            req_param['search_taskid'] = search_taskid

        return self.request_data(api_name, api_path, req_param, method='post')

    def start_copy_move(self,
                        path: str | list[str],
                        dest_folder_path: str | list[str],
                        overwrite: Optional[bool] = None,
                        remove_src: Optional[bool] = None,
                        accurate_progress: Optional[bool] = None,
                        search_taskid: Optional[str] = None
                        ) -> str | dict[str, object]:
        """
        Start a copy or move task.

        Parameters
        ----------
        path : str or list of str
            Source path or list of source paths to copy or move.
        dest_folder_path : str or list of str
            Destination folder path or list of destination folder paths.
        overwrite : bool, optional
            If True, existing files will be overwritten.
        remove_src : bool, optional
            If True, source files will be removed after copying.
        accurate_progress : bool, optional
            If True, shows accurate progress.
        search_taskid : str, optional
            Task ID of a search task.

        Returns
        -------
        str or dict[str, object]
            Task ID or error message.

        Examples
        --------
        Start a simple move task:
        You have to specify only the file on the path and not the dest folder.

        >>> fs = FileStation(**params)
        >>> task_id = fs.start_copy_task(
        ...     path="/Media/Film/Action/movie1.mkv",
        ...     dest_folder_path="/Media/Film/Drama",
        ...     overwrite=True
        ... )
        """
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        if type(dest_folder_path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in dest_folder_path]
            dest_folder_path = new_path
            dest_folder_path = '[' + ','.join(dest_folder_path) + ']'
            req_param['name'] = dest_folder_path
        elif dest_folder_path is not None:
            req_param['dest_folder_path'] = dest_folder_path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'additional',
                           'dest_folder_path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        self._copy_move_taskid = self.request_data(
            api_name, api_path, req_param)['data']['taskid']
        self._dir_taskid_list.append(self._copy_move_taskid)

        message = ('You can now check the status of request with '
                   'get_copy_move_status() , your id is: '
                   + self._copy_move_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._copy_move_taskid}

        return output

    def get_copy_move_status(self, taskid: str) -> dict[str, object] | str:
        """
        Get the status of a copy or move task.

        Parameters
        ----------
        taskid : str
            Task ID of the copy or move task.

        Returns
        -------
        dict[str, object] or str
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid choose between ' + str(self._copy_move_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        return self.request_data(api_name, api_path, req_param)

    def stop_copy_move_task(self, taskid: str) -> dict[str, object] | str:
        """
        Stop a copy or move task.

        Parameters
        ----------
        taskid : str
            Task ID of the copy or move task to stop.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid choose between ' + str(self._copy_move_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._copy_move_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def start_delete_task(self,
                          path: str | list[str],
                          accurate_progress: Optional[bool] = None,
                          recursive: Optional[bool] = None,
                          search_taskid: Optional[str] = None
                          ) -> dict[str, object] | str:
        """
        Start a delete task.

        Parameters
        ----------
        path : str or list of str
            Path or list of paths to the file or folder to delete.
        accurate_progress : bool, optional
            If True, shows accurate progress.
        recursive : bool, optional
            If True, deletes folders recursively.
        search_taskid : str, optional
            Task ID of a search task.

        Returns
        -------
        dict[str, object] or str
            Task ID or error message.
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        self._delete_taskid = self.request_data(
            api_name, api_path, req_param)['data']['taskid']
        self._delete_taskid_list.append(self._delete_taskid)

        message = ('You can now check the status of request with '
                   'get_delete_status() , task id is: '
                   + self._delete_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._delete_taskid}

        return output

    def get_delete_status(self, taskid: str) -> dict[str, object] | str:
        """
        Get the status of a delete task.

        Parameters
        ----------
        taskid : str
            Task ID of the delete task.

        Returns
        -------
        dict[str, object] or str
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._delete_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_delete_task(self, taskid: str) -> dict[str, object] | str:
        """
        Stop a delete task.

        Parameters
        ----------
        taskid : str
            Task ID of the delete task to stop.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._delete_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._delete_taskid_list.remove('"' + taskid + '"')

        return self.request_data(api_name, api_path, req_param)

    def delete_blocking_function(self,
                                 path: str,
                                 recursive: Optional[bool] = None,
                                 search_taskid: Optional[str] = None) -> dict[str, object] | str:
        """
        Delete a file or folder (blocking function).

        This function will stop your script until done! Do not interrupt.

        Parameters
        ----------
        path : str or list of str
            Path or list of paths to the file or folder to delete.
        recursive : bool, optional
            If True, deletes folders recursively.
        search_taskid : str, optional
            Task ID of a search task.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        'This function will stop your script until done! Do not interrupt '

        return self.request_data(api_name, api_path, req_param)

    def start_extract_task(self,
                           file_path: str,
                           dest_folder_path: str,
                           overwrite: Optional[bool] = None,
                           keep_dir: Optional[bool] = None,
                           create_subfolder: Optional[bool] = None,
                           codepage: Optional[str] = None,
                           password: Optional[str] = None,
                           item_id: Optional[str] = None
                           ) -> dict[str, object] | str:
        """
        Start an extract task.

        Parameters
        ----------
        file_path : str
            Path to the archive file.
        dest_folder_path : str
            Destination folder path where the files will be extracted.
        overwrite : bool, optional
            If True, existing files will be overwritten.
        keep_dir : bool, optional
            If True, the original directory structure will be kept.
        create_subfolder : bool, optional
            If True, a subfolder will be created for the extracted files.
        codepage : str, optional
            Codepage for the extraction.
        password : str, optional
            Password for the archive, if required.
        item_id : str, optional
            Item ID for the extraction task.

        Returns
        -------
        dict[str, object] or str
            Task ID or error message.
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start', 'file_path': file_path,
                     'dest_folder_path': dest_folder_path}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if file_path is None:
            return 'Enter a valid file_path'

        if dest_folder_path is None:
            return 'Enter a valid dest_folder_path'

        self._extract_taskid = self.request_data(
            api_name, api_path, req_param)['data']['taskid']
        self._extract_taskid_list.append(self._extract_taskid)

        message = ('You can now check the status of request with '
                   'get_extract_status() , your id is: '
                   + self._extract_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._extract_taskid}

        return output

    def get_extract_status(self, taskid: str) -> dict[str, object] | str:
        """
        Get the status of an extract task.

        Parameters
        ----------
        taskid : str
            Task ID of the extract task.

        Returns
        -------
        dict[str, object] or str
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._extract_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_extract_task(self, taskid: str) -> dict[str, object] | str:
        """
        Stop an extract task.

        Parameters
        ----------
        taskid : str
            Task ID of the extract task to stop.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._extract_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._extract_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def get_file_list_of_archive(self,
                                 file_path: str,
                                 offset: Optional[int] = None,
                                 limit: Optional[int] = None,
                                 sort_by: Optional[str] = None,
                                 sort_direction: Optional[str] = None,
                                 codepage: Optional[str] = None,
                                 password: Optional[str] = None,
                                 item_id: Optional[str] = None
                                 ) -> dict[str, object] | str:
        """
        Get the list of files in an archive.

        Parameters
        ----------
        file_path : str
            Path to the archive file.
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        codepage : str, optional
            Codepage for the file list.
        password : str, optional
            Password for the archive, if required.
        item_id : str, optional
            Item ID for the archive.

        Returns
        -------
        dict[str, object] or str
            List of files in the archive or error message.
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if file_path is None:
            return 'Enter a valid file_path'

        return self.request_data(api_name, api_path, req_param)

    def start_file_compression(self,
                               path: str | list[str],
                               dest_file_path: str,
                               level: Optional[int] = None,
                               mode: Optional[str] = None,
                               compress_format: Optional[str] = None,
                               password: Optional[str] = None
                               ) -> dict[str, object] | str | tuple[str]:
        """
        Start a file compression task.

        Parameters
        ----------
        path : str or list of str
            Path or list of paths to the file or folder to compress.
        dest_file_path : str
            Destination file path for the compressed file.
        level : int, optional
            Compression level.
        mode : str, optional
            Compression mode.
        compress_format : str, optional
            Compression format.
        password : str, optional
            Password for the compressed file, if required.

        Returns
        -------
        dict[str, object] or str
            Task ID or error message.
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'compress_format', '_password', '_api_path',
                           'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        if dest_file_path is None:
            return 'Enter a valid dest_file_path'

        if compress_format is not None:
            req_param['format'] = compress_format

        if password is not None:
            req_param['_password'] = password

        self._compress_taskid = self.request_data(
            api_name, api_path, req_param)['data']['taskid']

        message = ('You can now check the status of request with '
                   'get_compress_status() , your id is: '
                   + self._compress_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._compress_taskid}

        return output

    def get_compress_status(self, taskid: str) -> dict[str, object] | str:
        """
        Get the status of a file compression task.

        Parameters
        ----------
        taskid : str
            Task ID of the compression task.

        Returns
        -------
        dict[str, object] or str
            Task status or error message.
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_compress_task(self, taskid: str) -> dict[str, object] | str:
        """
        Stop a file compression task.

        Parameters
        ----------
        taskid : str
            Task ID of the compression task to stop.

        Returns
        -------
        dict[str, object] or str
            Response from the API or error message.
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_list_of_all_background_task(self,
                                        offset: Optional[int] = None,
                                        limit: Optional[int] = None,
                                        sort_by: Optional[str] = None,
                                        sort_direction: Optional[str] = None,
                                        api_filter: Optional[str, list] = None
                                        ) -> dict[str, object] | str:
        """
        Get a list of all background tasks.

        Parameters
        ----------
        offset : int, optional
            Offset for pagination.
        limit : int, optional
            Limit for pagination.
        sort_by : str, optional
            Field to sort by.
        sort_direction : str, optional
            Sort direction ('asc' or 'desc').
        api_filter : str, optional
            API filter.

        Returns
        -------
        dict[str, object] or str
            List of background tasks or error message.
        """
        api_name = 'SYNO.FileStation.BackgroundTask'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if isinstance(api_filter, list):
            new_path = []
            [new_path.append('"' + x + '"') for x in api_filter]
            api_filter = new_path
            api_filter = '[' + ','.join(api_filter) + ']'
            req_param['api_filter'] = api_filter

        return self.request_data(api_name, api_path, req_param)

    def get_file(self,
                 path: str,
                 mode: str,
                 dest_path: str = ".",
                 chunk_size: int = 8192,
                 verify: bool = False
                 ) -> Optional[str]:
        """
        Download a file from the server.

        Parameters
        ----------
        path : str
            The file path starting with a shared folder to be downloaded.
        mode : str
            Mode for downloading the file ('open' to open in browser, 'download' to download to disk).
        dest_path : str, optional
            Destination path on the local machine (for 'download' mode).
        chunk_size : int, optional
            Chunk size for downloading.
        verify : bool, optional
            If True, SSL certificates will be verified.

        Returns
        -------
        Optional[str]
            None if successful, error message otherwise.
        """
        api_name = 'SYNO.FileStation.Download'
        info = self.file_station_list[api_name]
        api_path = info['path']

        if path is None:
            return 'Enter a valid path'

        session = requests.session()

        url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=download&path=%s&mode=%s&_sid=%s' % (
            api_name, info['maxVersion'], parse.quote_plus(path), mode, self._sid)

        if mode is None:
            return 'Enter a valid mode (open / download)'

        if mode == r'open':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:  # filter out keep-alive new chunks
                        sys.stdout.buffer.write(chunk)

        if mode == r'download':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                if not os.path.isdir(dest_path):
                    os.makedirs(dest_path)
                with open(dest_path + "/" + os.path.basename(path), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)

        if mode == r'serve':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                return io.BytesIO(r.content)

    def generate_file_tree(self,
                           folder_path: str,
                           tree: Tree,
                           max_depth: Optional[int] = 1,
                           start_depth: Optional[int] = 0) -> None:
        """
        Recursively generate the file tree based on the folder path you give constrained with.

        You need to create the root node before calling this function.

        Parameters
        ----------
        folder_path : str
            Folder path to generate file tree.
        tree : Tree
            Instance of the Tree from the `treelib` library.
        max_depth : int, optional
            Non-negative number of maximum depth of tree generation if node tree is directory, default to '1' to generate full tree. If 'max_depth=0' it will be equivalent to no recursion.
        start_depth : int, optional
            Non negative number to start to control tree generation default to '0'.
        """

        if start_depth < 0:
            start_depth = 0
            warnings.warn(
                f"'start_depth={start_depth}'. It should not be less or than 0, setting 'start_depth' to 0!",
                RuntimeWarning,
                stacklevel=2
            )

        assert start_depth <= max_depth, ValueError(
            f"'start_depth' should not be greater than 'max_depth'. Got '{start_depth=}, {max_depth=}'")
        assert isinstance(tree, Tree), ValueError(
            "'tree' has to be a type of 'Tree'")

        data: dict[str, object] = self.get_file_list(
            folder_path=folder_path
        ).get("data")

        files = data.get("files")
        _file_info_getter = map(lambda x: (
            x.get('isdir'), x.get('name'), x.get('path')), files)
        for isdir, file_name, file_path in _file_info_getter:

            if isdir and (start_depth >= max_depth):
                tree.create_node(file_name, file_path, parent=folder_path, data={
                                 "isdir": isdir, "max_depth": True})

            elif isdir:
                tree.create_node(file_name, file_path, parent=folder_path, data={
                                 "isdir": isdir, "max_depth": False})
                self.generate_file_tree(
                    file_path, tree, max_depth, start_depth + 1)

            else:
                tree.create_node(file_name, file_path, parent=folder_path, data={
                                 "isdir": isdir, "max_depth": False})


# TODO SYNO.FileStation.Thumb to be done
