---
sidebar_position: 35
title: 🚧 Virtualization
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Virtualization
:::warning
 
This API is not documented yet.
 
:::
## Overview
API wrapper for Synology Virtual Machine Manager.  
  
Provides methods to manage tasks, networks, storage, hosts, VMs, and images.  
  
### Parameters
<div class="padding-left--md">
**_ip_address_** `str`  
IP address of the Synology NAS.  
  
**_port_** `str`  
Port number to connect to.  
  
**_username_** `str`  
DSM username.  
  
**_password_** `str`  
DSM password.  
  
**_secure_** `bool`  
Use HTTPS if True. Default is False.  
  
**_cert_verify_** `bool`  
Verify SSL certificate if True. Default is False.  
  
**_dsm_version_** `int`  
DSM version. Default is 7.  
  
**_debug_** `bool`  
Enable debug mode. Default is True.  
  
**_otp_code_** `str`  
One-time password for 2FA, if required.  
  

</div>
  
## Methods
### `get_task_list`
Get the list of virtualization tasks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Task.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`list of str`  
List of task IDs.  

</div>



---


### `clear_task`
Clear a specific task by its ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Task.Info` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID to clear.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the clear operation or error message.  

</div>



---


### `get_task_info`
Get information about a specific task.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Task.Info` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_taskid_** `str`  
Task ID to retrieve information for.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Task information or error message.  

</div>



---


### `get_network_group_list`
Get the list of network groups.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Network` 
</div>
  
#### Returns
<div class="padding-left--md">
`list of dict`  
List of network group information.  

</div>



---


### `get_storage_operation`
Get the list of storage operations.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Storage` 
</div>
  
#### Returns
<div class="padding-left--md">
`list of str`  
List of storage operation information.  

</div>



---


### `get_host_operation`
Get the list of host operations.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Host` 
</div>
  
#### Returns
<div class="padding-left--md">
`list of str`  
List of host operation information.  

</div>



---


### `get_vm_operation`
Get the list of virtual machines.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_** `bool`  
Whether to include additional information. Default is False.  
  

</div>
#### Returns
<div class="padding-left--md">
`list of dict`  
List of VM information.  

</div>



---


### `get_specific_vm_info`
Get information about a specific virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_additional_** `str or list of str`  
Additional fields to include.  
  
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
VM information or error message.  

</div>



---


### `set_vm_property`
Set properties for a virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  
**_autorun_** `int`  
Autorun setting (0: off, 1: last state, 2: on).  
  
**_description_** `str`  
VM description.  
  
**_new_guest_name_** `str`  
New VM name.  
  
**_vcpu_num_** `int`  
Number of virtual CPUs.  
  
**_vram_size_** `int`  
RAM size in MB.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the set operation or error message.  

</div>



---


### `delete_vm`
Delete a virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error message.  

</div>



---


### `vm_power_on`
Power on a virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Action` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  
**_host_id_** `str`  
Host ID.  
  
**_host_name_** `str`  
Host name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the power on operation or error message.  

</div>



---


### `vm_force_power_off`
Force power off a virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Action` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the power off operation or error message.  

</div>



---


### `vm_shut_down`
Shut down a virtual machine.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Action` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_guest_id_** `str`  
Guest VM ID.  
  
**_guest_name_** `str`  
Guest VM name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the shutdown operation or error message.  

</div>



---


### `get_images_list`
Get the list of VM images.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Image` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
Dictionary containing image information.  

</div>



---


### `delete_image`
Delete a VM image.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Image` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_image_id_** `str`  
Image ID.  
  
**_image_name_** `str`  
Image name.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the delete operation or error message.  

</div>



---


### `create_image`
Create a new VM image.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Virtualization.API.Guest.Image` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_auto_clean_task_** `bool`  
Whether to auto-clean the task after creation. Default is True.  
  
**_storage_names_** `str`  
Storage names.  
  
**_storage_ids_** `str`  
Storage IDs.  
  
**_type_** `str`  
Image type ('disk', 'vdsm', or 'iso').  
  
**_ds_file_path_** `str`  
File path (should begin with a shared folder).  
  
**_image_name_** `str`  
Name of the image.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Result of the create operation or error message.  

</div>



---


