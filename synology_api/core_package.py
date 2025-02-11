import json
from typing import List
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import os, requests, tqdm, time
from . import base_api

class Package(base_api.BaseApi):
    """
    Core Package API implementation.
    """
    
    def get_package(self, package_id: str, additional: List[str] = []) -> dict:
        """Get infos of a package
        
            Parameters
            ----------
            package_id : str
                Package ID
            additional : List[str], optional
                Additional field to retrieves. Defaults to `[]`
                All filed known are:
                `["status","dsm_apps"]`
        
            Returns
            -------
            dict
                Informations about the package
        
            Example return
            ----------
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
        """
        api_name = 'SYNO.Core.Package'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "get",
            "version": info['minVersion'],
            "id": package_id,
            "additional": json.dumps(additional)
        }
        return self.request_data(api_name, api_path, req_param)
    
    def list_installed(self, additional: list = [], ignore_hidden: bool = False) -> dict:
        """List installed packages
            Parameters
            ----------
            additional : list[str], optional
                    Additional fields to retrieve. Defaults to `[]`.
                    All fields known are: 
                        `["description", "description_enu", "dependent_packages", "beta", "distributor", "distributor_url",
                        "maintainer", "maintainer_url", "dsm_apps", "dsm_app_page", "dsm_app_launch_name","report_beta_url",
                        "support_center", "startable", "installed_info", "support_url", "is_uninstall_pages","install_type",
                        "autoupdate", "silent_upgrade", "installing_progress", "ctl_uninstall", "updated_at", "status",
                        "url","available_operation"]`.
            ignore_hidden : bool
                TODO: Write description
                    
            Returns
            -------
            dict
                List of packages installed on the NAS

            Example return
            --------------
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
        """
        api_name = 'SYNO.Core.Package'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "list",
            "version": info['maxVersion'],
            "ignore_hidden": ignore_hidden,
            "additional": json.dumps(additional)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_installable(self) -> dict:
        """List installable packages
            Returns
            -------
            dict
                List of beta_package, categories and packages available
                    
            Example return
            --------------
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
        """
        api_name = 'SYNO.Core.Package.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "list",
            "version": info['maxVersion'],
            "blforcereload": False,
            "blloadothers": False
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def get_package_center_settings(self) -> dict:
        """Get package center settings
            Returns
            -------
            dict
                List settings of the Package center
                
            Example return
            --------------
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
        """
        api_name = 'SYNO.Core.Package.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "get",
            "version": info['maxVersion'],
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def set_package_center_settings(self, 
                        enable_email: bool, enable_dsm: bool, enable_autoupdate: bool,
                        autoupdateall: bool, autoupdateimportant: bool,
                        default_vol: str, update_channel: str
            ) -> dict:
        """Set settings of the package center
            Parameters
            ----------
            enable_email : bool
                Enable email notification
                
            enable_dsm : bool 
                Enable desktop notification

            enable_autoupdate: bool
                Update packages automatically

            autoupdateall : bool
                Auto update all packages

            autoupdateimportant : bool
                Auto update "important" packages

            default_vol : str
                Default volume for installation, all your volumes or `"no_default_vol" = Always ask me` 
                
            udpate_channel : str
                "stable" => Disable beta packages
                "beta" => Enable beta packages

            Returns
            -------
            dict
                Return some settings

            Example return
            --------------
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
        """
        
        api_name = 'SYNO.Core.Package.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "set",
            "version": info['maxVersion'],
            "enable_email": enable_email,
            "enable_dsm": enable_dsm,
            "enable_autoupdate": enable_autoupdate,
            "autoupdateall": autoupdateall,
            "autoupdateimportant": autoupdateimportant,
            "default_vol": default_vol,
            "update_channel": update_channel
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def get_package_center_infos(self) -> dict:
        """Get package center informations
            Returns
            -------
            dict
                List of configs
        
            Return example
            --------------
            ```json
            {
                "data": {
                    "config": {
                        "auth_key": "------------------------------",
                        "blBetaChannel": false,
                        "blOtherServer": false,
                        "def_void": "",
                        "ds_build": "72806",
                        "ds_major": "7",
                        "ds_minor": "2",
                        "ds_timezone": "Amsterdam",
                        "ds_unique": "synology_r1000_723+",
                        "myPayBaseURL": "https://payment.synology.com",
                        "myds_id": "7886858",
                        "serial": "2260TPR7X30E6",
                        "success": true
                    },
                    "prerelease": {
                        "agreed": true,
                        "success": true
                    },
                    "term": {
                        "agreed_term_version": "0003",
                        "curr_term_version": "0003",
                        "success": true
                    }
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Package.Info'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "get",
            "version": info['maxVersion'],
        }
        return self.request_data(api_name, api_path, req_param)

    def feasibility_check_install(self, packages: List[str]) -> dict:
        """Check if installation is possible
        
            Parameters
            ----------
            packages : List[str]
                List of package IDs to check for feasibility
        
            Returns
            -------
            dict
                _description_
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "template": "data"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Package.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "feasibility_check",
            "version": info['maxVersion'],
            "type": "install_check",
            "packages": json.dumps(packages)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def download_package(self, url: str, package_id: str, checksum: str, filesize: str) -> dict:
        """Start download of the package, return a taskId for check status
        
            Parameters
            ----------
            url : str
                Url that can be retrieve from package info using `get_installable` function, in the `link` field
            package_id : str
                Package ID that can be retrieve from package info using `get_installable` function, in the `id` field
            checksum : str
                Checksum that can be retrieve from package info using `get_installable` function, in the `md5` field
            filesize : str
                Filesize that can be retrieve from package info using `get_installable` function, in the `size` field
        
            Returns
            -------
            dict
                Retreive first progress of the download and the taskid used to check download status with `get_dowload_package_status` function
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "progress": 1.0000000000000001e-05,
                    "taskid": "@SYNOPKG_DOWNLOAD_DhcpServer"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Package.Installation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "install",
            "version": info['minVersion'],
            "operation": "install",
            "type": 0,
            "blqinst": False,
            "url": url,
            "name": package_id,
            "checksum": checksum,
            "filesize": filesize
        }
        return self.request_data(api_name, api_path, req_param)
        
    def get_dowload_package_status(self, task_id: str) -> dict:
        """Get current download status of the package
        
            Parameters
            ----------
            task_id : str
                task ID retrieve from response of `download_package` function
        
            Returns
            -------
            dict
                Retrieve informations about the download, important info is the `progress` field
        
            Example return
            ----------
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
        """
        api_name = 'SYNO.Core.Package.Installation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "status",
            "version": info['minVersion'],
            "task_id": task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def check_installation_from_download(self, task_id: str) -> dict:
        """Get info about downloaded package file, response field is used for `check_installation` and `install_package` function
        
            Parameters
            ----------
            task_id : str
                task ID retrieve from response of `download_package` function
        
            Returns
            -------
            dict
                Retrieve information about downloaded package installation file, response field is used for `check_installation` and `install_package` function
        
            Example return
            ----------
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
        """
        api_name = 'SYNO.Core.Package.Installation.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "check",
            "version": info['minVersion'],
            "taskid": task_id
        }
        return self.request_data(api_name, api_path, req_param)
        
    def upload_package_file(self, file_path: str, verify: bool = False, progress_bar: bool = True, additional: list = []) -> dict:
        """Upload a file for install a package
        
            Parameters
            ----------
            file_path : str
                File path
            verify : bool, optional
                Use https. Defaults to `False`
            progress_bar : bool, optional
                Enable progress bar in the terminal. Defaults to `True`
            additional : list, optional
                Additional field to retrieves. Defaults to `[]`
                All fields know are:
                `["description","maintainer","distributor","startable","dsm_apps","status","install_reboot",
                "install_type","install_on_cold_storage","break_pkgs","replace_pkgs"]`.
        
            Returns
            -------
            dict
                Informations about the uploaded file for installation
        
            Example return
            ----------
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
        """
        api_name = 'SYNO.Core.Package.Installation'
        info = self.core_list[api_name]
        api_path = info['path']
        filename = os.path.basename(file_path)
        
        session = requests.session()

        with open(file_path, 'rb') as payload:
            url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=upload&_sid=%s' % (
                api_name, info['minVersion'], self._sid)

            encoder = MultipartEncoder({
                'additional': json.dumps(additional),
                'file': (filename, payload, 'application/octet-stream')
            })

            if progress_bar:
                bar = tqdm.tqdm(desc='Upload Progress',
                                total=encoder.len,
                                dynamic_ncols=True,
                                unit='B',
                                unit_scale=True,
                                unit_divisor=1024
                                )

                monitor = MultipartEncoderMonitor(encoder, lambda monitor: bar.update(monitor.bytes_read - bar.n))

                r = session.post(
                    url,
                    data=monitor,
                    verify=verify,
                    headers={"X-SYNO-TOKEN": self.session._syno_token, 'Content-Type': monitor.content_type}
                )

            else:
                r = session.post(
                    url,
                    data=encoder,
                    verify=verify,
                    headers={"X-SYNO-TOKEN": self.session._syno_token, 'Content-Type': encoder.content_type}
                )

        session.close()
        if r.status_code != 200 or not r.json()['success']:
            return r.status_code, r.json()

        return r.json()
    
    def get_default_install_volume(self) -> dict:
        """Get default install volume for package
        
            Returns
            -------
            dict
                Return default volume, if default volume is set to `Always ask me` it return error 4501
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "default_vol": "/volume1"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Package.Setting.Volume'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "get",
            "version": info['maxVersion'],
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def check_installation(self, 
                        package_id: str, install_type: str = "", install_on_cold_storage: bool = False,
                        blCheckDep: bool = False, replacepkgs: dict = {}
                        ) -> dict:
        """Check installation of the package on the default volume
        
            Parameters
            ----------
            package_id : str
                Id of the package to install
            install_type : str, optionnal
                Installation type, Defaults to `""`. TODO: Add description and possible types
            install_on_cold_storage : bool, optional
                Defaults to `False`. TODO: Add description
            blCheckDep : bool, optional
                Defaults to `False`. TODO: Add description
            replacepkgs : dict, optional
                Defaults to `{}`. TODO: Add description
        
            Returns
            -------
            dict
                List of usefull informations about volumes
        
            Example return
            ----------
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
        """
        
        api_name = 'SYNO.Core.Package.Installation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "check",
            "version": info['maxVersion'],
            "id": package_id,
            "install_type": install_type,
            "install_on_cold_storage": install_on_cold_storage,
            "breakpkgs": None,
            "blCheckDep": blCheckDep,
            "replacepkgs": json.dumps(replacepkgs)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def upgrade_package(self, task_id: str, check_codesign: bool = False, force: bool = False, installrunpackage: bool = True, extra_values: dict = {}) -> dict:
        """Upgrade an existing package
        
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
                    "message": "<br><strong><p style='color:blue'><big><b>Installation Successful!</big></p>\n<br><p style='color:blue'>Note: If Plex cannot access your media, verify user <strong>PlexMediaServer</strong> is granted permission in <strong>Control Panel</strong>.</p><br>\nSet access to your media share(s) by performing the following steps:<br><br>\n1. Open <strong>Control Panel</strong> and select <strong>Shared Folder</strong><br>\n2. Select the share which contains your media and click <strong>Edit</strong><br>\n3. Click the <strong>Permissions</strong> tab<br>\n4. Change the dropdown from <strong>Local Users</strong> to <strong>System internal user</strong><br>\n5. Check the <strong>Read/Write</strong> checkbox for the <strong>PlexMediaServer</strong> user<br>\n6. Click <strong>Save</strong> to confirm the new permissions<br>\n7. Repeat steps 2-6 for each share you want Plex Media Server to access<br>\n",
                    "packageName": "Plex Media Server",
                    "worker_message": []
                },
                "success": true,
            }
            ```
        """
    
        api_name = 'SYNO.Core.Package.Installation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method":"upgrade",
            "version":info['minVersion'],
            "type":0,
            "check_codesign": check_codesign,
            "force": force,
            "installrunpackage": installrunpackage,
            "task_id": task_id,
            "extra_values": json.dumps(extra_values),
        }
        return self.request_data(api_name, api_path, req_param)
    
    def install_package(self, package_id:str, volume_path: str, file_path: str, check_codesign: bool = True, force: bool = True, installrunpackage: bool = True, extra_values: dict = {}) -> dict:
        """Install a package that is already downloaded
        
            Parameters
            ----------
            package_id : str
                Id of the package to install
            volume_path : str
                Volume path of the installation, can get from `check_installation` function
            file_path : str
                File path of the installation, can get from `check_installation_from_download` function
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
        """
        compound = [
            {
                "api": "SYNO.Core.Package.Installation",
                "method": "check",
                "version": self.core_list['SYNO.Core.Package.Installation']['minVersion'],
                "id": package_id,
                "install_type": "",
                "install_on_cold_storage": False,
                "breakpkgs": None,
                "blCheckDep": False,
                "replacepkgs": None
            },
            {
                "api": "SYNO.Core.Package.Installation",
                "method":"install",
                "version":self.core_list["SYNO.Core.Package.Installation"]['minVersion'],
                "type":0,
                "volume_path": volume_path,
                "path": file_path,
                "check_codesign": check_codesign,
                "force": force,
                "installrunpackage": installrunpackage,
                "extra_values": json.dumps(extra_values),
            }
        ]
        return self.batch_request(compound=compound)

    def uninstall_package(self, package_id: str) -> dict:
        """Uninstall a package
        
            Parameters
            ----------
            package_id : str
                Id of the package to uninstall
        
            Returns
            -------
            dict
                Possible message to the user
                
            Example return
            ----------
            ```json
            {
                "data": {
                    "message": "",
                    "worker_message": []
                },
                "success": true
            }
            ```
        """
        
        if not self._is_package_already_installed(package_id=package_id):
            raise Exception(f"""Package "{package_id}" is not installed, it cannot be uninstalled""")
        
        api_name = 'SYNO.Core.Package.Uninstallation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "method": "uninstall",
            "version": info['minVersion'],
            "id": package_id,
            "dsm_apps": ""
        }
        
        return self.request_data(api_name, api_path, req_param)

    def _is_package_already_installed(self, package_id: str) -> bool:
        response: dict = self.list_installed()
        data: dict = response.get("data")
        installed_packages = data.get("packages")
        package_infos: dict = next((package for package in installed_packages if package["id"] == package_id), None)
        return package_infos != None

    def easy_install(self, package_id: str, volume_path: str, install_dependencies: bool = True) -> dict:
        """Execute an "easy" installation process of the package
        
            Parameters
            ----------
            package_id : str
                Package ID to install
            volume_path : str
                Volume path where you want to install the package
            install_dependencies : bool, optional
                If you want to install dependencies. Defaults to `True`
        
            Returns
            -------
            dict
                Information about installation, same as `install_package` function
        
            Example return
            ----------
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
        """        

        # Package already installed
        if self._is_package_already_installed(package_id):
            raise Exception(f"""Package "{package_id}" already installed""")

        response: dict = self.list_installable()
        data: dict = response.get("data")
        installable_packages = data.get("packages")
        package_infos: dict = next((package for package in installable_packages if package["id"] == package_id), None)
        # Package not found
        if package_infos == None:
            raise Exception(f"""Package "{package_id}" not found in installable list, installation not possible""")


        # Check dependencies
        deppkgs = package_infos.get("deppkgs")
        if deppkgs:
            if not install_dependencies:
                raise Exception(f"""Package "{package_id}" has dependencies that needs to be installed but "install_dependencies" is set to "False" """)
            deppkg: str
            for deppkg in deppkgs:
                if not self._is_package_already_installed(deppkg):
                    print(f"""Installation of dependency "{deppkg}" for "{package_id}" started""")
                    self.easy_install(package_id=deppkg, volume_path=volume_path)
                    print(f"""Installation of dependency "{deppkg}" for "{package_id}" done""")
        
        # Store information of the package
        url = package_infos.get("link")
        filesize = package_infos.get("size")
        version = package_infos.get("version")
        checksum = package_infos.get("md5")
        
        ## Start installation sequence
        
        # Start download the package installation file
        response: dict = self.download_package(url=url, package_id=package_id, checksum=checksum, filesize=filesize)
        data: dict = response.get("data")
        task_id = data.get("taskid")
        
        # Create progress bar of the status
        response: dict = self.get_dowload_package_status(task_id=task_id)
        data: dict = response.get("data")
        progress = data.get("progress")
        if not data.get("finished"):
            with tqdm.tqdm(total=100) as pbar:
                while not data.get("finished"):
                    response: dict = self.get_dowload_package_status(task_id=task_id)
                    data: dict = response.get("data")
                    progress: float = data.get("progress")
                    if progress:
                        pbar.update(int(progress*100))
                        time.sleep(0.500)
                pbar.update(100)

        print(f"""Download of "{package_id}" done""")

        # Check downloaded file
        response: dict = self.check_installation_from_download(task_id=task_id)
        data: dict = response.get("data")
        status = data.get("status")
        file_path = data.get("filename")
        print(f"""Downloaded file status : {status}""")
        
        # Check installation
        response = self.check_installation(package_id=package_id)
        
        # Install package
        extra_values = {}
        if package_id == "SurveillanceStation":
            extra_values = {
                "chkSVS_Alias": True,
                "strSVS_Alias": "cam",
                "chkSVS_HTTP": True,
                "strSVS_HTTP": "9900",
                "chkSVS_HTTPS": True,
                "strSVS_HTTPS": "9901"
            }
        
        return self.install_package(package_id=package_id, volume_path=volume_path, file_path=file_path, extra_values=extra_values)
