---
sidebar_position: 57
title: ✅ WebStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# WebStation
## Overview
Synology Web Station API client.  
  
Manages Web Station virtual hosts, PHP/Python runtimes,
web service portals, error pages, URL shortcuts, and
background tasks via the SYNO.WebStation.* WebAPI
endpoints.

Requires Web Station package installed on the target NAS.  
  
## Methods
### `ws_status`
Get Web Station status and backend information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Status`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Status including available backends (PHP, Python,
server), current backend, home share, and
web service configuration.  
</div>
  



---


### `ws_default`
Get default web server configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Default`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Default backend server, PHP settings, and
user directory configuration.  
</div>
  



---


### `ws_vhost_list`
List all virtual hosts.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.HTTP.VHost`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"hosts": [...], "total": N}, "success": true}``.
Each host includes name, document root, ports,
and PHP backend.  
</div>
  



---


### `ws_php_info`
Get PHP configuration and available extensions.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.PHP`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
PHP metadata, default settings, and available
PHP extensions list.  
</div>
  



---


### `ws_php_profile_list`
List PHP profiles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.PHP.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"profiles": [...], "total": N}, "success": true}``.
Each profile includes version, extensions, and
custom PHP settings.  
</div>
  



---


### `ws_python_info`
Get Python configuration metadata.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Python`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Python runtime metadata and available versions.  
</div>
  



---


### `ws_python_profile_list`
List Python profiles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Python.Profile`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"profiles": [...], "total": N}, "success": true}``.
Each profile includes Python version, virtualenv
path, and WSGI configuration.  
</div>
  



---


### `ws_error_page_list`
List custom error page profiles.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.ErrorPage`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"profiles": [...]}, "success": true}``.  
</div>
  



---


### `ws_portal_list`
List web service portals.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.WebService.Portal`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"portals": [...]}, "success": true}``.
Portals are the entry points that map hostnames
and ports to web services.  
</div>
  



---


### `ws_service_list`
List web services.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.WebService.Service`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"services": [...]}, "success": true}``.  
</div>
  



---


### `ws_package_list`
List packages with web service configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Package`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"packages": [...]}, "success": true}``.  
</div>
  



---


### `ws_shortcut_list`
List URL shortcuts/redirects.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Shortcut`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"shortcuts": [...]}, "success": true}``.  
</div>
  



---


### `ws_task_list`
List Web Station background tasks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.WebStation.Task`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"tasks": [...]}, "success": true}``.  
</div>
  



---


