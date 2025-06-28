---
sidebar_position: 1
title: ✅ BaseApi
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# BaseApi
## Overview
Base class to be used for all API implementations.

Takes auth and connection information to create a session to the NAS.

The session is created on instanciation.

Parameters
----------
ip_address : str
    The IP/DNS address of the NAS.

port : str
    The port of the NAS. Defaults to `5000`.

username : str
    The username to use for authentication.

password : str
    The password to use for authentication.

secure : bool
    Whether to use HTTPS or not. Defaults to `False`.

cert_verify : bool
    Whether to verify the SSL certificate or not. Defaults to `False`.

dsm_version : int
    The DSM version. Defaults to `7`.

debug : bool
    Whether to print debug messages or not. Defaults to `True`.

otp_code : str
    The OTP code to use for authentication. Defaults to `None`
## Methods
### `logout`
Close current session.  
  
#### Internal API
<div class="padding-left--md">
`hotfix` 
</div>
  



---


