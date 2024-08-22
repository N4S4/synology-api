from __future__ import annotations
from . import base_api


class CloudSync(base_api.BaseApi):
    '''
       Cloud Sync API implementation.
    '''

    def get_config(self) -> dict[str, object] | str:
        '''
        Get package settings.
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_config'
        }

        return self.request_data(api_name, api_path, req_param)
    

