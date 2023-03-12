import requests
from .error_codes import error_codes, CODE_SUCCESS, CODE_UNKNOWN
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


class Authentication:
    def __init__(self, ip_address: str, port: int, 
                 username: str, password: str, 
                 secure=False, cert_verify=False, 
                 dsm_version=7, debug=True,
                 otp_code: str = None):
        self._ip_address = ip_address
        self._port = port
        self._username = username
        self._password = password
        self._sid = None
        self._session_expire = True
        self._verify = cert_verify
        self._version = dsm_version
        self._debug = debug
        self._otp_code = otp_code
        if self._verify is False:
            disable_warnings(InsecureRequestWarning)
        schema = 'https' if secure else 'http'
        self._base_url = '%s://%s:%s/webapi/' % (schema, self._ip_address, self._port)

        self.full_api_list = {}
        self.app_api_list = {}

    def verify_cert_enabled(self):
        return self._verify

    def login(self, application: str):
        login_api = 'auth.cgi?api=SYNO.API.Auth'
        params = {'version': self._version, 'method': 'login', 'account': self._username,
                  'passwd': self._password, 'session': application, 'format': 'cookie'}
        if self._otp_code:
            params['otp_code'] = self._otp_code

        if not self._session_expire and self._sid is not None:
            self._session_expire = False
            if self._debug is True:
                print('User already logged in')
        else:
            session_request = requests.get(self._base_url + login_api, params, verify=self._verify)
            session_request_json = session_request.json()
            error_code = self._get_error_code(session_request_json)
            if not error_code:
                self._sid = session_request_json['data']['sid']
                self._session_expire = False
                if self._debug is True:
                    print('User logged in, new session started!')
            else:
                self._sid = None
                if self._debug is True:
                    print('Login failed: ' + self._get_error_message(error_code))

    def logout(self, application: str):
        logout_api = 'auth.cgi?api=SYNO.API.Auth'
        param = {'version': self._version, 'method': 'logout', 'session': application}

        response = requests.get(self._base_url + logout_api, param, verify=self._verify)
        error_code = self._get_error_code(response.json())
        self._session_expire = True
        self._sid = None
        if self._debug is True:
            if not error_code:
                print('Successfully logged out.')
            else:
                print('Logout failed: ' + self._get_error_message(error_code))

    def get_api_list(self, app: str = None):
        query_path = 'query.cgi?api=SYNO.API.Info'
        list_query = {'version': '1', 'method': 'query', 'query': 'all'}

        response = requests.get(self._base_url + query_path, list_query, verify=self._verify).json()

        if app is not None:
            for key in response['data']:
                if app.lower() in key.lower():
                    self.app_api_list[key] = response['data'][key]
        else:
            self.full_api_list = response['data']

        return

    def show_api_name_list(self):
        prev_key = ''
        for key in self.full_api_list:
            if key != prev_key:
                print(key)
                prev_key = key
        return

    def show_json_response_type(self):
        for key in self.full_api_list:
            for sub_key in self.full_api_list[key]:
                if sub_key == 'requestFormat':
                    if self.full_api_list[key]['requestFormat'] == 'JSON':
                        print(key + '   Returns JSON data')
        return

    def search_by_app(self, app: str):
        print_check = 0
        for key in self.full_api_list:
            if app.lower() in key.lower():
                print(key)
                print_check += 1
                continue
        if print_check == 0:
            print('Not Found')
        return

    def request_data(self, api_name: str, api_path: str, 
                     req_param: dict, method: str = None, response_json=True):  # 'post' or 'get'

        # Convert all boolean in string in lowercase because Synology API is waiting for "true" or "false"
        for k, v in req_param.items():
            if isinstance(v, bool):
                req_param[k] = str(v).lower()

        if method is None:
            method = 'get'

        req_param['_sid'] = self._sid

        url = f"{self._base_url}{api_path}?api={api_name}"

        if method == 'get':
            response = requests.get(url, req_param, verify=self._verify)
        elif method == 'post':
            response = requests.post(url, req_param, verify=self._verify)

        error_code = self._get_error_code(response.json())

        if error_code:
            if self._debug is True:
                print('Data request failed: ' + self._get_error_message(error_code))

        if response_json is True:
            return response.json()
        else:
            return response

    @staticmethod
    def _get_error_code(response: dict):
        if response.get('success'):
            code = CODE_SUCCESS
        else:
            code = response.get('error').get('code')
        return code

    @staticmethod
    def _get_error_message(code: int) -> str:
        message = error_codes.get(code, CODE_UNKNOWN)
        return 'Error {} - {}'.format(code, message)

    @property
    def sid(self):
        return self._sid

    @property
    def base_url(self):
        return self._base_url
