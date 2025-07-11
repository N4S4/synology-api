"""
Synology Core Group API wrapper.

This module provides a Python interface for managing groups on Synology NAS devices,
including group creation, deletion, membership management, quota and permission settings,
and bandwidth control.
"""

import json
from typing import Any
from . import base_api


class Group(base_api.BaseApi):
    """
    Core Group API implementation for Synology NAS.

    This class provides methods to manage groups, including:
    - Retrieving group information, members, permissions, quotas, and speed limits.
    - Modifying group name, description, share permissions, quotas, and speed limits.
    - Creating and deleting groups.
    - Adding and removing users from groups.

    Methods
    -------
    get_groups(offset=0, limit=-1, name_only=False)
        Retrieve groups information.
    get_users(group, in_group=True)
        Retrieve users who are members or not members of a group.
    get_speed_limits(group)
        Retrieve bandwidth control settings for a group.
    get_quota(group)
        Retrieve quota settings for a group.
    get_permissions(group)
        Retrieve share permissions for a group.
    set_group_info(group, new_name="", new_description="")
        Change group name and/or description.
    set_share_quota(group, share_quotas)
        Set group quota for a given share.
    set_share_permissions(group, permissions)
        Set group permissions for a given share.
    set_speed_limit(group, upload_limit, download_limit, protocol)
        Set speed limit for a given share.
    add_users(group, users)
        Add users to a group.
    remove_users(group, users)
        Remove users from a group.
    create(name, description="")
        Create a new group.
    delete(groups)
        Delete specified groups.
    """

    def get_groups(
        self, offset: int = 0, limit: int = -1, name_only: bool = False
    ) -> dict[str, object]:
        """
        Retrieve groups information.

        Parameters
        ----------
        offset : int, optional
            The offset of the groups to retrieve. Defaults to 0.
        limit : int, optional
            The maximum number of groups to retrieve. Defaults to -1 (all groups).
        name_only : bool, optional
            If True, returns only group names. If False, returns full group information. Defaults to False.

        Returns
        -------
        dict[str, object]
            A dictionary containing the groups information.

        Examples
        --------
        ```json
        {
            "data": {
                "groups": [
                    {
                        "description": "System default admin group",
                        "gid": 101,
                        "name": "administrators"
                    },
                    {
                        "description": "System default group for Web services",
                        "gid": 1023,
                        "name": "http"
                    },
                    {
                        "description": "A test group",
                        "gid": 65536,
                        "name": "Test"
                    },
                    {
                        "description": "System default group",
                        "gid": 100,
                        "name": "users"
                    }
                ],
                "offset": 0,
                "total": 4
            },
            "success": true
        }
        ```
        """

        api_name = "SYNO.Core.Group"
        info = self.core_list[api_name]
        api_path = info["path"]

        if name_only:
            name_only = "true"
        elif not name_only:
            name_only = "false"
        else:
            return "name_only must be True or False"
        req_param = {
            "version": info["maxVersion"],
            "method": "list",
            "offset": offset,
            "limit": limit,
            "name_only": name_only,
            "type": "local",
        }

        return self.request_data(api_name, api_path, req_param)

    def get_users(self, group: str, in_group: bool = True) -> dict[str, object]:
        """
        Retrieve users who are members or not members of a group.

        Parameters
        ----------
        group : str
            The group to list users from.
        in_group : bool, optional
            If True, retrieves users who are members of the specified group.
            If False, retrieves users who are not members of the group. Defaults to True.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "offset": 0,
                "total": 3,
                "users": [
                    {
                        "description": "System default user",
                        "name": "admin",
                        "uid": 1024
                    },
                    {
                        "description": "",
                        "name": "customAdmin",
                        "uid": 1026
                    },
                    {
                        "description": "",
                        "name": "test",
                        "uid": 1032
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Group.Member"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "list",
            "group": group,
            "ingroup": in_group,
        }

        return self.request_data(api_name, api_path, req_param)

    def get_speed_limits(self, group: str) -> dict[str, object]:
        """
        Retrieve bandwidth control settings for a given group.

        Parameters
        ----------
        group : str
            The group to retrieve settings for.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "bandwidths": [
                    {
                        "download_limit_1": 0,
                        "download_limit_2": 0,
                        "name": "group_name",
                        "owner_type": "local_group",
                        "policy": "notexist",
                        "protocol": "FTP",
                        "protocol_ui": "FTP",
                        "schedule_plan": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                        "upload_limit_1": 0,
                        "upload_limit_2": 0
                    },
                ]
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.BandwidthControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": 2,
            "method": "get",
            "name": group,
            "owner_type": "local_group",
        }
        return self.request_data(api_name, api_path, req_param)

    def get_quota(self, group: str) -> dict[str, object]:
        """
        Retrieve quota settings for a given group.

        Parameters
        ----------
        group : str
            The group to retrieve quota settings for.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "group_quota": [
                    {
                        "deduped": false,
                        "quota_status": "v1",
                        "shares": [
                            {
                                "description": "",
                                "name": "ActiveBackupforBusiness",
                                "quota": 1024
                            }
                        ],
                        "support_share_quota": true,
                        "volume": "/volume3"
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Quota"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": 1,
            "method": "get",
            "name": group,
            "subject_type": "group",
            "support_share_quota": True,
        }
        return self.request_data(api_name, api_path, req_param)

    def get_permissions(self, group: str) -> dict[str, object]:
        """
        Retrieve share permissions for a given group.

        Parameters
        ----------
        group : str
            The group to list permissions for.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
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
                ["dec", "local", "usb", "sata", "cluster",
                    "c2", "cold_storage", "worm"]
            ),
            "additional": json.dumps(["hidden", "encryption", "is_aclmode"]),
        }
        return self.request_data(api_name, api_path, req_param)

    def set_group_info(
        self, group: str, new_name: str = "", new_description: str = ""
    ) -> dict[str, object]:
        """
        Change group name and/or description.

        Parameters
        ----------
        group : str
            The group to set information for.
        new_name : str, optional
            The new name of the group. Defaults to current value.
        new_description : str, optional
            The new description of the group. Defaults to current value.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "gid": 65536,
                "name": "Test_mod"
            },
            "success": true
        }
        ```
        """
        current_groups_info = self.groups_info()
        current_group = filter(
            lambda group: group["name"] == group, current_groups_info["data"]["groups"]
        )

        # Set to current if no name or description is provided
        if new_name == "":
            new_name = group
        if new_description == "":
            new_description = list(current_group)[0]["description"]

        api_name = "SYNO.Core.Group"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "set",
            "name": group,
            "new_name": new_name,
            "description": new_description,
        }

        return self.request_data(api_name, api_path, req_param)

    def set_share_quota(
        self, group: str, share_quotas: list[dict[str, Any]]
    ) -> dict[str, object]:
        """
        Set group quota for a given share.

        Parameters
        ----------
        group : str
            The group to set the quota for.
        share_quotas : list of dict
            The quotas to set for the group.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {},
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Quota"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "set",
            "name": group,
            "group_quota": json.dumps(share_quotas),
        }

        return self.request_data(api_name, api_path, req_param)

    def set_share_permissions(
        self, group: str, permissions: list[dict[str, object]]
    ) -> dict[str, object]:
        """
        Set group permissions for a given share.

        Parameters
        ----------
        group : str
            The group to set the permissions for.
        permissions : list of dict
            The permissions to set for the group.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
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

    def set_speed_limit(
        self,
        group: str,
        upload_limit: int,
        download_limit: int,
        protocol: str,
    ) -> dict[str, object]:
        """
        Set speed limit for a given share.

        Parameters
        ----------
        group : str
            The group to set the speed limit for.
        upload_limit : int
            The maximum upload speed in KB/s.
        download_limit : int
            The maximum download speed in KB/s.
        protocol : str
            The protocol to set the speed limit for. Possible values:
            FileStation, WebDAV, FTP, NetworkBackup (Rsync), CloudStation (Synology Drive).

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "results": [
                    true
                ]
            },
            "success": true
        }
        ```

        Note: Doesn't support scheduled speed limits, only on/off.
        """
        settings = [
            {
                "upload_limit_1": upload_limit,
                "download_limit_1": download_limit,
                "policy": "enabled",
                "protocol": protocol,
                "owner_type": "local_group",
                "schedule_plan": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "upload_limit_2": 0,
                "download_limit_2": 0,
                "name": group,
            }
        ]

        api_name = "SYNO.Core.BandwidthControl"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {"version": 1, "method": "set",
                     "bandwidths": json.dumps(settings)}

        return self.request_data(api_name, api_path, req_param)

    def add_users(self, group: str, users: list[str]) -> dict[str, object]:
        """
        Add users to a group.

        Parameters
        ----------
        group : str
            The group to add users to.
        users : list of str
            The users to add to the group.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {},
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Group.Member"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "change",
            "group": group,
            "add_member": json.dumps(users),
            "remove_member": "[]",
        }

        return self.request_data(api_name, api_path, req_param)

    def remove_users(self, group: str, users: list[str]) -> dict[str, object]:
        """
        Remove users from a group.

        Parameters
        ----------
        group : str
            The group to remove users from.
        users : list of str
            The users to remove from the group.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {},
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Group.Member"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "change",
            "group": group,
            "add_member": "[]",
            "remove_member": json.dumps(users),
        }

        return self.request_data(api_name, api_path, req_param)

    def create(self, name: str, description: str = "") -> dict[str, object]:
        """
        Create a new group.

        Parameters
        ----------
        name : str
            Name to assign to the group.
        description : str, optional
            Description to assign to the group. Defaults to empty string.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {
                "gid": 65541,
                "name": "new_group"
            },
            "success": true
        }
        ```
        """

        api_name = "SYNO.Core.Group"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "create",
            "name": name,
            "description": description,
        }

        return self.request_data(api_name, api_path, req_param)

    def delete(self, groups: list[str]) -> dict[str, object]:
        """
        Delete specified groups.

        Parameters
        ----------
        groups : list of str
            The groups to delete.

        Returns
        -------
        dict[str, object]
            A dictionary containing the result of the request.

        Examples
        --------
        ```json
        {
            "data": {},
            "success": true
        }
        ```
        """
        api_name = "SYNO.Core.Group"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "delete",
            "name": json.dumps(groups),
        }

        return self.request_data(api_name, api_path, req_param)
