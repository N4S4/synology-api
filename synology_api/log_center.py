from . import base_api_core


class LogCenter(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7,
                 debug=True, otp_code=None):
        super(LogCenter, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def logcenter(self):
        api_name = 'SYNO.LogCenter.RecvRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_cnt(self):
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'cnt_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_eps(self):
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'eps_get'}

        return self.request_data(api_name, api_path, req_param)

    def remote_log_archives(self):
        api_name = 'SYNO.LogCenter.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_remotearch_subfolder'}

        return self.request_data(api_name, api_path, req_param)

    def display_logs(self):
        api_name = 'SYNO.Core.SyslogClient.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def setting_storage_list(self):
        api_name = 'SYNO.LogCenter.Setting.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def registry_send_list(self):
        api_name = 'SYNO.LogCenter.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def history(self):
        api_name = 'SYNO.LogCenter.History'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
