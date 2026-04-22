"""
Synology Core Network API wrapper.

This module provides a Python interface for managing network configuration
on Synology NAS devices, covering endpoints not already present in core_sys_info.py.
"""

from __future__ import annotations
from typing import Optional
from . import base_api
import json


class CoreNetwork(base_api.BaseApi):
    """
    Core Network API implementation for Synology NAS.

    Covers SYNO.Core.Network.* endpoints not implemented in SysInfo,
    including 802.1X authentication, IPv6, MAC cloning, OVS, PPPoE relay,
    static routes, traffic control, UPnP, VPN helpers, and Wake on LAN.
    """

    # ------------------------------------------------------------------
    # SYNO.Core.Network.Authentication — 802.1X network authentication
    # ------------------------------------------------------------------

    def network_auth_get(self) -> dict[str, object] | str:
        """
        Get 802.1X network authentication settings.

        Returns
        -------
        dict[str, object] or str
            Current 802.1X authentication configuration.
        """
        api_name = 'SYNO.Core.Network.Authentication'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_auth_set(
        self,
        enable: bool = False,
        profile: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set 802.1X network authentication settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable 802.1X authentication. Defaults to False.
        profile : str, optional
            Authentication profile name to apply.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Authentication'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if profile is not None:
            req_param['profile'] = profile

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.Authentication.Cert — authentication certificates
    # ------------------------------------------------------------------

    def network_auth_cert_get(self) -> dict[str, object] | str:
        """
        Get 802.1X authentication certificate information.

        Returns
        -------
        dict[str, object] or str
            Certificate details for 802.1X authentication.
        """
        api_name = 'SYNO.Core.Network.Authentication.Cert'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_auth_cert_set(
        self,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
        ca_path: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Upload or update 802.1X authentication certificates.

        Parameters
        ----------
        cert_path : str, optional
            Path to the client certificate file on the NAS.
        key_path : str, optional
            Path to the private key file on the NAS.
        ca_path : str, optional
            Path to the CA certificate file on the NAS.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Authentication.Cert'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if cert_path is not None:
            req_param['cert_path'] = cert_path
        if key_path is not None:
            req_param['key_path'] = key_path
        if ca_path is not None:
            req_param['ca_path'] = ca_path

        return self.request_data(api_name, api_path, req_param)

    def network_auth_cert_delete(self) -> dict[str, object] | str:
        """
        Delete 802.1X authentication certificates.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Authentication.Cert'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.Ethernet.External — external ethernet config
    # ------------------------------------------------------------------

    def ethernet_external_get(self) -> dict[str, object] | str:
        """
        Get external ethernet configuration.

        Returns
        -------
        dict[str, object] or str
            External ethernet interface settings.
        """
        api_name = 'SYNO.Core.Network.Ethernet.External'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ethernet_external_set(
        self,
        ifname: Optional[str] = None,
        enable: bool = True
    ) -> dict[str, object] | str:
        """
        Set external ethernet configuration.

        Parameters
        ----------
        ifname : str, optional
            Interface name (e.g., 'eth0').
        enable : bool, optional
            Enable or disable the external interface. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Ethernet.External'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if ifname is not None:
            req_param['ifname'] = ifname

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.IPv6 — IPv6 settings
    # ------------------------------------------------------------------

    def ipv6_get(self) -> dict[str, object] | str:
        """
        Get IPv6 network settings.

        Returns
        -------
        dict[str, object] or str
            IPv6 configuration details.
        """
        api_name = 'SYNO.Core.Network.IPv6'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ipv6_set(
        self,
        enable: bool = True,
        type: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set IPv6 network settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable IPv6. Defaults to True.
        type : str, optional
            IPv6 configuration type (e.g., 'auto', 'static', 'dhcpv6').

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.IPv6'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if type is not None:
            req_param['type'] = type

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.IPv6.Router — IPv6 router config
    # ------------------------------------------------------------------

    def ipv6_router_get(self) -> dict[str, object] | str:
        """
        Get IPv6 router advertisement configuration.

        Returns
        -------
        dict[str, object] or str
            IPv6 router settings.
        """
        api_name = 'SYNO.Core.Network.IPv6.Router'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ipv6_router_set(
        self,
        enable: bool = True,
        mode: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set IPv6 router advertisement configuration.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable IPv6 router advertisements. Defaults to True.
        mode : str, optional
            Router advertisement mode.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.IPv6.Router'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if mode is not None:
            req_param['mode'] = mode

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.IPv6.Router.Prefix — IPv6 router prefix config
    # ------------------------------------------------------------------

    def ipv6_router_prefix_get(self) -> dict[str, object] | str:
        """
        Get IPv6 router prefix configuration.

        Returns
        -------
        dict[str, object] or str
            IPv6 router prefix settings.
        """
        api_name = 'SYNO.Core.Network.IPv6.Router.Prefix'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ipv6_router_prefix_set(
        self,
        prefix: Optional[str] = None,
        prefix_length: int = 64,
        enable_auto: bool = True
    ) -> dict[str, object] | str:
        """
        Set IPv6 router prefix configuration.

        Parameters
        ----------
        prefix : str, optional
            IPv6 prefix address.
        prefix_length : int, optional
            Prefix length in bits. Defaults to 64.
        enable_auto : bool, optional
            Enable automatic prefix delegation. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.IPv6.Router.Prefix'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'prefix_length': prefix_length,
            'enable_auto': str(enable_auto).lower(),
        }
        if prefix is not None:
            req_param['prefix'] = prefix

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.MACClone — MAC address cloning
    # ------------------------------------------------------------------

    def mac_clone_get(self) -> dict[str, object] | str:
        """
        Get MAC address cloning settings.

        Returns
        -------
        dict[str, object] or str
            MAC cloning configuration.
        """
        api_name = 'SYNO.Core.Network.MACClone'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def mac_clone_set(
        self,
        ifname: Optional[str] = None,
        mac: Optional[str] = None,
        enable: bool = False
    ) -> dict[str, object] | str:
        """
        Set MAC address cloning configuration.

        Parameters
        ----------
        ifname : str, optional
            Interface name to apply cloned MAC on.
        mac : str, optional
            MAC address to clone (e.g., 'AA:BB:CC:DD:EE:FF').
        enable : bool, optional
            Enable or disable MAC cloning. Defaults to False.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.MACClone'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if ifname is not None:
            req_param['ifname'] = ifname
        if mac is not None:
            req_param['mac'] = mac

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.OVS — Open vSwitch settings
    # ------------------------------------------------------------------

    def ovs_get(self) -> dict[str, object] | str:
        """
        Get Open vSwitch (OVS) settings.

        Returns
        -------
        dict[str, object] or str
            OVS configuration.
        """
        api_name = 'SYNO.Core.Network.OVS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ovs_set(self, enable: bool = False) -> dict[str, object] | str:
        """
        Set Open vSwitch (OVS) settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable OVS. Defaults to False.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.OVS'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.PPPoE.Relay — PPPoE relay settings
    # ------------------------------------------------------------------

    def pppoe_relay_get(self) -> dict[str, object] | str:
        """
        Get PPPoE relay settings.

        Returns
        -------
        dict[str, object] or str
            PPPoE relay configuration.
        """
        api_name = 'SYNO.Core.Network.PPPoE.Relay'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def pppoe_relay_set(
        self,
        enable: bool = False,
        server_ifname: Optional[str] = None,
        client_ifname: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set PPPoE relay settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable PPPoE relay. Defaults to False.
        server_ifname : str, optional
            Server-side interface name.
        client_ifname : str, optional
            Client-side interface name.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.PPPoE.Relay'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }
        if server_ifname is not None:
            req_param['server_ifname'] = server_ifname
        if client_ifname is not None:
            req_param['client_ifname'] = client_ifname

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.Router.Static.Route — static route management
    # ------------------------------------------------------------------

    def static_route_list(self) -> dict[str, object] | str:
        """
        List all static routes.

        Returns
        -------
        dict[str, object] or str
            List of configured static routes.
        """
        api_name = 'SYNO.Core.Network.Router.Static.Route'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def static_route_get(self, route_id: str) -> dict[str, object] | str:
        """
        Get a specific static route by ID.

        Parameters
        ----------
        route_id : str
            The identifier of the static route.

        Returns
        -------
        dict[str, object] or str
            Static route details.
        """
        api_name = 'SYNO.Core.Network.Router.Static.Route'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'id': route_id,
        }

        return self.request_data(api_name, api_path, req_param)

    def static_route_create(
        self,
        dest: str,
        gateway: str,
        ifname: Optional[str] = None,
        mask: str = '255.255.255.0',
        metric: int = 0
    ) -> dict[str, object] | str:
        """
        Create a new static route.

        Parameters
        ----------
        dest : str
            Destination network address.
        gateway : str
            Gateway address for the route.
        ifname : str, optional
            Interface name to bind the route to.
        mask : str, optional
            Subnet mask. Defaults to '255.255.255.0'.
        metric : int, optional
            Route metric. Defaults to 0.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Router.Static.Route'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'create',
            'dest': dest,
            'gateway': gateway,
            'mask': mask,
            'metric': metric,
        }
        if ifname is not None:
            req_param['ifname'] = ifname

        return self.request_data(api_name, api_path, req_param)

    def static_route_delete(self, route_id: str) -> dict[str, object] | str:
        """
        Delete a static route.

        Parameters
        ----------
        route_id : str
            The identifier of the static route to delete.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.Router.Static.Route'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'id': route_id,
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.TrafficControl.RouterRules — router traffic control
    # ------------------------------------------------------------------

    def traffic_control_router_rules_get(self) -> dict[str, object] | str:
        """
        Get router traffic control rules.

        Returns
        -------
        dict[str, object] or str
            Router-level traffic control rules.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.RouterRules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def traffic_control_router_rules_list(self) -> dict[str, object] | str:
        """
        List router traffic control rules.

        Returns
        -------
        dict[str, object] or str
            List of router traffic control rules.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.RouterRules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def traffic_control_router_rules_set(self, rules: str) -> dict[str, object] | str:
        """
        Set router traffic control rules.

        Parameters
        ----------
        rules : str
            JSON-encoded string of traffic control rules to apply.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.RouterRules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'rules': rules,
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.TrafficControl.Rules — traffic control rules
    # ------------------------------------------------------------------

    def traffic_control_rules_get(self) -> dict[str, object] | str:
        """
        Get traffic control rules.

        Returns
        -------
        dict[str, object] or str
            Traffic control rules configuration.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.Rules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def traffic_control_rules_list(self) -> dict[str, object] | str:
        """
        List traffic control rules.

        Returns
        -------
        dict[str, object] or str
            List of traffic control rules.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.Rules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def traffic_control_rules_create(
        self,
        protocol: str,
        port: Optional[int] = None,
        upload_limit: int = 0,
        download_limit: int = 0,
        enabled: bool = True
    ) -> dict[str, object] | str:
        """
        Create a traffic control rule.

        Parameters
        ----------
        protocol : str
            Protocol to match (e.g., 'tcp', 'udp', 'all').
        port : int, optional
            Port number to match.
        upload_limit : int, optional
            Upload bandwidth limit in KB/s. 0 means unlimited. Defaults to 0.
        download_limit : int, optional
            Download bandwidth limit in KB/s. 0 means unlimited. Defaults to 0.
        enabled : bool, optional
            Whether the rule is active. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.Rules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'create',
            'protocol': protocol,
            'upload_limit': upload_limit,
            'download_limit': download_limit,
            'enabled': str(enabled).lower(),
        }
        if port is not None:
            req_param['port'] = port

        return self.request_data(api_name, api_path, req_param)

    def traffic_control_rules_delete(self, rule_id: str) -> dict[str, object] | str:
        """
        Delete a traffic control rule.

        Parameters
        ----------
        rule_id : str
            The identifier of the rule to delete.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.TrafficControl.Rules'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'id': rule_id,
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.UPnPServer — UPnP server settings
    # ------------------------------------------------------------------

    def upnp_server_get(self) -> dict[str, object] | str:
        """
        Get UPnP server settings.

        Returns
        -------
        dict[str, object] or str
            UPnP server configuration.
        """
        api_name = 'SYNO.Core.Network.UPnPServer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def upnp_server_set(self, enable: bool = False) -> dict[str, object] | str:
        """
        Set UPnP server settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable the UPnP server. Defaults to False.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.UPnPServer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Network.WOL — Wake on LAN
    # ------------------------------------------------------------------

    def wol_get(self) -> dict[str, object] | str:
        """
        Get Wake on LAN settings.

        Returns
        -------
        dict[str, object] or str
            WOL configuration.
        """
        api_name = 'SYNO.Core.Network.WOL'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def wol_set(self, enable: bool = False) -> dict[str, object] | str:
        """
        Set Wake on LAN settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable WOL. Defaults to False.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.WOL'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': str(enable).lower(),
        }

        return self.request_data(api_name, api_path, req_param)

    def wol_wake(self, mac: str, ifname: Optional[str] = None) -> dict[str, object] | str:
        """
        Send a Wake on LAN magic packet to a device.

        Parameters
        ----------
        mac : str
            MAC address of the target device (e.g., 'AA:BB:CC:DD:EE:FF').
        ifname : str, optional
            Network interface to send the packet from.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Network.WOL'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'wake',
            'mac': mac,
        }
        if ifname is not None:
            req_param['ifname'] = ifname

        return self.request_data(api_name, api_path, req_param)
