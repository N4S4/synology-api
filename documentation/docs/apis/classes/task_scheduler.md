---
sidebar_position: 30
title: ✅ TaskScheduler
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# TaskScheduler
## Overview
Task Scheduler API implementation.

This API provides the functionality to get information related to the scheduler settings and current tasks.

### Supported methods

- **Getters** : 
    - Get all tasks
    - Get task information
    - Get task results
    - Get output path for task results
- **Setters** :
    - Set output path for task results
    - Set task settings 
- **Actions** :
    - Run task
    - Create task
    - Delete task
    - Enable task
    - Disable task
## Methods
### `get_output_config`
Retrieve tasks output configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing a list of the tasks and information related to them.  

</div>



---


### `get_task_list`
List all present scheduled tasks and event triggered tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sort_by_** `str, optional `  
The field to sort tasks by. Defaults to `"next_trigger_time"`.  
Possible values:
- "next_trigger_time"
- "name"
- "type"
- "action"
- "owner"  
  
**_sort_direction_** `str, optional `  
The sort direction. Defaults to `"ASC"`.  
Possible values:
- "ASC"
- "DESC"  
  
**_offset_** `int, optional `  
Task offset for pagination. Defaults to `0`.  
  
**_limit_** `int, optional `  
Number of tasks to retrieve. Defaults to `50`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing a list of the tasks and information related to them.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_task_config`
Retrieve the configuration for a specific task or list of all the available services and their corresponding IDs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int `  
The ID of the task to retrieve the configuration for. Pass `-1` to get a list of all available services with their IDs.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  
**_type_** `str, optional `  
The type of task (e.g., 'service'). Pass "service" to get a list of all available services with their IDs. Defaults to `""`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the task configuration.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_task_results`
Retrieve the results list for a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int `  
The ID of the task to retrieve the results for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the task results.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `set_output_config`
Configure the output settings for tasks results.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_output_** `bool `  
Whether to enable result logging or not.  
  
**_output_path_** `str, optional `  
The path where the result logs will be stored, e.g. `share/scripts_output'`. Defaults to `""`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the output configuration.  

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


### `task_set_enable`
Enable or disable a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int `  
The ID of the task to be enabled.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  
**_enable_** `bool`  
Wheter to enable (`True`) or disable (`False`) the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task enabling.  

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


### `task_run`
Run a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int `  
The ID of the task to be run.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task execution.  

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


### `task_delete`
Delete a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int `  
The ID of the task to be deleted.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  

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


### `create_script_task`
Create a new Script task with the provided schedule and notification settings.   
:::tip
 
 If the task needs to run with root privileges, please specify the owner as "root".  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str `  
The name of the task.  
  
**_owner_** `str `  
The task owner. If the task needs to run with root privileges, please specify the owner as "root".  
  
**_script_** `str `  
The script to be executed.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (`True`) or only on a specific date (`False`). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `daily`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`.   
Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Possible values: `0..23`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  
**_notify_email_** `str, optional `  
Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.  
  
**_notify_only_on_error_** `bool, optional `  
If `True`, notifications are only sent when an error occurs. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `modify_script_task`
Modify settings of a Script task.   
:::warning
 
 This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.
 
:::

 
:::tip
 
 If the task needs to run with root privileges, please specify the owner as "root".  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_task_name_** `str `  
The name of the task.  
  
**_owner_** `str `  
The task owner. If the task needs to run with root privileges, please specify the owner as "root".  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  
**_script_** `str `  
The script to be executed.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired. 
Set to `0` to disable same-day repeats. Defaults to `0`.  
Possible values: `0..23`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired. 
Set to `0` to disable same-day repeats. Defaults to `0`.  
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  
**_notify_email_** `str, optional `  
Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.  
  
**_notify_only_on_error_** `bool, optional `  
If `True`, notifications are only sent when an error occurs. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `create_beep_control_task`
Create a new Beep Control task with the provided schedule and beep duration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str `  
The name of the task.  
  
**_owner_** `str `  
The task owner.  
  
**_beep_duration_** `int, optional `  
The amount of seconds the beep will be triggered for, in seconds. Defaults to `60`.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. 
Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired. 
Set to `0` to disable same-day repeats. Defaults to `0`.  
Possible values: `0..23`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired. 
Set to `0` to disable same-day repeats. Defaults to `0`.   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `modify_beep_control_task`
Modify settings of a Beep Control task.   
:::warning
 
 This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str `  
The name of the task.  
  
**_real_owner_** `str `  
The task owner.  
  
**_beep_duration_** `int, optional `  
The amount of seconds the beep will be triggered for, in seconds. Defaults to `60`.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.  
Possible values: `0..23`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.  
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `create_service_control_task`
Create a new Service Control task with the provided schedule and services to start/stop.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str `  
The name of the task.  
  
**_owner_** `str `  
The task owner.  
  
**_services (list)_** ``  
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
  
**_action_** `str `  
The action to apply to the services. Either `'start'` or `'stop'`.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (`True`) or only on a specific date (`False`). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.   
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.   
Possible values: `0..23`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `modify_service_control_task`
Modify settings of a Service Control task.   
:::warning
 
 This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_task_name_** `str `  
The name of the task.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  
**_services (list)_** ``  
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
  
**_action_** `str `  
The action to apply to the services. Either `'start'` or `'stop'`.  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list 
(e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). 
Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.   
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`. 
Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.   
Possible values: `0..23`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0`.   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `create_recycle_bin_task`
Create a new Recycle Bin Control task with the provided schedule and services to start/stop.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str `  
The name of the task.  
  
**_owner_** `str `  
The task owner.  
  
**_clean_all_shares_** `bool `  
Whether the task should empty the recycle bins of all shares or not, if set to `False`, shares must be specified.  
  
**_shares_** `list[str]`  
List of shares of which to clean the recycle bins. Pass only the name of the shares without slashes, e.g. `shares=['photo', 'web']`. Defaults to `[]`.  
  
**_policy (dict)_** ``  
Determines what files will be deleted from the recycle bins.   
Possible values are:
- `{"policy": "clean_all"}` -> Clean all files
- `{"policy": "time", "time": int}` -> Clean all files older than X days, days being possed as value for "time" key.
- `{"policy": "size", "size": int , "sort_type": int}` -> Clean files until recycle bin size reaches given "size" in MB, delete files by "sort_type".  
Possible values for "sort_type" are:
- `0` -> Delete bigger files first
- `1` -> Delete older files first  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). 
Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`.   
Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Possible values: `0..23`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


### `modify_recycle_bin_task`
Modify settings of a Recycle Bin Control task.   
:::warning
 
 This method overwrites all the settings of the task, so if you only want to change one setting, you can fetch the current task configuration with `get_task_config()` and pass all the settings to this method.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.TaskScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
The ID of the task.  
  
**_task_name_** `str `  
The name of the task.  
  
**_real_owner_** `str `  
The task real owner, usually it is `root`, you can double check from the result of `get_task_config()`.  
  
**_clean_all_shares_** `bool `  
Whether the task should empty the recycle bins of all shares or not, if set to `False`, shares must be specified.  
  
**_shares_** `list[str]`  
List of shares of which to clean the recycle bins. Pass only the name of the shares without slashes, e.g. `shares=['photo', 'web']`. Defaults to `[]`.  
  
**_policy (dict)_** ``  
Determines what files will be deleted from the recycle bins.   
Possible values are:
- `{"policy": "clean_all"}` -> Clean all files
- `{"policy": "time", "time": int}` -> Clean all files older than X days, days being possed as value for "time" key.
- `{"policy": "size", "size": int , "sort_type": int}` -> Clean files until recycle bin size reaches given "size" in MB, delete files by "sort_type".  
Possible values for "sort_type" are:
- `0` -> Delete bigger files first
- `1` -> Delete older files first  
  
**_enable_** `bool, optional `  
Whether the task should be enabled upon creation. Defaults to `True`.  
  
**_run_frequently_** `bool, optional `  
Determines whether the task runs on a recurring schedule (True) or only on a specific date (False). Defaults to `True`.  
  
**_run_days_** `str, optional `  
Days of the week when the task should run, used if `run_frequently` is set to `True`, specified as a comma-separated list (e.g., '0,1,2' for Sunday, Monday, Tuesday). Defaults to `'0,1,2,3,4,5,6'` (Daily).  
  
**_run_date_** `str, optional `  
The specific date the task should run, used if `run_frequently` is set to `False`. Format: `yyyy/m/d` (no prefix zeros). 
Defaults to `""`.  
  
**_repeat_** `str, optional `  
How often the task should repeat. Defaults to `'daily'`.  
Possible values:
- `daily` -> Only when 'run_frequently=True'
- `weekly` -> Only when 'run_frequently=True'
- `monthly` -> Works for both 'run_frequently=True' and 'run_frequently=False'
- `no_repeat` -> Only when 'run_frequently=False'
- `every_3_months` -> Only when 'run_frequently=False'
- `every_6_months` -> Only when 'run_frequently=False'
- `yearly` -> Only when 'run_frequently=False'  
  
**_monthly_week_** `list[str], optional `  
If `run_frequently=True` and `repeat='monthly'`, specifies the weeks the task should run, e.g., `['first', 'third']`.   
Defaults to `[]`.  
  
**_start_time_h_** `int, optional `  
Hour at which the task should start. Defaults to `0`.  
  
**_start_time_m_** `int, optional `  
Minute at which the task should start. Defaults to `0`.  
  
**_same_day_repeat_h_** `int, optional `  
Number of hours between repeated executions on the same day (run every x hours), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Possible values: `0..23`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_m_** `int, optional `  
Number of minutes between repeated executions on the same day (run every x minutes), if "Continue running within the same day" is desired.   
Set to `0` to disable same-day repeats. Defaults to `0` (disable same day repeat).   
Posible values: `1`, `5`, `10`, `15`, `20`, `30`  
:::info
 
 The args `same_day_repeat_h` and `same_day_repeat_m` cannot be used at the same time, if both are passed, `same_day_repeat_h` will be prioritized.  
 
:::

  
**_same_day_repeat_until_** `int, optional `  
Last hour of the day when the task can repeat. Defaults to `start_time_h`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary with the id of the created task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "id": 20
    },
    "success": true
}
```
</details>



---


