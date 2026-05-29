---
sidebar_position: 37
title: 🚧 LdapServer
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# LdapServer
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Synology LDAP Server API client.  
  
Manages LDAP Server configuration, users, profiles,
and base DNs on DSM 7.x+.

Requires the LDAP Server package installed and at least
one LDAP directory configured on the target NAS.  
  
## Methods
### `ldap_config`
Get LDAP Server configuration.  
Returns the current LDAP client/server settings including
base DN, server address, encryption, schema type, and
connection status.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP configuration dictionary. When LDAP is not
configured, ``base_dn`` is empty and ``error``
contains a status code (e.g. 2703).  
</div>
  



---


### `ldap_basedn_list`
List LDAP Base DNs.  
.. note::
   This method requires an active LDAP configuration.
   Returns error 2701 if LDAP is not configured.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.BaseDN`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of configured Base DNs.  
</div>
  



---


### `ldap_profile_list`
List LDAP client profiles.  
.. note::
   Requires an active LDAP configuration.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of LDAP profiles.  
</div>
  



---


### `ldap_user_list`
List LDAP users.  
.. note::
   Requires an active LDAP configuration.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 100).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


### `ldap_refresh`
Refresh LDAP user/group cache.  
Triggers a re-sync of local LDAP cache with the
LDAP server.  
.. note::
   Requires an active LDAP configuration.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Refresh`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ldap_login_notify_get`
Get LDAP login notification settings.  
.. note::
   Requires an active LDAP configuration.  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Login.Notify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Login notification configuration.  
</div>
  



---


