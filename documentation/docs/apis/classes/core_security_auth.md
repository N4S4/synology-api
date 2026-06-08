---
sidebar_position: 19
title: 🚧 CoreSecurityAuth
description: "Core Security Auth API for SmartBlock/OTP/TrustDevice/DisableAdmin." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreSecurityAuth
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Security Auth API for SmartBlock/OTP/TrustDevice/DisableAdmin.  
  
Covers SYNO.Core.SmartBlock.*, OTP.*, TrustDevice, DisableAdmin,
SYNO.API.Auth.Key, Auth.Type, Auth.RedirectURI, SYNO.Auth.RescueEmail.  
  
## Methods
### `smartblock_get`
Get SmartBlock settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SmartBlock settings.  
</div>
  



---


### `smartblock_set`
Set SmartBlock settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of SmartBlock settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_device_get`
Get SmartBlock blocked devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Blocked device information.  
</div>
  



---


### `smartblock_device_list`
List SmartBlock blocked devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of blocked devices.  
</div>
  



---


### `smartblock_device_delete`
Remove devices from the SmartBlock blocked list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Device`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_devices_** `list[str]`  
List of device identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_trusted_get`
Get SmartBlock trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Trusted list entries.  
</div>
  



---


### `smartblock_trusted_list`
List SmartBlock trusted entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of trusted entries.  
</div>
  



---


### `smartblock_trusted_set`
Set SmartBlock trusted list entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[dict[str, object]]`  
List of trusted entry objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_trusted_delete`
Delete entries from the SmartBlock trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Trusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[str]`  
List of entry identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_untrusted_get`
Get SmartBlock untrusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Untrusted list entries.  
</div>
  



---


### `smartblock_untrusted_list`
List SmartBlock untrusted entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of untrusted entries.  
</div>
  



---


### `smartblock_untrusted_set`
Set SmartBlock untrusted list entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[dict[str, object]]`  
List of untrusted entry objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_untrusted_delete`
Delete entries from the SmartBlock untrusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.Untrusted`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_entries_** `list[str]`  
List of entry identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `smartblock_user_get`
Get SmartBlock user-level block settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User-level block settings.  
</div>
  



---


### `smartblock_user_list`
List SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of user-level blocks.  
</div>
  



---


### `smartblock_user_set`
Set SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_users_** `list[dict[str, object]]`  
List of user block objects to set.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `smartblock_user_delete`
Delete SmartBlock user-level blocks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SmartBlock.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_users_** `list[str]`  
List of user identifiers to unblock.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `otp_get`
Get OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP settings.  
</div>
  



---


### `otp_set`
Set OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_admin_get`
Get OTP admin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Admin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP admin settings.  
</div>
  



---


### `otp_admin_set`
Set OTP admin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Admin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP admin settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_enforce_policy_get`
Get OTP enforcement policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.EnforcePolicy`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP enforcement policy settings.  
</div>
  



---


### `otp_enforce_policy_set`
Set OTP enforcement policy.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.EnforcePolicy`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of enforcement policy settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_ex_get`
Get extended OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Ex`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Extended OTP settings.  
</div>
  



---


### `otp_ex_set`
Set extended OTP settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Ex`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of extended OTP settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `otp_mail_get`
Get OTP mail settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Mail`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OTP mail settings.  
</div>
  



---


### `otp_mail_set`
Set OTP mail settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.OTP.Mail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of OTP mail settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `trust_device_get`
Get trusted device settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Trusted device settings.  
</div>
  



---


### `trust_device_list`
List trusted devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of trusted devices.  
</div>
  



---


### `trust_device_delete`
Remove devices from the trusted list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.TrustDevice`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_devices_** `list[str]`  
List of device identifiers to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the delete operation.  
</div>
  



---


### `disable_admin_get`
Get disabled admin account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DisableAdmin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Disabled admin account settings.  
</div>
  



---


### `disable_admin_set`
Set disabled admin account settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.DisableAdmin`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_**kwargs_** `object`  
Key-value pairs of admin disable settings to update.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `rescue_email_get`
Get rescue email configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Auth.RescueEmail`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Rescue email settings (verified: bool, email address if set).  
</div>
  



---


### `rescue_email_set`
Set rescue email address.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Auth.RescueEmail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_email_** `str`  
Email address to use for account rescue.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the set operation.  
</div>
  



---


### `rescue_email_verify`
Verify rescue email with confirmation code.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Auth.RescueEmail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_code_** `str`  
Verification code sent to the rescue email.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the verify operation.  
</div>
  



---


### `auth_key_get`
Get the DSM authentication key.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Authentication key data (auth_key: str).  
</div>
  



---


### `auth_key_grant`
Request a new authentication key grant.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.Key`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Grant response from the DSM auth key service.  
</div>
  



---


### `auth_key_code_get`
Get the authentication key code (used in login flow).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.Key.Code`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Key code data from ``SYNO.API.Auth.Key.Code``.  
</div>
  



---


### `auth_type_get`
Get available authentication types on this DSM.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.Type`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of auth types (e.g. ``[{"type": "passwd"}]``).  
</div>
  



---


### `auth_redirect_uri_check`
Check if OAuth redirect URI is configured and available.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.RedirectURI`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Redirect URI availability (available: bool, code: int).  
</div>
  



---


### `auth_redirect_uri_run`
Execute the OAuth redirect URI workflow.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.API.Auth.RedirectURI`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Redirect URI execution result.  
</div>
  



---


