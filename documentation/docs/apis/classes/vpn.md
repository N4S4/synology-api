---
sidebar_position: 34
title: 🚧 VPN
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# VPN
:::warning
 
This API is not documented yet.
 
:::
## Overview
API wrapper for Synology VPN Server.  
  
Provides methods to retrieve VPN settings, active connections, logs, network interfaces,
security autoblock settings, permissions, and VPN protocol-specific settings.  
  
## Methods
### `settings_list`
Retrieve VPN server settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Config` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
VPN server settings as a dictionary, or an error message as a string.  

</div>



---


### `active_connections_list`
Retrieve a list of active VPN connections.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Management.Connection` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sort_** `str`  
Field to sort by. Default is 'login_time'.  
  
**_sort_dir_** `str`  
Sort direction ('ASC' or 'DESC'). Default is 'DESC'.  
  
**_start_** `int`  
Pagination start index. Default is 0.  
  
**_limit_** `int`  
Maximum number of results to return. Default is 100.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Active connections as a dictionary, or an error message as a string.  

</div>



---


### `log_list`
Retrieve VPN server logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Management.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Pagination start index. Default is 0.  
  
**_limit_** `int`  
Maximum number of logs to return. Default is 50.  
  
**_prtltype_** `int`  
Protocol type filter. Default is 0 (all).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Logs as a dictionary, or an error message as a string.  

</div>



---


### `network_interface_setting`
Retrieve VPN network interface settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Management.Interface` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network interface settings as a dictionary, or an error message as a string.  

</div>



---


### `security_autoblock_setting`
Retrieve security autoblock settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Security.AutoBlock` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Autoblock settings as a dictionary, or an error message as a string.  

</div>



---


### `permission_setting`
Retrieve VPN permission settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Management.Account` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_start_** `int`  
Pagination start index. Default is 0.  
  
**_limit_** `int`  
Maximum number of results to return. Default is 100.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Permission settings as a dictionary, or an error message as a string.  

</div>



---


### `pptp_settings_info`
Retrieve PPTP VPN settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Config` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
PPTP settings as a dictionary, or an error message as a string.  

</div>



---


### `openvpn_settings_info`
Retrieve OpenVPN settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Config` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
OpenVPN settings as a dictionary, or an error message as a string.  

</div>



---


### `l2tp_settings_info`
Retrieve L2TP VPN settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Config` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
L2TP settings as a dictionary, or an error message as a string.  

</div>



---


### `openvpn_export_configuration`
Download the OpenVPN configuration as a zip file or bytes.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_as_zip_file_** `bool`  
If True, return a ZipFile object. If False, return bytes. Default is False.  
  

</div>
#### Returns
<div class="padding-left--md">
`bytes or ZipFile`  
The OpenVPN configuration file as bytes, or a ZipFile object if `as_zip_file` is True.  

</div>



---


