---
sidebar_position: 2
title: 🚧 ActiveBackupBusiness
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# ActiveBackupBusiness
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview

## Methods
### `list_vm_hypervisor`
This function returns a list of list of all configured hypervisors present in ABB.  
  



---


### `list_device_transfer_size`
This function returns a list of all devices and their respective transfer size for the given time frame. Default value is 24 hours.  
  



---


### `backup_task_list`
This function returns a list of all tasks. Can also retrieve versions corresponding to each task with the `load_versions` parameter.  
`filter` can be used to retrieve only specific information:  
filter: dict[str, any] = {}
    "task_id": int,
    "backup_type": int,
    "load_available": bool,
    "limit": int,
    "is_snapshot": bool,
    etc..  



---


### `backup_task_run`
This function will trigger a backup event for the given tasks. Even if only one task is specified, a list has to be passed as argument.  
  



---


### `backup_task_cancel`
This function will trigger a cancel backup event for the given tasks. Even if only one task is specified, a list has to be passed as argument.  
  



---


### `backup_task_remove`
This function will trigger a task deletion event for the given tasks. Even if only one task is specified, a list has to be passed as argument.  
  



---


### `backup_task_delete_versions`
This function will trigger a version deletion event for the given version. Even if only one version is specified, a list has to be passed as argument.  
  



---


### `list_logs`
This function returns a dictionary of the logs of all tasks.  
`filter` can be used to retrieve only specific information:  
filter: dict[str, any] = {}
    "task_id": int,
    "backup_type": int,
    "load_available": bool,
    "limit": int,
    "is_snapshot": bool,
    etc..  



---


### `list_logs_details`
This function returns a dictionary of the logs of a given task event. `result_id` can be retrieved from `list_logs()` function.  
  



---


### `list_storage`
This function returns a dictionary of the current storages being used by ABB.  
  



---


