---
sidebar_position: 25
title: 🚧 CoreUpgrade
description: "Extended Core Upgrade API implementation for Synology NAS." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreUpgrade
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Extended Core Upgrade API implementation for Synology NAS.  
  
This class provides methods for cluster-level upgrades, group upgrades,
patch management, pre-checks, and remote upgrade actions.  
  
## Methods
### `auto_upgrade_security_get`
Get auto-upgrade security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.AutoUpgrade.Security`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Security auto-upgrade configuration.  
</div>
  



---


### `auto_upgrade_security_set`
Set auto-upgrade security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.AutoUpgrade.Security`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable or disable security auto-upgrade. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `cluster_patch_get`
Get cluster patch information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Patch`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Cluster patch status.  
</div>
  



---


### `cluster_patch_list`
List available cluster patches.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Patch`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of cluster patches.  
</div>
  



---


### `cluster_server_get`
Get cluster upgrade server information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Cluster upgrade server status.  
</div>
  



---


### `cluster_server_list`
List cluster upgrade servers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of cluster upgrade servers.  
</div>
  



---


### `cluster_server_download_get`
Get cluster server download status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Server.Download`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Download status for cluster server upgrade.  
</div>
  



---


### `cluster_server_download_start`
Start cluster server upgrade download.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Cluster.Server.Download`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `upgrade_group_get`
Get upgrade group information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Upgrade group status.  
</div>
  



---


### `upgrade_group_list`
List upgrade groups.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of upgrade groups.  
</div>
  



---


### `upgrade_group_download_get`
Get group download status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group.Download`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Group upgrade download status.  
</div>
  



---


### `upgrade_group_download_start`
Start group upgrade download.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group.Download`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `upgrade_group_setting_get`
Get group upgrade settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group.Setting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Group upgrade settings.  
</div>
  



---


### `upgrade_group_setting_set`
Set group upgrade settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Group.Setting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable or disable group upgrade. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `group_install_get`
Get group install status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.GroupInstall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Group install status.  
</div>
  



---


### `group_install_start`
Start a group install.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.GroupInstall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `group_install_network_get`
Get group install network status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.GroupInstall.Network`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Network status for group install.  
</div>
  



---


### `group_install_network_set`
Set group install network configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.GroupInstall.Network`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Network configuration key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `junior_mode_data_get`
Get junior mode data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.JuniorModeData`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Junior mode data.  
</div>
  



---


### `junior_mode_data_set`
Set junior mode data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.JuniorModeData`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Junior mode configuration key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `upgrade_patch_get`
Get upgrade patch information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Patch`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Upgrade patch status.  
</div>
  



---


### `upgrade_patch_list`
List available upgrade patches.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.Patch`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of upgrade patches.  
</div>
  



---


### `upgrade_precheck_get`
Get upgrade pre-check status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.PreCheck`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Pre-check results for pending upgrade.  
</div>
  



---


### `upgrade_precheck_start`
Start an upgrade pre-check.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.PreCheck`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `remote_action_get`
Get remote upgrade action status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.RemoteAction`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Remote action status.  
</div>
  



---


### `remote_action_set`
Set a remote upgrade action.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Upgrade.RemoteAction`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_action_** `str`  
The remote action to perform (e.g., 'install', 'cancel').  
  
**_**kwargs_** `object`  
Additional action parameters.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


