---
sidebar_position: 5
title: ✅ Antivirus
description: "Synology Antivirus Essential API client." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# Antivirus
## Overview
Synology Antivirus Essential API client.  
  
Manages antivirus configuration, scan schedules,
quarantine, and system information via the
SYNO.AntiVirus.* WebAPI endpoints.

Requires Antivirus Essential installed on the target NAS.  
  
## Methods
### `config_get`
Get antivirus configuration.  
Retrieves current antivirus settings including whitelist,
scan behaviour, and virus action policy.  
#### Internal API
<div class="padding-left--md">

`SYNO.AntiVirus.Config`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Configuration dictionary with keys like ``enableWhitelist``,
``scanExtensionOnly``, ``smartScan``, ``updateBeforeScan``,
and ``virusAction`` (e.g. ``"do_nothing"``, ``"clean"``,
``"quarantine"``, ``"delete"``).  
</div>
  



---


### `schedule_load`
Get all scheduled scan jobs.  
Returns the list of configured scan schedules
with their activation status, trigger times,
and scan types.  
#### Internal API
<div class="padding-left--md">

`SYNO.AntiVirus.Schedule`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Dictionary with ``jobCount`` (int) and
``scheduleScanJobs`` (list of schedule objects),
each with keys ``activated``, ``triggerTime``,
``scanType``, and ``scanTarget``.  
</div>
  



---


### `quarantine_load`
Get quarantined files with pagination.  
Lists files currently held in quarantine.  
#### Internal API
<div class="padding-left--md">

`SYNO.AntiVirus.Quarantine`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_start_** `int`  
Starting offset for pagination (default 0).  
  
**_limit_** `int`  
Maximum items to return (default 200).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Dictionary with ``quarantineCount`` (int) and
``quarantineArray`` (list of quarantined file objects).  
</div>
  



---


### `general_sys_info`
Get antivirus system and definition information.  
Returns virus definition status, download progress,
licence expiration, and overall protection status.  
#### Internal API
<div class="padding-left--md">

`SYNO.AntiVirus.General`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Dictionary with keys like ``downloadSizeNow``,
``downloadSizeTotal``, ``licenceExpire``,
``button`` (UI status flags), and ``errormsg``.  
</div>
  



---


