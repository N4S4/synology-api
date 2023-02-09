
from typing import Dict
from requests import get
from .webservice import SynoWebService

# urls

ENTRY_URL = '{url}/webapi/entry.cgi'

# parameter sets

ENTRY_PARAMS = {
    'api': 'SYNO.API.Info',
    'version': 1,
    'method': 'query',
    #    'query': 'SYNO.Foto.Browse.Folder', # querying a single endpoint is possible
}

class SynoWebApi( SynoWebService ):

    def info( self ) -> Dict:
        return get(self.get_url(ENTRY_URL), ENTRY_PARAMS, verify=True).json()
