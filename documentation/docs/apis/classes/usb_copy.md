---
sidebar_position: 32
title: ✅ USBCopy
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# USBCopy
## Overview
USB Copy Implementation.

### Supported methods

    - **Getters** : 
        - Get package settings
        - Get package logs
        - Get task settings
        
    - **Actions** :
        - Enable / Disable task
## Methods
### `get_package_settings`
Retrieve package settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.USBCopy` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Parsed JSON into `dict`  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```python
{
    "data" : {
        "beep_on_task_start_end" : True,
        "log_rotate_count" : 100000,
        "repo_volume_path" : "/volume2"
    },
    "success" : True
}
```
</details>



---


### `get_package_logs`
Retrieve package logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.USBCopy` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Defaults to `0`.  
  
**_limit_** `int`  
Defaults to `200`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Parsed response JSON into `dict`  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```python
{
    "data" : {
        "count" : 1,
        "log_list" : [
            {
                "description_id" : 101,
                "description_parameter" : "["asdf"]",
                "error" : 0,
                "log_type" : 1,
                "task_id" : 2,
                "timestamp" : 1738341351
            },
        ]
    },
    "success" : True
}
```
</details>



---


### `get_task_settings`
Retrieve task settings  
  
#### Internal API
<div class="padding-left--md">
`SYNO.USBCopy` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
Task ID to retrieve info for  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Parsed response JSON into `dict`  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```python
{
    "data" : {
        "task" : {
            "conflict_policy" : "rename",
            "copy_file_path" : "",
            "copy_strategy" : "versioning",
            "default_device_port" : "NA",
            "destination_path" : "[USB]",
            "eject_when_task_done" : True,
            "enable_rotation" : False,
            "error_code" : 0,
            "id" : 2,
            "is_default_task" : False,
            "is_ds_mounted" : False,
            "is_task_runnable" : False,
            "is_usb_mounted" : False,
            "latest_finish_time" : 1738341351,
            "max_version_count" : 256,
            "name" : "asdf",
            "next_run_time" : "N/A",
            "not_keep_dir_structure" : False,
            "remove_src_file" : False,
            "rename_photo_video" : False,
            "rotation_policy" : "oldest_version",
            "run_when_plug_in" : False,
            "schedule_id" : 13,
            "smart_create_date_dir" : False,
            "source_path" : "/music",
            "status" : "unmounted",
            "type" : "export_general"
        }
    },
    "success" : True
}
```
</details>



---


### `toggle_task`
Enable or disable USB Copy task  
  
#### Internal API
<div class="padding-left--md">
`SYNO.USBCopy` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `int`  
Task ID to apply the setting to.  
  
**_enable_** `bool`  
Whether to enable (`True`) or disable (`False`) USB Copy. Defaults to `True`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Parsed response JSON into `dict`  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```python
{
    "success": True
}
```
</details>



---


