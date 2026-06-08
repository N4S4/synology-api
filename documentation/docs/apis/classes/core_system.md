---
sidebar_position: 24
title: 🚧 CoreSystem
description: "Extended Core System API implementation for Synology NAS." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreSystem
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Extended Core System API implementation for Synology NAS.  
  
This class provides methods for system reset button, region/NTP,
theme customisation, desktop settings, help, UI search, and
personal/group/user settings.  
  
## Methods
### `reset_button_get`
Get reset button configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.System.ResetButton`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Reset button configuration.  
</div>
  



---


### `reset_button_set`
Enable or disable the hardware reset button.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.System.ResetButton`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable if True, disable if False. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `region_language_get`
Get system language settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.Language`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Language configuration.  
</div>
  



---


### `region_language_set`
Set system language.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.Language`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_language_** `str`  
Language code (e.g., 'enu', 'cht', 'jpn').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `region_ntp_get`
Get NTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
NTP configuration.  
</div>
  



---


### `region_ntp_set`
Set NTP configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable NTP synchronisation. Defaults to True.  
  
**_server_** `str`  
NTP server address.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ntp_datetime_format_get`
Get date/time format settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP.DateTimeFormat`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Date/time format configuration.  
</div>
  



---


### `ntp_datetime_format_set`
Set date/time format.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP.DateTimeFormat`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_date_format_** `str`  
Date format string (e.g., 'YYYY/MM/DD').  
  
**_time_format_** `str`  
Time format string (e.g., 'HH:mm').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ntp_server_get`
Get NTP server configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
NTP server settings.  
</div>
  



---


### `ntp_server_set`
Enable or disable the NAS as an NTP server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Region.NTP.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
Enable NTP server if True. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `theme_app_portal_login_get`
Get app portal login theme settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.AppPortalLogin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
App portal login theme configuration.  
</div>
  



---


### `theme_app_portal_login_set`
Set app portal login theme.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.AppPortalLogin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Theme key-value pairs (e.g., title, background).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `theme_desktop_get`
Get desktop theme settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Desktop`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Desktop theme configuration.  
</div>
  



---


### `theme_desktop_set`
Set desktop theme.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Desktop`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Theme key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `theme_file_sharing_login_get`
Get file sharing login theme settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.FileSharingLogin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
File sharing login theme configuration.  
</div>
  



---


### `theme_file_sharing_login_set`
Set file sharing login theme.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.FileSharingLogin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Theme key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `theme_image_get`
Get theme image settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Image`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Theme image configuration.  
</div>
  



---


### `theme_image_list`
List available theme images.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Image`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of theme images.  
</div>
  



---


### `theme_login_get`
Get login page theme settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Login`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Login page theme configuration.  
</div>
  



---


### `theme_login_set`
Set login page theme.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Theme.Login`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Theme key-value pairs (e.g., title, background).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `desktop_defs_get`
Get desktop definitions.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.Defs`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Desktop definitions.  
</div>
  



---


### `desktop_initdata_get`
Get desktop initialisation data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.Initdata`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Desktop initialisation data.  
</div>
  



---


### `desktop_jsui_string_get`
Get desktop JS UI string resources.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.JSUIString`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
JS UI string data.  
</div>
  



---


### `desktop_personal_updater_get`
Get desktop personal updater settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.PersonalUpdater`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Personal updater configuration.  
</div>
  



---


### `desktop_personal_updater_set`
Set desktop personal updater settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.PersonalUpdater`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Updater configuration key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `desktop_session_data_get`
Get desktop session data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.SessionData`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Desktop session data.  
</div>
  



---


### `desktop_timeout_get`
Get desktop session timeout settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.Timeout`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Timeout configuration.  
</div>
  



---


### `desktop_timeout_set`
Set desktop session timeout.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.Timeout`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_timeout_minutes_** `int`  
Timeout in minutes. Defaults to 15.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `desktop_ui_string_get`
Get desktop UI string resources.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.UIString`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
UI string data.  
</div>
  



---


### `desktop_upgrade_get`
Get desktop upgrade notification status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Desktop.Upgrade`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Desktop upgrade notification data.  
</div>
  



---


### `help_get`
Get help content.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Help`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_topic_** `str`  
Help topic identifier. If None, returns general help.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Help content.  
</div>
  



---


### `help_list`
List available help topics.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Help`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of help topics.  
</div>
  



---


### `ui_search_get`
Search the DSM UI.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.UISearch`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_query_** `str`  
Search query string.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Search results.  
</div>
  



---


### `ui_search_list`
List all searchable UI items.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.UISearch`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of searchable UI items.  
</div>
  



---


### `personal_settings_get`
Get personal settings for the current user.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalSettings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Personal settings.  
</div>
  



---


### `personal_settings_set`
Set personal settings for the current user.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Settings key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `group_settings_get`
Get group settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.GroupSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_group_** `str`  
Group name. If None, returns all group settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Group settings.  
</div>
  



---


### `group_settings_set`
Set group settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.GroupSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_group_** `str`  
Group name.  
  
**_**kwargs_** `object`  
Settings key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_settings_get`
Get user settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.UserSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
Username. If None, returns current user settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User settings.  
</div>
  



---


### `user_settings_set`
Set user settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.UserSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Settings key-value pairs.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `socketio_emit`
Emit/send a snapshot event notification.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Entry.SocketIo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Entry.SocketIo``.  
</div>
  



---


### `socketio_listeners_count`
Get the current number of active Socket.IO listeners.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Entry.SocketIo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Entry.SocketIo``.  
</div>
  



---


### `license_ha_get_uuid`
Get the Taipei enclosure UUID.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.License.HA`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.License.HA``.  
</div>
  



---


### `license_ha_ha_remote_login`
Perform a remote login via High Availability credential.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.License.HA`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.License.HA``.  
</div>
  



---


### `license_ha_save_vault`
Save/persist the encryption key vault configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.License.HA`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.License.HA``.  
</div>
  



---


### `remote_credential_set`
Set or update the configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Remote.Credential`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Remote.Credential``.  
</div>
  



---


### `remote_credential_challenge_get`
Get remote credential challenge parameters.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Remote.Credential.Challenge`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Remote.Credential.Challenge``.  
</div>
  



---


### `remote_credential_info_get`
Get remote credential service information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Remote.Credential.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Remote.Credential.Info``.  
</div>
  



---


### `remote_credential_verifier_get`
Get remote credential verifier status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Remote.Credential.Verifier`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.Remote.Credential.Verifier``.  
</div>
  



---


### `videoplayer_subtitle_get`
Get VideoPlayer subtitle configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.VideoPlayer.Subtitle`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.VideoPlayer.Subtitle``.  
</div>
  



---


### `videoplayer_drive_subtitle_get`
Get Synology Drive VideoPlayer subtitle settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.VideoPlayer.SynologyDrive.Subtitle`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.VideoPlayer.SynologyDrive.Subtitle``.  
</div>
  



---


