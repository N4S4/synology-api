---
sidebar_position: 19
title: 🚧 LogCenter
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# LogCenter
:::warning
 
This API is not documented yet.
 
:::
## Overview
Interface for Synology Log Center API.

Provides methods to interact with log center features such as retrieving logs,
client status, remote archives, and storage settings.
## Methods
### `logcenter`
Retrieve the list of log center receive rules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.LogCenter.RecvRule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the receive rules or an error message.  

</div>



---


### `client_status_cnt`
Retrieve the count status from the syslog client.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the count status or an error message.  

</div>



---


### `client_status_eps`
Retrieve the EPS (events per second) status from the syslog client.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the EPS status or an error message.  

</div>



---


### `remote_log_archives`
Retrieve the list of remote log archive subfolders.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.LogCenter.Log` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing remote archive subfolders or an error message.  

</div>



---


### `display_logs`
Retrieve the list of logs from the syslog client.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.Log` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the logs or an error message.  

</div>



---


### `setting_storage_list`
Retrieve the log center storage settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.LogCenter.Setting.Storage` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing storage settings or an error message.  

</div>



---


### `registry_send_list`
Retrieve the list of log center client registry send settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.LogCenter.Client` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing registry send settings or an error message.  

</div>



---


### `history`
Retrieve the log center history.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.LogCenter.History` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the log center history or an error message.  

</div>



---


