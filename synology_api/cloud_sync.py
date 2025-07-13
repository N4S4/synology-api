"""
CloudSync API module.

This module provides the CloudSync class, which implements methods to interact with Synology's Cloud Sync API.
It allows retrieving and setting package settings, managing cloud connections and tasks, and handling synchronization processes.
"""
from __future__ import annotations
from typing import Any
from . import base_api
import json
from .utils import merge_dicts, make_folder_meta_list_from_path


class CloudSync(base_api.BaseApi):
    """
    Cloud Sync API implementation.

       This API provides the functionality to get information related to the package settings and current connections and tasks.
       It also provides functionalities to set most of the settings for tasks and package configuration, as well as manage the current syncing processes.

       Due to the vast amount of public clouds available in the project, the API was not tested for every cloud scenario, so some params request may be missing in specific not tested clouds.

       The tested clouds so far are:
       - Google Drive
       - OneDrive
       - DropBox
       - Amazon S3 (task creation)

       Supported methods:
            - Getters:
               - Get package settings
               - Get connections
               - Get connections settings
               - Get connection information
               - Get connection auth information
               - Get connection logs
               - Get connection tasks
               - Get task filters
               - Get task synced remote directories
               - Get recently modified & currently syncing files
            - Setters:
               - Set package settings
               - Set relink behavior
               - Set connection settings
               - Set connection schedule settings
               - Set task settings
               - Set task filters
            - Actions:
               - Pause connection
               - Resume connection
               - Delete connection
               - Delete task
               - Validate task settings
               - Create S3 task
    """

    def get_pkg_config(self) -> dict[str, object]:
        """
        Retrieve package settings.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of package settings.

            Examples
            --------
            ```json
            {
                "data": {
                    "admin_mode": "enable",
                    "log_count": 20000,
                    "repo_vol_path": "/volume2",
                    "sync_mode": false,
                    "volume_count": 2,
                    "volume_list": [
                        {
                            "desc": "",
                            "display": "Volume 1 (Available capacity:  715.84 GB )",
                            "mount_point": "/volume1",
                            "size_free": "768625090560",
                            "size_total": "955458760704",
                            "value": "1",
                            "vol_desc": ""
                        },
                        {
                            "desc": "",
                            "display": "Volume 2 (Available capacity:  1841.73 GB )",
                            "mount_point": "/volume2",
                            "size_free": "1977547526144",
                            "size_total": "3835577597952",
                            "value": "2",
                            "vol_desc": ""
                        }
                    ],
                    "worker_count": 20
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_config'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_connections(self, group_by: str = 'group_by_user') -> dict[str, object]:
        """
        Retrieve a list of current cloud connections.

            Parameters
            ----------
            group_by : str, optional
                How to group the connection list, by user or cloud type. Defaults to `"group_by_user"`.

                Possible values:
                - `group_by_user`: Group connection by owner user.
                - `group_by_cloud_type`: Group connections by cloud provider.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of cloud connections.

            Examples
            --------
            ```json
            {
                "data": {
                    "conn": [
                        {
                            "id": 3,
                            "link_status": 1,
                            "resource": "",
                            "status": "uptodate",
                            "task_display_name": "Dropbox",
                            "task_name": "Dropbox",
                            "type": "db",
                            "type_id": 2,
                            "unfinished_files": 0,
                            "user_id": "dbid:xxxxxxxxxxxxxxxxxx",
                            "user_name": "username"
                        },
                        {
                            "id": 2,
                            "link_status": 1,
                            "resource": "",
                            "status": "syncing",
                            "task_display_name": "Microsoft OneDrive",
                            "task_name": "Microsoft OneDrive",
                            "type": "od_v1",
                            "type_id": 22,
                            "unfinished_files": 2,
                            "user_id": "xxxxxx",
                            "user_name": "username"
                        }
                    ],
                    "is_admin_mode": true,
                    "is_pause": false,
                    "notification": null,
                    "total": 2,
                    "tray_status": "syncing"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'list_conn',
            'is_tray': False,
            'group_by': group_by
        }

        return self.request_data(api_name, api_path, req_param)

    def get_connection_settings(self, conn_id: int) -> dict[str, object]:
        """
        Retrieve settings for a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the connection settings.

            Examples
            --------
            ```json
            {
                "data": {
                    "client_type": "db",
                    "isSSE": false,
                    "is_enabled_schedule": false,
                    "max_download_speed": 0,
                    "max_upload_speed": 0,
                    "part_size": 0,
                    "pull_event_period": 60,
                    "schedule_info": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                    "storage_class": "",
                    "task_name": "Dropbox"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_connection_setting',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

    def get_connection_information(self, conn_id: int) -> dict[str, object]:
        """
        Retrieve cloud information for a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing cloud information.

            Examples
            --------
            ```json
            {
                "data": {
                    "auth_version": "",
                    "bucket_name": "",
                    "container_name": "",
                    "project_id": "",
                    "public_url": "",
                    "quota_total": 2147483648,
                    "quota_used": 423330996,
                    "region": "",
                    "server_addr": "",
                    "shared_drive_name": "",
                    "storage_class": "",
                    "type": "db",
                    "type_id": 2,
                    "user_name": "username"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_property',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

    def get_connection_auth(self, conn_id: int) -> dict[str, object]:
        """
        Retrieve authentication information for a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the connection authentication details.

            Examples
            --------
            ```json
            {
                "data": {
                    "access_key": "",
                    "access_token": "xxxxxxxx",
                    "auth_pass": "",
                    "auth_scheme": 0,
                    "auth_user": "",
                    "bucket_id": "",
                    "bucket_name": "",
                    "client_id": "xxxxxxxx",
                    "client_type": "db",
                    "conn_id": 3,
                    "container_name": "",
                    "download_url": "",
                    "openstack_api_key": "",
                    "openstack_domain_id": "",
                    "openstack_domain_name": "",
                    "openstack_identity_service_url": "",
                    "openstack_identity_service_version": "",
                    "openstack_password": "",
                    "openstack_proj_id": "",
                    "openstack_region": "",
                    "openstack_tenant_id": "",
                    "openstack_tenant_name": "",
                    "openstack_token": "",
                    "public_url": "",
                    "refresh_token": "xxxxxxxx",
                    "resource": "",
                    "root_folder_id": "",
                    "root_folder_path": "/",
                    "secret_key": "",
                    "server_addr": "",
                    "service_host": "",
                    "unique_id": "dbid:xxxxxxxx",
                    "user_name": "username"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_conn_auth_info',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

    def get_connection_logs(
        self,
        conn_id: int,
        keyword: str = '',
        date_from: int = 0,
        date_to: int = 0,
        log_level: int = -1,
        action: int = -1,
        offset: int = 0,
        limit: int = 200
    ) -> dict[str, object]:
        """
        Retrieve logs for a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            keyword : str, optional
                A keyword to filter logs. Defaults to `''`.

            date_from : int, optional
                The starting date in epoch format. Defaults to `0`.

            date_to : int, optional
                The ending date in epoch format. Defaults to `0`.

            log_level : int, optional
                Log level filter. Defaults to `-1`.

                Possible values:
                - `-1`: All
                - `0`: Info
                - `1`: Warning
                - `2`: Error

            action : int, optional
                Action filter. Defaults to `-1`.

                Possible values:
                - `-1`: All
                - `0`: Delete Remote
                - `1`: Download
                - `2`: Upload
                - `3`: Delete Local
                - `4`: Rename Remote
                - `8`: Merge
                - `9`: Merge Deletion

            offset : int, optional
                Log offset for pagination. Defaults to `0`.

            limit : int, optional
                Number of logs to retrieve. Defaults to `200`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the connection logs.

            Examples
            --------
            ```json
            {
                "data": {
                    "items": [
                        {
                            "action": 1,
                            "error_code": -36,
                            "file_name": "OCR Japanese extension.paper",
                            "file_type": "file",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/OCR Japanese extension.paper",
                            "session_id": 4,
                            "time": 1724418508
                        },
                        {
                            "action": 1,
                            "error_code": -36,
                            "file_name": "OCR Japanese extension.paper",
                            "file_type": "file",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/OCR Japanese extension.paper",
                            "session_id": 4,
                            "time": 1724418119
                        }
                    ],
                    "total": 2
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_log',
            'connection_id': conn_id,
            'offset': offset,
            'keyword': keyword,
            'date_from': date_from,
            'date_to': date_to,
            'log_level': log_level,
            'action': action,
            'limit': limit
        }

        return self.request_data(api_name, api_path, req_param)

    def get_tasks(self, conn_id: int) -> dict[str, object]:
        """
        Retrieve a list of tasks related to a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of tasks.

            Examples
            --------
            ```json
            {
                "data": {
                    "sess": [
                        {
                            "cloud_type_str": "db",
                            "conn_id": 3,
                            "error": 0,
                            "error_desc": "",
                            "link_status": 1,
                            "local_sync_path": "/test_share/WebDAV test/subfolder",
                            "remote_folder_id": "id:xxxx",
                            "remote_sync_path": "/docs",
                            "sess_id": 4,
                            "sync_direction": "ONLY_DOWNLOAD",
                            "sync_status": "uptodate"
                        }
                    ],
                    "total": 1
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'list_sess',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

    def get_task_filters(self, sess_id: int) -> dict[str, object]:
        """
        Retrieve filter information for a specific task.

            Parameters
            ----------
            sess_id : int
                The ID of the task, obtained from `get_tasks()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing task filter information.

            Examples
            --------
            ```json
            {
                "data": {
                    "filtered_extensions": [
                        "wbmp",
                        "webdoc",
                        "x3f",
                        "xbm"
                    ],
                    "filtered_max_upload_size": 1048576,
                    "filtered_names": [
                        "test"
                    ],
                    "filtered_paths": [
                        "/subfolder_1"
                    ],
                    "user_defined_extensions": [
                        "iso"
                    ],
                    "user_defined_names": [
                        "test"
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_selective_sync_config',
            'session_id': sess_id
        }

        return self.request_data(api_name, api_path, req_param)

    def get_task_cloud_folders(
        self,
        sess_id: int,
        remote_folder_id: str,
        path: str = '/'
    ) -> dict[str, object]:
        """
        Retrieve a list of children directories in the cloud for a specific task.

            Parameters
            ----------
            sess_id : int
                The ID of the task, obtained from `get_tasks()`.

            remote_folder_id : str
                The ID of the remote folder, obtained from `get_tasks()`.

            path : str, optional
                The folder path to retrieve the child directories from. Defaults to root `'/'`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of children directories.

            Examples
            --------
            ```json
            {
                "data": {
                    "children": [
                        {
                            "exists_type": 1,
                            "file_id": "",
                            "path": "/subfolder_1",
                            "text": "subfolder_1"
                        },
                        {
                            "exists_type": 1,
                            "file_id": "",
                            "path": "/new folder",
                            "text": "new folder"
                        },
                        {
                            "exists_type": 3,
                            "file_id": "id:xxxx",
                            "path": "/test1",
                            "text": "test1"
                        },
                        {
                            "exists_type": 3,
                            "file_id": "id:xxxx",
                            "path": "/test2",
                            "text": "test2"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_selective_folder_list',
            'session_id': sess_id,
            'path': path,
            'file_id': remote_folder_id,
            'exists_type': 'null'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_recently_modified(self) -> dict[str, object]:
        """
        Retrieve the 5 latest modified files and the currently syncing items.

            Returns
            -------
            dict[str, object]
                A dictionary containing the recently modified files.

            Examples
            --------
            ```json
            {
                "data": {
                    "history_items": [
                        {
                            "action": 1,
                            "base_name": "test_file.paper",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/test_file.paper",
                            "session_id": 4,
                            "syncfolder_basename": "subfolder"
                        },
                        {
                            "action": 1,
                            "base_name": "perfect plan.paper",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/perfect plan.paper",
                            "session_id": 4,
                            "syncfolder_basename": "subfolder"
                        },
                        {
                            "action": 1,
                            "base_name": "Untitled.paper",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/Untitled.paper",
                            "session_id": 4,
                            "syncfolder_basename": "subfolder"
                        },
                        {
                            "action": 1,
                            "base_name": "translation hw.paper",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/translation hw.paper",
                            "session_id": 4,
                            "syncfolder_basename": "subfolder"
                        },
                        {
                            "action": 1,
                            "base_name": "The Tao of Harp.paper",
                            "log_level": 2,
                            "path": "/test_share/WebDAV test/subfolder/song ideas/The Tao of Harp.paper",
                            "session_id": 4,
                            "syncfolder_basename": "subfolder"
                        }
                    ],
                    "is_admin_mode": true,
                    "processing_items": [
                        {
                            "base_name": "1111111111111111111111125.jpg",
                            "bit_rate": 2114,
                            "current_size": 65535,
                            "path": "/test_share/WebDAV test/subfolder/test1/asd/1111111111111111.jpg",
                            "session_id": 3,
                            "status": "uploading",
                            "total_size": 295493,
                            "user_name": "username"
                        },
                        {
                            "base_name": "ans1.3.png",
                            "bit_rate": 1047,
                            "current_size": 358122,
                            "path": "/test_share/WebDAV test/subfolder/test2/ans1.3.png",
                            "session_id": 3,
                            "status": "uploading",
                            "total_size": 358122,
                            "user_name": "username"
                        }
                    ],
                    "server_merge_items": []
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get_recently_change'
        }

        return self.request_data(api_name, api_path, req_param)

    def set_pkg_config(
        self,
        pkg_volume: str,
        log_count: int = 20000,
        workers: int = 3,
        admin_mode: bool = True
    ) -> dict[str, object]:
        """
        Set package configuration settings.

            Parameters
            ----------
            pkg_volume : str
                The volume path where the package data will be stored (e.g., `/volume1`).

            log_count : int, optional
                Maximum number of logs retained per connection. Defaults to `20000`, max is `100000`.

            workers : int, optional
                Number of concurrent uploads allowed. Defaults to `3`, max is `20`.

            admin_mode : bool, optional
                Whether all users' tasks are retrieved or not. Defaults to `True`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the configuration update.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        admin_mode = 'enable' if admin_mode else 'disable'

        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set_global_config',
            'repo_vol_path': pkg_volume,
            'log_count': log_count,
            'worker_count': workers,
            'admin_mode': admin_mode,
        }

        return self.request_data(api_name, api_path, req_param)

    def set_relink_behavior(self, delete_from_cloud: bool) -> dict[str, object]:
        """
        Set the relinking behavior for personal user accounts.

            Warning: Miss-configuration of this action may lead to data loss.

            Parameters
            ----------
            delete_from_cloud : bool
                Set to `False` for "locally deleted files will be re-fetched from the cloud".

                Set to `True` for "locally deleted files will also be removed from the cloud".

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the relink behavior update.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set_personal_config',
            'sync_mode': delete_from_cloud
        }

        return self.request_data(api_name, api_path, req_param)

    def set_connection_settings(
        self,
        conn_id: str,
        task_name: str,
        pull_event_period: int = 60,
        max_upload_speed: int = 0,
        max_download_speed: int = 0,
        storage_class: str = '',
        isSSE: bool = False,
        part_size: int = 128
    ) -> dict[str, object]:
        """
        Set settings for a specific cloud connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            task_name : str
                The name of the cloud sync task.

            pull_event_period : int, optional
                Frequency (in seconds) to pull event updates. Defaults to `60`.

            max_upload_speed : int, optional
                Maximum upload speed in bytes. Defaults to `0` (unlimited).

            max_download_speed : int, optional
                Maximum download speed in bytes. Defaults to `0` (unlimited).

            storage_class : str, optional
                Cloud-specific storage class. Defaults to `''`.

            isSSE : bool, optional
                Enable Security Service Edge (SSE) for compatible cloud storage. Defaults to `False`.

            part_size : int, optional
                Part size for file uploads, in megabytes. Defaults to `128`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the updated connection settings.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': info['minVersion'],
            'method': 'set_connection_setting',
            'connection_id': conn_id,
            'task_name': task_name,
            'pull_event_period': pull_event_period,
            'max_upload_speed': max_upload_speed,
            'max_download_speed': max_download_speed,
            'storage_class': f'\"{storage_class}\"',
            'isSSE': isSSE,
            'part_size': part_size,
        }

        return self.request_data(api_name, api_path, req_param)

    def set_connection_schedule(
        self,
        conn_id: int,
        enable: bool,
        schedule_info: list[str] = []
    ) -> dict[str, object]:
        """
        Set the schedule for a specific connection.

            Parameters
            ----------
            conn_id : int
                The ID of the connection, obtained from `get_connections()`.

            enable : bool
                Whether the scheduling is enabled (`True`) or disabled (`False`).

            schedule_info : list[str], optional
                A list of 7 strings where each string represents a day of the week, going from Sunday to Saturday.

                Each string is composed of 24 characters, where each character is either '1' (enabled) or '0' (disabled) for the respective hour of the day.

                The default value (if `schedule_info` is not provided) enables all days and hours.

                Example format for enabling the schedule at every time and day:
                ```python
                # Keep this day order, Sunday to Saturday
                days = [
                    '111111111111111111111111', # sunday    - hours from 0 to 23
                    '111111111111111111111111', # monday    - hours from 0 to 23
                    '111111111111111111111111', # tuesday   - hours from 0 to 23
                    '111111111111111111111111', # wednesday - hours from 0 to 23
                    '111111111111111111111111', # thursday  - hours from 0 to 23
                    '111111111111111111111111', # friday    - hours from 0 to 23
                    '111111111111111111111111', # saturday  - hours from 0 to 23
                ]
                set_connection_schedule(conn_id=3, enable=True, schedule_info=days)
                ```

            Returns
            -------
            dict[str, object]
                A dictionary containing the schedule settings.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        if len(schedule_info) != 7 and len(''.join(schedule_info)) != 168:
            schedule_info = '1' * 24 * 7
        else:
            schedule_info = ''.join(schedule_info)

        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set_schedule_setting',
            'connection_id': conn_id,
            'is_enabled_schedule': enable,
            'schedule_info': f'\"{schedule_info}\"'
        }

        return self.request_data(api_name, api_path, req_param)

    def set_task_settings(
        self,
        sess_id: int,
        sync_direction: str,
        consistency_check: bool = True,
        no_delete_on_cloud: bool = True,
        convert_gd: bool = False
    ) -> dict[str, object]:
        """
        Set the task settings for a specific session.

            Parameters
            ----------
            sess_id : int
                The ID of the task, obtained from `get_tasks()`.

            sync_direction : str
                The synchronization direction.

                Possible values:
                - `ONLY_UPLOAD`: Upload local changes only.
                - `BIDIRECTION`: Sync both ways (upload and download).
                - `ONLY_DOWNLOAD`: Download remote changes only.

            consistency_check : bool, optional
                If True, enables advanced consistency check (requires more resources). Defaults to `True`.

            no_delete_on_cloud : bool, optional
                If `True`, prevents deletion of files in the remote folder when removed from the local directory. Defaults to `True`.

            convert_gd : bool, optional
                If `True`, converts Google Drive Online documents to Microsoft Office format. Defaults to `False`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task settings configuration.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set_session_setting',
            'session_id': sess_id,
            'sync_direction': sync_direction,
            'sync_attr_check_option': consistency_check,
            'no_delete': no_delete_on_cloud,
            'google_drive_convert_online_doc': convert_gd
        }

        return self.request_data(api_name, api_path, req_param)

    def set_task_filters(
        self,
        sess_id: int,
        filtered_paths: list[str] = [],
        filtered_filenames: list[str] = [],
        filtered_extensions: list[str] = [],
        max_upload_size: int = 0
    ) -> dict[str, object]:
        """
        Set task filters for selective synchronization in a specific session.

            Parameters
            ----------
            sess_id : int
                The ID of the session, obtained from `get_tasks()`.

            filtered_paths : list[str], optional
                A list of paths (directories / subdirectories) to exclude from the synchronization process, e.g, `['/images', '/videos/movies']`. Defaults to `[]`.

            filtered_filenames : list[str], optional
                A list of filenames to exclude from synchronization. Defaults to `[]`.

            filtered_extensions : list[str], optional
                A list of file extensions to exclude from synchronization, e.g., `['mp3', 'iso', 'mkv']`. Defaults to `[]`.
            max_upload_size : int, optional
                The maximum file size for uploads, in bytes. Files larger than this size will be excluded from synchronization. Defaults to `0` (no size limit).

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task filters configuration.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        # Using json.dumps() to convert from list to str to match the '["text"]' format the API is waiting for. Otherwise, error 120 is raised.
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set_selective_sync_config',
            'session_id': sess_id,
            'filtered_paths': json.dumps(filtered_paths),
            'filtered_names': json.dumps(filtered_filenames),
            'filtered_extensions': json.dumps(filtered_extensions),
            'user_defined_names': json.dumps(filtered_filenames),
            'user_defined_extensions': json.dumps(filtered_extensions),
            'filtered_max_upload_size': max_upload_size,
        }

        return self.request_data(api_name, api_path, req_param)

    def connection_pause(self, conn_id: int = -1) -> dict[str, object]:
        """
        Pause one or all connections.

            Parameters
            ----------
            conn_id : int, optional
                The ID of the connection to pause. If not specified or set to `-1`, all connections will be paused.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the pause action.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'pause'
        }

        if conn_id > -1:
            req_param['connection_id'] = conn_id

        return self.request_data(api_name, api_path, req_param)

    def connection_resume(self, conn_id: int = -1) -> dict[str, object]:
        """
        Resume one or all connections.

            Parameters
            ----------
            conn_id : int, optional
                The ID of the connection to resume. If not specified or set to `-1`, all connections will be resumed.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the resume action.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'resume'
        }

        if conn_id > -1:
            req_param['connection_id'] = conn_id

        return self.request_data(api_name, api_path, req_param)

    def connection_remove(self, conn_id: int) -> dict[str, object]:
        """
        Remove a specific connection and all associated tasks.

            The data will remain in both the local and remote directories.

            Parameters
            ----------
            conn_id : int
                The ID of the connection to be removed, obtained from `get_connections()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the remove action.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'unlink_connection',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

    def task_remove(
        self,
        conn_id: int,
        sess_id: int
    ) -> dict[str, object]:
        """
        Remove a specific task.

            The data will remain in both the local and remote directories.

            Parameters
            ----------
            conn_id : int
                The ID of the connection associated with the task, obtained from `get_connections()`.
            sess_id : int
                The ID of the task to be removed, obtained from `get_tasks()`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task removal.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'unlink_session',
            'connection_id': conn_id,
            'session_id': sess_id
        }

        return self.request_data(api_name, api_path, req_param)

    def __generate_sync_task_s3_params(
        self,
        conn_id: int,
        local_path: str,
        cloud_path: str,
        sync_direction='BIDIRECTION',
        storage_class='STANDARD',
        file_filter: list[str] = [],
        filter_max_upload_size: int = 0,
        filter_names: list[str] = [],
        server_folder_id: str = '',
    ) -> dict[str, Any]:
        """
        Generate parameters for creating a sync task with S3.

            Parameters
            ----------
            conn_id : int
                The ID of the connection.

            local_path : str
                The local path to sync.

            cloud_path : str
                The cloud path to sync.

            sync_direction : str, optional
                The synchronization direction. Defaults to `'BIDIRECTION'`.

            storage_class : str, optional
                The storage class. Defaults to `'STANDARD'`.

            file_filter : list[str], optional
                List of file extensions to filter. Defaults to `[]`.

            filter_max_upload_size : int, optional
                Maximum upload size for files. Defaults to `0`.

            filter_names : list[str], optional
                List of file names to filter. Defaults to `[]`.

            server_folder_id : str, optional
                The unique identifier of the remote (cloud) folder to be synchronized. Defaults ``.

            Returns
            -------
            dict[str, Any]
                A dictionary containing the parameters for the sync task.
        """
        # Validate local path format
        if local_path[0] != '/' or local_path.count('/') < 2:
            raise ValueError(
                'Invalid local path, must be in format /<share_folder>/<sub_directory>')

        # Validate cloud path format
        if cloud_path[0] != '/' or cloud_path[-1] == '/':
            raise ValueError(
                'Invalid cloud path, must be started with / and not ended with /')

        # Get connection authentication details
        auth = self.get_connection_auth(conn_id)

        # Extract path components
        path_share = local_path.split('/')[1]
        path_sync = local_path[local_path.index('/', 1):]

        # Build request parameters
        create_session_request_params = {
            'path': local_path,
            'path_share': path_share,
            'path_sync': path_sync,
            'filter_file': {
                'filtered_extensions': file_filter,
                'filtered_max_upload_size': filter_max_upload_size,
                'filtered_names': filter_names
            },
            'sync_direction': sync_direction,
            'server_folder': cloud_path,
            'server_folder_path': cloud_path,
            'server_folder_id': server_folder_id,
            'part_size': '',
            'storage_class': storage_class,
            'server_folder_meta_list': make_folder_meta_list_from_path(cloud_path),
            'filter_folder': [],
            'filter_changed': False,
            'no_delete': False,
            'isSSE': False,
            'server_encryption': False,
            'sync_attr_check_option': True,
            'mode_add_session': True,
        }

        # Merge authentication details with request parameters
        return merge_dicts(auth['data'], create_session_request_params)

    def create_sync_task_s3(
        self,
        conn_id: int,
        local_path: str,
        cloud_path: str,
        sync_direction='BIDIRECTION',
        storage_class='STANDARD',
        file_filter: list[str] = [],
        filter_max_upload_size: int = 0,
        filter_names: list[str] = [],
    ) -> tuple[bool, Any]:
        """
        Add a new synchronization task.

            Parameters
            ----------
            conn_id : int
                The ID of the connection.

            local_path : str
                The local path to sync.

            cloud_path : str
                The cloud path to sync.

            sync_direction : str, optional
                The synchronization direction. Defaults to `'BIDIRECTION'`.

            storage_class : str, optional
                The storage class. Defaults to `'STANDARD'`.

            file_filter : list[str], optional
                List of file extensions to filter. Defaults to `[]`.

            filter_max_upload_size : int, optional
                Maximum upload size for files. Defaults to `0`.

            filter_names : list[str], optional
                List of file names to filter. Defaults to `[]`.

            Returns
            -------
            tuple[bool, Any]
                A tuple containing the result of the task creation.
        """

        # Validate is connection is Amazon S3
        conn_info = self.get_connection_information(conn_id)
        if conn_info['data']['type'] != 'az':
            return (False, 'Connection is not Amazon S3')

        # Merge authentication details with request parameters
        creation_params = self.__generate_sync_task_s3_params(
            conn_id,
            local_path,
            cloud_path,
            sync_direction,
            storage_class,
            file_filter,
            filter_max_upload_size,
            filter_names
        )
        # Prepare API request data
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        # Run test task setting
        test_result = self.test_task_setting(
            conn_id,
            local_path,
            cloud_path,
            sync_direction,
            storage_class,
            file_filter,
            filter_max_upload_size,
            filter_names
        )
        if not test_result[0]:
            return (False, test_result[1])

        create_session_request = {
            'api': api_name,
            'method': 'create_session',
            'version': info['minVersion'],
            'conn_info': creation_params,
        }
        list_session_request = {
            'api': api_name,
            'method': 'list_sess',
            'version': info['minVersion'],
            'connection_id': conn_id
        }
        # Compound data
        compound_data = [create_session_request, list_session_request]
        # Send request and return response
        return (True, self.batch_request(compound_data, method='post'))

    def test_task_setting(
        self,
        conn_id: int,
        local_path: str,
        cloud_path: str,
        sync_direction='BIDIRECTION',
        storage_class='STANDARD',
        file_filter: list[str] = [],
        filter_max_upload_size: int = 0,
        filter_names: list[str] = [],
    ) -> tuple[bool, dict[str, object] | str]:
        """
        Test the task settings make sure they are valid.

            Parameters
            ----------
            conn_id : int
                The ID of the connection.

            local_path : str
                The local path to sync.

            cloud_path : str
                The cloud path to sync.

            sync_direction : str, optional
                The synchronization direction. Defaults to `'BIDIRECTION'`.

            storage_class : str, optional
                The storage class. Defaults to `'STANDARD'`.

            file_filter : list[str], optional
                List of file extensions to filter. Defaults to `[]`.

            filter_max_upload_size : int, optional
                Maximum upload size for files. Defaults to `0`.

            filter_names : list[str], optional
                List of file names to filter. Defaults to `[]`.

            Returns
            -------
            tuple[bool, dict[str, object] | str]
                A tuple containing a boolean indicating success, and a dictionary or string with the result.
        """
        # Generate sync task parameters
        creation_params = self.generate_sync_task_s3_params(
            conn_id,
            local_path,
            cloud_path,
            sync_direction,
            storage_class,
            file_filter,
            filter_max_upload_size,
            filter_names
        )

        # Prepare API request data
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        request_params = {
            'api': api_name,
            'method': 'test_task_setting',
            'version': info['minVersion'],
            'conn_info': creation_params
        }

        # Send request and get result
        compound_data = [request_params]
        result = self.batch_request(compound_data, method='post')

        # Check if the request was successful
        if result is not None and result['data']['has_fail'] == False:
            # print('Task setting is valid')
            return (True, result['data'])
        else:
            # print('Task setting is invalid')
            return (False, 'Invalid task setting')
