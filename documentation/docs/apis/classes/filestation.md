---
sidebar_position: 15
title: 🚧 FileStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# FileStation
:::warning
 
This API is not documented yet.
 
:::
## Overview
FileStation API implementation.  
Provides methods to interact with Synology NAS FileStation API for file and folder operations,
search, upload, download, and background task management.

### Supported methods
 
    - **Getters** : 
        - Get FileStation info 
        - Get list of shared folders 
        - Get file list in a folder 
        - Get file information 
        - Get search task results 
        - Get mount point list 
        - Get favorite list 
        - Get directory size calculation status 
        - Get MD5 calculation status 
        - Check file/folder permissions 
        - Get shared link information 
        - Get shared link list 
        - Get copy or move task status 
        - Get delete task status 
        - Get extract task status 
        - Get file list of archive 
        - Get compression task status 
        - Get list of all background tasks 
    - **Setters** : 
        - Edit favorite name 
        - Replace all favorites 
        - Edit shared link 
    - **Actions** : 
        - Start search task 
        - Stop search task 
        - Stop all search tasks 
        - Add a favorite 
        - Delete a favorite 
        - Clear broken favorites 
        - Start directory size calculation 
        - Stop directory size calculation 
        - Start MD5 calculation 
        - Stop MD5 calculation 
        - Upload file 
        - Create sharing link 
        - Delete shared link 
        - Clear invalid shared links 
        - Create folder 
        - Rename folder 
        - Start copy or move task 
        - Stop copy or move task 
        - Start delete task 
        - Stop delete task 
        - Delete file or folder (blocking) 
        - Start extract task 
        - Stop extract task 
        - Start file compression 
        - Stop file compression 
        - Download file 
        - Generate file tree  
  
### Parameters
<div class="padding-left--md">
**_ip_address_** `str`  
IP address of the Synology NAS.  
  
**_port_** `str`  
Port number for the connection.  
  
**_username_** `str`  
Username for authentication.  
  
**_password_** `str`  
Password for authentication.  
  
**_secure_** `bool`  
Use HTTPS if True, HTTP otherwise. Default is False.  
  
**_cert_verify_** `bool`  
Verify SSL certificates if True. Default is False.  
  
**_dsm_version_** `int`  
DSM version of the Synology NAS. Default is 7.  
  
**_debug_** `bool`  
Enable debug output if True. Default is True.  
  
**_otp_code_** `str`  
One-time password for 2-step verification. Default is None.  
  
**_device_id_** `str`  
Device ID for authentication. Default is None.  
  
**_device_name_** `str`  
Name of the device. Default is None.  
  
**_interactive_output_** `bool`  
If True, enables interactive output. Default is False.  
  

</div>
  
## Methods
### `get_info`
Get FileStation information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
FileStation information or error message.  

</div>



---


### `get_list_share`
List shared folders.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.List` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_** `str or list of str`  
Additional attributes to include.  
  
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_onlywritable_** `bool`  
If True, only writable shares are listed.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of shared folders or error message.  

</div>



---


### `get_file_list`
List files in a folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.List` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_path_** `str`  
Path to the folder.  
  
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_pattern_** `str`  
Pattern to filter files.  
  
**_filetype_** `str`  
File type filter.  
  
**_goto_path_** `str`  
Path to go to.  
  
**_additional_** `str or list of str`  
Additional attributes to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
List of files or error message.  

</div>



---


### `get_file_info`
Get information about a file or files.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.List` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Path(s) to the file(s).  
  
**_additional_param_** `str or list of str`  
Additional attributes to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
File information or error message.  

</div>



---


### `search_start`
Start a search task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_path_** `str`  
Path to the folder where the search will start.  
  
**_recursive_** `bool`  
If True, the search will be recursive.  
  
**_pattern_** `str`  
Pattern to search for.  
  
**_extension_** `str`  
File extension to filter by.  
  
**_filetype_** `str`  
File type filter.  
  
**_size_from_** `int`  
Minimum file size.  
  
**_size_to_** `int`  
Maximum file size.  
  
**_mtime_from_** `str or int`  
Minimum modification time (Unix timestamp or formatted string).  
  
**_mtime_to_** `str or int`  
Maximum modification time (Unix timestamp or formatted string).  
  
**_crtime_from_** `str or int`  
Minimum creation time (Unix timestamp or formatted string).  
  
**_crtime_to_** `str or int`  
Maximum creation time (Unix timestamp or formatted string).  
  
**_atime_from_** `str or int`  
Minimum access time (Unix timestamp or formatted string).  
  
**_atime_to_** `str or int`  
Maximum access time (Unix timestamp or formatted string).  
  
**_owner_** `str`  
Owner filter.  
  
**_group_** `str`  
Group filter.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Search task ID or error message.  

</div>



---


### `get_search_list`
Get the results of a search task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
Task ID of the search task.  
  
**_filetype_** `str`  
File type filter.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_offset_** `int`  
Offset for pagination.  
  
**_additional_** `str or list of str`  
Additional attributes to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Search results or error message.  

</div>



---


### `stop_search_task`
Stop a search task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Search` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the search task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `stop_all_search_task`
Stop all running search tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Search` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
Confirmation message.  

</div>



---


### `get_mount_point_list`
List mount points.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.VirtualFolder` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_mount_type_** `str`  
Type of mount point to return.  
Posible values:
- `"ftp"` = FTP and FTPS connections
- `"davs"` = WebDAV connections
- `"sharing"` = Public cloud connections  
  
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
Posible values:
- `"name"`
- `"path"`  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_additional_** `str or list of str`  
Additional attributes to include. Defaults to `["real_path","owner","time","perm","mount_point_type"]`.  
Possible values (not exhaustive):
- `"real_path"`
- `"size"`
- `"owner"`
- `"time"`
- `"mount_point_type"`
- `"perm"`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of mount points or error message.  

</div>



---


### `get_favorite_list`
List favorite files and folders.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_status_filter_** `str`  
Status filter.  
  
**_additional_** `str or list of str`  
Additional attributes to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of favorites or error message.  

</div>



---


### `add_a_favorite`
Add a file or folder to favorites.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the file or folder.  
  
**_name_** `str`  
Name for the favorite.  
  
**_index_** `int`  
Index for the favorite.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `delete_a_favorite`
Delete a favorite.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the favorite to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `clear_broken_favorite`
Clear broken favorites.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `edit_favorite_name`
Edit the name of a favorite.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the favorite.  
  
**_new_name_** `str`  
New name for the favorite.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `replace_all_favorite`
Replace all favorites with new paths and names.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Favorite` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
New path or list of new paths for the favorites.  
  
**_name_** `str or list of str`  
New name or list of new names for the favorites.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `start_dir_size_calc`
Start a directory size calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.DirSize` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the directory.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task ID or error message.  

</div>



---


### `stop_dir_size_calc`
Stop a directory size calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.DirSize` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the size calculation task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`str`  
Confirmation message.  

</div>



---


### `get_dir_status`
Get the status of a directory size calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.DirSize` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the size calculation task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task status or error message.  

</div>



---


### `start_md5_calc`
Start an MD5 calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.MD5` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_file_path_** `str`  
Path to the file.  
  

</div>
#### Returns
<div class="padding-left--md">
`str or dict[str, object]`  
Task ID or error message.  

</div>



---


### `get_md5_status`
Get the status of an MD5 calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.MD5` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the MD5 calculation task.  
  

</div>
#### Returns
<div class="padding-left--md">
`str or dict[str, object]`  
Task status or error message.  

</div>



---


### `stop_md5_calc`
Stop an MD5 calculation task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.DirSize` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the MD5 calculation task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`str`  
Confirmation message.  

</div>



---


### `check_permissions`
Check permissions for a file or folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.CheckPermission` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the file or folder.  
  
**_filename_** `str`  
Name of the file.  
  
**_overwrite_** `bool`  
If True, overwriting is allowed.  
  
**_create_only_** `bool`  
If True, only creation is allowed.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Permission check result or error message.  

</div>



---


### `upload_file`
Upload a file to the server.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Upload` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_dest_path_** `str`  
Destination path on the server.  
  
**_file_path_** `str`  
Path to the file to upload.  
  
**_create_parents_** `bool`  
If True, parent folders will be created.  
  
**_overwrite_** `bool`  
If True, existing files will be overwritten.  
  
**_verify_** `bool`  
If True, SSL certificates will be verified.  
  
**_progress_bar_** `bool`  
If True, shows a progress bar during upload.  
  

</div>
#### Returns
<div class="padding-left--md">
`str or tuple[int, dict[str, object]]`  
Upload result or error message.  

</div>



---


### `get_shared_link_info`
Get information about a shared link.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_link_id_** `str`  
ID of the shared link.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Shared link information or error message.  

</div>



---


### `get_shared_link_list`
List shared links.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_force_clean_** `bool`  
If True, forces a clean of the shared link list.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of shared links or error message.  

</div>



---


### `create_sharing_link`
Create a shared link.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
Path to the file or folder to share.  
  
**_password_** `str`  
Password for the shared link.  
  
**_date_expired_** `str or int`  
Expiration date for the shared link (Unix timestamp or formatted string).  
  
**_date_available_** `str or int`  
Availability date for the shared link (Unix timestamp or formatted string).  
  
**_expire_times_** `int`  
Number of times the link can be accessed before expiring.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Shared link details or error message.  

</div>



---


### `delete_shared_link`
Delete a shared link.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_link_id_** `str`  
ID of the shared link to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `clear_invalid_shared_link`
Clear invalid shared links.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `edit_shared_link`
Edit a shared link.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Sharing` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_link_id_** `str`  
ID of the shared link to edit.  
  
**_password_** `str`  
New password for the shared link.  
  
**_date_expired_** `str or int`  
New expiration date for the shared link (Unix timestamp or formatted string).  
  
**_date_available_** `str or int`  
New availability date for the shared link (Unix timestamp or formatted string).  
  
**_expire_times_** `int`  
New number of times the link can be accessed before expiring.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `create_folder`
Create a new folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.CreateFolder` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_path_** `str or list of str`  
Path or list of paths where the folder should be created.  
  
**_name_** `str or list of str`  
Name or list of names for the new folder.  
  
**_force_parent_** `bool`  
If True, parent folders will be created if they don't exist.  
  
**_additional_** `str or list of str`  
Additional attributes to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`str or dict[str, object]`  
Creation result or error message.  

</div>



---


### `rename_folder`
Rename a file or a folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Rename` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Current path or list of paths of the files or folder(s) to rename.  
  
**_name_** `str or list of str`  
New name or list of new names for the file or folder(s).  
  
**_additional_** `str or list of str`  
Additional attributes to include.  
  
**_search_taskid_** `str`  
Task ID of a search task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `start_copy_move`
Start a copy or move task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.CopyMove` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Source path or list of source paths to copy or move.  
  
**_dest_folder_path_** `str or list of str`  
Destination folder path or list of destination folder paths.  
  
**_overwrite_** `bool`  
If True, existing files will be overwritten.  
  
**_remove_src_** `bool`  
If True, source files will be removed after copying.  
  
**_accurate_progress_** `bool`  
If True, shows accurate progress.  
  
**_search_taskid_** `str`  
Task ID of a search task.  
  

</div>
#### Returns
<div class="padding-left--md">
`str or dict[str, object]`  
Task ID or error message.  

</div>



---


### `get_copy_move_status`
Get the status of a copy or move task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.CopyMove` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the copy or move task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task status or error message.  

</div>



---


### `stop_copy_move_task`
Stop a copy or move task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.CopyMove` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the copy or move task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `start_delete_task`
Start a delete task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Delete` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Path or list of paths to the file or folder to delete.  
  
**_accurate_progress_** `bool`  
If True, shows accurate progress.  
  
**_recursive_** `bool`  
If True, deletes folders recursively.  
  
**_search_taskid_** `str`  
Task ID of a search task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task ID or error message.  

</div>



---


### `get_delete_status`
Get the status of a delete task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Delete` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the delete task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task status or error message.  

</div>



---


### `stop_delete_task`
Stop a delete task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Delete` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the delete task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `delete_blocking_function`
Delete a file or folder (blocking function).  
This function will stop your script until done! Do not interrupt.  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Delete` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Path or list of paths to the file or folder to delete.  
  
**_recursive_** `bool`  
If True, deletes folders recursively.  
  
**_search_taskid_** `str`  
Task ID of a search task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `start_extract_task`
Start an extract task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Extract` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_file_path_** `str`  
Path to the archive file.  
  
**_dest_folder_path_** `str`  
Destination folder path where the files will be extracted.  
  
**_overwrite_** `bool`  
If True, existing files will be overwritten.  
  
**_keep_dir_** `bool`  
If True, the original directory structure will be kept.  
  
**_create_subfolder_** `bool`  
If True, a subfolder will be created for the extracted files.  
  
**_codepage_** `str`  
Codepage for the extraction.  
  
**_password_** `str`  
Password for the archive, if required.  
  
**_item_id_** `str`  
Item ID for the extraction task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task ID or error message.  

</div>



---


### `get_extract_status`
Get the status of an extract task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Extract` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the extract task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task status or error message.  

</div>



---


### `stop_extract_task`
Stop an extract task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Extract` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the extract task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `get_file_list_of_archive`
Get the list of files in an archive.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Extract` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_file_path_** `str`  
Path to the archive file.  
  
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_codepage_** `str`  
Codepage for the file list.  
  
**_password_** `str`  
Password for the archive, if required.  
  
**_item_id_** `str`  
Item ID for the archive.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of files in the archive or error message.  

</div>



---


### `start_file_compression`
Start a file compression task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Compress` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str or list of str`  
Path or list of paths to the file or folder to compress.  
  
**_dest_file_path_** `str`  
Destination file path for the compressed file.  
  
**_level_** `int`  
Compression level.  
  
**_mode_** `str`  
Compression mode.  
  
**_compress_format_** `str`  
Compression format.  
  
**_password_** `str`  
Password for the compressed file, if required.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task ID or error message.  

</div>



---


### `get_compress_status`
Get the status of a file compression task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Compress` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the compression task.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task status or error message.  

</div>



---


### `stop_compress_task`
Stop a file compression task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Compress` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID of the compression task to stop.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Response from the API or error message.  

</div>



---


### `get_list_of_all_background_task`
Get a list of all background tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.BackgroundTask` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination.  
  
**_limit_** `int`  
Limit for pagination.  
  
**_sort_by_** `str`  
Field to sort by.  
  
**_sort_direction_** `str`  
Sort direction ('asc' or 'desc').  
  
**_api_filter_** `str`  
API filter.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
List of background tasks or error message.  

</div>



---


### `get_file`
Download a file from the server.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.FileStation.Download` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
The file path starting with a shared folder to be downloaded.  
  
**_mode_** `str`  
Mode for downloading the file ('open' to open in browser, 'download' to download to disk).  
  
**_dest_path_** `str`  
Destination path on the local machine (for 'download' mode).  
  
**_chunk_size_** `int`  
Chunk size for downloading.  
  
**_verify_** `bool`  
If True, SSL certificates will be verified.  
  

</div>
#### Returns
<div class="padding-left--md">
`Optional[str]`  
None if successful, error message otherwise.  

</div>



---


### `generate_file_tree`
Recursively generate the file tree based on the folder path you give constrained with.  
You need to create the root node before calling this function.  
#### Internal API
<div class="padding-left--md">
`hotfix` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_path_** `str`  
Folder path to generate file tree.  
  
**_tree_** `Tree`  
Instance of the Tree from the `treelib` library.  
  
**_max_depth_** `int`  
Non-negative number of maximum depth of tree generation if node tree is directory, default to '1' to generate full tree. If 'max_depth=0' it will be equivalent to no recursion.  
  
**_start_depth_** `int`  
Non negative number to start to control tree generation default to '0'.  
  

</div>



---


