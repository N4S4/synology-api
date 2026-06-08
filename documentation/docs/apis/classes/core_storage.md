---
sidebar_position: 23
title: 🚧 CoreStorage
description: "Core Storage API implementation for Synology NAS." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
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


### `btrfs_dedupe_check_quota`
Check storage quota usage.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_dry_run`
Run a dry-run (simulation) operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_get_schedule_plan`
Get the current schedule plan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_get_status`
Get the current operational status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_get_volume_info`
Get volume information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_manual_dedupe`
Manually trigger data deduplication.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_rescan_quota_v2`
Rescan storage quota (version 2).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_set_reclaim_type`
Set the space reclamation type.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_set_schedule_plan`
Set or update the schedule plan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_set_volume_schedule_config`
Configure the volume schedule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `btrfs_dedupe_stop`
Stop the current operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.BtrfsDedupe`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.BtrfsDedupe``.  
</div>
  



---


### `cache_protection_disable_passive`
Disable passive cache protection mode.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `cache_protection_enable_passive`
Enable passive cache protection mode.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `cache_protection_get_config`
Get the current configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `cache_protection_get_status`
Get the current operational status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `cache_protection_get_status_all`
Get the status of all items.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `cache_protection_update_config`
Update the configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Cache.Protection`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Cache.Protection``.  
</div>
  



---


### `storage_check_do_data_scrubbing`
Start a data scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_do_disk_scan`
Start a disk scan operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_ignore_data_scrubbing`
Ignore/skip a data scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_is_building`
Check if the storage is currently building/rebuilding.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_is_data_scrubbing`
Check if data scrubbing is currently running.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_reboot_after_rebuild`
Get or configure auto-reboot after rebuild.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_remove_ask_for_fsck`
Clear the file-system check prompt.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_remove_ask_for_fsck_scan`
Clear the fsck scan prompt.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_remove_ask_for_remap_scan`
Clear the remap scan prompt.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_remove_ask_for_wcache_lost_data_scrubbing`
Clear the write-cache lost data scrubbing prompt.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `storage_check_should_ask_for_fsck_scan`
Check whether an fsck scan prompt should be shown.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Check`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Check``.  
</div>
  



---


### `detected_pool_assemble`
Assemble/re-assemble a detected storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.DetectedPool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.DetectedPool``.  
</div>
  



---


### `detected_pool_remove`
Remove a component.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.DetectedPool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.DetectedPool``.  
</div>
  



---


### `dual_enclosure_load`
Load/retrieve all entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.DualEnclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.DualEnclosure``.  
</div>
  



---


### `enclosure_exp_fw_fail_get`
Get expansion unit firmware failure information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_exp_fw_update`
Update expansion unit firmware.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_exp_fw_update_cancel_notify`
Cancel expansion unit firmware update notification.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_exp_fw_update_list_get`
Get the list of available expansion unit firmware updates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_exp_fw_update_status_get`
Get the status of expansion unit firmware update.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_is_exp_connected`
Check if the expansion unit is connected.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_load`
Load all enclosure information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_exp_fw_fail_get`
Get SHA expansion unit firmware failure information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_exp_fw_update`
Update SHA expansion unit firmware.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_exp_fw_update_cancel_notify`
Cancel SHA expansion unit firmware update notification.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_exp_fw_update_list_get`
List SHA expansion unit firmware updates available.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_exp_fw_update_status_get`
Get SHA expansion unit firmware update status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `enclosure_sha_is_exp_connected`
Check if the SHA expansion unit is connected.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Enclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Enclosure``.  
</div>
  



---


### `encryption_vault_disable`
Disable offline volume operations.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_enable`
Enable the feature.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_get_info`
Get flash cache information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_pack_for_ma`
Package OAuth credentials for the mail account.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_repair`
Repair/recover the entity.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_reset`
Reset the Taipei enclosure.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_set_autounlock_key`
Set an auto-unlock key for the encryption vault.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_set_for_ma`
Set the person mail account for the Mail Account service.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_sync_to_passive`
Sync data to the passive enclosure.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_verify_passwd`
Verify the encryption vault password.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault``.  
</div>
  



---


### `encryption_vault_unlock_enter_passwd`
Enter passwd.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.  
</div>
  



---


### `encryption_vault_unlock_get_passwd_wrong_record`
Get passwd wrong record.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.  
</div>
  



---


### `encryption_vault_unlock_skip_passwd`
Skip passwd.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.EncryptionKeyVault.UnlockMode``.  
</div>
  



---


### `flashcache_add_drive`
Add an SSD drive to the flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_advisor_history_get`
Get the Security Advisor scan history.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_advisor_poll`
Poll for Security Advisor scan progress.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_advisor_start`
Start a Security Advisor security scan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_advisor_stop`
Stop a running Security Advisor scan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_check_can_create`
Check if a new user can be created.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_check_can_lock_space`
Check if deduplication space can be locked.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_check_pin_metadata_and_rec_size`
Check pinned metadata and record size settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_check_system_raid`
Check system RAID configuration on the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_check_volume_abnormal_cant_create_cache`
Check if a volume abnormality prevents cache creation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_configure`
Configure DSM FindMe (QuickConnect) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_create_feasibility_hard_check`
Run a feasibility check for pool creation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_enable`
Enable a flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_estimate_mem_size`
Estimate memory requirements for pool operations.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_estimate_raid_size`
Estimate the RAID size for a pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_is_redundancy_degraded`
Check if pool redundancy is degraded.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_remove`
Remove SSDs from a flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_remove_cancel`
Cancel a volume removal operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_repair`
Repair a flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_replace`
Replace SSDs in a flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_shared_cache_config_get`
Get the shared SSD cache configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `flashcache_shared_cache_config_set`
Set the shared SSD cache configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Flashcache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Flashcache``.  
</div>
  



---


### `kmip_check_loop`
Check the deduplication background loop status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_delete_key`
Delete an encryption key from the vault.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_erase_all_data`
Erase all data on spare disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_get`
Get KMIP server configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_get_key_list`
List all encryption keys in the vault.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_get_server_hostname`
Get the hostname of the storage server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_get_version_info`
Get HA license version information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_import_cert`
Import a KMIP server certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_import_server_ca`
Import the KMIP server CA certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_list_cert`
List KMIP client certificates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_remove_cert`
Remove a KMIP certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_renew_cert`
Renew a KMIP certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_set`
Configure KMIP server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_set_cert`
Set/configure a KMIP certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_test_conn`
Test the KMIP server connection.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `kmip_transfer_data`
Transfer volume data to another location.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.KMIP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.KMIP``.  
</div>
  



---


### `pool_cancel_data_scrubbing`
Cancel an ongoing data scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_check_fast_repair`
Check if a fast repair is possible on the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_create`
Create a new storage pool on the NAS.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_data_scrubbing`
Get/set data scrubbing status for the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_data_scrubbing_plain`
Run a plain data scrubbing operation (no dedupe).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_deactivate`
Deactivate the flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_delete`
Delete an existing storage pool (destructive — all data lost).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_edit_desc`
Edit the description of a user account.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_enum_resource`
Enumerate resources within a storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_estimate_size`
Estimate the resulting size after pool expansion.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_expand_by_add_disk`
Expand a storage pool by adding new disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_expand_unallocated`
Expand a pool using unallocated space.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_expand_unfinished_shr`
Resume an interrupted SHR expansion.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_get_setting`
Get the flash cache settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_is_disk_detected_old_info`
Check if a detected disk has old RAID information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_migrate`
Migrate a storage pool to a different RAID type.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_pause_data_scrubbing`
Pause an ongoing data scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_pre_delete_check`
Check if a pool can be safely deleted.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_reassemble`
Re-assemble a pool from detected disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_remove_missing_pool`
Remove a missing storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_remove_raid_sb_cache`
Remove RAID superblock cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_repair`
Repair a degraded storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_replace`
Replace a failing disk in a storage pool with a new one.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_set_setting`
Configure advanced storage pool settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `pool_update_raid_sb_cache`
Update RAID superblock cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Pool`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Pool``.  
</div>
  



---


### `scrubbing_get_state`
Get the current data scrubbing state for a storage space.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Scrubbing`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_space_id_** `str`  
Storage space/volume identifier to query scrubbing state for.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict`  
Scrubbing state for the specified space.  
</div>
  



---


### `smart_get_health_info`
Get storage health information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_get_latest_online_drive_db_info`
Get the latest online drive database info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_get_smart_info`
Get S.M.A.R.T. information for all disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_list`
List all entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_secure_erase`
Securely erase a disk in the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_smart_warning_get`
Get S.M.A.R.T. warning settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_smart_warning_set`
Configure S.M.A.R.T. warning settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `smart_update_smartctl_db`
Update the smartctl drive database.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Smart`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Smart``.  
</div>
  



---


### `spare_conf_get`
Get detailed information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Spare.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Spare.Conf``.  
</div>
  



---


### `spare_conf_set`
Set spare disk configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Spare.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Spare.Conf``.  
</div>
  



---


### `taipei_enclosure_load`
Load/retrieve all entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.TaipeiEnclosure`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.TaipeiEnclosure``.  
</div>
  



---


### `volume_cancel_data_scrubbing`
Cancel volume data scrubbing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_cancel_defrag`
Cancel an ongoing defragmentation operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_cancel_fs_scrubbing`
Cancel an ongoing file-system scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_change_recovery_key`
Change the encryption key vault recovery key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_clean_dek`
Clean DEK (Data Encryption Key) entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_convert_shr_to_pool`
Convert SHR to a storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_convert_shr_without_drive`
Convert SHR to a pool without adding drives.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_create`
Create a new volume on the NAS.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_create_on_existing_pool`
Create a volume on an existing pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_data_scrubbing`
Get/set data scrubbing status for the volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_defrag`
Start a defragmentation operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_delete`
Delete an existing volume (destructive).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_deploy_unused`
Deploy unused disk space to a volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_disable_space_usage`
Disable Btrfs space usage tracking.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_enable_space_usage`
Enable Btrfs space usage tracking.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_enum_resource`
Enumerate resources in a volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_estimate_size`
Estimate volume size after changes.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_expand_by_add_disk`
Expand a volume by adding disks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_expand_pool_child`
Expand a child of the storage pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_expand_unallocated`
Expand a volume using unallocated space.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_expand_unfinished_shr`
Resume interrupted SHR volume expansion.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_export_recovery_key`
Export the encryption vault recovery key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_failover_keep_rw`
Fail over to secondary enclosure while keeping read-write.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_fs_info_on_pool_meta_set`
Set file-system info on pool metadata.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_fs_info_on_pool_meta_update`
Update file-system info on pool metadata.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_fs_scrubbing`
Start a file-system scrubbing operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_get_dump_volumes`
Get dump/backup volume information for flash cache.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_get_recovery_key`
Get the encryption key vault recovery key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_get_recovery_key_info`
Get information about the vault recovery key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_get_space_usage`
Get Btrfs deduplication space usage statistics.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_migrate`
Migrate a volume to a different configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_next_trim_time_get`
Get the next scheduled TRIM time for a volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_pause_data_scrubbing`
Pause volume data scrubbing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_pre_delete_check`
Check if a volume can be safely deleted.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_repair`
Repair a degraded volume.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_set_dek`
Set a DEK (Data Encryption Key) entry.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_set_setting`
Configure advanced volume settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_ssd_trim_get`
Get SSD TRIM configuration for the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_ssd_trim_save`
Save SSD TRIM configuration for the pool.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_transfer_to_rw`
Transfer volume to read-write mode.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_unlock_by_recovery_key`
Unlock the encryption vault using the recovery key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_unlock_by_vault`
Unlock the encryption vault using a vault key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_unlock_by_vault_password_key`
Unlock the encryption vault using a vault password key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_vol_extent_size_get`
Get volume extent size configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_vol_extent_size_set`
Set volume extent size configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume``.  
</div>
  



---


### `volume_installer_quick_create`
Quick create.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume.Installer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume.Installer``.  
</div>
  



---


### `volume_installer_quick_create_precheck`
Quick create precheck.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume.Installer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume.Installer``.  
</div>
  



---


### `volume_offline_execute`
Execute the pending offline volume operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume.OfflineOp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.  
</div>
  



---


### `volume_offline_pre_estimate`
Pre estimate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume.OfflineOp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.  
</div>
  



---


### `volume_offline_stop`
Stop the current operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Storage.CGI.Volume.OfflineOp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Storage.CGI.Volume.OfflineOp``.  
</div>
  



---


