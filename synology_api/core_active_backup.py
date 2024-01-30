from __future__ import annotations
from typing import Optional
from . import base_api

import time


class ActiveBackupBusiness(base_api.BaseApi):
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
        super(ActiveBackupBusiness, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                                   dsm_version, debug, otp_code)

    def list_vm_hypervisor(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def list_device_transfer_size(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_device_transfer_size',
                     'time_start': int(time.time() - 86400),
                     'time_end': int(time.time())}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                    'method': 'list',
                    'load_status': 'true',
                    'load_result': 'true'}

        return self.request_data(api_name, api_path, req_param)

    def list_storage(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Share'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_storage'}

        return self.request_data(api_name, api_path, req_param)
