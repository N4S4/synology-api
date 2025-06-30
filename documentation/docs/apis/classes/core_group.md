---
sidebar_position: 16
title: ✅ Group
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Group
## Overview
Core Group API implementation.

### Supported methods

    - **Getters** : 
        - Get all groups
        - Get group members
        - Get group shares permissions
        - Get group shares quota
        - Get group services speed limits

    - **Setters** :
        - Set group name/description
        - Set group share permissions
        - Set group share quotas
        - Set group service speed limit
    
    - **Actions** :
        - Create new group
        - Delete groups
        - Add users to a group
        - Remove users from a group
## Methods
### `get_groups`
Retrieve groups information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The offset of the groups to retrieve. Defaults to `0`.  
  
**_limit_** `int`  
The maximum number of groups to retrieve. Defaults to `-1` (all groups).  
  
**_name_only_** `bool`  
If `True`, returns only group names. If `False`, returns full group information. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the groups information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "groups": [
            {
                "description": "System default admin group",
                "gid": 101,
                "name": "administrators"
            },
            {
                "description": "System default group for Web services",
                "gid": 1023,
                "name": "http"
            },
            {
                "description": "A test group",
                "gid": 65536,
                "name": "Test"
            },
            {
                "description": "System default group",
                "gid": 100,
                "name": "users"
            }
        ],
        "offset": 0,
        "total": 4
    },
    "success": true
}
```
</details>



---


### `get_users`
Retrieve users members or not of a group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group.Member` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to list users from.  
  
**_in_group_** `bool`  
Defaults to `True`.  
If `True`, retrieves users who are members of the specified group.   
If `False`, retrieves users who are not members of the group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "offset": 0,
        "total": 3,
        "users": [
            {
                "description": "System default user",
                "name": "admin",
                "uid": 1024
            },
            {
                "description": "",
                "name": "customAdmin",
                "uid": 1026
            },
            {
                "description": "",
                "name": "test",
                "uid": 1032
            }
        ]
    },
    "success": true
}
```
</details>



---


### `get_speed_limits`
Retrieve bandwidth control settings for a given group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.BandwidthControl` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str `  
The group to retrieve settings for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>



---


### `get_quota`
Retrieve quota settings for a given group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Quota` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str `  
The group to retrieve quota settings for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] `  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "group_quota": [
            {
                "deduped": false,
                "quota_status": "v1",
                "shares": [
                    {
                        "description": "",
                        "name": "ActiveBackupforBusiness",
                        "quota": 1024
                    }
                ],
                "support_share_quota": true,
                "volume": "/volume3"
            }
        ]
    },
    "success": true
}
```
</details>



---


### `get_permissions`
Retrieve share permissions for a given group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to list permissions for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "shares": [
            {
                "is_aclmode": true,
                "is_custom": false,
                "is_deny": true,
                "is_mask": false,
                "is_readonly": false,
                "is_sync_share": false,
                "is_unite_permission": false,
                "is_writable": false,
                "name": "ActiveBackupforBusiness",
                "share_path": "/volume3/ActiveBackupforBusiness"
            }
        ],
        "total": 1
    },
    "success": true
}     
```
</details>



---


### `set_group_info`
Change group name and/or description.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to set information for.  
  
**_new_name_** `str`  
The new name of the group. Defaults to current value.  
  
**_new_description_** `str`  
The new description of the group. Defaults to current value.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] `  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "gid": 65536,
        "name": "Test_mod"
    },
    "success": true
}
```
</details>



---


### `set_share_quota`
Set group quota for a given share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Quota` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to set the quota for.  
  
**_share_quotas (list[dict[str, Any]])_** ``  
The quotas to set for the group.  
Example:
```python
[
    {
        "share": "web",
        "quota": 1024, # in MB
    },
    {
        "share": "photo",
        "quota": 5120, # in MB
    }
]
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] `  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {},
    "success": true
}
```
</details>



---


### `set_share_permissions`
Set group permissions for a given share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to set the permissions for.  
  
**_permissions_** `list[dict[str, object]]:`  
The permissions to set for the group.  
Example:
```python
[
    {
        "name": "web",
        "is_readonly": False,
        "is_writable": False,
        "is_deny": True
    },
    {
        "name": "ActiveBackupforBusiness",
        "is_readonly": False,
        "is_writable": True,
        "is_deny": False
    }
]
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

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


### `set_speed_limit`
Set speed limit for a given share.   
:::info
 
 Doesn't support **scheduled** speed limits, only on/off.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.BandwidthControl` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to set the speed limit for.  
  
**_upload_limit_** `int`  
The maximum upload speed in KB/s.  
  
**_download_limit_** `int`  
The maximum download speed in KB/s.  
  
**_protocol_** `str`  
The protocol to set the speed limit for.   
Possible values:
- FileStation
- WebDAV
- FTP
- NetworkBackup (Rsync)
- CloudStation (Synology Drive)  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "results": [
            true
        ]
    },
    "success": true
}
```
</details>



---


### `add_users`
Add users to a group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group.Member` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str `  
The group to add users to.  
  
**_users_** `list[str]`  
The users to add to the group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {},
    "success": true
}
```
</details>



---


### `remove_users`
Remove users from a group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group.Member` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str `  
The group to remove users from.  
  
**_users_** `list[str]`  
The users to remove from the group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {},
    "success": true
}
```
</details>



---


### `create`
Create group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Name to assign to the group.  
  
**_description_** `str`  
Description to assign to the group. Defaults to empty string.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] `  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "gid": 65541,
        "name": "new_group"
    },
    "success": true
}
```
</details>



---


### `delete`
Delete specified groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_groups_** `list[str]`  
The groups to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] `  
A dictionary containing the result of the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {},
    "success": true
}
```
</details>



---


