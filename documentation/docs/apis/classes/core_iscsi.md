---
sidebar_position: 16
title: ✅ ISCSI
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
:::tip
 
This page contains documentation for the `ISCSI` class and its subclasses:  
-  [LUN](#lun)   
-  [Target](#target)   

 
:::
# ISCSI
## Overview
Abstract wrapper class for `SYNO.Core.ISCSI.*` requests.  
  
  
  
## LUN
## Overview
API wrapper for Synology iSCSI LUN management. This class targets the `SYNO.Core.ISCSI.LUN` WebAPI.  
  
Methods
-------
- **Getters** :
    - List LUNs
    - Get LUN details
- **Setters** :
    - Update LUN properties
- **Actions** :
    - Create / delete LUN
    - Clone LUN
    - Map / unmap targets  
  
## Methods
### `create`
Create a new iSCSI LUN.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
LUN name.  
  
**_type_** `{"FILE","THIN","ADV","BLUN","BLUN_THICK",...}`  
LUN type. Availability depends on filesystem and DSM version.  
  
**_location_** `str`  
Target location, typically a volume path (example: `"/volume1"`).  
  
**_size_** `int or str`  
LUN size in bytes.  
  
**_description_** `str`  
Optional textual description.  
  
**_extent_size_** `int or str`  
Extent size (may be ignored depending on type). [Untested]  
  
**_emulate_caw_** `bool`  
Enable SCSI COMPARE AND WRITE (CAW) support.
Allows atomic compare-and-write operations, typically used
by clustered filesystems or applications requiring
conditional block updates. When enabled, the LUN reports
support for the CAW command to the initiator.  
  
**_emulate_3pc_** `bool`  
Enable SCSI Third-Party Copy (XCOPY) support.
Allows block-level offloaded copy operations between
devices without transferring data through the initiator.
Used by hypervisors and storage-aware backup systems.  
  
**_emulate_tpu_** `bool`  
Enable SCSI UNMAP support (Thin Provisioning UNMAP).
Allows the initiator to explicitly deallocate logical
block ranges that are no longer in use (e.g. filesystem
discard/TRIM). Required for proper space reclamation
on thin-provisioned LUNs.  
  
**_emulate_tpws_** `bool`  
Enable SCSI WRITE SAME support with thin provisioning
semantics (Thin Provisioning WRITE SAME).
Allows large zero-write operations that may be interpreted
by the storage backend as deallocation hints. Often used
as an alternative or complement to UNMAP for space
reclamation.  
  
**_emulate_fua_write_** `bool`  
Enable handling of the SCSI Force Unit Access (FUA) bit
on write commands (DSM 7+).
When enabled, write commands marked with FUA are forced
to stable storage before completion is reported. Disabling
this may improve performance but can weaken durability
guarantees.  
  
**_emulate_sync_cache_** `bool`  
Enable support for the SCSI SYNCHRONIZE CACHE command
(DSM 7+).
When enabled, explicit cache flush requests from the
initiator are honored, ensuring that buffered writes are
committed to stable storage. Disabling this may increase
performance at the cost of reduced crash-consistency
guarantees.  
  
**_can_snapshot_** `bool`  
Enable snapshot capability for the LUN.
When set, the LUN is eligible for snapshot creation and
snapshot-based operations (e.g. cloning, replication).
Valid only for thin-provisioned LUN types.  
  
**_src_lun_dir_** `str`  
Source lun directory (likely) for creation based on snapshot import.  
  
**_src_lun_file_** `str`  
Source lun file (likely) for creation based on snapshot import.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    "data": {
        "lun_id": 0,
        "uuid": "2e349f91-e2a4-45dc-ba1c-774eb80d8b6f"
    },
    "success": true
}
```
</details>


---


### `delete`
Delete one or more LUNs.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_or_uuids_list_** `str | Sequence[str]`  
LUN UUID or list of LUN UUIDs  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `safe_delete`
Delete one or more LUNs, awaiting for complete deletion before returning.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_or_uuids_list_** `str | Sequence[str]`  
LUN UUID or list of LUN UUIDs  
  
**_min_request_delay_** `float`  
Minimum delay (in seconds) between two calls to LUN.list() when checking for complete deletion.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `list`
List available LUNs.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_types_** `List[str]`  
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
  
**_additional_info_** `List[str]`  
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
  
**_location_** `str`  
Filter by location.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response containing LUN list.  
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


### `get`
Get a specific LUN.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_** `str`  
LUN UUID.  
  
**_additional_info_** `List[str]`  
Additional LUN information to include in the response. Specify `[]` to get only basic information.
Defaults to `[ "is_action_locked", "is_mapped", "extent_size", "allocated_size", "status", "import_status", "sync_progress", "is_vhost_mapped", "is_bound", "whitelist", "flashcache_status", "family_config" ]`.
Possible values:
- `"is_action_locked"`
- `"is_mapped"`
- `"extent_size"`
- `"allocated_size"`
- `"status"`
- `"import_status"`
- `"sync_progress"`
- `"is_vhost_mapped"`
- `"is_bound"`
- `"whitelist"`
- `"flashcache_status"`
- `"family_config"`  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'data': {
        'import_done': 0,
        'import_errno': 18990593,
        'import_total': 0,
        'lun': {
            'allocated_size': 4294967296,
            'block_size': 512,
            'create_from': '',
            'description': '',
            'dev_attribs': [
                {'dev_attrib': 'emulate_3pc', 'enable': 0},
                {'dev_attrib': 'emulate_tpws', 'enable': 0},
                {'dev_attrib': 'emulate_caw', 'enable': 1},
                {'dev_attrib': 'emulate_tpu', 'enable': 0},
                {'dev_attrib': 'emulate_fua_write', 'enable': 0},
                {'dev_attrib': 'emulate_sync_cache', 'enable': 0},
                {'dev_attrib': 'can_snapshot', 'enable': 0}
            ],
            'dev_attribs_bitmap': 2,
            'dev_config': '',
            'dev_qos': {
                'dev_limit': 0,
                'dev_reservation': 0,
                'dev_weight': 0,
                'iops_enable': 0
            },
            'direct_io_pattern': 0,
            'extent_size': 0,
            'family_config': {
                'parent_lun_name': '',
                'parent_lun_uuid': '',
                'parent_snapshot_time': 0,
                'parent_snapshot_uuid': ''
            },
            'flashcache_id': -1,
            'flashcache_status': 'no_cache',
            'is_action_locked': False,
            'is_bound': False,
            'is_mapped': True,
            'is_vhost_mapped': False,
            'location': '/volume2',
            'lun_id': 1,
            'max_snapshot_count': 256,
            'name': 'xxxxx',
            'restored_time': 0,
            'size': 4294967296,
            'status': 'normal',
            'sync_done': 0,
            'sync_errno': 0,
            'sync_total': 0,
            'type': 259,
            'type_str': 'BLUN_THICK',
            'uuid': 'f699bc85-3be4-4eb0-9332-020b47143169',
            'vpd_unit_sn': 'f699bc85-3be4-4eb0-9332-020b47143169'
        },
        'sync_done': 0,
        'sync_errno': 0,
        'sync_total': 0,
        'whitelist': ['0.0.0.0', '0.0.0.0']
    },
    'success': True
}
```
</details>


---


### `set`
Update LUN properties.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_** `str`  
LUN UUID.  
  
**_new_name_** `str`  
Rename LUN.  
  
**_new_size_** `int or str`  
Resize LUN (may be unsupported in many cases).  
  
**_new_type_** `{"BLOCK","FILE","THIN","ADV","BLUN","BLUN_THICK"}`  
Change type (may be unsupported in many cases).  
  
**_new_location_** `str`  
Move LUN location (may be unsupported in many cases).  
  
**_emulate_caw_** `bool`  
Enable SCSI COMPARE AND WRITE (CAW) support.
Allows atomic compare-and-write operations, typically used
by clustered filesystems or applications requiring
conditional block updates. When enabled, the LUN reports
support for the CAW command to the initiator.  
  
**_emulate_3pc_** `bool`  
Enable SCSI Third-Party Copy (XCOPY) support.
Allows block-level offloaded copy operations between
devices without transferring data through the initiator.
Used by hypervisors and storage-aware backup systems.  
  
**_emulate_tpu_** `bool`  
Enable SCSI UNMAP support (Thin Provisioning UNMAP).
Allows the initiator to explicitly deallocate logical
block ranges that are no longer in use (e.g. filesystem
discard/TRIM). Required for proper space reclamation
on thin-provisioned LUNs.  
  
**_emulate_tpws_** `bool`  
Enable SCSI WRITE SAME support with thin provisioning
semantics (Thin Provisioning WRITE SAME).
Allows large zero-write operations that may be interpreted
by the storage backend as deallocation hints. Often used
as an alternative or complement to UNMAP for space
reclamation.  
  
**_emulate_fua_write_** `bool`  
Enable handling of the SCSI Force Unit Access (FUA) bit
on write commands (DSM 7+).
When enabled, write commands marked with FUA are forced
to stable storage before completion is reported. Disabling
this may improve performance but can weaken durability
guarantees.  
  
**_emulate_sync_cache_** `bool`  
Enable support for the SCSI SYNCHRONIZE CACHE command
(DSM 7+).
When enabled, explicit cache flush requests from the
initiator are honored, ensuring that buffered writes are
committed to stable storage. Disabling this may increase
performance at the cost of reduced crash-consistency
guarantees.  
  
**_can_snapshot_** `bool`  
Enable snapshot capability for the LUN.
When set, the LUN is eligible for snapshot creation and
snapshot-based operations (e.g. cloning, replication).
Valid only for thin-provisioned LUN types.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response (e.g. `{'success': True}`).  
</div>
  



---


### `clone`
Clone a LUN.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_src_lun_uuid_** `str`  
Source LUN UUID.  
  
**_dst_lun_name_** `str`  
Destination LUN name.  
  
**_clone_type_** `str`  
Clone type.  
  
**_dst_location_** `str`  
Destination location.  
  
**_dst_node_uuid_** `str`  
Destination node UUID (for remote scenarios).  
  
**_dst_address_** `str`  
Destination address (for remote scenarios).  
  
**_dst_port_** `int or str`  
Destination port (for remote scenarios).  
  
**_is_data_encrypted_** `bool`  
Whether data is encrypted in transit ?  
  
**_is_soft_feas_ignored_** `bool`  
Ignore "soft-feasibility"  
  
**_is_data_clone_** `bool`  
Unknown flag  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `stop_clone`
Stop an in-progress clone operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_src_lun_uuid_** `str`  
Source LUN UUID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `map_target`
Map a LUN to one or more targets.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_** `str`  
LUN UUID.  
  
**_target_ids_** `(int or str) or Sequence[int or str]`  
Target ID or IDs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `unmap_target`
Unmap a LUN from one or more targets.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.LUN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuid_** `str`  
LUN UUID.  
  
**_target_ids_** `(int or str) or Sequence[int or str]`  
Target ID or IDs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


## Target
## Overview
API wrapper for Synology iSCSI Target management. This class targets the `SYNO.Core.ISCSI.Target` WebAPI.  
  
Methods
-------
- **Getters** :
    - List targets
    - Get target details
- **Setters** :
    - Update target properties (name/iqn/session limits/checksums/auth)
- **Actions** :
    - Create / delete
    - Enable / disable
    - Map / unmap LUNs  
  
## Methods
### `create`
Create a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
Target name.  
  
**_iqn_** `str`  
ISCSI Qualified Name.  
  
**_auth_type_** `{0,1,2}`  
Authentication type:
- `0` -> none (default)
- `1` -> single CHAP
- `2` -> mutual CHAP  
  
**_max_sessions_** `int`  
Maximum sessions (use `0` for unlimited on some systems).  
  
**_user_** `str`  
CHAP username (client). Requires `auth_type` >= 1.  
  
**_password_** `str`  
CHAP password (client). Requires `auth_type` >= 1.  
  
**_mutual_user_** `str`  
Mutual CHAP username (server). Requires `auth_type` == 2.  
  
**_mutual_password_** `str`  
Mutual CHAP password (server). Requires `auth_type` == 2.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'data': {
        'target_id': 3
    },
    'success': True
}
```
</details>


---


### `delete`
Delete a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'success': True
}
```
</details>


---


### `list`
List available iSCSI targets.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_additional_info_** `List[str]`  
Additional information to include in the response. Specify `[]` to get only basic information.
Defaults to `["mapped_lun","acls","connected_sessions","status"]`  
  
**_lun_uuid_** `str`  
Filter targets mapped to LUN with provided uuid.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response containing iSCSI target list.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'data': {
        'targets': [
            {
                'auth_type': 0,
                'connected_sessions': [],
                'has_data_checksum': False,
                'has_header_checksum': False,
                'iqn': 'iqn.2025-01.com.synology:raspberry-pi',
                'is_default_target': False,
                'is_enabled': True,
                'mapped_luns': [
                    {
                        'lun_uuid': 'f699bc85-3be4-4eb0-9332-020b47143169',
                        'mapping_index': 1
                    }
                ],
                'mapping_index': -1,
                'max_recv_seg_bytes': 262144,
                'max_send_seg_bytes': 262144,
                'max_sessions': 1,
                'mutual_password': '',
                'mutual_user': '',
                'name': 'raspberry-pi',
                'network_portals': [
                    {'interface_name': 'all', 'ip': '', 'port': 3260}
                ],
                'password': '',
                'status': 'online',
                'target_id': 1,
                'user': ''
            },
            {
                'auth_type': 0,
                'connected_sessions': [],
                'has_data_checksum': False,
                'has_header_checksum': False,
                'iqn': 'iqn.2000-01.com.synology:xxx.default-target.xxxxxxx',
                'is_default_target': True,
                'is_enabled': True,
                'mapped_luns': [],
                'mapping_index': -1,
                'max_recv_seg_bytes': 262144,
                'max_send_seg_bytes': 262144,
                'max_sessions': 1,
                'mutual_password': '',
                'mutual_user': '',
                'name': 'Synology iSCSI Target',
                'network_portals': [
                    {'interface_name': 'all', 'ip': '', 'port': 3260}
                ],
                'password': '',
                'status': 'online',
                'target_id': 2,
                'user': ''
            }
        ]
    },
    'success': True
}
```
</details>


---


### `get`
Get information on iSCSI target with id `target_id`.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
**_additional_info_** `List[str]`  
Additional information to include in the response. Specify `[]` to get only basic information.
Defaults to `["mapped_lun","acls","connected_sessions","status"]`  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response containing iSCSI target info.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'data': {
        'target': {
            'auth_type': 0,
            'connected_sessions': [],
            'has_data_checksum': False,
            'has_header_checksum': False,
            'iqn': 'iqn.2000-01.com.synology:xxx.default-target.xxxxxxx',
            'is_default_target': True,
            'is_enabled': True,
            'mapped_luns': [],
            'mapping_index': 0,
            'max_recv_seg_bytes': 262144,
            'max_send_seg_bytes': 262144,
            'max_sessions': 1,
            'mutual_password': '',
            'mutual_user': '',
            'name': 'Synology iSCSI Target',
            'network_portals': [{'interface_name': 'all', 'ip': '', 'port': 3260}],
            'password': '',
            'status': 'online',
            'target_id': 2,
            'user': ''
        }
    },
    'success': True
}
```
</details>


---


### `set`
Update target properties.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
**_new_name_** `str`  
New target name.  
  
**_new_iqn_** `str`  
New target iqn.  
  
**_max_sessions_** `int`  
Maximum sessions (use `0` for unlimited on some systems).  
  
**_auth_type_** `{0,1,2}`  
New authentication type:
- `0` -> none
- `1` -> single CHAP
- `2` -> mutual CHAP  
  
**_user_** `str`  
CHAP username (client). Requires `auth_type` >= 1.  
  
**_password_** `str`  
CHAP password (client). Requires `auth_type` >= 1.  
  
**_mutual_user_** `str`  
Mutual CHAP username (server). Requires `auth_type` == 2.  
  
**_mutual_password_** `str`  
Mutual CHAP password (server). Requires `auth_type` == 2.  
  
**_has_header_checksum_** `bool`  
Enable CRC (cyclic redundancy check) header digest. Typically redundant in Ethernet + TCP settings.  
  
**_has_data_checksum_** `bool`  
Enable CRC (cyclic redundancy check) data digest. Typically redundant in Ethernet + TCP settings.  
  
**_max_recv_seg_bytes_** `int`  
Maximum receive segment bytes. Available values in Diskstation GUI are 4096, 8192, 65536, 262144 (default).  
  
**_max_send_seg_bytes_** `int`  
Maximum send segment bytes. Available values in Diskstation GUI are 4096, 8192, 65536, 262144 (default).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>

```json
{
    'success': True
}
```
</details>


---


### `enable`
Enable a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `disable`
Disable a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `map_lun`
Map one or more LUNs to a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
**_lun_uuid_or_uuids_list_** `str | Sequence[str]`  
LUN UUID or list of LUN UUIDs  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


### `unmap_lun`
Unmap one or more LUNs from a target.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Target`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_target_id_** `int | str`  
Integer id of iSCSI target.  
  
**_lun_uuid_or_uuids_list_** `str | Sequence[str]`  
LUN UUID or list of LUN UUIDs  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
API response.  
</div>
  



---


