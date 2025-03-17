from typing import Optional, Any
from . import auth as syn


class BaseApi(object):
    """Base class to be used for all API implementations.

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

        secure : bool  
            Whether to use HTTPS or not. Defaults to `False`.

        cert_verify : bool  
            Whether to verify the SSL certificate or not. Defaults to `False`.

        dsm_version : int  
            The DSM version. Defaults to `7`.

        debug : bool  
            Whether to print debug messages or not. Defaults to `True`.

        otp_code : str  
            The OTP code to use for authentication. Defaults to `None`
    """
    
    # Class-level attribute to store the shared session
    shared_session: Optional[syn.Authentication] = None
    
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
            device_name: Optional[str] = None,
            application: str = 'Core',
        ) -> None:

        self.application = application
        
        # Reuse shared session if it exists, otherwise create a new one
        if BaseApi.shared_session:
            self.session = BaseApi.shared_session
        else:
            if not all([ip_address, port, username, password]):
                raise ValueError("Missing required credentials for initial authentication.")

            self.session = syn.Authentication(
                ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code,
                device_id, device_name
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
        """Close current session."""
        if self.session:
            self.session.logout()
            if BaseApi.shared_session == self.session:
                BaseApi.shared_session = None
        return
