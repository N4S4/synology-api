"""
Event Scheduler API module.

This module provides the EventScheduler class for managing event-based tasks and power schedules
on Synology NAS devices via the SYNO.Core.EventScheduler API.
"""
from __future__ import annotations
from . import base_api
from .core_sys_info import SysInfo
import json
from typing import List


class EventScheduler(base_api.BaseApi):
    """
    Event Scheduler API implementation.

    This API provides functionality solely related to Event Tasks. For scheduled tasks, check `TaskScheduler`.

    Methods
    -------
    Getters:
        - Get task results
        - Get result output
    Setters:
        - Set task settings
        - Set power schedule
    Actions:
        - Enable task
        - Disable task
        - Run task
        - Delete task
        - Create task
    """

    def __get_root_token(self) -> str:
        """
        Get the SynoConfirmPWToken for root operations.

        Returns
        -------
        str
            The SynoConfirmPWToken if successful, otherwise an empty string.
        """
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
        """
        Retrieve the results list for a specific task.

        Parameters
        ----------
        task_name : str
            Name of the Event task to enable/disable.

        Returns
        -------
        dict[str, object]
            A dictionary containing the task results.

        Examples
        --------
        ```json
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
        ```
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
        """
        Retrieve the output for a given result.

        Parameters
        ----------
        task_name : str
            Name of the Event task to enable/disable.
        result_id : int
            ID of the result to retrieve. From get_task_results().

        Returns
        -------
        dict[str, object]
            A dictionary containing the result output.

        Examples
        --------
        ```json
        {
            "data": {
                "script_in": "hello",
                "script_out": "/volume3/datastore/scripts_output/asd/1726190267/script.log: line 1: hello: command not found\\n"
            },
            "success": true
        }
        ```
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
        """
        Enable or disable Event task.

        Parameters
        ----------
        task_name : str
            Name of the Event task to enable/disable.
        enable : bool
            Whether to enable (`True`) or disable (`False`) the task.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the action.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
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
        """
        Run a specific Event task.

        Parameters
        ----------
        task_name : str
            Name of the Event task to run.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the task execution.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
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
        """
        Delete a specific Event task.

        Parameters
        ----------
        task_name : str
            Name of the Event task to run.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the task deletion.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
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
        """
        Create or modify an event-based task.

        Parameters
        ----------
        action : str
            Action to perform on the task.

            Possible values:
            - `create` -> Create a new task.
            - `set` -> Modify an existing task.
        task_name : str
            The name of the task.
        owner : dict[str, str]
            Dictionary containing the owner's ID and name (e.g., `{"1026": "user1"}`).
            You can get the user UID by running `synouser --get your_user` in your NAS CLI.
            For root privileges, pass `{"0":"root"}`.
        trigger_event : str
            The event that triggers the task.
            Possible values:
            - `shutdown`
            - `bootup`
        script : str
            The script to be executed when the task is triggered.
        depend_on_task : list[str], optional
            A list of event triggered task names that this task depends on (i.e., tasks that will be run before this one). Defaults to `[]`.
        enable : bool, optional
            Whether to enable the task. Defaults to `True`.
        notify_email : str, optional
            Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.
        notify_only_on_error : bool, optional
            If `True`, notifications are only sent when an error occurs. Defaults to `False`.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the task creation or modification, or a string in case of an error.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        if action != 'create' and action != 'set':
            return {'error': f'action <{action}> is not valid.'}
        if trigger_event != 'shutdown' and trigger_event != 'bootup':
            return {'error': f'trigger_event <{trigger_event}> is not valid.'}

        pre_tasks = ''
        for task in depend_on_task:  # NAS expects "[Task Name 1][Task Name 2]"
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
            # Fails if not formatted with double quotes.
            'notify_mail': f'"{notify_email}"',
            'notify_if_error':  notify_only_on_error,
            'operation': script,
            'operation_type': 'script'
        }

        if owner['0'] == 'root':
            api_name = 'SYNO.Core.EventScheduler.Root'
            req_param['SynoConfirmPWToken'] = self.__get_root_token()

        return self.request_data(api_name, api_path, req_param)

    def set_power_schedule(self, poweron_tasks: List[dict] = [], poweroff_tasks: List[dict] = []) -> dict:
        """
        Set the power schedule, poweron tasks and poweroff tasks.

        Parameters
        ----------
        poweron_tasks : List[dict], optional
            List of tasks for power on. Defaults to `[]`.
            Example of a task:
            ```python
            {
                "enabled": True, # Enable or not the task
                "hour": 13, # Hour 0-23
                "min": 59, # Minutes 0-59
                "weekdays": "0,1,2,3,4,5,6" # All days of the week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
            }
            ```
        poweroff_tasks : List[dict], optional
            List of tasks for power off. Defaults to `[]`.
            Example of a task:
            ```python
            {
                "enabled": True, # Enable or not the task
                "hour": 13, # Hour 0-23
                "min": 59, # Minutes 0-59
                "weekdays": "0,1,2,3,4,5,6" # All days of the week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
            }
            ```

        Returns
        -------
        dict
            List of tasks in power schedule.

        Examples
        --------
        ```json
        {
            "data": {
                "poweroff_tasks": [],
                "poweron_tasks": [
                    {
                        "enabled": true,
                        "hour": 0,
                        "min": 0,
                        "weekdays": "1,2,3,4,5"
                    }
                ]
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Hardware.PowerSchedule'
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "save",
            "poweron_tasks": json.dumps(poweron_tasks),
            "poweroff_tasks": json.dumps(poweroff_tasks)
        }

        return self.request_data(api_name, api_path, req_param)

    def load_power_schedule(self) -> dict:
        """
        Load the power schedule, poweron tasks and poweroff tasks.

        Returns
        -------
        dict
            List of tasks in power schedule.

        Examples
        --------
        ```json
        {
            "data": {
                "poweroff_tasks": [],
                "poweron_tasks": [
                    {
                        "enabled": true,
                        "hour": 0,
                        "min": 0,
                        "weekdays": "1,2,3,4,5"
                    }
                ]
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Hardware.PowerSchedule'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'load'
        }

        return self.request_data(api_name, api_path, req_param)
