
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from typing_extensions import Protocol

class WebService( Protocol ):

    @property
    def base_url( self ) -> Optional[str]:
        return None

    @base_url.setter
    def base_url( self, base_url: str ) -> None:
        pass

    @abstractmethod
    def url( self, url_stub: str ) -> str:
        pass

@dataclass
class SynoWebService:

    base_url: str = field( default=None )

    def url( self, url_stub: str ) -> str:
        return url_stub.format( base_url=self.base_url )
