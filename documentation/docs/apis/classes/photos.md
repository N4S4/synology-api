---
sidebar_position: 43
title: 🚧 Photos
description: "Interface for Synology Photos API." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# Photos
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Interface for Synology Photos API.  
  
Provides methods to interact with Photos features such as retrieving user info,
folders, albums, sharing, and items.  
  
### Parameters
<div class="padding-left--md">

**_ip_address_** `str`  
The IP address or hostname of the Synology NAS.  
  
**_port_** `str`  
The port number to connect to.  
  
**_username_** `str`  
The username for authentication.  
  
**_password_** `str`  
The password for authentication.  
  
**_secure_** `bool`  
Whether to use HTTPS. Default is False.  
  
**_cert_verify_** `bool`  
Whether to verify SSL certificates. Default is False.  
  
**_dsm_version_** `int`  
DSM version. Default is 7.  
  
**_debug_** `bool`  
Enable debug output. Default is True.  
  
**_otp_code_** `str`  
One-time password for 2FA, if required.  
  
**_device_id_** `str`  
Device ID for the session.  
  
**_device_name_** `str`  
Device name for the session.  
  
**_quickconnect_id_** `str`  
QuickConnect ID for relay-based access. Defaults to None.  
  
</div>
  
  
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

`SYNO.Foto.Browse.Folder`  
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

`SYNO.FotoTeam.Browse.Folder`  
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

`SYNO.Foto.Browse.Folder`  
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

`SYNO.FotoTeam.Browse.Folder`  
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

**_album_id_** `str or int or list of str or int`  
The album ID or list of album IDs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response for album deletion.  
</div>
  



---


### `create_normal_album`
Create a normal (manual) album with the specified items.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.NormalAlbum`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
The name of the album.  
  
**_item_ids_** `list of int`  
List of item IDs to add to the album.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response. Album data is in ``data['album']``.  
</div>
  



---


### `rename_album`
Rename an album.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Album`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int`  
The ID of the album to rename.  
  
**_name_** `str`  
The new name for the album.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `get_normal_album`
Retrieve information about a normal (manual) album.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.NormalAlbum`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int`  
The album ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The album information or an error message.  
</div>
  



---


### `list_categories`
List photo categories (recently added, geocoding, general tag, video).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Category`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of categories or an error message.  
</div>
  



---


### `list_concepts`
List AI-detected concepts (tags, objects, scenes).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Concept`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of concepts to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of concepts to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of concepts or an error message.  
</div>
  



---


### `list_team_concepts`
List AI-detected concepts in Team Space.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of concepts to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of concepts to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of concepts or an error message.  
</div>
  



---


### `count_concepts`
Count AI-detected concepts.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of concepts or an error message.  
</div>
  



---


### `count_team_concepts`
Count AI-detected concepts in Team Space.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of concepts or an error message.  
</div>
  



---


### `list_general_tags`
List general tags.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.GeneralTag`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of tags to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of tags to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of tags or an error message.  
</div>
  



---


### `list_team_general_tags`
List general tags in Team Space.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of tags to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of tags to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of tags or an error message.  
</div>
  



---


### `count_general_tags`
Count general tags.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of tags or an error message.  
</div>
  



---


### `count_team_general_tags`
Count general tags in Team Space.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of tags or an error message.  
</div>
  



---


### `list_geocoding`
List geocoding locations from all photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Geocoding`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of locations to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of locations to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of geocoding locations or an error message.  
</div>
  



---


### `list_team_geocoding`
List geocoding locations in Team Space.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of locations to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of locations to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of geocoding locations or an error message.  
</div>
  



---


### `count_geocoding`
Count geocoding locations.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of geocoding locations or an error message.  
</div>
  



---


### `count_team_geocoding`
Count geocoding locations in Team Space.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of geocoding locations or an error message.  
</div>
  



---


### `list_persons`
List detected persons (face recognition).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Person`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of persons to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of persons to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of persons or an error message.  
</div>
  



---


### `list_team_persons`
List detected persons in Team Space.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of persons to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of persons to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of persons or an error message.  
</div>
  



---


### `count_persons`
Count detected persons.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of persons or an error message.  
</div>
  



---


### `count_team_persons`
Count detected persons in Team Space.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of persons or an error message.  
</div>
  



---


### `get_person`
Get information about a detected person.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Person`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_person_id_** `int`  
The person ID (from ``list_persons()``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The person information or an error message.  
</div>
  



---


### `rename_person`
Rename a detected person.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Person`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_person_id_** `int`  
The person ID (from ``list_persons()``).  
  
**_name_** `str`  
The new name for the person. Use ``'Unnamed'`` to clear.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `list_items_by_person`
List photos of a specific person.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_person_id_** `int`  
The person ID (from ``list_persons()``).  
  
**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
**_additional_** `list of str`  
Additional fields to include (e.g., ``['thumbnail', 'person']``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of photos or an error message.  
</div>
  



---


### `get_team_person`
Get information about a detected person in Team Space.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.Person`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_person_id_** `int`  
The person ID (from ``list_team_persons()``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The person information or an error message.  
</div>
  



---


### `list_items_by_team_person`
List Team Space photos of a specific person.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_person_id_** `int`  
The person ID (from ``list_team_persons()``).  
  
**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
**_additional_** `list of str`  
Additional fields to include.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of photos or an error message.  
</div>
  



---


### `list_recently_added`
List recently added items.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.RecentlyAdded`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of recently added items or an error message.  
</div>
  



---


### `list_team_recently_added`
List recently added items in Team Space.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of recently added items or an error message.  
</div>
  



---


### `count_recently_added`
Count recently added items.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of recently added items or an error message.  
</div>
  



---


### `count_team_recently_added`
Count recently added items in Team Space.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of recently added items or an error message.  
</div>
  



---


### `get_timeline`
Get the timeline sections.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Timeline`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The timeline sections or an error message.  
</div>
  



---


### `get_team_timeline`
Get the Team Space timeline sections.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.Timeline`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The timeline sections or an error message.  
</div>
  



---


### `get_similar_timeline`
Get the similar-items timeline.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.SimilarTimeline`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The similar timeline sections or an error message.  
</div>
  



---


### `get_team_similar_timeline`
Get the Team Space similar-items timeline.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.SimilarTimeline`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The similar timeline sections or an error message.  
</div>
  



---


### `list_similar_items`
List items similar to the specified item.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.SimilarItem`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The ID of the reference item.  
  
**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of similar items or an error message.  
</div>
  



---


### `list_team_similar_items`
List items similar to the specified item in Team Space.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.SimilarItem`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The ID of the reference item.  
  
**_offset_** `int`  
Number of items to skip. Default is 0.  
  
**_limit_** `int`  
Maximum number of items to return. Default is 1000.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of similar items or an error message.  
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

`SYNO.Foto.Sharing.Passphrase`  
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

`SYNO.FotoTeam.Sharing.Passphrase`  
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
List items in a Personal Space folder.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Specify how many items are skipped before beginning to return listed items.  
  
**_limit_** `int`  
Number of items requested. Default is 1000.  
  
**_folder_id_** `int, required`  
ID of the folder returned by ``list_folders``.  
  
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


### `list_item_in_team_folders`
List items in a Team Space folder.  
  
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Specify how many items are skipped before beginning to return listed items.  
  
**_limit_** `int`  
Number of items requested. Default is 1000.  
  
**_folder_id_** `int, required`  
ID of the folder returned by ``list_teams_folders``.  
  
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
The list of team items or an error message.  
</div>
  



---


### `list_items_in_album`
List items in an album.  
  
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int, required`  
The ID of the album (from ``list_albums()``).  
  
**_offset_** `int`  
Specify how many items are skipped before beginning to return listed items.  
  
**_limit_** `int`  
Number of items requested. Default is 1000.  
  
**_sort_by_** `str`  
Possible values: ``'filename'``, ``'filesize'``, ``'takentime'``, ``'item_type'``.  
  
**_sort_direction_** `str`  
Possible values: ``'asc'`` or ``'desc'``. Defaults to ``'desc'``.  
  
**_type_** `str`  
Possible values: ``'photo'``, ``'video'``, ``'live'``.  
  
**_passphrase_** `str`  
Passphrase for a shared album.  
  
**_additional_** `list`  
Additional fields to include.
Possible values:
    ``["thumbnail", "resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of album items or an error message.  
</div>
  



---


### `count_items_in_album`
Count items in an album.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int`  
The ID of the album.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of album items or an error message.  
</div>
  



---


### `list_items_in_team_album`
List items in a Team Space album.  
  
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int, required`  
The ID of the Team Space album (from ``list_albums()``).  
  
**_offset_** `int`  
Specify how many items are skipped before beginning to return listed items.  
  
**_limit_** `int`  
Number of items requested. Default is 1000.  
  
**_sort_by_** `str`  
Possible values: ``'filename'``, ``'filesize'``, ``'takentime'``, ``'item_type'``.  
  
**_sort_direction_** `str`  
Possible values: ``'asc'`` or ``'desc'``. Defaults to ``'desc'``.  
  
**_type_** `str`  
Possible values: ``'photo'``, ``'video'``, ``'live'``.  
  
**_passphrase_** `str`  
Passphrase for a shared album.  
  
**_additional_** `list`  
Additional fields to include.
Possible values:
    ``["thumbnail", "resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The list of album items or an error message.  
</div>
  



---


### `count_items_in_team_album`
Count items in a Team Space album.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_album_id_** `int`  
The ID of the Team Space album.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The count of album items or an error message.  
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


### `get_index_status`
Get the indexing status for photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Index`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The index status counters (basic, thumbnail, metadata, face, concept, geo)
or an error message.  
</div>
  



---


### `get_team_index_status`
Get the Team Space indexing status for photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.FotoTeam.Index`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The index status counters or an error message.  
</div>
  



---


### `get_admin_settings`
Get the admin settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.Admin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The admin settings (package version, global config) or an error message.  
</div>
  



---


### `set_admin_settings`
Set admin settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.Admin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Admin settings key-value pairs to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `get_user_settings`
Get the user settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The user settings (theme, sort, AME status) or an error message.  
</div>
  



---


### `set_user_settings`
Set user settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
User settings key-value pairs to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `get_team_space_settings`
Get Team Space settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.TeamSpace`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The Team Space settings (enabled, concepts, person, similar) or an error message.  
</div>
  



---


### `set_team_space_settings`
Set Team Space settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.TeamSpace`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Team Space settings key-value pairs to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `get_wizard_settings`
Get the wizard (first-time setup) settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.Wizard`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The wizard settings or an error message.  
</div>
  



---


### `set_wizard_settings`
Set wizard (first-time setup) settings for Photos.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.Wizard`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `dict`  
Wizard settings key-value pairs to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `get_mobile_compatibility`
Get mobile version compatibility info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Setting.MobileCompatibility`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The mobile compatibility settings or an error message.  
</div>
  



---


### `get_item_info`
Get detailed information about a photo item.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The item ID (from ``list_items_in_album()`` or ``list_item_in_folders()``).  
  
**_additional_** `list of str`  
Additional fields to include.
Possible values:
    ``["exif", "gps", "tag", "description", "person", "address",
    "thumbnail", "resolution", "orientation"]``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The item information. Detail fields are in ``data['list'][0]['additional']``.  
</div>
  



---


### `set_item_description`
Set the description of a photo item.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The item ID.  
  
**_description_** `str`  
The new description. Pass an empty string to clear it.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `set_item_favorite`
Set or unset the favorite flag on a photo item.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The item ID.  
  
**_favorite_** `bool`  
``True`` to mark as favorite, ``False`` to unmark. Default is ``True``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `set_item_rating`
Set the star rating of a photo item (0-5).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Browse.Item`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The item ID.  
  
**_rating_** `int`  
Star rating from 0 to 5. Default is 0.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response.  
</div>
  



---


### `search_suggestions`
Get search suggestions for a keyword.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Search.Search`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_keyword_** `str`  
The search keyword.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The search suggestions or an error message.  
</div>
  



---


### `download_item`
Download a photo item to a file.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Foto.Download`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_item_id_** `int`  
The item ID to download.  
  
**_dest_path_** `str`  
The destination file path. If not provided, saves to the current
directory using the item's filename.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`str or None`  
The path to the downloaded file, or ``None`` if the download failed.  
</div>
  



---


