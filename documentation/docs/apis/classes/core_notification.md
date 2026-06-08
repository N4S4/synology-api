---
sidebar_position: 17
title: 🚧 CoreNotification
description: "Core Notification API implementation for Synology NAS." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreNotification
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Notification API implementation for Synology NAS.  
  
Covers SYNO.Core.Notification.Advance, CMS, Line, Mail, Push, SMS,
and Sysnotify endpoints not already present in core_sys_info.py.  
  
## Methods
### `notification_advance_customized_data_get`
Get advanced notification customized data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.CustomizedData`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Customized notification data.  
</div>
  



---


### `notification_advance_customized_data_set`
Set advanced notification customized data.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.CustomizedData`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_data_** `str`  
JSON-encoded customized data payload.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_advance_filter_settings_get`
Get advanced notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Filter settings configuration.  
</div>
  



---


### `notification_advance_filter_settings_set`
Set advanced notification filter settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded filter settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_advance_filter_profile_get`
Get advanced notification filter settings profile.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Filter settings profile.  
</div>
  



---


### `notification_advance_filter_profile_set`
Set advanced notification filter settings profile.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings.Profile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_** `str`  
JSON-encoded profile data.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_advance_filter_template_get`
Get advanced notification filter settings template.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings.Template`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Filter settings template.  
</div>
  



---


### `notification_advance_filter_template_set`
Set advanced notification filter settings template.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.FilterSettings.Template`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_template_** `str`  
JSON-encoded template data.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_advance_variables_get`
Get advanced notification variables.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.Variables`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Notification variables.  
</div>
  



---


### `notification_advance_variables_set`
Set advanced notification variables.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.Variables`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_variables_** `str`  
JSON-encoded variables data.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_advance_warning_percentage_get`
Get advanced notification warning percentage thresholds.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.WarningPercentage`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Warning percentage configuration.  
</div>
  



---


### `notification_advance_warning_percentage_set`
Set advanced notification warning percentage thresholds.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Advance.WarningPercentage`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_percentage_** `int`  
Warning percentage threshold value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_cms_get`
Get CMS notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.CMS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
CMS notification settings.  
</div>
  



---


### `notification_cms_set`
Set CMS notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.CMS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded CMS notification settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_cms_conf_get`
Get CMS notification configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.CMS.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
CMS notification configuration.  
</div>
  



---


### `notification_cms_conf_set`
Set CMS notification configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.CMS.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_conf_** `str`  
JSON-encoded CMS notification configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_line_get`
Get Line notification configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Line`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Line notification configuration.  
</div>
  



---


### `notification_line_set`
Set Line notification configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Line`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_token_** `str`  
Line notification access token.  
  
**_enable_** `bool`  
Enable or disable Line notifications.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_mail_get`
Get mail notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Mail notification settings.  
</div>
  



---


### `notification_mail_set`
Set mail notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded mail notification settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_mail_auth_get`
Get mail notification authentication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Auth`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Mail authentication settings.  
</div>
  



---


### `notification_mail_auth_set`
Set mail notification authentication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Auth`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_auth_type_** `str`  
Authentication type (e.g., 'plain', 'login').  
  
**_username_** `str`  
SMTP authentication username.  
  
**_password_** `str`  
SMTP authentication password.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_mail_oauth_get`
Get mail notification OAuth settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Oauth`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Mail OAuth settings.  
</div>
  



---


### `notification_mail_oauth_set`
Set mail notification OAuth settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Oauth`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_client_id_** `str`  
OAuth client ID.  
  
**_client_secret_** `str`  
OAuth client secret.  
  
**_refresh_token_** `str`  
OAuth refresh token.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_mail_profile_conf_get`
Get mail notification profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Profile.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Mail profile configuration.  
</div>
  



---


### `notification_mail_profile_conf_set`
Set mail notification profile configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Mail.Profile.Conf`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_profile_** `str`  
JSON-encoded mail profile configuration.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_push_get`
Get push notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Push notification settings.  
</div>
  



---


### `notification_push_set`
Set push notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable push notifications.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_push_auth_token_get`
Get push notification authentication token.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.AuthToken`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Push authentication token information.  
</div>
  



---


### `notification_push_auth_token_set`
Set push notification authentication token.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.AuthToken`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_token_** `str`  
Push authentication token.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_push_mobile_get`
Get mobile push notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.Mobile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Mobile push notification settings.  
</div>
  



---


### `notification_push_mobile_set`
Set mobile push notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.Mobile`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded mobile push settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_push_webhook_provider_get`
Get push notification webhook provider configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.Webhook.Provider`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Webhook provider configuration.  
</div>
  



---


### `notification_push_webhook_provider_set`
Set push notification webhook provider configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Push.Webhook.Provider`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_provider_** `str`  
Webhook provider name.  
  
**_url_** `str`  
Webhook endpoint URL.  
  
**_token_** `str`  
Webhook authentication token.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_sms_get`
Get SMS notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.SMS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SMS notification settings.  
</div>
  



---


### `notification_sms_set`
Set SMS notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.SMS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded SMS notification settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_sms_provider_get`
Get SMS notification provider configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.SMS.Provider`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SMS provider configuration.  
</div>
  



---


### `notification_sms_provider_set`
Set SMS notification provider configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.SMS.Provider`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_provider_** `str`  
SMS provider name.  
  
**_api_key_** `str`  
SMS provider API key.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `notification_sysnotify_get`
Get system notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Sysnotify`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
System notification settings.  
</div>
  



---


### `notification_sysnotify_set`
Set system notification settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Notification.Sysnotify`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_settings_** `str`  
JSON-encoded system notification settings.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `push_notification_requesttoken`
Request a push notification authentication token.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.DSM.PushNotification`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.DSM.PushNotification``.  
</div>
  



---


