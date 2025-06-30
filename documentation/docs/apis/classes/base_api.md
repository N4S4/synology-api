---
sidebar_position: 1
title: ✅ BaseApi
---
<!-- -------------------------------------------------------------------------------------- -->
<!-- Hand generated docs, due to nature of API, it doesn't follow template Class docstring. -->
<!-- -------------------------------------------------------------------------------------- -->

# BaseApi
## Overview
Base class to be used for all API implementations. Takes auth and connection information to create a session to the NAS.  

:::note
The **session** is created on instantiation.  
:::

:::tip
If accessing the NAS through a **remote connection**, it is advised to use _HTTPS_ to connect to it. Please make sure the certificate is valid.
:::

#### Parameters
<div class="padding-left--md">

_**ip_address**_ `str`  
    The IP/DNS address of the NAS.

_**port**_ `str`  
    The port of the NAS. Defaults to `5000`.

_**username**_ `str`  
    The username to use for authentication.

_**password**_ `str`  
    The password to use for authentication.

_**secure**_ `bool`  
    Whether to use HTTPS or not. Defaults to `False`.

_**cert_verify**_ `bool`  
    Whether to verify the SSL certificate or not. Defaults to `False`.

_**dsm_version**_ `int`  
    The DSM version. Defaults to `7`.

_**debug**_ `bool`
    Whether to print debug messages or not. Defaults to `True`.

_**otp_code**_ `str`  
    The OTP code to use for authentication. Defaults to `None`.
</div>

## Methods
### `logout`  
Close the current session.  

---


