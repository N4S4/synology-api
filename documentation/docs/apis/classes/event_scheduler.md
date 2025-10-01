---
sidebar_position: 14
title: ✅ EventScheduler
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# EventScheduler
## Overview
Event Scheduler API implementation.

This API provides functionality solely related to Event Tasks. For scheduled tasks, check `TaskScheduler`.

Methods
-------
**Getters** :
    - Get task results
    - Get result output
**Setters** :
    - Set task settings
    - Set power schedule
**Actions** :
    - Enable task
    - Disable task
    - Run task
    - Delete task
    - Create task
## Methods
### `get_task_results`
Retrieve the results list for a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
Name of the Event task to enable/disable.  
  

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
</details>



---


### `get_result_output`
Retrieve the output for a given result.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
Name of the Event task to enable/disable.  
  
**_result_id_** `int`  
ID of the result to retrieve. From get_task_results().  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result output.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "script_in": "hello",
        "script_out": "/volume3/datastore/scripts_output/asd/1726190267/script.log: line 1: hello: command not found\n"
    },
    "success": true
}
```
</details>



---


### `task_set_enable`
Enable or disable Event task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
Name of the Event task to enable/disable.  
  
**_enable_** `bool`  
Whether to enable (`True`) or disable (`False`) the task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the action.  

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
Run a specific Event task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
Name of the Event task to run.  
  

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
Delete a specific Event task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_name_** `str`  
Name of the Event task to run.  
  

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


### `task_create_or_set`
Create or modify an event-based task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.EventScheduler` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_action_** `str`  
Action to perform on the task.  
Possible values:
- `create` -> Create a new task.
- `set` -> Modify an existing task.  
  
**_task_name_** `str`  
The name of the task.  
  
**_owner_** `dict[str, str]`  
Dictionary containing the owner's ID and name (e.g., `{"1026": "user1"}`).
You can get the user UID by running `synouser --get your_user` in your NAS CLI.
For root privileges, pass `{"0":"root"}`.  
  
**_trigger_event_** `str`  
The event that triggers the task.
Possible values:
- `shutdown`
- `bootup`  
  
**_script_** `str`  
The script to be executed when the task is triggered.  
  
**_depend_on_task_** `list[str]`  
A list of event triggered task names that this task depends on (i.e., tasks that will be run before this one). Defaults to `[]`.  
  
**_enable_** `bool`  
Whether to enable the task. Defaults to `True`.  
  
**_notify_email_** `str`  
Email address to send notifications to. Defaults to `""`, thus disabling the notification feature.  
  
**_notify_only_on_error_** `bool`  
If `True`, notifications are only sent when an error occurs. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task creation or modification, or a string in case of an error.  

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


### `set_power_schedule`
Set the power schedule, poweron tasks and poweroff tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.PowerSchedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_poweron_tasks_** `List[dict]`  
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
  
**_poweroff_tasks_** `List[dict]`  
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
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of tasks in power schedule.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `load_power_schedule`
Load the power schedule, poweron tasks and poweroff tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.PowerSchedule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of tasks in power schedule.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


