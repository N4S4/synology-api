---
sidebar_position: 21
title: 🚧 CoreServiceHW
description: "Core hardware/media/package: Group, Hardware, ISCSI, Media, OAuth, Package, PortFwd." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreServiceHW
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core hardware/media/package: Group, Hardware, ISCSI, Media, OAuth, Package, PortFwd.  
  
  
  
## Methods
### `group_extra_admin_get`
Get extra admin group settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.ExtraAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group extra admin get operation.  
</div>
  



---


### `group_member_list`
List members of a group.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.Member`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_group_** `str`  
The group value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group member list operation.  
</div>
  



---


### `group_valid_local_admin_get`
Get valid local admin information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Group.ValidLocalAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the group valid local admin get operation.  
</div>
  



---


### `hardware_lcm_get`
Get LCD monitor panel settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.LCM`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware lcm get operation.  
</div>
  



---


### `hardware_led_brightness_get`
Get LED brightness settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.Led.Brightness`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware led brightness get operation.  
</div>
  



---


### `hardware_led_brightness_set`
Set LED brightness level.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.Led.Brightness`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_brightness_** `int`  
The brightness value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware led brightness set operation.  
</div>
  



---


### `hardware_memory_layout_get`
Get memory layout information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.MemoryLayout`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware memory layout get operation.  
</div>
  



---


### `hardware_need_reboot_get`
Check if a reboot is required.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.NeedReboot`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware need reboot get operation.  
</div>
  



---


### `hardware_oob_management_get`
Get out-of-band management (IPMI/BMC) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.OOBManagement`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware oob management get operation.  
</div>
  



---


### `hardware_remote_fan_status_get`
Get remote fan status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.RemoteFanStatus`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware remote fan status get operation.  
</div>
  



---


### `hardware_spectre_meltdown_get`
Get Spectre/Meltdown mitigation status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.SpectreMeltdown`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware spectre meltdown get operation.  
</div>
  



---


### `hardware_video_transcoding_get`
Get hardware video transcoding capability.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Hardware.VideoTranscoding`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the hardware video transcoding get operation.  
</div>
  



---


### `iscsi_fc_target_get`
Get Fibre Channel target settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.FCTarget`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi fc target get operation.  
</div>
  



---


### `iscsi_host_get`
Get iSCSI host settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Host`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi host get operation.  
</div>
  



---


### `iscsi_lunbkp_get`
Get iSCSI LUN backup settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Lunbkp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi lunbkp get operation.  
</div>
  



---


### `iscsi_node_get`
Get iSCSI node information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Node`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi node get operation.  
</div>
  



---


### `iscsi_replication_get`
Get iSCSI replication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.Replication`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi replication get operation.  
</div>
  



---


### `iscsi_vmware_get`
Get iSCSI VMware integration settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ISCSI.VMware`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the iscsi vmware get operation.  
</div>
  



---


### `media_indexing_get`
Get media indexing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing get operation.  
</div>
  



---


### `media_indexing_set`
Set media indexing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing set operation.  
</div>
  



---


### `media_indexing_index_folder_get`
Get indexed folder list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.IndexFolder`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing index folder get operation.  
</div>
  



---


### `media_indexing_media_converter_get`
Get media converter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.MediaConverter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing media converter get operation.  
</div>
  



---


### `media_indexing_scheduler_get`
Get media indexing scheduler settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.Scheduler`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing scheduler get operation.  
</div>
  



---


### `media_indexing_thumbnail_quality_get`
Get thumbnail quality settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MediaIndexing.ThumbnailQuality`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the media indexing thumbnail quality get operation.  
</div>
  



---


### `mydscenter_get`
Get MyDS Center settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter get operation.  
</div>
  



---


### `mydscenter_account_get`
Get MyDS Center account information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter account get operation.  
</div>
  



---


### `mydscenter_login`
Login to MyDS Center.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Login`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_username_** `str`  
The username value.  
  
**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter login operation.  
</div>
  



---


### `mydscenter_logout`
Logout from MyDS Center.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Logout`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter logout operation.  
</div>
  



---


### `mydscenter_purchase_get`
Get MyDS Center purchase information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.MyDSCenter.Purchase`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the mydscenter purchase get operation.  
</div>
  



---


### `normal_user_get`
Get normal user settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.NormalUser`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the normal user get operation.  
</div>
  



---


### `normal_user_login_notify_get`
Get normal user login notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.NormalUser.LoginNotify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the normal user login notify get operation.  
</div>
  



---


### `oauth_scope_get`
Get OAuth scope settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Scope`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth scope get operation.  
</div>
  



---


### `oauth_server_get`
Get OAuth server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Server`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth server get operation.  
</div>
  



---


### `oauth_server_set`
Set OAuth server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OAuth.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the oauth server set operation.  
</div>
  



---


### `package_auto_upgrade_progress_get`
Get package auto-upgrade progress.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.AutoUpgrade.Progress`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package auto upgrade progress get operation.  
</div>
  



---


### `package_control`
Control a package (start/stop).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Control`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
**_action_** `str`  
The action value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package control operation.  
</div>
  



---


### `package_fake_iframe_get`
Get package fake iframe info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.FakeIFrame`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package fake iframe get operation.  
</div>
  



---


### `package_feed_list`
List package feeds.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Feed`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package feed list operation.  
</div>
  



---


### `package_feed_set`
Set package feed settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Feed`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package feed set operation.  
</div>
  



---


### `package_legal_prerelease_get`
Get package pre-release legal agreement status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Legal.PreRelease`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package legal prerelease get operation.  
</div>
  



---


### `package_log_get`
Get package log entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Log`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package log get operation.  
</div>
  



---


### `package_myds_get`
Get MyDS package info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.MyDS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package myds get operation.  
</div>
  



---


### `package_myds_purchase_get`
Get MyDS package purchase info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.MyDS.Purchase`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package myds purchase get operation.  
</div>
  



---


### `package_progress_get`
Get package installation/upgrade progress.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Progress`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_task_id_** `str`  
The task id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package progress get operation.  
</div>
  



---


### `package_screenshot_get`
Get package screenshots.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Screenshot`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package screenshot get operation.  
</div>
  



---


### `package_screenshot_server_get`
Get package screenshot from server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Screenshot.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package screenshot server get operation.  
</div>
  



---


### `package_setting_update_get`
Get package update settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Setting.Update`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package setting update get operation.  
</div>
  



---


### `package_thumb_get`
Get package thumbnail.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Thumb`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package thumb get operation.  
</div>
  



---


### `package_thumb_server_get`
Get package thumbnail from server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Package.Thumb.Server`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_package_id_** `str`  
The package id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the package thumb server get operation.  
</div>
  



---


### `personal_notification_device_get`
Get personal notification device settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification device get operation.  
</div>
  



---


### `personal_notification_event_get`
Get personal notification events.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Event`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification event get operation.  
</div>
  



---


### `personal_notification_filter_get`
Get personal notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Filter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification filter get operation.  
</div>
  



---


### `personal_notification_filter_set`
Set personal notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Filter`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification filter set operation.  
</div>
  



---


### `personal_notification_mobile_get`
Get personal notification mobile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Mobile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification mobile get operation.  
</div>
  



---


### `personal_notification_settings_get`
Get personal notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Settings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification settings get operation.  
</div>
  



---


### `personal_notification_settings_set`
Set personal notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PersonalNotification.Settings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the personal notification settings set operation.  
</div>
  



---


### `photo_viewer_get`
Get photo viewer settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PhotoViewer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the photo viewer get operation.  
</div>
  



---


### `port_forwarding_get`
Get port forwarding settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding get operation.  
</div>
  



---


### `port_forwarding_compatibility_get`
Get port forwarding compatibility status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.Compatibility`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding compatibility get operation.  
</div>
  



---


### `port_forwarding_router_info_get`
Get router information for port forwarding.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.RouterInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding router info get operation.  
</div>
  



---


### `port_forwarding_router_list`
List detected routers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.RouterList`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding router list operation.  
</div>
  



---


### `port_forwarding_rules_serv_get`
Get service-based port forwarding rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.PortForwarding.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the port forwarding rules serv get operation.  
</div>
  



---


