---
sidebar_position: 33
title: ✅ User
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# User
## Overview
Core User API implementation.

Supported actions:
    - **Getters** : 
        - Get all users
        - Password policies
        - Password expiry

    - **Setters** :
        - Set user password policy
    
    - **Actions** :
        - Create new user
        - Modify user
        - Delete user
        - User join/leave group
## Methods
### `get_users`
Retrieve groups information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The offset of the groups to retrieve. Defaults to `0`.  
  
**_limit_** `int`  
The maximum number of groups to retrieve. Defaults to `-1` .  
  
**_sort_by_** `str`  
Sort by a specific field. Defaults to `"name"`.  
  
**_sort_direction_** `str`  
The sort direction. Defaults to `"ASC"` else `"DESC"`.  
  
**_additional_** `list[str]`  
Additional fields to retrieve. Defaults to `[]`.  
All fields known are: `["description","email","expired","cannot_chg_passwd","passwd_never_expire","password_last_change", "groups", "2fa_status"]`.  
  

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
        "offset": 0,
        "total": 5,
        "users": [
        {
            "description": "System default user",
            "email": "",
            "expired": "now",
            "name": "admin",
            "passwd_never_expire": true
        },
        {
            "description": "Guest",
            "email": "",
            "expired": "now",
            "name": "guest",
            "passwd_never_expire": true
        },
        {
            "description": "",
            "email": "",
            "expired": "normal",
            "name": "test_api",
            "passwd_never_expire": true
        },
        {
            "description": "test description",
            "email": "testemail@test.com",
            "expired": "normal",
            "name": "test_user",
            "passwd_never_expire": true
        }
        ]
    },
    "success": true
}
```
</details>



---


### `get_user`
Retrieve a user information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the user.  
  
**_additional_** `list[str]`  
Additional fields to retrieve. Defaults to `[]`.  
All fields known are: `["description","email","expired","cannot_chg_passwd","passwd_never_expire","password_last_change","is_password_pending"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the user information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User",
    "data": {
        "users": [
            {
                "cannot_chg_passwd": false,
                "description": "",
                "email": "",
                "expired": "normal",
                "is_password_pending": false,
                "name": "test_api",
                "passwd_never_expire": true,
                "password_last_change": 19789,
                "uid": 1027
            }
        ]
    },
    "method": "get",
    "success": true,
    "version": 1
}
```
</details>



---


### `create_user`
Create a new user.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the user.  
  
**_password_** `str`  
The password of the user.  
  
**_description_** `str`  
The description of the user. Defaults to `""`.  
  
**_email_** `str`  
The email of the user. Defaults to `""`.  
  
**_expire_** `str`  
The expiration date of the user. Defaults to `"never"`.  
  
**_cannot_chg_passwd_** `bool`  
Whether the password can be changed. Defaults to `False`.  
  
**_passwd_never_expire_** `bool`  
Whether the password should never expire. Defaults to `True`.  
  
**_notify_by_email_** `bool`  
Whether to notify by email. Defaults to `False`.  
  
**_send_password_** `bool`  
Whether to send the password. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the user information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{ 
    "data":
    {
        "name":"toto",
        "uid": 1030
    },
    "success": true
}
```
</details>



---


### `modify_user`
Modify a user.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the actual user.  
  
**_new_name_** `str`  
The new name of the user.  
  
**_password_** `str`  
The password of the user. Defaults to `""`.  
  
**_description_** `str`  
The description of the user. Defaults to `""`.  
  
**_email_** `str`  
The email of the user. Defaults to `""`.  
  
**_expire_** `str`  
The expiration date of the user. Defaults to `"never"`.  
  
**_cannot_chg_passwd_** `bool`  
Whether the password can be changed. Defaults to `False`.  
  
**_passwd_never_expire_** `bool`  
Whether the password should never expire. Defaults to `True`.  
  
**_notify_by_email_** `bool`  
Whether to notify by email. Defaults to `False`.  
  
**_send_password_** `bool`  
Whether to send the password. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the user information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data":{
        "name": "test_user2",
        "password_last_change": 20106,
        "uid": 1028
    },
    "success": true
}
```
</details>



---


### `delete_user`
Delete a user.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the user to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the user information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "name": "toto",
        "uid": 1030
    },
    "success": true
}
```
</details>



---


### `affect_groups`
Affect or disaffect groups to a user.  
:::tip
 
 This request is asynchronous and will return a task id to check the status of the join task. Use `affect_groups_status` func to check the status of the task.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the user.  
  
**_join_groups_** `list[str]`  
The names of the groups to join.  
  
**_leave_groups_** `list[str]`  
The names of the groups to leave.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the task id to check the status of the join task. Use `affect_groups_status` func to check the status of the task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User.Group",
    "data": {
        "task_id": "@administrators/groupbatch1737238746C6723E33"
    },
    "method": "join",
    "success": true,
    "version": 1
}
```
</details>



---


### `affect_groups_status`
Get the status of a join task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
The task id of the join task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the status of the join task.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "auto_remove": false,
        "data": {
            "name": "test_user2",
            "pid": 18126,
            "progress": 1,
            "total": 1,
            "uid": 1028
        },
        "finish": false,
        "info": {
            "api": "SYNO.Core.User.Group",
            "group": "admin",
            "method": "join",
            "prefix": "groupbatch",
            "version": 1
        },
        "success": true
    },
    "success": true
}
```
</details>



---


### `get_password_policy`
Get the password policy.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.PasswordPolicy` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the password policy information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User.PasswordPolicy",
    "data": {
        "enable_reset_passwd_by_email": false,
        "password_must_change": false,
        "strong_password": {
            "exclude_username": true,
            "history_num": 0,
            "included_numeric_char": true,
            "included_special_char": false,
            "min_length": 8,
            "min_length_enable": true,
            "mixed_case": true
        }
    },
    "method": "get",
    "success": true,
    "version": 1
}
```
</details>



---


### `set_password_policy`
Set the password policy.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.PasswordPolicy` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_reset_passwd_by_email_** `bool, optional `  
Defaults to `False`.  
  
**_password_must_change_** `bool, optional `  
Defaults to `False`.  
  
**_exclude_username_** `bool, optional `  
Defaults to `True`.  
  
**_included_numeric_char_** `bool, optional `  
Defaults to `True`.  
  
**_included_special_char_** `bool, optional `  
Defaults to `False`.  
  
**_min_length_** `int, optional `  
Defaults to `8`.  
  
**_min_length_enable_** `bool, optional `  
Defaults to `True`.  
  
**_mixed_case_** `bool, optional `  
Defaults to `True`.  
  
**_exclude_common_password_** `bool, optional `  
Defaults to `False`.  
  
**_exclude_history_** `bool, optional `  
Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary indicating the success of the operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
        "api": "SYNO.Core.User.PasswordPolicy",
        "data": {},
        "method": "set",
        "success": true,
        "version": 1
    }
```
</details>



---


### `get_password_expiry`
Get the password expiry.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.PasswordExpiry` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the password expiry information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User.PasswordExpiry",
    "data": {
        "allow_reset_after_expired": true,
        "enable_login_prompt": false,
        "enable_mail_notification": false,
        "mail_notification_days": "",
        "min_age_enable": false,
        "password_expire_enable": false
    },
    "method": "get",
    "success": true,
    "version": 1
}
```
</details>



---


### `set_password_expiry`
Set the password expiry.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.PasswordExpiry` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_password_expire_enable_** `bool`  
Enable password expiry. Defaults to `False`.  
  
**_max_age_** `int`  
Maximum time before password expiry. Defaults to `30`.  
  
**_min_age_enable_** `bool`  
Enable minimum time before password expiry. Defaults to `False`.  
  
**_min_age_** `int`  
Minimum time before password expiry. Defaults to `1`.  
  
**_enable_login_prompt_** `bool`  
Enable login prompt. Defaults to `False`.  
  
**_login_prompt_days_** `int`  
Days before login prompt. Defaults to `1`.  
  
**_allow_reset_after_expired_** `bool`  
Allow reset after password expiry. Defaults to `True`.  
  
**_enable_mail_notification_** `bool`  
Enable mail notification. Defaults to `False`.  
  
**_never_expired_list_** `list[str]`  
List of users that should never expire.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary indicating the success of the operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User.PasswordExpiry",
    "method": "set",
    "success": true,
    "version": 1
}
```
</details>



---


### `password_confirm`
Issues a passowrd/session comparison to ensure the given password matches the auth of the current session.  
:::note
 
 This is needed by some APIs as a confirmation method, for example, when creating/modifying a scheduled task with root permissions, seldom needed by end users.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.PasswordConfirm` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_password_** `str`  
The password with which the session was initiated.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing a `SynoConfirmPWToken`, or an error message.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "SynoConfirmPWToken": "xxxxx"
    },
    "success": true
}
```
</details>



---


### `get_username_policy`
Get the username policy (List of username that are not usable).  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.UsernamePolicy` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the username policy information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "api": "SYNO.Core.User.UsernamePolicy",
    "data": ["root", "rootuser", "rootusr", "admin", "administrator", "adm", "adminuser", "adminusr", "user",…],
    "method": "get",
    "success": true,
    "version": 1
}
```
</details>



---


