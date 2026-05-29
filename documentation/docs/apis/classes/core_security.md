---
sidebar_position: 18
title: 🚧 CoreSecurity
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreSecurity
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Security API implementation for Synology NAS.  
  
Provides methods to manage security features including auto-block rules,
firewall settings, DoS protection, SmartBlock, OTP, and trusted devices.  
  
## Methods
### `autoblock_rules_get`
Get auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Auto-block rules configuration.  
</div>
  



---


### `autoblock_rules_list`
List all auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of auto-block rules.  
</div>
  



---


### `autoblock_rules_set`
Set auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of rule objects to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `autoblock_rules_delete`
Delete auto-block rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.AutoBlock.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of rule objects to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `security_dsm_get`
Get DSM security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM security settings.  
</div>
  



---


### `security_dsm_set`
Set DSM security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of DSM security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dsm_embed_get`
Get DSM embed security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Embed`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM embed security settings.  
</div>
  



---


### `security_dsm_embed_set`
Set DSM embed security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Embed`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of embed security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dsm_proxy_get`
Get DSM proxy security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Proxy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DSM proxy security settings.  
</div>
  



---


### `security_dsm_proxy_set`
Set DSM proxy security settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DSM.Proxy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of proxy security settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `security_dos_get`
Get DoS protection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DoS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
DoS protection settings.  
</div>
  



---


### `security_dos_set`
Set DoS protection settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.DoS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of DoS protection settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_get`
Get firewall status and settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall status and settings.  
</div>
  



---


### `firewall_set`
Set firewall settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of firewall settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_adapter_get`
Get firewall adapter configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Adapter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall adapter configuration.  
</div>
  



---


### `firewall_adapter_list`
List firewall adapters.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Adapter`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of firewall adapters.  
</div>
  



---


### `firewall_conf_get`
Get firewall configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall configuration.  
</div>
  



---


### `firewall_conf_set`
Set firewall configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of firewall configuration to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_geoip_get`
Get geo-IP blocking settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Geoip`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Geo-IP blocking settings.  
</div>
  



---


### `firewall_geoip_set`
Set geo-IP blocking settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Geoip`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of geo-IP blocking settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_profile_apply`
Apply a firewall profile.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Profile.Apply`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_name_** `str`  
Name of the firewall profile to apply. Defaults to empty string.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the apply operation.  
</div>
  



---


### `firewall_profile_apply_status`
Get the status of a firewall profile apply operation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Profile.Apply`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Status of the apply operation.  
</div>
  



---


### `firewall_rules_get`
Get firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Firewall rules configuration.  
</div>
  



---


### `firewall_rules_list`
List all firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of firewall rules.  
</div>
  



---


### `firewall_rules_set`
Set firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of firewall rule objects to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `firewall_rules_delete`
Delete firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `list[dict[str, object]]`  
List of firewall rule objects to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `firewall_rules_serv_get`
Get service-based firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Service-based firewall rules.  
</div>
  



---


### `firewall_rules_serv_list`
List service-based firewall rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Security.Firewall.Rules.Serv`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of service-based firewall rules.  
</div>
  



---


