from __future__ import annotations
import json

from . import base_api

class ActiveBackupMicrosoft(base_api.BaseApi):
    """Active Backup for Microsoft 365 Implementation. 

        Supported methods:
        - Getters: 
            - Get all tasks info
            - Get task settings
            - Get task logs
            - Get package logs
            - Get worker settings

        - Setters:
            - Set worker settings
            - Set task schedule policy
            - Set task retention policy
        
        - Actions:
            - Run backup
            - Cancel backup
            - Delete task
            - Relink task
    """
    def __trim_task_info(self, task_info: dict[str, any]) -> dict[str, any]:
        # Remove unnecessary / readonly fields
        task_info.pop('app_permissions')
        task_info.pop('administrator_account_email')
        task_info.pop('application_id')
        task_info.pop('tenant_id')

        # This can be modified, but only if something is added, 
        # e.g. for adding a user to the task, we would have to send the user_list array only with the new user.
        task_info['user_list'] = []
        task_info['group_list'] = []
        task_info['all_site_list'] = []
        task_info['general_site_list'] = []
        task_info['my_site_list'] = []
        task_info['team_list'] = []

        return task_info
    
    def get_tasks(self) -> dict[str, object]:
        """Retrieve all tasks.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of tasks.

            Example return
            --------------
            ```json
            {
                "data": {
                    event_log: [
                        {
                            "description": "Backup task [test] completed.",
                            "error_code": 0,
                            "last_execution_time": 1733794236,
                            "log_type": 0,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "timestamp": 1733794236
                        },
                    ],
                    service_usage: [
                        {
                            "service_type": 0,
                            "storage_usage": 319196921578
                        },
                        {
                            "service_type": 1,
                            "storage_usage": 1211160588
                        },
                        {
                            "service_type": 4,
                            "storage_usage": 9704366035
                        },
                        {
                            "service_type": 2,
                            "storage_usage": 259976
                        },
                        {
                            "service_type": 3,
                            "storage_usage": 2561252
                        },
                        {
                            "service_type": 5,
                            "storage_usage": 21544726
                        },
                        {
                            "service_type": 8,
                            "storage_usage": 0
                        },
                        {
                            "service_type": 6,
                            "storage_usage": 0
                        },
                        {
                            "service_type": 7,
                            "storage_usage": 0
                        },
                        {
                            "service_type": 9,
                            "storage_usage": 46484
                        }
                    ],
                    tasks: [
                        {
                            "archive_mail_used_storage": 9704366035,
                            "attention_count": 0,
                            "backup_policy": 1,
                            "calendar_used_storage": 2561252,
                            "contact_used_storage": 259976,
                            "drive_used_storage": 319196921578,
                            "duration": 22553,
                            "enable_archive_mail": 1,
                            "enable_calendar": 1,
                            "enable_contact": 1,
                            "enable_drive": 1,
                            "enable_exchange": 1,
                            "enable_group": 0,
                            "enable_group_calendar": 0,
                            "enable_group_mail": 0,
                            "enable_mail": 1,
                            "enable_mysite": 0,
                            "enable_schedule": false,
                            "enable_site": 1,
                            "enable_teams": 1,
                            "error_archive_mail": 0,
                            "error_calendar": 0,
                            "error_contact": 0,
                            "error_drive": 0,
                            "error_group_calendar": 0,
                            "error_group_mail": 0,
                            "error_mail": 0,
                            "error_site": 0,
                            "error_teams": 0,
                            "group_calendar_used_storage": 0,
                            "group_mail_used_storage": 0,
                            "job_id": 0,
                            "last_execution_time": 1733794235,
                            "mail_used_storage": 1211160588,
                            "mysite_used_storage": 0,
                            "processed_archive_mail": 1,
                            "processed_calendar": 1,
                            "processed_contact": 1,
                            "processed_drive": 1,
                            "processed_group_calendar": 0,
                            "processed_group_mail": 0,
                            "processed_mail": 1,
                            "processed_site": 1,
                            "processed_teams": 1,
                            "progress_list": [],
                            "region": 0,
                            "schedule": {
                                "date": "2025/1/26",
                                "date_type": 0,
                                "hour": 0,
                                "last_work_hour": 0,
                                "minute": 0,
                                "monthly_week": [],
                                "repeat_date": 0,
                                "repeat_hour": 0,
                                "repeat_hour_store_config": null,
                                "repeat_min": 0,
                                "repeat_min_store_config": null,
                                "week_day": "0,1,2,3,4,5,6"
                            },
                            "schedule_id": 4,
                            "site_used_storage": 21544726,
                            "status": 1,
                            "status_archive_mail": 1,
                            "status_calendar": 1,
                            "status_contact": 1,
                            "status_drive": 1,
                            "status_group_calendar": 0,
                            "status_group_mail": 0,
                            "status_mail": 1,
                            "status_site": 1,
                            "status_teams": 1,
                            "success_count": 3,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "task_name": "test",
                            "task_status": 2,
                            "task_status_error_code": 0,
                            "teams_used_storage": 46484,
                            "transferred_size_archive_mail": 9704366035,
                            "transferred_size_calendar": 2561252,
                            "transferred_size_contact": 259976,
                            "transferred_size_drive": 319196921578,
                            "transferred_size_group_calendar": 0,
                            "transferred_size_group_mail": 0,
                            "transferred_size_mail": 1211160588,
                            "transferred_size_site": 21544726,
                            "transferred_size_teams": 46484,
                            "upgrade_progress": 0,
                            "warning_archive_mail": 0,
                            "warning_calendar": 0,
                            "warning_contact": 0,
                            "warning_drive": 0,
                            "warning_group_calendar": 0,
                            "warning_group_mail": 0,
                            "warning_mail": 0,
                            "warning_site": 0,
                            "warning_teams": 0
                        }
                    ],
                    users: [
                        {
                            "display_name": "username",
                            "original_name": "username@xxxx.onmicrosoft.com",
                            "service_list": [
                                0,
                                1,
                                4,
                                2,
                                3
                            ],
                            "task_name": "test",
                            "type": 0,
                            "usage_percentage": 99.99345992145251,
                            "usage_total": 330115269429
                        },
                        {
                            "display_name": "sharepoint site",
                            "original_name": "https://xxx.sharepoint.com/sites/sharepointsite",
                            "service_list": [],
                            "task_name": "test",
                            "type": 1,
                            "usage_percentage": 0.006525998326360428,
                            "usage_total": 21544726
                        },
                        {
                            "display_name": "test team",
                            "original_name": "https://teams.microsoft.com/l/team/xxxx",
                            "service_list": [],
                            "task_name": "test",
                            "type": 4,
                            "usage_percentage": 0.000014080221127088742,
                            "usage_total": 46484
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list_tasks'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_package_log(self, offset: int = 0, limit: int = 200) -> dict[str, object]:
        """Retrieve general logs.

            Parameters
            ----------
            offset : int
                The offset of the logs to retrieve. Defaults to `0`.

            limit : int
                The maximum number of logs to retrieve. Defaults to `200`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of logs.

            Example return
            --------------
            ```json
            {
                "data": {
                    "logs": [
                        {
                            "category": 0,
                            "description": "Backup task [test] completed.",
                            "error_code": 0,
                            "log_type": 0,
                            "storage_remove_id": 0,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "timestamp": 1733794236
                        },
                        {
                            "category": 3,
                            "description": "[user] ran backup task [test].",
                            "error_code": 0,
                            "log_type": 0,
                            "storage_remove_id": 0,
                            "task_execution_id": 0,
                            "task_id": 1,
                            "timestamp": 1733771681
                        },
                        {
                            "category": 3,
                            "description": "[user] created task [test].",
                            "error_code": 0,
                            "log_type": 0,
                            "storage_remove_id": 0,
                            "task_execution_id": 0,
                            "task_id": 1,
                            "timestamp": 1733771267
                        }
                    ],
                    "offset": 0
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'get_general_log',
            'offset': offset,
            'limit': limit
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_task_log(self, task_id: int, limit: int = 200, offset: int = 0, key_word: str = '') -> dict[str, object]:
        """Retrieve all logs for a given task.

            Parameters
            ----------
            task_id : int
                The ID of the task.

            limit : int
                The maximum number of logs to retrieve. Defaults to `200`.

            offset : int
                The offset of the logs to retrieve. Defaults to `0`.

            key_word : str, optional
                A keyword to filter logs. Defaults to `''`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of logs.

            Example return
            --------------
            ```json
            {
                "data": {
                    "logs": [
                        {
                            "description": "User [username@xxxx.onmicrosoft.com]'s OneDrive data was backed up (success: 34177; warning: 0; error: 0).",
                            "error_code": 0,
                            "log_type": 0,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "timestamp": 1733780274
                        },
                        {
                            "description": "The data of site [test site] was backed up (List: success: 6, warning: 0, error: 0; Document library: success: 13, warning: 0, error: 0; Document library item: success: 288, warning: 0, error: 0).",
                            "error_code": 0,
                            "log_type": 0,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "timestamp": 1733771918
                        },
                        {
                            "description": "The data of team [test team] was backed up (Channel: success: 3, warning: 0, error: 0; Post: success: 18, warning: 0, error: 0).",
                            "error_code": 0,
                            "log_type": 0,
                            "task_execution_id": 1,
                            "task_id": 1,
                            "timestamp": 1733771786
                        }
                    ],
                    "offset": 0
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'get_all_log',
            'task_id': task_id,
            'limit': limit,
            'offset': offset,
            'key_word': key_word
        }

        return self.request_data(api_name, api_path, req_param)
        
    def get_task_setting(self, task_id: int) -> dict[str, object]:
        """Retrieve the settings of a task.

            Parameters
            ----------
            task_id : int 
                The ID of the task.

            Returns
            -------
            dict[str, object]
                A dictionary containing the settings of the task.

            Example return
            --------------
            ```json
            {
                "data": {
                    "task_info": {
                        "administrator_account_email": "username@xxxx.onmicrosoft.com",
                        "app_permissions": [...],
                        "application_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                        "backup_policy": 1,
                        "enable_auto_add_archive_mail": false,
                        "enable_auto_add_calendar": false,
                        "enable_auto_add_contact": false,
                        "enable_auto_add_drive": false,
                        "enable_auto_add_mail": false,
                        "enable_auto_discover_external_account": true,
                        "enable_auto_discover_general_site": false,
                        "enable_auto_discover_group_alias_archive_mail": false,
                        "enable_auto_discover_group_alias_calendar": false,
                        "enable_auto_discover_group_alias_contact": false,
                        "enable_auto_discover_group_alias_drive": false,
                        "enable_auto_discover_group_alias_mail": false,
                        "enable_auto_discover_group_calendar": false,
                        "enable_auto_discover_group_mail": false,
                        "enable_auto_discover_my_site": false,
                        "enable_auto_discover_teams": false,
                        "enable_auto_discover_unlicensed_account": true,
                        "enable_schedule": false,
                        "enable_user_restore": true,
                        "is_customized_app": true,
                        "is_team_list_ready": true,
                        "local_path": "/datastore/ActiveBackupForMicrosoft365/task_1",
                        "preserve_day_number": 30,
                        "region": 0,
                        "rotation_policy": 0,
                        "schedule": {
                            "date": "2025/1/26",
                            "date_type": 0,
                            "hour": 0,
                            "last_work_hour": 0,
                            "minute": 0,
                            "monthly_week": [],
                            "repeat_date": 0,
                            "repeat_hour": 0,
                            "repeat_hour_store_config": null,
                            "repeat_min": 0,
                            "repeat_min_store_config": null,
                            "week_day": "0,1,2,3,4,5,6"
                        },
                        "schedule_id": 4,
                        "site_domain": "https://xxxx.sharepoint.com",
                        "task_id": 1,
                        "task_name": "test",
                        "task_status": 2,
                        "task_status_error_code": 0,
                        "tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                        "user_list": [
                            {
                                "account_status": 1,
                                "account_type": 2,
                                "email": "username@xxxx.onmicrosoft.com",
                                "enable_archive_mail": false,
                                "enable_calendar": false,
                                "enable_contact": false,
                                "enable_drive": false,
                                "enable_mail": false,
                                "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "local_used_storage": 0,
                                "smtp_mail": "",
                                "user_name": "username"
                            }
                        ],
                        "group_list": [
                            {
                                "description": "test group",
                                "display_name": "test group",
                                "enable_calendar": false,
                                "enable_group_alias_archive_mail": false,
                                "enable_group_alias_calendar": false,
                                "enable_group_alias_contact": false,
                                "enable_group_alias_drive": false,
                                "enable_group_alias_mail": false,
                                "enable_mail": false,
                                "group_status": 1,
                                "group_type": 0,
                                "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "local_used_storage": 0,
                                "mail": "test_group@xxxx.onmicrosoft.com",
                                "mail_nickname": "test group",
                                "owners": [],
                                "title": "test group",
                                "visibility": "Private"
                            },
                        ],
                        "team_list": [
                            {
                                "description": "test team",
                                "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "local_used_storage": 0,
                                "name": "test team",
                                "selected": false,
                                "team_status": 1,
                                "visibility": 0,
                                "web_url": "https://teams.microsoft.com/l/team/xxxx"
                            },
                        ],
                        "my_site_list": [
                            {
                                "description": "",
                                "id": 313,
                                "local_used_storage": 0,
                                "owner_type": 0,
                                "parent_id": "",
                                "primary_admin": "username@xxxx.onmicrosoft.com",
                                "selected": false,
                                "site_collection_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "site_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "site_name": "username",
                                "site_root": "https://xxxx-my.sharepoint.com",
                                "site_status": 1,
                                "site_type": 1,
                                "url": "https://xxxx-my.sharepoint.com/personal/username"
                            },
                        ],
                        "general_site_list": [
                            {
                                "description": "",
                                "id": 1,
                                "local_used_storage": 0,
                                "owner_type": 0,
                                "parent_id": "",
                                "primary_admin": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "selected": false,
                                "site_collection_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "site_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
                                "site_name": "test sharepoint",
                                "site_root": "https://xxxx.sharepoint.com",
                                "site_status": 1,
                                "site_type": 0,
                                "url": "https://xxxx.sharepoint.com"
                            },
                        ],
                    },
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'get_task_setting',
            'task_id': task_id
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_worker_count(self) -> dict[str, object]:
        """Get the number of workers for the Active Backup for Microsoft 365 package.

            Returns
            -------
            dict[str, object]
                A dictionary containing the number of workers.

            Example return
            --------------
            ```json
            {
                "data": {
                    "backup_job_worker_count": 40,
                    "event_worker_count": 40,
                    "max_backup_job_worker_count": 40,
                    "max_event_worker_count": 40
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'get_worker_count'
        }

        return self.request_data(api_name, api_path, req_param)

    def set_worker_count(self, backup_job_workers: int = 40, event_workers: int = 40) -> dict[str, object]:
        """Set the number of workers for the Active Backup for Microsoft 365 package.

            Parameters
            ----------
            backup_job_workers : int 
                Maximum number of concurrent backup accounts. Defaults to `40`.

            event_workers : int 
                Maximum number of concurrent backup files. Defaults to `40`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the worker count update.
            
            Example return
            --------------
            ```json
            {
                "success": true
            }
            ```
        """
        if backup_job_workers < 5 or event_workers < 5:
            raise Exception("The number of workers must be at least 5.")
        
        # Avoid setting the worker count to a value higher than the maximum allowed by the NAS.
        response = self.get_worker_count()
        
        backup_job_workers = min(backup_job_workers, response['data']['max_backup_job_worker_count'])
        event_workers = min(event_workers, response['data']['max_event_worker_count'])

        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'update_worker_count',
            'backup_job_worker_count': backup_job_workers,
            'event_worker_count': event_workers
        }

        return self.request_data(api_name, api_path, req_param)

    def set_task_schedule(self, 
        task_id: int, 
        policy: int, 
        schedule: dict[
            "start_hour": int,
            "start_minute": int,
            "last_run_hour": int,
            "repeat_every_hours": int,
            "run_days": list[int]
        ] = {"place_holder": None}
    ) -> dict[str, object]:
        """Set the schedule for a given task. 

            Parameters
            ----------
            task_id : int
                The ID of the task.  

            policy : int
                The schedule policy. 
                
                Possible values:  
                - 0 = continuous  
                - 1 = manual  
                - 2 = scheduled  

            schedule : dict
                A dictionary containing the schedule settings. 
                
                Possible values:
                - `start_hour` (int): The start hour of the schedule.
                - `start_minute` (int): The start minute of the schedule.
                - `last_run_hour` (int): The last run hour of the schedule.
                - `repeat_every_hours` (int): Run the backup every X hours.
                - `run_days` (list[int]): Run the backup at the specified days (Sunday = 0, Morning = 1, and so on...).  
                
                Note: If `repeat_every_hours` is set to 0, the backup will run once a day.

                Example, to run the backup every day hourly starting at 08:30 until 23:30.
                ```json
                {
                    "start_hour": 8,
                    "start_minute": 30,
                    "last_run_hour": 23,
                    "repeat_every_hours": 1,
                    "run_days": [0, 1, 2, 3, 4, 5, 6]
                }
                ```

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the schedule update.
            
            Example return
            --------------
            ```json 
            {
                "success": true
            }
            ```
        """
        if policy == 2 and "place_holder" in schedule:
            raise Exception("Received schedule policy, but no schedule was provided.")
        
        if policy == 2 and (
            "start_hour" not in schedule
            or "start_minute" not in schedule
            or "last_run_hour" not in schedule
            or "repeat_every_hours" not in schedule
            or "run_days" not in schedule
        ):
            raise Exception("Invalid schedule provided.")
        
        response = self.get_task_setting(task_id)
        task_info = self.__trim_task_info(response['data']['task_info'])
        
        if policy != 2:
            task_info['backup_policy'] = policy
            task_info['enable_schedule'] = False
        else:
            task_info['backup_policy'] = 1 # Manual - needed for scheduled setting
            task_info['enable_schedule'] = True
            task_info['schedule']['date_type'] = 0 # Recurring backup
            task_info['schedule']['monthly_week'] = [] # Not implemented
            task_info['schedule']['repeat_hour_store_config'] = None # Unnecesary
            task_info['schedule']['repeat_minute_store_config'] = None # Unnecesary
            task_info['schedule']['repeat_date'] = 0 # Repeat Daily
            task_info['schedule']['repeat_min'] = 0 # Not implemented
            task_info['schedule']['hour'] = schedule['start_hour']
            task_info['schedule']['minute'] = schedule['start_minute']
            task_info['schedule']['last_work_hour'] = schedule['last_run_hour']
            task_info['schedule']['repeat_hour'] = schedule['repeat_every_hours']
            task_info['schedule']['week_day'] = ",".join(map(str,schedule['run_days']))

        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'set_task_setting',
            'task_id': task_id,
            'task_info': json.dumps(task_info)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_rotation_policy(self, task_id: int, days_to_keep: int) -> dict[str, object]:
        """Set the rotation policy for a given task.

            Parameters
            ----------
            task_id : int
                The ID of the task.  

            days_to_keep : int
                The amount of days to keep previous versions. Defaults to `0` (keep all versions).

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the rotation policy update.
            
            Example return
            --------------
            ```json 
            {
                "success": true
            }
            ```
        """
        response = self.get_task_setting(task_id=task_id)
        task_info = self.__trim_task_info(response['data']['task_info'])
        
        if days_to_keep == 0:
            task_info['rotation_policy'] = 0
        else: 
            task_info['rotation_policy'] = 1
            task_info['preserve_day_number'] = days_to_keep 
        
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'set_task_setting',
            'task_id': task_id,
            'task_info': json.dumps(task_info)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def run_backup(self, task_id: int) -> dict[str, object]:
        """Manually run backup for a given task id.

            Parameters
            ----------
            task_id : int
                The ID of the task.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the backup task.
            
            Example return
            --------------
            ```json
            {
                "success": true
            }
            ```
        """

        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'backup_task',
            'task_id': task_id
        }

        return self.request_data(api_name, api_path, req_param)
    
    def cancel_backup(self, task_id: int) -> dict[str, object]:
        """Cancel a running backup task.

            Parameters
            ----------
            task_id : int
                The ID of the task.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task cancellation.
            
            Example return
            --------------
            ```json 
            {
                "success": true
            }
            ```
        """
        response = self.get_tasks()
        tasks = response['data']['tasks']
        matching_task = next((task for task in tasks if task.get("task_id") == task_id), None)
        
        if matching_task is None:
            raise Exception(f"Task with ID {task_id} not found.")
        
        # Return if task is not running
        if matching_task['status'] != 4:
            return 
        
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'cancel_task',
            'task_id': task_id,
            'job_id': matching_task['job_id'],
            'job_type': 0
        }

        return self.request_data(api_name, api_path, req_param)
    
    def delete_task(self, task_id: int, remove_data: bool = False) -> dict[str, object]:
        """Delete a task.

            Warning: Miss-use of this action may lead to data loss.

            Parameters
            ----------
            task_id : int
                The ID of the task.

            remove_data : bool
                Whether to remove the backup data in the NAS. Defaults to `False`.
                
                Warning: If this is set to `True`, all task data in the NAS will be lost and the task cannot be relinked in the future. 

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task deletion.
            
            Example return
            --------------
            ```json 
            {
                "success": true
            }
            ```
        """

        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'delete_task',
            'task_id': task_id,
            'should_remove_storage': remove_data
        }

        return self.request_data(api_name, api_path, req_param)
    
    def relink_task(self, 
        task_name: str, 
        local_shared: str, 
        local_path: str, 
        admin_email: str,
        region: str = "Microsoft 365"
    ) -> dict[str, object]:
        """Relink a task.

            Parameters
            ----------
            task_name : str
                The name of the task.

            shared_folder : str
                The name of the shared folder where the task is stored. 
                
                Example: `ActiveBackupforBusiness`

            task_path : str
                The relative path from the the shared folder where the task is stored. 
                
                Example: `/ActiveBackupForMicrosoft365/task_1`

            admin_email : str
                The email of the Microsoft 365 administrator.
                
            region : str
                The region of the Microsoft 365 account. Defaults to `Microsoft 365`

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the task relinking.
            
            Example return
            --------------
            ```json 
            {
                "data": {
                    "task_id": 3
                },
                "success": true
            }
            ```
        """
        task_info = {
            "selected": True,
            "task_name": task_name,
            "local_shared": local_shared,
            "local_path": local_path,
            "region": region,
            "admin_email": admin_email
        }

        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'relink_task',
            'task_info': json.dumps(task_info)
        }

        return self.request_data(api_name, api_path, req_param)