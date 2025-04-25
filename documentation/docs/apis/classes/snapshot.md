---
sidebar_position: 27
title: ✅ Snapshot
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Snapshot
## Overview
Class for interacting with Snapshot Replication APIs.

This class implements APIs to manage snapshots.
There is no documentation for these APIs, so the implementation is based on network inspection.

### Supported methods

    - **Getters** : 
        - Get all share/LUN snapshots
        - Get all replications
        - Get all LUNs

    - **Setters** :
        - Set snapshot attributes
    
    - **Actions** :
        - Create share/LUN snapshot (WORM support only for share snaps ATM)
        - Delete share/LUN snapshot
        - Sync replication

Examples
--------
List snapshots for a share/LUN:
```python
from synology_api import snapshot
ss = snapshot.Snapshot('IP', 'PORT', 'USER', 'PASSWORD')

resp_share = ss.list_snapshots('share_name')
resp_lun = ss.list_snapshots_lun('src_lun_uuid')

print(resp_share, resp_lun)
```

Create a snapshot for a share/LUN:
```python
resp_share = ss.create_snapshot('share_name')
resp_lun = create_snapshot_lun('lun_id')

print(resp_share, resp_lun)
```

Delete snapshots for a share:
```python
resp_share = ss.delete_snapshots('share_name', ['snapshot_name'])
resp_lun = ss.delete_snapshots_lun(['snapshot_uuid'])

print(resp_share, resp_lun)
```

Set attributes for a snapshot:
```python
resp = ss.set_snapshot_attr('share_name', 'snapshot_name', description='new description', lock=True)
print(resp)
```
## Methods
### `list_snapshots`
List snapshots for a share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Snapshot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_name_** `str`  
Name of the share to list snapshots for.  
  
**_attribute_filter_** `list[str]`  
List of attributes filter to apply. Defaults to `[]` (no filter).  

Each attribute filter is a string in the format of `"attr==value"` or `"attr=value"` and optionally prefixed with `!` to negate the filter.  

The following are examples of valid attribute filters:
    - `["!hide==true", "desc==abc"]` -> hide is not true and desc is exactly abc.
    - `["desc=abc"]` -> desc has abc in it.  
  
**_additional_attribute_** `list[str]`  
List of snapshot attributes whose values are included in the response. Defaults to `[]` (only time is returned).  

Note that not all attributes are available via API. The following are confirmed to work:
    - `"desc"`
    - `"lock"`
    - `"worm_lock"`
    - `"schedule_snapshot"`  
  
**_offset_** `int`  
Offset to start listing from. Defaults to `0`.  
  
**_limit_** `int`  
Number of snapshots to return. Defaults to `-1` (all).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful, error message if not.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "snapshots": [
            {
                "desc": "",
                "lock": true,
                "schedule_snapshot": false,
                "time": "GMT+09-2023.09.11-23.23.40",
                "worm_lock": true,
                "worm_lock_begin": "1694442321",
                "worm_lock_day": "1",
                "worm_lock_end": "1694528721"
            }
        ],
        "total": 1
    },
    "success": true
}
```
</details>



---


### `list_snapshots_lun`
List snapshots for a LUN.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ISCSI.LUN` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_src_lun_uuid_** `str`  
UUID of the source LUN to list snapshots for.  
  
**_additional_** `list[str]`  
Additional fields to retrieve. Specify `[]` to get only basic information.   
Defaults to `["locked_app_keys", "is_worm_locked"]`  

Possible values:
- `"locked_app_keys"` -> If snapshot is preserved by the system, the locking package key will be returned.
- `"is_worm_locked"` -> Whether the snapshot is locked by WORM.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Dictionary containing the LUN snapshots information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "count": 2,
        "snapshots": [
            {
                "create_time": 1742739365,
                "description": "test",
                "is_app_consistent": false,
                "is_user_locked": true,
                "is_worm_locked": false,
                "locked_app_keys": [],
                "mapped_size": 0,
                "name": "SnapShot-1",
                "parent_lun_id": 6,
                "parent_uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "root_path": "/volume2",
                "snapshot_id": 1,
                "snapshot_time": 1742739365,
                "status": "Healthy",
                "taken_by": "user",
                "total_size": 1073741824,
                "type": 2,
                "uuid": "fb388ec7-f23a-4011-8d24-08ad9b1fef34",
                "version": "d4236543-510f-4269-ae73-7bc789aaa763",
                "worm_lock_day": "0"
            },
            {
                "create_time": 1742833700,
                "description": "Snapshot taken by [Synology API]",
                "is_app_consistent": false,
                "is_user_locked": false,
                "is_worm_locked": false,
                "locked_app_keys": [
                    "SnapshotReplication-synodr-657f3c72-f357-400d-96df-bb8ae4e5051f"
                ],
                "mapped_size": 0,
                "name": "SnapShot-2",
                "parent_lun_id": 6,
                "parent_uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "root_path": "/volume2",
                "snapshot_id": 2,
                "snapshot_time": 1742833700,
                "status": "Healthy",
                "taken_by": "user",
                "total_size": 1073741824,
                "type": 2,
                "uuid": "e981770c-f56d-4cb2-b7a7-4c4b11ba8eaa",
                "version": "58ee3b1a-192d-46fe-9cf3-0960e2a8670b",
                "worm_lock_day": "0"
            }
        ]
    },
    "success": true
}
```
</details>



---


### `list_luns`
List available LUNs  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ISCSI.LUN` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_types_** `list[str]`  
Type of LUNS to retrieve.  

 Defaults to `[ "BLOCK", "FILE", "THIN", "ADV", "SINK", "CINDER", "CINDER_BLUN", "CINDER_BLUN_THICK", "BLUN", "BLUN_THICK", "BLUN_SINK", "BLUN_THICK_SINK" ]`.  
 
 Possible values:
 - `"BLOCK"`
 - `"FILE"`
 - `"THIN"`
 - `"ADV"`
 - `"SINK"`
 - `"CINDER"`
 - `"CINDER_BLUN"`
 - `"CINDER_BLUN_THICK"`
 - `"BLUN"`
 - `"BLUN_THICK"`
 - `"BLUN_SINK"`
 - `"BLUN_THICK_SINK"`  
  
**_additional_info_** `list[str]`  
Additional LUN information to include in the response. Specify `[]` to get only basic information.  

Defaults to `[ "is_action_locked", "is_mapped", "extent_size", "allocated_size", "status", "allow_bkpobj", "flashcache_status", "family_config", "snapshot_info" ]`.  

Possible values:
- `"is_action_locked"`
- `"is_mapped"`
- `"extent_size"`
- `"allocated_size"`
- `"status"`
- `"allow_bkpobj"`
- `"flashcache_status"`
- `"family_config"`
- `"snapshot_info"`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing a list of LUNs present in the system.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "luns": [
            {
                "allocated_size": 0,
                "block_size": 512,
                "create_from": "",
                "description": "",
                "dev_attribs": [
                    {
                        "dev_attrib": "emulate_3pc",
                        "enable": 1
                    },
                    {
                        "dev_attrib": "emulate_tpws",
                        "enable": 1
                    },
                    {
                        "dev_attrib": "emulate_caw",
                        "enable": 1
                    },
                    {
                        "dev_attrib": "emulate_tpu",
                        "enable": 1
                    },
                    {
                        "dev_attrib": "emulate_fua_write",
                        "enable": 0
                    },
                    {
                        "dev_attrib": "emulate_sync_cache",
                        "enable": 0
                    },
                    {
                        "dev_attrib": "can_snapshot",
                        "enable": 1
                    }
                ],
                "dev_attribs_bitmap": 31,
                "dev_config": "",
                "dev_qos": {
                    "dev_limit": 0,
                    "dev_reservation": 0,
                    "dev_weight": 0,
                    "iops_enable": 0
                },
                "direct_io_pattern": 0,
                "extent_size": 0,
                "family_config": {
                    "parent_lun_name": "",
                    "parent_lun_uuid": "",
                    "parent_snapshot_time": 0,
                    "parent_snapshot_uuid": ""
                },
                "flashcache_id": -1,
                "flashcache_status": "no_cache",
                "is_action_locked": false,
                "is_mapped": true,
                "location": "/volume2",
                "lun_id": 6,
                "name": "LUN-1",
                "restored_time": 0,
                "retention": null,
                "scheduled_task": [
                    {
                        "general": {
                            "snap_rotate": true,
                            "snap_type": "app",
                            "task_enabled": false,
                            "task_name": "Task LUN-1",
                            "tid": -1,
                            "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                        },
                        "schedule": {
                            "date": "2025/3/24",
                            "date_type": 0,
                            "hour": 0,
                            "last_work_hour": 0,
                            "min": 0,
                            "monthly_week": [],
                            "next_trigger_time": "",
                            "repeat": 0,
                            "repeat_hour": 0,
                            "repeat_hour_store_config": null,
                            "repeat_min": 0,
                            "repeat_min_store_config": null,
                            "week_name": "0,1,2,3,4,5,6"
                        }
                    }
                ],
                "size": 1073741824,
                "snapshots": [
                    {
                        "create_time": 1742739365,
                        "description": "test",
                        "is_app_consistent": false,
                        "is_user_locked": true,
                        "mapped_size": 0,
                        "name": "SnapShot-1",
                        "parent_lun_id": 6,
                        "parent_uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "root_path": "/volume2",
                        "snapshot_id": 1,
                        "snapshot_time": 1742739365,
                        "status": {
                            "progress": {
                                "percent": -1,
                                "step": "waiting"
                            },
                            "type": "Healthy"
                        },
                        "taken_by": "user",
                        "total_size": 1073741824,
                        "type": 2,
                        "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "version": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    }
                ],
                "status": "normal",
                "type": 263,
                "type_str": "BLUN",
                "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "vpd_unit_sn": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
        ]
    },
    "success": true
}
```
</details>



---


### `list_replication_plans`
List replication plans.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DR.Plan` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_info_** `list[str]`  
List of additional information to include in the response. Specify `[]` to get only basic information.  

Defaults to `["sync_policy", "sync_report", "main_site_info", "dr_site_info", "can_do", "op_info", "last_op_info", "topology", "testfailover_info", "retention_lock_report"]`.  

Possible values:
    - `"sync_policy"` -> Information about the sync policy as schedule, retention, lock, etc.
    - `"sync_report"` -> Information about the previous runs and their results / error count.
    - `"main_site_info"` -> Information about the main site.
    - `"dr_site_info"` -> Information about the destination site.
    - `"can_do"` -> Information about the actions that can be performed on the replication plan.
    - `"op_info"` -> Information about the current operation (restoring / syncing / etc.).
    - `"last_op_info"` -> Information about the last operation.
    - `"topology"` -> Information about the replication topology (main / dr site & plan information).
    - `"testfailover_info"` -> Information about the previous test failover operation.
    - `"retention_lock_report"` -> Information about the first / last snapshot.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful, error message if not  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "plans": [{
            "additional": {
                "can_do": {
                    "can_cleanup_testfailover": false,
                    "can_delete": true,
                    "can_edit": true,
                    "can_export": false,
                    "can_failover": false,
                    "can_import": false,
                    "can_switchover": true,
                    "can_sync": true,
                    "can_testfailover": true,
                    "candidate_reprotect_new_mainsite": null
                },
                "dr_site_info": {
                    "hostname": "hostname",
                    "node_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "op_info": {
                        "op_progress": {
                            "percentage": -1
                        },
                        "op_status": 1
                    },
                    "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "role": 2,
                    "status": 1,
                    "target_id": "api-1",
                    "target_name": "api-1"
                },
                "last_op_info": {
                    "err_code": 0,
                    "is_success": true,
                    "op_status": 16,
                    "update_time": 1742739562
                },
                "main_site_info": {
                    "hostname": "hostname",
                    "node_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "op_info": {
                        "op_progress": {
                            "percentage": -1
                        },
                        "op_status": 1
                    },
                    "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "role": 1,
                    "status": 1,
                    "target_id": "api",
                    "target_name": "api"
                },
                "op_info": {
                    "op_progress": {
                        "percentage": -1
                    },
                    "op_status": 1
                },
                "retention_lock_report": {
                    "first_snapshot": "GMT+01-2025.03.23-15.17.39",
                    "last_snapshot": "GMT+01-2025.03.23-15.18.46",
                    "retain_first": false
                },
                "sync_policy": {
                    "enabled": true,
                    "is_app_aware": false,
                    "is_send_encrypted": false,
                    "is_sync_local_snapshots": false,
                    "mode": 2,
                    "next_trigger_time": 1742770800,
                    "notify_time_in_min": 720,
                    "readable_next_trigger_time": "Mon Mar 24 00:00:00 2025",
                    "schedule": {
                        "date_type": 0,
                        "hour": 0,
                        "last_work_hour": 0,
                        "min": 0,
                        "repeat_hour": 0,
                        "repeat_min": 0,
                        "week_name": "0,1,2,3,4,5,6"
                    },
                    "sync_window": {
                        "enabled": false,
                        "window": [
                            16777215,
                            16777215,
                            16777215,
                            16777215,
                            16777215,
                            16777215,
                            16777215
                        ]
                    },
                    "worm_lock_day": 7,
                    "worm_lock_enable": false,
                    "worm_lock_notify_time": 0
                },
                "sync_report": {
                    "fail_sync_count": 0,
                    "recent_records": [
                        {
                            "begin_time": 1742739460,
                            "current_speed": 0,
                            "data_size_byte": 750513392,
                            "dr_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "elapsed_time": 37,
                            "extra": {
                                "site_task": {
                                    "site_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                    "task_op": 2
                                }
                            },
                            "finish_time": 1742739497,
                            "is_done": true,
                            "is_stopped": false,
                            "is_success": true,
                            "main_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "readable_begin_time": "Sun Mar 23 15:17:40 2025",
                            "readable_finish_time": "Sun Mar 23 15:18:17 2025",
                            "snapshot_version": "GMT+01-2025.03.23-15.17.39",
                            "sync_size_byte": 750513392,
                            "total_size_byte": 750513392,
                            "update_time": 1742739497,
                            "version": 3
                        },
                        {
                            "begin_time": 1742739528,
                            "current_speed": 0,
                            "data_size_byte": 8210,
                            "dr_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "elapsed_time": 28,
                            "extra": {
                                "site_task": {
                                    "site_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                    "task_op": 2
                                }
                            },
                            "finish_time": 1742739556,
                            "is_done": true,
                            "is_stopped": false,
                            "is_success": true,
                            "main_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "readable_begin_time": "Sun Mar 23 15:18:48 2025",
                            "readable_finish_time": "Sun Mar 23 15:19:16 2025",
                            "snapshot_version": "GMT+01-2025.03.23-15.18.46",
                            "sync_size_byte": 8210,
                            "total_size_byte": 8210,
                            "update_time": 1742739556,
                            "version": 3
                        }
                    ],
                    "success_sync_count": 2,
                    "syncing_record": null,
                    "total_success_sync_size_byte": 750521602,
                    "total_success_sync_time_sec": 65
                },
                "testfailover_info": null,
                "topology": {
                    "links": [
                        {
                            "dr_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "main_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                        }
                    ],
                    "sites": [
                        {
                            "addr": "",
                            "hostname": "hostname",
                            "node_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "plans": [
                                {
                                    "additional": {
                                        "sync_policy": {
                                            "enabled": true,
                                            "is_app_aware": false,
                                            "is_send_encrypted": false,
                                            "is_sync_local_snapshots": false,
                                            "mode": 2,
                                            "next_trigger_time": 1742770800,
                                            "notify_time_in_min": 720,
                                            "readable_next_trigger_time": "Mon Mar 24 00:00:00 2025",
                                            "schedule": {
                                                "date_type": 0,
                                                "hour": 0,
                                                "last_work_hour": 0,
                                                "min": 0,
                                                "repeat_hour": 0,
                                                "repeat_min": 0,
                                                "week_name": "0,1,2,3,4,5,6"
                                            },
                                            "sync_window": {
                                                "enabled": false,
                                                "window": [
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215
                                                ]
                                            },
                                            "worm_lock_day": 7,
                                            "worm_lock_enable": false,
                                            "worm_lock_notify_time": 0
                                        }
                                    },
                                    "is_to_local": true,
                                    "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                    "remote_target_name": "api-1",
                                    "role": 1,
                                    "status": 1,
                                    "target_id": "api",
                                    "target_name": "api"
                                },
                            ],
                            "status": 1
                        },
                        {
                            "addr": "",
                            "hostname": "hostname2",
                            "node_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "plans": [
                                {
                                    "additional": {
                                        "sync_policy": {
                                            "enabled": true,
                                            "is_app_aware": false,
                                            "is_send_encrypted": true,
                                            "is_sync_local_snapshots": false,
                                            "mode": 2,
                                            "next_trigger_time": 1742770800,
                                            "notify_time_in_min": 720,
                                            "readable_next_trigger_time": "Mon Mar 24 00:00:00 2025",
                                            "schedule": {
                                                "date_type": 0,
                                                "hour": 0,
                                                "last_work_hour": 0,
                                                "min": 0,
                                                "repeat_hour": 0,
                                                "repeat_min": 0,
                                                "week_name": "0,1,2,3,4,5,6"
                                            },
                                            "sync_window": {
                                                "enabled": false,
                                                "window": [
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215,
                                                    16777215
                                                ]
                                            },
                                            "worm_lock_day": 7,
                                            "worm_lock_enable": false,
                                            "worm_lock_notify_time": 0
                                        }
                                    },
                                    "is_to_local": false,
                                    "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                    "remote_target_name": "api",
                                    "role": 2,
                                    "status": 1,
                                    "target_id": "api",
                                    "target_name": "api"
                                }
                            ],
                            "status": 1
                        }
                    ],
                    "target": {
                        "target_id": "api",
                        "target_type": 2
                    }
                }
            },
            "dr_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "is_to_local": true,
            "main_site": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "plan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "role": 1,
            "role_str": "mainsite",
            "solution_type": 1,
            "sync_mode": 2,
            "target_id": "api",
            "target_type": 2
        }]
    },
    "success": true
}
```
</details>



---


### `create_snapshot`
Create a snapshot for a share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Snapshot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_name_** `str`  
Name of the share to create a snapshot for.  
  
**_description_** `str`  
Description of the snapshot. Defaults to `""`.  
  
**_lock_** `bool`  
Whether to lock the snapshot. Defaults to `False`.  
  
**_immutable_** `bool`  
Whether to make the snapshot immutable. Defaults to `False`.  
  
**_immutable_days_** `int`  
Number of days to make the snapshot immutable for. Defaults to `7`.  
Must be greater than `0`. Mandatory if immutable is `True`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful, error message if not.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": "GMT+09-2023.09.12-00.33.20",
    "success": true
}
```
</details>



---


### `delete_snapshots`
Delete snapshots for a share.  
:::warning
 
 This action removes data from the file system. Use with caution.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Snapshot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_name_** `str`  
Name of the share to delete snapshots for.  
  
**_snapshots_** `list[str]`  
List of snapshots to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful, error message if not.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "success": true
}
```
</details>



---


### `set_snapshot_attr`
Set attributes for a snapshot.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Snapshot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_name_** `str`  
Name of the share to set attributes for  
  
**_snapshot_** `str`  
Name of the snapshot to set attributes for  
  
**_description_** `str`  
Description of the snapshot. Defaults to `None` (no change).  
  
**_lock_** `bool`  
Whether to lock the snapshot. Defaults to `None` (no change).  
  
**_immutable_** `bool`  
Whether to make the snapshot immutable. Defaults to `None` (no change).  
  
**_immutable_days_** `int`  
Number of days to make the snapshot immutable for. Defaults to `None` (no change).
Must be greater than `0`. Mandatory if immutable is `True`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful, error message if not.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json     
{
    "success": true
}
```
</details>



---


### `sync_replication`
Trigger a sync for a replication plan.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DR.Plan` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_plan_id_** `str`  
ID of the replication plan to sync.  
  
**_lock_snapshot_** `bool`  
Whether to lock the snapshot to prevent rotation. Defaults to `True`.  
  
**_description_** `str`  
Description of the snapshot. Defaults to `Snapshot taken by [Synology API]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "success": true
}
```
</details>



---


### `create_snapshot_lun`
Create a snapshot for a LUN.   
:::note
 
 At the moment, it does not support creating WORM snapshots.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.ISCSI.LUN` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_lun_id_** `str`  
ID of the LUN to create a snapshot for  
  
**_description_** `str`  
Description of the snapshot. Defaults to `Snapshot taken by [Synology API]`.  
  
**_lock_** `bool`  
Whether to lock the snapshot. Defaults to `True`.  
  
**_app_aware_** `bool`  
Whether to make the snapshot application aware. Defaults to `True`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "snapshot_id": 4,
        "snapshot_uuid": "31aa7808-9ffc-4689-bb70-262bb1665c9b"
    },
    "success": true
}
```
</details>



---


### `delete_snapshots_lun`
Delete snapshots for a LUN.  
:::warning
 
 This action removes data from the file system. Use with caution.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.ISCSI.LUN` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_snapshot_uuids_** `list[str]`  
List of UUIDs of the snapshots to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response if successful.   

If deletion fails, an error code is returned alonside the snapshot uuid:
```json
{
    "data": [
        {
            "5c9bf4a7-05ea-4cb8-b9e0-e0b0ca1186b0": 18990540
        }
    ],
    "success": true
}
```  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": [],
    "success": true
}
```
</details>



---


