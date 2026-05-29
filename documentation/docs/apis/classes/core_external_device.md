---
sidebar_position: 15
title: 🚧 CoreExternalDevice
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# CoreExternalDevice
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core External Device API implementation for Synology NAS.  
  
Covers Bluetooth, printer (driver, network, USB, OAuth), and storage
(expansion unit, settings) endpoints not handled by other modules.  
  
## Methods
### `bluetooth_get`
Get Bluetooth adapter status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth get operation.  
</div>
  



---


### `bluetooth_set`
Enable or disable the Bluetooth adapter.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
The enable value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth set operation.  
</div>
  



---


### `bluetooth_device_list`
List discovered Bluetooth devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Device`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth device list operation.  
</div>
  



---


### `bluetooth_device_get`
Get information for a specific Bluetooth device.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Device`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_id_** `str`  
The device id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth device get operation.  
</div>
  



---


### `bluetooth_device_connect`
Connect to a Bluetooth device.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Device`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_id_** `str`  
The device id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth device connect operation.  
</div>
  



---


### `bluetooth_device_disconnect`
Disconnect a Bluetooth device.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Device`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_id_** `str`  
The device id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth device disconnect operation.  
</div>
  



---


### `bluetooth_settings_get`
Get Bluetooth settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Settings`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth settings get operation.  
</div>
  



---


### `bluetooth_settings_set`
Set Bluetooth settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Bluetooth.Settings`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_discoverable_** `str`  
The discoverable value.  
  
**_name_** `str`  
The name value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the bluetooth settings set operation.  
</div>
  



---


### `default_permission_get`
Get default permission settings for external devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.DefaultPermission`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the default permission get operation.  
</div>
  



---


### `default_permission_set`
Set default permission for external devices.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.DefaultPermission`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_permission_** `str`  
The permission value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the default permission set operation.  
</div>
  



---


### `printer_list`
List all printers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer list operation.  
</div>
  



---


### `printer_get`
Get printer information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_printer_id_** `str`  
The printer id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer get operation.  
</div>
  



---


### `printer_clean`
Clean the print queue for a printer.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_printer_id_** `str`  
The printer id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer clean operation.  
</div>
  



---


### `printer_driver_list`
List available printer drivers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Driver`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer driver list operation.  
</div>
  



---


### `printer_driver_get`
Get a specific printer driver.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Driver`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_driver_id_** `str`  
The driver id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer driver get operation.  
</div>
  



---


### `printer_network_list`
List network printers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Network`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer network list operation.  
</div>
  



---


### `printer_network_create`
Add a network printer.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Network`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_host_** `str`  
The host value.  
  
**_port_** `int`  
The port value.  
  
**_driver_id_** `str`  
The driver id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer network create operation.  
</div>
  



---


### `printer_network_delete`
Remove a network printer.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Network`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_printer_id_** `str`  
The printer id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer network delete operation.  
</div>
  



---


### `printer_network_host_list`
List network printer hosts discovered on the network.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.Network.Host`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer network host list operation.  
</div>
  



---


### `printer_oauth_get`
Get OAuth settings for cloud printing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.OAuth`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer oauth get operation.  
</div>
  



---


### `printer_oauth_set`
Set OAuth token for cloud printing.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.OAuth`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_token_** `str`  
The token value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer oauth set operation.  
</div>
  



---


### `printer_usb_list`
List USB printers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.USB`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer usb list operation.  
</div>
  



---


### `printer_usb_get`
Get USB printer information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.USB`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_printer_id_** `str`  
The printer id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer usb get operation.  
</div>
  



---


### `printer_usb_release`
Release a USB printer from the server.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Printer.USB`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_printer_id_** `str`  
The printer id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the printer usb release operation.  
</div>
  



---


### `storage_eunit_list`
List connected expansion units.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Storage.EUnit`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the storage eunit list operation.  
</div>
  



---


### `storage_eunit_get`
Get expansion unit details.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Storage.EUnit`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_unit_id_** `str`  
The unit id value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the storage eunit get operation.  
</div>
  



---


### `storage_setting_get`
Get external storage settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Storage.Setting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the storage setting get operation.  
</div>
  



---


### `storage_setting_set`
Set external storage settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.ExternalDevice.Storage.Setting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_auto_format_** `str`  
The auto format value.  
  
**_auto_mount_** `str`  
The auto mount value.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Result of the storage setting set operation.  
</div>
  



---


