from __future__ import annotations
from . import base_api
import json

class _Schedule():
    def __init__(
            self,
            run_frequently: bool = True, # date_type
            run_days: str = '0,1,2,3,4,5,6', # week_days
            run_date: str = '', # date
            repeat: str = 'Daily',
            monthly_week: list[str] = [],
            start_time_h: int = 0,
            start_time_m: int = 0,
            same_day_repeat_h: int = 0,
            same_day_repeat_m: int = 0,
            same_day_repeat_until: int = 0,
        ):
        self.run_frequently = run_frequently
        self.run_days = run_days
        self.run_date = run_date
        self.repeat = repeat
        self.monthly_week = monthly_week
        self.start_time_h = start_time_h
        self.start_time_m = start_time_m
        self.same_day_repeat_h = same_day_repeat_h
        self.same_day_repeat_m = same_day_repeat_m
        self.same_day_repeat_until = same_day_repeat_until

    def _generate_dict(self) -> dict:
        schedule_dict = {
            'date_type': 0 if self.run_frequently else 1,
            'monthly_week': json.dumps(self.monthly_week),
            'hour': self.start_time_h,                    # Start time - Hour for the schedule
            'minute': self.start_time_m,                  # Start time - Minute for the schedule
            'repeat_hour': self.same_day_repeat_h,        # Continue running on the same day - Repeat each X hours 0..23 
            'repeat_min': self.same_day_repeat_m,         # Continue running on the same day - Repeat every X minute [1, 5, 10, 15, 20, 30] // 0 = disabled
            'last_work_hour': self.same_day_repeat_until if self.same_day_repeat_until > -1 else self.start_time_h, # Last run time, defaults to start time if not provided
        }
        repeat_modality = -1

        if self.run_frequently:
            if self.repeat == 'daily':
                repeat_modality = 1001 
            if self.repeat == 'weekly':
                repeat_modality = 1002
            if self.repeat == 'monthly':
                repeat_modality = 1003
            
            schedule_dict['week_day'] = self.run_days
        else:
            if self.repeat == 'no_repeat':
                repeat_modality = 0 
            if self.repeat == 'monthly':
                repeat_modality = 1
            if self.repeat == 'every_3_months':
                repeat_modality = 5
            if self.repeat == 'every_6_months':
                repeat_modality = 3
            if self.repeat == 'yearly':
                repeat_modality = 2
            
            schedule_dict['date'] = self.run_date

        schedule_dict['repeat_date'] = repeat_modality

        return schedule_dict
    

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
    
    def set_output_config(
            self,
            enable_output: bool,
            output_path: str
        ) -> dict[str, object] | str:
        """
        """
        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'config_set',
            'type': 'esynoscheduler',
            'output_path': output_path,
            'enable_output': enable_output
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_task_settings(self) -> dict[str, object] | str:
        # TODO
        print()

    def task_enable(
            self,
            task_id: int,
            real_owner: str
        ) -> dict[str, object] | str:
        """
        """
        task_dict = {
            'id': task_id,
            'real_owner': real_owner,
            'enable': 'true'
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 2, 
            'method': 'set_enable',
            'status': f'[{json.dumps(task_dict)}]',
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_disable(
            self,
            task_id: int,
            real_owner: str
        ) -> dict[str, object] | str:
        """
        """
        task_dict = {
            'id': task_id,
            'real_owner': real_owner,
            'enable': 'false'
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 2, 
            'method': 'set_enable',
            'status': f'[{json.dumps(task_dict)}]',
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_run(
            self,
            task_id: int,
            real_owner: str
        ) -> dict[str, object] | str:
        """
        """
        task_dict = {
            'id': task_id,
            'real_owner': real_owner
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 2, 
            'method': 'run',
            'tasks': f'[{json.dumps(task_dict)}]',
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_delete(
            self,
            task_id: int,
            real_owner: str
        ) -> dict[str, object] | str:
        """
        """
        task_dict = {
            'id': task_id,
            'real_owner': real_owner
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 2, 
            'method': 'delete',
            'tasks': f'[{json.dumps(task_dict)}]',
        }

        return self.request_data(api_name, api_path, req_param)
    
    def create_script_task(
            self,
            task_name: str,
            owner: str,
            script: str,
            enable: bool = True,
            run_frequently: bool = True,
            run_days: str = '0,1,2,3,4,5,6',
            run_date: str = '',
            repeat: str = 'Daily',
            monthly_week: list[str] = [],
            start_time_h: int = 0,
            start_time_m: int = 0,
            same_day_repeat_h: int = 0,
            same_day_repeat_m: int = 0,
            same_day_repeat_until: int = -1,
            notify_email: str = '',
            notify_only_on_error: bool = False
        ) -> dict[str, object] | str:
        """Create a new script task with the provided schedule and notification settings.

        Args:
            task_name (str): 
                The name of the task.
            owner (str): 
                The task owner.
            script (str): 
                The script to be executed.
            enable (bool, optional): 
                Whether the task should be enabled upon creation. Defaults to `True`.
            run_frequently (bool, optional): 
                Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.
            run_days (str, optional): 
                Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list 
                (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).
            run_date (str, optional): 
                The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). 
                Defaults to an empty string.
            repeat (str, optional): 
                How often the task should repeat. Possible values:
                - "daily" -> Only when 'run_frequently=True'
                - "weekly" -> Only when 'run_frequently=True'
                - "monthly" -> Works for both 'run_frequently=True' and 'run_frequently=False'
                - "no_repeat" -> Only when 'run_frequently=False'
                - "every_3_months" -> Only when 'run_frequently=False'
                - "every_6_months" -> Only when 'run_frequently=False'
                - "yearly" -> Only when 'run_frequently=False'
                Defaults to 'daily'.
            monthly_week (list[str], optional): 
                If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. 
                Defaults to an empty list.
            start_time_h (int, optional): 
                Hour at which the task should start. Defaults to `0`.
            start_time_m (int, optional): 
                Minute at which the task should start. Defaults to `0`.
            same_day_repeat_h (int, optional): 
                Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired. 
                Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat). 

                Possible values: `0..23`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
            same_day_repeat_m (int, optional): 
                Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired. 
                Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat). 
                
                Posible values: `1`, `5`, `10`, `15`, `20`, `30`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
            same_day_repeat_until (int, optional): 
                Last hour of the day when the task can repeat. Defaults to `start_time_h`.
            notify_email (str, optional): 
                Email address to send notifications to. Defaults to an empty string, thus disabling the notification feature.
            notify_only_on_error (bool, optional): 
                If `True`, notifications are only sent when an error occurs. Defaults to `False`.

        Returns:
            dict|str:
                A dictionary with the id of the created task, or a string if there is an error.

        Example return:
            {
            "data": {
                "id": 20
            },
            "success": true
        }
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                            same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)
        
        schedule_dict = schedule._generate_dict()

        extra = {
            'notify_enable': 'true' if notify_email is not '' else 'false',
            'notify_mail': notify_email,
            'notify_if_error': 'true' if notify_only_on_error else 'false',
            'script': script
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4, 
            'method': 'create',
            'name': task_name,
            'real_owner': owner,
            'owner': owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra),
            'type': 'script'
        }

        return self.request_data(api_name, api_path, req_param)

