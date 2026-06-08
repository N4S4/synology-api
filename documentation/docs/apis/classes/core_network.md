---
sidebar_position: 16
title: 🚧 CoreNetwork
description: "Core Network API implementation for Synology NAS." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# CoreNetwork
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Core Network API implementation for Synology NAS.  
  
Covers SYNO.Core.Network.* endpoints not implemented in SysInfo,
including 802.1X authentication, IPv6, MAC cloning, OVS, PPPoE relay,
static routes, traffic control, UPnP, VPN helpers, and Wake on LAN.  
  
## Methods
### `network_auth_get`
Get 802.1X network authentication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Authentication`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Current 802.1X authentication configuration.  
</div>
  



---


### `network_auth_set`
Set 802.1X network authentication settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Authentication`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable 802.1X authentication. Defaults to False.  
  
**_profile_** `str`  
Authentication profile name to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `network_auth_cert_get`
Get 802.1X authentication certificate information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Authentication.Cert`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Certificate details for 802.1X authentication.  
</div>
  



---


### `network_auth_cert_set`
Upload or update 802.1X authentication certificates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Authentication.Cert`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cert_path_** `str`  
Path to the client certificate file on the NAS.  
  
**_key_path_** `str`  
Path to the private key file on the NAS.  
  
**_ca_path_** `str`  
Path to the CA certificate file on the NAS.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `network_auth_cert_delete`
Delete 802.1X authentication certificates.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Authentication.Cert`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ethernet_external_get`
Get external ethernet configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Ethernet.External`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
External ethernet interface settings.  
</div>
  



---


### `ethernet_external_set`
Set external ethernet configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Ethernet.External`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_ifname_** `str`  
Interface name (e.g., 'eth0').  
  
**_enable_** `bool`  
Enable or disable the external interface. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ipv6_get`
Get IPv6 network settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
IPv6 configuration details.  
</div>
  



---


### `ipv6_set`
Set IPv6 network settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable IPv6. Defaults to True.  
  
**_type_** `str`  
IPv6 configuration type (e.g., 'auto', 'static', 'dhcpv6').  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ipv6_router_get`
Get IPv6 router advertisement configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6.Router`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
IPv6 router settings.  
</div>
  



---


### `ipv6_router_set`
Set IPv6 router advertisement configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6.Router`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable IPv6 router advertisements. Defaults to True.  
  
**_mode_** `str`  
Router advertisement mode.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ipv6_router_prefix_get`
Get IPv6 router prefix configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6.Router.Prefix`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
IPv6 router prefix settings.  
</div>
  



---


### `ipv6_router_prefix_set`
Set IPv6 router prefix configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.IPv6.Router.Prefix`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_prefix_** `str`  
IPv6 prefix address.  
  
**_prefix_length_** `int`  
Prefix length in bits. Defaults to 64.  
  
**_enable_auto_** `bool`  
Enable automatic prefix delegation. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `mac_clone_get`
Get MAC address cloning settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.MACClone`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
MAC cloning configuration.  
</div>
  



---


### `mac_clone_set`
Set MAC address cloning configuration.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.MACClone`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_ifname_** `str`  
Interface name to apply cloned MAC on.  
  
**_mac_** `str`  
MAC address to clone (e.g., 'AA:BB:CC:DD:EE:FF').  
  
**_enable_** `bool`  
Enable or disable MAC cloning. Defaults to False.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `ovs_get`
Get Open vSwitch (OVS) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.OVS`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
OVS configuration.  
</div>
  



---


### `ovs_set`
Set Open vSwitch (OVS) settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.OVS`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable OVS. Defaults to False.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `pppoe_relay_get`
Get PPPoE relay settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.PPPoE.Relay`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
PPPoE relay configuration.  
</div>
  



---


### `pppoe_relay_set`
Set PPPoE relay settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.PPPoE.Relay`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable PPPoE relay. Defaults to False.  
  
**_server_ifname_** `str`  
Server-side interface name.  
  
**_client_ifname_** `str`  
Client-side interface name.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `static_route_list`
List all static routes.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Router.Static.Route`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of configured static routes.  
</div>
  



---


### `static_route_get`
Get a specific static route by ID.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Router.Static.Route`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_route_id_** `str`  
The identifier of the static route.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Static route details.  
</div>
  



---


### `static_route_create`
Create a new static route.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Router.Static.Route`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_dest_** `str`  
Destination network address.  
  
**_gateway_** `str`  
Gateway address for the route.  
  
**_ifname_** `str`  
Interface name to bind the route to.  
  
**_mask_** `str`  
Subnet mask. Defaults to '255.255.255.0'.  
  
**_metric_** `int`  
Route metric. Defaults to 0.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `static_route_delete`
Delete a static route.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.Router.Static.Route`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_route_id_** `str`  
The identifier of the static route to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `traffic_control_router_rules_get`
Get router traffic control rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.RouterRules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Router-level traffic control rules.  
</div>
  



---


### `traffic_control_router_rules_list`
List router traffic control rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.RouterRules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of router traffic control rules.  
</div>
  



---


### `traffic_control_router_rules_set`
Set router traffic control rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.RouterRules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rules_** `str`  
JSON-encoded string of traffic control rules to apply.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `traffic_control_rules_get`
Get traffic control rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Traffic control rules configuration.  
</div>
  



---


### `traffic_control_rules_list`
List traffic control rules.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.Rules`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
List of traffic control rules.  
</div>
  



---


### `traffic_control_rules_create`
Create a traffic control rule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_protocol_** `str`  
Protocol to match (e.g., 'tcp', 'udp', 'all').  
  
**_port_** `int`  
Port number to match.  
  
**_upload_limit_** `int`  
Upload bandwidth limit in KB/s. 0 means unlimited. Defaults to 0.  
  
**_download_limit_** `int`  
Download bandwidth limit in KB/s. 0 means unlimited. Defaults to 0.  
  
**_enabled_** `bool`  
Whether the rule is active. Defaults to True.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `traffic_control_rules_delete`
Delete a traffic control rule.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.TrafficControl.Rules`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_rule_id_** `str`  
The identifier of the rule to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `upnp_server_get`
Get UPnP server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.UPnPServer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
UPnP server configuration.  
</div>
  



---


### `upnp_server_set`
Set UPnP server settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.UPnPServer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable the UPnP server. Defaults to False.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `wol_get`
Get Wake on LAN settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.WOL`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
WOL configuration.  
</div>
  



---


### `wol_set`
Set Wake on LAN settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.WOL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_enable_** `bool`  
Enable or disable WOL. Defaults to False.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `wol_wake`
Send a Wake on LAN magic packet to a device.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Core.Network.WOL`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_mac_** `str`  
MAC address of the target device (e.g., 'AA:BB:CC:DD:EE:FF').  
  
**_ifname_** `str`  
Network interface to send the packet from.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


