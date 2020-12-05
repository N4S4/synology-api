![synology-api](https://user-images.githubusercontent.com/33936751/100731387-99fffc00-33cb-11eb-833c-b6ab87177651.jpg)

# Synology Wrapper

If you find yourself on this page,
most probably you are trying to develop something for your NAS,

this wrapper might come to your help to build your script.

I would like to specify that **I am Not** a programmer as I do it all
for hobby as is my passion and in my **little** free time.

Said this you will find many things can be simplified and I slowly will.
 
## Feeling kind?
If this code helps and you wish to support me 
- Paypal: https://paypal.me/ren4s4


## SOMETHING GOING ON IN OUR MINDS

I am working on a major update which will change how the wrapper works on the backstage, 
improvements in responses speed and less resources used on your NAS. 
I am trying to keep functions name in the same way so you wont have many (or at all ) issues if you were using it before.
Both branches will be kept active and updated with latest functionalities (I'll try my best at least)

### Which one should you download? 
If you wish to have a stable one I'd suggest to download the master branch.

If you are looking for troubles or just to help me to develop the improving-code branch than download that, as it is written in a more "pythonic" way,
the improving-code is still in development (and not sure if will ever be stable as it has more complicated code, which means time consuming)

You can find the active branch, on this page, named 'Improving-code'.
If you wish to help just don't be shy and let me know!
 
 
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
# it will login automatically 

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password')

fl.get_info()

dwn = downloadstation.DownloadStation('Synology Ip', 'Synology Port', 'Username', 'Password')

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

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=True, cert_verify=True)

```

the ```secure=True``` variable is needed to be set to true if https is required; default value is ```False``` <br />
the ```cert_verify=True```  is optional, if you want to verify your certificate set it to ```True```; default value is ```False```


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

| sys_info |
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

| Backup |
| ------ |
| SYNO.Backup.Repository |
| SYNO.Backup.Task |

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
| upload_file() | upload a file to the station |
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
| get_file() | Download or open file by [kidburglar](https://github.com/kidburglar) |

#### DownloadStations functions are:

| Function | Description |
| --- | --- |
| get_info()  | Download Station info  |
| get_config()  | Download Station Settings info  |
| set_server_config()  | Sets Download Station settings  |
| schedule_info()  | Provides advanced schedule settings info  |
| schedule_set_config()  | Sets advanced schedule settings.  |
| tasks_list()  | Provides task listing  |
| tasks_info()  | Provides detailed task information  |
| delete_task()  | Delete a Task  |
| pause_task()  | Pause a Task  |
| resume_task()  | Resume a task  |
| edit_task()  | Edit a Task  |

#### sys_info 

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
| network_openvpn_with_conf() |
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

### Backup

| Functions |  
| --- | 
| backup_repository_get() |
| backup_repository_list() |
| backup_task_list |
| backup_task_status |
| backup_task_get |


#### What's still missing

There is still few missing function which is a work in progress:

| Missing in FileStation |
|----------------------|
| SYNO.FileStation.Thumb  |  

| Missing in DownloadStation |
|---|
| SYNO.DownloadStation.Task create |

| Missing in Virtualization |
|---|
| SYNO.Virtualization.API.Guest create |

### Bugs

Maybe? 

I hate bugs..

well report them please (if you'll ever use this code)

### Conclusions

There is still a lot to implement.

The code is probably is some parts twisted and I will try to optimize it at best

### Contributing

Just Don't Be Scared

## Groups to Ask Discuss Request and Improve the code

- Telegram [Synology Api](https://t.me/SynologyApi) Preferred
- Slack [Synology Api](https://bit.ly/SynologyApi)


## Authors

- Renato Visaggio - _Initial_ _Work_ - [N4S4](https://github.com/N4S4)





