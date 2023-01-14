from typing import Optional
from . import base_api_core


class DhcpServer(base_api_core.Core):
    def __init__(self,
                    ip_address : str,
                    port : str,
                    username : str,
                    password : str,
                    secure : bool = False,
                    cert_verify : bool = False,
                    dsm_version : int = 7,
                    debug : bool = True,
                    otp_code : Optional[str] = None
                ) -> None:
        super(DhcpServer, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        return

    def general_info(self) -> dict[str, object]:
        api_name = 'SYNO.Network.DHCPServer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'ifname': 'ovs_eth0'}

        return self.request_data(api_name, api_path, req_param)

    def vendor(self) -> dict[str, object]:
        api_name = 'SYNO.Network.DHCPServer.Vendor'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def pxe(self) -> dict[str, object]:
        api_name = 'SYNO.Network.DHCPServer.PXE'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def tftp(self) -> dict[str, object]:
        api_name = 'SYNO.Core.TFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self) -> dict[str, object]:
        api_name = 'SYNO.Core.Network.Bond'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self) -> dict[str, object]:
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
