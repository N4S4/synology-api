from __future__ import annotations
from . import base_api
from .core_sys_info import SysInfo
import json

class EventScheduler(base_api.BaseApi):
    """
       Event Scheduler API implementation.

       This API provides functionality solely related to Event Tasks. For scheduled tasks, check `TaskScheduler`.

       For the moment, the available actions with the API are:
       - Get task results
       - Get result output
       - Enable/Disable task
       - Run task
       - Delete task
       - Create task
       - Set task settings 
    """

    def __get_root_token(self) -> str:
        sys_info = SysInfo(ip_address=self.session._ip_address, port=self.session._port, username=self.session._username, password=self.session._password,
                            secure=self.session._secure, cert_verify=self.session._verify, dsm_version=self.session._version, debug=self.session._debug, 
                            otp_code=self.session._otp_code, application=self.application)
        response = sys_info.password_confirm(password=self.session._password)
        if response['success']: 
            return response['data']['SynoConfirmPWToken']
        else:
            return ''
        
    def get_task_results(
            self,
            task_name: str
        ) -> dict[str, object] | str:
        """Retrieve the results list for a specific task.

        Args:
            task_name (str):
                Name of the Event task to enable/disable.

        Returns:
            dict|str:
                A dictionary containing the task results or a string in case of an error.

            Example return:
                {
                    "data": [
                        {
                            "event_fire_time": "2024-09-13 03:17:47",
                            "exit_info": {
                                "exit_code": 0,
                                "exit_type": "stop"
                            },
                            "extra": {},
                            "pid": 16058,
                            "result_id": 115,
                            "run_time_env": {},
                            "start_time": "2024-09-13 03:17:47",
                            "stop_time": "2024-09-13 03:17:47",
                            "task_name": "asd",
                            "trigger_event": "on_demand"
                        }
                    ],
                    "success": true
                }
        """
        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'result_list',
            'task_name': task_name
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_result_output(
            self,
            task_name: str,
            result_id: int
        ) -> dict[str, object] | str:
        """Retrieve the output for a given result.

        Args:
            task_name (str):
                Name of the Event task to enable/disable.
            result_id (int):
                ID of the result to retrieve. From `get_task_results()`.

        Returns:
            dict|str:
                A dictionary containing the result output or a string in case of an error.

            Example return:
                {
                    "data": {
                        "script_in": "hello",
                        "script_out": "/volume3/datastore/scripts_output/asd/1726190267/script.log: line 1: hello: command not found\n"
                    },
                    "success": true
                }
        """
        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'result_get_file',
            'task_name': task_name,
            'result_id': result_id
        }

        return self.request_data(api_name, api_path, req_param)
        
    def task_set_enable(
            self,
            task_name: str,
            enable: bool
        ) -> dict[str, object] | str:
        """Enable or disable Event task.

        Args:
            task_name (str):
                Name of the Event task to enable/disable.
            enable (bool):
                Wheter to enable (`True`) or disable (`False`) the task.
        
        Returns:
            dict|str:
                A dictionary containing the result of the action or a string in case of an error.

            Example return:
                {
                    "success": true
                }
        
        """
        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'set_enable',
            'enable': enable,
            'task_name': task_name
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_run(
            self,
            task_name: str
        ) -> dict[str, object] | str:
        """Run a specific Event task.

        Args:
            task_name (str): 
                Name of the Event task to run.

        Returns:
            dict|str:
                A dictionary containing the result of the task execution or a string in case of an error.

            Example return:
                {
                    "success": true
                }
        """

        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'run',
            'task_name': task_name
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_delete(
            self,
            task_name: str
        ) -> dict[str, object] | str:
        """Delete a specific Event task.

        Args:
            task_name (str): 
                Name of the Event task to run.

        Returns:
            dict|str:
                A dictionary containing the result of the task deletion or a string in case of an error.

            Example return:
                {
                    "success": true
                }
        """

        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': 'delete',
            'task_name': task_name
        }

        return self.request_data(api_name, api_path, req_param)
    
    def task_create_or_set(
            self,
            action: str, 
            task_name: str,
            owner: dict, 
            trigger_event: str, 
            script: str,
            depend_on_task: list[str] = [],
            enable: bool = True,
            notify_email: str = '',
            notify_only_on_error: bool = False
        ) -> dict[str, object] | str:
        """Create or modify an event-based task.

        Args:
            action (str): 
                Action to perform on the task. Possible values:
                - "create" -> Creates a new task.
                - "set" -> Modify an existing task.
            task_name (str): 
                The name of the task.
            owner (dict): 
                Dictionary containing the owner's ID and name (e.g., `{"1026": "user1"}`). 
                You can get the user UID by running `synouser --get your_user` in your NAS CLI.

                For root privileges, pass `{"0":"root"}`.
            trigger_event (str): 
                The event that triggers the task. Possible values:
                - "shutdown"
                - "bootup"
            script (str): 
                The script to be executed when the task is triggered.
            depend_on_task (list[str], optional): 
                A list of event triggered task names that this task depends on (i.e., tasks that will be run before this one). Defaults to an empty list.
            enable (bool, optional): 
                Whether to enable the task. Defaults to `True`.
            notify_email (str, optional): 
                Email address to send notifications to. Defaults to an empty string. Defaults to an empty string, thus disabling the notification feature.
            notify_only_on_error (bool, optional): 
                If `True`, notifications are only sent when an error occurs. Defaults to `False`.

        Returns:
            dict|str:
                A dictionary containing the result of the task creation or modification, or a strnig in case of an error.

            Example return:
                {
                    "success": true
                }
        """
        if action != 'create' and action != 'set':
            return {'error': f'action <{action}> is not valid.'}
        if trigger_event != 'shutdown' and trigger_event != 'bootup':
            return {'error': f'trigger_event <{trigger_event}> is not valid.'} 
        
        pre_tasks = ''
        for task in depend_on_task: # NAS expects "[Task Name 1][Task Name 2]"
            pre_tasks += f'[{task}]'

        api_name = 'SYNO.Core.EventScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 1, 
            'method': action,
            'task_name': task_name,
            'owner': json.dumps(owner),
            'event': trigger_event,
            'depend_on_task': pre_tasks,
            'enable': enable,
            'notify_enable': notify_email != '',
            'notify_mail': f'"{notify_email}"', # Fails if not formatted with double quotes.
            'notify_if_error':  notify_only_on_error,
            'operation': script,
            'operation_type': 'script'
        }
    
        if owner['0'] == 'root':
            api_name = 'SYNO.Core.EventScheduler.Root'
            req_param['SynoConfirmPWToken'] = self.__get_root_token()

        return self.request_data(api_name, api_path, req_param)