---
sidebar_position: 29
title: 🚧 SysInfo
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# SysInfo
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core System Information API implementation for Synology NAS.  
  
This class provides methods to retrieve and manage system, network, hardware,
service, and package information from a Synology NAS.  
  
## Methods
### `fileserv_smb`
Get SMB file service status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.SMB` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SMB file service status.  

</div>



---


### `fileserv_afp`
Get AFP file service status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.AFP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
AFP file service status.  

</div>



---


### `fileserv_nfs`
Get NFS file service status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.NFS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
NFS file service status.  

</div>



---


### `fileserv_ftp`
Get FTP file service status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.FTP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
FTP file service status.  

</div>



---


### `fileserv_sftp`
Get SFTP file service status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.FTP.SFTP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SFTP file service status.  

</div>



---


### `network_backup_info`
Get network backup service information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Backup.Service.NetworkBackup` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network backup service information.  

</div>



---


### `bandwidth_control_protocol`
Get bandwidth control protocol information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.BandwidthControl.Protocol` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Bandwidth control protocol information.  

</div>



---


### `shared_folders_info`
Get shared folders information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Share` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Shared folders information.  

</div>



---


### `services_status`
Get status of core services.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Service` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Status of core services.  

</div>



---


### `services_discovery`
Get service discovery information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.ServiceDiscovery` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Service discovery information.  

</div>



---


### `file_transfer_status`
Get file transfer status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.FileTransfer` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
File transfer status.  

</div>



---


### `network_status`
Get network status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network status.  

</div>



---


### `web_status`
Get DSM web status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Web.DSM` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DSM web status.  

</div>



---


### `current_connection`
Get current connection information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.CurrentConnection` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Current connection information.  

</div>



---


### `bandwidth_control_status`
Get bandwidth control status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.BandwidthControl.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Bandwidth control status.  

</div>



---


### `sys_status`
Get system status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System status.  

</div>



---


### `latest_logs`
Get latest system logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Latest system logs.  

</div>



---


### `client_notify_settings_status`
Get client notification settings status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SyslogClient.Setting.Notify` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Client notification settings status.  

</div>



---


### `get_security_scan_info`
Get security scan configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SecurityScan.Conf` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Security scan configuration.  

</div>



---


### `get_security_scan_rules`
Get security scan rules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SecurityScan.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Security scan rules.  

</div>



---


### `get_security_scan_status`
Get security scan status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SecurityScan.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Security scan status.  

</div>



---


### `get_user_list`
Get user list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
User list.  

</div>



---


### `quickconnect_info`
Get QuickConnect configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.QuickConnect` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
QuickConnect configuration.  

</div>



---


### `quickconnect_permissions`
Get QuickConnect permissions.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.QuickConnect.Permission` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
QuickConnect permissions.  

</div>



---


### `network_topology`
Get network topology.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Router.Topology` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network topology.  

</div>



---


### `network_wifi_client`
Get WiFi client information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Wifi.Client` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
WiFi client information.  

</div>



---


### `network_bond`
Get network bond information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Bond` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network bond information.  

</div>



---


### `network_bridge`
Get network bridge information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Bridge` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network bridge information.  

</div>



---


### `network_ethernet`
Get network ethernet information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Ethernet` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network ethernet information.  

</div>



---


### `network_local_bridge`
Get local network bridge information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.LocalBridge` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Local network bridge information.  

</div>



---


### `network_usb_modem`
Get USB modem information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.USBModem` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
USB modem information.  

</div>



---


### `network_pppoe`
Get PPPoE information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.PPPoE` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
PPPoE information.  

</div>



---


### `network_ipv6tunnel`
Get IPv6 tunnel information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.IPv6Tunnel` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
IPv6 tunnel information.  

</div>



---


### `network_vpn_pptp`
Get VPN PPTP information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.VPN.PPTP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
VPN PPTP information.  

</div>



---


### `network_openvpn`
Get OpenVPN information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.VPN.OpenVPN` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
OpenVPN information.  

</div>



---


### `network_vpn_l2tp`
Get VPN L2TP information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.VPN.L2TP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
VPN L2TP information.  

</div>



---


### `domain_schedule`
Get domain schedule.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.Domain.Schedule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Domain schedule.  

</div>



---


### `client_ldap`
Get LDAP client information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.LDAP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
LDAP client information.  

</div>



---


### `client_sso`
Get SSO client information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.SSO` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SSO client information.  

</div>



---


### `sys_upgrade_check`
Check for system upgrades.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade.Server` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System upgrade check result.  

</div>



---


### `sys_upgrade_download`
Get system upgrade download progress.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade.Server.Download` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System upgrade download progress.  

</div>



---


### `sys_upgrade_setting`
Get system upgrade settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade.Setting` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System upgrade settings.  

</div>



---


### `notification_sms_conf`
Get SMS notification configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Notification.SMS.Conf` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SMS notification configuration.  

</div>



---


### `notification_mail_conf`
Get mail notification configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Notification.Mail.Conf` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Mail notification configuration.  

</div>



---


### `notification_push_mail`
Get push mail notification configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Notification.Push.Mail` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Push mail notification configuration.  

</div>



---


### `notification_push_conf`
Get push notification configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Notification.Push.Conf` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Push notification configuration.  

</div>



---


### `hardware_beep_control`
Get hardware beep control status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.BeepControl` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Hardware beep control status.  

</div>



---


### `hardware_fan_speed`
Get hardware fan speed.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.FanSpeed` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Hardware fan speed.  

</div>



---


### `set_fan_speed`
Set hardware fan speed.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.FanSpeed` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_fan_speed_** `str`  
Fan speed mode (e.g., 'quietfan', 'coolfan', 'fullfan'). Defaults to 'quietfan'.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `enable_zram`
Enable or disable ZRAM.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.ZRAM` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_zram_** `bool`  
Enable ZRAM if True, disable if False. Defaults to True.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `enable_power_recovery`
Enable power recovery options.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.PowerRecovery` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_restart_auto_after_issue_** `bool`  
Restart automatically after issue. Defaults to True.  
  
**_wake_on_lan_** `bool`  
Enable Wake-on-LAN. Defaults to False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `enable_beep_control`
Enable or disable beep control options.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.BeepControl` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_fan_fail_** `bool`  
Enable beep on fan failure.  
  
**_volume_crash_** `bool`  
Enable beep on volume crash.  
  
**_poweron_beep_** `bool`  
Enable beep on power on.  
  
**_poweroff_beep_** `bool`  
Enable beep on power off.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `set_led_control`
Set LED brightness.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Led.Brightness` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_led_brightness_** `int`  
LED brightness level. Defaults to 2.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `set_hibernation`
Set hibernation times.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.Hibernation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_internal_hd_idletime_** `int`  
Idle time for internal hard drives. Defaults to 0.  
  
**_usb_idletime_** `int`  
Idle time for USB devices. Defaults to 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `enable_external_ups`
Enable or configure external UPS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ExternalDevice.UPS` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_enable_** `bool`  
Enable external UPS. Defaults to False.  
  
**_mode_** `str`  
UPS mode. Defaults to 'SLAVE'.  
  
**_delay_time_** `int`  
Delay time. Defaults to 1.  
  
**_snmp_auth_key_dirty_** `bool`  
SNMP auth key dirty flag. Defaults to False.  
  
**_snmp_privacy_key_dirty_** `bool`  
SNMP privacy key dirty flag. Defaults to False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `get_system_info`
Get system information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System information.  

</div>



---


### `get_cpu_temp`
Get CPU temperature.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
CPU temperature.  

</div>



---


### `get_all_system_utilization`
Get all system utilization statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Utilization` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
System utilization statistics.  

</div>



---


### `get_cpu_utilization`
Get CPU utilization statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Utilization` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
CPU utilization statistics.  

</div>



---


### `get_disk_utilization`
Get disk utilization statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Utilization` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
Disk utilization statistics.  

</div>



---


### `get_memory_utilization`
Get memory utilization statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Utilization` 
</div>
  
#### Returns
<div class="padding-left--md">
`str`  
Memory utilization statistics.  

</div>



---


### `shutdown`
Shutdown the system.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_version_** `str`  
API version to use. Defaults to None.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `reboot`
Reboot the system.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
API response.  

</div>



---


### `dsm_info`
Get DSM information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.DSM.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DSM information.  

</div>



---


### `get_network_info`
Get network information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network information.  

</div>



---


### `get_volume_info`
Get volume information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Volume information.  

</div>



---


### `hardware_hibernation`
Get hardware hibernation status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Hardware.Hibernation` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Hardware hibernation status.  

</div>



---


### `hardware_ups`
Get hardware UPS status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ExternalDevice.UPS` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Hardware UPS status.  

</div>



---


### `terminal_info`
Get terminal information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Terminal` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Terminal information.  

</div>



---


### `snmp_info`
Get SNMP information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.SNMP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SNMP information.  

</div>



---


### `process`
Get system process information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Process` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System process information.  

</div>



---


### `storage`
Get storage information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Storage.CGI.Storage` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Storage information.  

</div>



---


### `external_device_storage_usb`
Get USB storage device information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ExternalDevice.Storage.USB` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
USB storage device information.  

</div>



---


### `external_device_storage_esata`
Get eSATA storage device information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ExternalDevice.Storage.eSATA` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
eSATA storage device information.  

</div>



---


### `file_index_resource`
Get file indexing status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Finder.FileIndexing.Status` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
File indexing status.  

</div>



---


### `cms_info`
Get CMS information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.CMS.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
CMS information.  

</div>



---


### `port_forwarding_rules`
Get port forwarding rules.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.PortForwarding.Rules` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Port forwarding rules.  

</div>



---


### `port_forwarding_router_conf`
Get port forwarding router configuration.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.PortForwarding.RouterConf` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Port forwarding router configuration.  

</div>



---


### `disk_list`
Get disk list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Polling.Data` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Disk list.  

</div>



---


### `ddns_provider_info`
Get DDNS provider information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.DDNS.Provider` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DDNS provider information.  

</div>



---


### `ddns_record_info`
Get DDNS record information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.DDNS.Record` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DDNS record information.  

</div>



---


### `ddns_external_ip`
Get DDNS external IP.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.DDNS.ExtIP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DDNS external IP.  

</div>



---


### `ddns_synology`
Get Synology DDNS information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.DDNS.Synology` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Synology DDNS information.  

</div>



---


### `iscsi_lun_info`
Get iSCSI LUN information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ISCSI.LUN` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
iSCSI LUN information.  

</div>



---


### `hddman`
Get HDD manager information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Storage.CGI.HddMan` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
HDD manager information.  

</div>



---


### `ftp_security_info`
Get FTP security information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.FTP.Security` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
FTP security information.  

</div>



---


### `bandwidth_control_info`
Get bandwidth control information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.BandwidthControl.Protocol` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Bandwidth control information.  

</div>



---


### `directory_domain_info`
Get directory domain information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.Domain` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Directory domain information.  

</div>



---


### `ws_transfer_info`
Get WS transfer information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.ServiceDiscovery.WSTransfer` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
WS transfer information.  

</div>



---


### `ref_link_copy_info`
Get reflink copy information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.ReflinkCopy` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Reflink copy information.  

</div>



---


### `bonjour_service_info`
Get Bonjour service information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.ExternalDevice.Printer.BonjourSharing` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Bonjour service information.  

</div>



---


### `personal_photo_enable`
Get personal photo enable status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.User.Home` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Personal photo enable status.  

</div>



---


### `ftp_chroot_user`
Get FTP chroot user information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileServ.FTP.ChrootUser` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
FTP chroot user information.  

</div>



---


### `server_pair`
Get server pair information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.S2S.Server.Pair` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Server pair information.  

</div>



---


### `groups_info`
Get groups information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Group` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
Offset for pagination. Defaults to 0.  
  
**_limit_** `int`  
Maximum number of groups to retrieve. Defaults to -1.  
  
**_name_only_** `bool`  
If True, returns only group names. Defaults to False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Groups information.  

</div>



---


### `ldap_info`
Get LDAP information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.LDAP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
LDAP information.  

</div>



---


### `sso_iwa_info`
Get SSO IWA information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.SSO.IWA` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SSO IWA information.  

</div>



---


### `sso_info`
Get SSO information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Directory.SSO` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
SSO information.  

</div>



---


### `network_interface_info`
Get network interface information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Interface` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network interface information.  

</div>



---


### `proxy_info`
Get proxy information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Proxy` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Proxy information.  

</div>



---


### `gateway_list`
Get gateway list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Router.Gateway.List` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ip_type_** `str`  
IP type (e.g., 'ipv4', 'ipv6'). Defaults to 'ipv4'.  
  
**_type_** `str`  
Gateway type (e.g., 'wan'). Defaults to 'wan'.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Gateway list.  

</div>



---


### `firewall_info`
Get firewall information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Security.Firewall.Profile` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Firewall information.  

</div>



---


### `auto_upgrade_status`
Get auto upgrade status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade.AutoUpgrade` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Auto upgrade status.  

</div>



---


### `upgrade_server_check`
Check upgrade server.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade.Server` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Upgrade server check result.  

</div>



---


### `alarm_rules_logs`
Get alarm rules logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ResourceMonitor.Log` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Alarm rules logs.  

</div>



---


### `alarm_rules_list`
Get alarm rules list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ResourceMonitor.EventRule` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Alarm rules list.  

</div>



---


### `resource_monitor_settings_list`
Get resource monitor settings.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.ResourceMonitor.Setting` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Resource monitor settings.  

</div>



---


### `file_handling_access`
Get file handling access information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.FileHandle` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_sort_direction_** `str`  
Sort direction ('ASC' or 'DESC'). Defaults to 'ASC'.  
  
**_sort_by_** `str`  
Field to sort by. Defaults to 'service'.  
  
**_limit_** `int`  
Maximum number of results. Defaults to 50.  
  
**_offset_** `int`  
Offset for pagination. Defaults to 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
File handling access information.  

</div>



---


### `list_service_group`
Get service group list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.ProcessGroup` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_interval_** `int`  
Interval for statistics. Defaults to 0.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Service group list.  

</div>



---


### `list_process_group`
Get process group list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Process` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Process group list.  

</div>



---


### `installed_package_list`
Get installed package list.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Package` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Installed package list.  

</div>



---


### `active_notifications`
Get active notifications.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.DSMNotify` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Active notifications.  

</div>



---


### `get_system_health`
Get system health information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.SystemHealth` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
System health information.  

</div>



---


### `upgrade_status`
Get upgrade status.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Upgrade` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Upgrade status.  

</div>



---


