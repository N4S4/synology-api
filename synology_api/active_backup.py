from . import auth as syn

import time

class ActiveBackupBusiness:
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False):

        self.session = syn.Authentication(ip_address, port, username, password, secure, cert_verify)

        self.session.login('Core')
        self.session.get_api_list('Core')
        self.session.get_api_list()

        self.request_data = self.session.request_data
        self.core_list = self.session.app_api_list
        self.gen_list = self.session.full_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

        print('You are now logged in!')

    def logout(self):
        self.session.logout('Core')

    def list_vm_hypervisor(self):
        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = { 'version': '1', 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
   
    def list_device_transfer_size(self):
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = { 'version': '1', 'method': 'list_device_transfer_size', 'time_start': int(time.time() - 86400), 'time_end': int(time.time()) }

        return self.request_data(api_name, api_path, req_param)


