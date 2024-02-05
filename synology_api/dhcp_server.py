from __future__ import annotations

from typing import Optional

from . import base_api


class DhcpServer(base_api.BaseApi):

    def general_info(self, ifname:str = 'ovs_eth0') -> dict[str, object] | str:
        api_name = 'SYNO.Network.DHCPServer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)

    def vendor(self) -> dict[str, object] | str:
        api_name = 'SYNO.Network.DHCPServer.Vendor'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def pxe(self) -> dict[str, object] | str:
        api_name = 'SYNO.Network.DHCPServer.PXE'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def tftp(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.TFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Bond'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def dhcp_clientlist(self, ifname:str = 'bond0') -> dict[str, object] | str:
        api_name = 'SYNO.Network.DHCPServer.ClientList'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)

    def dhcp_reservations(self, ifname:str = 'bond0') -> dict[str, object] | str:
        api_name = 'SYNO.Network.DHCPServer.Reservation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'ifname': ifname}

        return self.request_data(api_name, api_path, req_param)
