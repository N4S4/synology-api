---
sidebar_position: 9
title: ✅ CloudSync
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CloudSync
## Overview
Cloud Sync API implementation.

This API provides the functionality to get information related to the package settings and current connections and tasks.
It also provides functionalities to set most of the settings for tasks and package configuration, as well as manage the current syncing processes.

Due to the vast amount of public clouds available in the project, the API was not tested for every cloud scenario, so some params request may be missing in specific not tested clouds.

The tested clouds so far are:
- Google Drive
- OneDrive
- DropBox
- Amazon S3 (task creation)

### Supported methods

     - **Getters** :
        - Get package settings
        - Get connections
        - Get connections settings
        - Get connection information
        - Get connection auth information
        - Get connection logs
        - Get connection tasks
        - Get task filters
        - Get task synced remote directories
        - Get recently modified & currently syncing files
     - **Setters** :
        - Set package settings
        - Set relink behavior
        - Set connection settings
        - Set connection schedule settings
        - Set task settings
        - Set task filters
     - **Actions** :
        - Pause connection
        - Resume connection
        - Delete connection
        - Delete task
        - Validate task settings
        - Create S3 task
## Methods
### `get_pkg_config`
Retrieve package settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of package settings.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "admin_mode": "enable",
        "log_count": 20000,
        "repo_vol_path": "/volume2",
        "sync_mode": false,
        "volume_count": 2,
        "volume_list": [
            {
                "desc": "",
                "display": "Volume 1 (Available capacity:  715.84 GB )",
                "mount_point": "/volume1",
                "size_free": "768625090560",
                "size_total": "955458760704",
                "value": "1",
                "vol_desc": ""
            },
            {
                "desc": "",
                "display": "Volume 2 (Available capacity:  1841.73 GB )",
                "mount_point": "/volume2",
                "size_free": "1977547526144",
                "size_total": "3835577597952",
                "value": "2",
                "vol_desc": ""
            }
        ],
        "worker_count": 20
    },
    "success": true
}
```
</details>



---


### `get_connections`
Retrieve a list of current cloud connections.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_group_by_** `str`  
How to group the connection list, by user or cloud type. Defaults to `"group_by_user"`.  
Possible values:
- `group_by_user`: Group connection by owner user.
- `group_by_cloud_type`: Group connections by cloud provider.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of cloud connections.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "conn": [
            {
                "id": 3,
                "link_status": 1,
                "resource": "",
                "status": "uptodate",
                "task_display_name": "Dropbox",
                "task_name": "Dropbox",
                "type": "db",
                "type_id": 2,
                "unfinished_files": 0,
                "user_id": "dbid:xxxxxxxxxxxxxxxxxx",
                "user_name": "username"
            },
            {
                "id": 2,
                "link_status": 1,
                "resource": "",
                "status": "syncing",
                "task_display_name": "Microsoft OneDrive",
                "task_name": "Microsoft OneDrive",
                "type": "od_v1",
                "type_id": 22,
                "unfinished_files": 2,
                "user_id": "xxxxxx",
                "user_name": "username"
            }
        ],
        "is_admin_mode": true,
        "is_pause": false,
        "notification": null,
        "total": 2,
        "tray_status": "syncing"
    },
    "success": true
}
```
</details>



---


### `get_connection_settings`
Retrieve settings for a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the connection settings.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "client_type": "db",
        "isSSE": false,
        "is_enabled_schedule": false,
        "max_download_speed": 0,
        "max_upload_speed": 0,
        "part_size": 0,
        "pull_event_period": 60,
        "schedule_info": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "storage_class": "",
        "task_name": "Dropbox"
    },
    "success": true
}
```
</details>



---


### `get_connection_information`
Retrieve cloud information for a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing cloud information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "auth_version": "",
        "bucket_name": "",
        "container_name": "",
        "project_id": "",
        "public_url": "",
        "quota_total": 2147483648,
        "quota_used": 423330996,
        "region": "",
        "server_addr": "",
        "shared_drive_name": "",
        "storage_class": "",
        "type": "db",
        "type_id": 2,
        "user_name": "username"
    },
    "success": true
}
```
</details>



---


### `get_connection_auth`
Retrieve authentication information for a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the connection authentication details.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "access_key": "",
        "access_token": "xxxxxxxx",
        "auth_pass": "",
        "auth_scheme": 0,
        "auth_user": "",
        "bucket_id": "",
        "bucket_name": "",
        "client_id": "xxxxxxxx",
        "client_type": "db",
        "conn_id": 3,
        "container_name": "",
        "download_url": "",
        "openstack_api_key": "",
        "openstack_domain_id": "",
        "openstack_domain_name": "",
        "openstack_identity_service_url": "",
        "openstack_identity_service_version": "",
        "openstack_password": "",
        "openstack_proj_id": "",
        "openstack_region": "",
        "openstack_tenant_id": "",
        "openstack_tenant_name": "",
        "openstack_token": "",
        "public_url": "",
        "refresh_token": "xxxxxxxx",
        "resource": "",
        "root_folder_id": "",
        "root_folder_path": "/",
        "secret_key": "",
        "server_addr": "",
        "service_host": "",
        "unique_id": "dbid:xxxxxxxx",
        "user_name": "username"
    },
    "success": true
}
```
</details>



---


### `get_connection_logs`
Retrieve logs for a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  
**_keyword_** `str`  
A keyword to filter logs. Defaults to `''`.  
  
**_date_from_** `int`  
The starting date in epoch format. Defaults to `0`.  
  
**_date_to_** `int`  
The ending date in epoch format. Defaults to `0`.  
  
**_log_level_** `int`  
Log level filter. Defaults to `-1`.  
Possible values:
- `-1`: All
- `0`: Info
- `1`: Warning
- `2`: Error  
  
**_action_** `int`  
Action filter. Defaults to `-1`.  
Possible values:
- `-1`: All
- `0`: Delete Remote
- `1`: Download
- `2`: Upload
- `3`: Delete Local
- `4`: Rename Remote
- `8`: Merge
- `9`: Merge Deletion  
  
**_offset_** `int`  
Log offset for pagination. Defaults to `0`.  
  
**_limit_** `int`  
Number of logs to retrieve. Defaults to `200`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the connection logs.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "items": [
            {
                "action": 1,
                "error_code": -36,
                "file_name": "OCR Japanese extension.paper",
                "file_type": "file",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/OCR Japanese extension.paper",
                "session_id": 4,
                "time": 1724418508
            },
            {
                "action": 1,
                "error_code": -36,
                "file_name": "OCR Japanese extension.paper",
                "file_type": "file",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/OCR Japanese extension.paper",
                "session_id": 4,
                "time": 1724418119
            }
        ],
        "total": 2
    },
    "success": true
}
```
</details>



---


### `get_tasks`
Retrieve a list of tasks related to a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of tasks.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "sess": [
            {
                "cloud_type_str": "db",
                "conn_id": 3,
                "error": 0,
                "error_desc": "",
                "link_status": 1,
                "local_sync_path": "/test_share/WebDAV test/subfolder",
                "remote_folder_id": "id:xxxx",
                "remote_sync_path": "/docs",
                "sess_id": 4,
                "sync_direction": "ONLY_DOWNLOAD",
                "sync_status": "uptodate"
            }
        ],
        "total": 1
    },
    "success": true
}
```
</details>



---


### `get_task_filters`
Retrieve filter information for a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sess_id_** `int`  
The ID of the task, obtained from `get_tasks()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing task filter information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "filtered_extensions": [
            "wbmp",
            "webdoc",
            "x3f",
            "xbm"
        ],
        "filtered_max_upload_size": 1048576,
        "filtered_names": [
            "test"
        ],
        "filtered_paths": [
            "/subfolder_1"
        ],
        "user_defined_extensions": [
            "iso"
        ],
        "user_defined_names": [
            "test"
        ]
    },
    "success": true
}
```
</details>



---


### `get_task_cloud_folders`
Retrieve a list of children directories in the cloud for a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sess_id_** `int`  
The ID of the task, obtained from `get_tasks()`.  
  
**_remote_folder_id_** `str`  
The ID of the remote folder, obtained from `get_tasks()`.  
  
**_path_** `str`  
The folder path to retrieve the child directories from. Defaults to root `'/'`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of children directories.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "children": [
            {
                "exists_type": 1,
                "file_id": "",
                "path": "/subfolder_1",
                "text": "subfolder_1"
            },
            {
                "exists_type": 1,
                "file_id": "",
                "path": "/new folder",
                "text": "new folder"
            },
            {
                "exists_type": 3,
                "file_id": "id:xxxx",
                "path": "/test1",
                "text": "test1"
            },
            {
                "exists_type": 3,
                "file_id": "id:xxxx",
                "path": "/test2",
                "text": "test2"
            }
        ]
    },
    "success": true
}
```
</details>



---


### `get_recently_modified`
Retrieve the 5 latest modified files and the currently syncing items.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the recently modified files.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "history_items": [
            {
                "action": 1,
                "base_name": "test_file.paper",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/test_file.paper",
                "session_id": 4,
                "syncfolder_basename": "subfolder"
            },
            {
                "action": 1,
                "base_name": "perfect plan.paper",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/perfect plan.paper",
                "session_id": 4,
                "syncfolder_basename": "subfolder"
            },
            {
                "action": 1,
                "base_name": "Untitled.paper",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/Untitled.paper",
                "session_id": 4,
                "syncfolder_basename": "subfolder"
            },
            {
                "action": 1,
                "base_name": "translation hw.paper",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/translation hw.paper",
                "session_id": 4,
                "syncfolder_basename": "subfolder"
            },
            {
                "action": 1,
                "base_name": "The Tao of Harp.paper",
                "log_level": 2,
                "path": "/test_share/WebDAV test/subfolder/song ideas/The Tao of Harp.paper",
                "session_id": 4,
                "syncfolder_basename": "subfolder"
            }
        ],
        "is_admin_mode": true,
        "processing_items": [
            {
                "base_name": "1111111111111111111111125.jpg",
                "bit_rate": 2114,
                "current_size": 65535,
                "path": "/test_share/WebDAV test/subfolder/test1/asd/1111111111111111.jpg",
                "session_id": 3,
                "status": "uploading",
                "total_size": 295493,
                "user_name": "username"
            },
            {
                "base_name": "ans1.3.png",
                "bit_rate": 1047,
                "current_size": 358122,
                "path": "/test_share/WebDAV test/subfolder/test2/ans1.3.png",
                "session_id": 3,
                "status": "uploading",
                "total_size": 358122,
                "user_name": "username"
            }
        ],
        "server_merge_items": []
    },
    "success": true
}
```
</details>



---


### `set_pkg_config`
Set package configuration settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_pkg_volume_** `str`  
The volume path where the package data will be stored (e.g., `/volume1`).  
  
**_log_count_** `int`  
Maximum number of logs retained per connection. Defaults to `20000`, max is `100000`.  
  
**_workers_** `int`  
Number of concurrent uploads allowed. Defaults to `3`, max is `20`.  
  
**_admin_mode_** `bool`  
Whether all users' tasks are retrieved or not. Defaults to `True`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the configuration update.  

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


### `set_relink_behavior`
Set the relinking behavior for personal user accounts.  
:::warning
 
 Miss-configuration of this action may lead to data loss.  
 
:::

#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_delete_from_cloud_** `bool`  
Set to `False` for "locally deleted files will be re-fetched from the cloud".  
Set to `True` for "locally deleted files will also be removed from the cloud".  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the relink behavior update.  

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


### `set_connection_settings`
Set settings for a specific cloud connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  
**_task_name_** `str`  
The name of the cloud sync task.  
  
**_pull_event_period_** `int`  
Frequency (in seconds) to pull event updates. Defaults to `60`.  
  
**_max_upload_speed_** `int`  
Maximum upload speed in bytes. Defaults to `0` (unlimited).  
  
**_max_download_speed_** `int`  
Maximum download speed in bytes. Defaults to `0` (unlimited).  
  
**_storage_class_** `str`  
Cloud-specific storage class. Defaults to `''`.  
  
**_isSSE_** `bool`  
Enable Security Service Edge (SSE) for compatible cloud storage. Defaults to `False`.  
  
**_part_size_** `int`  
Part size for file uploads, in megabytes. Defaults to `128`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the updated connection settings.  

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


### `set_connection_schedule`
Set the schedule for a specific connection.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection, obtained from `get_connections()`.  
  
**_enable_** `bool`  
Whether the scheduling is enabled (`True`) or disabled (`False`).  
  
**_schedule_info_** `list[str]`  
A list of 7 strings where each string represents a day of the week, going from Sunday to Saturday.  
Each string is composed of 24 characters, where each character is either '1' (enabled) or '0' (disabled) for the respective hour of the day.  
The default value (if `schedule_info` is not provided) enables all days and hours.  
Example format for enabling the schedule at every time and day:
```python
# Keep this day order, Sunday to Saturday
days = [
    '111111111111111111111111', # sunday    - hours from 0 to 23
    '111111111111111111111111', # monday    - hours from 0 to 23
    '111111111111111111111111', # tuesday   - hours from 0 to 23
    '111111111111111111111111', # wednesday - hours from 0 to 23
    '111111111111111111111111', # thursday  - hours from 0 to 23
    '111111111111111111111111', # friday    - hours from 0 to 23
    '111111111111111111111111', # saturday  - hours from 0 to 23
]
set_connection_schedule(conn_id=3, enable=True, schedule_info=days)
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the schedule settings.  

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


### `set_task_settings`
Set the task settings for a specific session.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sess_id_** `int`  
The ID of the task, obtained from `get_tasks()`.  
  
**_sync_direction_** `str`  
The synchronization direction.  
Possible values:
- `ONLY_UPLOAD`: Upload local changes only.
- `BIDIRECTION`: Sync both ways (upload and download).
- `ONLY_DOWNLOAD`: Download remote changes only.  
  
**_consistency_check_** `bool`  
If True, enables advanced consistency check (requires more resources). Defaults to `True`.  
  
**_no_delete_on_cloud_** `bool`  
If `True`, prevents deletion of files in the remote folder when removed from the local directory. Defaults to `True`.  
  
**_convert_gd_** `bool`  
If `True`, converts Google Drive Online documents to Microsoft Office format. Defaults to `False`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task settings configuration.  

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


### `set_task_filters`
Set task filters for selective synchronization in a specific session.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sess_id_** `int`  
The ID of the session, obtained from `get_tasks()`.  
  
**_filtered_paths_** `list[str]`  
A list of paths (directories / subdirectories) to exclude from the synchronization process, e.g, `['/images', '/videos/movies']`. Defaults to `[]`.  
  
**_filtered_filenames_** `list[str]`  
A list of filenames to exclude from synchronization. Defaults to `[]`.  
  
**_filtered_extensions_** `list[str]`  
A list of file extensions to exclude from synchronization, e.g., `['mp3', 'iso', 'mkv']`. Defaults to `[]`.  
  
**_max_upload_size_** `int`  
The maximum file size for uploads, in bytes. Files larger than this size will be excluded from synchronization. Defaults to `0` (no size limit).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task filters configuration.  

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


### `connection_pause`
Pause one or all connections.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection to pause. If not specified or set to `-1`, all connections will be paused.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the pause action.  

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


### `connection_resume`
Resume one or all connections.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection to resume. If not specified or set to `-1`, all connections will be resumed.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the resume action.  

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


### `connection_remove`
Remove a specific connection and all associated tasks.  
The data will remain in both the local and remote directories.  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection to be removed, obtained from `get_connections()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the remove action.  

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


### `task_remove`
Remove a specific task.  
The data will remain in both the local and remote directories.  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection associated with the task, obtained from `get_connections()`.  
  
**_sess_id_** `int`  
The ID of the task to be removed, obtained from `get_tasks()`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the task removal.  

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


### `test_task_setting`
Test the task settings make sure they are valid.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection.  
  
**_local_path_** `str`  
The local path to sync.  
  
**_cloud_path_** `str`  
The cloud path to sync.  
  
**_sync_direction_** `str`  
The synchronization direction. Defaults to `'BIDIRECTION'`.  
  
**_storage_class_** `str`  
The storage class. Defaults to `'STANDARD'`.  
  
**_file_filter_** `list[str]`  
List of file extensions to filter. Defaults to `[]`.  
  
**_filter_max_upload_size_** `int`  
Maximum upload size for files. Defaults to `0`.  
  
**_filter_names_** `list[str]`  
List of file names to filter. Defaults to `[]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`tuple[bool, dict[str, object] | str]`  
A tuple containing a boolean indicating success, and a dictionary or string with the result.  

</div>



---


### `create_sync_task_s3`
Add a new synchronization task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.CloudSync` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_conn_id_** `int`  
The ID of the connection.  
  
**_local_path_** `str`  
The local path to sync.  
  
**_cloud_path_** `str`  
The cloud path to sync.  
  
**_sync_direction_** `str`  
The synchronization direction. Defaults to `'BIDIRECTION'`.  
  
**_storage_class_** `str`  
The storage class. Defaults to `'STANDARD'`.  
  
**_file_filter_** `list[str]`  
List of file extensions to filter. Defaults to `[]`.  
  
**_filter_max_upload_size_** `int`  
Maximum upload size for files. Defaults to `0`.  
  
**_filter_names_** `list[str]`  
List of file names to filter. Defaults to `[]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`tuple[bool, Any]`  
A tuple containing the result of the task creation.  

</div>



---


