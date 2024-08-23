from __future__ import annotations
from . import base_api


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
    """

    def get_pkg_config(self) -> dict[str, object] | str:
        """Retrieve package settings.

        Returns:
            (dict || str): A dictionary containing the result of the schedule configuration, or a string in case of an error.

            Example return:
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
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_config'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connections(self, group_by: str = 'group_by_user') -> dict[str, object] | str:
        """Retrieve a list of current cloud connections.

        Parameters
        ----------
        group_by : str, optional
            Method to group the connections, by user or cloud type. Default is `'group_by_user'`.

        Returns
        -------
        dict or str
            A dictionary containing the list of cloud connections, or a string in case of an error.
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
    
    def get_connection_settings(self, conn_id: int) -> dict[str, object] | str:
        """Retrieve settings for a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.

        Returns
        -------
        dict or str
            A dictionary containing the connection settings, or a string in case of an error.
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
    
    def get_connection_information(self, conn_id: int) -> dict[str, object] | str:
        """Retrieve information for a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.

        Returns
        -------
        dict or str
            A dictionary containing connection information, or a string in case of an error.
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
    
    def get_connection_auth(self, conn_id: int) -> dict[str, object] | str:
        """Retrieve authentication information for a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.

        Returns
        -------
        dict or str
            A dictionary containing the authentication details, or a string in case of an error.
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
        ) -> dict[str, object] | str:
        """Retrieve logs for a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.
        keyword : str, optional
            A keyword to filter logs. Default is an empty string.
        date_from : int, optional
            The starting date in epoch format. Default is 0.
        date_to : int, optional
            The ending date in epoch format. Default is 0.
        log_level : int, optional
            Log level filter. Default is -1 (All). Possible values:
            - -1: All
            - 0: Info
            - 1: Warning
            - 2: Error
        action : int, optional
            Action filter. Default is -1 (All). Possible values:
            - -1: All
            - 0: Delete Remote
            - 1: Download
            - 2: Upload
            - 3: Delete Local
            - 4: Rename Remote
            - 8: Merge
            - 9: Merge Deletion
        offset : int, optional
            Log offset for pagination. Default is 0.
        limit : int, optional
            Number of logs to retrieve. Default is 200.

        Returns
        -------
        dict or str
            A dictionary containing the logs, or a string in case of an error.
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

    def get_tasks(self, conn_id: int) -> dict[str, object] | str:
        """Retrieve a list of tasks related to a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.

        Returns
        -------
        dict or str
            A dictionary containing the list of tasks, or a string in case of an error.
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
    
    def get_task_filters(self, sess_id: int) -> dict[str, object] | str:
        """Retrieve filter information for a specific task.

        Parameters
        ----------
        sess_id : int
            The ID of the task, obtained from `get_tasks()`.

        Returns
        -------
        dict or str
            A dictionary containing task filter information, or a string in case of an error.
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
        ) -> dict[str, object] | str:
        """Retrieve a list of child directories in the cloud for a specific task.

        Parameters
        ----------
        sess_id : int
            The ID of the task, obtained from `get_tasks()`.
        remote_folder_id : str
            The ID of the remote folder, obtained from `get_tasks()`.
        path : str, optional
            The folder path to retrieve the child directories from. Default is root `'/'`.

        Returns
        -------
        dict or str
            A dictionary containing the list of child directories, or a string in case of an error.
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
    
    def get_recently_modified(self) -> dict[str, object] | str:
        """Retrieve the 5 latest modified files and the currently syncing items.

        Returns
        -------
        dict or str
            A dictionary containing the recently modified files, or a string in case of an error.
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
        ) -> dict[str, object] | str:
        """Set package configuration settings.

        Parameters
        ----------
        pkg_volume : str
            The volume path where the package data will be stored (e.g., "/volume1").
        log_count : int, optional
            Maximum number of logs retained per connection. Default is 20000, max is 100000.
        workers : int, optional
            Number of concurrent uploads allowed. Default is 3, max is 20.
        admin_mode : bool, optional
            Whether all users' tasks are retrieved or not. Default is True.

        Returns
        -------
        dict or str
            A dictionary containing the result of the configuration update, or a string in case of an error.
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
    
    def set_relink_behavior(self, sync_mode: bool = False) -> dict[str, object] | str:
        """Set the relinking behavior for personal user accounts.

        Parameters
        ----------
        sync_mode : bool, optional
            If `False` (default), locally deleted files will be re-fetched from the cloud.
            If `True`, locally deleted files will also be removed from the cloud.

        Returns
        -------
        dict or str
            A dictionary containing the relink behavior settings, or a string in case of an error.
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'set_personal_config',
            'sync_mode': sync_mode
        }

        return self.request_data(api_name, api_path, req_param) 
    
    def set_connection_settings(
            self, 
            conn_id: int,
            task_name: str,
            pull_event_period: int = 60,
            max_upload_speed: int = 0,
            max_download_speed: int = 0,
            storage_class: str = '',
            isSSE: bool = False,
            part_size: int = 128
        ) -> dict[str, object] | str:
        """Set settings for a specific cloud connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.
        task_name : str
            The name of the cloud sync task.
        pull_event_period : int, optional
            Frequency (in seconds) to pull event updates. Default is 60.
        max_upload_speed : int, optional
            Maximum upload speed in bytes. Default is 0 (unlimited).
        max_download_speed : int, optional
            Maximum download speed in bytes. Default is 0 (unlimited).
        storage_class : str, optional
            Cloud-specific storage class.
        isSSE : bool, optional
            Enable Security Service Edge (SSE) for compatible cloud storage. Default is False.
        part_size : int, optional
            Part size for file uploads, in megabytes. Default is 128.

        Returns
        -------
        dict or str
            A dictionary containing the updated connection settings, or a string in case of an error.
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'set_connection_setting',
            'conn_id': conn_id,
            'task_name': task_name,
            'pull_event_period': pull_event_period,
            'max_upload_speed': max_upload_speed,
            'max_download_speed': max_download_speed,
            'storage_class': storage_class,
            'isSSE': isSSE,
            'part_size': part_size,
        }

        return self.request_data(api_name, api_path, req_param) 
    
    def set_connection_schedule(
            self, 
            conn_id: int,
            enable: bool,
            schedule_info: list[str] = []
        ) -> dict[str, object] | str:
        """Set the schedule for a specific connection.

        Parameters
        ----------
        conn_id : int
            The ID of the connection, obtained from `get_connections()`.
        enable : bool
            Whether the scheduling is enabled (`True`) or disabled (`False`).
        schedule_info : list of str, optional
            A list of 7 strings where each string represents a day of the week, going from Sunday to Saturday.

            Each string is composed of 24 characters, where each character is either '1' (enabled) or '0' (disabled) for the respective hour of the day.
            
            The default value (if `schedule_info` is not provided) enables all days and hours.

        Returns
        -------
        dict or str
            A dictionary containing the schedule settings, or a string in case of an error.
        
        Example
        -------
        Function usage for enabling the schedule at every time and day:
        >>> # Keep this day order, Sunday to Saturday
        ... days = [
        ...     '111111111111111111111111', # sunday    - hours from 0 to 23
        ...     '111111111111111111111111', # monday    - hours from 0 to 23
        ...     '111111111111111111111111', # tuesday   - hours from 0 to 23
        ...     '111111111111111111111111', # wednesday - hours from 0 to 23
        ...     '111111111111111111111111', # thursday  - hours from 0 to 23
        ...     '111111111111111111111111', # friday    - hours from 0 to 23
        ...     '111111111111111111111111', # saturday  - hours from 0 to 23
        ... ]
        ... set_connection_schedule(task_id=2, enable=True, schedule_info=days)
        """
        if len(schedule_info) != 7 and len(''.join(schedule_info) != 168):
            schedule_info = '1' * 24 * 7
        else:
            schedule_info = ''.join(schedule_info)

        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'set_schedule_setting',
            'conn_id': conn_id,
            'is_enabled_schedule': enable,
            'schedule_info': schedule_info
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_task_settings(
            self,
            sess_id: int, 
            sync_direction: str,
            consistency_check: bool = True,
            no_delete_on_cloud: bool = True,
            convert_gd: bool = False
        ) -> dict[str, object] | str:
        """Set the task settings for a specific session.

        Parameters
        ----------
        sess_id : int
            The ID of the task, obtained from `get_tasks()`.
        sync_direction : str
            The synchronization direction. Possible values:
            - "ONLY_UPLOAD": Upload local changes only.
            - "BIDIRECTION": Sync both ways (upload and download).
            - "ONLY_DOWNLOAD": Download remote changes only.
        consistency_check : bool, optional
            If True, enables advanced consistency check (requires more resources), by default True.
        no_delete_on_cloud : bool, optional
            If True, prevents deletion of files in the destination folder when removed from the source, by default True.
        convert_gd : bool, optional
            If True, converts Google Drive Online documents to Microsoft Office format, by default False.

        Returns
        -------
        dict or str
            A dictionary containing the result of the task settings configuration, or a string in case of an error.
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'set_session_setting',
            'sess_id': sess_id,
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
        ) -> dict[str, object] | str:
        """Set task filters for selective synchronization in a specific session.

        Parameters
        ----------
        sess_id : int
            The ID of the session, obtained from `get_tasks()`.
        filtered_paths : list[str], optional
            A list of paths (directories / subdirectories) to exclude from the synchronization process, by default an empty list.
        filtered_filenames : list[str], optional
            A list of filenames to exclude from synchronization, by default an empty list.
        filtered_extensions : list[str], optional
            A list of file extensions to exclude from synchronization, e.g., ['mp3', 'iso', 'mkv'], by default an empty list.
        max_upload_size : int, optional
            The maximum file size for uploads, in bytes. Files larger than this size will be excluded from synchronization, by default 0 (no size limit).

        Returns
        -------
        dict or str
            A dictionary containing the result of the task filters configuration, or a string in case of an error.
        """
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'set_selective_sync_config',
            'sess_id': sess_id,
            'filtered_paths': filtered_paths,
            'filtered_names': filtered_filenames,
            'filtered_extensions': filtered_extensions,
            'user_defined_names': '[]',         # Leave this empty cause the params have to be sent in filtered_names anyways
            'user_defined_extensions': '[]',    # Leave this empty cause the params have to be sent in filtered_extensions anyways 
            'filtered_max_upload_size': max_upload_size,
        }

        return self.request_data(api_name, api_path, req_param) 
    
    def connection_pause(self, conn_id: int = -1) -> dict[str, object] | str:
        """Pause one or all connections.

        Parameters
        ----------
        conn_id : int, optional
            The ID of the connection to pause. If not specified or set to -1, all connections will be paused.

        Returns
        -------
        dict or str
            A dictionary containing the result of the pause action, or a string in case of an error.
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
    
    def connection_resume(self, conn_id: int = -1) -> dict[str, object] | str:
        """Resume one or all connections.

        Parameters
        ----------
        conn_id : int, optional
            The ID of the connection to resume. If not specified or set to -1, all connections will be resumed.

        Returns
        -------
        dict or str
            A dictionary containing the result of the resume action, or a string in case of an error.
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
    
    def connection_remove(self, conn_id: int) -> dict[str, object] | str:
        """Remove a specific connection and all associated tasks.

        The data will remain in both the local and remote directories.

        Parameters
        ----------
        conn_id : int
            The ID of the connection to be removed, obtained from `get_connections()`.

        Returns
        -------
        dict or str
            A dictionary containing the result of the remove action, or a string in case of an error.
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
        ) -> dict[str, object] | str:
        """Remove a specific task.

        The data will remain in both the local and remote directories.

        Parameters
        ----------
        conn_id : int
            The ID of the connection associated with the task, obtained from `get_connections()`.
        sess_id : int
            The ID of the task to be removed, obtained from `get_tasks()`.

        Returns
        -------
        dict or str
            A dictionary containing the result of the task removal, or a string in case of an error.
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