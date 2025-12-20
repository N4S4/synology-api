"""Provides authentication and API request handling for Synology DSM, including session management, encryption utilities, and error handling for various Synology services."""
from __future__ import annotations
from random import randint
from typing import Optional, Any, Union
import requests
import json

from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from .error_codes import error_codes, CODE_SUCCESS, download_station_error_codes, file_station_error_codes
from .error_codes import auth_error_codes, virtualization_error_codes
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from .exceptions import CoreError
from .exceptions import SynoConnectionError, HTTPError, JSONDecodeError, LoginError, LogoutError, DownloadStationError
from .exceptions import FileStationError, AudioStationError, ActiveBackupError, ActiveBackupMicrosoftError, VirtualizationError, BackupError
from .exceptions import CertificateError, CloudSyncError, DHCPServerError, DirectoryServerError, DockerError, DriveAdminError
from .exceptions import LogCenterError, NoteStationError, OAUTHError, PhotosError, SecurityAdvisorError, TaskSchedulerError, EventSchedulerError
from .exceptions import UniversalSearchError, USBCopyError, VPNError, CoreSysInfoError, UndefinedError
import hashlib
from os import urandom
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import base64
import hashlib
import urllib
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
import base64
from noise.connection import NoiseConnection, Keypair
import time

USE_EXCEPTIONS: bool = True


class Authentication:
    """
    Handles authentication and API requests for Synology DSM.

    Parameters
    ----------
    ip_address : str
        The IP address of the Synology device.
    port : str
        The port to connect to.
    username : str
        The username for authentication.
    password : str
        The password for authentication.
    secure : bool, optional
        Whether to use HTTPS (default is False).
    cert_verify : bool, optional
        Whether to verify SSL certificates (default is False).
    dsm_version : int, optional
        DSM API version (default is 7).
    debug : bool, optional
        Enable debug output (default is True).
    otp_code : str, optional
        One-time password for 2FA.
    device_id : str, optional
        Device ID for device binding.
    device_name : str, optional
        Device name for device binding.
    """

    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 device_id: Optional[str] = None,
                 device_name: Optional[str] = None
                 ) -> None:
        """
        Initialize the Authentication object for Synology DSM.

        Parameters
        ----------
        ip_address : str
            The IP address of the Synology device.
        port : str
            The port to connect to.
        username : str
            The username for authentication.
        password : str
            The password for authentication.
        secure : bool, optional
            Whether to use HTTPS (default is False).
        cert_verify : bool, optional
            Whether to verify SSL certificates (default is False).
        dsm_version : int, optional
            DSM API version (default is 7).
        debug : bool, optional
            Enable debug output (default is True).
        otp_code : str, optional
            One-time password for 2FA (default is None).
        device_id : str, optional
            Device ID for device binding (default is None).
        device_name : str, optional
            Device name for device binding (default is None).

        Returns
        -------
        None
            Just setter, no return values.
        """
        self._ip_address: str = ip_address
        self._port: str = port
        self._username: str = username
        self._password: str = password
        self._secure: bool = secure
        self._sid: Optional[str] = None
        self._syno_token: Optional[str] = None
        self._session_expire: bool = True
        self._verify: bool = cert_verify
        self._version: int = dsm_version
        self._debug: bool = debug
        self._otp_code: Optional[str] = otp_code
        self._device_id: Optional[str] = device_id
        self._device_name: Optional[str] = device_name

        if self._verify is False:
            disable_warnings(InsecureRequestWarning)

        schema = 'https' if secure else 'http'

        self._base_url = '%s://%s:%s/webapi/' % (
            schema, self._ip_address, self._port)

        self.full_api_list = {}
        self.app_api_list = {}

    def get_ik_message(self) -> str:
        """
        Get the IK message for authentication.

        Returns
        -------
        str
            The IK message.
        """

        url = self._base_url + 'entry.cgi/SYNO.API.Auth.UIConfig'
        data = {
            "api": "SYNO.API.Auth.UIConfig",
            "method": "get",
            "version": "1"
        }
        response = requests.post(url, data=data, verify=self._verify)

        # Try to get cookie "_SSID"
        if response.status_code != 200:
            raise Exception("Failed to access the URL for IK message. Status code: {}".format(
                response.status_code))
        cookies = response.cookies
        if "_SSID" not in cookies:
            raise Exception("Cookie '_SSID' not found in the response.")
        _SSID_encoded = cookies["_SSID"]
        _SSID = self.decode_ssid_cookie(_SSID_encoded)

        private_bytes = X25519PrivateKey.generate().private_bytes_raw()

        noise = NoiseConnection.from_name(b"Noise_IK_25519_ChaChaPoly_BLAKE2b")
        noise.set_as_initiator()
        noise.set_keypair_from_private_bytes(Keypair.STATIC, private_bytes)
        noise.set_keypair_from_public_bytes(Keypair.REMOTE_STATIC, _SSID)

        noise.start_handshake()

        payload = json.dumps({
            "time": int(time.time()),
        }).encode('utf-8')

        message = noise.write_message(payload)
        ik_message = self.encode_ssid_cookie(message)

        return ik_message

    def verify_cert_enabled(self) -> bool:
        """
        Check if SSL certificate verification is enabled.

        Returns
        -------
        bool
            True if certificate verification is enabled, False otherwise.
        """
        return self._verify

    def login(self) -> None:
        """
        Log in to the Synology DSM and obtain a session ID and token.

        Raises
        ------
        SynoConnectionError
            If a connection error occurs.
        HTTPError
            If an HTTP error occurs.
        JSONDecodeError
            If the response cannot be decoded as JSON.
        LoginError
            If login fails due to an API error.
        """
        login_api = 'auth.cgi'
        params = {'api': "SYNO.API.Auth", 'version': self._version,
                  'method': 'login', 'enable_syno_token': 'yes', 'client': 'browser'}

        if self._version >= 7:
            params.update({'ik_message': self.get_ik_message()})

        params_enc = {
            'account': self._username,
            'enable_device_token': 'no',
            'logintype': 'local',
            'otp_code': '',
            'rememberme': 0,
            'passwd': self._password,
            'session': 'webui',  # Hardcoded for handle non administrator users API usage
            'format': 'cookie'
        }
        if self._secure:
            params.update(params_enc)
        else:
            encrypted_params = self.encrypt_params(params_enc)
            params.update(encrypted_params)

        if self._otp_code:
            params['otp_code'] = self._otp_code
        if self._device_id is not None and self._device_name is not None:
            params['device_id'] = self._device_id
            params['device_name'] = self._device_name
        if self._device_id is not None and self._device_name is None or self._device_id is None and self._device_name is not None:
            print("device_id and device_name must be set together")

        if not self._session_expire and self._sid is not None:
            self._session_expire = False
            if self._debug is True:
                print('User already logged in')
        else:
            # Check request for error:
            session_request_json: dict[str, object] = {}
            if USE_EXCEPTIONS:
                try:
                    session_request = requests.post(
                        self._base_url + login_api, data=params, verify=self._verify)
                    session_request.raise_for_status()
                    session_request_json = session_request.json()
                except requests.exceptions.ConnectionError as e:
                    raise SynoConnectionError(error_message=e.args[0])
                except requests.exceptions.HTTPError as e:
                    raise HTTPError(error_message=str(e.args))
                except requests.exceptions.JSONDecodeError as e:
                    raise JSONDecodeError(error_message=str(e.args))
            else:
                # Will raise its own errors:
                session_request = requests.post(
                    self._base_url + login_api, data=params, verify=self._verify)
                session_request_json = session_request.json()

            # Check dsm response for error:
            error_code = self._get_error_code(session_request_json)
            if not error_code:
                self._sid = session_request_json['data']['sid']
                self._syno_token = session_request_json['data']['synotoken']
                self._session_expire = False
                if self._debug is True:
                    print('User logged in, new session started!')
            else:
                self._sid = None
                if self._debug is True:
                    print('Login failed: ' +
                          self._get_error_message(error_code, 'Auth'))
                if USE_EXCEPTIONS:
                    raise LoginError(error_code=error_code)
        return

    def logout(self) -> None:
        """
        Log out from the Synology DSM and invalidate the session.

        Raises
        ------
        SynoConnectionError
            If a connection error occurs.
        HTTPError
            If an HTTP error occurs.
        JSONDecodeError
            If the response cannot be decoded as JSON.
        LogoutError
            If logout fails due to an API error.
        """
        logout_api = 'auth.cgi?api=SYNO.API.Auth'
        param = {'version': self._version,
                 'method': 'logout', 'session': 'webui'}

        if USE_EXCEPTIONS:
            try:
                response = requests.get(
                    self._base_url + logout_api, param, verify=self._verify)
                response.raise_for_status()
                response_json = response.json()
                error_code = self._get_error_code(response_json)
            except requests.exceptions.ConnectionError as e:
                raise SynoConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                raise HTTPError(error_message=str(e.args))
            except requests.exceptions.JSONDecodeError as e:
                raise JSONDecodeError(error_message=str(e.args))
        else:
            response = requests.get(
                self._base_url + logout_api, param, verify=self._verify)
            error_code = self._get_error_code(response.json())
        self._session_expire = True
        self._sid = None
        if self._debug is True:
            if not error_code:
                print('Successfully logged out.')
            else:
                print('Logout failed: ' +
                      self._get_error_message(error_code, 'Auth'))
        if USE_EXCEPTIONS and error_code:
            raise LogoutError(error_code=error_code)

        return

    def get_api_list(self, app: Optional[str] = None) -> None:
        """
        Retrieve the list of available APIs from the Synology DSM.

        Parameters
        ----------
        app : str, optional
            Filter APIs by application name.

        Raises
        ------
        SynoConnectionError
            If a connection error occurs.
        HTTPError
            If an HTTP error occurs.
        JSONDecodeError
            If the response cannot be decoded as JSON.
        """
        query_path = 'query.cgi?api=SYNO.API.Info'
        list_query = {'version': '1', 'method': 'query', 'query': 'all'}

        if USE_EXCEPTIONS:
            # Check request for error, and raise our own error.:
            try:
                response = requests.get(
                    self._base_url + query_path, list_query, verify=self._verify)
                response.raise_for_status()
                response_json = response.json()
            except requests.exceptions.ConnectionError as e:
                raise SynoConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                raise HTTPError(error_message=str(e.args))
            except requests.JSONDecodeError as e:
                raise JSONDecodeError(error_message=str(e.args))
        else:
            # Will raise its own errors:
            response_json = requests.get(
                self._base_url + query_path, list_query, verify=self._verify).json()

        if app is not None:
            for key in response_json['data']:
                if app.lower() in key.lower():
                    self.app_api_list[key] = response_json['data'][key]
        else:
            self.full_api_list = response_json['data']

        return

    def show_api_name_list(self) -> None:
        """Print the list of available API names."""
        prev_key = ''
        for key in self.full_api_list:
            if key != prev_key:
                print(key)
                prev_key = key
        return

    def show_json_response_type(self) -> None:
        """Print API names that return JSON data."""
        for key in self.full_api_list:
            for sub_key in self.full_api_list[key]:
                if sub_key == 'requestFormat':
                    if self.full_api_list[key]['requestFormat'] == 'JSON':
                        print(key + '   Returns JSON data')
        return

    def search_by_app(self, app: str) -> None:
        """
        Search and print API names containing the specified application name.

        Parameters
        ----------
        app : str
            Application name to search for.
        """
        print_check = 0
        for key in self.full_api_list:
            if app.lower() in key.lower():
                print(key)
                print_check += 1
                continue
        if print_check == 0:
            print('Not Found')
        return

    def _random_AES_passphrase(self, length):
        """
        Generate a random passphrase for AES encryption.

        Parameters
        ----------
        length : int
            Length of the passphrase.

        Returns
        -------
        bytes
            Randomly generated passphrase.
        """
        available = ('0123456789'
                     'abcdefghijklmnopqrstuvwxyz'
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                     '~!@#$%^&*()_+-/')
        key = b''

        while length > 0:
            key += available[randint(0, len(available) - 1)].encode('utf-8')
            length -= 1

        return key

    def _get_enc_info(self):
        """
        Retrieve encryption information from the Synology API.

        Returns
        -------
        dict
            Encryption information including public key and cipher details.
        """
        api_name = 'SYNO.API.Encryption'
        req_params = {
            "method": "getinfo",
            "version": 1,
            "format": "module"
        }
        response = self.request_data(api_name, "encryption.cgi", req_params)
        return response["data"]

    def _encrypt_RSA(self, modulus, passphrase, text):
        """
        Encrypt text using RSA public key encryption.

        Parameters
        ----------
        modulus : int
            RSA modulus.
        passphrase : int
            RSA public exponent.
        text : str or bytes
            Text to encrypt.

        Returns
        -------
        bytes
            Encrypted ciphertext.
        """
        public_numbers = rsa.RSAPublicNumbers(passphrase, modulus)
        public_key = public_numbers.public_key(default_backend())

        if isinstance(text, str):
            text = text.encode('utf-8')

        ciphertext = public_key.encrypt(
            text,
            padding.PKCS1v15()
        )
        return ciphertext

    def _encrypt_AES(self, passphrase, text):
        """
        Encrypt text using AES encryption.

        Parameters
        ----------
        passphrase : bytes
            AES passphrase.
        text : str
            Text to encrypt.

        Returns
        -------
        bytes
            Encrypted ciphertext.
        """
        cipher = AESCipher(passphrase)

        return cipher.encrypt(text)

    def encrypt_params(self, params):
        """
        Encrypt login parameters using RSA and AES.

        Parameters
        ----------
        params : dict
            Parameters to encrypt.

        Returns
        -------
        dict
            Encrypted parameters suitable for login.
        """
        enc_info = self._get_enc_info()
        public_key = enc_info["public_key"]
        cipher_key = enc_info["cipherkey"]
        cipher_token = enc_info["ciphertoken"]
        server_time = enc_info["server_time"]
        random_passphrase = self._random_AES_passphrase(501)

        params[cipher_token] = server_time

        encrypted_passphrase = self._encrypt_RSA(int(public_key, 16),
                                                 int("10001", 16),
                                                 random_passphrase)

        encrypted_params = self._encrypt_AES(random_passphrase,
                                             urllib.parse.urlencode(params))

        enc_params = {
            "rsa": base64.b64encode(encrypted_passphrase).decode("utf-8"),
            "aes": base64.b64encode(encrypted_params).decode("utf-8")
        }

        return {cipher_key: json.dumps(enc_params)}

    def request_multi_datas(self,
                            compound: dict[object] = None,
                            method: Optional[str] = None,
                            # "sequential" or "parallel"
                            mode: Optional[str] = "sequential",
                            response_json: bool = True
                            ) -> dict[str, object] | str | list | requests.Response:  # 'post' or 'get'
        """
        Send multiple requests to the Synology API, either sequentially or in parallel.

        Parameters
        ----------
        compound : dict[object], optional
            A JSON structure containing multiple requests to be executed.
            Example:
            compound = [
                {
                    "api": "SYNO.Core.User",
                    "method": "list",
                    "version": self.core_list["SYNO.Core.User"]
                }
            ].
        method : str, optional
            The HTTP method to use ('get' or 'post'). Defaults to 'get' if not specified.
        mode : str, optional
            The execution mode for the requests, either "sequential" or "parallel".
            Defaults to "sequential".
        response_json : bool, optional
            Whether to return the response as JSON. If False, returns the raw response object.

        Returns
        -------
        dict[str, object] or str or list or requests.Response
            The response from the API, either as a JSON-decoded object, string, list, or the raw response.

        Raises
        ------
        SynoConnectionError
            If a connection error occurs.
        HTTPError
            If an HTTP error occurs.
        """
        api_name = 'hotfix'  # fix for docs_parser.py issue
        api_path = self.full_api_list['SYNO.Entry.Request']['path']
        api_version = self.full_api_list['SYNO.Entry.Request']['maxVersion']
        url = f"{self._base_url}{api_path}"

        req_param = {
            "api": "SYNO.Entry.Request",
            "method": "request",
            "version": f"{api_version}",
            "mode": mode,
            "stop_when_error": "true",
            "_sid": self._sid,
            "compound": json.dumps(compound)
        }

        if method is None:
            method = 'get'

        # Request need some headers to work properly
        # X-SYNO-TOKEN is the token that we get when we login
        # We get it from the self._syno_token variable and by param 'enable_syno_token':'yes' in the login request

        if method == 'get':
            response = requests.get(url, req_param, verify=self._verify, headers={
                                    "X-SYNO-TOKEN": self._syno_token})
        elif method == 'post':
            response = requests.post(url, req_param, verify=self._verify, headers={
                                     "X-SYNO-TOKEN": self._syno_token})

        if response_json is True:
            return response.json()
        else:
            return response

    def request_data(self,
                     api_name: str,
                     api_path: str,
                     req_param: dict[str, object],
                     method: Optional[str] = None,
                     data: MultiPartEncoderMonitor | MultipartEncoder | str | None = None,
                     response_json: bool = True
                     ) -> dict[str, object] | str | list | requests.Response:  # 'post' or 'get'
        """
        Send a request to the Synology API and handle errors based on the API name.

        Parameters
        ----------
        api_name : str
            The name of the Synology API to call.
        api_path : str
            The path to the API endpoint.
        req_param : dict[str, object]
            The parameters to include in the request.
        method : str, optional
            The HTTP method to use ('get' or 'post'). Defaults to 'get' if not specified.
        data : str, optional
         The data to send to upload a file like a torrent file.
        response_json : bool, optional
            Whether to return the response as JSON. If False, returns the raw response object.

        Returns
        -------
        dict[str, object] or str or list or requests.Response
            The response from the API, either as a JSON-decoded object, string, list, or the raw response.

        Raises
        ------
        SynoConnectionError
            If a connection error occurs.
        HTTPError
            If an HTTP error occurs.
        DownloadStationError, FileStationError, AudioStationError, ActiveBackupError, ActiveBackupMicrosoftError, VirtualizationError, BackupError, CloudSyncError, CertificateError, DHCPServerError, DirectoryServerError, DockerError, DriveAdminError, LogCenterError, NoteStationError, OAUTHError, PhotosError, SecurityAdvisorError, TaskSchedulerError, EventSchedulerError, UniversalSearchError, USBCopyError, VPNError, CoreError, CoreSysInfoError, UndefinedError
            If the API returns an error code specific to the API being called.
        """
        # Convert all boolean in string in lowercase because Synology API is waiting for "true" or "false"
        for k, v in req_param.items():
            if isinstance(v, bool):
                req_param[k] = str(v).lower()

        if method is None:
            method = 'get'

        req_param['_sid'] = self._sid

        url = ('%s%s' % (self._base_url, api_path)) + '?api=' + api_name

        # Do request and check for error:
        response: Optional[requests.Response] = None
        if USE_EXCEPTIONS:
            # Catch and raise our own errors:
            try:
                if method == 'get':
                    response = requests.get(url, req_param, verify=self._verify, headers={
                                            "X-SYNO-TOKEN": self._syno_token})
                elif method == 'post':
                    if data is None:
                        response = requests.post(url, req_param, verify=self._verify, headers={
                                                 "X-SYNO-TOKEN": self._syno_token})
                    else:
                        url = ('%s%s' % (self._base_url, api_path)) + \
                            '/' + api_name
                        response = requests.post(url, data=data, params=req_param, verify=self._verify, headers={
                                                 "Content-Type": data.content_type, "X-SYNO-TOKEN": self._syno_token})
                response.raise_for_status()
            except requests.exceptions.ConnectionError as e:
                raise SynoConnectionError(error_message=e.args[0])
            except requests.exceptions.HTTPError as e:
                raise HTTPError(error_message=str(e.args))
        else:
            # Will raise its own error:
            if method == 'get':
                response = requests.get(url, req_param, verify=self._verify, headers={
                                        "X-SYNO-TOKEN": self._syno_token})
            elif method == 'post':
                response = requests.post(url, req_param, verify=self._verify, headers={
                                         "X-SYNO-TOKEN": self._syno_token})
            response.raise_for_status()

        # Check for error response from dsm:
        error_code = 0
        if USE_EXCEPTIONS:
            # Catch a JSON Decode error:
            try:
                error_code = self._get_error_code(response.json())
            except requests.exceptions.JSONDecodeError:
                pass
        else:
            # Will raise its own error:
            error_code = self._get_error_code(response.json())

        if error_code:
            if self._debug is True:
                print('Data request failed: ' +
                      self._get_error_message(error_code, api_name))

            if USE_EXCEPTIONS:
                # Download station error:
                if api_name.find('DownloadStation') > -1:
                    raise DownloadStationError(error_code=error_code)
                # File station error:
                elif api_name.find('FileStation') > -1:
                    raise FileStationError(error_code=error_code)
                # Audio station error:
                elif api_name.find('AudioStation') > -1:
                    raise AudioStationError(error_code=error_code)
                # ABM (ActiveBackupOffice365) error:
                elif api_name.find('ActiveBackupOffice365') > -1:
                    raise ActiveBackupMicrosoftError(error_code=error_code)
                # Active backup error:
                elif api_name.find('ActiveBackup') > -1:
                    raise ActiveBackupError(error_code=error_code)
                # Virtualization error:
                elif api_name.find('Virtualization') > -1:
                    raise VirtualizationError(error_code=error_code)
                # Syno backup error:
                elif api_name.find('SYNO.Backup') > -1:
                    raise BackupError(error_code=error_code)
                # CloudSync error:
                elif api_name.find('CloudSync') > -1:
                    raise CloudSyncError(error_code=error_code)
                # Core certificate error:
                elif api_name.find('Core.Certificate') > -1:
                    raise CertificateError(error_code=error_code)
                # DHCP Server error:
                elif api_name.find('DHCPServer') > -1 or api_name == 'SYNO.Core.TFTP':
                    raise DHCPServerError(error_code=error_code)
                # Active Directory error:
                elif api_name.find('ActiveDirectory') > -1 or api_name in ('SYNO.Auth.ForgotPwd', 'SYNO.Entry.Request'):
                    raise DirectoryServerError(error_code=error_code)
                # Docker Error:
                elif api_name.find('Docker') > -1:
                    raise DockerError(error_code=error_code)
                # Synology drive admin error:
                elif api_name.find('SynologyDrive') > -1 or api_name == 'SYNO.C2FS.Share':
                    raise DriveAdminError(error_code=error_code)
                # Log center error:
                elif api_name.find('LogCenter') > -1:
                    raise LogCenterError(error_code=error_code)
                # Note station error:
                elif api_name.find('NoteStation') > -1:
                    raise NoteStationError(error_code=error_code)
                # OAUTH error:
                elif api_name.find('SYNO.OAUTH') > -1:
                    raise OAUTHError(error_code=error_code)
                # Photo station error:
                elif api_name.find('SYNO.Foto') > -1:
                    raise PhotosError(error_code=error_code)
                # Security advisor error:
                elif api_name.find('SecurityAdvisor') > -1:
                    raise SecurityAdvisorError(error_code=error_code)
                # Task Scheduler error:
                elif api_name.find('SYNO.Core.TaskScheduler') > -1:
                    raise TaskSchedulerError(error_code=error_code)
                # Event Scheduler error:
                elif api_name.find('SYNO.Core.EventScheduler') > -1:
                    raise EventSchedulerError(error_code=error_code)
                # Universal search error:
                elif api_name.find('SYNO.Finder') > -1:
                    raise UniversalSearchError(error_code=error_code)
                # USB Copy error:
                elif api_name.find('SYNO.USBCopy') > -1:
                    raise USBCopyError(error_code=error_code)
                # VPN Server error:
                elif api_name.find('VPNServer') > -1:
                    raise VPNError(error_code=error_code)
                # Core:
                elif api_name.find('SYNO.Core') > -1:
                    raise CoreError(error_code=error_code)
                # Core Sys Info:
                elif api_name.find('SYNO.Storage') > -1:
                    raise CoreSysInfoError(error_code=error_code)
                elif api_name.find('SYNO.ResourceMonitor') > -1:
                    raise CoreSysInfoError(error_code=error_code)
                elif (api_name in ('SYNO.Backup.Service.NetworkBackup', 'SYNO.Finder.FileIndexing.Status',
                                   'SYNO.S2S.Server.Pair')):
                    raise CoreSysInfoError(error_code=error_code)
                # Unhandled API:
                else:
                    raise UndefinedError(
                        error_code=error_code, api_name=api_name)

        if response_json is True:
            return response.json()
        else:
            return response

    @staticmethod
    def _get_error_code(response: dict[str, object]) -> int:
        """
        Extract the error code from an API response.

        Parameters
        ----------
        response : dict
            The API response.

        Returns
        -------
        int
            Error code, or 0 if successful.
        """
        if response.get('success'):
            code = CODE_SUCCESS
        else:
            code = response.get('error').get('code')
        return code

    @staticmethod
    def _get_error_message(code: int, api_name: str) -> str:
        """
        Get a human-readable error message for a given error code and API.

        Parameters
        ----------
        code : int
            Error code.
        api_name : str
            Name of the API.

        Returns
        -------
        str
            Error message.
        """
        if code in error_codes.keys():
            message = error_codes[code]
        elif api_name == 'Auth':
            message = auth_error_codes.get(code, "<Undefined.Auth.Error>")
        elif api_name.find('DownloadStation') > -1:
            message = download_station_error_codes.get(
                code, "<Undefined.DownloadStation.Error>")
        elif api_name.find('Virtualization') > -1:
            message = virtualization_error_codes.get(
                code, "<Undefined.Virtualization.Error>")
        elif api_name.find('FileStation') > -1:
            message = file_station_error_codes.get(
                code, "<Undefined.FileStation.Error>")
        else:
            message = "<Undefined.%s.Error>" % api_name
        return 'Error {} - {}'.format(code, message)

    @staticmethod
    def decode_ssid_cookie(ssid: str) -> bytes:
        """
        Decode the SSID cookie.

            Parameters
            ----------
            ssid : str
                The SSID cookie string to decode.

            Returns
            -------
            bytes
                The decoded SSID cookie.
        """
        # Replace '-' with '+' and '_' with '/'
        ssid_fixed = ssid.replace('-', '+').replace('_', '/')
        # Pad with '=' if needed
        padding = '=' * (-len(ssid_fixed) % 4)
        ssid_fixed += padding
        # Decode base64
        return base64.b64decode(ssid_fixed)

    @staticmethod
    def encode_ssid_cookie(ssid_bytes: bytes) -> str:
        """
        Encode the SSID cookie.

            Parameters
            ----------
            ssid_bytes : bytes
                The SSID cookie bytes to encode.

            Returns
            -------
            str
                The encoded SSID cookie.
        """
        # Encode to base64
        ssid_b64 = base64.b64encode(ssid_bytes).decode('utf-8')
        # Replace '+' with '-' and '/' with '_'
        ssid_fixed = ssid_b64.replace('+', '-').replace('/', '_')
        # Remove padding '='
        ssid_fixed = ssid_fixed.rstrip('=')
        return ssid_fixed

    @property
    def sid(self) -> Optional[str]:
        """
        Get the current session ID.

        Returns
        -------
        str or None
            Session ID if logged in, else None.
        """
        return self._sid

    @property
    def base_url(self) -> str:
        """
        Get the base URL for API requests.

        Returns
        -------
        str
            Base URL.
        """
        return self._base_url

    @property
    def syno_token(self) -> str:
        """
        Get the Synology token for API requests.

        Returns
        -------
        str
            Synology token.
        """
        return self._syno_token


class AESCipher(object):
    """
    Encrypt with OpenSSL-compatible way.

    Parameters
    ----------
    password : bytes
        The password to derive the key from.
    key_length : int, optional
        Length of the key (default is 32).
    """

    SALT_MAGIC = b'Salted__'

    def __init__(self, password, key_length=32):
        """
        Initialize the AESCipher object.

        Parameters
        ----------
        password : bytes
            The password to derive the key from.
        key_length : int, optional
            Length of the key (default is 32).
        """
        self._bs = 16
        self._salt = urandom(self._bs - len(self.SALT_MAGIC))

        self._key, self._iv = self._derive_key_and_iv(password,
                                                      self._salt,
                                                      key_length,
                                                      self._bs)

    def _pad(self, s):
        """
        Pad the input string to a multiple of the block size.

        Parameters
        ----------
        s : str
            String to pad.

        Returns
        -------
        bytes
            Padded string as bytes.
        """
        bs = self._bs
        return (s + (bs - len(s) % bs) * chr(bs - len(s) % bs)).encode('utf-8')

    def _derive_key_and_iv(self, password, salt, key_length, iv_length):
        """
        Derive the key and IV from the password and salt.

        Parameters
        ----------
        password : bytes
            Password.
        salt : bytes
            Salt.
        key_length : int
            Length of the key.
        iv_length : int
            Length of the IV.

        Returns
        -------
        tuple
            (key, iv).
        """
        d = d_i = b''
        while len(d) < key_length + iv_length:
            md5_str = d_i + password + salt
            d_i = hashlib.md5(md5_str).digest()
            d += d_i
        return d[:key_length], d[key_length:key_length + iv_length]

    def encrypt(self, text):
        """
        Encrypt the given text using AES CBC mode.

        Parameters
        ----------
        text : str
            Text to encrypt.

        Returns
        -------
        bytes
            Encrypted ciphertext with OpenSSL salt header.
        """
        cipher = Cipher(
            algorithms.AES(self._key),
            modes.CBC(self._iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(self._pad(text)) + encryptor.finalize()

        return self.SALT_MAGIC + self._salt + ciphertext
