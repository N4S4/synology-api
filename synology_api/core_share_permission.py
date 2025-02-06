import json
from typing import Any, List
from . import base_api

class SharePermission(base_api.BaseApi):
    """
    Core Share Permission API implementation.
    """
    
    def get_folder_permission_by_name(self, 
                name: str, permission_substr: str, offset: int = 0, limit: int = 50, is_unite_permission: bool = False, with_inherit: bool = False,
                user_group_type: str = "local_user"
        ) -> dict[str, object] | str:
        """
        Retrieve share permissions for a given folder filtered by permission name (sub string)
        
        Args:
            name (str):
                The folder name to list permissions for.
            offset (int, optional):
                The offset to start at. Defaults to `0`.
            limit (int, optional):
                The maximum number of results to return. Defaults to `50`.
            is_unite_permission (bool, optional):
                Whether to return unified permissions. Defaults to `False`.
            with_inherit (bool, optional):
                Whether to include inherited permissions. Defaults to `False`.
            user_group_type (str, optional):
                The type of user group to list permissions for. Defaults to `"local_user"`.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
            permission_substr (str, optional):
                The substring to search for in the permissions. Defaults to `""`.
        
        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.
            
            Example return:
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
        ) -> dict[str, object] | str:
        """
        Retrieve share permissions for a given folder.

        Args:
            name (str):
                The folder name to list permissions for.
            offset (int, optional):
                The offset to start at. Defaults to `0`.
            limit (int, optional):
                The maximum number of results to return. Defaults to `50`.
            is_unite_permission (bool, optional):
                Whether to return unified permissions. Defaults to `False`.
            with_inherit (bool, optional):
                Whether to include inherited permissions. Defaults to `False`.
            user_group_type (str, optional):
                The type of user group to list permissions for. Defaults to `"local_user"`.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.

        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.

            Example return:
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
        """
        Set folder permissions for a given folder.
        Args:
            name (str):
                The folder name to set permissions for.
            user_group_type (str):
                The type of user group to set permissions for.
                All known values are: `["system", "local_user", "local_group", "ldap_user", "ldap_group"]`.
            permissions (dict):
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
        Returns:
            dict: A dictionary containing the result of the request.
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
    
    def get_local_group_permissions(self, group: str) -> dict[str, object] | str:
        """
        Retrieve share permissions for a given group.

        Args:
            group (str):
                The group to list permissions for.

        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.

            Example return:
            ```
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
    ) -> dict[str, object] | str:
        """
        Set group permissions for a given share.

        Args:
            group (str):
                The group to set the permissions for.
            permissions (list[dict[str, Any]]):
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

        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.

            Example return:
            ```
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
    