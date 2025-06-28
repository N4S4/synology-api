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

## Methods
### `settings_list`



---


### `active_connections_list`



---


### `log_list`



---


### `network_interface_setting`



---


### `security_autoblock_setting`



---


### `permission_setting`



---


### `pptp_settings_info`



---


### `openvpn_settings_info`



---


### `l2tp_settings_info`



---


### `openvpn_export_configuration`
Downloads the openvpn\.zip containing the VPNConfig\.ovpn file  
  
#### Internal API
<div class="padding-left--md">
`SYNO.VPNServer.Settings.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_as_zip_file_** `bool`  
If the bytes should be converted to a ZipFile  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the OpenVPN configuration file as bytes or a ZipFile object if `as_zip_file` is True.  

</div>



---


