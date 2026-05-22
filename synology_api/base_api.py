"""
Base API module for Synology DSM.

Provides a base class for all API implementations, handling authentication,
session management, and connection setup to a Synology NAS device.
"""
from typing import Optional, Any
from . import auth as syn


class BaseApi(object):
    """
    Base class to be used for all API implementations.

    Takes auth and connection information to create a session to the NAS.
    The session is created on instanciation.

    Parameters
    ----------
    ip_address : str
        The IP/DNS address of the NAS.
    port : str
        The port of the NAS. Defaults to `5000`.
    username : str
        The username to use for authentication.
    password : str
        The password to use for authentication.
    secure : bool, optional
        Whether to use HTTPS or not. Defaults to `False`.
    cert_verify : bool, optional
        Whether to verify the SSL certificate or not. Defaults to `False`.
    dsm_version : int, optional
        The DSM version. Defaults to `7`.
    debug : bool, optional
        Whether to print debug messages or not. Defaults to `True`.
    otp_code : str, optional
        The OTP code to use for authentication. Defaults to `None`.
    device_id : str, optional
        Device ID for device binding. Defaults to `None`.
    device_name : str, optional
        Device name for device binding. Defaults to `None`.
    application : str, optional
        The application context for API list retrieval. Defaults to `'Core'`.
    quickconnect_id : str, optional
        QuickConnect ID for relay-based access. Defaults to `None`.
    """

    # Class-level attribute to store the shared session
    shared_session: Optional[syn.Authentication] = None

    def __init__(self,
                 ip_address: Optional[str] = None,
                 port: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 device_id: Optional[str] = None,
                 device_name: Optional[str] = None,
                 application: str = 'Core',
                 quickconnect_id: Optional[str] = None,
                 ) -> None:
        """
        Initialize the BaseApi object and create or reuse a session.

        Parameters
        ----------
        ip_address : str
            The IP/DNS address of the NAS.
        port : str
            The port of the NAS.
        username : str
            The username to use for authentication.
        password : str
            The password to use for authentication.
        secure : bool, optional
            Whether to use HTTPS or not. Defaults to `False`.
        cert_verify : bool, optional
            Whether to verify the SSL certificate or not. Defaults to `False`.
        dsm_version : int, optional
            The DSM version. Defaults to `7`.
        debug : bool, optional
            Whether to print debug messages or not. Defaults to `True`.
        otp_code : str, optional
            The OTP code to use for authentication. Defaults to `None`.
        device_id : str, optional
            Device ID for device binding. Defaults to `None`.
        device_name : str, optional
            Device name for device binding. Defaults to `None`.
        application : str, optional
            The application context for API list retrieval. Defaults to `'Core'`.
        quickconnect_id : str, optional
            QuickConnect ID for relay-based access. When provided, `ip_address`
            and `port` are not required.

        Returns
        -------
        None
            Just actions, no return values.
        """
        self.application = application

        # Reuse shared session if it exists, otherwise create a new one
        if BaseApi.shared_session:
            self.session = BaseApi.shared_session
        else:
            if quickconnect_id:
                missing_credentials = not all([username, password])
            else:
                missing_credentials = not all(
                    [ip_address, port, username, password])
            if missing_credentials:
                raise ValueError(
                    "Missing required credentials for initial authentication.")

            self.session = syn.Authentication(
                ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code,
                device_id, device_name, quickconnect_id
            )
            self.session.login()
            self.session.get_api_list(self.application)
            self.session.get_api_list()

            # Store the new session in the shared class-level attribute
            BaseApi.shared_session = self.session

        # Initialize other attributes from the session
        self.request_data: Any = self.session.request_data
        self.batch_request = self.session.request_multi_datas
        self.core_list: Any = self.session.app_api_list
        self.gen_list: Any = self.session.full_api_list
        self._sid: str = self.session.sid
        self.base_url: str = self.session.base_url

    def logout(self) -> None:
        """
        Close current session.

        Returns
        -------
        None
            Action, no return values.
        """
        if self.session:
            self.session.logout()
            if BaseApi.shared_session == self.session:
                BaseApi.shared_session = None
        return
