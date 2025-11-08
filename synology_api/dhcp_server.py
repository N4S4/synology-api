"""
Synology DHCP Server API wrapper.

This module provides a Python interface for managing DHCP server, PXE, TFTP, and network
interfaces on Synology NAS devices.
"""

from __future__ import annotations

from typing import Optional

from . import base_api


class DhcpServer(base_api.BaseApi):
    """
    Core DHCP Server API implementation for Synology NAS.

    This class provides methods to retrieve and manage DHCP server, PXE, TFTP, and network
    interface information.
    """

    def general_info(self, ifname: str = 'ovs_eth0') -> dict[str, object] | str:
        """
        Get general DHCP server information for a given interface.

        Parameters
        ----------
        ifname : str, optional
            Interface name. Defaults to 'ovs_eth0'.

        Returns
        -------
        dict[str, object] or str
            General DHCP server information.
        """
        api_name = 'SYNO.Network.DHCPServer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)

    def vendor(self) -> dict[str, object] | str:
        """
        Get DHCP vendor information.

        Returns
        -------
        dict[str, object] or str
            DHCP vendor information.
        """
        api_name = 'SYNO.Network.DHCPServer.Vendor'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def pxe(self) -> dict[str, object] | str:
        """
        Get PXE server information.

        Returns
        -------
        dict[str, object] or str
            PXE server information.
        """
        api_name = 'SYNO.Network.DHCPServer.PXE'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def tftp(self) -> dict[str, object] | str:
        """
        Get TFTP server information.

        Returns
        -------
        dict[str, object] or str
            TFTP server information.
        """
        api_name = 'SYNO.Core.TFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self) -> dict[str, object] | str:
        """
        Get network bond interface information.

        Returns
        -------
        dict[str, object] or str
            Network bond interface information.
        """
        api_name = 'SYNO.Core.Network.Bond'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self) -> dict[str, object] | str:
        """
        Get network ethernet interface information.

        Returns
        -------
        dict[str, object] or str
            Network ethernet interface information.
        """
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def dhcp_clientlist(self, ifname: str = 'bond0') -> dict[str, object] | str:
        """
        Get DHCP client list for a given interface.

        Parameters
        ----------
        ifname : str, optional
            Interface name. Defaults to 'bond0'.

        Returns
        -------
        dict[str, object] or str
            DHCP client list.
        """
        api_name = 'SYNO.Network.DHCPServer.ClientList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)

    def dhcp_reservations(self, ifname: str = 'bond0') -> dict[str, object] | str:
        """
        Get DHCP reservations for a given interface.

        Parameters
        ----------
        ifname : str, optional
            Interface name. Defaults to 'bond0'.

        Returns
        -------
        dict[str, object] or str
            DHCP reservations.
        """
        api_name = 'SYNO.Network.DHCPServer.Reservation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)
