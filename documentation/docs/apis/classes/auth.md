---
sidebar_position: 
title: 🚧 Authentication
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
:::tip
 
This page contains documentation for the `Authentication` class and its subclasses:  
-  [AESCipher](#aescipher)   

 
:::
# Authentication
## Overview

## Methods
### `verify_cert_enabled`



---


### `login`



---


### `logout`



---


### `get_api_list`



---


### `show_api_name_list`



---


### `show_json_response_type`



---


### `search_by_app`



---


### `encrypt_params`



---


### `request_multi_datas`
Compound is a json structure that contains multiples requests, you can execute them sequential or parallel  
Example of compound:
compound = [
    {
        "api": "SYNO.Core.User",
        "method": "list",
        "version": self.core_list["SYNO.Core.User"]
    }
]  
#### Internal API
<div class="padding-left--md">
`hotfix` 
</div>
  



---


### `request_data`



---


### `sid`



---


### `base_url`



---


### `syno_token`



---


## AESCipher
## Overview
Encrypt with OpenSSL-compatible way
## Methods
### `encrypt`



---


