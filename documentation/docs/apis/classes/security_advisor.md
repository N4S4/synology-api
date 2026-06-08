---
sidebar_position: 44
title: 🚧 SecurityAdvisor
description: "Interface for Synology Security Advisor API." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# SecurityAdvisor
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Interface for Synology Security Advisor API.  
  
Provides methods to retrieve general info, scan results, checklists,
login activity, and configuration for Security Advisor.  
  
## Methods
### `general_info`
Retrieve general information about Security Advisor location configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Conf.Location`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing location configuration or an error message.  
</div>
  



---


### `security_scan`
Retrieve the current security scan configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing security scan configuration or an error message.  
</div>
  



---


### `checklist`
Retrieve the checklist for the Security Advisor.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Conf.Checklist`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing the checklist or an error message.  
</div>
  



---


### `login_activity`
Retrieve login activity records.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.LoginActivity`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_offset_** `int`  
The starting index of the login activity list. Default is 0.  
  
**_limit_** `int`  
The maximum number of records to retrieve. Default is 20.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing login activity records or an error message.  
</div>
  



---


### `advisor_config`
Retrieve Security Advisor configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing advisor configuration or an error message.  
</div>
  



---


### `scan_config`
Retrieve custom group enumeration for security scan configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.SecurityScan.Conf`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
The API response containing custom group enumeration or an error message.  
</div>
  



---


### `advisor_alert_set`
Set or update the configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Conf.Checklist.Alert`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.SecurityAdvisor.Conf.Checklist.Alert``.  
</div>
  



---


### `advisor_login_get`
Get user login activity log from Security Advisor.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.LoginActivity.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.SecurityAdvisor.LoginActivity.User``.  
</div>
  



---


### `advisor_report_create`
Create a new user group.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Report`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.SecurityAdvisor.Report``.  
</div>
  



---


### `advisor_report_list`
List snapshot usage entries.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Report`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.SecurityAdvisor.Report``.  
</div>
  



---


### `advisor_report_html_open`
Open a snapshot usage tracking session.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.SecurityAdvisor.Report.HTML`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict`  
API response from ``SYNO.SecurityAdvisor.Report.HTML``.  
</div>
  



---


