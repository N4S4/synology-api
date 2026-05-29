---
sidebar_position: 13
title: 🚧 CoreDirectory
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreDirectory
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Directory API implementation for Synology NAS.  
  
Covers SYNO.Core.Directory.* endpoints including Azure SSO, domain
configuration, LDAP, OIDC, and SAML-based SSO settings.  
  
## Methods
### `directory_azure_sso_get`
Get Azure SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Azure.SSO`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Azure SSO configuration.  
</div>
  



---


### `directory_azure_sso_set`
Set Azure SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Azure.SSO`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable Azure SSO.  
  
**_tenant_id_** `str`  
Azure AD tenant ID.  
  
**_client_id_** `str`  
Azure AD client/application ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_domain_conf_get`
Get domain directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Domain.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Domain configuration.  
</div>
  



---


### `directory_domain_conf_set`
Set domain directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Domain.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_conf_** `str`  
JSON-encoded domain configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_domain_trust_get`
Get domain trust relationship information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Domain.Trust`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Domain trust relationships.  
</div>
  



---


### `directory_domain_trust_set`
Set domain trust relationship configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.Domain.Trust`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_trust_** `str`  
JSON-encoded domain trust configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_ldap_base_dn_get`
Get LDAP base DN configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.BaseDN`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP base DN configuration.  
</div>
  



---


### `directory_ldap_base_dn_set`
Set LDAP base DN configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.BaseDN`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_base_dn_** `str`  
LDAP base distinguished name.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_ldap_login_notify_get`
Get LDAP login notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Login.Notify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP login notification settings.  
</div>
  



---


### `directory_ldap_login_notify_set`
Set LDAP login notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Login.Notify`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable LDAP login notifications.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_ldap_profile_get`
Get LDAP profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP profile configuration.  
</div>
  



---


### `directory_ldap_profile_set`
Set LDAP profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Profile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_** `str`  
JSON-encoded LDAP profile configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_ldap_refresh_get`
Get LDAP refresh status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.Refresh`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP refresh status.  
</div>
  



---


### `directory_ldap_refresh_set`
Trigger an LDAP refresh.  
  
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


### `directory_ldap_user_get`
Get LDAP user configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
LDAP user configuration.  
</div>
  



---


### `directory_ldap_user_set`
Set LDAP user configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.LDAP.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_** `str`  
JSON-encoded LDAP user configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_oidc_sso_get`
Get OIDC SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.OIDC.SSO`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OIDC SSO configuration.  
</div>
  



---


### `directory_oidc_sso_set`
Set OIDC SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.OIDC.SSO`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable OIDC SSO.  
  
**_issuer_** `str`  
OIDC issuer URL.  
  
**_client_id_** `str`  
OIDC client ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_cas_get`
Get SSO CAS configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.CAS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO CAS configuration.  
</div>
  



---


### `directory_sso_cas_set`
Set SSO CAS configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.CAS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded SSO CAS settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_profile_get`
Get SSO profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO profile configuration.  
</div>
  



---


### `directory_sso_profile_set`
Set SSO profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Profile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_** `str`  
JSON-encoded SSO profile configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_saml_get`
Get SSO SAML configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO SAML configuration.  
</div>
  



---


### `directory_sso_saml_set`
Set SSO SAML configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded SSO SAML settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_saml_metadata_get`
Get SSO SAML metadata.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML.Metadata`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO SAML metadata.  
</div>
  



---


### `directory_sso_saml_metadata_set`
Set SSO SAML metadata.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML.Metadata`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_metadata_** `str`  
SAML metadata XML or JSON-encoded configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_saml_status_get`
Get SSO SAML status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML.Status`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO SAML status.  
</div>
  



---


### `directory_sso_saml_status_set`
Set SSO SAML status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.SAML.Status`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable SSO SAML.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_setting_get`
Get SSO general settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Setting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO general settings.  
</div>
  



---


### `directory_sso_setting_set`
Set SSO general settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Setting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded SSO general settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_status_get`
Get SSO status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Status`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO status.  
</div>
  



---


### `directory_sso_status_set`
Set SSO status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.Status`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable SSO.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_sso_utils_get`
Get SSO utility information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.utils`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SSO utility information.  
</div>
  



---


### `directory_sso_utils_set`
Set SSO utility configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.SSO.utils`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_data_** `str`  
JSON-encoded SSO utility data.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `directory_websphere_sso_get`
Get WebSphere SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.WebSphere.SSO`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
WebSphere SSO configuration.  
</div>
  



---


### `directory_websphere_sso_set`
Set WebSphere SSO directory configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Directory.WebSphere.SSO`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable WebSphere SSO.  
  
**_settings_** `str`  
JSON-encoded WebSphere SSO settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


