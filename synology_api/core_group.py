from __future__ import annotations
import json
from typing import Any
from . import base_api


class Group(base_api.BaseApi):
    """
    Core Group API implementation.

    """

    def groups_info(
        self, offset: int = 0, limit: int = -1, name_only: bool = False
    ) -> dict[str, object] | str:
        """Retrieve groups information.

                Returns:
                    dict|str:
                        A dictionary containing the groups information, or a string in case of an error.

                    Example return:
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

    def add_users(self, group_name: str, users: list[str]) -> dict[str, object] | str:
        """
        Add users to a group.

        Args:
            group_name (str): The group to add users to.
            users (list[str]): The users to add to the group.

        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.

            Example return:
            {
                "data": {},
                "success": true
            }
        """
        api_name = "SYNO.Core.Group.Member"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "change",
            "group": group_name,
            "add_member": json.dumps(users),
            "remove_member": "[]",
        }

        return self.request_data(api_name, api_path, req_param)

    def remove_users(
        self, group_name: str, users: list[str]
    ) -> dict[str, object] | str:
        """
        Remove users from a group.

        Args:
            group_name (str): The group to remove users from.
            users (list[str]): The users to remove from the group.

        Returns:
            dict|str: A dictionary containing the result of the request, or a string in case of an error.

            Example return:
            {
                "data": {},
                "success": true
            }
        """
        api_name = "SYNO.Core.Group.Member"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["minVersion"],
            "method": "change",
            "group": group_name,
            "add_member": "[]",
            "remove_member": json.dumps(users),
        }

        return self.request_data(api_name, api_path, req_param)
