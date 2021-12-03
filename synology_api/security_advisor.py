from . import base_api_core


class SecurityAdvisor(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(SecurityAdvisor, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code=None)

    def general_info(self):
        api_name = 'SYNO.SecurityAdvisor.Conf.Location'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_scan(self):
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def checklist(self):
        api_name = 'SYNO.SecurityAdvisor.Conf.Checklist'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'group': 'home'}

        return self.request_data(api_name, api_path, req_param)

    def login_activity(self, offset=0, limit=20):
        api_name = 'SYNO.SecurityAdvisor.LoginActivity'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offser': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def advisor_config(self):
        api_name = 'SYNO.SecurityAdvisor.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def scan_config(self):
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'group_enum', 'argGroup': 'custom'}

        return self.request_data(api_name, api_path, req_param)
