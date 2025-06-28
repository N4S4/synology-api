---
sidebar_position: 11
title: ✅ DirectoryServer
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# DirectoryServer
## Overview
The directory server API.

Not all items within this class use the Active Directory API.  Some use the Synology Entry API which proxies
the request. Some are related to managing users in ways that are useful in the Directory Server context.  For
example, sending a user password reset email, or updating the user information. This api works slightly
differently than other similar APIs. There are multi-leveled calls where Synology makes requests on behalf of
the original request and relays information back. Additionally, the query-string api item is not used often in
this class as API is defined within the actual request.

The APIs in this class are tested working against the following scenarios:
- **Getters** :
    - Get Active Directory information
    - List objects within a Base DN on the Active Directory Server
    - Check if an AD object within your Directory Server
    - Get the status of a running task such as the Domain status update
- **Setters** :
    - Set the user's AD password
    - Update user information within the Directory Server
    - Update Synology's awareness of the current state of the Domain
- **Actions** :
    - Create an AD user
    - Add an AD user to an AD group
    - Create a new AD group
    - Send a password reset email to any Synology user
    - Delete a list of items from the Directory Server
    - Delete a single item from the Directory Server
    - Perform an entry request to complete a Deletion
## Methods
### `get_directory_info`
Gets directory info.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Information about your domain.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "data": {
        "domainBasicInfo": {
            "realm": "MY.DOMAIN.COM",
            "workgroup": "NETBIOSNAME"
        },
        "domainControllers": [
            {
            "cn": "AD",
            "dn": "CN=AD,OU=Domain Controllers,DC=MY,DC=DOMAIN,DC=COM",
            "dnshostname": "AD.MY.DOMAIN.COM",
            "roles": [
                "pdc",
                "rid",
                "schema",
                "naming",
                "infrastructure"
            ]
            }
        ]
        },
        "status": "running"
    },
    "success": true
}
```
</details>



---


### `list_directory_objects`
lists directory objects.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_basedn_** `str`  
The Base DN for the search. eg. `CN=Users,CN=MY,CN=DOMAIN,CN=COM" or CN=MY,CN=DOMAIN,CN=COM`  
  
**_offset_** `int`  
When searching large data, you may wish to start at a certain number, e.g. for 10 at a time one
would set the limit to 10 and the offset by multiples of 10 for each request.
Defaults to `0`  
  
**_limit_** `int`  
The numeric the number of maximum objects to return.
Defaults to `40`  
  
**_objectCategory_** `optional, list[str]`  
The categories of items to search.  e.g. `["organizationalUnit","container","builtinDomain"]` for a list of
base server containers, and `["person","group","organizationalUnit","computer"]` for a list of contained objects.
Defaults to `["person","group","organizationalUnit","computer","container","builtinDomain"]`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "data": [
        {
            "accountExpiryTime": 910692730085,
            "deletable": true,
            "description": "This is a description of a user person",
            "disabled": false,
            "displayName": "John Doe",
            "dn": "CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM",
            "locked": false,
            "mail": "jdoe@MY.EMAIL.COM",
            "movable": true,
            "name": "john",
            "objectCategory": "person",
            "passwordExpired": true,
            "physicalDeliveryOfficeName": "official office of officers",
            "primaryGroupToken": 0,
            "renamable": true,
            "sAMAccountName": "jdoe",
            "showInAdvancedViewOnly": false,
            "telephoneNumber": "123-444-5677"
        },
        ],
        "total": 99999
    },
    "success": true
}
```
</details>



---


### `create_new_user`
Create a new user.  
:::note
 
 The user can be created in AD, but not able to log on until the next synchronization occurs.  
 
:::

:::note
 
 Please note that synchronization with Synology is a separate step.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.User` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_logon_name_** `str`  
The desired username. E.g `jdoe`.  
  
**_email_** `str`  
The desired email.  
  
**_password_** `str`  
The plain-text password for the new user. E.g `Password123`.  
  
**_located_dn_** `str`  
The DN for the user. E.g `CN=Users,CN=MY,CN=DOMAIN,CN=COM`.  
  
**_description_** `str`  
A description for the user.  
  
**_account_is_disabled_** `str`  
Set to 'true' if the account should be disabled Defaults to `False`.  
  
**_cannot_change_password_** `str`  
Set to 'true' if the user cannot change the password Defaults to `False`.  
  
**_change_password_next_logon_** `str`  
Set to 'true' if the user must change password on next logon Defaults to `False`.  
  
**_cannot_change_password_** `str`  
Set to 'true' if the user cannot change the password Defaults to `False`.  
  
**_password_never_expire_** `str`  
Pwd Never Expire  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary. The data dictionary contains an 'error', or it contains a 'dn' and a 'name'.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    'data': {
        'dn': 'CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM',
        'name': 'NETBIOSNAME\ababab'
    },
    'success': true
}
```
</details>



---


### `reset_password`
Send a password reset email.  
This will trigger the password reset email from
Control Panel>Notification>Rules>System>Reset password for your account to be sent to the user.  
:::info
 
 In order to use this, Control Panel>User & Group>Advanced>"Allow non-administrator users to reset forgotten passwords via email" must be enabled.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Auth.ForgotPwd` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_username_** `str`  
The username to reset.  E.g. `My Group`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The return object can be checked for the "success" to be a true or false.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "msg": 3
    },
    "success": true
}
```
</details>



---


### `change_user_password`
Change the user's password.  
:::info
 
 This is a compound dual-level request where the synology API proxies your request to the Directory Server.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_user_dn_** `str`  
The user DN to be modified. eg. `CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM`  
  
**_password_** `str`  
The new password to be set. e.g. `Password123`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.User",
            "data": [
            {
                "code": 0,
                "msg": "update record successfully"
            }
            ],
            "method": "set",
            "success": true,
            "version": 2
        }
        ]
    },
    "success": true
}
```
</details>



---


### `create_new_group`
Create a new AD group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the group.  E.g. `My Group`  
  
**_located_dn_** `str`  
The DN to place the group in.  eg. `CN=Groups,DC=MY,DC=DOMAIN,DC=COM`  
  
**_email_** `str`  
The email address used to reference this group.
Defaults to `""`  
  
**_description_** `str`  
A description of the AD Group.
Defaults to `""`  
  
**_type_** `str`  
Example Options: `security`, `distribution`  
(definitions from https://docs.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups?view=o365-worldwide )
    - `distribution` (Distribution groups) are used for sending email
    notifications to a group of people.
    - `security` - Security groups are used for granting access to resources
    such as SharePoint sites.  
Defaults to `"security"`  
  
**_scope_** `str`  
Example Options : `local`, `global`, `universal`  
(Definitions from
https://www.netwrix.com/active_directory_group_management.html )
    - `local` (Domain Local Groups) should be used to manage permissions to
    resources because this group can be applied everywhere in the domain.
    A domain local group can include members of any type in the domain and
    members from trusted domains. For example, suppose you need access
    management for a collection of folders on one or more servers that
    contain information for managers. The group you create for that purpose
    should be a domain local group (ex. “DL_Managers_Modify”).
    - `global` (Global Groups) are used primarily to define collections of
    domain objects (users, other global groups and computers) based on
    business roles, which means that they mostly serve as role groups.
    Role-based groups of users (such as “HR” or “Marketing”) and role-based
    groups of computers (such as a “Marketing Workstations”) areusually
    global groups.
    - `universal` (Universal Groups) in Active Directory are useful in
    multi-domain forests. They enable you to define roles or manage
    resources that span more than one domain. Each universal group is
    stored in the domain of where it was created, but its group membership
    is stored in the Global Catalog and replicated forest-wide. Don’t use
    universal groups if you have only one domain.  
Defaults to `"global"`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A success object, and data object containing the new dn and the netbios name of the group.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    'data': {
        'dn': 'CN=My Group,CN=Groups,DC=MY,DC=DOMAIN,DC=COM',
        'name': 'NETBIOSNAME\My Group'
    },
    'success': true
}
```
</details>



---


### `add_user_to_group`
Adds a user as a member of a group.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_userDn_** `str`  
The fully qualified dn to add.  eg. `CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM`  
  
**_groupDn_** `str`  
the fully qualified dn of the group to which the user is to be added. e.g. `CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.Group.Member",
            "data": {
            "members": [
                "CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM"
            ]
            },
            "method": "add",
            "success": true,
            "version": 1
        }
        ]
    },
    "success": true
}
```
</details>



---


### `does_dn_exist`
Checks if a container exists. This can be used to verifiy the username or group name is unique.  
:::info
 
 This will not check the container, only if a similarly named container already exists.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_groupName_** `str`  
The user, or group's name. e.g.  `jdoe` or `My Cool Group`  
Fully Qualified Domain Name such as `CN=My Cool Group,CN=Groups,DC=MY,DC=DOMAIN,DC=COM` are not successful.  
Improper case such as `my cool group` instead of `My Cool Group` are successful  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
`True` if the group exists. `False` if the group does not exist  

</div>



---


### `modify_user_info`
Performs modification to user information within the Active Directory.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_user_dn_** `str`  
The user DN to be modified. eg. `CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM`  
  
**_firstName_** `str`  
The First name of the user. e.g. `John`  
  
**_lastName_** `str`  
The Last Name of the user. e.g. `Doe`  
  
**_displayName_** `str`  
The Display name of the user. e.g. `John Doe`  
  
**_description_** `str`  
The Descrition of the user. e.g. `The guy who just came in`  
  
**_initials_** `str`  
The Initials of the user.  e.g. `JD`  
  
**_physicalDeliveryOfficeName_** `str`  
The office location in the user's place of business  
  
**_telephoneNumber_** `str`  
The user's telephone number.  
  
**_web_** `str`  
The user's website or location on the web where information can be obtained.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server. The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": true,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.User",
            "error": {
            "code": 10104,
            "errors": [
                {
                "code": 10237,
                "msg": "ldb updaterecords: modify"
                }
            ]
            },
            "method": "set",
            "success": false,
            "version": 2
        }
        ]
    },
    "success": true
}
```
</details>



---


### `setEntryRequest`
Performs modification to an object within the Active Directory.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_modificationAPI_** `str`  
API to be used  
  
**_method_** `str`  
Method to be called  
  
**_nameOfObject_** `str`  
The user DN to be modified. eg. `"CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM"`  
  
**_jsonObject_** `str`  
The json Object to be added, eg, a user object where the  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": true,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.User",
            "error": {
            "code": 10104,
            "errors": [
                {
                "code": 10237,
                "msg": "ldb updaterecords: modify"
                }
            ]
            },
            "method": "set",
            "success": false,
            "version": 2
        }
        ]
    },
    "success": true
}
```
</details>



---


### `update_domain_records`
Updates the Synology users and groups database with information from Directory Server.  
This is a long-running and asynchronous task.  You are given back a task_id, and you can use that task_id to check the status with the get_task_status(task_id) method.  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.Domain` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The 'data' object contains the 'task_id' used to track with the getTaskStatus() method.  
The 'success' object will be true if the operation was successful. or false if failed.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```python
    updateResponse=directory.updateDomain()
    status = directory.getTaskStatus(updateResponse['data']['task_id'])
    while status['data']['status'] == 'updating':
        status=directory.getTaskStatus(updateResponse['data']['task_id'])
    ```
</details>



---


### `get_task_status`
Gets the current status of a task running on the Directory Domain object.  
This is used to ensure the task is completed.  For example, the primary utilization of this is when updating Synology's internal Domain user and group list.  
Until this method reports finish, the job is not completed, and it is not safe to operate under the assumption that users have been synchronized.  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.Domain` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
The task ID to be tracked for status.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The 'data' object contains the 'status' used to determine the current status. 'status' will be 'updating' or 'finish' if the job was started.
T
The 'success' object will be true if the operation was successful. or false if failed.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    'data': {
        'status': 'updating'
    },
    'success': true
}
```
</details>



---


### `deleteItems`
Deletes an array of DNs from AD.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ActiveDirectory.Directory` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dnList_** `list[str]`  
The fully qualified DN to be removed from the directory server.
eg. `["CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM","CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM"]`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.Polling",
            "data": {
            "data": [
                {
                "dn": "CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM",
                "status": {}
                }
            ],
            "finished": true,
            "total": 1
            },
            "method": "get",
            "success": true,
            "version": 1
        }
        ]
    },
    "success": true
}
```
</details>



---


### `delete_item`
Deletes a DN from AD.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dn_** `str`  
The fully qualified DN to be removed from the directory server.
eg. `CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM` or `CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.  
The first level is the success to the AD server.  The second Data level is the status of the actual request.  
Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
        {
            "api": "SYNO.ActiveDirectory.Polling",
            "data": {
            "data": [
                {
                "dn": "CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM",
                "status": {}
                }
            ],
            "finished": true,
            "total": 1
            },
            "method": "get",
            "success": true,
            "version": 1
        }
        ]
    },
    "success": true
}
```
</details>



---


### `entryRequest`
Some requests require an entry.  
Delete for example requires an entry.  If an entry is required, the task will not complete without an Entry Request.  
#### Internal API
<div class="padding-left--md">
`SYNO.Entry.Request` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
The ID of the task to be checked. This is provided when making a request.  
An example Task ID may look like this
`@administrators/Synoads_SYNO.ActiveDirectory.Directory_delete6145EA17C4F03DA9`  
  

</div>



---


