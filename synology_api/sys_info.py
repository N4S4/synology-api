from . import auth as syn


class SysInfo:
    def __init__(self, ip_address, port, username, password, secure=False):

        self.session = syn.Authentication(ip_address, port, username, password, secure)

        self.session.login('Core')
        self.session.get_api_list('Core')
        self.session.get_api_list()

        self.request_data = self.session.request_data
        self.core_list = self.session.app_api_list
        self.gen_list = self.session.full_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

        print('You are now logged in!')

    def logout(self):
        self.session.logout('Core')

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

    def network_openvpn_with_conf(self):
        api_name = 'SYNO.Core.Network.VPN.OpenVPNWithConf'
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
