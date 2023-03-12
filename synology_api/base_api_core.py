from typing import Optional
from . import auth as syn


class Core(object):
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

        self.session : syn.Authentication = syn.Authentication(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        self.session.login('Core')
        self.session.get_api_list('Core')
        self.session.get_api_list()

        self.request_data : function = self.session.request_data
        self.core_list : dict[str, object] = self.session.app_api_list
        self.gen_list : dict[str, object] = self.session.full_api_list
        self._sid : str = self.session.sid
        self.base_url : str = self.session.base_url

    def logout(self) -> None:
        self.session.logout('Core')
        return
