from __future__ import annotations
from . import base_api
import json


class TaskScheduler(base_api.BaseApi):
    """
       Task Scheduler API implementation.

       This API provides the functionality to get information related to the scheduler settings and current tasks.

       For the moment, the available actions with the API are:
       - Get all tasks
       - Get task information
       - Get task results
       - Get task result log
       - Enable/Disable task
       - Run task
       - Delete task
       - Get/Set output path for task results
       - Create task
       - Set task settings 

       To implement in the future:
       - Add retention settings for Recycle bin task set/create methods.
    """

    def get_task_list(
            self,
            sort_by: str = 'next_trigger_time',
            sort_direction: str = 'ASC',
            offset: int = 0,
            limit: int = 50
        ) -> dict[str, object] | str:
        """List all present tasks.

        Args:
            sort_by (str, optional): 
                The field to sort tasks by. Defaults to `"next_trigger_time"`.
                Possible values:
                - "next_trigger_time"
                - "name"
                - "type"
                - "action"
                - "owner"
            sort_direction (str, optional): 
                The sort direction. Defaults to `"ASC"`.
                Possible values:
                - "ASC"
                - "DESC"
            offset (int, optional): 
                Task offset for pagination. Defaults to `0`.
            limit (int, optional): 
                Number of tasks to retrieve. Defaults to `50`.

        Returns:
            dict|str:
                A dictionary containing a list of the tasks and information related to them, or a string in case of an error.

            Example return:
            {
                "data": {
                    "tasks": [
                        {
                            "action": "Run: rsync -aP --delete /volume1/test/ /volume1/test2/",
                            "can_delete": true,
                            "can_edit": true,
                            "can_run": true,
                            "enable": false,
                            "id": 13,
                            "name": "Sync folders",
                            "next_trigger_time": "2024-09-09 12:26",
                            "owner": "root",
                            "real_owner": "root",
                            "type": "script"
                        },
                        {
                            "action": "Run: echo hello > /tmp/awacate.out",
                            "can_delete": true,
                            "can_edit": true,
                            "can_run": true,
                            "enable": true,
                            "id": 11,
                            "name": "TEST_CRONTAB",
                            "next_trigger_time": "2024-09-10 00:00",
                            "owner": "root",
                            "real_owner": "root",
                            "type": "script"
                        }
                    ]
                    "total": 2
                },
                "success": true
            }
        """
        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 3, 
            'method': 'list',
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'offset': offset,
            'limit': limit
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_output_config(self) -> dict[str, object] | str:
        """
        """
        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'config_get',
            'type': 'esynoscheduler'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_task_config(
            self,
            task_id: int,
            real_owner: str
        ) -> dict[str, object] | str:
        """
        """
        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4, 
            'method': 'get',
            'id': task_id,
            'real_owner': real_owner
            
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_task_results(
            self,
            task_id: int
        ) -> dict[str, object] | str:
        """
        """
        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'get_history_status_list',
            'id': task_id
            
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_task_result_logs(
            self,
            task_id: int,
            timestamp: int
        ) -> dict[str, object] | str:
        """
        """
        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'get_history_log',
            'timestamp': str(timestamp),
            'id': task_id
        }

        return self.request_data(api_name, api_path, req_param)
    
