import sys
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

from dataclass_factory import Factory
from requests import get, Response
from typing_extensions import Protocol

from .parameters.webservice import LOGIN_PARAMS

ENTRY_URL = '{url}/webapi/entry.cgi'

# parameter sets

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
class SynoRequest:

    pass

@dataclass
class SynoResponse:

    response: Response = field( default=None )
    status_code: int = field(default=None)
    data: Dict = field( default_factory=dict )
    success: bool = field( default=False )
    error_code: int = field( default=None )
    error_msg: str = field( default=None )

    def __post_init__( self ):
        self.status_code = self.response.status_code
        json = self.response.json()
        self.success = json.get( 'success', False )
        if self.success:
            self.data = json.get( 'data', {} )
        else:
            self.error_code = json.get( 'error' ).get( 'code' )
            self.error_msg = '...' # todo

    def response_data( self, key: str ) -> Any:
        return self.data.get( key, None )

@dataclass
class SynoWebService:

    url: str = field(default=None)
    account: str = field( default=None )
    password: str = field( default=None )
    session_id: str = field( default=None )
    device_id: str = field( default=None )

    def __post_init__(self):
        self._factory = Factory()

    def get( self, url: str, template: Dict, **kwargs ) -> SynoResponse:
        if self.session_id:
            template = { **template, '_sid': self.session_id }

        response = get(
            url=self.get_url( url ),
            params={ **template, **kwargs },
            verify=True
        )

        return SynoResponse( response=response )

    def get_list_to_dataclass( self, url, params, cls ):
        syno_response = self.get( url, params )
        if not syno_response.success:
            print( f'error doing get request: code={syno_response.error_code}' )
            sys.exit( -1 )
        element_list = syno_response.data.get( 'list' )
        return [ self._factory.load( e, cls ) for e in element_list ]

    def get_url( self, stub: str ) -> str:
        return stub.format( url=self.url )

    def login( self ) -> SynoResponse:
        syno_response = self.get(ENTRY_URL, LOGIN_PARAMS, account=self.account, passwd=self.password)
        if syno_response.success:
            self.session_id = syno_response.response_data( 'sid' )
            self.device_id = syno_response.response_data( 'device_id' )

        return syno_response
