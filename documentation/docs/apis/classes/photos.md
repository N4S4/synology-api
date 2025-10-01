---
sidebar_position: 23
title: 🚧 Photos
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Photos
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Interface for Synology Photos API.

Provides methods to interact with Photos features such as retrieving user info,
folders, albums, sharing, and items.

Parameters
----------
ip_address : str
    The IP address or hostname of the Synology NAS.
port : str
    The port number to connect to.
username : str
    The username for authentication.
password : str
    The password for authentication.
secure : bool, optional
    Whether to use HTTPS. Default is False.
cert_verify : bool, optional
    Whether to verify SSL certificates. Default is False.
dsm_version : int, optional
    DSM version. Default is 7.
debug : bool, optional
    Enable debug output. Default is True.
otp_code : str, optional
    One-time password for 2FA, if required.
device_id : str, optional
    Device ID for the session.
device_name : str, optional
    Device name for the session.
## Methods
### `get_userinfo`
Retrieve user information for the current session.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.UserInfo` 
</div>
  
#### Returns
<div class="padding-left--md">
`Any`  
The user information data.  

</div>



---


### `get_folder`
Retrieve information about a specific folder.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Folder` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The ID of the folder. Default is 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The folder information or an error message.  

</div>



---


### `list_folders`
List folders in Personal Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The parent folder ID. Default is 0.  
  
**_limit_** `int`  
Maximum number of folders to return. Default is 1000.  
  
**_offset_** `int`  
Number of folders to skip. Default is 0.  
  
**_additional_** `str or list of str`  
Additional fields to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of folders or an error message.  

</div>



---


### `list_teams_folders`
List folders in Team Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The parent folder ID. Default is 0.  
  
**_limit_** `int`  
Maximum number of folders to return. Default is 2000.  
  
**_offset_** `int`  
Number of folders to skip. Default is 0.  
  
**_additional_** `str or list of str`  
Additional fields to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of team folders or an error message.  

</div>



---


### `count_folders`
Count folders in Personal Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The parent folder ID. Default is 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The count of folders or an error message.  

</div>



---


### `count_team_folders`
Count folders in Team Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The parent folder ID. Default is 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The count of team folders or an error message.  

</div>



---


### `lookup_folder`
Lookup a folder by path in Personal Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
The folder path.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The folder information or None if not found.  

</div>



---


### `lookup_team_folder`
Lookup a folder by path in Team Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_path_** `str`  
The folder path.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The folder information or None if not found.  

</div>



---


### `get_album`
Retrieve information about a specific album.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_album_id_** `str`  
The album ID.  
  
**_additional_** `str or list of str`  
Additional fields to include.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The album information or an error message.  

</div>



---


### `list_albums`
List albums.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Number of albums to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of albums to return. Default is 100.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of albums or an error message.  

</div>



---


### `suggest_condition`
Suggest album conditions based on a keyword.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.ConditionAlbum` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_keyword_** `str`  
The keyword to suggest conditions for.  
  
**_condition_** `list of str`  
List of conditions to use. Default is ['general_tag'].  
  
**_user_id_** `str`  
User ID to use. If None, uses the current user.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The suggested conditions or an error message.  

</div>



---


### `create_album`
Create a new album with the specified condition.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.ConditionAlbum` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_name_** `str`  
The name of the album.  
  
**_condition_** `list of str`  
The condition for the album.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response for album creation.  

</div>



---


### `delete_album`
Delete an album by ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Album` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_album_id_** `str`  
The album ID.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response for album deletion.  

</div>



---


### `set_album_condition`
Set the condition for an album.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.ConditionAlbum` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The folder ID.  
  
**_condition_** `list of str`  
The condition to set.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response for setting the condition.  

</div>



---


### `share_album`
Share an album with specified permissions.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Sharing.Misc` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_album_id_** `str`  
The album ID.  
  
**_permission_** `str or list of str`  
Permissions to set.  
  
**_enabled_** `bool`  
Whether sharing is enabled. Default is True.  
  
**_expiration_** `int or str`  
Expiration time for the share. Default is 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`Any`  
The API response for sharing the album.  

</div>



---


### `share_team_folder`
Share a team folder with specified permissions.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Sharing.Misc` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_folder_id_** `int`  
The folder ID.  
  
**_permission_** `str`  
Permissions to set.  
  
**_enabled_** `bool`  
Whether sharing is enabled. Default is True.  
  
**_expiration_** `int or str`  
Expiration time for the share. Default is 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`Any`  
The API response for sharing the team folder.  

</div>



---


### `list_shareable_users_and_groups`
List users and groups that can be shared with.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Sharing.Misc` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_team_space_sharable_list_** `bool`  
Whether to include team space sharable list. Default is False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of users and groups or an error message.  

</div>



---


### `list_item_in_folders`
List all items in all folders in Personal Space.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Item` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Specify how many shared folders are skipped before beginning to return listed shared folders.  
  
**_limit_** `int`  
Number of shared folders requested. Set to `0` to list all shared folders.  
  
**_folder_id_** `int`  
ID of folder.  
  
**_sort_by_** `str`  
Possible values: 'filename', 'filesize', 'takentime', 'item_type'.  
  
**_sort_direction_** `str`  
Possible values: 'asc' or 'desc'. Defaults to: 'desc'.  
  
**_type_** `str`  
Possible values: 'photo', 'video', 'live'.  
  
**_passphrase_** `str`  
Passphrase for a shared album.  
  
**_additional_** `list`  
Additional fields to include.
Possible values:
    `["thumbnail","resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of items or an error message.  

</div>



---


### `list_search_filters`
List available search filters.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Search.Filter` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The list of search filters or an error message.  

</div>



---


### `get_guest_settings`
Retrieve guest settings for Photos.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Setting.Guest` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The guest settings or an error message.  

</div>



---


