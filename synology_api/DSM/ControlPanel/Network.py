from synology_api import base_api
import json

class Network(base_api.BaseApi):
    """
    Network class for interacting with Synology DSM network settings.

    Supported methods:
    - Getters:
        - Get general settings
        - Get proxy settings
        - Get list of gateways
        - Get list of network interfaces
        - Get OVS status
        - Get list of bond interfaces
        - Get list of ethernet interfaces
        - Get list of PPPoE interfaces
        - Get list of PPTP VPN interfaces
        - Get list of OpenVPN with conf file VPN interfaces
        - Get list of OpenVPN VPN interfaces
        - Get list of L2TP VPN interfaces
        - Get traffic control rules
        - Get port list per service

    - Setters:
        - Set general settings
        - Set proxy settings
        - Set ethernet interfaces
    """
    
    def get_general_settings(self) -> dict:
        """Get general network settings.
        
            Returns
            -------
            dict
                General network settings.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "arp_ignore": true,
                    "dns_manual": true,
                    "dns_primary": "103.86.96.100",
                    "dns_secondary": "192.168.1.1",
                    "enable_ip_conflict_detect": true,
                    "enable_windomain": false,
                    "gateway": "192.168.1.1",
                    "gateway_info": {
                        "ifname": "ovs_eth0",
                        "ip": "192.168.1.14",
                        "mask": "255.255.255.0",
                        "status": "connected",
                        "type": "ovseth",
                        "use_dhcp": true
                    },
                    "ipv4_first": false,
                    "multi_gateway": false,
                    "server_name": "SERVER-NAME",
                    "use_dhcp_domain": true,
                    "v6gateway": "fe80::670:56ff:fe48:1f94"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_general_settings(
            self, server_name: str, dns_manual: bool, dns_primary: str,
            dns_secondary: str, arp_ignore: bool, multi_gateway: bool,
            ipv4_first: bool, enable_ip_conflict_detect: bool, use_dhcp_domain: bool
        ) -> dict:
        """Set general network settings.
        
        Parameters
        ----------
        server_name : str
            Server name.
        dns_manual : bool
            Whether to set DNS manually.
        dns_primary : str
            Primary DNS server.
        dns_secondary : str
            Secondary DNS server.
        arp_ignore : bool
            Whether to ignore ARP.
        multi_gateway : bool
            Whether to enable multiple gateways.
        ipv4_first : bool
            Whether to prioritize IPv4.
        enable_ip_conflict_detect : bool
            Whether to enable IP conflict detection.
        use_dhcp_domain : bool
            Whether to use DHCP domain.
        
        Returns
        -------
        dict
            Result of setting general network settings.
        
        Example return
        ----------
        ```json
        {
            "data": {
                "has_fail": false,
                "result": [
                    {
                        "api": "SYNO.Core.Network",
                        "data": {
                            "hostname_changed_and_join_domain": false
                        },
                        "method": "set",
                        "success": true,
                        "version": 2
                    }
                ]
            },
            "success": true
        }
        ```
        """
        
        api_name = 'SYNO.Core.Network'
        info = self.gen_list[api_name]
        compound = [
            {
                'api': api_name,
                'version': info['maxVersion'],
                'method': 'set',
                'server_name': server_name,
                'dns_manual': dns_manual,
                'dns_primary': dns_primary,
                'dns_secondary': dns_secondary,
                'arp_ignore': arp_ignore,
                'multi_gateway': multi_gateway,
                'ipv4_first': ipv4_first,
                'enable_ip_conflict_detect': enable_ip_conflict_detect,
                'use_dhcp_domain': use_dhcp_domain
            }
        ]
        return self.batch_request(compound=compound)
    
    def get_proxy_settings(self) -> dict:
        """Get proxy settings.
        
            Returns
            -------
            dict
                Proxy settings.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "enable": false,
                    "enable_auth": false,
                    "enable_bypass": true,
                    "enable_different_host": false,
                    "http_host": "",
                    "http_port": "80",
                    "https_host": "",
                    "https_port": "80",
                    "password": "\t\t\t\t\t\t\t\t",
                    "username": ""
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Proxy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_proxy_settings(
        self, enable: bool, enable_auth: bool, enable_bypass: bool,
        enable_different_host: bool, http_host: str, http_port: str,
        https_host: str, https_port: str, username: str = None, password: str = None
        ) -> dict:
        """Set proxy settings.
        
        Parameters
        ----------
        enable : bool
            Whether to enable proxy.
        enable_auth : bool
            Whether to enable authentication.
        enable_bypass : bool
            Whether to enable bypass.
        enable_different_host : bool
            Whether to enable different host.
        http_host : str
            HTTP host.
        http_port : str
            HTTP port.
        https_host : str
            HTTPS host.
        https_port : str
            HTTPS port.
        username : str, optional
            Username for authentication. Default is None.
        password : str, optional
            Password for authentication. Default is None.
        
        Returns
        -------
        dict
            Result of setting proxy settings.
        
        Example return
        ----------
        ```json
        {
        "data": {
            "has_fail": false,
            "result": [
            {
                "api": "SYNO.Core.Network.Proxy",
                "method": "set",
                "success": true,
                "version": 1
            }
            ]
        },
        "success": true
        }
        ```
        """
        
        api_name = 'SYNO.Core.Network.Proxy'
        info = self.gen_list[api_name]
        compound = [
            {
                'api': api_name,
                'version': info['maxVersion'],
                'method': 'set',
                'enable': enable,
                'enable_auth': enable_auth,
                'enable_bypass': enable_bypass,
                'enable_different_host': enable_different_host,
                'http_host': http_host,
                'http_port': http_port,
                'https_host': https_host,
                'https_port': https_port
            }
        ]
        
        if username and password:
            if self.session._secure:
                compound[0]['username'] = username
                compound[0]['password'] = password
            else:
                params_enc = {
                    'username': username,
                    'password': password
                }
                compound[0].update(self.session.encrypt_params(params_enc))
        
        
        return self.batch_request(compound=compound)
    
    def get_gateway_list(self) -> dict:
        """Get list of gateways.
        
            Returns
            -------
            dict
                List of gateways.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "configs": [
                        {
                            "class": "ethernet",
                            "dns": "192.168.1.1",
                            "gateway": "192.168.1.1",
                            "ifname": "ovs_eth0",
                            "priority": 0,
                            "slave": false
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Gateway.List'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_interfaces_list(self) -> dict:
        """Get list of network interfaces.
        
            Returns
            -------
            dict
                List of network interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "ifname": "ovs_eth0",    
                        "ip": "192.168.1.14",    
                        "mask": "255.255.255.0", 
                        "speed": 1000,
                        "status": "connected",   
                        "type": "ovseth",        
                        "use_dhcp": true
                    },
                    {
                        "ifname": "ovs_eth1",    
                        "ip": "169.254.183.6",   
                        "mask": "255.255.0.0",   
                        "speed": -1,
                        "status": "disconnected",
                        "type": "ovseth",        
                        "use_dhcp": true
                    },
                    {
                        "ifname": "pppoe",       
                        "ip": "",
                        "mask": "",
                        "speed": 0,
                        "status": "disconnected",
                        "type": "pppoe",
                        "use_dhcp": true
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Interface'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
        
    def get_ovs_status(self) -> dict:
        """Get infos if ovs is enabled or not.
        
            Returns
            -------
            dict
                Infos about ovs status.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "enable_ovs": true
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.OVS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_bond_list(self) -> dict:
        """Get list of bond interfaces.
        
            Returns
            -------
            dict
                List of bond interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "block": 0,
                        "dns": "192.168.1.1",
                        "duplex": true,
                        "enable_ha_ip": false,
                        "enable_vlan": false,
                        "enabled": true,
                        "error": false,
                        "gateway": "192.168.1.1",
                        "ha_local_ip": "",
                        "ha_local_mask": "",
                        "ifname": "ovs_bond0",
                        "ip": "192.168.1.14",
                        "ipv6": [
                            "2a01:cb05:814e:7d00:9209:d0ff:fe25:7371/64",
                            "fe80::9209:d0ff:fe25:7371/64"
                        ],
                        "is_default_gateway": false,
                        "is_main_ha_ip": false,
                        "mask": "255.255.255.0",
                        "max_supported_speed": -1,
                        "mode": "balance-slb",
                        "mtu": 1500,
                        "mtu_config": 1500,
                        "nat": false,
                        "slaves": [
                            {
                                "block": 0,
                                "dns": "",
                                "duplex": true,
                                "enable_ha_ip": false,
                                "enable_vlan": false,
                                "gateway": "",
                                "ha_local_ip": "",
                                "ha_local_mask": "",
                                "ifname": "eth0",
                                "ip": "",
                                "ipv6": [],
                                "is_default_gateway": false,
                                "is_main_ha_ip": false,
                                "mask": "",
                                "max_supported_speed": 1000,
                                "mtu": 1500,
                                "mtu_config": 1500,
                                "nat": false,
                                "speed": 1000,
                                "status": "connected",
                                "type": "lan",
                                "use_dhcp": true,
                                "vlan_id": 0
                            },
                            {
                                "block": 0,
                                "dns": "",
                                "duplex": true,
                                "enable_ha_ip": false,
                                "enable_vlan": false,
                                "gateway": "",
                                "ha_local_ip": "",
                                "ha_local_mask": "",
                                "ifname": "eth1",
                                "ip": "",
                                "ipv6": [],
                                "is_default_gateway": false,
                                "is_main_ha_ip": false,
                                "mask": "",
                                "max_supported_speed": 1000,
                                "mtu": 1500,
                                "mtu_config": 1500,
                                "nat": false,
                                "speed": -1,
                                "status": "disconnected",
                                "type": "lan",
                                "use_dhcp": true,
                                "vlan_id": 0
                            }
                        ],
                        "speed": 1000,
                        "status": "connected",
                        "type": "ovsbond",
                        "use_dhcp": true,
                        "vlan_id": 0
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Bond'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_ethernet_interface_list(self) -> dict:
        """Get list of ethernet interfaces.
        
            Returns
            -------
            dict
                List of ethernet interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "block": 0,
                        "dns": "192.168.1.1",
                        "duplex": true,
                        "enable_ha_ip": false,
                        "enable_vlan": false,
                        "gateway": "192.168.1.1",
                        "ha_local_ip": "",
                        "ha_local_mask": "",
                        "ifname": "ovs_eth0",
                        "ip": "192.168.1.14",
                        "ipv6": [
                            "2a01:cb05:814e:7d00:9209:d0ff:fe25:7371/64",
                            "fe80::9209:d0ff:fe25:7371/64"
                        ],
                        "is_default_gateway": false,
                        "is_main_ha_ip": false,
                        "mask": "255.255.255.0",
                        "max_supported_speed": 1000,
                        "mtu": 1500,
                        "mtu_config": 1500,
                        "nat": false,
                        "speed": 1000,
                        "status": "connected",
                        "type": "ovseth",
                        "use_dhcp": true,
                        "vlan_id": 0
                    },
                    {
                        "block": 0,
                        "dns": "",
                        "duplex": true,
                        "enable_ha_ip": false,
                        "enable_vlan": false,
                        "gateway": "",
                        "ha_local_ip": "",
                        "ha_local_mask": "",
                        "ifname": "ovs_eth1",
                        "ip": "169.254.183.6",
                        "ipv6": [],
                        "is_default_gateway": false,
                        "is_main_ha_ip": false,
                        "mask": "255.255.0.0",
                        "max_supported_speed": 1000,
                        "mtu": 1500,
                        "mtu_config": 1500,
                        "nat": false,
                        "speed": -1,
                        "status": "disconnected",
                        "type": "ovseth",
                        "use_dhcp": true,
                        "vlan_id": 0
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_ethernet_interfaces(self, configs: list) -> dict:
        """Set ethernet interfaces.
        
            Parameters
            ----------
            configs : list
                List of configurations for ethernet interfaces. Each configuration is a dictionary with the following keys:
                - ifname : str
                    Interface name.
                - use_dhcp : bool
                    Whether to use DHCP.
                - enable_ha_ip : bool, optional
                    Whether to enable HA IP.
                - is_default_gateway : bool, optional
                    Whether this interface is the default gateway.
                - mtu : int, optional
                    MTU size.
                - enable_vlan : bool, optional
                    Whether to enable VLAN.
                - ip : str, optional
                    IP address.
                - mask : str, optional
                    Subnet mask.
                - gateway : str, optional
                    Gateway address.
                - dns : str, optional
                    DNS server address.

            Returns
            -------
            dict
                Result of setting ethernet interfaces.

            Example return
            ----------
            ```json
            {
                "data": {
                    "has_fail": false,
                    "result": [
                        {
                            "api": "SYNO.Core.Network.Ethernet",
                            "method": "set",
                            "success": true,
                            "version": 2
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        compound = [
            {
                'api': api_name,
                'version': info['maxVersion'],
                'method': 'set',
                'configs': configs
            }
        ]
        return self.batch_request(compound=compound)
    
    def get_pppoe_interface_list(self) -> dict:
        """Get list of pppoe interfaces.
        
            Returns
            -------
            dict
                List of pppoe interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [
                    {
                        "devs": [
                            "ovs_eth0",
                            "ovs_eth1"
                        ],
                        "guest_enabled": false,
                        "ifname": "pppoe",
                        "ip": "",
                        "is_default_gateway": 1,
                        "mask": "",
                        "mtu_config": "1492",
                        "password": "",
                        "real_ifname": "ovs_eth0",
                        "status": "disconnected",
                        "type": "pppoe",
                        "use_dhcp": true,
                        "username": ""
                    }
                ],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.PPPoE'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_vpn_pptp_list(self) -> dict:
        """Get list of pptp vpn interfaces.
        
            Returns
            -------
            dict
                List of pptp vpn interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.VPN.PPTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_vpn_openvpn_with_conf_list(self) -> dict:
        """Get list of openvpn with conf file vpn interfaces.
        
            Returns
            -------
            dict
                List of openvpn with conf file vpn interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.VPN.OpenVPNWithConf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_vpn_openvpn_list(self) -> dict:
        """Get list of openvpn vpn interfaces.
        
            Returns
            -------
            dict
                List of openvpn vpn interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.VPN.OpenVPN'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_vpn_l2tp_list(self) -> dict:
        """Get list of l2tp vpn interfaces.
        
            Returns
            -------
            dict
                List of l2tp vpn interfaces.
        
            Example return
            ----------
            ```json
            {
                "data": [],
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.VPN.L2TP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_traffic_control_rules(self, adapter: str) -> dict:
        """Get traffic control rules.
        
            Parameters
            ----------
            adapter : str
                Adapter name, e.g. 'ovs_eth0'.
        
            Returns
            -------
            dict
                _description_
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "rules": [],
                    "total": 0
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Network.TrafficControl.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'load',
            'adapter': adapter
        }
        return self.request_data(api_name, api_path, req_param)

    def get_port_list_per_service(self) -> dict:
        """Get port list per service.
        
            Returns
            -------
            dict
                Port list per service.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "port_info": [
                        {
                            "desc": "rsync",
                            "dst_port": [
                                "873"
                            ],
                            "name": "rsync",
                            "port_id": "netbkp",
                            "protocol": "tcp",
                            "src_port": null
                        },
                        {
                            "desc": "Network MFP",
                            "dst_port": [
                                "3240-3259"
                            ],
                            "name": "Network MFP",
                            "port_id": "mfp",
                            "protocol": "tcp",
                            "src_port": null
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.Service.PortInfo'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'load',
            'target': json.dumps(["traffic_control"])
        }
        return self.request_data(api_name, api_path, req_param)


    pass