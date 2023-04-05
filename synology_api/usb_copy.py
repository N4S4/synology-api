from __future__ import annotations
from typing import Optional
from . import base_api_core


class USBCopy(base_api_core.Core):
    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None
                 ) -> None:
        super(USBCopy, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug,
                                      otp_code)
        return

    def usb_copy_info(self, id: int = 1) -> dict[str, object] | str:
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': id}

        return self.request_data(api_name, api_path, req_param)

    def toggle_usb_copy(self, enable: bool = True, id: int = 1) -> dict[str, object] | str:
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']

        if enable:
            enable = 'enable'
        elif not enable:
            enable = 'disable'
        else:
            return 'enable must be True or False'

        req_param = {'version': info['maxVersion'], 'method': enable, 'id': id}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset: int = 0, limit: int = 200) -> dict[str, object] | str:
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_log_list', 'offset': offset, 'limit': limit,
                     'log_filter': '{"log_desc_id_list":[0,1,2,3,10,11,100,101,102,103,104,105,1000]}'}

        return self.request_data(api_name, api_path, req_param)

    def global_settings(self) -> dict[str, object] | str:
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_global_setting'}

        return self.request_data(api_name, api_path, req_param)
