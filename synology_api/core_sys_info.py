from __future__ import annotations
from typing import Optional, List
from . import base_api
import json


class SysInfo(base_api.BaseApi):

    def fileserv_smb(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.SMB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_afp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.AFP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_nfs(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.NFS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_ftp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.FTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_sftp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.FTP.SFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_backup_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Service.NetworkBackup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_protocol(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.BandwidthControl.Protocol'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'protocol': 'NetworkBackup'}

        return self.request_data(api_name, api_path, req_param)

    def shared_folders_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Share'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def services_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Service'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def services_discovery(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def file_transfer_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.FileTransfer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def web_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Web.DSM'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def current_connection(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.CurrentConnection'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.BandwidthControl.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def sys_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def latest_logs(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'latestlog_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_notify_settings_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.Setting.Notify'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'first_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_rules(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SecurityScan.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'items': 'ALL', 'method': 'rule_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SecurityScan.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'system_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_user_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.User'
        info = self.core_list[api_name]
        api_path = info['path']
        additional = '["email", "description", "expired"]'
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional}

        return self.request_data(api_name, api_path, req_param)

    def quickconnect_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.QuickConnect'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_misc_config'}

        return self.request_data(api_name, api_path, req_param)

    def quickconnect_permissions(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.QuickConnect.Permission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_topology(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Router.Topology'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_wifi_client(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Wifi.Client'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Bond'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_bridge(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Bridge'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_local_bridge(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.LocalBridge'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_usb_modem(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.USBModem'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_pppoe(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.PPPoE'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ipv6tunnel(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.IPv6Tunnel'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_vpn_pptp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.VPN.PPTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_openvpn(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.VPN.OpenVPN'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': '["status"]'}

        return self.request_data(api_name, api_path, req_param)

    def network_vpn_l2tp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.VPN.L2TP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def domain_schedule(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.Domain.Schedule'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def client_ldap(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.LDAP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def client_sso(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.SSO'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_check(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_download(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.Server.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'progress'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_setting(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_sms_conf(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Notification.SMS.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_conf(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Notification.Mail.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_mail(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Notification.Push.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_conf(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Notification.Push.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_beep_control(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.BeepControl'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_fan_speed(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.FanSpeed'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def set_fan_speed(self, fan_speed: str = 'quietfan') -> dict[str, object] | str:  # coolfan , fullfan
        api_name = 'SYNO.Core.Hardware.FanSpeed'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', "dual_fan_speed": fan_speed}

        return self.request_data(api_name, api_path, req_param)

    def enable_zram(self, enable_zram: bool = True) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.ZRAM'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', "enable_zram": str(enable_zram).lower()}

        return self.request_data(api_name, api_path, req_param)

    def enable_power_recovery(self,
                              restart_auto_after_issue: bool = True,
                              wake_on_lan: bool = False
                              ) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.PowerRecovery'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     "rc_power_config": str(restart_auto_after_issue).lower(), 'wol1': str(wake_on_lan).lower()}

        return self.request_data(api_name, api_path, req_param)

    def enable_beep_control(self,
                            fan_fail: Optional[bool] = None,
                            volume_crash: Optional[bool] = None,
                            poweron_beep: Optional[bool] = None,
                            poweroff_beep: Optional[bool] = None
                            ) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.BeepControl'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', "fan_fail": str(fan_fail).lower(),
                     "volume_crash": str(volume_crash).lower(), "poweron_beep": str(poweron_beep).lower(),
                     "poweroff_beep": str(poweroff_beep).lower()}

        return self.request_data(api_name, api_path, req_param)

    def set_led_control(self, led_brightness: int = 2) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Led.Brightness'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', 'led_brightness': led_brightness}

        return self.request_data(api_name, api_path, req_param)

    def set_hibernation(self, internal_hd_idletime: int = 0, usb_idletime: int = 0) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.Hibernation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', 'internal_hd_idletime': internal_hd_idletime,
                     'usb_idletime': usb_idletime}

        return self.request_data(api_name, api_path, req_param)

    def enable_external_ups(self,
                            enable: bool = False,
                            mode: str = 'SLAVE',
                            delay_time: int = 1,
                            snmp_auth_key_dirty: bool = False,
                            snmp_privacy_key_dirty: bool = False
                            ) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ExternalDevice.UPS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', 'enable': str(enable).lower(), 'mode': mode,
                     'delay_time': delay_time, 'snmp_auth_key_dirty': str(snmp_auth_key_dirty).lower(),
                     'snmp_privacy_key_dirty': str(snmp_privacy_key_dirty).lower()}

        return self.request_data(api_name, api_path, req_param)

    def get_system_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'info'}

        return self.request_data(api_name, api_path, req_param)

    def get_cpu_temp(self) -> str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'info'}

        return self.request_data(api_name, api_path, req_param)['data']['sys_temp']

    def get_all_system_utilization(self) -> str:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)['data']

    def get_cpu_utilization(self) -> str:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)['data']['cpu']

    def get_disk_utilization(self) -> str:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)['data']['disk']

    def get_memory_utilization(self) -> str:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)['data']['memory']

    def shutdown(self, version: str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': (info['maxVersion'] if version is None else version), 'method': 'shutdown'}

        return self.request_data(api_name, api_path, req_param)

    def reboot(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'reboot'}

        return self.request_data(api_name, api_path, req_param)

    def dsm_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.DSM.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, req_param)
    def get_network_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'info', 'type': 'network'}

        return self.request_data(api_name, api_path, req_param)

    def get_volume_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'info', 'type': 'storage_v2'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_hibernation(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Hardware.Hibernation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_ups(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ExternalDevice.UPS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)
    
    def terminal_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Terminal'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def snmp_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SNMP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def process(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.Process'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage(self) -> dict[str, object] | str:
        api_name = 'SYNO.Storage.CGI.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load_info'}

        return self.request_data(api_name, api_path, req_param)

    def external_device_storage_usb(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ExternalDevice.Storage.USB'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'additional': ['dev_type', 'product', 'status', 'partitions']}

        return self.request_data(api_name, api_path, req_param)

    def external_device_storage_esata(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ExternalDevice.Storage.eSATA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': ['dev_type', 'status']}

        return self.request_data(api_name, api_path, req_param)

    def file_index_resource(self) -> dict[str, object] | str:
        api_name = 'SYNO.Finder.FileIndexing.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def cms_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.CMS.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 2502}, 'success': False}
    '''def service_port_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Service.PortInfo'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'target': ['port_forward']}

        return self.request_data(api_name, api_path, req_param)'''

    def port_forwarding_rules(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.PortForwarding.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def port_forwarding_router_conf(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.PortForwarding.RouterConf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def disk_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Polling.Data'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_provider_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.DDNS.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_record_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.DDNS.Record'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_external_ip(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.DDNS.ExtIP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'retry': 'true'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_synology(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.DDNS.Synology'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_myds_account'}

        return self.request_data(api_name, api_path, req_param)

    def iscsi_lun_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ISCSI.LUN'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def hddman(self) -> dict[str, object] | str:
        api_name = 'SYNO.Storage.CGI.HddMan'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ftp_security_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.FTP.Security'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.BandwidthControl.Protocol'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'protocol': 'FTP'}

        return self.request_data(api_name, api_path, req_param)

    def directory_domain_info(self) -> dict[str, object] | str:  # TODO to test
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ws_transfer_info(self) -> dict[str, object] | str:  # TODO to test
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery.WSTransfer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ref_link_copy_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.ReflinkCopy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bonjour_service_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.ExternalDevice.Printer.BonjourSharing'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def personal_photo_enable(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.User.Home'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ftp_chroot_user(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileServ.FTP.ChrootUser'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def server_pair(self) -> dict[str, object] | str:
        api_name = 'SYNO.S2S.Server.Pair'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': ['sync_shares']}

        return self.request_data(api_name, api_path, req_param)

    def groups_info(self, offset: int = 0, limit: int = -1, name_only: bool = False) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Group'
        info = self.core_list[api_name]
        api_path = info['path']

        if name_only:
            name_only = 'true'
        elif not name_only:
            name_only = 'false'
        else:
            return 'name_only must be True or False'
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit,
                     'name_only': name_only, 'type': 'local'}

        return self.request_data(api_name, api_path, req_param)

    def ldap_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.LDAP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 103}, 'success': False}
    '''def domain_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'get': {'additional': 'true'}}

        return self.request_data(api_name, api_path, req_param)'''

    def sso_iwa_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.SSO.IWA'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def sso_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Directory.SSO'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_interface_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Interface'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def proxy_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Proxy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def gateway_list(self, ip_type: str = 'ipv4', type: str = 'wan') -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Router.Gateway.List'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'iptype': ip_type, 'type': type}

        return self.request_data(api_name, api_path, req_param)

    def firewall_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Security.Firewall.Profile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 101}, 'success': False}
    '''def upgrade_schedule_set(self, week_day=4, hour=4, minute=10) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.Setting'
        info = self.core_list[api_name]
        api_path = info['path']

        schedule = {'week_day': '4', 'hour': 4, 'minute': 10}
        req_param = {'version': info['maxVersion'], 'method': 'set', 'autoupdate_type': 'hotfix-security',
                     'schedule': schedule}

        return self.request_data(api_name, api_path, req_param)'''

    def auto_upgrade_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.AutoUpgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_server_check(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check', 'user_reading': 'true',
                     'need_auto_smallupdate': 'true', 'need_promotion': 'true'}

        return self.request_data(api_name, api_path, req_param)

    def alarm_rules_logs(self) -> dict[str, object] | str:
        api_name = 'SYNO.ResourceMonitor.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': 0, 'limit': 100,
                     'sort_direction': 'DESC', 'sort_by': 'time', 'mode': 'sequential'}

        return self.request_data(api_name, api_path, req_param)

    def alarm_rules_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.ResourceMonitor.EventRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def resource_monitor_settings_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.ResourceMonitor.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def file_handling_access(self, sort_direction: str = 'ASC', sort_by: str = 'service', limit: int = 50,
                             offset: int = 0) -> dict[str, object] | str:
        api_name = 'SYNO.Core.FileHandle'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'forceReload': 'true', 'action': 'enum',
                     'sort_direction': sort_direction, 'sort_by': sort_by, 'limit': limit, 'offset': offset}

        return self.request_data(api_name, api_path, req_param)

    def list_service_group(self, interval=0) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.ProcessGroup'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'node': 'xnode-3697', 'interval': interval}

        return self.request_data(api_name, api_path, req_param)

    def list_process_group(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.Process'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def installed_package_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Package'
        info = self.core_list[api_name]
        api_path = info['path']
        additional = ["description", "description_enu", "dependent_packages", "beta", "distributor", "distributor_url",
                      "maintainer", "maintainer_url", "dsm_apps", "dsm_app_page", "dsm_app_launch_name",
                      "report_beta_url",
                      "support_center", "startable", "installed_info", "support_url", "is_uninstall_pages",
                      "install_type",
                      "autoupdate", "silent_upgrade", "installing_progress", "ctl_uninstall", "updated_at", "status",
                      "url",
                      "available_operation"]

        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional}

        return self.request_data(api_name, api_path, req_param)

    def active_notifications(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.DSMNotify'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'notify', 'action': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def get_system_health(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.SystemHealth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        return self.request_data(api_name, api_path, req_param)

    def upgrade_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Upgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}
        return self.request_data(api_name, api_path, req_param)
