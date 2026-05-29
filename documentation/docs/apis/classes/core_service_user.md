---
sidebar_position: 22
title: 🚧 CoreServiceUser
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreServiceUser
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core user/web services: Promotion, QuickConnect, Report, Share, Sharing, User, Web.  
  
  
  
## Methods
### `promotion_info_get`
Get Synology promotion information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Promotion.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the promotion info get operation.  
</div>
  



---


### `promotion_preinstall_get`
Get pre-install promotion information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Promotion.PreInstall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the promotion preinstall get operation.  
</div>
  



---


### `quickconnect_hostname_get`
Get QuickConnect hostname settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.Hostname`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect hostname get operation.  
</div>
  



---


### `quickconnect_register_site_get`
Get QuickConnect registration site info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.RegisterSite`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect register site get operation.  
</div>
  



---


### `quickconnect_sni_get`
Get QuickConnect SNI settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.SNI`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect sni get operation.  
</div>
  



---


### `quickconnect_upnp_get`
Get QuickConnect UPnP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickConnect.Upnp`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickconnect upnp get operation.  
</div>
  



---


### `quickstart_info_get`
Get quick start wizard information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickStart.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickstart info get operation.  
</div>
  



---


### `quickstart_install`
Run quick start installation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.QuickStart.Install`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the install operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the quickstart install operation.  
</div>
  



---


### `report_get`
Get report settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report get operation.  
</div>
  



---


### `report_analyzer_get`
Get report analyzer settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer get operation.  
</div>
  



---


### `report_analyzer_file_get`
Get report analyzer file info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer.File`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer file get operation.  
</div>
  



---


### `report_analyzer_share_get`
Get report analyzer share info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Analyzer.Share`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report analyzer share get operation.  
</div>
  



---


### `report_config_get`
Get report configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report config get operation.  
</div>
  



---


### `report_config_set`
Set report configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Config`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report config set operation.  
</div>
  



---


### `report_history_get`
Get report history.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.History`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report history get operation.  
</div>
  



---


### `report_redirect_get`
Get report redirect settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Redirect`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report redirect get operation.  
</div>
  



---


### `report_util_get`
Get report utility information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Report.Util`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the report util get operation.  
</div>
  



---


### `reset_admin_get`
Get admin reset status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ResetAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the reset admin get operation.  
</div>
  



---


### `security_scan_operation_start`
Start a security scan.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Operation`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the security scan operation start operation.  
</div>
  



---


### `security_scan_operation_get`
Get security scan operation status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Operation`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the security scan operation get operation.  
</div>
  



---


### `service_conf_get`
Get service configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service conf get operation.  
</div>
  



---


### `service_conf_set`
Set service configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service conf set operation.  
</div>
  



---


### `service_port_info_get`
Get service port information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Service.PortInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the service port info get operation.  
</div>
  



---


### `share_crypto_get`
Get shared folder encryption settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Crypto`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto get operation.  
</div>
  



---


### `share_crypto_key_get`
Get shared folder encryption key info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Crypto.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto key get operation.  
</div>
  



---


### `share_crypto_file_get`
Get encrypted shared folder file settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.CryptoFile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share crypto file get operation.  
</div>
  



---


### `share_key_manager_auto_key_get`
Get key manager auto-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.AutoKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager auto key get operation.  
</div>
  



---


### `share_key_manager_key_get`
Get key manager key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager key get operation.  
</div>
  



---


### `share_key_manager_machine_key_get`
Get key manager machine key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.MachineKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager machine key get operation.  
</div>
  



---


### `share_key_manager_store_get`
Get key manager store settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.KeyManager.Store`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share key manager store get operation.  
</div>
  



---


### `share_migration_get`
Get shared folder migration status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Migration`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share migration get operation.  
</div>
  



---


### `share_migration_task_get`
Get shared folder migration task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Migration.Task`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share migration task get operation.  
</div>
  



---


### `share_permission_get`
Get permissions for a shared folder.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Permission`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
The name value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission get operation.  
</div>
  



---


### `share_permission_set`
Set permissions for a shared folder.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.Permission`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
The name value.  
  
**_permissions_** `dict`  
The permissions value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission set operation.  
</div>
  



---


### `share_permission_report_get`
Get shared folder permission report.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.PermissionReport`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share permission report get operation.  
</div>
  



---


### `share_shell_file_get`
Get shared folder shell file settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Share.ShellFile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the share shell file get operation.  
</div>
  



---


### `sharing_get`
Get file sharing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing get operation.  
</div>
  



---


### `sharing_initdata_get`
Get sharing initialization data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Initdata`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing initdata get operation.  
</div>
  



---


### `sharing_login`
Login to a file sharing link.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Login`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_sharing_id_** `str`  
The sharing id value.  
  
**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing login operation.  
</div>
  



---


### `sharing_session_get`
Get sharing session information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Sharing.Session`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the sharing session get operation.  
</div>
  



---


### `support_form_get`
Get support form configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Form`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form get operation.  
</div>
  



---


### `support_form_log_get`
Get support form submission log.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Log`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form log get operation.  
</div>
  



---


### `support_form_service_get`
Get support form service status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SupportForm.Service`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the support form service get operation.  
</div>
  



---


### `synohdpack_get`
Get Synology HD pack information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Synohdpack`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the synohdpack get operation.  
</div>
  



---


### `syslog_personal_activity_get`
Get personal activity syslog settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SyslogClient.PersonalActivity`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the syslog personal activity get operation.  
</div>
  



---


### `tuned_get`
Get system tuning (tuned) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Tuned`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the tuned get operation.  
</div>
  



---


### `tuned_set`
Set system tuning settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Tuned`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the tuned set operation.  
</div>
  



---


### `user_group_get`
Get groups a user belongs to.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.Group`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
The user value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user group get operation.  
</div>
  



---


### `user_password_expiry_get`
Get password expiry settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordExpiry`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password expiry get operation.  
</div>
  



---


### `user_password_meter_get`
Check password strength.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordMeter`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_password_** `str`  
The password value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password meter get operation.  
</div>
  



---


### `user_password_policy_get`
Get password policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordPolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password policy get operation.  
</div>
  



---


### `user_password_policy_set`
Set password policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.PasswordPolicy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user password policy set operation.  
</div>
  



---


### `user_username_policy_get`
Get username policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.User.UsernamePolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the user username policy get operation.  
</div>
  



---


### `virtualization_host_capability_get`
Get virtualization host capability information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Virtualization.Host.Capability`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the virtualization host capability get operation.  
</div>
  



---


### `vol_enc_keep_key_get`
Get volume encryption keep-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.VolEncKeepKey`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the vol enc keep key get operation.  
</div>
  



---


### `vol_enc_keep_key_set`
Set volume encryption keep-key settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.VolEncKeepKey`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the vol enc keep key set operation.  
</div>
  



---


### `web_dsm_external_get`
Get DSM external web access settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.DSM.External`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web dsm external get operation.  
</div>
  



---


### `web_dsm_external_set`
Set DSM external web access settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.DSM.External`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web dsm external set operation.  
</div>
  



---


### `web_security_http_compression_get`
Get HTTP compression settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.HTTPCompression`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security http compression get operation.  
</div>
  



---


### `web_security_http_compression_set`
Set HTTP compression settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.HTTPCompression`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security http compression set operation.  
</div>
  



---


### `web_security_tls_profile_get`
Get TLS profile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.TLSProfile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security tls profile get operation.  
</div>
  



---


### `web_security_tls_profile_set`
Set TLS profile settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Web.Security.TLSProfile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the web security tls profile set operation.  
</div>
  



---


