---
sidebar_position: 7
title: 🚧 Backup
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Backup
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Synology Hyper Backup API.
## Methods
### `backup_repository_get`
Get repository information for a given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Repository` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Repository information.  

</div>



---


### `backup_repository_list`
Get a list of all present repositories in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Repository` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of repositories.  

</div>



---


### `backup_task_list`
Get current restoring information and a list of present tasks in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of tasks and restoring information.  

</div>



---


### `backup_task_status`
Get status and state of a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status and state information.  

</div>



---


### `backup_task_get`
Get detailed task information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task information.  

</div>



---


### `backup_task_result`
Get last result summary information of a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Last result summary.  

</div>



---


### `backup_task_run`
Run backup task for corresponding task_id.  
If the task is not in backupable state, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `backup_task_cancel`
Cancel currently running backup task.  
If the task is not running, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `backup_task_suspend`
Suspend currently running backup task.  
If the task is not running or not yet suspendable, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `backup_task_discard`
Discard currently suspended backup task.  
If the task is not suspended, the request will not fail, and will fail to discard the task, leaving the task state as "Failed".  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `backup_task_resume`
Resume currently suspended backup task.  
If the task is not suspended, the request will not fail, and will fail to resume the task, leaving the task state as "Failed".  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `backup_task_remove`
Remove one or more backup tasks.  
Data in destination will not be removed. It is still possible to relink the task using the original .hbk file.
The API requires an array of tasks to remove, it should be passed as a string with the following format:
`task_id_list = '[29]'` or `task_id_list = '[29,15]'`  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_list_** `str`  
List of task IDs as a string.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `integrity_check_run`
Run integrity check for backup task.  
If the task is running, the request will not fail, and will fail to perform the integrity check due to target being busy.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Target` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `integrity_check_cancel`
Cancel currently running integrity check for backup task.  
If integrity check is not running, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Target` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `hb_logs_get`
Get Hyper Backup UI logs.  
`filter_date_from` and `filter_date_to` need to be passed in epoch format.  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Client.Common.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_limit_** `int`  
Maximum number of logs to return (default is 1000).  
  
**_offset_** `int`  
Offset for pagination (default is 0).  
  
**_filter_keyword_** `str`  
Keyword to filter logs (default is '').  
  
**_filter_date_from_** `int`  
Start date in epoch format (default is 0).  
  
**_filter_date_to_** `int`  
End date in epoch format (default is 0).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Logs information.  

</div>



---


### `vault_target_list`
List all available targets in Vault.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Target` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
List of available targets.  

</div>



---


### `vault_concurrency_get`
Get number of concurrent tasks allowed to run in HB Vault.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Config` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Number of concurrent tasks (default is 2).  

</div>



---


### `vault_concurrency_set`
Set number of concurrent tasks allowed to run in HB Vault.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Config` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_parallel_backup_limit_** `int`  
Number of concurrent tasks (default is 2).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response.  

</div>



---


### `vault_target_settings_get`
Get settings of a target.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Target` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_target_id_** `int`  
Target ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Target settings.  

</div>



---


### `vault_task_statistics_get`
Get statistics for a given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Server.Common.Statistic` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
Task ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Task statistics.  

</div>



---


### `vault_target_logs_get`
Get logs for a given target.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Server.Common.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_target_id_** `int`  
Target ID.  
  
**_limit_** `int`  
Maximum number of logs to return (default is 1000).  
  
**_offset_** `int`  
Offset for pagination (default is 0).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Logs information.  

</div>



---


