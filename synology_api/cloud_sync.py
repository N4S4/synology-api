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

    def get_config(self) -> dict[str, object] | str:
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
