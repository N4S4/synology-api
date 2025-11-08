---
sidebar_position: 3
title: ✅ ActiveBackupMicrosoft
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# ActiveBackupMicrosoft
## Overview
Active Backup for Microsoft 365 Implementation.

    ### Supported methods

    - **Getters** :
        - Get all tasks info
        - Get task settings
        - Get task logs
        - Get package logs
        - Get worker settings

    - **Setters** :
        - Set worker settings
        - Set task schedule policy
        - Set task retention policy

    - **Actions** :
        - Run backup
        - Cancel backup
        - Delete task
        - Relink task
## Methods
### `get_tasks`
Retrieve all tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of tasks.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_package_log`
Retrieve general logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The offset of the logs to retrieve. Defaults to `0`.  
  
**_limit_** `int`  
The maximum number of logs to retrieve. Defaults to `200`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of logs.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_task_log`
Retrieve all logs for a given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_limit_** `int`  
The maximum number of logs to retrieve. Defaults to `200`.  
  
**_offset_** `int`  
The offset of the logs to retrieve. Defaults to `0`.  
  
**_key_word_** `str`  
A keyword to filter logs. Defaults to `''`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of logs.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_task_setting`
Retrieve the settings of a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the settings of the task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_worker_count`
Get the number of workers for the Active Backup for Microsoft 365 package.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the number of workers.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `set_worker_count`
Set the number of workers for the Active Backup for Microsoft 365 package.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_backup_job_workers_** `int`  
Maximum number of concurrent backup accounts. Defaults to `40`.  
  
**_event_workers_** `int`  
Maximum number of concurrent backup files. Defaults to `40`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the worker count update.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `set_task_schedule`
Set the schedule for a given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_policy_** `int`  
The schedule policy.  
Possible values:
- 0 = continuous
- 1 = manual
- 2 = scheduled.  
  
**_schedule_** `dict`  
A dictionary containing the schedule settings.  
Possible values:
- `start_hour` (int): The start hour of the schedule.
- `start_minute` (int): The start minute of the schedule.
- `last_run_hour` (int): The last run hour of the schedule.
- `repeat_every_hours` (int): Run the backup every X hours.
- `run_days` (list[int]): Run the backup at the specified days (Sunday = 0, Morning = 1, and so on...).  
:::note
 
 If `repeat_every_hours` is set to 0, the backup will run once a day.  
 
:::

Examples, to run the backup every day hourly starting at 08:30 until 23:30.
```json
{
    "start_hour": 8,
    "start_minute": 30,
    "last_run_hour": 23,
    "repeat_every_hours": 1,
    "run_days": [0, 1, 2, 3, 4, 5, 6]
}
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the schedule update.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `set_rotation_policy`
Set the rotation policy for a given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_days_to_keep_** `int`  
The amount of days to keep previous versions. Defaults to `0` (keep all versions).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the rotation policy update.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `run_backup`
Manually run backup for a given task id.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the backup task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `cancel_backup`
Cancel a running backup task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task cancellation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `delete_task`
Delete a task.  
:::warning
 
 Miss-use of this action may lead to data loss.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_remove_data_** `bool`  
Whether to remove the backup data in the NAS. Defaults to `False`.  
:::warning
 
 If this is set to `True`, all task data in the NAS will be lost and the task cannot be relinked in the future.  
 
:::

  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task deletion.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "success": true
    }
    ```
</details>



---


### `relink_task`
Relink a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveBackupOffice365` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
The name of the task.  
  
**_local_shared_** `str`  
The name of the shared folder where the task is stored.  
Examples: `ActiveBackupforBusiness`.  
  
**_local_path_** `str`  
The relative path from the shared folder where the task is stored.  
Examples: `/ActiveBackupForMicrosoft365/task_1`.  
  
**_admin_email_** `str`  
The email of the Microsoft 365 administrator.  
  
**_region_** `str`  
The region of the Microsoft 365 account. Defaults to `Microsoft 365`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task relinking.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "data": {
            "task_id": 3
        },
        "success": true
    }
    ```
</details>



---


