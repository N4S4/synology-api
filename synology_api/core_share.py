import json
from typing import List, Any
from . import base_api

class Share(base_api.BaseApi):
    """
    Core Share API implementation.
    """
    
    def validate_set(self, name: str, vol_path: str, desc: str = "", enable_share_compress: bool = False, enable_share_cow: bool = False, enc_passwd: str = "", encryption: bool = False) -> dict:
        """Validate set of parameter for a new / modified shared folder
            Parameters
            ----------
            name : str
                Share name.
                
            vol_path : str
                Volume path.
                
            desc : str, optional
                Share description. Defaults to `""`.
                
            enable_share_compress : bool, optional
                Enable share compress. Defaults to `False`.
                
            enable_share_cow : bool, optional
                Enable share cow. Defaults to `False`.
                
            enc_passwd : str, optional
                Encrypted password. Defaults to `""`.
                
            encryption : bool, optional
                Enable encryption. Defaults to `False`.
                    
            Returns
            -------
            dict
                Success.

            Example return
            --------------
            ```json
            {
                "success": true,
            }
            ```
        """
        api_name = "SYNO.Core.Share"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "validate_set",
            "version": info['maxVersion'],
            "name": name,
        }
        
        req_param_encrypted = {
            "shareinfo": json.dumps({
                "name": name,
                "vol_path": vol_path,
                "desc": desc,
                "enable_share_compress": enable_share_compress,
                "enable_share_cow": enable_share_cow,
                "enc_passwd": enc_passwd,
                "encryption": encryption,
            })
        }
        
        # If using https don't use encryption
        if self.session._secure:
            req_param.update(req_param_encrypted)
        else:
            encrypted_params = self.session.encrypt_params(req_param_encrypted)
            req_param.update(encrypted_params)
        
        
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def list_folders(self, share_type: str = "all", additional: list = []) -> dict:
        """List all folders informations
            Parameters
            ----------
            share_type : str, optional
                Share type. Defaults to `all`.
                
            additional : list[str], optional
                Additional fields to retrieve. Defaults to `[]`.
                All fields known are: `[
                    "hidden","encryption","is_aclmode","unite_permission","is_support_acl","is_sync_share","is_force_readonly","force_readonly_reason",
                    "recyclebin","is_share_moving","is_cluster_share","is_exfat_share","is_c2_share","is_cold_storage_share","is_missing_share",
                    "is_offline_share","support_snapshot","share_quota","enable_share_compress","enable_share_cow","enable_share_tiering",
                    "load_worm_attr","include_cold_storage_share","is_cold_storage_share","include_missing_share","is_missing_share",
                    "include_offline_share","is_offline_share","include_worm_share"
                ]`.
                    
            Returns
            -------
            dict
                A dictionary containing the shared folders information.

            Example return
            --------------
            ```json
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
        """Get a folder by name
            Parameters
            ----------
            name : str
                Share name.
                
            additional : list, optional
                Additional fields to retrieve. Defaults to `[]`.
                All fields known are: `["disable_list","disable_modify","disable_download","unite_permission","is_aclmode"]`.
                    
            Returns
            -------
            dict
                A dictionary containing the shared folder information.

            Example return
            --------------
            ```json
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
        """Create a new shared folder
            Parameters
            ----------
            name : str
                Share name.
                
            vol_path : str
                Volume path.
                
            desc : str, optional
                Share description. Defaults to `""`.
                
            hidden : bool, optional
                Hide share. Defaults to `False`.
                
            enable_recycle_bin : bool, optional
                Enable recycle bin. Defaults to `True`.
                
            recycle_bin_admin_only : bool, optional
                Recycle bin admin only. Defaults to `True`.
                
            hide_unreadable : bool, optional
                Hide unreadable. Defaults to `False`.
                
            enable_share_cow : bool, optional
                Enable share cow. Defaults to `False`.
                
            enable_share_compress : bool, optional
                Enable share compress. Defaults to `False`.
                
            share_quota : int, optional 
                Share quota. Defaults to `0`.
                
            name_org : str, optional 
                Defaults to `""`.
                    
            Returns
            -------
            dict
                Name of the created shared folder

            Example return
            ---------------
            ```json
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
    
    def delete_folders(self, name: List[str]) -> dict:
        """Delete folder(s) by name(s)
        
            Parameters
            ----------
            name : List[str]
                Share names.
                    
            Returns
            -------
            dict
                Success.

            Example return
            --------------
            ```json
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
    
    def clone(self,
                name: str, name_org: str, vol_path: str, desc: str = "", hidden: bool = False,
                enable_recycle_bin: bool = True, recycle_bin_admin_only: bool = True,
                hide_unreadable: bool = False, enable_share_cow: bool = False,
                enable_share_compress: bool = False, share_quota: int = 0
        ) -> dict:
        """Clone existing shared folder.
            Parameters
            ----------
            name : str
                New shared folder name.
                
            name_org : str
                Original shared folder name.
                
            vol_path : str
                Volume path.
                
            desc : str, optional
                Shared folder description. Defaults to `""`.
                
            hidden : bool, optional
                Hide shared folder. Defaults to `False`.
                
            enable_recycle_bin : bool, optional
                Enable recycle bin. Defaults to `True`.
                
            recycle_bin_admin_only : bool, optional
                Recycle bin admin only. Defaults to `True`.
                
            hide_unreadable : bool, optional
                Hide unreadable. Defaults to `False`.
                
            enable_share_cow : bool, optional
                Enable share cow. Defaults to `False`.
                
            enable_share_compress : bool, optional
                Enable share compress. Defaults to `False`.
                
            share_quota : int, optional
                Share quota. Defaults to `0`.
                    
            Returns
            -------
            dict
                Name of the created shared folder
                
            Example return
            --------------
            ```json
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
            "method": "clone",
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
    
class SharePermission(base_api.BaseApi):
    """
    Core Share Permission API implementation.
    """
    
    def get_folder_permission_by_name(self, 
                name: str, permission_substr: str, offset: int = 0, limit: int = 50, is_unite_permission: bool = False, with_inherit: bool = False,
                user_group_type: str = "local_user"
        ) -> dict:
        """Retrieve share permissions for a given folder filtered by permission name (sub string)
            Parameters
            ----------
            name : str
                The folder name to list permissions for.
                
            permission_substr : str
                The substring to search for in the permissions.
                
            offset : int, optional
                The offset to start at. Defaults to `0`.
                
            limit : int, optional
                The maximum number of results to return. Defaults to `50`.
                
            is_unite_permission : bool, optional
                Whether to return unified permissions. Defaults to `False`.
                
            with_inherit : bool, optional
                Whether to include inherited permissions. Defaults to `False`.
                
            user_group_type : str, optional
                The type of user group to list permissions for. Defaults to `"local_user"`.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
            
            Returns
            -------
            dict 
                List of permission(s) on the folder
                
            Example return
            --------------
            ```json
            {
                "data": {
                    "items": [
                        {
                            "inherit": "-",
                            "is_admin": false,
                            "is_custom": false,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "guest"
                        }
                    ],
                    "total": 1
                },
                "success": true
            }
            ```
        """
        
        api_name = "SYNO.Core.Share.Permission"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "list",
            "name": name,
            "offset": offset,
            "limit": limit,
            "action": "find",
            "substr": permission_substr,
            "is_unite_permission": is_unite_permission,
            "with_inherit": with_inherit,
            "user_group_type": user_group_type,
        }
        return self.request_data(api_name, api_path, req_param, method="get")
    
    def get_folder_permissions(self, 
                name: str, offset: int = 0, limit: int = 50, is_unite_permission: bool = False, with_inherit: bool = False,
                user_group_type: str = "local_user"
        ) -> dict:
        """Retrieve share permissions for a given folder.
            Parameters
            ----------
            name : str
                The folder name to list permissions for.
                
            offset : int, optional
                The offset to start at. Defaults to `0`.
                
            limit : int, optional
                The maximum number of results to return. Defaults to `50`.
                
            is_unite_permission : bool, optional
                Whether to return unified permissions. Defaults to `False`.
                
            with_inherit : bool, optional
                Whether to include inherited permissions. Defaults to `False`.
                
            user_group_type : str, optional
                The type of user group to list permissions for. Defaults to `"local_user"`.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.

            Returns
            -------
            dict
                All permissions on the folder

            Example return
            ----------
            ```json
            {
                "data": {
                    "items": [
                        {
                            "inherit": "rw",
                            "is_admin": true,
                            "is_custom": false,
                            "is_deny": true,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "admin"
                        },
                        {
                            "inherit": "-",
                            "is_admin": false,
                            "is_custom": false,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "guest"
                        },
                        {
                            "inherit": "rw",
                            "is_admin": true,
                            "is_custom": false,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": true,
                            "name": "test_api"
                        },
                        {
                            "inherit": "-",
                            "is_admin": false,
                            "is_custom": false,
                            "is_deny": false,
                            "is_readonly": false,
                            "is_writable": false,
                            "name": "test_test"
                        }
                    ],
                    "total": 5
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share.Permission"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "list",
            "name": name,
            "offset": offset,
            "limit": limit,
            "action": "enum",
            "is_unite_permission": is_unite_permission,
            "with_inherit": with_inherit,
            "user_group_type": user_group_type,
        }
        return self.request_data(api_name, api_path, req_param, method="get")
    
    def set_folder_permissions(self, name: str, user_group_type: str, permissions: List[dict[str, object]]) -> dict:
        """Set folder permissions for a given folder.
            Parameters
            ----------
            name : str
                The folder name to set permissions for.
                
            user_group_type : str
                The type of user group to set permissions for.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
                
            permissions : dict
                The permissions to set for the folder.
                Example:
                ```json
                [
                    {
                        "name":"guest",
                        "is_readonly":false,
                        "is_writable":true,
                        "is_deny":false,
                        "is_custom":false
                    }
                ]
                ```
                    
            Returns
            -------
            dict 
                Success
                    
            Example return
            --------------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share.Permission"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "set",
            "name": name,
            "user_group_type": user_group_type,
            "permissions": json.dumps(permissions),
        }
        return self.request_data(api_name, api_path, req_param, method="get")
    
    def get_local_group_permissions(self, group: str) -> dict:
        """Retrieve share permissions for a given group.
            Parameters
            ----------
            group : str
                The group to list permissions for.

            Returns
            -------
            dict
                Permissions of a group on Shared folders

            Example return
            --------------
            ```json
            {
                "data": {
                    "shares": [
                        {
                            "is_aclmode": true,
                            "is_custom": false,
                            "is_deny": true,
                            "is_mask": false,
                            "is_readonly": false,
                            "is_sync_share": false,
                            "is_unite_permission": false,
                            "is_writable": false,
                            "name": "ActiveBackupforBusiness",
                            "share_path": "/volume3/ActiveBackupforBusiness"
                        }
                    ],
                    "total": 1
                },
                "success": true
            }     
            ```
        """
        api_name = "SYNO.Core.Share.Permission"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": 1,
            "method": "list_by_group",
            "name": group,
            "user_group_type": "local_group",
            "share_type": json.dumps(
                ["dec", "local", "usb", "sata", "cluster", "c2", "cold_storage", "worm"]
            ),
            "additional": json.dumps(["hidden", "encryption", "is_aclmode"]),
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_local_group_permissions(
        self, group: str, permissions: list[dict[str, Any]]
    ) -> dict:
        """Set group permissions for a given share.
            Parameters
            ----------
            group : str
                The group to set the permissions for.
                
            permissions : list[dict[str, Any]]
                The permissions to set for the group.
                Example:
                ```
                [
                    {
                        "name": "web",
                        "is_readonly": False,
                        "is_writable": False,
                        "is_deny": True
                    },
                    {
                        "name": "ActiveBackupforBusiness",
                        "is_readonly": False,
                        "is_writable": True,
                        "is_deny": False
                    }
                ]
                ```

            Returns
            -------
            dict
                Success

            Example return
            --------------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.Share.Permission"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "set_by_user_group",
            "name": group,
            "user_group_type": "local_group",
            "permissions": json.dumps(permissions),
        }

        return self.request_data(api_name, api_path, req_param)
    
class KeyManagerStore(base_api.BaseApi):
    """
    Core Share KeyManager Store API implementation.
    """
    
    def init(self) -> dict:
        """Initialize KeyManagerStore API.
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
        """Explore KeyManagerStore API. Get list of existing stores
            Returns
            -------
            dict
                List of stores existing on the NAS
                    
            Example return
            --------------
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
    
class KeyManagerAutoKey(base_api.BaseApi):
    """
    Core Share KeyManager AutoKey API implementation.
    """
    
    def list(self) -> dict:
        """List KeyManagerStore API.
            Returns
            -------
            dict
                List of keys in the manager
                    
            Example return
            --------------
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

