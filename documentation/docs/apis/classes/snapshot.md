---
sidebar_position: 27
title: ✅ Snapshot
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Snapshot
## Overview
Class for interacting with Snapshot APIs.

### Supported methods

    - **Getters** : 
        - Get all snapshots

    - **Setters** :
        - Set snapshot attributes
    
    - **Actions** :
        - Create snapshot
        - Delete snapshot

This class implements APIs to manage snapshots.
There is no documentation for these APIs, so the implementation is based on network inspection.

Examples
--------
List snapshots for a share:
```python
from synology_api import snapshot
ss = snapshot.Snapshot('IP', 'PORT', 'USER', 'PASSWORD')
resp = ss.list_snapshots('share_name')
print(resp)
```

Create a snapshot for a share:
```python
resp = ss.create_snapshot('share_name')
print(resp)
```

Delete snapshots for a share:
```python
resp = ss.delete_snapshots('share_name', ['snapshot_name'])
print(resp)
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
Name of the share to list snapshots for  
  
**_attribute_filter_** `list[str]`  
List of attributes filter to apply. Defaults to `[]` (no filter).  
Each attribute filter is a string in the format of `"attr==value"` or `"attr=value"` and optionally prefixed with `!` to negate the filter.  
The following are examples of valid attribute filters:
    - `["!hide==true", "desc==abc"]` -> hide is not true and desc is exactly abc
    - `["desc=abc"]` -> desc has abc in it  
  
**_additional_attribute_** `list[str]`  
List of snapshot attributes whose values are included in the response.
Defaults to `[]` (only time is returned).  
Note that not all attributes are available via API. The following are confirmed to work:
    - desc
    - lock
    - worm_lock
    - schedule_snapshot  
  
**_offset_** `int`  
Offset to start listing from. Defaults to `0`.  
  
**_limit_** `int`  
Number of snapshots to return. Defaults to `-1` (all).  
  

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
API response if successful, error message if not  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json:
{
    "data": "GMT+09-2023.09.12-00.33.20",
    "success": true
}
```
</details>



---


### `delete_snapshots`
Delete snapshots for a share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Snapshot` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_name_** `str`  
Name of the share to delete snapshots for  
  
**_snapshots_** `list[str]`  
List of snapshots to delete  
  

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
API response if successful, error message if not  

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


