---
sidebar_position: 25
title: 🚧 Share
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
:::tip
 
This page contains documentation for the `Share` class and its subclasses:  
-  [SharePermission](#sharepermission)   
-  [KeyManagerStore](#keymanagerstore)   
-  [KeyManagerAutoKey](#keymanagerautokey)   

 
:::
# Share
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Share API implementation.  
  
  
  
## Methods
### `validate_set`
Validate set of parameter for a new / modified shared folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Share name.  
  
**_vol_path_** `str`  
Volume path.  
  
**_desc_** `str`  
Share description. Defaults to `""`.  
  
**_enable_share_compress_** `bool`  
Enable share compress. Defaults to `False`.  
  
**_enable_share_cow_** `bool`  
Enable share cow. Defaults to `False`.  
  
**_enc_passwd_** `str`  
Encrypted password. Defaults to `""`.  
  
**_encryption_** `bool`  
Enable encryption. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "success": true,
}
```
</details>



---


### `list_folders`
List all folders informations.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_share_type_** `str`  
Share type. Defaults to `all`.  
  
**_additional_** `list[str]`  
Additional fields to retrieve. Defaults to `[]`.
All fields known are: `[
    "hidden","encryption","is_aclmode","unite_permission","is_support_acl","is_sync_share","is_force_readonly","force_readonly_reason",
    "recyclebin","is_share_moving","is_cluster_share","is_exfat_share","is_c2_share","is_cold_storage_share","is_missing_share",
    "is_offline_share","support_snapshot","share_quota","enable_share_compress","enable_share_cow","enable_share_tiering",
    "load_worm_attr","include_cold_storage_share","is_cold_storage_share","include_missing_share","is_missing_share",
    "include_offline_share","is_offline_share","include_worm_share"
]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
A dictionary containing the shared folders information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "shares": [
        {
            "desc": "",
            "is_usb_share": false,
            "name": "test_shared_folder",
            "uuid": "18585c8d-4d74-41a1-b561-21906a7f6f14",
            "vol_path": "/volume1"
        }
        ],
        "total": 1
    },
    "success": true
}
```
</details>



---


### `get_folder`
Get a folder by name.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Share name.  
  
**_additional_** `list`  
Additional fields to retrieve. Defaults to `[]`.
All fields known are: `["disable_list","disable_modify","disable_download","unite_permission","is_aclmode"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
A dictionary containing the shared folder information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "desc": "",
        "disable_download": false,
        "disable_list": false,
        "disable_modify": false,
        "is_aclmode": true,
        "is_usb_share": false,
        "name": "test_shared_folder",
        "unite_permission": false,
        "uuid": "18585c8d-4d74-41a1-b561-21906a7f6f14",
        "vol_path": "/volume1"
    },
    "success": true,
```
</details>



---


### `create_folder`
Create a new shared folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
Share name.  
  
**_vol_path_** `str`  
Volume path.  
  
**_desc_** `str`  
Share description. Defaults to `""`.  
  
**_hidden_** `bool`  
Hide share. Defaults to `False`.  
  
**_enable_recycle_bin_** `bool`  
Enable recycle bin. Defaults to `True`.  
  
**_recycle_bin_admin_only_** `bool`  
Recycle bin admin only. Defaults to `True`.  
  
**_hide_unreadable_** `bool`  
Hide unreadable. Defaults to `False`.  
  
**_enable_share_cow_** `bool`  
Enable share cow. Defaults to `False`.  
  
**_enable_share_compress_** `bool`  
Enable share compress. Defaults to `False`.  
  
**_share_quota_** `int`  
Share quota. Defaults to `0`.  
  
**_name_org_** `str`  
Defaults to `""`.  
  
**_encryption_** `bool`  
Enable encryption. Defaults to `False`.  
  
**_enc_passwd_** `str`  
Encrypted password. Defaults to `""`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Name of the created shared folder.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "name": "test_shared_folder"
    },
    "success": true,
```
</details>



---


### `delete_folders`
Delete folder(s) by name(s).  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `List[str]`  
Share names.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

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


### `clone`
Clone existing shared folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
New shared folder name.  
  
**_name_org_** `str`  
Original shared folder name.  
  
**_vol_path_** `str`  
Volume path.  
  
**_desc_** `str`  
Shared folder description. Defaults to `""`.  
  
**_hidden_** `bool`  
Hide shared folder. Defaults to `False`.  
  
**_enable_recycle_bin_** `bool`  
Enable recycle bin. Defaults to `True`.  
  
**_recycle_bin_admin_only_** `bool`  
Recycle bin admin only. Defaults to `True`.  
  
**_hide_unreadable_** `bool`  
Hide unreadable. Defaults to `False`.  
  
**_enable_share_cow_** `bool`  
Enable share cow. Defaults to `False`.  
  
**_enable_share_compress_** `bool`  
Enable share compress. Defaults to `False`.  
  
**_share_quota_** `int`  
Share quota. Defaults to `0`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Name of the created shared folder.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "name": "test_shared_folder"
    },
    "success": true,
```
</details>



---


### `decrypt_folder`
Decrypt a given share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Crypto` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The share name to decrypt.  
  
**_password_** `str`  
The password to use for decrypting the share.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

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


### `encrypt_folder`
Encrypt a given share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Crypto` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The share name to encrypt.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

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


## SharePermission
## Overview
Core Share Permission API implementation.  
  
  
  
## Methods
### `get_folder_permission_by_name`
Retrieve share permissions for a given folder filtered by permission name (sub string).  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The folder name to list permissions for.  
  
**_permission_substr_** `str`  
The substring to search for in the permissions.  
  
**_offset_** `int`  
The offset to start at. Defaults to `0`.  
  
**_limit_** `int`  
The maximum number of results to return. Defaults to `50`.  
  
**_is_unite_permission_** `bool`  
Whether to return unified permissions. Defaults to `False`.  
  
**_with_inherit_** `bool`  
Whether to include inherited permissions. Defaults to `False`.  
  
**_user_group_type_** `str`  
The type of user group to list permissions for. Defaults to `"local_user"`.
All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of permission(s) on the folder.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "items": [
            {
                "inherit": "-",
                "is_admin": false,
                "is_custom": false,
                "is_deny": false,
                "is_readonly": false,
                "is_writable": false,
                "name": "guest"
            }
        ],
        "total": 1
    },
    "success": true
}
```
</details>



---


### `get_folder_permissions`
Retrieve share permissions for a given folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The folder name to list permissions for.  
  
**_offset_** `int`  
The offset to start at. Defaults to `0`.  
  
**_limit_** `int`  
The maximum number of results to return. Defaults to `50`.  
  
**_is_unite_permission_** `bool`  
Whether to return unified permissions. Defaults to `False`.  
  
**_with_inherit_** `bool`  
Whether to include inherited permissions. Defaults to `False`.  
  
**_user_group_type_** `str`  
The type of user group to list permissions for. Defaults to `"local_user"`.
All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
All permissions on the folder.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "items": [
            {
                "inherit": "rw",
                "is_admin": true,
                "is_custom": false,
                "is_deny": true,
                "is_readonly": false,
                "is_writable": false,
                "name": "admin"
            },
            {
                "inherit": "-",
                "is_admin": false,
                "is_custom": false,
                "is_deny": false,
                "is_readonly": false,
                "is_writable": false,
                "name": "guest"
            },
            {
                "inherit": "rw",
                "is_admin": true,
                "is_custom": false,
                "is_deny": false,
                "is_readonly": false,
                "is_writable": true,
                "name": "test_api"
            },
            {
                "inherit": "-",
                "is_admin": false,
                "is_custom": false,
                "is_deny": false,
                "is_readonly": false,
                "is_writable": false,
                "name": "test_test"
            }
        ],
        "total": 5
    },
    "success": true
}
```
</details>



---


### `set_folder_permissions`
Set folder permissions for a given folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The folder name to set permissions for.  
  
**_user_group_type_** `str`  
The type of user group to set permissions for.
All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.  
  
**_permissions_** `dict`  
The permissions to set for the folder.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

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


### `get_local_group_permissions`
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
`dict`  
Permissions of a group on Shared folders.  

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


### `set_local_group_permissions`
Set group permissions for a given share.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.Permission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_** `str`  
The group to set the permissions for.  
  
**_permissions_** `list[dict[str, Any]]`  
The permissions to set for the group.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Success.  

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


## KeyManagerStore
## Overview
Core Share KeyManager Store API implementation.  
  
  
  
## Methods
### `init`
Initialize KeyManagerStore API.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.KeyManager.Store` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
Not implemented yet.  

</div>



---


### `verify`
Not implemented yet.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.KeyManager.Store` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
Not implemented yet.  

</div>



---


### `explore`
Explore KeyManagerStore API.  
Get list of existing stores.  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.KeyManager.Store` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of stores existing on the NAS.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "stores": []
    },
    "success": true
}
```
</details>



---


## KeyManagerAutoKey
## Overview
Core Share KeyManager AutoKey API implementation.  
  
  
  
## Methods
### `list`
List KeyManagerStore API.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share.KeyManager.AutoKey` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of keys in the manager.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "keys": []
    },
    "success": true
}
```
</details>



---


