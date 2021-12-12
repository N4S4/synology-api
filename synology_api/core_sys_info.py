from . import base_api_core


class SysInfo(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(SysInfo, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def fileserv_smb(self):
        api_name = 'SYNO.Core.FileServ.SMB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_afp(self):
        api_name = 'SYNO.Core.FileServ.AFP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_nfs(self):
        api_name = 'SYNO.Core.FileServ.NFS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_ftp(self):
        api_name = 'SYNO.Core.FileServ.FTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def fileserv_sftp(self):
        api_name = 'SYNO.Core.FileServ.FTP.SFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_backup_info(self):
        api_name = 'SYNO.Backup.Service.NetworkBackup'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_protocol(self):
        api_name = 'SYNO.Core.BandwidthControl.Protocol'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'protocol': 'NetworkBackup'}

        return self.request_data(api_name, api_path, req_param)

    def shared_folders_info(self):
        api_name = 'SYNO.Core.Share'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def services_status(self):
        api_name = 'SYNO.Core.Service'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def services_discovery(self):
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def file_transfer_status(self):
        api_name = 'SYNO.Core.SyslogClient.FileTransfer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_status(self):
        api_name = 'SYNO.Core.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def web_status(self):
        api_name = 'SYNO.Core.Web.DSM'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def current_connection(self):
        api_name = 'SYNO.Core.CurrentConnection'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_status(self):
        api_name = 'SYNO.Core.BandwidthControl.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def sys_status(self):
        api_name = 'SYNO.Core.System.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def latest_logs(self):
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'latestlog_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_notify_settings_status(self):
        api_name = 'SYNO.Core.SyslogClient.Setting.Notify'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_info(self):
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'first_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_rules(self):
        api_name = 'SYNO.Core.SecurityScan.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'items': 'ALL', 'method': 'rule_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_security_scan_status(self):
        api_name = 'SYNO.Core.SecurityScan.Status'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'system_get'}

        return self.request_data(api_name, api_path, req_param)

    def get_user_list(self):
        api_name = 'SYNO.Core.User'
        info = self.core_list[api_name]
        api_path = info['path']
        additional = '["email", "description", "expired"]'
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional}

        return self.request_data(api_name, api_path, req_param)

    def quickconnect_info(self):
        api_name = 'SYNO.Core.QuickConnect'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_misc_config'}

        return self.request_data(api_name, api_path, req_param)

    def quickconnect_permissions(self):
        api_name = 'SYNO.Core.QuickConnect.Permission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_topology(self):
        api_name = 'SYNO.Core.Network.Router.Topology'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_wifi_client(self):
        api_name = 'SYNO.Core.Network.Wifi.Client'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self):
        api_name = 'SYNO.Core.Network.Bond'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_bridge(self):
        api_name = 'SYNO.Core.Network.Bridge'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self):
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_local_bridge(self):
        api_name = 'SYNO.Core.Network.LocalBridge'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_usb_modem(self):
        api_name = 'SYNO.Core.Network.USBModem'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_pppoe(self):
        api_name = 'SYNO.Core.Network.PPPoE'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ipv6tunnel(self):
        api_name = 'SYNO.Core.Network.IPv6Tunnel'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_vpn_pptp(self):
        api_name = 'SYNO.Core.Network.VPN.PPTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_openvpn(self):
        api_name = 'SYNO.Core.Network.VPN.OpenVPN'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': '["status"]'}

        return self.request_data(api_name, api_path, req_param)

    def network_vpn_l2tp(self):
        api_name = 'SYNO.Core.Network.VPN.L2TP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def domain_schedule(self):
        api_name = 'SYNO.Core.Directory.Domain.Schedule'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def client_ldap(self):
        api_name = 'SYNO.Core.Directory.LDAP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def client_sso(self):
        api_name = 'SYNO.Core.Directory.SSO'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_check(self):
        api_name = 'SYNO.Core.Upgrade.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_download(self):
        api_name = 'SYNO.Core.Upgrade.Server.Download'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'progress'}

        return self.request_data(api_name, api_path, req_param)

    def sys_upgrade_setting(self):
        api_name = 'SYNO.Core.Upgrade.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_sms_conf(self):
        api_name = 'SYNO.Core.Notification.SMS.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_conf(self):
        api_name = 'SYNO.Core.Notification.Mail.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_mail(self):
        api_name = 'SYNO.Core.Notification.Push.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_conf(self):
        api_name = 'SYNO.Core.Notification.Push.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_beep_control(self):
        api_name = 'SYNO.Core.Hardware.BeepControl'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_fan_speed(self):
        api_name = 'SYNO.Core.Hardware.FanSpeed'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_hibernation(self):
        api_name = 'SYNO.Core.Hardware.Hibernation'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_ups(self):
        api_name = 'SYNO.Core.ExternalDevice.UPS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def hardware_power_schedule(self):
        api_name = 'SYNO.Core.Hardware.PowerSchedule'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def terminal_info(self):
        api_name = 'SYNO.Core.Terminal'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def snmp_info(self):
        api_name = 'SYNO.Core.SNMP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def process(self):
        api_name = 'SYNO.Core.System.Process'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def utilisation(self):
        api_name = 'SYNO.Core.System.Utilization'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def storage(self):
        api_name = 'SYNO.Storage.CGI.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load_info'}

        return self.request_data(api_name, api_path, req_param)

    def external_device_storage_usb(self):
        api_name = 'SYNO.Core.ExternalDevice.Storage.USB'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'additional': ['dev_type', 'product', 'status', 'partitions']}

        return self.request_data(api_name, api_path, req_param)

    def external_device_storage_esata(self):
        api_name = 'SYNO.Core.ExternalDevice.Storage.eSATA'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': ['dev_type', 'status']}

        return self.request_data(api_name, api_path, req_param)

    def file_index_resource(self):
        api_name = 'SYNO.Finder.FileIndexing.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def cms_info(self):
        api_name = 'SYNO.Core.CMS.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 2502}, 'success': False}
    '''def service_port_info(self):
        api_name = 'SYNO.Core.Service.PortInfo'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'target': ['port_forward']}

        return self.request_data(api_name, api_path, req_param)'''

    def port_forwarding_rules(self):
        api_name = 'SYNO.Core.PortForwarding.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def port_forwarding_router_conf(self):
        api_name = 'SYNO.Core.PortForwarding.RouterConf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def disk_list(self):
        api_name = 'SYNO.Core.Polling.Data'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_provider_info(self):
        api_name = 'SYNO.Core.DDNS.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_record_info(self):
        api_name = 'SYNO.Core.DDNS.Record'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_external_ip(self):
        api_name = 'SYNO.Core.DDNS.ExtIP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'retry': 'true'}

        return self.request_data(api_name, api_path, req_param)

    def ddns_synology(self):
        api_name = 'SYNO.Core.DDNS.Synology'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_myds_account'}

        return self.request_data(api_name, api_path, req_param)

    def iscsi_lun_info(self):
        api_name = 'SYNO.Core.ISCSI.LUN'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def hddman(self):
        api_name = 'SYNO.Storage.CGI.HddMan'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ftp_security_info(self):
        api_name = 'SYNO.Core.FileServ.FTP.Security'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bandwidth_control_info(self):
        api_name = 'SYNO.Core.BandwidthControl.Protocol'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'protocol': 'FTP'}

        return self.request_data(api_name, api_path, req_param)

    def directory_domain_info(self):  # TODO to test
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ws_transfer_info(self):  # TODO to test
        api_name = 'SYNO.Core.FileServ.ServiceDiscovery.WSTransfer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ref_link_copy_info(self):
        api_name = 'SYNO.Core.FileServ.ReflinkCopy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bonjour_service_info(self):
        api_name = 'SYNO.Core.ExternalDevice.Printer.BonjourSharing'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def users_info(self, offset=0, limit=-1):
        api_name = 'SYNO.Core.User'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'type': 'local', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def password_policy(self):
        api_name = 'SYNO.Core.User.PasswordPolicy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def password_expiry(self):
        api_name = 'SYNO.Core.User.PasswordExpiry'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def personal_photo_enable(self):
        api_name = 'SYNO.Core.User.Home'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ftp_chroot_user(self):
        api_name = 'SYNO.Core.FileServ.FTP.ChrootUser'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def server_pair(self):
        api_name = 'SYNO.S2S.Server.Pair'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': ['sync_shares']}

        return self.request_data(api_name, api_path, req_param)

    def groups_info(self, offset=0, limit=-1, name_only=False):
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

    def ldap_info(self):
        api_name = 'SYNO.Core.Directory.LDAP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 103}, 'success': False}
    '''def domain_info(self):
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'get': {'additional': 'true'}}

        return self.request_data(api_name, api_path, req_param)'''

    def sso_iwa_info(self):
        api_name = 'SYNO.Core.Directory.SSO.IWA'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def sso_info(self):
        api_name = 'SYNO.Core.Directory.SSO'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_interface_info(self):
        api_name = 'SYNO.Core.Network.Interface'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def proxy_info(self):
        api_name = 'SYNO.Core.Network.Proxy'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def gateway_list(self, ip_type='ipv4', type='wan'):
        api_name = 'SYNO.Core.Network.Router.Gateway.List'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'iptype': ip_type, 'type': type}

        return self.request_data(api_name, api_path, req_param)

    def firewall_info(self):
        api_name = 'SYNO.Core.Security.Firewall.Profile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # TODO {'error': {'code': 101}, 'success': False}
    '''def upgrade_schedule_set(self, week_day=4, hour=4, minute=10):
        api_name = 'SYNO.Core.Upgrade.Setting'
        info = self.core_list[api_name]
        api_path = info['path']

        schedule = {'week_day': '4', 'hour': 4, 'minute': 10}
        req_param = {'version': info['maxVersion'], 'method': 'set', 'autoupdate_type': 'hotfix-security',
                     'schedule': schedule}

        return self.request_data(api_name, api_path, req_param)'''

    def auto_upgrade_status(self):
        api_name = 'SYNO.Core.Upgrade.AutoUpgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    def upgrade_server_check(self):
        api_name = 'SYNO.Core.Upgrade.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'check', 'user_reading': 'true',
                     'need_auto_smallupdate': 'true', 'need_promotion': 'true'}

        return self.request_data(api_name, api_path, req_param)
