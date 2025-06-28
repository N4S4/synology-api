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

## Methods
### `backup_repository_get`
Get repository information for given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Repository` 
</div>
  



---


### `backup_repository_list`
Get a list of all present repositories in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Repository` 
</div>
  



---


### `backup_task_list`
Get current restoring information and a list of present tasks in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_status`
Get status and state of task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_get`
Get detailed task information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_result`
Get last result summary information of a task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_run`
Run backup task for corresponding task_id.  
If the task is not in backupable state, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_cancel`
Cancel currently running backup task.  
If the task is not running, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_suspend`
Suspend currently running backup task.  
If the task is not running or not yet suspendable, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_discard`
Discard currently suspended backup task.  
If the task is not suspended, the request will not fail, and will fail to discard the task, leaving the task state as "Failed".  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_resume`
Discard currently suspended backup task.  
If the task is not suspended, the request will not fail, and will fail to resume the task, leaving the task state as "Failed".  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `backup_task_remove`
Remove one or more backup tasks.  
Data in destination will not be removed. It is still possible to relink the task using the original .hbk file.
The API requires an array of tasks to remove, it should be passed as a string with the following format:
`task_id_list = '[29]'` || `task_id_list = '[29,15]'`  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Task` 
</div>
  



---


### `integrity_check_run`
Run integrity check for backup task.  
If the task is running, the request will not fail, and will fail to perform the integrity check due to target is busy.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Target` 
</div>
  



---


### `integrity_check_cancel`
Cancel currently running integrity check for backup task.  
If integrity check is not running, the API will return an error, usually 44xx.  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Target` 
</div>
  



---


### `hb_logs_get`
Get Hyper Backup UI logs.  
`filter_date_from` and `filter_date_to` need to be passed in epoch format.  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Client.Common.Log` 
</div>
  



---


### `vault_target_list`
List all available targets in Vault.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Target` 
</div>
  



---


### `vault_concurrency_get`
Get number of concurrent tasks allowed to run in HB Vault. Default value is 2.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Config` 
</div>
  



---


### `vault_concurrency_set`
Set number of concurrent tasks allowed to run in HB Vault. Default value is 2.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Config` 
</div>
  



---


### `vault_target_settings_get`
Get settings of target.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.VersionBackup.Target` 
</div>
  



---


### `vault_task_statistics_get`
Get statistics for given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Server.Common.Statistic` 
</div>
  



---


### `vault_target_logs_get`
Get logs for given task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.SDS.Backup.Server.Common.Log` 
</div>
  



---


