---
sidebar_position: 8
title: 🚧 Certificate
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Certificate
:::warning
 
This API is not documented yet.
 
:::
## Overview

## Methods
### `list_cert`



---


### `set_default_cert`



---


### `delete_certificate`



---


### `upload_cert`



---


### `set_certificate_for_service`



---


### `export_cert`
Export a certificate from the Synology NAS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cert_id_** `str`  
The certificate ID to export. This can be found in the list_cert() method.  
  

</div>
#### Returns
<div class="padding-left--md">
`Optional[BytesIO]`  
A BytesIO object containing the certificate archive.  

</div>



---


