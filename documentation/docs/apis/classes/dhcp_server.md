---
sidebar_position: 10
title: 🚧 DhcpServer
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# DhcpServer
:::warning
 
This API is not documented yet.
 
:::
## Overview
Core DHCP Server API implementation for Synology NAS.

This class provides methods to retrieve and manage DHCP server, PXE, TFTP, and network
interface information.
## Methods
### `general_info`
Get general DHCP server information for a given interface.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Network.DHCPServer` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ifname_** `str`  
Interface name. Defaults to 'ovs_eth0'.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
General DHCP server information.  

</div>



---


### `vendor`
Get DHCP vendor information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Network.DHCPServer.Vendor` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DHCP vendor information.  

</div>



---


### `pxe`
Get PXE server information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Network.DHCPServer.PXE` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
PXE server information.  

</div>



---


### `tftp`
Get TFTP server information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.TFTP` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
TFTP server information.  

</div>



---


### `network_bond`
Get network bond interface information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Bond` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network bond interface information.  

</div>



---


### `network_ethernet`
Get network ethernet interface information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.Network.Ethernet` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
Network ethernet interface information.  

</div>



---


### `dhcp_clientlist`
Get DHCP client list for a given interface.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Network.DHCPServer.ClientList` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ifname_** `str`  
Interface name. Defaults to 'bond0'.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DHCP client list.  

</div>



---


### `dhcp_reservations`
Get DHCP reservations for a given interface.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Network.DHCPServer.Reservation` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_ifname_** `str`  
Interface name. Defaults to 'bond0'.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
DHCP reservations.  

</div>



---


