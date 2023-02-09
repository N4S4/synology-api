
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from requests import get
from typing_extensions import Protocol

ENTRY_URL = '{url}/webapi/entry.cgi'

# parameter sets

LOGIN_PARAMS = {
    'api': 'SYNO.API.Auth',
    'version': 7,
    'method': 'login',
    'account': None,
    'passwd': None,
}

class WebService( Protocol ):

    @property
    def url( self ) -> Optional[str]:
        return None

    @url.setter
    def url( self, url: str ) -> None:
        pass

    @abstractmethod
    def get_url( self, url_stub: str ) -> str:
        pass

@dataclass
class SynoWebService:

    url: str = field(default=None)
    account: str = field( default=None )
    password: str = field( default=None )
    session_id: str = field( default=None )
    device_id: str = field( default=None )

    def get_url( self, stub: str ) -> str:
        return stub.format( url=self.url )

    def login( self ):
        response = get(
            url=self.get_url( ENTRY_URL ),
            params={ **LOGIN_PARAMS, 'account': self.account, 'passwd': self.password },
            verify=True
        )
        response_json = response.json()
        if response_json.get( 'success' ):
            self.session_id = response_json.get( 'data' ).get( 'sid' )
            self.device_id = response_json.get( 'data' ).get( 'device_id' )
        else:
            error_code = response_json.get( 'error' ).get( 'code' )
            error_msg = ''
