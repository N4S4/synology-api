from synology_api import base_api

class ExternalAccess(base_api.BaseApi):
    """
    External access class for interacting with Synology DSM External Access settings.
    
    Supported methods:
    - Getters:
        - get_ddns_provider_list
        - get_ddns_record_list
        - get_external_ip_list
        - get_ddns_synology_account
        - get_certificate_list
        - get_ethernet_port_list
        - get_quickconnect_info
        - get_quickconnect_status
        - get_quickconnect_permission
        - check_quickconnect_availability
        - get_quickconnect_misc_config
        - get_detect_router_information_task
        - get_detect_router_information_status
        - get_router_list
        - get_port_forwarding_rule_list
        - get_services_port_info
        - get_advanced_external_access

    - Setters:
        - set_quickconnect_server_alias
        - set_quickconnect_enable
        - set_router_config
        - set_advanced_external_access
        
    """
    
    def get_ddns_provider_list(self) -> dict:
        """Get the list of DDNS providers.
        
            Returns
            -------
            dict
                List of ddns provider.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "providers": 
                        [
                            {
                            "id": "Synology",
                            "provider": "Synology",
                            "website": "https://account.synology.com"
                            },
                            {
                            "id": "Oray.com",
                            "provider": "Oray.com",
                            "website": ""
                            }
                        ]
                    }
                },
                "success": true
            ```
        """
        api_name = 'SYNO.Core.DDNS.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_ddns_record_list(self) -> dict:
        """Get the list of DDNS records.
        
            Returns
            -------
            dict
                List of ddns record.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "next_update_time": "",
                    "records": []
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.DDNS.Record'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_external_ip_list(self) -> dict:
        """Get the list of external IP addresses.
        
            Returns
            -------
            dict
                List of external IP addresses.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "ip": "XXX.XXX.XXX.XXX",
                        "ipv6": "cf92:1469:123f:219f:73af:319a:1c77:181e",
                        "type": "WAN"
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.DDNS.ExtIP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_ddns_synology_account(self) -> dict:
        """Get the Synology DDNS account email.
        
            Returns
            -------
            dict
                Synology DDNS account email.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "email": "YOUR_EMAIL",
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.DDNS.Synology'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get_myds_account'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_certificate_list(self) -> dict:
        """Get the list of certificates.
        
            Returns
            -------
            dict
                List of certificates.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "certificates": [
                        {
                            "desc": "",
                            "id": "C6meKD",
                            "is_broken": false,
                            "is_default": false,
                            "issuer": {
                                "city": "Taipel",
                                "common_name": "Synology Inc. CA",
                                "country": "TW",
                                "organization": "Synology Inc."
                            },
                            "key_types": "",
                            "renewable": false,
                            "self_signed_cacrt_info": {
                                "issuer": {
                                "city": "Taipel",
                                "common_name": "Synology Inc. CA",
                                "country": "TW",
                                "organization": "Synology Inc."
                                },
                                "subject": {
                                "city": "Taipel",
                                "common_name": "Synology Inc. CA",
                                "country": "TW",
                                "organization": "Synology Inc."
                                }
                            },
                            "services": [],
                            "signature_algorithm": "sha256WithRSAEncryption",
                            "subject": {
                                "city": "Taipel",
                                "common_name": "synology",
                                "country": "TW",
                                "organization": "Synology Inc.",
                                "sub_alt_name": [
                                "synology"
                                ]
                            },
                            "user_deletable": true,
                            "valid_from": "Nov  4 12:33:40 2024 GMT",
                            "valid_till": "Nov  5 12:33:40 2025 GMT"
                            }
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Certificate.CRT'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_ethernet_port_list(self) -> dict:
        """Get the list of ethernet ports.
        
            Returns
            -------
            dict
                List of ethernet ports.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "ifname": "ovs_eth0",
                        "ip": "XXX.XXX.XXX.XXX",
                        "ipv6": [
                            "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                        ]
                    },
                    {
                        "ifname": "ovs_eth1",
                        "ip": "XXX.XXX.XXX.XXX",
                        "ipv6": []
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.DDNS.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_quickconnect_info(self) -> dict:
        """Get the QuickConnect information.
        
            Returns
            -------
            dict
                QuickConnect information.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "ddns_domain": "direct.quickconnect.to",
                    "domain": "quickconnect.to",
                    "enabled": false,
                    "myds_account": "YOUR_MYDS_ACCOUNT",
                    "region": "fr",
                    "server_alias": "YOUR_SERVER_ALIAS",
                    "server_id": ""
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_quickconnect_status(self) -> dict:
        """Get the QuickConnect status.
        
            Returns
            -------
            dict
                QuickConnect status.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "alias_status": "success",
                    "status": "not_running"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_quickconnect_permission(self) -> dict:
        """Get the QuickConnect permission.
        
            Returns
            -------
            dict
                QuickConnect permission.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "services": [
                            {
                                "enabled": true,
                                "id": "mobile_apps"
                            },
                            {
                                "enabled": true,
                                "id": "cloudstation"
                            },
                            {
                                "enabled": true,
                                "id": "file_sharing"
                            },
                            {
                                "enabled": true,
                                "id": "dsm_portal"
                            }
                        ]
                    },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect.Permission'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def check_quickconnect_availability(self) -> dict:
        """Check the availability of QuickConnect.
        
            Returns
            -------
            dict
                Availability status of QuickConnect.
        
            Example return
            ----------
            ```json
            {  
                "data": {
                    "available": true,
                    "code": 2908,
                    "country": "FR"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'check_availability'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_quickconnect_misc_config(self) -> dict:
        """Get the QuickConnect miscellaneous configuration.
        
            Returns
            -------
            dict
                QuickConnect miscellaneous configuration.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "relay_enabled": true
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get_misc_config'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_quickconnect_server_alias(self, server_alias: str) -> dict:
        """Set the QuickConnect server alias.
        
            Parameters
            ----------
            server_alias : str
                The server alias to set.
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true,
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set_server_alias',
            'server_alias': server_alias
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_quickconnect_enable(self, enable: bool) -> dict:
        """Enable or disable QuickConnect.
        
            Parameters
            ----------
            enable : bool
                True to enable, False to disable.
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true,
            }
            ```
        """
        api_name = 'SYNO.Core.QuickConnect'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_detect_router_information_task(self) -> dict:
        """Get the task information for detecting router.
        
            Returns
            -------
            dict
                Task information for detecting router.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "task_id": "@administrators/SYNO.Core.PortForwarding.detect174570013646DCEDAC"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.PortForwarding'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'detect'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_detect_router_information_status(self, task_id: str) -> dict:
        """Get the status of the task for detecting router.
        
            Parameters
            ----------
            task_id : str
                The task ID to check the status of.
        
            Returns
            -------
            dict
                Status of the task for detecting router.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "percentage": 30,
                    "progress": {
                        "check_connect_wan_step": {
                            "check_id": 3,
                            "status": "initial"
                        },
                        "check_dns_setting_step": {
                            "check_id": 5,
                            "status": "initial"
                        },
                        "check_gateway_setting_step": {
                            "check_id": 2,
                            "status": "processing"
                        },
                        "check_hops_lan2wan_step": {
                            "check_id": 4,
                            "status": "initial"
                        },
                        "check_interface_enable_step": {
                            "check_id": 1,
                            "network_interface": "ovs_eth0",
                            "status": "success"
                        },
                        "detect_router_step": {
                            "check_id": 6,
                            "status": "initial"
                        }
                    }
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.PortForwarding'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'detect_status',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_router_list(self) -> dict:
        """Get the list of routers.
        
            Returns
            -------
            dict
                List of routers.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "routers":[
                        {
                            "generic": false,
                            "router_brand": "3rd Party",
                            "router_model": "DD-WRT",
                            "router_version": "v24-sp1 micro"
                        },
                        {
                            "generic": false,
                            "router_brand": "3rd Party",
                            "router_model": "DD-WRT",
                            "router_version": "v24-sp2 std - build 14896"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.PortForwarding.RouterList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_router_config(self, 
                router_brand: str, router_model: str, router_version: str, router_protocol: str, router_port: int,
                support_upnp: bool = False, support_natpmp: bool = False
        ) -> dict:
        """Set the router configuration.
        
            Parameters
            ----------
            router_brand : str
                The brand of the router.
            router_model : str
                The model of the router.
            router_version : str
                The version of the router.
            router_protocol : str
                The protocol used by the router.
            router_port : int
                The port used by the router.
            support_upnp : bool, optional
                Whether UPnP is supported (default is False).
            support_natpmp : bool, optional
                Whether NAT-PMP is supported (default is False).
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true,
            }
            ```
        """
        api_name = 'SYNO.Core.PortForwarding.RouterConf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'router_brand': router_brand,
            'router_model': router_model,
            'router_version': router_version,
            'router_protocol': router_protocol,
            'router_port': router_port,
            'support_upnp': "yes" if support_upnp else "no",
            'support_natpmp': "yes" if support_natpmp else "no"
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_port_forwarding_rule_list(self) -> dict:
        """Get the list of port forwarding rules.
        
            Returns
            -------
            dict
                List of port forwarding rules.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "ds_port": "873",
                        "enable": true,
                        "router_port": "873",
                        "router_protocol": "tcp",
                        "rule_id": "1",
                        "service_name": "",
                        "serviceid": "netbkp"
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.PortForwarding.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'load'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_services_port_info(self) -> dict:
        """Get the port information of services.
        
            Returns
            -------
            dict
                Port information of services.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "service": [
                        {
                            "additional": {
                            "port_info": [
                                {
                                "desc": "Share files with Mac",
                                "dst_port": [
                                    "548"
                                ],
                                "name": "AFP",
                                "port_id": "afp",
                                "protocol": "tcp",
                                "src_port": null
                                }
                            ]
                            },
                            "display_name": "AFP",
                            "enable_status": "disabled",
                            "service_id": "atalk"
                        },
                        {
                            "additional": {
                            "port_info": [
                                {
                                "desc": "Bonjour",
                                "dst_port": [
                                    "5353"
                                ],
                                "name": "Bonjour Service",
                                "port_id": "bonjour",
                                "protocol": "udp",
                                "src_port": null
                                }
                            ]
                            },
                            "display_name": "Bonjour Printer Broadcast",
                            "enable_status": "disabled",
                            "service_id": "bonjour"
                        }
                    ]
                },
                "success": true
                }
            ```
        """
        api_name = 'SYNO.Core.Service'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'additional': ["port_info"]
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_advanced_external_access(self) -> dict:
        """Get the advanced external access settings.
        
            Returns
            -------
            dict
                Advanced external access settings:
                - `hostname`: The hostname of the DSM.
                - `http_port`: The HTTP port of the DSM.
                - `https_port`: The HTTPS port of the DSM.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "hostname": "HOSTNAME",
                    "http_port": 5000,
                    "https_port": 5001
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_advanced_external_access(self, hostname: str, http_port: int, https_port: int) -> dict:
        """Set the advanced external access settings.
        
            Parameters
            ----------
            hostname : str
                The hostname of the DSM.
            http_port : int
                The HTTP port of the DSM.
            https_port : int
                The HTTPS port of the DSM.
        
            Returns
            -------
            dict
                Result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true,
            }
            ```
        """
        api_name = 'SYNO.Core.Web.DSM.External'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'hostname': hostname,
            'http_port': http_port,
            'https_port': https_port
        }
        return self.request_data(api_name, api_path, req_param)
    
    
    pass