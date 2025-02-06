import json
from typing import Any, List
from . import base_api

class KeyManagerStore(base_api.BaseApi):
    """
    Core Share KeyManager Store API implementation.
    """
    
    def init(self) -> dict:
        """
        Initialize KeyManagerStore API.
        
        Returns:
            dict: API response.
            ```json
            {
                "success": true
            }
            ```
        """
        
        raise NotImplementedError("This method is not completly implemented yet. API return error 403")
        
        api_name = "SYNO.Core.Share.KeyManager.Store"
        version = self.core_list[api_name]["maxVersion"]
        api_path = self.core_list[api_name]["path"]
        req_param = {
            "version": version,
            "method": "init",
            "share_path": "/usr/syno/etc/.encrypt"
        }
        
        req_param_encrypted = {
            "passphrase": "",
        }
        
        # If using https don't use encryption
        if self.session._secure:
            req_param.update(req_param_encrypted)
        else:
            encrypted_params = self.session.encrypt_params(req_param_encrypted)
            req_param.update(encrypted_params)
        
        
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def verify(self) -> dict:
        
        raise NotImplementedError("This method is not implemented yet.")
    
        api_name = "SYNO.Core.Share.KeyManager.Store"
        version = self.core_list[api_name]["maxVersion"]
        api_path = self.core_list[api_name]["path"]
        req_param = {
            "version": version,
            "method": "verify",
        }
        
        req_param_encrypted = {
            "passphrase": "",
        }
        
        # If using https don't use encryption
        if self.session._secure:
            req_param.update(req_param_encrypted)
        else:
            encrypted_params = self.session.encrypt_params(req_param_encrypted)
            req_param.update(encrypted_params)
        
        
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def explore(self) -> dict:
        """
        Explore KeyManagerStore API.
        
        Returns:
            dict: API response.
            ```json
            {
                "data": {
                    "stores": []
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share.KeyManager.Store"
        version = self.core_list[api_name]["minVersion"]
        api_path = self.core_list[api_name]["path"]
        req_param = {
            "version": version,
            "method": "explore",
        }
        
        return self.request_data(api_name, api_path, req_param)