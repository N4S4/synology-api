---
sidebar_position: 23
title: 🚧 CoreStorage
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreStorage
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Storage API implementation for Synology NAS.  
  
This class provides methods to manage storage disks, pools, volumes,
iSCSI LUNs, quotas, and recycle bin operations.  
  
## Methods
### `storage_disk_list`
List all storage disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Disk`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of storage disks and their status.  
</div>
  



---


### `storage_disk_get`
Get information for a specific disk.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Disk`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_disk_id_** `str`  
The disk identifier (e.g., 'sda').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Disk information.  
</div>
  



---


### `storage_disk_fw_upgrade_get`
Get disk firmware upgrade status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Disk.FWUpgrade`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firmware upgrade availability and status.  
</div>
  



---


### `storage_disk_fw_upgrade_start`
Start a disk firmware upgrade.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Disk.FWUpgrade`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_disk_id_** `str`  
The disk identifier to upgrade.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `storage_pool_list`
List all storage pools.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of storage pools.  
</div>
  



---


### `storage_pool_get`
Get information for a specific storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Pool`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_pool_id_** `str`  
The storage pool identifier.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Storage pool information.  
</div>
  



---


### `storage_pool_set`
Update storage pool settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Pool`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_pool_id_** `str`  
The storage pool identifier.  
  
**_description_** `str`  
New description for the pool.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `storage_volume_list`
List all storage volumes.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of storage volumes.  
</div>
  



---


### `storage_volume_get`
Get information for a specific volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Volume`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_volume_path_** `str`  
The volume path (e.g., '/volume1').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Volume information.  
</div>
  



---


### `storage_volume_set`
Update volume settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.Volume`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_volume_path_** `str`  
The volume path (e.g., '/volume1').  
  
**_description_** `str`  
New description for the volume.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `iscsi_lun_list`
List all iSCSI LUNs.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.iSCSILUN`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of iSCSI LUNs.  
</div>
  



---


### `iscsi_lun_get`
Get information for a specific iSCSI LUN.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.iSCSILUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_lun_id_** `str`  
The iSCSI LUN identifier.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
iSCSI LUN information.  
</div>
  



---


### `iscsi_lun_set`
Update iSCSI LUN settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Storage.iSCSILUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_lun_id_** `str`  
The iSCSI LUN identifier.  
  
**_name_** `str`  
New name for the LUN.  
  
**_description_** `str`  
New description for the LUN.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `storage_load_info`
Get full Storage Manager overview.  
Returns disk, pool, volume, enclosure and port information
in a single call. This is the primary endpoint used by the
Storage Manager web UI.  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Storage`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"disks": [...], "detected_pools": [...],
"overview_data": {...}, "ports": [...], ...}, "success": true}``.  
</div>
  



---


### `storage_smart_scheduler_list`
List S.M.A.R.T. test schedules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart.Scheduler`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.
Each item includes schedule type, frequency, and target disks.  
</div>
  



---


### `storage_hdd_manager_get`
Get HDD health threshold settings.  
Returns S.M.A.R.T. warning thresholds for bad sectors,
remaining life, and other disk health indicators.  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.HddMan`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"BadSctrThrEn": ..., "RemainLifeThrEn": ...,
...}, "success": true}``.  
</div>
  



---


### `storage_spare_list`
List hot spare disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Spare`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"hotSpares": [...]}, "success": true}``.  
</div>
  



---


### `quota_get`
Get quota settings for a volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Quota`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_volume_path_** `str`  
The volume path (e.g., '/volume1').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Quota configuration.  
</div>
  



---


### `quota_list`
List quota settings for all volumes.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Quota`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of quota settings.  
</div>
  



---


### `quota_set`
Set quota for a volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Quota`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_volume_path_** `str`  
The volume path (e.g., '/volume1').  
  
**_enabled_** `bool`  
Enable or disable quota. Defaults to True.  
  
**_quota_mb_** `int`  
Quota size in megabytes.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `recycle_bin_get`
Get recycle bin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.RecycleBin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Recycle bin configuration.  
</div>
  



---


### `recycle_bin_set`
Set recycle bin configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.RecycleBin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable or disable recycle bin. Defaults to True.  
  
**_retention_days_** `int`  
Number of days to retain deleted files.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `recycle_bin_clean`
Empty the recycle bin.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.RecycleBin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_share_name_** `str`  
Shared folder name to clean. If None, cleans all recycle bins.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `recycle_bin_user_get`
Get per-user recycle bin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.RecycleBin.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
The username.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Per-user recycle bin configuration.  
</div>
  



---


### `recycle_bin_user_set`
Set per-user recycle bin configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.RecycleBin.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
The username.  
  
**_enabled_** `bool`  
Enable or disable per-user recycle bin. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


