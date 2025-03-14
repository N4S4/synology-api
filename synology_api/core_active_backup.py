from __future__ import annotations
from typing import Optional
from . import base_api

import time
import json


class ActiveBackupBusiness(base_api.BaseApi):

    def list_vm_hypervisor(self) -> dict[str, object] | str:
        '''
        This function returns a list of list of all configured hypervisors present in ABB.
        '''
        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def list_device_transfer_size(self, 
                                  time_start: int = int(time.time() - 86400), 
                                  time_end: int = int(time.time())) -> dict[str, object] | str:
        '''
        This function returns a list of all devices and their respective transfer size for the given time frame. Default value is 24 hours.
        '''
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_device_transfer_size',
                     'time_start': time_start,
                     'time_end': time_end}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_list(self, load_versions: bool = False, filter: dict[str, any] = {}) -> dict[str, object] | str:
        '''
        This function returns a list of all tasks. Can also retrieve versions corresponding to each task with the `load_versions` parameter.
        
        `filter` can be used to retrieve only specific information:
        
        filter: dict[str, any] = {}
            "task_id": int,
            "backup_type": int,
            "load_available": bool,
            "limit": int,
            "is_snapshot": bool,
            etc..
         
        '''
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                    'method': 'list',
                    'load_status': 'true',
                    'load_result': 'true',
                    'load_versions': load_versions,
                    'filter': json.dumps(filter)}

        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_run(self, task_ids: list[int]) -> dict[str, object] | str:
        '''
        This function will trigger a backup event for the given tasks. Even if only one task is specified, a list has to be passed as argument.
        '''
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'backup',
                     'task_ids': str(task_ids),
                     'trigger_type': '1'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_cancel(self, task_ids: list[int]) -> dict[str, object] | str:
        '''
        This function will trigger a cancel backup event for the given tasks. Even if only one task is specified, a list has to be passed as argument.
        '''
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'cancel',
                     'task_ids': str(task_ids)}
        
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_remove(self, task_ids: list[int]) -> dict[str, object] | str:
        '''
        This function will trigger a task deletion event for the given tasks. Even if only one task is specified, a list has to be passed as argument.
        '''
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'remove',
                     'task_ids': str(task_ids)}
        
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_delete_versions(self, task_id: int, versions_ids: list[int]) -> dict[str, object] | str:
        '''
        This function will trigger a version deletion event for the given version. Even if only one version is specified, a list has to be passed as argument.
        '''
        api_name = 'SYNO.ActiveBackup.Version'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'delete',
                     'task_id': task_id,
                     'version_ids': str(versions_ids)}
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_activity_logs(
            self, 
            offset: int = 0, 
            limit: int = 200,
            log_level: int = -1,
            keyword: str = "",
            from_date: int = 0,
            to_date: int = 0
        ) -> dict[str, object]:
        """Get package general logs.

            Parameters
            ----------
            offset : int, optional
                Offset results by this value. Defaults to `0`.
            
            limit : int, optional
                Amount of results to be returned. Defaults to `200`.
            
            log_level : int, optional
                Type of logs to return. Defaults to `-1` (all types).

                Possible values:  
                - `0` -> Error
                - `1` -> Warning
                - `2` -> Information

            keyword : str, optional
                Keyword used to filter the results. Defaults to `""`.

            from_date : int, optional
                Date from which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            to_date : int, optional
                Date until which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).

            Returns
            -------
            dict[str, object]
                Disctionary containing a list of logs.

            Example return
            --------------
            ```json
            {
                "count": 1,
                "logs": [
                    {
                        "backup_type": 4,
                        "device_id": 6,
                        "device_name": "xxxx",
                        "error_code": 0,
                        "log_id": 5525,
                        "log_level": 0,
                        "log_time": 1741897498,
                        "log_type": 1104,
                        "other_params": {
                            "backup_type": 4,
                            "device_id": 6,
                            "device_name": "xxxx",
                            "platform_type": 0,
                            "task_id": 8,
                            "task_name": "xxxxxxxx",
                            "user_id": 0,
                            "user_name": ""
                        },
                        "result_id": 592,
                        "task_id": 8,
                        "task_name": "xxxxxxxx",
                        "user_id": 0,
                        "user_name": ""
                    }
                ]
            }
            ```
        """
        filter = {}
        if keyword != "":
            filter['key_word'] = keyword
        if log_level > -1:
            filter['log_level'] = log_level
        if from_date > 0: 
            filter['from_timestamp'] = from_date
        if to_date > 0: 
            filter['to_timestamp'] = to_date

        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list_log',
            'offset': offset,
            'limit': limit,
            'filter': json.dumps(filter)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_logs(self, filter: dict[str, any] = {}) -> dict[str, object] | str:
        '''
        This function returns a dictionary of the logs of all tasks.
        
        `filter` can be used to retrieve only specific information:
        
        filter: dict[str, any] = {}
            "task_id": int,
            "backup_type": int,
            "load_available": bool,
            "limit": int,
            "is_snapshot": bool,
            etc..
         
        '''
        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_result',
                     'filter': json.dumps(filter)}
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_logs_details(self, 
                          result_id: int, 
                          limit: int = 500, 
                          order_by: str = "log_level", 
                          direction: str = "ASC") -> dict[str, object] | str:
        '''
        This function returns a dictionary of the logs of a given task event. `result_id` can be retrieved from `list_logs()` function.
        '''
        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_result_detail',
                     'result_id': result_id,
                     'limit': limit,
                     'order_by': order_by,
                     'direction': direction}
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_storage(self) -> dict[str, object] | str:
        '''
        This function returns a dictionary of the current storages being used by ABB.
        '''
        api_name = 'SYNO.ActiveBackup.Share'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_storage'}

        return self.request_data(api_name, api_path, req_param)
    
