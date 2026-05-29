---
sidebar_position: 20
title: 🚧 CoreServiceApps
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreServiceApps
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core app/file services: ACL, AppPortal, CMS, FileServ, Findhost, and more.  
  
  
  
## Methods
### `acl_get`
Get ACL for a given path.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ACL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the acl get operation.  
</div>
  



---


### `acl_set`
Set ACL for a given path.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ACL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
**_acl_** `dict`  
The acl value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the acl set operation.  
</div>
  



---


### `action_priv_get`
Get action privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv get operation.  
</div>
  



---


### `action_priv_role_get`
Get action privilege roles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv.Role`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv role get operation.  
</div>
  



---


### `action_priv_role_set`
Set action privilege roles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ActionPriv.Role`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_roles_** `dict`  
The roles value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the action priv role set operation.  
</div>
  



---


### `app_notify_get`
Get application notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppNotify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app notify get operation.  
</div>
  



---


### `app_portal_get`
Get application portal settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal get operation.  
</div>
  



---


### `app_portal_set`
Set application portal settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal set operation.  
</div>
  



---


### `app_portal_access_control_get`
Get application portal access control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control get operation.  
</div>
  



---


### `app_portal_access_control_list`
List application portal access control entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control list operation.  
</div>
  



---


### `app_portal_access_control_set`
Set application portal access control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control set operation.  
</div>
  



---


### `app_portal_access_control_update`
Update an application portal access control entry.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.AccessControl`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entry_** `dict[str, object] or str`  
Access control entry to update. Dict values are JSON encoded before
they are sent to DSM.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal access control update operation.  
</div>
  



---


### `app_portal_config_get`
Get application portal configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal config get operation.  
</div>
  



---


### `app_portal_reverse_proxy_get`
List reverse proxy rules for app portal.  
  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy list operation.  
</div>
  



---


### `app_portal_reverse_proxy_list`
List reverse proxy rules for app portal.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy list operation.  
</div>
  



---


### `app_portal_reverse_proxy_create`
Create an app portal reverse proxy rule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entry_** `dict[str, object] or str`  
Reverse proxy entry to create. Dict values are JSON encoded before
they are sent to DSM.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy create operation.  
</div>
  



---


### `app_portal_reverse_proxy_update`
Update an app portal reverse proxy rule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entry_** `dict[str, object] or str`  
Reverse proxy entry to update. Dict values are JSON encoded before
they are sent to DSM.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy update operation.  
</div>
  



---


### `app_portal_reverse_proxy_delete`
Delete app portal reverse proxy rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_uuids_** `str or Sequence[str]`  
Reverse proxy UUID or UUIDs to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy delete operation.  
</div>
  



---


### `app_portal_reverse_proxy_set`
Update reverse proxy rules for app portal.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPortal.ReverseProxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the update operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app portal reverse proxy update operation.  
</div>
  



---


### `app_priv_get`
Get application privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv get operation.  
</div>
  



---


### `app_priv_app_get`
Get per-application privilege settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.App`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv app get operation.  
</div>
  



---


### `app_priv_rule_get`
Get application privilege rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.Rule`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv rule get operation.  
</div>
  



---


### `app_priv_rule_set`
Set application privilege rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.AppPriv.Rule`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `dict`  
The rules value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the app priv rule set operation.  
</div>
  



---


### `background_task_list`
List all background tasks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BackgroundTask`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the background task list operation.  
</div>
  



---


### `background_task_get`
Get a specific background task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BackgroundTask`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_task_id_** `str`  
The task id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the background task get operation.  
</div>
  



---


### `backup_ed_get`
Get encrypted data backup settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Backup.ED`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the backup ed get operation.  
</div>
  



---


### `bandwidth_control_get`
Get bandwidth control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BandwidthControl`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bandwidth control get operation.  
</div>
  



---


### `bandwidth_control_set`
Set bandwidth control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.BandwidthControl`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bandwidth control set operation.  
</div>
  



---


### `cms_get`
Get CMS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms get operation.  
</div>
  



---


### `cms_cache_get`
Get CMS cache information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Cache`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms cache get operation.  
</div>
  



---


### `cms_identity_get`
Get CMS identity information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Identity`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms identity get operation.  
</div>
  



---


### `cms_policy_get`
Get CMS policy settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Policy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms policy get operation.  
</div>
  



---


### `cms_policy_set`
Set CMS policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Policy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms policy set operation.  
</div>
  



---


### `cms_server_info_get`
Get CMS server information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.ServerInfo`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms server info get operation.  
</div>
  



---


### `cms_task_get`
Get CMS task status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Task`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms task get operation.  
</div>
  



---


### `cms_token_get`
Get CMS authentication token.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.CMS.Token`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the cms token get operation.  
</div>
  



---


### `certificate_csr_get`
Get certificate signing request settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.CSR`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate csr get operation.  
</div>
  



---


### `certificate_csr_create`
Create a certificate signing request.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.CSR`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the create operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate csr create operation.  
</div>
  



---


### `certificate_letsencrypt_get`
Get Let's Encrypt certificate settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt get operation.  
</div>
  



---


### `certificate_letsencrypt_create`
Create/renew a Let's Encrypt certificate.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the create operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt create operation.  
</div>
  



---


### `certificate_letsencrypt_account_get`
Get Let's Encrypt account information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.LetsEncrypt.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate letsencrypt account get operation.  
</div>
  



---


### `certificate_tencent_get`
Get Tencent SSL certificate settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Certificate.Tencent`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the certificate tencent get operation.  
</div>
  



---


### `ddns_ethernet_get`
Get DDNS ethernet interface settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DDNS.Ethernet`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ddns ethernet get operation.  
</div>
  



---


### `ddns_twnic_get`
Get TWNIC DDNS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DDNS.TWNIC`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ddns twnic get operation.  
</div>
  



---


### `dsm_notify_mail_content_get`
Get DSM notification mail content templates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DSMNotify.MailContent`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the dsm notify mail content get operation.  
</div>
  



---


### `dsm_notify_strings_get`
Get DSM notification strings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DSMNotify.Strings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the dsm notify strings get operation.  
</div>
  



---


### `data_collect_get`
Get data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect get operation.  
</div>
  



---


### `data_collect_set`
Set data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enabled_** `bool`  
The enabled value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect set operation.  
</div>
  



---


### `data_collect_application_get`
Get per-application data collection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DataCollect.Application`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the data collect application get operation.  
</div>
  



---


### `ew_info_get`
Get extended warranty information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.EW.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the ew info get operation.  
</div>
  



---


### `factory_config_get`
Get factory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Factory.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the factory config get operation.  
</div>
  



---


### `factory_manutild_get`
Get factory manufacturing settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Factory.Manutild`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the factory manutild get operation.  
</div>
  



---


### `file_get`
Get file information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.File`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the file get operation.  
</div>
  



---


### `file_thumbnail_get`
Get file thumbnail.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.File.Thumbnail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_path_** `str`  
The path value.  
  
**_size_** `str`  
The size value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the file thumbnail get operation.  
</div>
  



---


### `fileserv_nfs_advanced_get`
Get NFS advanced settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.AdvancedSetting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs advanced get operation.  
</div>
  



---


### `fileserv_nfs_advanced_set`
Set NFS advanced settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.AdvancedSetting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs advanced set operation.  
</div>
  



---


### `fileserv_nfs_conf_backup_get`
Get NFS configuration backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.ConfBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs conf backup get operation.  
</div>
  



---


### `fileserv_nfs_idmap_get`
Get NFS ID mapping settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.IDMap`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs idmap get operation.  
</div>
  



---


### `fileserv_nfs_kerberos_get`
Get NFS Kerberos settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.Kerberos`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs kerberos get operation.  
</div>
  



---


### `fileserv_nfs_share_privilege_get`
Get NFS share privileges.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.NFS.SharePrivilege`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv nfs share privilege get operation.  
</div>
  



---


### `fileserv_rsync_account_get`
Get rsync account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.Rsync.Account`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv rsync account get operation.  
</div>
  



---


### `fileserv_rsync_account_set`
Set rsync account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.Rsync.Account`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Additional DSM API parameters for the set operation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv rsync account set operation.  
</div>
  



---


### `fileserv_smb_conf_backup_get`
Get SMB configuration backup.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.ConfBackup`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb conf backup get operation.  
</div>
  



---


### `fileserv_smb_control_get`
Get SMB control settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.Control`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb control get operation.  
</div>
  



---


### `fileserv_smb_msdfs_get`
Get SMB MS-DFS settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.FileServ.SMB.MSDFS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the fileserv smb msdfs get operation.  
</div>
  



---


### `findhost_get`
Get find-host settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Findhost`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the findhost get operation.  
</div>
  



---


