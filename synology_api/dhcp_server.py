from . import base_api_core


class dhcp_server(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(dhcp_server, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def general_info(self):
        api_name = 'SYNO.Network.DHCPServer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'ifname': 'ovs_eth0'}

        return self.request_data(api_name, api_path, req_param)

    def vendor(self):
        api_name = 'SYNO.Network.DHCPServer.Vendor'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def pxe(self):
        api_name = 'SYNO.Network.DHCPServer.PXE'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def tftp(self):
        api_name = 'SYNO.Core.TFTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network_bond(self):
        api_name = 'SYNO.Core.Network.Bond'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def network_ethernet(self):
        api_name = 'SYNO.Core.Network.Ethernet'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
