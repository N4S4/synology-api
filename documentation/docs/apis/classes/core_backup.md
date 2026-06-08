---
sidebar_position: 7
title: ✅ Backup
description: "Synology Hyper Backup API." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
:::tip
 
This page contains documentation for the `Backup` class and its subclasses:  
-  [S2SServer](#s2sserver)   
-  [DRNode](#drnode)   

 
:::
# Backup
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


### `backup_app_get_icon`
Get the Hyper Backup application icon.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App``.  
</div>
  



---


### `backup_app_list`
List all backup tasks currently configured in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Backup``.  
</div>
  



---


### `backup_app_mysql_check`
Check whether MySQL/MariaDB backup support is available on the NAS.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Backup``.  
</div>
  



---


### `backup_app_surveillance_check`
Check whether Surveillance Station backup support is available on the NAS.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Backup``.  
</div>
  



---


### `restore_app_list`
List available restore points/tasks in Hyper Backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Restore``.  
</div>
  



---


### `restore_app_mysql_check`
Check whether MySQL/MariaDB restore capability is available.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Restore``.  
</div>
  



---


### `restore_app_surveillance_check`
Check whether Surveillance Station restore capability is available.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.App.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.App.Restore``.  
</div>
  



---


### `autobackup_config_backup`
Trigger an automatic backup based on the configured schedule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_download_private_key`
Download the private key used for encrypted backup archives.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_get`
Get the current auto-backup configuration (schedule, targets, encryption).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_get_meta`
Get metadata about the auto-backup configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_list`
List all auto-backup configuration entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_restore`
Restore system configuration from an auto-backup archive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_set`
Set or update the auto-backup configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_status`
Get the current status of auto-backup operations.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `autobackup_config_upload_private_key`
Upload a private key for encrypting future auto-backup archives.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.AutoBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.AutoBackup``.  
</div>
  



---


### `backup_config_download`
Download a system configuration backup archive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Backup``.  
</div>
  



---


### `backup_config_list`
List available system configuration backup archives.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Backup``.  
</div>
  



---


### `backup_config_start`
Start a system configuration backup immediately.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Backup``.  
</div>
  



---


### `backup_config_status`
Get the status of a system configuration backup operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Backup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Backup``.  
</div>
  



---


### `restore_config_check`
Verify the integrity and compatibility of a restore archive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_delete`
Delete a saved system configuration restore archive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_list`
List available system configuration restore archives.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_list_conflict`
List any conflicts detected in a restore archive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_start`
Start a system configuration restore operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_status`
Get the status of a restore operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


### `restore_config_upload`
Upload a system configuration archive for restore.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Backup.Config.Restore`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Backup.Config.Restore``.  
</div>
  



---


## S2SServer
## Overview
Synology S2S (Server-to-Server) backup API wrapper.  
  
  
  
## Methods
### `s2s_server_get`
Get the current Server-to-Server backup server configuration (task list, schedule, targets).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.S2S.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.S2S.Server``.  
</div>
  



---


### `s2s_server_set`
Set or update the Server-to-Server backup server configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.S2S.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.S2S.Server``.  
</div>
  



---


## DRNode
## Overview
Synology Disaster Recovery / Snapshot Replication API wrapper.  
  
  
  
## Methods
### `dr_node_check_and_reset`
Check the DR node status and reset if needed (used during setup/recovery).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_get_net_info`
Get network information for the local DR node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_get_remote_net_info`
Get network information for the remote DR partner node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_info`
Get general information and status of the DR node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_reset`
Reset the DR node configuration to factory defaults.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_test_connection`
Test the network connection to the remote DR partner node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_test_download_speed`
Run a download speed test to the remote DR partner.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_test_privilege`
Verify that the DR node has sufficient privileges for replication.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_node_test_sync_speed`
Run a sync speed benchmark between local and remote DR nodes.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node``.  
</div>
  



---


### `dr_credential_create`
Create credentials for authenticating with a remote DR partner node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_delete`
Delete stored DR partner credentials.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_get`
Get the current DR partner credential details.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_list`
List all stored DR partner credentials.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_relay`
Relay/forward credentials through an intermediate DR node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_reverse_create`
Create reverse credentials so the partner node can authenticate back.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_set`
Set or update DR partner credentials.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_temp_create`
Create temporary credentials for one-time DR operations.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_temp_reverse_create`
Create temporary reverse credentials for partner node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_test_create`
Test-validate credential creation parameters before committing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_test_reverse_create`
Test-validate reverse credential parameters before committing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_credential_test_set`
Test-validate credential update parameters before committing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Credential``.  
</div>
  



---


### `dr_session_create`
Create a new DR replication session with the partner node.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Session``.  
</div>
  



---


### `dr_session_delete`
Delete/terminate an existing DR replication session.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Session``.  
</div>
  



---


### `dr_session_find`
Find and enumerate active DR replication sessions.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Session``.  
</div>
  



---


### `dr_session_get`
Get details and status of a specific DR replication session.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Session``.  
</div>
  



---


### `dr_session_temp_create`
Create a temporary DR session for testing or one-off sync.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DR.Node.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DR.Node.Session``.  
</div>
  



---


### `dr_log_clear`
Clear all entries from the Disaster Recovery log.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Log`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Log``.  
</div>
  



---


### `dr_log_export`
Export the Disaster Recovery log to a downloadable file.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Log`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Log``.  
</div>
  



---


### `dr_log_list`
List all entries in the Disaster Recovery log.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Log`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Log``.  
</div>
  



---


### `dr_retention_check_worm_lockable`
Check whether a snapshot can be WORM-locked (Write Once Read Many).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_clear_worm_lock_notify_time`
Clear the WORM lock expiration notification timer.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_delete`
Delete a retention policy entry.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_get`
Get the current snapshot retention policy configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_get_timezone`
Get the timezone used for retention policy scheduling.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_get_worm_lock`
Get the WORM lock configuration for protected snapshots.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_info`
Get general information about the retention policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_notify_worm_lock_disable`
Disable WORM lock expiration notifications.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_set`
Set or update the snapshot retention policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_set_timezone`
Set the timezone used for retention policy scheduling.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


### `dr_retention_set_worm_lock`
Enable/configure WORM lock protection for snapshots.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DisasterRecovery.Retention`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DisasterRecovery.Retention``.  
</div>
  



---


