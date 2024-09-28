from typing import Optional, Any
from . import auth as syn


class BaseApi(object):
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
                 application: str = 'Core',
                 ) -> None:

        self.application = application
        self.session: syn.Authentication = syn.Authentication(ip_address, port, username, password, secure, cert_verify,
                                                              dsm_version, debug, otp_code)
        self.session.login(self.application)
        self.session.get_api_list(self.application)
        self.session.get_api_list()

        self.request_data: Any = self.session.request_data
        self.request_multi_data = self.session.request_multi_datas
        self.core_list: Any = self.session.app_api_list
        self.gen_list: Any = self.session.full_api_list
        self._sid: str = self.session.sid
        self.base_url: str = self.session.base_url

    def logout(self) -> None:
        self.session.logout(self.application)
        return
