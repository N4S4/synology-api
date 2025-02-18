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

## Methods
### `get_userinfo`



---


### `get_folder`



---


### `list_folders`



---


### `list_teams_folders`



---


### `count_folders`



---


### `count_team_folders`



---


### `lookup_folder`



---


### `lookup_team_folder`



---


### `get_album`



---


### `list_albums`



---


### `suggest_condition`



---


### `create_album`



---


### `delete_album`



---


### `set_album_condition`



---


### `share_album`



---


### `share_team_folder`



---


### `list_shareable_users_and_groups`



---


### `list_item_in_folders`
List all items in all folders in Personal Space  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Foto.Browse.Item` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Specify how many shared folders are skipped before beginning to return listed shared folders.  
  
**_limit_** `int `  
Number of shared folders requested. Set to `0` to list all shared folders.  
  
**_folder_id_** `int`  
ID of folder  
  
**_sort_by_** `str`  
Possible values: 
- `filename`
- `filesize`
- `takentime`
- `item_type`  
  
**_sort_direction_** `str, optional `  
Possible values: `asc` or `desc`. Defaults to: `desc`  
  
**_passphrase_** `str`  
Passphrase for a shared album  
  
**_additional_** `list[str]`  
Possible values:
`["thumbnail","resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]`  
  
**_type_** `str `  
Possible values:
- `photo`: Photo 
- `video`: Video 
- `live`: iPhone live photos'  
  

</div>



---


### `list_search_filters`



---


### `get_guest_settings`



---


