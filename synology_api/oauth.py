from __future__ import annotations
from typing import Optional
from . import base_api


class OAuth(base_api.BaseApi):

    def clients(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        api_name = 'SYNO.OAUTH.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def tokens(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        api_name = 'SYNO.OAUTH.Token'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        api_name = 'SYNO.OAUTH.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'action': 'list',
                     'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)
