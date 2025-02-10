import json
from typing import List
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import os, requests, tqdm
from . import base_api

class Package(base_api.BaseApi):
    """
    Core Päckage API implementation.
    """
    
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

    def check_install(self, packages: List[str]) -> dict:
        """Check if installation is possible
        
            Parameters
            ----------
            packages : List[str]
                _description_
        
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
    
    def upload_package_file(self, file_path: str, verify: bool = False, progress_bar: bool = True, additional: list = []) -> dict:
        """TODO: Docstring
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
    
    
    