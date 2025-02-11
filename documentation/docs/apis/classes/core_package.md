---
sidebar_position: 20
title: 🚧 Package
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Package
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Package API implementation.
## Methods
### `get_package`
Get infos of a package  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_package_id_** `str`  
Package ID  
  
**_additional_** `List[str]`  
Additional field to retrieves. Defaults to `[]`
All filed known are:
`["status","dsm_apps"]`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Informations about the package  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "additional": {
            "dsm_apps": " com.plexapp.plexmediaserver",
            "status": "running",
            "status_code": 0,
            "status_description": "retrieve from status script",
            "status_origin": "running"
        },
        "id": "PlexMediaServer",
        "name": "Plex Media Server",
        "timestamp": 1739228562839,
        "version": "1.41.3.9314-72009314"
    },
    "success": true
}
```
</details>



---


### `list_installed`
List installed packages  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_** `list[str]`  
Additional fields to retrieve. Defaults to `[]`.
All fields known are: 
    `["description", "description_enu", "dependent_packages", "beta", "distributor", "distributor_url",
    "maintainer", "maintainer_url", "dsm_apps", "dsm_app_page", "dsm_app_launch_name","report_beta_url",
    "support_center", "startable", "installed_info", "support_url", "is_uninstall_pages","install_type",
    "autoupdate", "silent_upgrade", "installing_progress", "ctl_uninstall", "updated_at", "status",
    "url","available_operation"]`.  
  
**_ignore_hidden_** `bool`  
TODO: Write description  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of packages installed on the NAS  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "packages": [
            {
                "additional": {
                    "install_type": ""
                },
                "id": "ActiveBackup-Office365",
                "name": "Active Backup for Microsoft 365",
                "timestamp": 1738880043640,
                "version": "2.5.5-14034"
            }
        ]
    },
    "success": true
}
```
</details>



---


### `list_installable`
List installable packages  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Server` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of beta_package, categories and packages available  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "banners": [],
        "beta_packages": [...],
        "categories": [...],
        "packages": [...]
    },
    "success": true
}
```
</details>



---


### `get_package_center_settings`
Get package center settings  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Setting` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List settings of the Package center  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "autoupdateall": false,
        "autoupdateimportant": true,
        "default_vol": "/volume1",
        "enable_autoupdate": true,
        "enable_dsm": true,
        "enable_email": false,
        "mailset": true,
        "trust_level": 0,
        "update_channel": true,
        "volume_count": 2,
        "volume_list": [
            {
                "desc": "",
                "display": "Volume 1 (Available capacity:  184.72 GB )",
                "mount_point": "/volume1",
                "size_free": "198336327680",
                "size_total": "206158430208",
                "vol_desc": "Apps",
                "volume_features": []
            },
            {
                "desc": "",
                "display": "Volume 2 (Available capacity:  2391.14 GB )",
                "mount_point": "/volume2",
                "size_free": "2567467421696",
                "size_total": "3623234412544",
                "vol_desc": "Stockage",
                "volume_features": []
            }
        ]
    },
    "success": true
}
```
</details>



---


### `set_package_center_settings`
Set settings of the package center  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Setting` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_email_** `bool`  
Enable email notification  
  
**_enable_dsm_** `bool `  
Enable desktop notification  
  
**_enable_autoupdate_** `bool`  
Update packages automatically  
  
**_autoupdateall_** `bool`  
Auto update all packages  
  
**_autoupdateimportant_** `bool`  
Auto update "important" packages  
  
**_default_vol_** `str`  
Default volume for installation, all your volumes or `"no_default_vol" = Always ask me`  
  
**_udpate_channel_** `str`  
"stable" => Disable beta packages
"beta" => Enable beta packages  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Return some settings  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "enable_dsm": true,
        "enable_email": false,
        "update_channel": "stable"
    },
    "success": true
}
```
</details>



---


### `get_package_center_infos`
Get package center informations  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
List of configs  

</div>



---


### `feasibility_check_install`
Check if installation is possible  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Setting` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_packages_** `List[str]`  
List of package IDs to check for feasibility  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
_description_  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "template": "data"
    },
    "success": true
}
```
</details>



---


### `download_package`
Start download of the package, return a taskId for check status  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_url_** `str`  
Url that can be retrieve from package info using `get_installable` function, in the `link` field  
  
**_package_id_** `str`  
Package ID that can be retrieve from package info using `get_installable` function, in the `id` field  
  
**_checksum_** `str`  
Checksum that can be retrieve from package info using `get_installable` function, in the `md5` field  
  
**_filesize_** `str`  
Filesize that can be retrieve from package info using `get_installable` function, in the `size` field  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Retreive first progress of the download and the taskid used to check download status with `get_dowload_package_status` function  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "progress": 1.0000000000000001e-05,
        "taskid": "@SYNOPKG_DOWNLOAD_DhcpServer"
    },
    "success": true
}
```
</details>



---


### `get_dowload_package_status`
Get current download status of the package  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
task ID retrieve from response of `download_package` function  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Retrieve informations about the download, important info is the `progress` field  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "beta": false,
        "blqinst": false,
        "finished": false,
        "id": "DhcpServer",
        "installing": false,
        "name": "DhcpServer",
        "pid": 27844,
        "progress": 1.0000000000000001e-05,
        "remote_link": "https://global.synologydownload.com/download/Package/spk/DhcpServer/1.0.2-0046/DhcpServer-x86_64-1.0.2-0046.spk",
        "size": "1378697",
        "success": true,
        "taskid": "@SYNOPKG_DOWNLOAD_DhcpServer",
        "tmp_folder": "/volume1/@tmp/synopkg/download.esnnkb"
    },
    "success": true
}
```
</details>



---


### `check_installation_from_download`
Get info about downloaded package file, response field is used for `check_installation` and `install_package` function  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation.Download` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_task_id_** `str`  
task ID retrieve from response of `download_package` function  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Retrieve information about downloaded package installation file, response field is used for `check_installation` and `install_package` function  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "description": "DHCP Server turns your DiskStation into a DHCP server within LAN to assign dynamic IP addresses and manage DHCP clients.",
        "distributor": "",
        "dsm_apps": "SYNO.SDS.DHCP.Instance",
        "filename": "/volume1/@tmp/synopkg/download.esnnkb/@SYNOPKG_DOWNLOAD_DhcpServer",
        "id": "DhcpServer",
        "install_on_cold_storage": false,
        "install_reboot": false,
        "install_type": "system",
        "maintainer": "Synology Inc.",
        "name": "DHCP Server",
        "startable": true,
        "status": "non_installed",
        "status_code": 255,
        "status_description": "failed to locate given package",
        "status_origin": "non_installed",
        "version": "1.0.2-0046"
    },
    "success": true
}
```
</details>



---


### `upload_package_file`
Upload a file for install a package  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_file_path_** `str`  
File path  
  
**_verify_** `bool`  
Use https. Defaults to `False`  
  
**_progress_bar_** `bool`  
Enable progress bar in the terminal. Defaults to `True`  
  
**_additional_** `list`  
Additional field to retrieves. Defaults to `[]`
All fields know are:
`["description","maintainer","distributor","startable","dsm_apps","status","install_reboot",
"install_type","install_on_cold_storage","break_pkgs","replace_pkgs"]`.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Informations about the uploaded file for installation  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "additional": {
            "break_pkgs": null,
            "description": "Plex organizes all of your personal media so you can easily access and enjoy it.",
            "distributor": "",
            "dsm_apps": " com.plexapp.plexmediaserver",
            "install_on_cold_storage": false,
            "install_reboot": false,
            "install_type": "",
            "maintainer": "Plex Inc",
            "replace_pkgs": { "Plex Media Server": "" },
            "startable": true,
            "status": "running",
            "status_code": 0,
            "status_description": "retrieve from status script",
            "status_origin": "running"
        },
        "codesign_error": 4532,
        "id": "PlexMediaServer",
        "name": "Plex Media Server",
        "task_id": "@SYNOPKG_UPLOAD_17392283048566DD3",
        "version": "1.41.3.9314-72009314"
    },
    "success": true
}
```
</details>



---


### `get_default_install_volume`
Get default install volume for package  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Setting.Volume` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict`  
Return default volume, if default volume is set to `Always ask me` it return error 4501  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "default_vol": "/volume1"
    },
    "success": true
}
```
</details>



---


### `check_installation`
Check installation of the package on the default volume  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_package_id_** `str`  
Id of the package to install  
  
**_install_type_** `str, optionnal`  
Installation type, Defaults to `""`. TODO: Add description and possible types  
  
**_install_on_cold_storage_** `bool`  
Defaults to `False`. TODO: Add description  
  
**_blCheckDep_** `bool`  
Defaults to `False`. TODO: Add description  
  
**_replacepkgs_** `dict`  
Defaults to `{}`. TODO: Add description  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
List of usefull informations about volumes  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "is_occupied": false,
        "volume_count": 2,
        "volume_list": [
            {
                "desc": "",
                "display": "Volume 1 (Available capacity:  184.52 GB )",
                "mount_point": "/volume1",
                "size_free": "198126022656",
                "size_total": "206158430208",
                "vol_desc": "vol1",
                "volume_features": []
            },
            {
                "desc": "",
                "display": "Volume 2 (Available capacity:  2391.16 GB )",
                "mount_point": "/volume2",
                "size_free": "2567484923904",
                "size_total": "3623234412544",
                "vol_desc": "vol2",
                "volume_features": []
            }
        ],
        "volume_path": "/volume1"
    },
    "success": true,
}
```
</details>



---


### `upgrade_package`
Upgrade an existing package  
Parameters
            ----------
            task_id : str
                Task id of the download or the upload file
            check_codesign : bool, optional
                Check signature of the source code of the package (is it a Synology one). Defaults to `False`
            force : bool, optional
                Force installation. Defaults to `False`
            installrunpackage : bool, optional
                Run package after installation. Defaults to `True`
            extra_values : dict, optional
                Extra values due to some package installation. Defaults to `{}`
                All known extra values are:
                - Surveillance station
                ```json
                    {
                        "chkSVS_Alias": true,
                        "strSVS_Alias": "cam",
                        "chkSVS_HTTP": true,
                        "strSVS_HTTP": "9900",
                        "chkSVS_HTTPS": true,
                        "strSVS_HTTPS": "9901"
                    }
                ```
        
            Returns
            -------
            dict
                Message and some info about installation
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "message": "<br><strong><p style='color:blue'><big><b>Installation Successful!</big></p>
<br><p style='color:blue'>:::note
 
 If Plex cannot access your media, verify user <strong>PlexMediaServer</strong> is granted permission in <strong>Control Panel</strong>.</p><br>
 
:::

Set access to your media share(s) by performing the following steps:<br><br>
1. Open <strong>Control Panel</strong> and select <strong>Shared Folder</strong><br>
2. Select the share which contains your media and click <strong>Edit</strong><br>
3. Click the <strong>Permissions</strong> tab<br>
4. Change the dropdown from <strong>Local Users</strong> to <strong>System internal user</strong><br>
5. Check the <strong>Read/Write</strong> checkbox for the <strong>PlexMediaServer</strong> user<br>
6. Click <strong>Save</strong> to confirm the new permissions<br>
7. Repeat steps 2-6 for each share you want Plex Media Server to access<br>
",
                    "packageName": "Plex Media Server",
                    "worker_message": []
                },
                "success": true,
            }
            ```  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Installation` 
</div>
  



---


### `install_package`
Install a package that is already downloaded  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Uninstallation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_package_id_** `str`  
Id of the package to install  
  
**_volume_path_** `str`  
Volume path of the installation, can get from `check_installation` function  
  
**_file_path_** `str`  
File path of the installation, can get from `check_installation_from_download` function  
  
**_check_codesign_** `bool`  
Check signature of the source code of the package (is it a Synology one). Defaults to `False`  
  
**_force_** `bool`  
Force installation. Defaults to `False`  
  
**_installrunpackage_** `bool`  
Run package after installation. Defaults to `True`  
  
**_extra_values_** `dict`  
Extra values due to some package installation. Defaults to `{}`
All known extra values are:
- Surveillance station
```json
    {
        "chkSVS_Alias": true,
        "strSVS_Alias": "cam",
        "chkSVS_HTTP": true,
        "strSVS_HTTP": "9900",
        "chkSVS_HTTPS": true,
        "strSVS_HTTPS": "9901"
    }
```  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Message and some info about installation  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
            {
                "api": "SYNO.Core.Package.Installation",
                "data": {
                    "is_occupied": false,
                    "volume_count": 2,
                    "volume_list": [
                        {
                            "desc": "",
                            "display": "Volume 1 (Available capacity:  185.09 GB )",
                            "mount_point": "/volume1",
                            "size_free": "198739943424",
                            "size_total": "206158430208",
                            "vol_desc": "Apps",
                            "volume_features": []
                        },
                        {
                            "desc": "",
                            "display": "Volume 2 (Available capacity:  2391.17 GB )",
                            "mount_point": "/volume2",
                            "size_free": "2567495630848",
                            "size_total": "3623234412544",
                            "vol_desc": "Stockage",
                            "volume_features": []
                        }
                    ],
                    "volume_path": "/volume1"
                },
                "method": "check",
                "success": true,
                "version": 1
            },
            {
                "api": "SYNO.Core.Package.Installation",
                "data": {
                    "packageName": "Text Editor",
                    "worker_message": []
                },
                "method": "install",
                "success": true,
                "version": 1
            }
        ]
    },
    "success": true
}
```
</details>



---


### `uninstall_package`
Uninstall a package  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package.Uninstallation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_package_id_** `str`  
Id of the package to uninstall  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Possible message to the user  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "message": "",
        "worker_message": []
    },
    "success": true
}
```
</details>



---


### `easy_install`
Execute an "easy" installation process of the package  
  
  
#### Parameters
<div class="padding-left--md">
**_package_id_** `str`  
Package ID to install  
  
**_volume_path_** `str`  
Volume path where you want to install the package  
  
**_install_dependencies_** `bool`  
If you want to install dependencies. Defaults to `True`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict`  
Information about installation, same as `install_package` function  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
{
    "data": {
        "has_fail": false,
        "result": [
            {
                "api": "SYNO.Core.Package.Installation",
                "data": {
                    "is_occupied": false,
                    "volume_count": 2,
                    "volume_list": [
                        {
                            "desc": "",
                            "display": "Volume 1 (Available capacity:  185.11 GB )",
                            "mount_point": "/volume1",
                            "size_free": "198759485440",
                            "size_total": "206158430208",
                            "vol_desc": "Apps",
                            "volume_features": []
                        },
                        {
                            "desc": "",
                            "display": "Volume 2 (Available capacity:  2391.17 GB )",
                            "mount_point": "/volume2",
                            "size_free": "2567495565312",
                            "size_total": "3623234412544",
                            "vol_desc": "Stockage",
                            "volume_features": []
                        }
                    ],
                    "volume_path": "/volume1"
                },
                "method": "check",
                "success": true,
                "version": 1
            },
            {
                "api": "SYNO.Core.Package.Installation",
                "data": {
                    "packageName": "Text Editor",
                    "worker_message": []
                },
                "method": "install",
                "success": true,
                "version": 1
            }
        ]
    },
    "success": true
}
```
</details>



---


