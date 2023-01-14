from typing import Optional
from . import base_api_core


class OAuth(base_api_core.Core):
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
        super(OAuth, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        return

    def clients(self, offset:int=0, limit:int=20) -> dict[str, object]:
        api_name = 'SYNO.OAUTH.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def tokens(self, offset:int=0, limit:int=20) -> dict[str, object]:
        api_name = 'SYNO.OAUTH.Token'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset:int=0, limit:int=20) -> dict[str, object]:
        api_name = 'SYNO.OAUTH.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'action': 'list',
                     'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)
