"""Task Scheduler API implementation for Synology DSM."""
from __future__ import annotations
from . import base_api
from .core_user import User
import json


class _Schedule():
    """
    Schedule configuration class for Synology DSM task scheduling.

    This class encapsulates the parameters required to define a schedule for a task,
    such as frequency, days, dates, repeat patterns, and time settings.

    Parameters
    ----------
    run_frequently : bool, optional
        If True, the schedule runs frequently (default is True).
    run_days : str, optional
        Comma-separated string of week days to run the task (default is '0,1,2,3,4,5,6').
    run_date : str, optional
        Specific date to run the task (default is '').
    repeat : str, optional
        Repeat pattern for the schedule, e.g., 'Daily' (default is 'Daily').
    monthly_week : list of str, optional
        List of weeks in the month to run the task (default is empty list).
    start_time_h : int, optional
        Start time hour for the schedule (default is 0).
    start_time_m : int, optional
        Start time minute for the schedule (default is 0).
    same_day_repeat_h : int, optional
        Repeat interval in hours within the same day (default is 0).
    same_day_repeat_m : int, optional
        Repeat interval in minutes within the same day (default is 0).
    same_day_repeat_until : int, optional
        Time (in minutes) until which the same day repeat is active (default is 0).

    See Also
    --------
    TaskScheduler : Main API class for managing scheduled tasks.
    """

    def __init__(
        self,
        run_frequently: bool = True,  # date_type
        run_days: str = '0,1,2,3,4,5,6',  # week_days
        run_date: str = '',  # date
        repeat: str = 'Daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = 0,
    ):
        """
        Initialize a schedule configuration for a Synology DSM task.

        Parameters
        ----------
        run_frequently : bool, optional
            If True, the schedule runs frequently (default is True).
        run_days : str, optional
            Comma-separated string of week days to run the task (default is '0,1,2,3,4,5,6').
        run_date : str, optional
            Specific date to run the task (default is '').
        repeat : str, optional
            Repeat pattern for the schedule, e.g., 'Daily' (default is 'Daily').
        monthly_week : list of str, optional
            List of weeks in the month to run the task (default is empty list).
        start_time_h : int, optional
            Start time hour for the schedule (default is 0).
        start_time_m : int, optional
            Start time minute for the schedule (default is 0).
        same_day_repeat_h : int, optional
            Repeat interval in hours within the same day (default is 0).
        same_day_repeat_m : int, optional
            Repeat interval in minutes within the same day (default is 0).
        same_day_repeat_until : int, optional
            Time (in minutes) until which the same day repeat is active (default is 0).
        """
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
        """
        Generate a dictionary representation of the schedule configuration.

        This method converts the schedule parameters into a dictionary format
        suitable for use with the Synology DSM Task Scheduler API.

        Returns
        -------
        dict
            Dictionary containing the schedule configuration, including date type,
            repeat modality, start time, repeat intervals, and other relevant fields.

        Notes
        -----
        - The `repeat_date` field is set based on the `repeat` and `run_frequently` attributes.
        - The `monthly_week` field is JSON-encoded.
        - The `last_work_hour` defaults to `start_time_h` if `same_day_repeat_until` is not set.
        """
        schedule_dict = {
            'date_type': 0 if self.run_frequently else 1,
            'monthly_week': json.dumps(self.monthly_week),
            # Start time - Hour for the schedule
            'hour': self.start_time_h,
            # Start time - Minute for the schedule
            'minute': self.start_time_m,
            # Continue running on the same day - Repeat each X hours 0..23
            'repeat_hour': self.same_day_repeat_h,
            # Continue running on the same day - Repeat every X minute [1, 5, 10, 15, 20, 30] // 0 = disabled
            'repeat_min': self.same_day_repeat_m,
            # Last run time, defaults to start time if not provided
            'last_work_hour': self.same_day_repeat_until if self.same_day_repeat_until > -1 else self.start_time_h,
        }
        repeat_modality = -1

        if self.run_frequently == 1:
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

        Supported methods:
        - Getters:
            - Get all tasks
            - Get task information
            - Get task results
            - Get output path for task results
        - Setters:
            - Set output path for task results
            - Set task settings
        - Actions:
            - Run task
            - Create task
            - Delete task
            - Enable task
            - Disable task
    """

    def __get_root_token(self) -> str:
        """
        Retrieve a root confirmation token for privileged operations.

        This method authenticates the current user and retrieves a Synology DSM root confirmation token,
        which is required for executing privileged actions (e.g., creating or modifying root-owned tasks).

        Returns
        -------
        str
            The SynoConfirmPWToken if authentication is successful, otherwise an empty string.
        """
        user_api = User(ip_address=self.session._ip_address, port=self.session._port, username=self.session._username, password=self.session._password,
                        secure=self.session._secure, cert_verify=self.session._verify, dsm_version=self.session._version, debug=self.session._debug,
                        otp_code=self.session._otp_code, application=self.application)
        response = user_api.password_confirm(password=self.session._password)
        if response['success']:
            return response['data']['SynoConfirmPWToken']
        else:
            return ''

    def get_output_config(self) -> dict[str, object]:
        """
        Retrieve tasks output configuration.

        Returns
        -------
        dict[str, object]
            A dictionary containing a list of the tasks and information related to them.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_output": true,
                "output_path": "share/scripts_output",
                "type": "esynoscheduler",
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
    ) -> dict[str, object]:
        """
        List all present scheduled tasks and event triggered tasks.

        Parameters
        ----------
        sort_by : str, optional
            The field to sort tasks by. Defaults to `"next_trigger_time"`.

            Possible values:
            - "next_trigger_time"
            - "name"
            - "type"
            - "action"
            - "owner"

        sort_direction : str, optional
            The sort direction. Defaults to `"ASC"`.

            Possible values:
            - "ASC"
            - "DESC"

        offset : int, optional
            Task offset for pagination. Defaults to `0`.

        limit : int, optional
            Number of tasks to retrieve. Defaults to `50`.

        Returns
        -------
        dict[str, object]
            A dictionary containing a list of the tasks and information related to them.

        Examples
        --------
        ```json
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
        ```
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
        real_owner: str,
        type: str = ''
    ) -> dict[str, object]:
        """
        Retrieve the configuration for a specific task or list all available services and their corresponding IDs.

        Parameters
        ----------
        task_id : int
            The ID of the task to retrieve the configuration for. Pass `-1` to get a list of all available services with their IDs.
        real_owner : str
            The real owner of the task, usually `root`. You can double check from the result of `get_task_config()`.
        type : str, optional
            The type of task (e.g., 'service'). Pass `"service"` to get a list of all available services with their IDs. Defaults to `""`.

        Returns
        -------
        dict[str, object]
            A dictionary containing the task configuration.

        Examples
        --------
        ```json
        {
            "data": {
                "action": "Run: echo hello > /tmp/awacate.out",
                "can_edit_name": true,
                "can_edit_owner": true,
                "enable": true,
                "extra": {
                    "notify_enable": false,
                    "notify_if_error": false,
                    "notify_mail": "",
                    "script": "echo hello > /tmp/awacate.out"
                },
                "id": 11,
                "name": "TEST_CRONTAB",
                "owner": "root",
                "real_owner": "root",
                "schedule": {
                    "date": "2024/9/11",
                    "date_type": 0,
                    "hour": 0,
                    "last_work_hour": 0,
                    "minute": 0,
                    "monthly_week": [],
                    "repeat_date": 1001,
                    "repeat_hour": 0,
                    "repeat_hour_store_config": [
                        1..23
                    ],
                    "repeat_min": 0,
                    "repeat_min_store_config": [
                        1,
                        ...
                    ],
                    "version": 4,
                    "week_day": "0,1,2,3,4,5,6"
                },
                "type": "script"
            },
            "success": true
        }
        ```
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

        if type != '':
            req_param['type'] = type

        return self.request_data(api_name, api_path, req_param)

    def get_task_results(
        self,
        task_id: int
    ) -> dict[str, object]:
        """
        Retrieve the results list for a specific task.

        Parameters
        ----------
        task_id : int
            The ID of the task to retrieve the results for.

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
                    "exit_code": 127,
                    "exit_type": "by_signal",
                    "start_time": "2024-09-11 00:00:01",
                    "stop_time": "2024-09-11 00:00:06",
                    "timestamp": "1726005601"
                },
                {
                    "exit_code": 0,
                    "exit_type": "normal",
                    "start_time": "2024-06-01 00:00:01",
                    "stop_time": "2024-06-01 00:00:02",
                    "timestamp": "1717192801"
                }
            ],
            "success": true
        }
        ```
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

    ######
    # For some reason it keeps returning error 4800, in /var/log/synoscgi.log it logs:
    #   2024-09-11T21:27:56+02:00 xxx synowebapi_SYNO.Core.TaskScheduler_1_get_history_log[21830]: main.cpp:392 Invalid paramters.
    #
    # Tried with many combination of params but could not make it work so far.
    ######

    # def get_task_result_logs(
    #         self,
    #         task_id: int,
    #         timestamp: int
    #     ) -> dict[str, object]:
    #     """Retrieve the log information for a specific task result.

    #     Parameters
        # 		---------
    #         task_id : int
    #             The ID of the task to retrieve the log for.
    #         timestamp : int
    #             The timestamp of the result for which to retrieve the logs.

    #     Returns
        # 		---------
    #         dict[str, object]
    #             A dictionary containing the log of the result,.

    #         Example return
        # 		---------
        # 		```json
        # {}
    #      ```
    #     """
    #     api_name = 'SYNO.Core.TaskScheduler'
    #     info = self.gen_list[api_name]
    #     api_path = info['path']
    #     req_param = {
    #         'version': 1,
    #         'method': 'get_history_log',
    #         'timestamp': str(timestamp)
    #         'id': task_id
    #     }

    #     return self.request_data(api_name, api_path, req_param)

    def set_output_config(
        self,
        enable_output: bool,
        output_path: str = ''
    ) -> dict[str, object]:
        """
        Configure the output settings for tasks results.

            Parameters
            ----------
            enable_output : bool
                Whether to enable result logging or not.

            output_path : str, optional
                The path where the result logs will be stored, e.g. `share/scripts_output`. Defaults to `""`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the output configuration.

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
            'method': 'config_set',
            'type': 'esynoscheduler',
            'output_path': output_path,
            'enable_output': enable_output
        }

        return self.request_data(api_name, api_path, req_param)

    def task_set_enable(
        self,
        task_id: int,
        real_owner: str,
        enable: bool
    ) -> dict[str, object]:
        """
        Enable or disable a task.

            Parameters
            ----------
            task_id : int
                The ID of the task to be enabled.

            real_owner : str
                The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.

            enable : bool
                Wheter to enable (`True`) or disable (`False`) the task.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task enabling.

            Examples
            --------
            ```json
            {
                "success": true
            }
            ```
        """
        task_dict = {
            'id': task_id,
            'real_owner': real_owner,
            'enable': enable
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
    ) -> dict[str, object]:
        """
        Run a specific task.

            Parameters
            ----------
            task_id : int
                The ID of the task to be run.

            real_owner : str
                The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.

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
    ) -> dict[str, object]:
        """
        Delete a specific task.

            Parameters
            ----------
            task_id : int
                The ID of the task to be deleted.

            real_owner : str
                The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.

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
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1,
        notify_email: str = '',
        notify_only_on_error: bool = False
    ) -> dict[str, object]:
        """
        Create a new Script task with the provided schedule and notification settings.

            Tip: If the task needs to run with root privileges, please specify the owner as "root".

            Parameters
            ----------
            task_name : str
                The name of the task.

            owner : str
                The task owner. If the task needs to run with root privileges, please specify the owner as "root".

            script : str
                The script to be executed.

            enable : bool, optional
                Whether the task should be enabled upon creation. Defaults to `True`.

            run_frequently : bool, optional
                Determines whether the task runs on a recurring schedule (`True`) or only on a specific date (`False`). Defaults to `True`.

            run_days : str, optional
                Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).

            run_date : str, optional
                The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.

            repeat : str, optional
                How often the task should repeat. Defaults to `daily`.

                Possible values:
                - `daily` -> Only when 'run_frequently=True'
                - `weekly` -> Only when 'run_frequently=True'
                - `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
                - `no_repeat` -> Only when 'run_frequently=False'
                - `every_3_months` -> Only when 'run_frequently=False'
                - `every_6_months` -> Only when 'run_frequently=False'
                - `yearly` -> Only when 'run_frequently=False'

            monthly_week : list[str], optional
                If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`.

                Defaults to `[]`.

            start_time_h : int, optional
                Hour at which the task should start. Defaults to `0`.

            start_time_m : int, optional
                Minute at which the task should start. Defaults to `0`.

            same_day_repeat_h : int, optional
                Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).

                Possible values: `0..23`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_m : int, optional
                Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).

                Posible values: `1`, `5`, `10`, `15`, `20`, `30`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_until : int, optional
                Last hour of the day when the task can repeat. Defaults to `start_time_h`.

            notify_email : str, optional
                Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.

            notify_only_on_error : bool, optional
                If `True`, notifications are only sent when an error occurs. Defaults to `False`.

            Returns
            -------
            dict[str, object]
                A dictionary with the id of the created task.

            Examples
            --------
            ```json
            {
                "data": {
                    "id": 20
                },
                "success": true
            }
            ```
        """
        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'notify_enable': notify_email != '',
            'notify_mail': notify_email,
            'notify_if_error': notify_only_on_error,
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

        if owner == 'root':
            api_name = 'SYNO.Core.TaskScheduler.Root'
            req_param['SynoConfirmPWToken'] = self.__get_root_token()

        return self.request_data(api_name, api_path, req_param)

    def modify_script_task(
        self,
        task_id: int,
        task_name: str,
        owner: str,
        real_owner: str,
        script: str,
        enable: bool = True,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1,
        notify_email: str = '',
        notify_only_on_error: bool = False
    ) -> dict[str, object]:
        """
        Modify settings of a Script task.

            Warning: This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.

            Tip: If the task needs to run with root privileges, please specify the owner as "root".

            Parameters
            ----------
            task_id : int
                The ID of the task.

            task_name : str
                The name of the task.

            owner : str
                The task owner. If the task needs to run with root privileges, please specify the owner as "root".

            real_owner : str
                The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.

            script : str
                The script to be executed.

            enable : bool, optional
                Whether the task should be enabled upon creation. Defaults to `True`.

            run_frequently : bool, optional
                Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.

            run_days : str, optional
                Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).

            run_date : str, optional
                The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.

            repeat : str, optional
                How often the task should repeat. Defaults to `'daily'`.

                Possible values:
                - `daily` -> Only when 'run_frequently=True'
                - `weekly` -> Only when 'run_frequently=True'
                - `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
                - `no_repeat` -> Only when 'run_frequently=False'
                - `every_3_months` -> Only when 'run_frequently=False'
                - `every_6_months` -> Only when 'run_frequently=False'
                - `yearly` -> Only when 'run_frequently=False'

            monthly_week : list[str], optional
                If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.

            start_time_h : int, optional
                Hour at which the task should start. Defaults to `0`.

            start_time_m : int, optional
                Minute at which the task should start. Defaults to `0`.

            same_day_repeat_h : int, optional
                Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.
                Set to `0` to disable same-day repeats. Defaults to `0`.

                Possible values: `0..23`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_m : int, optional
                Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.
                Set to `0` to disable same-day repeats. Defaults to `0`.

                Posible values: `1`, `5`, `10`, `15`, `20`, `30`

                The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_until : int, optional
                Last hour of the day when the task can repeat. Defaults to `start_time_h`.

            notify_email : str, optional
                Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.

            notify_only_on_error : bool, optional
                If `True`, notifications are only sent when an error occurs. Defaults to `False`.

            Returns
            -------
            dict[str, object]
                A dictionary with the id of the created task.

            Examples
            --------
            ```json
            {
                "data": {
                    "id": 20
                },
                "success": true
            }
            ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'notify_enable': notify_email != '',
            'notify_mail': notify_email,
            'notify_if_error': notify_only_on_error,
            'script': script
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'set',
            'id': task_id,
            'name': task_name,
            'real_owner': real_owner,
            'owner': owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra)
        }

        if owner == 'root':
            api_name = 'SYNO.Core.TaskScheduler.Root'
            req_param['SynoConfirmPWToken'] = self.__get_root_token()

        return self.request_data(api_name, api_path, req_param)

    def create_beep_control_task(
        self,
        task_name: str,
        owner: str,
        enable: bool = True,
        beep_duration: int = 60,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Create a new Beep Control task with the provided schedule and beep duration.

        Parameters
        ----------
        task_name : str
            The name of the task.
        owner : str
            The task owner.
        enable : bool, optional
            Whether the task should be enabled upon creation. Defaults to True.
        beep_duration : int, optional
            The amount of seconds the beep will be triggered for. Defaults to 60.
        run_frequently : bool, optional
            Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to True.
        run_days : str, optional
            Days of the week when the task should run, used if `run_frequently` is set to True, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to '0,1,2,3,4,5,6'.
        run_date : str, optional
            The specific date the task should run, used if `run_frequently` is set to False. Format: yyyy/m/d (no prefix zeros). Defaults to "".
        repeat : str, optional
            How often the task should repeat. Defaults to 'daily'.

            Possible values:
                - 'daily' -> Only when run_frequently=True
                - 'weekly' -> Only when run_frequently=True
                - 'monthly' -> Works for both run_frequently=True and run_frequently=False
                - 'no_repeat' -> Only when run_frequently=False
                - 'every_3_months' -> Only when run_frequently=False
                - 'every_6_months' -> Only when run_frequently=False
                - 'yearly' -> Only when run_frequently=False
        monthly_week : list[str], optional
            If run_frequently=True and repeat='monthly', specifies the weeks the task should run, e.g., ['first', 'third']. Defaults to [].
        start_time_h : int, optional
            Hour at which the task should start. Defaults to 0.
        start_time_m : int, optional
            Minute at which the task should start. Defaults to 0.
        same_day_repeat_h : int, optional
            Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.
            Set to 0 to disable same-day repeats. Defaults to 0.

            Possible values: 0..23

            The args same_day_repeat_h and same_day_repeat_m cannot be used at the same time, if both are passed, same_day_repeat_h will be prioritized.
        same_day_repeat_m : int, optional
            Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.
            Set to 0 to disable same-day repeats. Defaults to 0.

            Possible values: 1, 5, 10, 15, 20, 30

            The args same_day_repeat_h and same_day_repeat_m cannot be used at the same time, if both are passed, same_day_repeat_h will be prioritized.
        same_day_repeat_until : int, optional
            Last hour of the day when the task can repeat. Defaults to start_time_h.

        Returns
        -------
        dict[str, object]
            A dictionary with the id of the created task.

        Examples
        --------
        ```json
        {
            "data": {
                "id": 20
            },
            "success": true
        }
        ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'beep_duration': str(beep_duration)
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'create',
            'name': task_name,
            'real_owner': owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra),
            'type': 'beep'
        }

        return self.request_data(api_name, api_path, req_param)

    def modify_beep_control_task(
        self,
        task_id: int,
        task_name: str,
        real_owner: str,
        enable: bool = True,
        beep_duration: int = 60,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Modify settings of a Beep Control task.

        Parameters
        ----------
        task_id : int
            The ID of the task to modify.
        task_name : str
            The name of the task.
        real_owner : str
            The task owner.
        enable : bool, optional
            Whether the task should be enabled upon modification. Defaults to `True`.
        beep_duration : int, optional
            The amount of seconds the beep will be triggered for, in seconds. Defaults to `60`.
        run_frequently : bool, optional
            Determines whether the task runs on a recurring schedule (`True`) or only on a specific date (`False`). Defaults to `True`.
        run_days : str, optional
            Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).
        run_date : str, optional
            The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.
        repeat : str, optional
            How often the task should repeat. Defaults to `'daily'`.

            Possible values:
                - `daily` -> Only when `run_frequently=True`
                - `weekly` -> Only when `run_frequently=True`
                - `monthly` -> Works for both `run_frequently=True` and `run_frequently=False`
                - `no_repeat` -> Only when `run_frequently=False`
                - `every_3_months` -> Only when `run_frequently=False`
                - `every_6_months` -> Only when `run_frequently=False`
                - `yearly` -> Only when `run_frequently=False`
        monthly_week : list[str], optional
            If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.
        start_time_h : int, optional
            Hour at which the task should start. Defaults to `0`.
        start_time_m : int, optional
            Minute at which the task should start. Defaults to `0`.
        same_day_repeat_h : int, optional
            Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.
            Set to `0` to disable same-day repeats. Defaults to `0`.

            Possible values: `0..23`

            Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
        same_day_repeat_m : int, optional
            Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.
            Set to `0` to disable same-day repeats. Defaults to `0`.

            Possible values: `1`, `5`, `10`, `15`, `20`, `30`

            Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
        same_day_repeat_until : int, optional
            Last hour of the day when the task can repeat. Defaults to `start_time_h`.

        Returns
        -------
        dict[str, object]
            A dictionary with the id of the modified task.

        Notes
        -----
        Warning: This method overwrites all the settings of the task, so if you only want to change one setting,
        you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.

        Examples
        --------
        ```json
        {
            "data": {
                "id": 20
            },
            "success": true
        }
        ```
        """
        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'beep_duration': str(beep_duration)
        }

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'set',
            'id': task_id,
            'name': task_name,
            'real_owner': real_owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra)
        }

        return self.request_data(api_name, api_path, req_param)

    def create_service_control_task(
        self,
        task_name: str,
        owner: str,
        services: list[dict],
        action: str,
        enable: bool = True,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Create a new Service Control task with the provided schedule and services to start/stop.

            Parameters
            ----------
            task_name : str
                The name of the task.

            owner : str
                The task owner.

            services : list[dict]
                A list containing the services and their type to be influenced by the specified action (start / stop).

                To get a list of all the available services and their corresponding IDs, call `get_task_config(task_id=-1, real_owner=your_username, type='service')`.

                E.g.:
                ```python
                [
                    {'id': 'AudioStation', 'type': 'package'},
                    {'id': 'HyperBackup', 'type': 'package'},
                    {'id': 'Samba', 'type': 'service'}
                ]
                ```

            action : str
                The action to apply to the services. Either `'start'` or `'stop'`.

            enable : bool, optional
                Whether the task should be enabled upon creation. Defaults to `True`.

            run_frequently : bool, optional
                Determines whether the task runs on a recurring schedule (`True`) or only on a specific date (`False`). Defaults to `True`.

            run_days : str, optional
                Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).

            run_date : str, optional
                The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.

            repeat : str, optional
                How often the task should repeat. Defaults to `'daily'`.

                Possible values:
                - `daily` -> Only when 'run_frequently=True'
                - `weekly` -> Only when 'run_frequently=True'
                - `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
                - `no_repeat` -> Only when 'run_frequently=False'
                - `every_3_months` -> Only when 'run_frequently=False'
                - `every_6_months` -> Only when 'run_frequently=False'
                - `yearly` -> Only when 'run_frequently=False'

            monthly_week : list[str], optional
                If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.

            start_time_h : int, optional
                Hour at which the task should start. Defaults to `0`.

            start_time_m : int, optional
                Minute at which the task should start. Defaults to `0`.

            same_day_repeat_h : int, optional
                Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0`.

                Possible values: `0..23`

                Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_m : int, optional
                Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0`.

                Posible values: `1`, `5`, `10`, `15`, `20`, `30`

                Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_until : int, optional
                Last hour of the day when the task can repeat. Defaults to `start_time_h`.

            Returns
            -------
            dict[str, object]
                A dictionary with the id of the created task.

            Examples
            --------
            ```json
            {
                "data": {
                    "id": 20
                },
                "success": true
            }
            ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'services': [],
            'action': action
        }

        for service in services:
            service_dict = {
                'enable': True,
                'id': service['id'],
                'type': service['type']
            }
            extra['services'].append(service_dict)

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
            'type': 'service'
        }

        return self.request_data(api_name, api_path, req_param)

    def modify_service_control_task(
        self,
        task_id: int,
        task_name: str,
        real_owner: str,
        services: list[dict],
        action: str,
        enable: bool = True,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Modify settings of a Service Control task.

            Warning: This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.

            Parameters
            ----------
            task_id : int
                The ID of the task.

            task_name : str
                The name of the task.

            real_owner : str
                The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.

            services : list[dict]
                A list containing the services and their type to be influenced by the specified action (start / stop).

                To get a list of all the available services and their corresponding IDs, call `get_task_config(task_id=-1, real_owner=your_username, type='service')`.

                E.g.:
                ```python
                [
                    {'id': 'AudioStation', 'type': 'package'},
                    {'id': 'HyperBackup', 'type': 'package'},
                    {'id': 'Samba', 'type': 'service'}
                ]
                ```

            action : str
                The action to apply to the services. Either `'start'` or `'stop'`.

            enable : bool, optional
                Whether the task should be enabled upon creation. Defaults to `True`.

            run_frequently : bool, optional
                Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.

            run_days : str, optional
                Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list
                (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).

            run_date : str, optional
                The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros).
                Defaults to `""`.

            repeat : str, optional
                How often the task should repeat. Defaults to `'daily'`.

                Possible values:
                - `daily` -> Only when 'run_frequently=True'
                - `weekly` -> Only when 'run_frequently=True'
                - `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
                - `no_repeat` -> Only when 'run_frequently=False'
                - `every_3_months` -> Only when 'run_frequently=False'
                - `every_6_months` -> Only when 'run_frequently=False'
                - `yearly` -> Only when 'run_frequently=False'

            monthly_week : list[str], optional
                If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`.
                Defaults to `[]`.

            start_time_h : int, optional
                Hour at which the task should start. Defaults to `0`.

            start_time_m : int, optional
                Minute at which the task should start. Defaults to `0`.

            same_day_repeat_h : int, optional
                Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0`.

                Possible values: `0..23`

                Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_m : int, optional
                Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.

                Set to `0` to disable same-day repeats. Defaults to `0`.

                Posible values: `1`, `5`, `10`, `15`, `20`, `30`

                Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.

            same_day_repeat_until : int, optional
                Last hour of the day when the task can repeat. Defaults to `start_time_h`.

            Returns
            -------
            dict[str, object]
                A dictionary with the id of the created task.

            Examples
            --------
            ```json
            {
                "data": {
                    "id": 20
                },
                "success": true
            }
            ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'services': [],
            'action': action
        }

        for service in services:
            service_dict = {
                'enable': True,
                'id': service['id'],
                'type': service['type']
            }
            extra['services'].append(service_dict)

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'set',
            'id': task_id,
            'name': task_name,
            'real_owner': real_owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra)
        }

        return self.request_data(api_name, api_path, req_param)

    def create_recycle_bin_task(
        self,
        task_name: str,
        owner: str,
        clean_all_shares: bool,
        policy: dict,
        shares: list[str] = [],
        enable: bool = True,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Create a new Recycle Bin Control task with the provided schedule and policy.

        Parameters
        ----------
        task_name : str
            The name of the task.
        owner : str
            The task owner.
        clean_all_shares : bool
            Whether the task should empty the recycle bins of all shares. If set to False, `shares` must be specified.
        policy : dict
            Determines what files will be deleted from the recycle bins.

            Possible values are:
                - \\{"policy": "clean_all"\\}: Clean all files.
                - \\{"policy": "time", "time": int\\}: Clean all files older than X days, where X is the value for "time".
                - \\{"policy": "size", "size": int, "sort_type": int\\}: Clean files until recycle bin size reaches given "size" in MB, delete files by "sort_type".

            Possible values for "sort_type":
                - 0: Delete bigger files first.
                - 1: Delete older files first.
        shares : list[str], optional
            List of shares of which to clean the recycle bins. Pass only the name of the shares without slashes, e.g. `shares=['photo', 'web']`. Defaults to [].
        enable : bool, optional
            Whether the task should be enabled upon creation. Defaults to True.
        run_frequently : bool, optional
            Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to True.
        run_days : str, optional
            Days of the week when the task should run, used if `run_frequently` is True, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to '0,1,2,3,4,5,6'.
        run_date : str, optional
            The specific date the task should run, used if `run_frequently` is False. Format: yyyy/m/d (no prefix zeros). Defaults to "".
        repeat : str, optional
            How often the task should repeat. Defaults to 'daily'.

            Possible values:
                - 'daily' (only when run_frequently=True)
                - 'weekly' (only when run_frequently=True)
                - 'monthly' (works for both run_frequently=True and run_frequently=False)
                - 'no_repeat' (only when run_frequently=False)
                - 'every_3_months' (only when run_frequently=False)
                - 'every_6_months' (only when run_frequently=False)
                - 'yearly' (only when run_frequently=False)
        monthly_week : list[str], optional
            If run_frequently=True and repeat='monthly', specifies the weeks the task should run, e.g., ['first', 'third']. Defaults to [].
        start_time_h : int, optional
            Hour at which the task should start. Defaults to 0.
        start_time_m : int, optional
            Minute at which the task should start. Defaults to 0.
        same_day_repeat_h : int, optional
            Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.
            Set to 0 to disable same-day repeats. Defaults to 0.

            Possible values: 0..23

            Note: The args same_day_repeat_h and same_day_repeat_m cannot be used at the same time; if both are passed, same_day_repeat_h will be prioritized.
        same_day_repeat_m : int, optional
            Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.
            Set to 0 to disable same-day repeats. Defaults to 0.

            Possible values: 1, 5, 10, 15, 20, 30

            Note: The args same_day_repeat_h and same_day_repeat_m cannot be used at the same time; if both are passed, same_day_repeat_h will be prioritized.
        same_day_repeat_until : int, optional
            Last hour of the day when the task can repeat. Defaults to start_time_h.

        Returns
        -------
        dict[str, object]
            A dictionary with the id of the created task.

            Examples
            --------
            ```json
            {
                "data": {
                    "id": 20
                },
                "success": true
            }
            ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'clean_share_policy': {
                'clean_all': clean_all_shares
            },
            'clean_file_policy': policy
        }

        if clean_all_shares == False:
            extra['clean_share_policy']['shares'] = shares

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'create',
            'name': task_name,
            'real_owner': owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra),
            'type': 'recycle'
        }

        return self.request_data(api_name, api_path, req_param)

    def modify_recycle_bin_task(
        self,
        task_id: int,
        task_name: str,
        real_owner: str,
        clean_all_shares: bool,
        policy: dict,
        shares: list[str] = [],
        enable: bool = True,
        run_frequently: bool = True,
        run_days: str = '0,1,2,3,4,5,6',
        run_date: str = '',
        repeat: str = 'daily',
        monthly_week: list[str] = [],
        start_time_h: int = 0,
        start_time_m: int = 0,
        same_day_repeat_h: int = 0,
        same_day_repeat_m: int = 0,
        same_day_repeat_until: int = -1
    ) -> dict[str, object]:
        """
        Modify settings of a Recycle Bin Control task.

        Parameters
        ----------
        task_id : int
            The ID of the task.
        task_name : str
            The name of the task.
        real_owner : str
            The task real owner, usually it is `root`. You can double check from the result of `get_task_config()`.
        clean_all_shares : bool
            Whether the task should empty the recycle bins of all shares. If set to `False`, `shares` must be specified.
        policy : dict
            Determines what files will be deleted from the recycle bins.

            Possible values are:
                - \\{"policy": "clean_all"\\}: Clean all files.
                - \\{"policy": "time", "time": int\\}: Clean all files older than X days, where X is the value for "time".
                - \\{"policy": "size", "size": int, "sort_type": int\\}: Clean files until recycle bin size reaches given "size" in MB, delete files by "sort_type".

            Possible values for "sort_type":
                - 0: Delete bigger files first.
                - 1: Delete older files first.
        shares : list[str], optional
            List of shares of which to clean the recycle bins. Pass only the name of the shares without slashes, e.g. `shares=['photo', 'web']`. Defaults to [].
        enable : bool, optional
            Whether the task should be enabled upon modification. Defaults to `True`.
        run_frequently : bool, optional
            Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.
        run_days : str, optional
            Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'`.
        run_date : str, optional
            The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.
        repeat : str, optional
            How often the task should repeat. Defaults to `'daily'`.

            Possible values:
                - `daily` (only when run_frequently=True)
                - `weekly` (only when run_frequently=True)
                - `monthly` (works for both run_frequently=True and run_frequently=False)
                - `no_repeat` (only when run_frequently=False)
                - `every_3_months` (only when run_frequently=False)
                - `every_6_months` (only when run_frequently=False)
                - `yearly` (only when run_frequently=False)
        monthly_week : list[str], optional
            If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to [].
        start_time_h : int, optional
            Hour at which the task should start. Defaults to `0`.
        start_time_m : int, optional
            Minute at which the task should start. Defaults to `0`.
        same_day_repeat_h : int, optional
            Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.
            Set to `0` to disable same-day repeats. Defaults to `0`.

            Possible values: `0..23`

            Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
        same_day_repeat_m : int, optional
            Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.
            Set to `0` to disable same-day repeats. Defaults to `0`.

            Possible values: `1`, `5`, `10`, `15`, `20`, `30`

            Info: The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.
        same_day_repeat_until : int, optional
            Last hour of the day when the task can repeat. Defaults to `start_time_h`.

        Returns
        -------
        dict[str, object]
            A dictionary with the id of the modified task.

        Notes
        -----
        Warning: This method overwrites all the settings of the task, so if you only want to change one setting,
        you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.

        Examples
        --------
        ```json
        {
            "data": {
                "id": 20
            },
            "success": true
        }
        ```
        """

        schedule = _Schedule(run_frequently, run_days, run_date, repeat, monthly_week, start_time_h, start_time_m,
                             same_day_repeat_h, same_day_repeat_m, same_day_repeat_until)

        schedule_dict = schedule._generate_dict()

        extra = {
            'clean_share_policy': {
                'clean_all': clean_all_shares
            },
            'clean_file_policy': policy
        }

        if clean_all_shares == False:
            extra['clean_share_policy']['shares'] = shares

        api_name = 'SYNO.Core.TaskScheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': 4,
            'method': 'set',
            'id': task_id,
            'name': task_name,
            'real_owner': real_owner,
            'enable': enable,
            'schedule': json.dumps(schedule_dict),
            'extra': json.dumps(extra)
        }

        return self.request_data(api_name, api_path, req_param)
