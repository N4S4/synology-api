from . import base_api_core


class OAuth(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None):
        super(OAuth, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)

    def clients(self, offset=0, limit=20):
        api_name = 'SYNO.OAUTH.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def tokens(self, offset=0, limit=20):
        api_name = 'SYNO.OAUTH.Token'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset=0, limit=20):
        api_name = 'SYNO.OAUTH.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'action': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)
