import json
from typing import List
from . import base_api

class Share(base_api.BaseApi):
    """
    Core Share API implementation.
    """
    
    def list_folders(self, share_type: str = "all", additional: list = []) -> dict:
        """
        Args:
            share_type (str, optional):
                Share type. Defaults to `all`.
            additional (list[str], optional):
                Additional fields to retrieve. Defaults to `[]`.
                All fields known are: `[
                    "hidden","encryption","is_aclmode","unite_permission","is_support_acl","is_sync_share","is_force_readonly","force_readonly_reason",
                    "recyclebin","is_share_moving","is_cluster_share","is_exfat_share","is_c2_share","is_cold_storage_share","is_missing_share",
                    "is_offline_share","support_snapshot","share_quota","enable_share_compress","enable_share_cow","enable_share_tiering",
                    "load_worm_attr","include_cold_storage_share","is_cold_storage_share","include_missing_share","is_missing_share",
                    "include_offline_share","is_offline_share","include_worm_share"
                ]`.


        Returns:
            dict|str:
                A dictionary containing the shared folders information.

            Example return:
            ```
            {
                "data": {
                    "shares": [
                    {
                        "desc": "",
                        "is_usb_share": false,
                        "name": "test_shared_folder",
                        "uuid": "18585c8d-4d74-41a1-b561-21906a7f6f14",
                        "vol_path": "/volume1"
                    }
                    ],
                    "total": 1
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": info['minVersion'],
            "shareType": share_type,
            "additional": json.dumps(additional)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    
    def get_folder(self, name: str, additional: list = []) -> dict:
        """
        Args:
            name (str):
                Share name.
            additional (list[str], optional):
                Additional fields to retrieve. Defaults to `[]`.
                All fields known are: `["disable_list","disable_modify","disable_download","unite_permission","is_aclmode"]`.
        Returns:
            dict|str:
                A dictionary containing the shared folder information.

            Example return:
            ```
            {
                "data": {
                    "desc": "",
                    "disable_download": false,
                    "disable_list": false,
                    "disable_modify": false,
                    "is_aclmode": true,
                    "is_usb_share": false,
                    "name": "test_shared_folder",
                    "unite_permission": false,
                    "uuid": "18585c8d-4d74-41a1-b561-21906a7f6f14",
                    "vol_path": "/volume1"
                },
                "success": true,
            ```
        """
        api_name = "SYNO.Core.Share"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": info['minVersion'],
            "name": name,
            "additional": json.dumps(additional)
        }
        
        return self.request_data(api_name, api_path, req_param)
    

    def create_folder(self,
                name: str, vol_path: str, desc: str = "", hidden: bool = False,
                enable_recycle_bin: bool = True, recycle_bin_admin_only: bool = True,
                hide_unreadable: bool = False, enable_share_cow: bool = False,
                enable_share_compress: bool = False, share_quota: int = 0, name_org: str = "",
        ) -> dict:
        
        """
        Args:
            name (str):
                Share name.
            vol_path (str):
                Volume path.
            desc (str, optional):
                Share description. Defaults to `""`.
            hidden (bool, optional):
                Hide share. Defaults to `False`.
            enable_recycle_bin (bool, optional):
                Enable recycle bin. Defaults to `True`.
            recycle_bin_admin_only (bool, optional):
                Recycle bin admin only. Defaults to `True`.
            hide_unreadable (bool, optional):
                Hide unreadable. Defaults to `False`.
            enable_share_cow (bool, optional):
                Enable share cow. Defaults to `False`.
            enable_share_compress (bool, optional): 
                Enable share compress. Defaults to `False`.
            share_quota (int, optional):    
                Share quota. Defaults to `0`.
            name_org (str, optional):   
                Defaults to `""`.
                
        Returns:
            dict|str:
                A dictionary containing the groups information.

            Example return:
            ```
            {
                "data": {
                    "name": "test_shared_folder"
                },
                "success": true,
            ```
        """
        
        api_name = "SYNO.Core.Share"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": info['maxVersion'],
            "name": name,
        }
        req_param_encrypted = {
            "shareinfo": json.dumps({
                "desc": desc,
                "enable_recycle_bin": enable_recycle_bin,
                "enable_share_compress": enable_share_compress,
                "enable_share_cow": enable_share_cow,
                "name": name,
                "name_org": name_org,
                "vol_path": vol_path,
                "recycle_bin_admin_only": recycle_bin_admin_only,
                "hidden": hidden,
                "hide_unreadable": hide_unreadable,
                "share_quota": share_quota,
            })
        }
        # If using https don't use encryption
        if self.session._secure:
            req_param.update(req_param_encrypted)
        else:
            encrypted_params = self.session.encrypt_params(req_param_encrypted)
            req_param.update(encrypted_params)
        
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def delete_folders(self, name: List[str]):
        """
        Args:
            name (list[str]):
                Share names.
        Returns:
            dict|str:
                Success.

            Example return:
            ```
            {
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": info['minVersion'],
            "name": name
        }
        
        return self.request_data(api_name, api_path, req_param)