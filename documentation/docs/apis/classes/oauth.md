---
sidebar_position: 21
title: 🚧 OAuth
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# OAuth
:::warning
 
This API is not documented yet.
 
:::
## Overview
Interface for Synology OAuth API.

Provides methods to interact with OAuth clients, tokens, and logs.
## Methods
### `clients`
Retrieve the list of OAuth clients.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.OAUTH.Client` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The starting index of the client list. Default is 0.  
  
**_limit_** `int`  
The maximum number of clients to retrieve. Default is 20.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of clients or an error message.  

</div>



---


### `tokens`
Retrieve the list of OAuth tokens.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.OAUTH.Token` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The starting index of the token list. Default is 0.  
  
**_limit_** `int`  
The maximum number of tokens to retrieve. Default is 20.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of tokens or an error message.  

</div>



---


### `logs`
Retrieve the list of OAuth logs.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.OAUTH.Log` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_offset_** `int`  
The starting index of the log list. Default is 0.  
  
**_limit_** `int`  
The maximum number of logs to retrieve. Default is 20.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of logs or an error message.  

</div>



---


