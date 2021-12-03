from . import base_api_core

import time


class ActiveBackupBusiness(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(ActiveBackupBusiness, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def list_vm_hypervisor(self):
        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def list_device_transfer_size(self):
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_device_transfer_size',
                     'time_start': int(time.time() - 86400),
                     'time_end': int(time.time()) }

        return self.request_data(api_name, api_path, req_param)
