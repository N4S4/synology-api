from __future__ import annotations
from typing import Optional
from . import base_api


class LogCenter(base_api.BaseApi):

    def logcenter(self) -> dict[str, object] | str:
        api_name = 'SYNO.LogCenter.RecvRule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_cnt(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'cnt_get'}

        return self.request_data(api_name, api_path, req_param)

    def client_status_eps(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'eps_get'}

        return self.request_data(api_name, api_path, req_param)

    def remote_log_archives(self) -> dict[str, object] | str:
        api_name = 'SYNO.LogCenter.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_remotearch_subfolder'}

        return self.request_data(api_name, api_path, req_param)

    def display_logs(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SyslogClient.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def setting_storage_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.LogCenter.Setting.Storage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def registry_send_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.LogCenter.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def history(self) -> dict[str, object] | str:
        api_name = 'SYNO.LogCenter.History'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
