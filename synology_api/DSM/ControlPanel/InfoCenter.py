"""
Info center class for Synology DSM Info center settings.
"""

from synology_api import base_api


class InfoCenter(base_api.BaseApi):
    """
    Info center class for interacting with Synology DSM Info center settings.

    Supported methods:
    - Getters:

    - Setters:
    """

    def get_system_info(self) -> dict:
        """
        Get system information.

        Returns
        -------
        dict
            Return system information including CPU, memory, and disk usage.

        Examples
        --------
        ```json
        {
            "data": {
                "cpu_clock_speed": 2600,
                "cpu_cores": "2",
                "cpu_family": "Ryzen",
                "cpu_series": "R1600",
                "cpu_vendor": "AMD",
                "enabled_ntp": true,
                "external_pci_slot_info": [
                    {
                        "Occupied": "no",
                        "Recognized": "no",
                        "cardName": "-",
                        "slot": "1"
                    }
                ],
                "firmware_date": "2025/01/20",
                "firmware_ver": "DSM 7.2.2-72806 Update 3",
                "model": "DS723+",
                "ntp_server": "time.google.com",
                "ram_size": 2048,
                "sata_dev": [],
                "serial": "YOUR-SERIAL-NUMBER",
                "support_esata": "yes",
                "sys_temp": 47,
                "sys_tempwarn": false,
                "systempwarn": false,
                "temperature_warning": false,
                "time": "2025-07-06 00:23:44",
                "time_zone": "Amsterdam",
                "time_zone_desc": "(GMT+01:00) Amsterdam, Berlin, Rome, Stockholm, Vienna",
                "up_time": "49:46:21",
                "usb_dev": []
            },
            "success": true,
        }
        ```
        """
        api_name = 'SYNO.Core.System'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'info'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_network_info(self) -> dict:
        """
        Get network information.

        Returns
        -------
        dict
            Return network information including interfaces, IP addresses, and DNS settings.

        Examples
        --------
        ```json
        {
            "data": {
                "dns": "YOUR-DNS",
                "enabled_domain": false,
                "enabled_samba": true,
                "gateway": "YOUR-GATEWAY",
                "hostname": "YOUR-HOSTNAME",
                "nif": [
                    {
                        "addr": "YOUR-IP-ADDRESS",
                        "duplex": true,
                        "id": "ovs_eth0",
                        "ipv6": [
                            {
                                "addr": "YOUR-IPv6-ADDRESS",
                                "prefix_len": 64,
                                "scope": "global"
                            },
                            {
                                "addr": "YOUR-IPv6-ADDRESS",
                                "prefix_len": 64,
                                "scope": "link"
                            }
                        ],
                        "mac": "YOUR-MAC-ADDRESS",
                        "mask": "255.255.255.0",
                        "mtu": 1500,
                        "speed": 1000,
                        "status": "connected",
                        "type": "ovseth",
                        "use_dhcp": true
                    },
                    {
                        "addr": "YOUR-SECOND-IP-ADDRESS",
                        "duplex": true,
                        "id": "ovs_eth1",
                        "mac": "YOUR-SECOND-MAC-ADDRESS",
                        "mask": "255.255.0.0",
                        "mtu": 1500,
                        "speed": -1,
                        "status": "disconnected",
                        "type": "ovseth",
                        "use_dhcp": true
                    }
                ],
                "wins": "",
                "workgroup": "WORKGROUP"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.System'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'info',
            'type': 'network'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_storage_info(self) -> dict:
        """
        Get storage information.

        Returns
        -------
        dict
            Return storage information including volumes, disks, and RAID status.

        Examples
        --------
        ```json
        {
            "data": {
                "hdd_info": [
                    {
                        "action": {
                            "alert": false,
                            "notification": false,
                            "selectable": true,
                            "show_lifetime_chart": true
                        },
                        "action_status": {
                            "action_name": "idle",
                            "action_progress": ""
                        },
                        "action_status_category": "processing",
                        "action_status_key": "idle",
                        "adv_progress": "",
                        "adv_status": "not_support",
                        "allocation_role": "reuse_1",
                        "below_remain_life_mail_notify_thr": false,
                        "below_remain_life_show_thr": false,
                        "below_remain_life_thr": false,
                        "compatibility": "support",
                        "container": {
                            "order": 0,
                            "str": "DS723+",
                            "supportPwrBtnDisable": false,
                            "type": "internal"
                        },
                        "container_id": 0,
                        "device": "/dev/sata1",
                        "disable_secera": false,
                        "diskType": "SATA",
                        "disk_code": "",
                        "disk_location": "Main",
                        "drive_status_category": "health",
                        "drive_status_key": "normal",
                        "erase_time": 450,
                        "firm": "SC60",
                        "firmware_status": "-",
                        "has_system": true,
                        "hide_info": [],
                        "i18nNamingInfo": "[\"dsm:volume:volume_disk\",\" \",\"1\"]",
                        "id": "sata1",
                        "ihm_testing": false,
                        "is4Kn": false,
                        "isSsd": false,
                        "isSynoDrive": false,
                        "isSynoPartition": true,
                        "is_bundle_ssd": false,
                        "is_erasing": false,
                        "longName": "Drive 1",
                        "m2_pool_support": false,
                        "model": "ST4000VN006-3CW104",
                        "name": "Drive 1",
                        "num_id": 1,
                        "order": 1,
                        "overview_status": "normal",
                        "pciSlot": -1,
                        "perf_testing": false,
                        "portType": "normal",
                        "remain_life": {
                            "trustable": true,
                            "value": -1
                        },
                        "remain_life_danger": false,
                        "remote_info": {
                            "compatibility": "disabled",
                            "unc": 0
                        },
                        "sb_days_left": 0,
                        "sb_days_left_below_show_thres": false,
                        "sb_days_left_critical": false,
                        "sb_days_left_warning": false,
                        "serial": "YOUR-FIRST-SERIAL-NUMBER",
                        "size_total": "4000787030016",
                        "slot_id": 1,
                        "smart_progress": "",
                        "smart_status": "normal",
                        "smart_test_limit": 0,
                        "smart_test_support": true,
                        "smart_testing": false,
                        "ssd_unhealth_reason": "none",
                        "status": "normal",
                        "summary_status_category": "health",
                        "summary_status_key": "normal",
                        "temp": 35,
                        "testing_progress": "",
                        "testing_type": "idle",
                        "tray_status": "join",
                        "ui_serial": "YOUR-FIRST-SERIAL-NUMBER",
                        "unc": 0,
                        "used_by": "reuse_1",
                        "vendor": "Seagate",
                        "wcache_force_off": false,
                        "wcache_force_on": false,
                        "wdda_support": false
                    },
                    {
                        "action": {
                            "alert": false,
                            "notification": false,
                            "selectable": true,
                            "show_lifetime_chart": true
                        },
                        "action_status": {
                            "action_name": "idle",
                            "action_progress": ""
                        },
                        "action_status_category": "processing",
                        "action_status_key": "idle",
                        "adv_progress": "",
                        "adv_status": "not_support",
                        "allocation_role": "reuse_1",
                        "below_remain_life_mail_notify_thr": false,
                        "below_remain_life_show_thr": false,
                        "below_remain_life_thr": false,
                        "compatibility": "support",
                        "container": {
                            "order": 0,
                            "str": "DS723+",
                            "supportPwrBtnDisable": false,
                            "type": "internal"
                        },
                        "container_id": 0,
                        "device": "/dev/sata2",
                        "disable_secera": false,
                        "diskType": "SATA",
                        "disk_code": "",
                        "disk_location": "Main",
                        "drive_status_category": "health",
                        "drive_status_key": "normal",
                        "erase_time": 462,
                        "firm": "SC60",
                        "firmware_status": "-",
                        "has_system": true,
                        "hide_info": [],
                        "i18nNamingInfo": "[\"dsm:volume:volume_disk\",\" \",\"2\"]",
                        "id": "sata2",
                        "ihm_testing": false,
                        "is4Kn": false,
                        "isSsd": false,
                        "isSynoDrive": false,
                        "isSynoPartition": true,
                        "is_bundle_ssd": false,
                        "is_erasing": false,
                        "longName": "Drive 2",
                        "m2_pool_support": false,
                        "model": "ST4000VN006-3CW104",
                        "name": "Drive 2",
                        "num_id": 2,
                        "order": 2,
                        "overview_status": "normal",
                        "pciSlot": -1,
                        "perf_testing": false,
                        "portType": "normal",
                        "remain_life": {
                            "trustable": true,
                            "value": -1
                        },
                        "remain_life_danger": false,
                        "remote_info": {
                            "compatibility": "disabled",
                            "unc": 0
                        },
                        "sb_days_left": 0,
                        "sb_days_left_below_show_thres": false,
                        "sb_days_left_critical": false,
                        "sb_days_left_warning": false,
                        "serial": "YOUR-SECOND-SERIAL-NUMBER",
                        "size_total": "4000787030016",
                        "slot_id": 2,
                        "smart_progress": "",
                        "smart_status": "normal",
                        "smart_test_limit": 0,
                        "smart_test_support": true,
                        "smart_testing": false,
                        "ssd_unhealth_reason": "none",
                        "status": "normal",
                        "summary_status_category": "health",
                        "summary_status_key": "normal",
                        "temp": 37,
                        "testing_progress": "",
                        "testing_type": "idle",
                        "tray_status": "join",
                        "ui_serial": "YOUR-SECOND-SERIAL-NUMBER",
                        "unc": 0,
                        "used_by": "reuse_1",
                        "vendor": "Seagate",
                        "wcache_force_off": false,
                        "wcache_force_on": false,
                        "wdda_support": false
                    }
                ],
                "vol_info": [
                    {
                        "desc": "",
                        "inode_free": "0",
                        "inode_total": "0",
                        "is_encrypted": false,
                        "name": "volume_1",
                        "status": "normal",
                        "total_size": "206158430208",
                        "used_size": "16905019392",
                        "vol_desc": "Apps",
                        "volume": "volume_1"
                    },
                    {
                        "desc": "",
                        "inode_free": "0",
                        "inode_total": "0",
                        "is_encrypted": false,
                        "name": "volume_2",
                        "status": "normal",
                        "total_size": "3623234412544",
                        "used_size": "1154716925952",
                        "vol_desc": "Stockage",
                        "volume": "volume_2"
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'info',
            'type': 'storage_v2'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_services_status(self) -> dict:
        """
        Get services status.

        Returns
        -------
        dict
            Return the status of various services running on the Synology DSM.

        Examples
        --------
        ```json
        {
            "data": {
                "service": [
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "helptoc:winmacnfs_mac",
                        "enable_status": "disabled",
                        "service_id": "atalk"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "network:bonjourPrinter_subject",
                        "enable_status": "enabled",
                        "service_id": "bonjour"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "helptoc:ntp_service",
                        "enable_status": "enabled",
                        "service_id": "chronyd"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "service:cups_printer_daemon",
                        "enable_status": "static",
                        "service_id": "cupsd"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "tree:leaf_ftp",
                        "enable_status": "disabled",
                        "service_id": "ftp-pure"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "tree:leaf_ftpes",
                        "enable_status": "disabled",
                        "service_id": "ftp-ssl"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "remote_key:kmip_tab_title",
                        "enable_status": "disabled",
                        "service_id": "kmip-server"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "nfs:nfs_title",
                        "enable_status": "disabled",
                        "service_id": "nfs-server"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "tree:leaf_iscsi",
                        "enable_status": "static",
                        "service_id": "pkg-iscsi"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "helptoc:winmacnfs_win",
                        "enable_status": "enabled",
                        "service_id": "pkg-synosamba-smbd"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "service:wstransfer_title",
                        "enable_status": "enabled",
                        "service_id": "pkg-synosamba-wstransfer-genconf"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "service:service_rsync",
                        "enable_status": "enabled",
                        "service_id": "rsyncd"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "tree:leaf_sftp",
                        "enable_status": "disabled",
                        "service_id": "sftp"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "SNMP",
                        "enable_status": "static",
                        "service_id": "snmpd"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "firewall:firewall_service_opt_ssh",
                        "enable_status": "enabled",
                        "service_id": "ssh-shell"
                    },
                    {
                        "additional": {
                            "active_status": "active"
                        },
                        "display_name_section_key": "about:dsm",
                        "enable_status": "static",
                        "service_id": "synoscgi"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "firewall:firewall_service_opt_telnet",
                        "enable_status": "disabled",
                        "service_id": "telnetd"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "ftp:tftp_title",
                        "enable_status": "disabled",
                        "service_id": "tftp"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "helptoc:power_ups",
                        "enable_status": "disabled",
                        "service_id": "ups-net"
                    },
                    {
                        "additional": {
                            "active_status": "inactive"
                        },
                        "display_name_section_key": "helptoc:power_ups",
                        "enable_status": "static",
                        "service_id": "ups-usb"
                    }
                ]
            },
            "success": true,
        }
        ```
        """
        api_name = 'SYNO.Core.Service'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'additional': ['active_status']
        }
        return self.request_data(api_name, api_path, req_param)

    pass
