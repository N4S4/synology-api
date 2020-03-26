from .synology import api_call, Synology


class SysInfo(Synology):
    app = 'Core'

    @api_call()
    def fileserv_smb(self):
        return self.api_request('FileServ.SMB', 'get')

    @api_call()
    def fileserv_afp(self):
        return self.api_request('FileServ.AFP', 'get')

    @api_call()
    def fileserv_nfs(self):
        return self.api_request('FileServ.NFS', 'get')

    @api_call()
    def fileserv_ftp(self):
        return self.api_request('FileServ.FTP', 'get')

    @api_call()
    def fileserv_sftp(self):
        return self.api_request('FileServ.FTP.SFTP', 'get')

    @api_call()
    def shared_folders_info(self):
        return self.api_request('Share', 'list')

    @api_call()
    def services_status(self):
        return self.api_request('Service', 'get')

    @api_call()
    def services_discovery(self):
        return self.api_request('FileServ.ServiceDiscovery', 'get')

    @api_call()
    def file_transfer_status(self):
        return self.api_request('SyslogClient.FileTransfer', 'get')

    @api_call()
    def network_status(self):
        return self.api_request('Network', 'get')

    @api_call()
    def web_status(self):
        return self.api_request('Web.DSM', 'get')

    @api_call()
    def current_connection(self):
        return self.api_request('CurrentConnection', 'get')

    @api_call()
    def bandwidth_control_status(self):
        return self.api_request('BandwidthControl.Status', 'list')

    @api_call()
    def sys_status(self):
        return self.api_request('System.Status', 'get')

    @api_call()
    def latest_logs(self):
        return self.api_request('SyslogClient.Status', 'latestlog_get')

    @api_call()
    def client_notify_settings_status(self):
        return self.api_request('SyslogClient.Setting.Notify', 'get')

    @api_call()
    def get_security_scan_info(self):
        return self.api_request('SecurityScan.Conf', 'first_get')

    @api_call()
    def get_security_scan_status(self):
        return self.api_request('SecurityScan.Status', 'system_get')

    @api_call()
    def quickconnect_info(self):
        return self.api_request('QuickConnect', 'get_misc_config')

    @api_call()
    def quickconnect_permissions(self):
        return self.api_request('QuickConnect.Permission', 'get')

    @api_call()
    def network_topology(self):
        return self.api_request('Network.Router.Topology', 'get')

    @api_call()
    def network_wifi_client(self):
        return self.api_request('Network.Wifi.Client', 'list')

    @api_call()
    def network_bond(self):
        return self.api_request('Network.Bond', 'list')

    @api_call()
    def network_bridge(self):
        return self.api_request('Network.Bridge', 'list')

    @api_call()
    def network_ethernet(self):
        return self.api_request('Network.Ethernet', 'list')

    @api_call()
    def network_local_bridge(self):
        return self.api_request('Network.LocalBridge', 'list')

    @api_call()
    def network_usb_modem(self):
        return self.api_request('Network.USBModem', 'list')

    @api_call()
    def network_pppoe(self):
        return self.api_request('Network.PPPoE', 'list')

    @api_call()
    def network_vpn_pptp(self):
        return self.api_request('Network.VPN.PPTP', 'list')

    @api_call()
    def network_openvpn_with_conf(self):
        return self.api_request('Network.VPN.OpenVPNWithConf', 'list')

    @api_call()
    def domain_schedule(self):
        return self.api_request('Directory.Domain.Schedule', 'get')

    @api_call()
    def client_ldap(self):
        return self.api_request('Directory.LDAP', 'get')

    @api_call()
    def client_sso(self):
        return self.api_request('Directory.SSO', 'get')

    @api_call()
    def sys_upgrade_check(self):
        return self.api_request('Upgrade.Server', 'check')

    @api_call()
    def sys_upgrade_download(self):
        return self.api_request('Upgrade.Server.Download', 'progress')

    @api_call()
    def sys_upgrade_setting(self):
        return self.api_request('Upgrade.Setting', 'get')

    @api_call()
    def notification_sms_conf(self):
        return self.api_request('Notification.SMS.Conf', 'get')

    @api_call()
    def notification_mail_conf(self):
        return self.api_request('Notification.Mail.Conf', 'get')

    @api_call()
    def notification_push_mail(self):
        return self.api_request('Notification.Push.Mail', 'get')

    @api_call()
    def notification_push_conf(self):
        return self.api_request('Notification.Push.Conf', 'get')

    @api_call()
    def hardware_beep_control(self):
        return self.api_request('Hardware.BeepControl', 'get')

    @api_call()
    def hardware_fan_speed(self):
        return self.api_request('Hardware.FanSpeed', 'get')

    @api_call()
    def hardware_hibernation(self):
        return self.api_request('Hardware.Hibernation', 'get')

    @api_call()
    def hardware_ups(self):
        return self.api_request('ExternalDevice.UPS', 'get')

    @api_call()
    def hardware_power_schedule(self):
        return self.api_request('Hardware.PowerSchedule', 'load')

    @api_call()
    def terminal_info(self):
        return self.api_request('Terminal', 'get')

    @api_call()
    def snmp_info(self):
        return self.api_request('SNMP', 'get')

    @api_call()
    def process(self):
        return self.api_request('System.Process', 'list')

    @api_call()
    def utilisation(self):
        return self.api_request('System.Utilization', 'get')

    @api_call()
    def network_vpn_l2tp(self):
        return self.api_request('Network.VPN.L2TP', 'list')

    @api_call()
    def network_ipv6tunnel(self):
        return self.api_request('Network.IPv6Tunnel', 'get')

    @api_call()
    def bandwidth_control_protocol(self):
        req_param = {'protocol': 'NetworkBackup'}
        return self.api_request('BandwidthControl.Protocol', 'get', req_param)

    @api_call()
    def network_openvpn(self):
        req_param = {'additional': '["status"]'}
        return self.api_request('Network.VPN.OpenVPN', 'list', req_param)

    @api_call()
    def get_user_list(self):
        additional = '["email", "description", "expired"]'
        req_param = {'additional': additional}
        return self.api_request('User', 'list', req_param)

    @api_call()
    def get_security_scan_rules(self):
        req_param = {'items': 'ALL'}
        return self.api_request('SecurityScan.Status', 'rule_get', req_param)


class Backup(Synology):
    app = "Backup"

    @api_call()
    def network_backup_info(self):
        return self.api_request('Service.NetworkBackup', 'get')


class Storage(Synology):
    app = "Storage"

    @api_call()
    def storage(self):
        return self.api_request('CGI.Storage', 'load_info')
