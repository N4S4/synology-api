
![synology-api](https://user-images.githubusercontent.com/33936751/100731387-99fffc00-33cb-11eb-833c-b6ab87177651.jpg)

# Synology Wrapper

If you find yourself on this page,
most probably you are trying to develop something for your NAS,

this wrapper might come to your help to build your script.

I would like to specify that I do this for hobby as is my passion and in my **little** free time.

Said this, there is no warranties chained and this library is provided **"As Is"**, 
you will find many things can be simplified, and I slowly will but feel free to [Contribute](https://github.com/N4S4/synology-api/blob/master/CONTRIBUTING.md).
 
## Feeling kind?
If this code helps and you wish to support me 
- Paypal: https://paypal.me/ren4s4

## Groups to Ask Discuss Request and Improve the code

- Telegram [Synology Api](https://t.me/SynologyApi) Preferred


## Something worth to read

[Contributing](https://github.com/N4S4/synology-api/blob/master/CONTRIBUTING.md),
[Code of Conduct](https://github.com/N4S4/synology-api/blob/master/CODE_OF_CONDUCT.md)


## See Related projects

- [Synology API Telegram Bot](https://github.com/N4S4/synology-api-telegram-bot)

If you want to show your project in this section, write me.

## Premise

I've tried this wrapper only with python3 
I do not know if it actually runs with previous versions 

Before opening an issue make sure you do your own research, if you are not sure, write me.

## Prerequisites

Prior to install this wrapper see requirements.txt.

## Installation

Just go to repository folder and run the setup.py it will install the wrapper for you.
from the command line go to the downloaded folder and run:

```
pip3 install synology-api
```

or


```
python3.6 setup.py install
```

or

```
pip3 install git+https://github.com/N4S4/synology-api
```


## Basic Usage HTTP

```python
from synology_api import filestation, downloadstation

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will log in automatically 
# NOTE: for Filestation and Downloadstation only has been added interactive_output=True,
# It can be omitted and initiate the wrapper with the below ove code

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

fl.`get_info()`

dwn = downloadstation.DownloadStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

dwn.`get_info()`

```

response would be json data

```json 
{"data": {"enable_list_usergrp": "False",
  "hostname": "MyCloud",
  "is_manager": "True",
  "items": [{"gid": 100}, {"gid": 101}],
  "support_file_request": "True",
  "support_sharing": "True",
  "support_vfs": "True",
  "support_virtual": {"enable_iso_mount": "True", "enable_remote_mount": "True"},
  "support_virtual_protocol": ["cifs", "nfs", "iso"],
  "system_codepage": "enu",
  "uid": 1026},
 "success": "True"}
```

## If required HTTPS  (it requires a valid certificate)

```python

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=True, cert_verify=True, dsm_version=7, debug=True, otp_code=None)

```

the ```secure=True``` variable is needed to be set to true if https is required; default value is ```False``` <br />
the ```cert_verify=True```  is optional, if you want to verify your certificate set it to ```True```; default value is ```False```<br />
the ```dsm_version=7``` is optional, make sure to set '7' if you use DSM version 7 or above, if left blank default value 
will be for DSM 6 or below 
the ```debug=True``` is optional, if set to False not all responses will return to console<br />
If your login require ```otp_code``` you can set it changing the None value.

## Available Functions

There are quite few available functions so... I will need to write a documentation as  
I will slowly implement more functions, Synology APIs are plenty, too many for my little time.

This wrapper cover the following APIs for now:

| DownloadStation                |
|--------------------------------|
| SYNO.DownloadStation.Info      |
| SYNO.DownloadStation.Schedule  |
| SYNO.DownloadStation.Task      |
| SYNO.DownloadStation.Statistic |
| SYNO.DownloadStation.RSS.Site  |
| SYNO.DownloadStation.RSS.Feed  |
| SYNO.DownloadStation.BTSearch  |

| FileStation                      |
|----------------------------------|
| SYNO.FileStation.Info            |
| SYNO.FileStation.List            | 
| SYNO.FileStation.Search          | 
| SYNO.FileStation.VirtualFolder   | 
| SYNO.FileStation.Favorite        | 
| SYNO.FileStation.DirSize         | 
| SYNO.FileStation.CheckPermission | 
| SYNO.FileStation.Upload          | 
| SYNO.FileStation.Sharing         | 
| SYNO.FileStation.CreateFolder    | 
| SYNO.FileStation.Rename          | 
| SYNO.FileStation.CopyMove        | 
| SYNO.FileStation.Delete          | 
| SYNO.FileStation.Extract         | 
| SYNO.FileStation.Compress        | 
| SYNO.FileStation.BackgroundTask  | 

| Photo                            |
|----------------------------------|
| SYNO.Foto.UserInfo               |
| SYNO.Foto.Browse.Folder          |
| SYNO.FotoTeam.Browse.Folder      |
| SYNO.Foto.Browse.Album           |
| SYNO.Foto.Browse.ConditionAlbum  |
| SYNO.Foto.Sharing.Passphrase     |
| SYNO.FotoTeam.Sharing.Passphrase |
| SYNO.Foto.Sharing.Misc           |
| SYNO.Foto.Browse.Item            |
| SYNO.Foto.Search.Filter          |
| SYNO.Foto.Setting.Guest          |

| core_sys_info                         |  
|---------------------------------------|  
| SYNO.Backup.Service.NetworkBackup     |  
| SYNO.Core.BandwidthControl            |  
| SYNO.Core.BandwidthControl.Protocol   |  
| SYNO.Core.BandwidthControl.Status     |  
| SYNO.Core.CurrentConnection           |  
| SYNO.Core.Directory.Domain.Schedule   |  
| SYNO.Core.Directory.LDAP              |  
| SYNO.Core.Directory.SSO               |  
| SYNO.Core.ExternalDevice.UPS          |  
| SYNO.Core.FileServ.AFP                |  
| SYNO.Core.FileServ.FTP                |  
| SYNO.Core.FileServ.FTP.SFTP           |  
| SYNO.Core.FileServ.NFS                |  
| SYNO.Core.FileServ.ServiceDiscovery   |  
| SYNO.Core.FileServ.SMB                |  
| SYNO.Core.Group                       | 
| SYNO.Core.Group.Member                | 
| SYNO.Core.Hardware.BeepControl        |  
| SYNO.Core.Hardware.FanSpeed           |  
| SYNO.Core.Hardware.Hibernation        |  
| SYNO.Core.Hardware.PowerSchedule      |  
| SYNO.Core.Network                     |  
| SYNO.Core.Network.Bond                |  
| SYNO.Core.Network.Bridge              |  
| SYNO.Core.Network.Ethernet            |  
| SYNO.Core.Network.IPv6Tunnel          |  
| SYNO.Core.Network.LocalBridge         |  
| SYNO.Core.Network.PPPoE               |  
| SYNO.Core.Network.Router.Topology     |  
| SYNO.Core.Network.USBModem            |  
| SYNO.Core.Network.VPN.L2TP            |  
| SYNO.Core.Network.VPN.OpenVPN         |  
| SYNO.Core.Network.VPN.OpenVPNWithConf |  
| SYNO.Core.Network.VPN.PPTP            |  
| SYNO.Core.Network.Wifi.Client         |  
| SYNO.Core.Notification.Mail.Conf      |  
| SYNO.Core.Notification.Push.Conf      |  
| SYNO.Core.Notification.Push.Mail      |  
| SYNO.Core.Notification.SMS.Conf       |  
| SYNO.Core.QuickConnect                |  
| SYNO.Core.QuickConnect.Permission     |  
| SYNO.Core.Quota                       |
| SYNO.Core.SecurityScan.Conf           |  
| SYNO.Core.SecurityScan.Status         |  
| SYNO.Core.Share                       |
| SYNO.Core.Share.Permission            |
| SYNO.Core.SNMP                        |  
| SYNO.Core.SyslogClient.FileTransfer   |  
| SYNO.Core.SyslogClient.Setting.Notify |  
| SYNO.Core.SyslogClient.Status         |  
| SYNO.Core.System                      |  
| SYNO.Core.System.Process              |  
| SYNO.Core.System.Status               |  
| SYNO.Core.System.Utilization          |  
| SYNO.Core.Terminal                    |  
| SYNO.Core.Upgrade.Server              |  
| SYNO.Core.Upgrade.Server.Download     |  
| SYNO.Core.Upgrade.Setting             |  
| SYNO.Core.User                        |  
| SYNO.Core.User.PasswordConfirm        |  
| SYNO.Core.User.PasswordExpiry         |  
| SYNO.Core.User.PasswordPolicy         |  
| SYNO.Core.Web.DSM                     |  
| SYNO.Storage.CGI.Storage              |  

| Virtualization                       |
|--------------------------------------|
| SYNO.Virtualization.API.Task.Info    |
| SYNO.Virtualization.API.Network      |
| SYNO.Virtualization.API.Storage      |
| SYNO.Virtualization.API.Host         |
| SYNO.Virtualization.API.Guest        |
| SYNO.Virtualization.API.Guest.Action |
| SYNO.Virtualization.API.Guest.Image  |

| core_backup (Hyper Backup / Hyper Backup Vault) |
|-------------------------------------------------|
| SYNO.Backup.Repository                          |
| SYNO.Backup.Task                                |
| SYNO.SDS.Backup.Client.Common.Log               |
| SYNO.SDS.Backup.Server.Common.Log               |
| SYNO.SDS.Backup.Server.Common.Statistic         |
| SYNO.Backup.Service.VersionBackup.Target        |
| SYNO.Backup.Service.VersionBackup.Config        | 

| core_active_backup (Active Backup for Business) |
|-------------------------------------------------|
| SYNO.ActiveBackup.Inventory                     |
| SYNO.ActiveBackup.Overview                      |
| SYNO.ActiveBackup.Task                          |
| SYNO.ActiveBackup.Share                         |
| SYNO.ActiveBackup.Version                       | 
| SYNO.ActiveBackup.Log                           |

| abm (Active Backup for Microsoft 365) |
|-------------------------------------------------|
| SYNO.ActiveBackupOffice365                      |

| Core User                      |
|--------------------------------|
| SYNO.Core.User                 |
| SYNO.Core.User.Group           |
| SYNO.Core.User.PasswordPolicy  |
| SYNO.Core.User.PasswordExpiry  |
| SYNO.Core.User.PasswordConfirm |
| SYNO.Core.User.UsernamePolicy  |

| Core Share                         |
|------------------------------------|
| SYNO.Core.Share                    |
| SYNO.Core.Share.Permission         |
| SYNO.Core.Share.KeyManager.Store   |
| SYNO.Core.Share.KeyManager.AutoKey |

| Snapshot Replication     |
|--------------------------|
| SYNO.Core.Share.Snapshot |

| Cloud Sync     |
|----------------|
| SYNO.CloudSync |

| Task Scheduler / Event Scheduler |
|----------------------------------|
| SYNO.Core.TaskScheduler          |
| SYNO.Core.TaskScheduler.Root     |
| SYNO.Core.EventScheduler         |
| SYNO.Core.EventScheduler.Root    |

### Not all Surveillance Station functions works.
| Surveillance Station                                      |
|-----------------------------------------------------------|
| SYNO.SurveillanceStation.Info                             |
| SYNO.SurveillanceStation.Camera                           |
| SYNO.Surveillance.Camera.Event                            |
| SYNO.SurveillanceStation.Camera.Group                     |
| SYNO.SurveillanceStation.Camera.Import                    |
| SYNO.SurveillanceStation.Camera.Wizard                    |
| SYNO.SurveillanceStation.PTZ                              |
| SYNO.SurveillanceStation.ExternalRecording.               |
| SYNO.SurveillanceStation.Recording                        |
| SYNO.SurveillanceStation.Recording.Export                 |
| SYNO.SurveillanceStation.Recording.Mount                  |
| SYNO.SurveillanceStation.CMS                              |
| SYNO.SurveillanceStation.CMS.GetDsStatus                  |
| SYNO.SurveillanceStation.CMS.SlavedsWizard                |
| SYNO.SurveillanceStation.CMS.SlavedsList                  |
| SYNO.SurveillanceStation.Log                              |
| SYNO.SurveillanceStation.License                          |
| SYNO.SurveillanceStation.Stream                           |
| SYNO.SurveillanceStation.ActionRule                       |
| SYNO.SurveillanceStation.Emap                             |
| SYNO.SurveillanceStation.Emap.Image                       |
| SYNO.SurveillanceStation.Notification                     |
| SYNO.SurveillanceStation.Notification.SMS                 |
| SYNO.SurveillanceStation.Notification.PushService         |
| SYNO.SurveillanceStation.Notification.Schedule            |
| SYNO.SurveillanceStation.Notification.Email               |
| SYNO.SurveillanceStation.Notification.Filter              |
| SYNO.SurveillanceStation.Notification.SMS.ServiceProvider |
| SYNO.SurveillanceStation.Addons                           |
| SYNO.SurveillanceStation.Alert                            |
| SYNO.SurveillanceStation.Alert.Setting                    |
| SYNO.SurveillanceStation.SnapShot                         |
| SYNO.SurveillanceStation.VisualStation                    |
| SYNO.SurveillanceStation.VisualStation.Layout             |
| SYNO.SurveillanceStation.VisualStation.Search             |
| SYNO.SurveillanceStation.AxisAcsCtrler                    |
| SYNO.SurveillanceStation.AxisAcsCtrler.Search             |
| SYNO.SurveillanceStation.DigitalOutput                    |
| SYNO.SurveillanceStation.ExternalEvent                    |
| SYNO.SurveillanceStation.IOModule                         |
| SYNO.SurveillanceStation.IOModuleSearch                   |
| SYNO.SurveillanceStation.Camera.Status                    |
| SYNO.SurveillanceStation.PTZ.Preset                       |
| SYNO.SurveillanceStation.PTZ.Patrol.                      |
| SYNO.SurveillanceStation.Camera.Search                    |
| SYNO.SurveillanceStation.HomeMode                         |
| SYNO.SurveillanceStation.Transactions.Device              |
| SYNO.SurveillanceStation.Transactions.Transaction         |
| SYNO.SurveillanceStation.Archiving.Pull                   |
| SYNO.SurveillanceStation.YoutubeLive                      |
| SYNO.SurveillanceStation.IVA                              |
| SYNO.SurveillanceStation.IVA.Report                       |
| SYNO.SurveillanceStation.IVA.Recording                    |
| SYNO.SurveillanceStation.IVA.TaskGroup                    |
| SYNO.SurveillanceStation.Face                             |
| SYNO.SurveillanceStation.Face.Result                      |
| SYNO.SurveillanceStation.Recording.Bookmark               |

#### FileStation Functions list

To explain the use of some function I will divide all the functions in two sets

you can run the following set of functions at your will entering just the required data,


| Function                            | Description                                                                                                              |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `get_info()`                        | Provide File Station information.                                                                                        |
| `get_list_share()`                  | List all shared folders.                                                                                                 |
| `get_file_list()`                   | Enumerate files in a given folder.                                                                                       |
| `get_file_info()`                   | Get information of file(s).                                                                                              |
| `get_mount_point_list()`            | List all mount point folders on one given type of virtual file system.                                                   |
| `get_favorite_list()`               | List user’s favorites.                                                                                                   |
| `add_a_favorite()`                  | Add a folder to user’s favorites.                                                                                        |
| `delete_a_favorite()`               | Delete a favorite in user’s favorites.                                                                                   |
| `clear_broken_favorite()`           | Delete all broken statuses of favorites.                                                                                 |
| `edit_favorite_name()`              | Edit a favorite name.                                                                                                    |
| `replace_all_favorite()`            | Replace multiple favorites of folders to the existed user’s favorites.                                                   |
| `check_permission()`                | Check if a logged-in user has write permission to create new files/folders in a given folder.                            |
| `upload_file()`                     | Upload a file to the station. (fix by @longyn)                                                                           |
| `get_shared_link_info()`            | Get information of a sharing link by the sharing link ID.                                                                |
| `get_shared_link_list()`            | List user’s file sharing links.                                                                                          |
| `create_sharing_link()`             | Generate one or more sharing link(s) by file/folder path(s).                                                             |
| `delete_shared_link()`              | Delete one or more sharing links.                                                                                        |
| `clear_invalid_shared_link()`       | Remove all expired and broken sharing links.                                                                             |
| `edit_shared_link()`                | Edit sharing link(s).                                                                                                    |
| `create_folder()`                   | Create folders.                                                                                                          |
| `rename_folder()`                   | Rename a file/folder.                                                                                                    |
| `delete_blocking_function()`        | Delete files/folders. This is a blocking method. The response is not returned until the deletion operation is completed. |
| `get_file_list_of_archive()`        | List archived files contained in an archive.                                                                             |
| `get_list_of_all_background_task()` | List all background tasks including copy, move, delete, compress and extract tasks.                                      |

To run the following functions you'll have to start the task with the start function

| Function                   | Description                                                |
|----------------------------|------------------------------------------------------------|
| `search_start()`           | Search files according to given criteria.                  |
| `get_search_list()`        | List matched files in a search temporary database.         |
| `stop_search_task()`       | Stop the searching task.                                   |
| `stop_all_search_task()`   | Stop the all searching tasks.                              |
| `start_dir_size_calc()`    | Start to calculate size for one or more file/folder paths. |
| `get_dir_status()`         | Get the status of the size calculating task.               |
| `stop_dir_size_calc()`     | Stop to calculate size.                                    |
| `start_copy_move()`        | Start to copy/move files.                                  |
| `get_copy_move_status()`   | Get the copying/moving status.                             |
| `stop_copy_move_task()`    | Stop a copy/move task.                                     |
| `start_delete_task()`      | Delete file(s)/folder(s).                                  |
| `get_delete_status()`      | Get the deleting status.                                   |
| `stop_delete_task()`       | Stop a delete task.                                        |
| `start_extract_task()`     | Start to extract an archive.                               |
| `get_extract_status()`     | Get the extract task status.                               |
| `stop_extract_task()`      | Stop the extract task.                                     |
| `start_file_compression()` | Start to compress file(s)/folder(s).                       |
| `get_compress_status()`    | Get the compress task status.                              |
| `stop_compress_task()`     | Stop the compress task.                                    |
| `get_file()`               | Download or open file.                                     |

#### DownloadStations functions:

For some of DownloadStation API there is the possibility to set version 2, ex. SYNO.DownloadStation.BTSearch,
if you encounter problems you might set ```download_st_version = 2``` during initialization. 

| Function                | Description                               |
|-------------------------|-------------------------------------------|
| `get_info()`            | Download Station info.                    |
| `get_config()`          | Download Station Settings info.           |
| `set_server_config()`   | Sets Download Station settings.           |
| `schedule_info()`       | Provides advanced schedule settings info. |
| `schedule_set_config()` | Sets advanced schedule settings.          |
| `tasks_list()`          | Provides task listing.                    |
| `tasks_info()`          | Provides detailed task information.       |
| `tasks_source()`        | Provides the original torrent file.       |
| `create_task`           | Create a download task.                   |
| `delete_task()`         | Delete a Task.                            |
| `pause_task()`          | Pause a Task.                             |
| `resume_task()`         | Resume a task.                            |
| `edit_task()`           | Edit a Task.                              |


#### Photo functions:
| Function                            |
|-------------------------------------|
| `get_userinfo()`                    |
| `get_folder()`                      |
| `list_folders()`                    |
| `list_teams_folders()`              |
| `count_folders()`                   |
| `count_team_folders()`              |
| `lookup_folder()`                   |
| `lookup_team_folder()`              |
| `get_album()`                       |
| `list_albums()`                     |
| `suggest_condition()`               |
| `create_album()`                    |
| `delete_album()`                    |
| `set_album_condition()`             |
| `share_album()`                     |
| `share_team_folder()`               |
| `list_shareable_users_and_groups()` |
| `list_item_in_folders()`            |
| `list_search_filters()`             |
| `get_guest_settings()`              |



#### core_sys_info:

Although there is nothing you can set (yet), is possible to retrieve lots of 
DS info with below functions:

| Functions                         |
|-----------------------------------|
| `fileserv_smb()`                  |  
| `fileserv_afp()`                  |  
| `fileserv_nfs()`                  |  
| `fileserv_ftp()`                  |  
| `fileserv_sftp()`                 |  
| `network_backup_info()`           |  
| `bandwidth_control_protocol()`    |  
| `shared_folders_info()`           |  
| `services_status()`               |  
| `services_discovery()`            |  
| `file_transfer_status()`          |  
| `network_status()`                |  
| `web_status()`                    |  
| `current_connection()`            |
| `bandwidth_control_status()`      |
| `sys_status()`                    |
| `latest_logs()`                   |
| `client_notify_settings_status()` |
| `get_security_scan_info()`        |
| `get_security_scan_rules()`       |
| `get_security_scan_status()`      |
| `get_user_list()`                 |
| `quickconnect_info()`             |
| `quickconnect_permissions()`      |
| `network_topology()`              |
| `network_wifi_client()`           |
| `network_bond()`                  |
| `network_bridge()`                |
| `network_ethernet()`              |
| `network_local_bridge()`          |
| `network_usb_modem()`             |
| `network_pppoe()`                 |
| `network_ipv6tunnel()`            |
| `network_vpn_pptp()`              |
| `network_openvpn()`               |
| `network_vpn_l2tp()`              |
| `domain_schedule()`               |
| `client_ldap()`                   |
| `client_sso()`                    |
| `sys_upgrade_check()`             |
| `sys_upgrade_download()`          |
| `sys_upgrade_setting()`           |
| `notification_sms_conf()`         |
| `notification_mail_conf()`        |
| `notification_push_mail()`        |
| `notification_push_conf()`        |
| `hardware_beep_control()`         |
| `hardware_fan_speed()`            |
| `hardware_hibernation()`          |
| `hardware_ups()`                  |
| `hardware_power_schedule()`       |
| `terminal_info()`                 |
| `snmp_info()`                     |
| `process()`                       |
| `utilisation()`                   |
| `storage()`                       |
| `external_device_storage_usb()`   |
| `external_device_storage_esata()` |
| `file_index_resource()`           |
| `cms_info()`                      |
| `port_forwarding_rules()`         |
| `port_forwarding_router_conf()`   |
| `disk_list()`                     |
| `ddns_provider_info()`            |
| `ddns_record_info()`              |
| `ddns_external_ip()`              |
| `ddns_synology()`                 |
| `iscsi_lun_info()`                |
| `hddman()`                        |
| `ftp_security_info()`             |
| `bandwidth_control_info()`        |
| `directory_domain_info()`         |
| `ws_transfer_info()`              |
| `ref_link_copy_info()`            |
| `bonjour_service_info()`          |
| `personal_photo_enable()`         |
| `ftp_chroot_user()`               |
| `server_pair()`                   |
| `ldap_info()`                     |
| `sso_iwa_info()`                  |
| `sso_info()`                      |
| `network_interface_info()`        |
| `proxy_info()`                    |
| `gateway_list()`                  |
| `firewall_info()`                 |
| `auto_upgrade_status()`           |
| `upgrade_server_check()`          |
| `set_fan_speed()`                 |
| `enable_zram()`                   |
| `enable_power_recovery()`         |
| `enable_beep_control()`           |
| `set_led_control()`               |
| `set_hibernation()`               |
| `enable_external_ups()`           |
| `get_system_info()`               |
| `get_cpu_temp()`                  |
| `get_network_info()`              |
| `get_volume_info()`               |
| `get_all_system_utilization()`    |
| `get_cpu_utilization()`           |
| `get_disk_utilization()`          |
| `get_memory_utilization()`        |
| `dsm_info()`                      |
| `get_system_health()`                      |
| `upgrade_status()`                      |
| `groups_info()`                      |

### core_group (DSM User Groups)
| Functions                  | Description                                                     |
|----------------------------|-----------------------------------------------------------------|
| `get_groups()`             | Get all groups                                                  |
| `get_users()`              | Get group members                                               |
| `get_permissions()`        | Get group shares permissions                                    |
| `get_quota()`              | Get group shares quota                                          |
| `get_speed_limits()`       | Get group services speed limits                                 |
| `set_group_info()`         | Set group name/description                                      |
| `set_share_permissions()`  | Set group share permissions                                     |
| `set_share_quota()`        | Set group share quotas.                                         |
| `set_speed_limit()`        | Set group service speed limit                                   |
| `add_users()`              | Add users to a group                                            |
| `remove_users()`           | Remove users from a group                                       |
| `create()`                 | Create new group                                                |
| `delete()`                 | Delete specified groups                                         |

### core_user (DSM User Settings)
| Functions                  | Description                                                     |
|----------------------------|-----------------------------------------------------------------|
| `get_users()`              | Retrieve users information                                      |
| `get_user()`               | Retrieve user information                                       |
| `create_user()`            | Create a new user                                               |
| `modify_user()`            | Modify a user                                                   |
| `delete_user()`            | Delete a user                                                   |
| `affect_groups()`          | Affect or disaffect groups to a user                            |
| `affect_groups_status()`   | Get the status of a join task                                   |
| `get_password_policy()`    | Get the password policy                                         |
| `set_password_policy()`    | Set the password policy                                         |
| `get_password_expiry()`    | Get the password expiry                                         |
| `set_password_expiry()`    | Set the password expiry                                         |
| `password_confirm()`       | Confirm password match with current logged user                 |
| `get_username_policy()`    | Get the username policy (List of username that are not usable). |

### core_share Share (DSM Shared Folder Settings)
| Functions                         | Description                                                               |
|-----------------------------------|---------------------------------------------------------------------------|
| `validate_set()`                  | Validate set of parameter for a new / modified shared folder              |
| `list_folders()`                  | List all folders informations                                             |
| `get_folder()`                    | Get a folder by name                                                      |
| `create_folder()`                 | Create a new shared folder                                                |
| `delete_folders()`                | Delete folder(s) by name(s)                                               |
| `clone()`                         | Clone existing shared folder                                              |

### core_share SharePermission (DSM Shared Folder Permissions Settings)
| Functions                         | Description                                                               |
|-----------------------------------|---------------------------------------------------------------------------|
| `get_folder_permission_by_name()` | Retrieve share permissions for a given folder filtered by permission name |
| `get_folder_permissions()`        | Retrieve share permissions for a given folder                             |
| `set_folder_permissions()`        | Set folder permissions for a given folder                                 |
| `get_local_group_permissions()`   | Retrieve share permissions for a given group                              |
| `set_local_group_permissions()`   | Set group permissions for a given share                                   |
| `set_local_group_permissions()`   | Set group permissions for a given share                                   |



### Virtualization
| Functions                  |
|----------------------------|
| `get_task_list()`          |
| `clear_task()`             |
| `get_taks_info()`          |
| `get_network_group_list()` |
| `get_storage_operation()`  |
| `get_host_operation()`     |
| `get_vm_operation()`       |
| `get_specific_vm_info()`   |
| `set_vm_property()`        |
| `delete_vm()`              |
| `vm_power_on()`            |
| `vm_force_power_off()`     |
| `vm_shut_down()`           |
| `get_images_list()`        |
| `delete_image()`           |
| `create_image()`           |

### core_backup (Hyper Backup)
| Functions                  | Description                                                     |
|----------------------------|-----------------------------------------------------------------|
| `backup_repository_get()`  | Get repository information for given task.                      |
| `backup_repository_list()` | List of present repositories.                                   |
| `backup_task_list()`       | Get current restoring information and list of present tasks.    | 
| `backup_task_status()`     | Get status and state of task.                                   |
| `backup_task_get()`        | Get task information.                                           |
| `backup_task_result()`     | Get last result summary information of a task.                  |
| `backup_task_run()`        | Run task.                                                       |
| `backup_task_cancel()`     | Cancel ongoing task.                                            |
| `backup_task_suspend()`    | Suspend ongoing task.                                           |
| `backup_task_discard()`    | Discard suspended task.                                         |
| `backup_task_resume()`     | Resume suspended task.                                          |
| `backup_task_remove()`     | Remove one or more tasks.                                       |
| `integrity_check_run()`    | Run integrity check for given task.                             |
| `integrity_check_cancel()` | Cancel ongoing integrity check.                                 |
| `hb_logs_get()`            | Get Hyper Backup UI logs.                                       |

### core_backup (Hyper Backup Vault)
| Functions                       | Description                                                | 
|---------------------------------|------------------------------------------------------------|
| `vault_target_list()`           | List of all targets in Vault.                              |
| `vault_concurrency_get()`       | Get number of concurrent tasks allowed to run in HB Vault. |
| `vault_concurrency_set()`       | Set number of concurrent tasks allowed to run in HB Vault. |
| `vault_target_settings_get()`   | Get settings of target.                                    |
| `vault_task_statistics_get()`   | Get statistics from task.                                  |
| `vault_target_logs_get()`       | Get logs of specific target.                               |

### core_active_backup (Active Backup for Business)
| Functions                     | Description                                               |
|-------------------------------|-----------------------------------------------------------|
| `list_vm_hypervisor()`          | List of all configured hypervisors.                     |
| `list_device_transfer_size()`   | List of all devices and their respective transfer size. |
| `list_storage()`                | List of all storages.                                   |
| `list_logs()`                   | List of logs.                                           |
| `list_logs_details()`           | Detailed list of task logs.                             |
| `backup_task_list()`            | List of all tasks.                                      |
| `backup_task_run()`             | Run given task(s).                                      |
| `backup_task_cancel()`          | Cancel given task(s).                                   |
| `backup_task_remove()`          | Remove given task(s).                                   |
| `backup_task_delete_versions()` | Delete given version(s).                                |

### abm (Active Backup for Microsoft 365)
| Functions              | Description                                           |
|------------------------|-------------------------------------------------------|
| `get_tasks()`          | Retrieve the list of all tasks.                       |
| `get_package_log()`    | Retrieve logs related to the package.                 |
| `get_task_log()`       | Retrieve logs for a specific task.                    |
| `get_task_setting()`   | Retrieve settings for a specific task.                |
| `get_worker_count()`   | Retrieve the current worker count.                    |
| `set_worker_count()`   | Set the number of workers.                            |
| `set_task_schedule()`  | Set the schedule for a task.                          |
| `set_rotation_policy()`| Set the rotation policy for backups.                  |
| `run_backup()`         | Trigger a backup task.                                |
| `cancel_backup()`      | Cancel an ongoing backup task.                        |
| `delete_task()`        | Delete a specified task.                              |
| `relink_task()`        | Relink a specified task.                              |


### core_certificate tnx to @ajarzyn
| Functions            | Description              |
|----------------------|--------------------------|
| `list_cert()`        | List certificates.       |
| `set_default_cert()` | Set default certificate. |
| `upload_cert()`      | Upload a certificate.    |

### vpn
| Functions                      |
|--------------------------------|
| `settings_list()`              |
| `active_connections_list()`    |
| `log_list()`                   |
| `network_interface_setting()`  |
| `security_autoblock_setting()` |
| `permission_setting()`         |
| `pptp_settings_info()`         |
| `openvpn_settings_info()`      |
| `l2tp_settings_info()`         |

### oauth
| Functions   |
|-------------|
| `clients()` | 
| `tokens()`  | 
| `logs()`    | 


### security_advisor
| Functions          | 
|--------------------|
| `general_info()`   | 
| `security_scan()`  | 
| `checklist()`      | 
| `login_activity()` | 
| `advisor_config()` | 
| `scan_config()`    | 


### dhcp_server
| Functions             | 
|-----------------------|
| `general_info()`      | 
| `vendor()`            | 
| `pxe()`               | 
| `tftp()`              | 
| `network_bond()`      | 
| `network_ethernet()`  | 
| `dhcp_clientlist()`   | 
| `dhcp_reservations()` | 


### usb_copy 
| Functions                | 
|--------------------------|
| `get_package_settings()` | 
| `get_package_logs()`     | 
| `get_task_settings()`    | 
| `toggle_task()`          | 

### log_center
| Functions                | 
|--------------------------|
| `logcenter()`            | 
| `client_status_cnt()`    | 
| `client_status_eps()`    | 
| `remote_log_archives()`  |
| `display_logs()`         | 
| `setting_storage_list()` | 
| `registry_send_list()`   | 
| `history()`              | 

### snapshot (Snapshot Replication)
| Functions             | 
|-----------------------|
| `list_snapshots()`    | 
| `create_snapshot()`   | 
| `delete_snapshots()`  | 
| `set_snapshot_attr()` |

### cloud_sync (Cloud Sync)
| Functions                      | Description                                                    |
|--------------------------------|----------------------------------------------------------------|
| `get_pkg_config()`             | Retrieve the package configuration.                            |
| `get_connections()`            | Get connection details.                                        |
| `get_connection_settings()`    | Get settings for a specific connection.                        |
| `get_connection_information()` | Get cloud information for a specific connection.               |
| `get_connection_auth()`        | Retrieve authentication details for a connection.              |
| `get_connection_logs()`        | Retrieve logs for a specific connection.                       |
| `get_tasks()`                  | Get tasks associated with a specific connection.               |
| `get_task_filters()`           | Retrieve filters applied to tasks for a specific session.      |
| `get_task_cloud_folders()`     | Retrieve cloud folders associated with tasks.                  |
| `get_recently_modified()`      | Retrieve recently modified resources.                          |
| `set_pkg_config()`             | Set or update the package configuration.                       |
| `set_relink_behavior()`        | Set behavior for relinking tasks.                              |
| `set_connection_settings()`    | Set or update settings for a connection.                       |
| `set_connection_schedule()`    | Define or update the schedule for a connection.                |
| `set_task_settings()`          | Update task settings.                                          |
| `set_task_filters()`           | Apply or modify filters to tasks.                              |
| `connection_pause()`           | Pause a specific or all connections.                           |
| `connection_resume()`          | Resume a paused or all connections.                            |
| `connection_remove()`          | Remove a specific connection.                                  |
| `create_sync_task_s3()`        | Add new task to connection(Only S3 tested).                    |
| `test_task_setting()`          | Test a task configuration before adding it.                    |
| `task_remove()`                | Remove a specific task.                                        |

### task_scheduler
| Functions                       | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| `get_output_config()`           | Retrieve the task output configuration.                        |
| `get_task_list()`               | Retrieve list of Scheduled and Event tasks.                    |
| `get_task_config()`             | Get Scheduled task settings.                                   |
| `get_task_results()`            | Get results of a Scheduled task.                               |
| `set_output_config()`           | Set the task output configuration.                             |
| `task_set_enable()`             | Enable or disable a Scheduled task.                            |
| `task_run()`                    | Run a Scheduled task.                                          |
| `task_delete()`                 | Delete a Scheduled task.                                       |
| `create_script_task()`          | Create a "User defined script scheduled task".                 |
| `modify_script_task()`          | Modify a "User defined script scheduled task".                 |
| `create_beep_control_task()`    | Create a "Beep control scheduled task".                        |
| `modify_beep_control_task()`    | Modify a "Beep control scheduled task".                        |
| `create_service_control_task()` | Create a "Service scheduled task".                             |
| `modify_service_control_task()` | Modify a "Service scheduled task".                             |
| `create_recycle_bin_task()`     | Create a "Recycle Bin scheduled task".                         |
| `modify_recycle_bin_task()`     | Modify a "Recycle Bin scheduled task".                         |

### event_scheduler
| Functions                      | Description                                                    |
|--------------------------------|----------------------------------------------------------------|
| `get_task_results()`           | Get results of a Event Triggered task.                         |
| `get_result_output()`          | Get the output for a given result.                             |
| `task_set_enable()`            | Enable or disable a Event Triggered task.                      |
| `task_run()`                   | Run a Event Triggered task.                                    |
| `task_delete()`                | Delete a Event Triggered task.                                 |
| `task_create_or_set()`         | Create or modify a Event Triggered task.                       |
 
#### What's still missing

There is still few missing function for the api supplied from Synology which is a work in progress:

| Missing in FileStation |
|------------------------|
| SYNO.FileStation.Thumb |  

| Missing in Virtualization            |
|--------------------------------------|
| SYNO.Virtualization.API.Guest create |

### Bugs

Maybe? 

I hate bugs..

well report them please (if you'll ever use this code)

### Conclusions

There is still a lot to implement.

The code is probably in some parts twisted, I will try to optimize it at best

### Contributing

Just Don't Be Scared

## Author

- Renato Visaggio - _Initial_ _Work_ - [N4S4](https://github.com/N4S4)

## Contributors

- List of contributors here_ - [Contributors](https://github.com/N4S4/synology-api/graphs/contributors)

