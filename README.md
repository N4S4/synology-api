
![synology-api](https://user-images.githubusercontent.com/33936751/100731387-99fffc00-33cb-11eb-833c-b6ab87177651.jpg)

# Synology Wrapper

If you find yourself on this page,
most probably you are trying to develop something for your NAS,

this wrapper might come to your help to build your script.

I would like to specify that **I am Not** a programmer as I do it all
for hobby as is my passion and in my **little** free time.

Said this you will find many things can be simplified, and I slowly will.
 
## Feeling kind?
If this code helps and you wish to support me 
- Paypal: https://paypal.me/ren4s4

## Groups to Ask Discuss Request and Improve the code

- Telegram [Synology Api](https://t.me/SynologyApi) Preferred


## Something worth to read

[Contributing](https://github.com/N4S4/synology-api/blob/master/CONTRIBUTING.md),
[Code of Conduct](https://github.com/N4S4/synology-api/blob/master/CODE_OF_CONDUCT.md)

## Premise

I've tried this wrapper only with python3 
I do not know if it actually runs with previous versions 

## Prerequisites

Prior to install this wrapper you will need to install requests library.

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

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

fl.get_info()

dwn = downloadstation.DownloadStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

dwn.get_info()

```

response would be json data

```json 
{'data': {'enable_list_usergrp': False,
  'hostname': 'MyCloud',
  'is_manager': True,
  'items': [{'gid': 100}, {'gid': 101}],
  'support_file_request': True,
  'support_sharing': True,
  'support_vfs': True,
  'support_virtual': {'enable_iso_mount': True, 'enable_remote_mount': True},
  'support_virtual_protocol': ['cifs', 'nfs', 'iso'],
  'system_codepage': 'enu',
  'uid': 1026},
 'success': True}
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

| DownloadStation  | 
| ------------- | 
| SYNO.DownloadStation.Info  | 
| SYNO.DownloadStation.Schedule  | 
| SYNO.DownloadStation.Task  | 

| FileStation   |
| ------------- | 
| SYNO.FileStation.Info | 
| SYNO.FileStation.List | 
| SYNO.FileStation.Search | 
| SYNO.FileStation.VirtualFolder | 
| SYNO.FileStation.Favorite | 
| SYNO.FileStation.DirSize | 
| SYNO.FileStation.CheckPermission | 
| SYNO.FileStation.Upload | 
| SYNO.FileStation.Sharing | 
| SYNO.FileStation.CreateFolder | 
| SYNO.FileStation.Rename | 
| SYNO.FileStation.CopyMove | 
| SYNO.FileStation.Delete | 
| SYNO.FileStation.Extract | 
| SYNO.FileStation.Compress | 
| SYNO.FileStation.BackgroundTask | 

| Photo |
| -------- |
|SYNO.Foto.UserInfo|
|SYNO.Foto.Browse.Folder|
|SYNO.FotoTeam.Browse.Folder|
|SYNO.Foto.Browse.Album|
|SYNO.Foto.Browse.ConditionAlbum|
|SYNO.Foto.Sharing.Passphrase|
|SYNO.FotoTeam.Sharing.Passphrase|
|SYNO.Foto.Sharing.Misc|

| core_sys_info |
| -------- |
| SYNO.Core.System |
| SYNO.Core.FileServ.SMB |
| SYNO.Core.FileServ.AFP |
| SYNO.Core.FileServ.NFS' |
| SYNO.Core.FileServ.FTP |
| SYNO.Core.FileServ.FTP.SFTP |
| SYNO.Backup.Service.NetworkBackup |
| SYNO.Core.BandwidthControl.Protocol |
| SYNO.Core.Share |
| SYNO.Core.FileServ.ServiceDiscovery |
| SYNO.Core.SyslogClient.FileTransfer |
| SYNO.Core.Network |
| SYNO.Core.Web.DSM |
| SYNO.Core.CurrentConnection |
| SYNO.Core.BandwidthControl.Status |
| SYNO.Core.System.Status |
| SYNO.Core.SyslogClient.Status |
| SYNO.Core.SyslogClient.Setting.Notify |
| SYNO.Core.SecurityScan.Conf |
| SYNO.Core.SecurityScan.Status |
| SYNO.Core.SecurityScan.Status |
| SYNO.Core.User |
| SYNO.Core.QuickConnect |
| SYNO.Core.QuickConnect.Permission |
| SYNO.Core.Network.Router.Topology |
| SYNO.Core.Network.Wifi.Client |
| SYNO.Core.Network.Bond |
| SYNO.Core.Network.Bridge |
| SYNO.Core.Network.Ethernet |
| SYNO.Core.Network.LocalBridge |
| SYNO.Core.Network.USBModem |
| SYNO.Core.Network.PPPoE |
| SYNO.Core.Network.IPv6Tunnel |
| SYNO.Core.Network.VPN.PPTP |
| SYNO.Core.Network.VPN.OpenVPNWithConf |
| SYNO.Core.Network.VPN.OpenVPN |
| SYNO.Core.Network.VPN.L2TP |
| SYNO.Core.Directory.Domain.Schedule |
| SYNO.Core.Directory.LDAP |
| SYNO.Core.Directory.SSO |
| SYNO.Core.Upgrade.Server |
| SYNO.Core.Upgrade.Server.Download |
| SYNO.Core.Upgrade.Setting |
| SYNO.Core.Notification.SMS.Conf |
| SYNO.Core.Notification.Mail.Conf |
| SYNO.Core.Notification.Push.Mail |
| SYNO.Core.Notification.Push.Conf |
| SYNO.Core.Hardware.BeepControl |
| SYNO.Core.Hardware.FanSpeed |
| SYNO.Core.Hardware.Hibernation |
| SYNO.Core.ExternalDevice.UPS |
| SYNO.Core.Hardware.PowerSchedule |
| SYNO.Core.Terminal |
| SYNO.Core.SNMP |
| SYNO.Core.System.Process |
| SYNO.Core.System.Utilization |
| SYNO.Storage.CGI.Storage |

| Virtualization |
| -------------- |
| SYNO.Virtualization.API.Task.Info |
| SYNO.Virtualization.API.Network |
| SYNO.Virtualization.API.Storage |
| SYNO.Virtualization.API.Host |
| SYNO.Virtualization.API.Guest |
| SYNO.Virtualization.API.Guest.Action |
| SYNO.Virtualization.API.Guest.Image |

| core_backup |
| ------ |
| SYNO.Backup.Repository |
| SYNO.Backup.Task |

| core_active_backup (Active Backup for Business) |
| ------ |
| SYNO.ActiveBackup.Inventory |
| SYNO.ActiveBackup.Overview |

#### FileStation Functions list

To explain the use of some function I will divide all the functions in two sets

you can run the following set of functions at your will entering just the required data,


| Function | Description |
| --- | --- |
| get_info() | Provide File Station information |
| get_list_share() | List all shared folders.  |
| get_file_list() | Enumerate files in a given folder  |
| get_file_info() | Get information of file(s)  |
| get_mount_point_list()  | List all mount point folders on one given type of virtual file system  |
| get_favorite_list()  | List user’s favorites  |
| add_a_favorite()  | Add a folder to user’s favorites  |
| delete_a_favorite() | Delete a favorite in user’s favorites.  |
| clear_broken_favorite()  | Delete all broken statuses of favorites.  |
| edit_favorite_name() | Edit a favorite name  |
| replace_all_favorite() | Replace multiple favorites of folders to the existed user’s favorites.  |
| check_permission() | Check if a logged-in user has write permission to create new files/folders in a given folder  |
| upload_file() | upload a file to the station (fix by @longyn) |
| get_shared_link_info() | Get information of a sharing link by the sharing link ID  |
| get_shared_link_list() | List user’s file sharing links.  |
| create_sharing_link() | Generate one or more sharing link(s) by file/folder path(s)  |
| delete_shared_link() | Delete one or more sharing links.  |
| clear_invalid_shared_link() | Remove all expired and broken sharing links  |
| edit_shared_link() | Edit sharing link(s)  |
| create_folder() | Create folders.  |
| rename_folder() | Rename a file/folder  |
| delete_blocking_function() | Delete files/folders. This is a blocking method. The response is not returned until the deletion
operation is completed. |
| get_file_list_of_archive()  | List archived files contained in an archive  |
| get_list_of_all_background_task()  | List all background tasks including copy, move, delete, compress and extract tasks  |

To run the following functions you'll have to start the task with the start function

| Function | Description |
| --- | --- |
| search_start()  | Search files according to given criteria.  |
| get_search_list()  | List matched files in a search temporary database.  |
| stop_search_task() | Stop the searching task |
| stop_all_search_task() | Stop the all searching tasks |
| start_dir_size_calc() | Start to calculate size for one or more file/folder paths. |
| get_dir_status() | Get the status of the size calculating task |
| stop_dir_size_calc() | Stop to calculate size |
| start_copy_move() | Start to copy/move files |
| get_copy_move_status() | Get the copying/moving status |
| stop_copy_move_task() | Stop a copy/move task. |
| start_delete_task() | Delete file(s)/folder(s). |
| get_delete_status() | Get the deleting status |
| stop_delete_task() | Stop a delete task |
| start_extract_task() | Start to extract an archive. |
| get_extract_status() | Get the extract task status |
| stop_extract_task() | Stop the extract task |
| start_file_compression() | Start to compress file(s)/folder(s). |
| get_compress_status() | Get the compress task status |
| stop_compress_task() | Stop the compress task |
| get_file() | Download or open file |

#### DownloadStations functions:

| Function | Description |
| --- | --- |
| get_info()  | Download Station info  |
| get_config()  | Download Station Settings info  |
| set_server_config()  | Sets Download Station settings  |
| schedule_info()  | Provides advanced schedule settings info  |
| schedule_set_config()  | Sets advanced schedule settings.  |
| tasks_list()  | Provides task listing  |
| tasks_info()  | Provides detailed task information  |
| create_task  | Create a download task |
| delete_task()  | Delete a Task  |
| pause_task()  | Pause a Task  |
| resume_task()  | Resume a task  |
| edit_task()  | Edit a Task  |

#### Photo functions:

| Function |
| --- |
|get_userinfo()|
|get_folder()|
|list_folders()|
|list_teams_folders()|
|count_folders()|
|count_team_folders()|
|lookup_folder()|
|lookup_team_folder()|
|get_album()|
|list_albums()|
|suggest_condition()|
|create_album()|
|delete_album()|
|set_album_condition()|
|share_album()|
|share_team_folder()|
|list_shareable_users_and_groups()|


#### core_sys_info:

Although there is nothing you can set (yet), is possible to retrieve lots of 
DS info with below functions:

| Functions |  
| --- | 
| fileserv_smb() |  
| fileserv_afp() |  
| fileserv_nfs() |  
| fileserv_ftp() |  
| fileserv_sftp() |  
| network_backup_info() |  
| bandwidth_control_protocol() |  
| shared_folders_info() |  
| services_status() |  
| services_discovery() |  
| file_transfer_status() |  
| network_status() |  
| web_status() |  
| current_connection() |
| bandwidth_control_status() |
| sys_status() |
| latest_logs() |
| client_notify_settings_status() |
| get_security_scan_info() |
| get_security_scan_rules() |
| get_security_scan_status() |
| get_user_list() |
| quickconnect_info() |
| quickconnect_permissions() |
| network_topology() |
| network_wifi_client() |
| network_bond() |
| network_bridge() |
| network_ethernet() |
| network_local_bridge() |
| network_usb_modem() |
| network_pppoe() |
| network_ipv6tunnel() |
| network_vpn_pptp() |
| network_openvpn() |
| network_vpn_l2tp() |
| domain_schedule() |
| client_ldap() |
| client_sso() |
| sys_upgrade_check() |
| sys_upgrade_download() |
| sys_upgrade_setting() |
| notification_sms_conf() |
| notification_mail_conf() |
| notification_push_mail() |
| notification_push_conf() |
| hardware_beep_control() |
| hardware_fan_speed() |
| hardware_hibernation() |
| hardware_ups() |
| hardware_power_schedule() |
| terminal_info() |
| snmp_info() |
| process() |
| utilisation() |
| storage() |
| external_device_storage_usb() ||
| external_device_storage_esata() |
| file_index_resource() |
| cms_info() |
| port_forwarding_rules() |
| port_forwarding_router_conf |
| disk_list |
| ddns_provider_info |
| ddns_record_info |
| ddns_external_ip |
| ddns_synology |
| iscsi_lun_info |
| hddman |
|ftp_security_info|
|bandwidth_control_info|
|directory_domain_info|
|ws_transfer_info|
|ref_link_copy_info|
|bonjour_service_info|
|users_info|
|password_policy|
|password_expiry|
|personal_photo_enable|
|ftp_chroot_user|
|server_pair|
|groups_info|
|ldap_info|
|sso_iwa_info|
|sso_info|
|network_interface_info|
|proxy_info|
|gateway_list|
|firewall_info|
|auto_upgrade_status|
|upgrade_server_check|

### Virtualization

| Functions |  
| --- | 
| get_task_list() |
| clear_task() |
| get_taks_info() |
| get_network_group_list() |
| get_storage_operation() |
| get_host_operation() |
| get_vm_operation() |
| get_specific_vm_info() |
| set_vm_property() |
| delete_vm() |
| vm_power_on() |
| vm_force_power_off() |
| vm_shut_down() |
| get_images_list() |
| delete_image() |
| create_image() |

### core_backup Hyper Backup

| Functions |  
| --- | 
| backup_repository_get() |
| backup_repository_list() |
| backup_task_list |
| backup_task_status |
| backup_task_get |
| backup_task_result() |

### core_backup Hyper Backup Vault

| vault_target_list() |

### core_active_backup Active Backup for Business

| Functions | Description |
| --- | --- |
| list_vm_hypervisor() | list of all configured hypervisors |
| list_device_transfer_size() | list of all detected vms |

### core_certificate tnx to @ajarzyn

| Functions | Description |
| --- | --- |
| list_cert() | list certificates |
| set_default_cert() | set default certificate |
| upload_cert() | upload a certificate |

### vpn
| Functions | 
| --- | 
|settings_list()|
|active_connections_list()|
|log_list()|
|network_interface_setting()|
|security_autoblock_setting()|
|permission_setting()|
|pptp_settings_info()|
|openvpn_settings_info()|
|l2tp_settings_info()|

### oauth
| Functions | 
| --- |
|clients()| 
|tokens()| 
|logs()| 


### security_advisor
| Functions | 
| --- |
|general_info()| 
|security_scan()| 
|checklist()| 
|login_activity()| 
|advisor_config()| 
|scan_config()| 


### dhcp_server
| Functions | 
| --- |
|general_info()| 
|vendor()| 
|pxe()| 
|tftp()| 
|network_bond()| 
|network_ethernet()| 


### usb_copy 
| Functions | 
| --- |
|usb_copy_info()| 
|toggle_usb_copy()| 
|logs()| 
|global_settings()| 

### log_center
| Functions | 
| --- |
|logcenter()| 
|client_status_cnt()| 
|client_status_eps()| 
|remote_log_archives()|
|display_logs()| 
|setting_storage_list()| 
|registry_send_list()| 
|history()| 

 
#### What's still missing

There is still few missing function for the api supplied from Synology which is a work in progress:

| Missing in FileStation |
|----------------------|
| SYNO.FileStation.Thumb  |  

| Missing in Virtualization |
|---|
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

