from __future__ import annotations
from typing import Optional
from . import base_api


class SecurityAdvisor(base_api.BaseApi):

    def general_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.SecurityAdvisor.Conf.Location'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_scan(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def checklist(self) -> dict[str, object] | str:
        api_name = 'SYNO.SecurityAdvisor.Conf.Checklist'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'group': 'home'}

        return self.request_data(api_name, api_path, req_param)

    def login_activity(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        api_name = 'SYNO.SecurityAdvisor.LoginActivity'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offser': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def advisor_config(self) -> dict[str, object] | str:
        api_name = 'SYNO.SecurityAdvisor.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def scan_config(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'group_enum', 'argGroup': 'custom'}

        return self.request_data(api_name, api_path, req_param)
