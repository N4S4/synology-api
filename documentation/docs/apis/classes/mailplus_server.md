---
sidebar_position: 39
title: ✅ MailPlusServer
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# MailPlusServer
## Overview
Synology MailPlus Server API client.  
  
Manages MailPlus Server configuration, SMTP/IMAP settings,
security policies, audit logs, and mail queue monitoring
via the SYNO.MailPlusServer.* WebAPI endpoints.

Requires MailPlus Server installed on the target NAS.  
  
## Methods
### `mailplus_info`
Get core MailPlus Server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.MailPlus`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Settings including SMTP sender name, DSM access,
mail export, PGP, and POP3 toggles.  
</div>
  



---


### `mailplus_server_list`
List MailPlus servers in the cluster.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.ServerList`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"server_list": [...], "balancer_enabled": ...,
"cluster_syncing": ...}, "success": true}``.  
</div>
  



---


### `mailplus_smtp_general`
Get SMTP general configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.SMTP.General`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
SMTP settings including banner, hostname,
max hops, recipients, and auth settings.  
</div>
  



---


### `mailplus_smtp_security`
Get SMTP security configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.SMTP.Security`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Security limits including max connections per minute,
max mails per minute, parallel connections, and
junk command thresholds.  
</div>
  



---


### `mailplus_imap_pop3`
Get IMAP/POP3 configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.IMAP_POP3`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
IMAP, IMAPS, POP3, POP3S enable/disable toggles
and authentication security settings.  
</div>
  



---


### `mailplus_security`
Get mail flow limit and sender quota settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.Security`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Flow limit (mails per time period) and sender
quota configuration.  
</div>
  



---


### `mailplus_report`
Get mail report configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.Report`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Report settings including enable toggle,
recipient, and scheduled hours/minutes.  
</div>
  



---


### `mailplus_admin_log`
List MailPlus admin audit log entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.Audit.AdminLog`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 50).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"log_list": [...], "offset": N,
"total": N}, "success": true}``.  
</div>
  



---


### `mailplus_transaction_log`
List MailPlus mail transaction log entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.Audit.TransactionLog`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 50).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "offset": N,
"total": N, "is_migrating": bool}, "success": true}``.  
</div>
  



---


### `mailplus_queue`
List messages in the mail queue.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.MailPlusServer.Queue`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
Pagination offset (default 0).  
  
**_limit_** `int`  
Maximum results per page (default 50).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"items": [...], "total": N}, "success": true}``.  
</div>
  



---


