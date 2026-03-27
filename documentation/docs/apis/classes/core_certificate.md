---
sidebar_position: 8
title: 🚧 Certificate
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Certificate
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Synology DSM Core Certificate API Wrapper.  
  
This class provides methods to interact with the Synology DSM Core Certificate API,
allowing management of SSL certificates on a Synology NAS.  
  
### Parameters
<div class="padding-left--md">
**_ip_address_** `str`  
IP address or hostname of the Synology NAS.  
  
**_port_** `str`  
Port number to connect to.  
  
**_username_** `str`  
Username for authentication.  
  
**_password_** `str`  
Password for authentication.  
  
**_secure_** `bool`  
Use HTTPS if True, HTTP if False (default is False).  
  
**_cert_verify_** `bool`  
Verify SSL certificates (default is False).  
  
**_dsm_version_** `int`  
DSM version (default is 7).  
  
**_debug_** `bool`  
Enable debug output (default is True).  
  
**_otp_code_** `Optional[str]`  
One-time password for 2FA (default is None).  
  

</div>
  
## Methods
### `list_cert`
List all certificates.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
List of certificates.  

</div>



---


### `set_default_cert`
Set a certificate as the default.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cert_id_** `str`  
Certificate ID to set as default.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response.  

</div>



---


### `delete_certificate`
Delete one or more certificates.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ids_** `str or list[str]`  
Certificate ID or list of IDs to delete.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
API response.  

</div>



---


### `upload_cert`
Upload a certificate to the Synology NAS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_serv_key_** `str`  
Path to the server key file (default is "server.key").  
  
**_ser_cert_** `str`  
Path to the server certificate file (default is "server.crt").  
  
**_ca_cert_** `Optional[str]`  
Path to the CA certificate file (default is None).  
  
**_set_as_default_** `bool`  
Set as default certificate after upload (default is True).  
  
**_cert_id_** `Optional[str]`  
Certificate ID to update (default is None).  
  
**_desc_** `Optional[str]`  
Description for the certificate (default is None).  
  

</div>
#### Returns
<div class="padding-left--md">
`tuple[int, dict[str, object]]`  
HTTP status code and API response.  

</div>



---


### `set_certificate_for_service`
Set a certificate for a specific DSM service.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Certificate.Service` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_cert_id_** `str`  
Certificate ID to assign.  
  
**_service_name_** `str`  
Name of the service (default is "DSM Desktop Service").  
  

</div>
#### Returns
<div class="padding-left--md">
`tuple[int, dict[str, object]]`  
HTTP status code and API response.  

</div>



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
A BytesIO object containing the certificate archive, or None if export fails.  

</div>



---


