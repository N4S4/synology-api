from synology_api import base_api
from typing import List
class ExternalDevices(base_api.BaseApi):
    """
    External devices class for interacting with Synology DSM External devices settings.
    
    Supported methods:
    - Getters:
        - get_printer_driver_list()
        - get_printer_bonjour_enabled()
        - get_storage_settings()
        - get_list_usb_devices()
        - get_list_esata_devices()
        - get_list_of_printer()
        - get_permissions()
    - Setters:
        - set_printer_bonjour_enabled()
        - set_permissions()

    """
    
    def get_printer_driver_list(self) -> dict:
        """Get the list of printer driver.
        
            Returns
            -------
            dict
                List of printer driver.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "Apollo": [
                        [
                            "Apollo P-2100",
                            "stp-pcl-apollo-p2100.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2150",
                            "stp-pcl-apollo-p2150.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2200",
                            "stp-pcl-apollo-p2200.5.2.ppd.tgz",
                            "EPSON",
                            "Stylus DX4800"
                        ],
                        [
                            "Apollo P-2250",
                            "stp-pcl-apollo-p2250.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2500",
                            "stp-pcl-apollo-p2500.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2550",
                            "stp-pcl-apollo-p2550.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2600",
                            "stp-pcl-apollo-p2600.5.2.ppd.tgz",
                            "",
                            ""
                        ],
                        [
                            "Apollo P-2650",
                            "stp-pcl-apollo-p2650.5.2.ppd.tgz",
                            "",
                            ""
                        ]
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Driver'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_printer_bonjour_enabled(self) -> dict:
        """Get the printer bonjour enabled status.
        
            Returns
            -------
            dict
                Printer bonjour enabled status.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "enable_bonjour_support": false
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.BonjourSharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_printer_bonjour_enabled(self, enable: bool) -> dict:
        """Set the printer bonjour enabled status.
        
            Parameters
            ----------
            enable : bool
                Printer bonjour enabled status.
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.BonjourSharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable_bonjour_support': enable
        }
        return self.request_data(api_name, api_path, req_param)
    
    
    def get_storage_settings(self) -> dict:
        """Get the external devices storage settings.
        
            Returns
            -------
            dict
                External devices storage settings.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "delalloc": false,
                    "forbid_usb": false,
                    "needReboot": false,
                    "non_admin_eject": false,
                    "setting": false,
                    "support_exfat_mkfs": false
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_list_usb_devices(self) -> dict:
        """Get the list of USB devices.
        
            Returns
            -------
            dict
                List of USB devices.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "devices": []
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.USB'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'additional': ["all"],
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_list_esata_devices(self) -> dict:
        """Get the list of eSATA devices.
        
            Returns
            -------
            dict
                List of eSATA devices.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "devices": []
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.eSATA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'additional': ["all"],
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_list_of_printer(self) -> dict:
        """Get the list of printers.
        
            Returns
            -------
            dict
                List of printers.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "printers": []
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'additional': ["all"],
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_permissions(self, 
                offset: int = 0, limit: int = 50,
                user_group_type: str = "local_user"
        ) -> dict:
        """Get the permissions of the external devices
            
            Parameters
            ----------
            offset : int, optional
                The offset for pagination. Defaults to `0`.
            limit : int, optional
                The limit for pagination. Defaults to `50`.
            user_group_type : str, optional
                The type of user group to list permissions for. Defaults to `"local_user"`.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
        
            Returns
            -------
            dict
                Permissions of the external devices.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "items": [
                        {
                            "is_admin": true,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "admin"
                        },
                        {
                            "is_admin": false,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "guest"
                        }
                    ],
                    "total": 2
                },
                "success": true
                }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'action': 'enum',
            'offset': offset,
            'limit': limit,
            'user_group_type': user_group_type
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_permissions(self, user_group_type: str, permissions: List[dict[str, object]]) -> dict:
        """Set the permissions of the external devices.
        
            Parameters
            ----------
            user_group_type : str
                The type of user group to set permissions for. All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
            permissions : List[dict[str, object]]
                List of permissions to set. Each permission is a dictionary.
                Example:
                ```json
                [
                    {
                        "name":"guest",
                        "is_readonly":false,
                        "is_writable":true,
                        "is_deny":false,
                        "is_custom":false
                    }
                ]
                ```
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'user_group_type': user_group_type,
            'permissions': permissions
        }
        return self.request_data(api_name, api_path, req_param)
    
    
    
    pass