---
sidebar_position: 13
title: 🚧 DownloadStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# DownloadStation
:::warning
 
This API is not documented yet.
 
:::
## Overview
Core Download Station API implementation for Synology NAS.

This class provides methods to manage downloads, tasks, RSS feeds, and BT searches.

Parameters
----------
ip_address : str
    IP address or hostname of the Synology NAS.
port : str
    Port number to connect to.
username : str
    Username for authentication.
password : str
    Password for authentication.
secure : bool, optional
    Use HTTPS if True, HTTP if False (default is False).
cert_verify : bool, optional
    Verify SSL certificates (default is False).
dsm_version : int, optional
    DSM version (default is 7).
debug : bool, optional
    Enable debug output (default is True).
otp_code : Optional[str], optional
    One-time password for 2FA (default is None).
device_id : Optional[str], optional
    Device ID (default is None).
device_name : Optional[str], optional
    Device name (default is None).
interactive_output : bool, optional
    Enable interactive output (default is True).
download_st_version : int, optional
    Download Station API version (default is None).

Methods
-------
get_info()
    Get Download Station info.
get_config()
    Get Download Station config.
set_server_config(...)
    Set Download Station server config.
schedule_info()
    Get schedule info.
schedule_set_config(...)
    Set schedule config.
tasks_list(...)
    List download tasks.
tasks_info(...)
    Get info for specific tasks.
tasks_source(...)
    Download task source.
create_task(...)
    Create a new download task.
delete_task(...)
    Delete a download task.
pause_task(...)
    Pause a download task.
resume_task(...)
    Resume a download task.
edit_task(...)
    Edit a download task.
get_statistic_info()
    Get Download Station statistics.
get_rss_info_list(...)
    Get RSS site info list.
refresh_rss_site(...)
    Refresh RSS site.
rss_feed_list(...)
    Get RSS feed list.
start_bt_search(...)
    Start a BT search.
get_bt_search_results(...)
    Get BT search results.
get_bt_search_category()
    Get BT search categories.
clean_bt_search(...)
    Clean BT search tasks.
get_bt_module()
    Get BT search modules.
## Methods
### `get_info`
Get Download Station info.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Download Station info.  

</div>



---


### `get_config`
Get Download Station config.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Download Station config.  

</div>



---


### `set_server_config`
Set Download Station server configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Info` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_bt_max_download_** `Optional[int]`  
Maximum BT download speed.  
  
**_bt_max_upload_** `Optional[int]`  
Maximum BT upload speed.  
  
**_emule_max_download_** `Optional[int]`  
Maximum eMule download speed.  
  
**_emule_max_upload_** `Optional[int]`  
Maximum eMule upload speed.  
  
**_nzb_max_download_** `Optional[int]`  
Maximum NZB download speed.  
  
**_http_max_download_** `Optional[int]`  
Maximum HTTP download speed.  
  
**_ftp_max_download_** `Optional[int]`  
Maximum FTP download speed.  
  
**_emule_enabled_** `Optional[bool]`  
Enable eMule.  
  
**_unzip_service_enabled_** `Optional[bool]`  
Enable unzip service.  
  
**_default_destination_** `Optional[str]`  
Default download destination.  
  
**_emule_default_destination_** `Optional[str]`  
Default eMule download destination.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `schedule_info`
Get Download Station schedule configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Schedule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Schedule configuration.  

</div>



---


### `schedule_set_config`
Set Download Station schedule configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Schedule` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enabled_** `bool`  
Enable schedule (default is False).  
  
**_emule_enabled_** `bool`  
Enable eMule schedule (default is False).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `tasks_list`
List download tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_param_** `Optional[str or list[str]]`  
Additional fields to retrieve.  
  
**_offset_** `int`  
Offset for pagination (default is 0).  
  
**_limit_** `int`  
Maximum number of tasks to retrieve (default is -1).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of download tasks.  

</div>



---


### `tasks_info`
Get information for specific download tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  
**_additional_param_** `Optional[str or list[str]]`  
Additional fields to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task information.  

</div>



---


### `tasks_source`
Download task source.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation2.Task.Source` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  

</div>
#### Returns
<div class="padding-left--md">
`bytes`  
Task source content.  

</div>



---


### `get_task_list`
Get info from a task list containing the files to be downloaded. This is to be used after creating a task, and before starting the download.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_list_id_** `str`  
List ID returned by create_task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, any]`  
A dictionary containing a task list information.  

</div>



---


### `create_task`
Create a new download task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_url_** `str`  
Download URL.  
  
**_destination_** `str`  
Download destination.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `delete_task`
Delete a download task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  
**_force_** `bool`  
Force delete (default is False).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `pause_task`
Pause a download task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `resume_task`
Resume a download task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `edit_task`
Edit a download task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str or list[str]`  
Task ID(s).  
  
**_destination_** `str`  
New download destination (default is 'sharedfolder').  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `download_task_list`
Download files from a task list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_list_id_** `str`  
Task list ID.  
  
**_file_indexes_** `list[int]`  
List of file indexes to download.  
For example, if `get_task_list()` returns `files: [{index: 0, name: "file1.txt"}, {index: 1, name: "file2.txt"}]`, then `file_indexes = [1]` will download only file2.txt.  
  
**_destination_** `str`  
Download destination, e.g. 'sharedfolder/subfolder'  
  
**_create_subfolder_** `bool`  
Create subfolder. Defaults to `True`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
A dictionary containing the task_id for the started download task.  

</div>



---


### `get_statistic_info`
Get Download Station statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.Statistic` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Statistics information.  

</div>



---


### `get_rss_info_list`
Get RSS site info list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.RSS.Site` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `Optional[int]`  
Offset for pagination.  
  
**_limit_** `Optional[int]`  
Maximum number of RSS sites to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
RSS site info list.  

</div>



---


### `refresh_rss_site`
Refresh an RSS site.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation.RSS.Site` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_rss_id_** `Optional[str]`  
RSS site ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `rss_feed_list`
Get RSS feed list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_rss_id_** `Optional[str]`  
RSS site ID.  
  
**_offset_** `Optional[int]`  
Offset for pagination.  
  
**_limit_** `Optional[int]`  
Maximum number of RSS feeds to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
RSS feed list.  

</div>



---


### `start_bt_search`
Start a BT search.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_keyword_** `Optional[str]`  
Search keyword.  
  
**_module_** `str`  
BT search module (default is 'all').  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
BT search task information or message.  

</div>



---


### `get_bt_search_results`
Get BT search results.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `Optional[str]`  
BT search task ID.  
  
**_offset_** `Optional[int]`  
Offset for pagination.  
  
**_limit_** `Optional[int]`  
Maximum number of results to retrieve.  
  
**_sort_by_** `Optional[str]`  
Field to sort by.  
  
**_sort_direction_** `Optional[str]`  
Sort direction.  
  
**_filter_category_** `Optional[str]`  
Filter by category.  
  
**_filter_title_** `Optional[str]`  
Filter by title.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
BT search results.  

</div>



---


### `get_bt_search_category`
Get BT search categories.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
BT search categories.  

</div>



---


### `clean_bt_search`
Clean BT search tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `Optional[str or list[str]]`  
BT search task ID(s).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `get_bt_module`
Get BT search modules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
BT search modules.  

</div>



---


