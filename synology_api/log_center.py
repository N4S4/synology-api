from typing import Optional
from . import base_api_core


class LogCenter(base_api_core.Core):
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
        super(LogCenter, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        return

    def logcenter(self) -> dict[str, object]:
        api_name = 'SYNO.LogCenter.RecvRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_cnt(self) -> dict[str, object]:
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'cnt_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_eps(self) -> dict[str, object]:
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'eps_get'}

        return self.request_data(api_name, api_path, req_param)

    def remote_log_archives(self) -> dict[str, object]:
        api_name = 'SYNO.LogCenter.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_remotearch_subfolder'}

        return self.request_data(api_name, api_path, req_param)

    def display_logs(self) -> dict[str, object]:
        api_name = 'SYNO.Core.SyslogClient.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def setting_storage_list(self) -> dict[str, object]:
        api_name = 'SYNO.LogCenter.Setting.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def registry_send_list(self) -> dict[str, object]:
        api_name = 'SYNO.LogCenter.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def history(self) -> dict[str, object]:
        api_name = 'SYNO.LogCenter.History'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
