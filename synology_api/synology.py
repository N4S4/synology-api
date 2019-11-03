#!/usr/bin/python3

import requests


class Synology:
    class AlreadyLoggedInError(ConnectionRefusedError):
        pass

    class NotLoggedInError(PermissionError):
        pass

    app = None

    def __init__(self, ipaddr, port, username, password):
        self.ipaddr = ipaddr
        self.port = port
        self.user = username
        self.passwd = password
        self.sid = None
        self.session_expire = True
        self.session = None
        self._log_api = '/auth.cgi?api=SYNO.API.Auth'
        self.url = 'http://{ip}:{p}/webapi'.format(ip=self.ipaddr, p=self.port)

        self.full_api_dict = {}
        self.app_api_dict = {}

    def _response(self, urlpath, param):
        return requests.get(self.url + urlpath, param)

    def app(self):
        raise NotImplementedError("Application undefined.")

    def login(self, app):
        param = {'version': '2', 'method': 'login', 'account': self.user,
                 'passwd': self.passwd, 'session': app, 'format': 'cookie'}

        if not self.session_expire:
            if self.sid is not None:
                self.session_expire = False
                raise self.AlreadyLoggedInError("Already logged in.")

        self.session = self._response(self._log_api, param)
        self.sid = self.session.json()['data']['sid']
        self.session_expire = False
        return True

    def logout(self, app):
        param = {'version': '2', 'method': 'logout', 'session': app}

        response = self._response(self._log_api, param)
        self.session_expire = True
        self.sid = None
        respjson = response.json()
        if 'success' in respjson.keys():
            return respjson['success']
        else:
            raise KeyError("No 'success' field in response.")

    def populate_api_dict(self, app=None):
        querydict = {'version': '1', 'method': 'query', 'query': 'all'}

        response = self._response('/query.cgi?api=SYNO.API.Info', querydict)

        self.full_api_dict = response.json()['data']
        if self.app is not None:
            for key in self.full_api_dict:
                if app.lower() in key.lower():
                    self.app_api_dict[key] = self.full_api_dict[key]
        else:
            self.app_api_dict = self.full_api_dict

    def json_response(self):
        if self.full_api_dict is {}:
            self.populate_api_dict(None)

        for key in self.full_api_dict.keys():
            for subkey in self.full_api_dict[key].keys():
                if self.full_api_dict[key][subkey] == 'JSON':
                    return self.full_api_dict[key]

    def search_by_app(self, app):
        data = []
        check = 0
        for key in self.full_api_dict:
            if app.lower() in key.lower():
                data.append(key)
        return data

    def api_request(self, api_name, api_method, param=None):
        r = {'app': self.app(), 'api_name': api_name, 'api_method': api_method}
        if param is not None:
            r.update(param)
        return r
    
    @classmethod
    def api_call(self, method=None, response_json=True):
        def decorator_api_call(func):
            global method
            reqdata = func()
            print(type(func))
            api_str = 'SYNO.{a}.{m}'.format(a=reqdata['app'],
                                            m=reqdata['api_name'])
            api_path = self.app_api_dict['path']
            req_param = {'version': self.app_api_dict['maxVersion'],
                         'method': reqdata['api_method']}
            if method not in ['post', 'get']:
                method = 'get'

            # synology expects strings "true" and "false" for bools
            for k, v in req_param.items():
                if isinstance(v, bool):
                    req_param[k] = str(v).lower()

            req_param['_sid'] = self.sid

            response = None
            requrl = '{u}{p}?api={s}'.format(u=self.url, p=api_path, s=api_str)
            if method is 'get':
                response = requests.get(requrl, req_param)
            else:
                response = requests.post(requrl, req_param)

            if response_json:
                return response.json()
            else:
                return response

        return decorator_api_call
