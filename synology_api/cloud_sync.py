from __future__ import annotations
from . import base_api


class CloudSync(base_api.BaseApi):
    '''
       Cloud Sync API implementation.

       This API provides the functionality to get information related to the package settings and current connections and tasks. 
       It also provides functionalities to set most of the settings for tasks and package configuration, as well as manage the current syncing processes.

       Due to the vast amount of public clouds available in the project, the API was not tested for every cloud scenario, so some params request may be missing in specific not tested clouds.

       The tested clouds so far are:
       - Google Drive  
       - OneDrive
       - DropBox
    '''

    def get_pkg_config(self) -> dict[str, object] | str:
        '''
        Return package settings.
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_config'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connections(self, group_by: str = 'group_by_user') -> dict[str, object] | str:
        '''
        Return list of current cloud connections.

        group_by = 'group_by_user' ||  'group_by_cloud_type'
        '''
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
        '''
        Return settings from a given connection.

        conn_id = int from get_connections
        '''
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
        '''
        Return information from a given connection.

        conn_id = int from get_connections
        '''
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
        '''
        Return authentication information from a given connection.

        conn_id = int from get_connections
        '''
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
        '''
        Return logs from a given connection.

        conn_id = int from get_connections
        date_from = int (epoch date)
        date_to = int (epoch date)
        log_level = int => (-1 => All, 0 => Info, 1=> Warning, 2 => Error)
        action = int => (
            -1 => All, 
            0 => Delete Remote, 
            1 => Download, 
            2 => Upload,
            3 => Delete Local,
            4 => Rename Remote,
            8 => Merge,
            9 => Merge Deletion, 
        )
        '''
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
        '''
        Return list of tasks related to given cloud connection.

        conn_id = int from get_connections
        '''
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
        '''
        Return filter information for given task.

        sess_id = int from get_tasks
        '''
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
        '''
        Return list of children directories in Cloud for given task.

        remote_folder_id = str from get_tasks
        path = str (the folder from which we want the children, default is the task root path)
        '''
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
        '''
        Return a list of the 5 latest modified files and the currently syncing items.
        '''
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
        '''
        Set package settings.

        pkg_volume = str (where package data will be stored, eg "/volume1")
        log_count = int (max number of logs retained in each connection, max is 100k)
        workers = int (max number of concurrent uploads, min is 3, max is 20)
        admin_mode = bool (defines whether admins can see all users tasks or not, default is True)
        '''
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
        '''
        Set personal user relinking behavior.

        Getter is `get_pkg_config()`.

        sync_mode = bool (
            False => Locally deleted files will be re-fetched from your public cloud,
            True => Locally deleted files will be removed from your public cloud
        )
        '''
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
        '''
        Set connection settings.

        pull_event_period: int = 60, default cahnges from cloud to cloud
        max_upload_speed: int = 0, in bytes
        max_download_speed: int = 0, in bytes
        storage_class: str = '',
        isSSE: bool = False, for security service edge enabled clouds
        part_size: int = 128
        '''
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
        '''
        Set connection schedule.

        conn_id: int,
        is_enabled_schedule: bool,
        schedlue_info: list[str] Default value is all days and hours enabled. => A list of 7 strings, composed of 1 and 0, each digit represents an hour of a day. Each day is represented by 24 digits, 1 being enabled, 0 being disabled:

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
        
        set_connection_schedule(task_id=2, enable=True, schedule_info=days)
        ```
        '''
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
        '''
        Set task settings.

        sync_direction: str = "ONLY_UPLOAD" || "BIDIRECTION" || "ONLY_DOWNLOAD",
        consistency_check: bool = True, (Enable advanced consistency check (more resources required))
        no_delete_on_cloud: bool = True, (Don't remove files in the destination folder when they are removed in the source folder.)
        convert_gd: bool = False (convert Google Drive Online documents to Microsoft Office)
        '''
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
        '''
        Set task settings.

        filtered_paths: list[str] = [], ["/path name"]
        filtered_names: list[str] = [], ["something"]
        filtered_extensions: list[str] = [], ["mp3", "iso", "mkv"]
        max_upload_size: int = 0, in bytes 
        '''
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
    
    def connection_pause(self, conn_id: int = 0) -> dict[str, object] | str:
        '''
        Pause one or all connections.

        Pause all connections if connection ID is not specified.
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'pause'
        }
        
        if conn_id > 0:
            req_param['connection_id'] = conn_id

        return self.request_data(api_name, api_path, req_param)
    
    def connection_resume(self, conn_id: int = 0) -> dict[str, object] | str:
        '''
        Resume one or all connections.

        Resume all connections if connection ID is not specified.
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'resume'
        }
        
        if conn_id > 0:
            req_param['connection_id'] = conn_id

        return self.request_data(api_name, api_path, req_param)
    
    def connection_remove(self, conn_id: int) -> dict[str, object] | str:
        '''
        Remove one given connection and all its tasks.

        Data remains in both local and remote directories.
        '''
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
        '''
        Remove one given task.

        Data remains in both local and remote directories.
        '''
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