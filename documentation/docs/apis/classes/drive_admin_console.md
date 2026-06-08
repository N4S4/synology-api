---
sidebar_position: 4
title: ✅ AdminConsole
description: "Synology Drive Admin Console API implementation." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# AdminConsole
## Overview
Synology Drive Admin Console API implementation.  
  
This class provides methods to retrieve and manage Synology Drive Admin Console status,
configuration, connections, logs, shares, and settings.  
  
## Methods
### `status_info`
Get Synology Drive status information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Status information.  
</div>
  



---


### `config_info`
Get Synology Drive configuration information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Configuration information.  
</div>
  



---


### `connections`
Get summary of Synology Drive connections.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Connection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Connections summary.  
</div>
  



---


### `drive_check_user`
Check user status in Synology Drive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User check result.  
</div>
  



---


### `active_connections`
Get list of active Synology Drive connections.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Connection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of active connections.  
</div>
  



---


### `active_sync_connections`
Get list of active Synology Drive ShareSync connections.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDriveShareSync.Connection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of active ShareSync connections.  
</div>
  



---


### `share_active_list`
Get list of active shares in Synology Drive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Share`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of active shares.  
</div>
  



---


### `log`
Get Synology Drive logs.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Log`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_share_type_** `str`  
Type of share to filter logs (default is 'all').  
  
**_get_all_** `bool`  
Whether to get all logs (default is False).  
  
**_limit_** `int`  
Maximum number of logs to return (default is 1000).  
  
**_keyword_** `str`  
Keyword to filter logs (default is '').  
  
**_date_from_** `int`  
Start date in epoch format (default is 0).  
  
**_date_to_** `int`  
End date in epoch format (default is 0).  
  
**_username_** `str`  
Username to filter logs (default is '').  
  
**_target_** `str`  
Target type to filter logs (default is 'user').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Log information.  
</div>
  



---


### `c2fs_share`
Get list of C2FS shares.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.C2FS.Share`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of C2FS shares.  
</div>
  



---


### `settings`
Get Synology Drive settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Settings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Settings information.  
</div>
  



---


### `db_usage`
Get Synology Drive database usage.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.DBUsage`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Database usage information.  
</div>
  



---


### `delete_status`
Get status of deleted nodes in Synology Drive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Node.Delete`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Delete status information.  
</div>
  



---


### `file_property_transfer_status`
Get file property transfer status for User Home migration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Migration.UserHome`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
File property transfer status.  
</div>
  



---


### `user_sync_profile`
Get user sync profile(s).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Profiles`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
Username to filter profiles (default is '').  
  
**_start_** `int`  
Start index for pagination (default is 0).  
  
**_limit_** `str or int`  
Maximum number of profiles to return (default is 'null').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User sync profile information.  
</div>
  



---


### `drive_info`
Get Synology Drive Server information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Server metadata including DSM ID, versioning settings,
display preferences, and beta feature flags.  
</div>
  



---


### `drive_dsm_info`
Get DSM integration information for Drive.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.DSM`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM-level Drive settings and integration status.  
</div>
  



---


### `drive_statistics`
Get Synology Drive usage statistics.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Statistics`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Statistics including file counts, user counts,
and storage usage breakdowns.  
</div>
  



---


### `drive_activation`
Get Synology Drive license activation status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Activation`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Activation status, time, and serial number.  
</div>
  



---


### `drive_share_list`
List all Synology Drive shares (team folders).  
Unlike :meth:`share_active_list` which uses ``list_active``,
this method uses the full ``list`` endpoint returning all
shares regardless of activity status.  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Share`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.
Each item includes share name, permissions, watermark
settings, and download restrictions.  
</div>
  



---


### `drive_team_folder_list`
List all Synology Drive team folders.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.TeamFolders`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


### `drive_privilege_list`
List Synology Drive user privileges.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Privilege`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 100).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"users": [...], "total": N, "offset": N}, "success": true}``.  
</div>
  



---


### `drive_task_list`
List Synology Drive background tasks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Tasks`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


### `drive_label_list`
List Synology Drive file labels/tags.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Labels`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


### `drive_notification_list`
List Synology Drive notifications.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Notifications`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 50).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


### `drive_node_locking_option`
Get Synology Drive file locking configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.NodeLockingOption`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
File locking settings including auto-lock, view-level
permissions, and supported file type views.  
</div>
  



---


### `sharesync_config`
Get Synology Drive ShareSync configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDriveShareSync.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
ShareSync settings including conflict policy,
rename handling, repository location, and
synchronization mode.  
</div>
  



---


### `index_pause`
Pause native client index for a specified duration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SynologyDrive.Index`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_time_pause_** `int`  
Pause duration in seconds (default is 60).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


