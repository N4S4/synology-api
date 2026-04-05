---
sidebar_position: 13
title: 🚧 DownloadStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# DownloadStation
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Download Station API implementation for Synology NAS.  
  
This class provides methods to manage downloads, tasks, RSS feeds, and BT searches.

### Supported methods

    - **Getters** :
        - Get Download Station info.
        - Get Download Station config.
        - Get Download Station statistics.
        - Get RSS site info list.
        - Get schedule info.
        - Get info for specific tasks.
        - List download tasks.
        - Get RSS feed list.
        - Get RSS feed filter list.
        - Get BT search results.
        - Get BT search categories.
        - Get BT search modules.
    - **Setters** :
        - Set Download Station server config.
        - Set schedule config.
        - Create a new download task.
        - Edit a download task.
        - Delete a download task.
        - Add RSS feed filter.
        - Set RSS feed filter.
        - Delete RSS feed filter.
    - **Actions** :
        - Download task source.
        - Pause a download task.
        - Resume a download task.
        - Refresh RSS site.
        - Start a BT search.
        - Clean BT search tasks.  
  
### Parameters
<div class="padding-left--md">
**_ip_address_** `str`  
IP address or hostname of the Synology NAS.  
  
**_port_** `str`  
Port number to connect to.  
  
**_username_** `str`  
Username for authentication.  
  
**_password_** `str`  
Password for authentication.  
  
**_secure_** `bool`  
Use HTTPS if True, HTTP if False (default is False).  
  
**_cert_verify_** `bool`  
Verify SSL certificates (default is False).  
  
**_dsm_version_** `int`  
DSM version (default is 7).  
  
**_debug_** `bool`  
Enable debug output (default is True).  
  
**_otp_code_** `Optional[str]`  
One-time password for 2FA (default is None).  
  
**_device_id_** `Optional[str]`  
Device ID (default is None).  
  
**_device_name_** `Optional[str]`  
Device name (default is None).  
  
**_interactive_output_** `bool`  
Enable interactive output (default is True).  
  
**_download_st_version_** `int`  
Download Station API version (default is None).  
  

</div>
  
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
Get info from a task list containing the files to be downloaded.  
This is to be used after creating a task, and before starting the download.  
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
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data" : {
        "files" : [
            {
                "index" : 0,
                "name" : "Pulp.Fiction.1994.2160p.4K.BluRay.x265.10bit.AAC5.1-[YTS.MX].mkv",
                "size" : 2391069024
            },
            {
                "index" : 1,
                "name" : "YTSProxies.com.txt",
                "size" : 604
            },
            {
                "index" : 2,
                "name" : "www.YTS.MX.jpg",
                "size" : 53226
            }
        ],
        "size" : 7835426779,
        "title" : "Pulp Fiction (1994) [2160p] [4K] [BluRay] [5.1] [YTS.MX]",
        "type" : "bt"
    },
}
```
</details>



---


### `create_task`
Create a new download task.  
You can choose between a url or a file path (.torrent).  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_url_** `str`  
Download URL. Use either `url` or `file_path`.  
  
**_file_path_** `str`  
Path to a file (e.g. a .torrent) to download.  
  
**_destination_** `str`  
Download destination folder (default is "").  
  

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
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    'data': {
        'task_id': 'username/SYNODLTaskListDownload1759340338C7C39ABA'
    }
}
```
</details>



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


### `rss_feed_filter_list`
Get RSS feed filter list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_feed_id_** `int`  
RSS feed ID.  
  
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Maximum number of filters to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
RSS feed filter list.  

</div>



---


### `rss_feed_filter_add`
Add RSS feed filter.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_feed_id_** `int`  
RSS feed ID.  
  
**_filter_name_** `str`  
Filter name.  
  
**_match_** `str`  
Match pattern.  
  
**_not_match_** `str`  
Not match pattern.  
  
**_destination_** `str`  
Download destination.  
  
**_is_regex_** `bool`  
Use regex for matching (default is False).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `rss_feed_filter_set`
Set RSS feed filter.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_id_** `int`  
Filter ID.  
  
**_filter_name_** `str`  
Filter name.  
  
**_match_** `str`  
Match pattern.  
  
**_not_match_** `str`  
Not match pattern.  
  
**_destination_** `str`  
Download destination.  
  
**_is_regex_** `bool`  
Use regex for matching (default is False).  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `rss_feed_filter_delete`
Delete RSS feed filter.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DownloadStation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_filter_id_** `int`  
Filter ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

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


