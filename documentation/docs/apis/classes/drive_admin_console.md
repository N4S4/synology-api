---
sidebar_position: 4
title: 🚧 AdminConsole
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# AdminConsole
:::warning
 
This API is not documented yet.
 
:::
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


