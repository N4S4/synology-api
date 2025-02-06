import json
from typing import Any, List
from . import base_api

class KeyManagerAutoKey(base_api.BaseApi):
    """
    Core Share KeyManager AutoKey API implementation.
    """
    
    def list(self) -> dict:
        """
        Explore KeyManagerStore API.
        
        Returns:
            dict: API response.
            ```json
            {
                "data": {
                    "keys": []
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share.KeyManager.AutoKey"
        version = self.core_list[api_name]["minVersion"]
        api_path = self.core_list[api_name]["path"]
        req_param = {
            "version": version,
            "method": "list",
        }
        
        return self.request_data(api_name, api_path, req_param)