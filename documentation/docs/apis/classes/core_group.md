---
sidebar_position: 16
title: ✅ Group
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Group
## Overview
Core Group API implementation for Synology NAS.  
  
This class provides methods to manage groups, including:
- Retrieving group information, members, permissions, quotas, and speed limits.
- Modifying group name, description, share permissions, quotas, and speed limits.
- Creating and deleting groups.
- Adding and removing users from groups.

### Supported methods

    - **Getters** : 
        - Retrieve groups information.
        - Retrieve users who are members or not members of a group.
        - Retrieve bandwidth control settings for a group.
        - Retrieve quota settings for a group.
        - Retrieve share permissions for a group.
    - **Setters** :
        - Change group name and/or description.
        - Set group quota for a given share.
        - Set group permissions for a given share.
        - Set speed limit for a given share.
        - Add users to a group.
        - Remove users from a group.
        - Create a new group.
        - Delete specified groups.  
  
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
The offset of the groups to retrieve. Defaults to 0.  
  
**_limit_** `int`  
The maximum number of groups to retrieve. Defaults to -1 (all groups).  
  
**_name_only_** `bool`  
If True, returns only group names. If False, returns full group information. Defaults to False.  
  

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
Retrieve users who are members or not members of a group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group.Member` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to list users from.  
  
**_in_group_** `bool`  
If True, retrieves users who are members of the specified group.
If False, retrieves users who are not members of the group. Defaults to True.  
  

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
**_group_** `str`  
The group to retrieve settings for.  
  

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
        "bandwidths": [
            {
                "download_limit_1": 0,
                "download_limit_2": 0,
                "name": "group_name",
                "owner_type": "local_group",
                "policy": "notexist",
                "protocol": "FTP",
                "protocol_ui": "FTP",
                "schedule_plan": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "upload_limit_1": 0,
                "upload_limit_2": 0
            },
        ]
    },
    "success": true
}
```
</details>



---


### `get_quota`
Retrieve quota settings for a given group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Quota` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to retrieve quota settings for.  
  

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
`dict[str, object]`  
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
  
**_share_quotas_** `list of dict`  
The quotas to set for the group.  
  

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
  
**_permissions_** `list of dict`  
The permissions to set for the group.  
  

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
The protocol to set the speed limit for. Possible values:
FileStation, WebDAV, FTP, NetworkBackup (Rsync), CloudStation (Synology Drive).  
  

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
**_group_** `str`  
The group to add users to.  
  
**_users_** `list of str`  
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
**_group_** `str`  
The group to remove users from.  
  
**_users_** `list of str`  
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
Create a new group.  
  
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
`dict[str, object]`  
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
**_groups_** `list of str`  
The groups to delete.  
  

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


