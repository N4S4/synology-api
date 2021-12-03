from . import base_api_core


class USB_Copy(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(USB_Copy, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def usb_copy_info(self, id=1):
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': id}

        return self.request_data(api_name, api_path, req_param)

    def toggle_usb_copy(self, enable=True, id=1):
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

    def logs(self, offset=0, limit=200):
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_log_list', 'offset': offset, 'limit': limit,
                     'log_filter': '{"log_desc_id_list":[0,1,2,3,10,11,100,101,102,103,104,105,1000]}'}

        return self.request_data(api_name, api_path, req_param)

    def global_settings(self):
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_global_setting'}

        return self.request_data(api_name, api_path, req_param)
