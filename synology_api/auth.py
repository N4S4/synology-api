from typing import Optional
import requests
# Import error codes:
from .error_codes import error_codes, CODE_SUCCESS, CODE_UNKNOWN, download_station_error_codes, file_station_error_codes
from .error_codes import auth_error_codes, virtualization_error_codes#, surveillance_station_error_codes

from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from .exceptions import ConnectionError, HTTPError, JSONDecodeError, LoginError, LogoutError, DownloadStationError
from .exceptions import FileStationError, AudioStationError, ActiveBackupError, VirtualizationError, BackupError
from .exceptions import CertificateError, DHCPServerError, DirectoryServerError, DockerError, DriveAdminError
from .exceptions import LogCenterError, NoteStationError, OAUTHError, PhotosError, SecurityAdvisorError
from .exceptions import UniversalSearchError, USBCopyError, VirtualizationError, VPNError, CoreSysInfoError
from .exceptions import UndefinedError

USE_EXCEPTIONS: bool = True

class Authentication:
    def __init__(self,
                    ip_address: str,
                    port: str,
                    username: str,
                    password: str,
                    secure: bool = False,
                    cert_verify: bool = False,
                    dsm_version: int = 7,
                    debug: bool = True,
                    otp_code: Optional[str] = None
                ) -> None:
        self._ip_address : str = ip_address
        self._port : str = port
        self._username : str = username
        self._password : str = password
        self._sid : Optional[str] = None
        self._session_expire : bool = True
        self._verify : bool = cert_verify
        self._version : int = dsm_version
        self._debug : bool = debug
        self._otp_code : Optional[str] = otp_code
        if self._verify is False:
            disable_warnings(InsecureRequestWarning)
        schema = 'https' if secure else 'http'
        self._base_url: str = '%s://%s:%s/webapi/' % (schema, self._ip_address, self._port)

        self.full_api_list = {}
        self.app_api_list = {}
        return

    def verify_cert_enabled(self) -> bool:
        return self._verify

    def login(self, application:str) -> None:
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
        # Check request for error:
            try:
                session_request = requests.get(self._base_url + login_api, params, verify=self._verify)
                session_request.raise_for_status()
                session_request_json = session_request.json()
            except requests.exceptions.ConnectionError as e:
                if (USE_EXCEPTIONS == True):
                    raise ConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                if (USE_EXCEPTIONS == True):
                    raise HTTPError(error_message=str(e.args))
            except requests.exceptions.JSONDecodeError as e:
                if (USE_EXCEPTIONS == True):
                    raise JSONDecodeError(error_message=str(e.args))
        # Check dsm response for error:
            error_code = self._get_error_code(session_request_json)
            if not error_code:
                self._sid = session_request_json['data']['sid']
                self._session_expire = False
                if self._debug is True:
                    print('User logged in, new session started!')
            else:
                self._sid = None
                if self._debug is True:
                    print('Login failed: ' + self._get_error_message(error_code, 'Auth'))
                if (USE_EXCEPTIONS == True):
                    raise LoginError(error_code=error_code)
        return

    def logout(self, application:str) -> None:
        logout_api = 'auth.cgi?api=SYNO.API.Auth'
        param = {'version': self._version, 'method': 'logout', 'session': application}

   # Check request for errors:
        try:
            response = requests.get(self._base_url + logout_api, param, verify=self._verify)
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.ConnectionError as e:
            if (USE_EXCEPTIONS == True):
                raise ConnectionError(error_message=e.args[0])
        except requests.exceptions.HTTPError as e:
            if (USE_EXCEPTIONS == True):
                raise HTTPError(error_message=str(e.args))
        except requests.exceptions.JSONDecodeError as e:
            if (USE_EXCEPTIONS == True):
                raise JSONDecodeError(error_message=str(e.args))
    # Check dsm response for errors:
        error_code = self._get_error_code(response_json)
        self._session_expire = True
        self._sid = None
        if self._debug is True:
            if not error_code:
                if (self._debug == True):
                    print('Successfully logged out.')
            else:
                if (self._debug == True):
                    print('Logout failed: ' + self._get_error_message(error_code, 'Auth'))
                if (USE_EXCEPTIONS == True):
                    raise LogoutError(error_code=error_code)
        return

    def get_api_list(self, app:Optional[str]=None) -> None:
        query_path = 'query.cgi?api=SYNO.API.Info'
        list_query = {'version': '1', 'method': 'query', 'query': 'all'}

        if (USE_EXCEPTIONS == True):
        # Check request for error, and raise our own error.:
            try:
                response = requests.get(self._base_url + query_path, list_query, verify=self._verify).json()
            except requests.exceptions.ConnectionError as e:
                raise ConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                raise HTTPError(error_message=str(e.args))
            except requests.JSONDecodeError as e:
                raise JSONDecodeError(error_message=str(e.args))
        else:
        # Will raise it's own errors:
            response = requests.get(self._base_url + query_path, list_query, verify=self._verify).json()
        if app is not None:
            for key in response['data']:
                if app.lower() in key.lower():
                    self.app_api_list[key] = response['data'][key]
        else:
            self.full_api_list = response['data']

        return

    def show_api_name_list(self) -> None:
        prev_key = ''
        for key in self.full_api_list:
            if key != prev_key:
                print(key)
                prev_key = key
        return

    def show_json_response_type(self) -> None:
        for key in self.full_api_list:
            for sub_key in self.full_api_list[key]:
                if sub_key == 'requestFormat':
                    if self.full_api_list[key]['requestFormat'] == 'JSON':
                        print(key + '   Returns JSON data')
        return

    def search_by_app(self, app:str) -> None:
        print_check = 0
        for key in self.full_api_list:
            if app.lower() in key.lower():
                print(key)
                print_check += 1
                continue
        if print_check == 0:
            print('Not Found')
        return

    def request_data(self,
                        api_name: str,
                        api_path: str,
                        req_param:dict[str, object],
                        method:Optional[str] = None,
                        response_json: bool = True
                    ) -> str:  # 'post' or 'get'

        # Convert all boolean in string in lowercase because Synology API is waiting for "true" or "false"
        for k, v in req_param.items():
            if isinstance(v, bool):
                req_param[k] = str(v).lower()

        if method is None:
            method = 'get'

        req_param['_sid'] = self._sid

        url = ('%s%s' % (self._base_url, api_path)) + '?api=' + api_name

    # Do request and check for error:
        if (USE_EXCEPTIONS == True):
        # Catch and raise our own errors:
            try:
                if method == 'get':
                    response = requests.get(url, req_param, verify=self._verify)
                elif method == 'post':
                    response = requests.post(url, req_param, verify=self._verify)
            except requests.exceptions.ConnectionError as e:
                raise ConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                raise HTTPError(error_message=str(e.args))
        else:
        # Will raise it's own error:
            if method == 'get':
                response = requests.get(url, req_param, verify=self._verify)
            elif method == 'post':
                response = requests.post(url, req_param, verify=self._verify)


    # Check for error response from dsm:
        error_code = 0
        if (USE_EXCEPTIONS == True):
        # Catch a JSON Decode error:
            try:
                error_code = self._get_error_code(response.json())
            except requests.exceptions.JSONDecodeError as e:
                pass
        else:
        # Will raise it's own error:
            error_code = self._get_error_code(response.json())


        if error_code:
            if self._debug is True:
                print('Data request failed: ' + self._get_error_message(error_code, api_name))
        if (USE_EXCEPTIONS == True):
            # Download station error:
                if (api_name.find('DownloadStation') > -1):
                    raise DownloadStationError(error_code=error_code)
            # File station error:
                elif (api_name.find('FileStation') > -1):
                    raise FileStationError(error_code=error_code)
            # Audio station error:
                elif (api_name.find('AudioStation') > -1):
                    raise AudioStationError(error_code=error_code)
            # Active backup error:
                elif (api_name.find('ActiveBackup') > -1):
                    raise ActiveBackupError(error_code=error_code)
            # Virtualization error:
                elif (api_name.find('Virtualization') > -1):
                    raise VirtualizationError(error_code=error_code)
            # Syno backup error:
                elif (api_name.find('SYNO.Backup') > -1):
                    raise BackupError(error_code=error_code)
            # Core certificate error:
                elif (api_name.find('Core.Certificate') > -1):
                    raise CertificateError(error_code=error_code)
            # DHCP Server error:
                elif (api_name.find('DHCPServer') > -1 or api_name == 'SYNO.Core.TFTP'):
                    raise DHCPServerError(error_code=error_code)
            # Active Directory error:
                elif (api_name.find('ActiveDirectory') > -1 or api_name in ('SYNO.Auth.ForgotPwd', 'SYNO.Entry.Request')):
                    raise DirectoryServerError(error_code=error_code)
            # Docker Error:
                elif (api_name.find('Docker') > -1):
                    raise DockerError(error_code=error_code)
            # Synology drive admin error:
                elif (api_name.find('SynologyDrive') > -1 or api_name == 'SYNO.C2FS.Share'):
                    raise DriveAdminError(error_code=error_code)
            # Log center error:
                elif (api_name.find('LogCenter') > -1):
                    raise LogCenterError(error_code=error_code)
            # Note station error:
                elif (api_name.find('NoteStation') > -1):
                    raise NoteStationError(error_code=error_code)
            # OAUTH error:
                elif (api_name.find('SYNO.OAUTH') > -1):
                    raise OAUTHError(error_code=error_code)
            # Photo station error:
                elif (api_name.find('SYNO.Foto') > -1):
                    raise PhotosError(error_code=error_code)
            # Security advisor error:
                elif (api_name.find('SecurityAdvisor') > -1):
                    raise SecurityAdvisorError(error_code=error_code)
            # Universal search error:
                elif (api_name.find('SYNO.Finder') > -1):
                    raise UniversalSearchError(error_code=error_code)
            # USB Copy error:
                elif (api_name.find('SYNO.USBCopy') > -1):
                    raise USBCopyError(error_code=error_code)
            # VPN Server error:
                elif (api_name.find('VPNServer') > -1):
                    raise VPNError(error_code=error_code)
            # Core Sys Info:
                elif (api_name.find('SYNO.Core') > -1):
                    raise CoreSysInfoError(error_code=error_code)
                elif (api_name.find('SYNO.Storage') > -1):
                    raise CoreSysInfoError(error_code=error_code)
                elif (api_name.find('SYNO.ResourceMonitor') > -1):
                    raise CoreSysInfoError(error_code=error_code)
                elif (api_name in ('SYNO.Backup.Service.NetworkBackup', 'SYNO.Finder.FileIndexing.Status',
                                    'SYNO.S2S.Server.Pair')):
                    raise CoreSysInfoError(error_code=error_code)
            # Unhandled API:
                else:
                    raise UndefinedError(error_code=error_code, api_name=api_name)
    # Return response:
        if response_json is True:
            if (USE_EXCEPTIONS == True):
            # Catch and raise our own error:
                try:
                    return response.json()
                except requests.exceptions.JSONDecodeError as e:
                    raise JSONDecodeError(error_message=str(e.args))
            else:
            # Will raise it's own error if server doesn't send JSON.
                return response.json()
        else:
            return response

    @staticmethod
    def _get_error_code(response: dict[str, object]) -> int:
        if response.get('success'):
            code = CODE_SUCCESS
        else:
            code = response.get('error').get('code')
        return code

    @staticmethod
    def _get_error_message(code: int, api_name: str) -> str:
        if (code in error_codes.keys()):
            message = error_codes[code]
        elif (api_name == 'Auth'):
            message = auth_error_codes.get(code, "<UndefinedAuthError>")
        elif (api_name.find('DownloadStation') > -1):
            message = download_station_error_codes.get(code, "<UndefinedDownloadStationError>")
        elif (api_name.find('Virtualization') > -1):
            message = virtualization_error_codes.get(code,"<UndefinedVirtualizationError>")
        elif (api_name.find('FileStation') > -1):
            message = file_station_error_codes.get("<UndefinedFileStationError>")
        else:
            message = "<Undefined%sError>" % (api_name)
        return 'Error {} - {}'.format(code, message)

    @property
    def sid(self) -> Optional[str]:
        return self._sid

    @property
    def base_url(self) -> str:
        return self._base_url
