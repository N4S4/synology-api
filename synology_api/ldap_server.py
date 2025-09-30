"""Directory_server.py works with base_api_core to provide AD capabilities."""

from __future__ import annotations
import json
from datetime import datetime
from typing import Literal
from . import base_api


class LdapServer(base_api.BaseApi):
    """
    The LDAP server API.

    Be aware that invalid parameters may result in incomplete entries instead of just throwing an error.

    Note that even though this API calls 'SYNO.DirectoryServer', this API is used for the LDAP server package,
    not for the Directory Server package.
    """

    def list_users(self,
                   offset: int = 0,
                   limit: int = 40,
                   sort_direction: Literal["ASC", "DESC"] = "ASC"
                   ) -> dict[str, object]:
        """
        List users.

        Parameters
        ----------
        offset : int, optional
            When searching large data, you may wish to start at a certain number, e.g. for 10 at a time one
            would set the limit to 10 and the offset by multiples of 10 for each request. Defaults to `0`.
        limit : int, optional
            The number of maximum objects to return. Defaults to `40`.
        sort_direction : str, optional
            Sorts the results in ascending or descending order. Possible values: "ASC" or "DESC". Defaults to `ASC`.

        Returns
        -------
        dict[str, object]
            This returns a list of users in your LDAP Server.

        Examples
        --------
        ```json
        {
            "data": {
                "items": [
                    {
                        "descr": "Directory/Diskstation default admin user",
                        "disabled": "Disable",
                        "dn": "uid=admin,cn=users,dc=my,dc=domain,dc=com",
                        "email": "",
                        "name": "admin"
                    },
                    {
                        "descr": "This is a dummy user",
                        "disabled": "Normal",
                        "dn": "uid=dummyuser,cn=users,dc=my,dc=domain,dc=com",
                        "email": "dummy@my-domain.com",
                        "name": "dummyuser"
                    }
                ],
                "total": 2,
                "total_entry": 2
            },
            "success": true
        }
        ```
        """
        action = 'enum'
        api = 'SYNO.DirectoryServer.User'
        method = 'list'
        sort_by = "name"
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api, 'action': action, 'limit': limit, "method": method, 'start': offset,
                     'sort_by': sort_by, 'sort_direction': sort_direction, 'version': info['maxVersion']}
        return self.request_data("", api_path, req_param, 'post')

    def create_new_user(
            self,
            username: str,
            description: str,
            email: str,
            password: str,
            group_dn: str,
            groups: list[str] = None,
            newusermail: bool = False,
            send_password: bool = False,
            disallowchpasswd: bool = False,
            disabled: bool = False,
            expireddate: str = None,
            employeeNumber: str = None,
            department: str = None,
            employeeType: str = None,
            title: str = None,
            telephoneNumber: str = None,
            homePhone: str = None,
            mobile: str = None,
            postalAddress: str = None,
            apple_birthday: str = None,
    ) -> dict[str, object]:
        """
        Create a new user.

        Parameters
        ----------
        username : str
            The desired username. E.g. `jdoe`.
        description : str
            The description of the user.
        email : str
            The email of the user.
        password : str
            The password of the user in Plaintext.
        group_dn : str
            Your group DN. Normally this is 'cn=users,dc=my,dc=domain,dc=com'.
        groups : list[str], optional
            Name of your groups. 'users' is automatically included.
        newusermail : bool, optional
            Set to 'True' to send the new user a notification email. Defaults to `False`.
        send_password : bool, optional
            Set to 'True' to include the password in the notification email.
            Requires newusermail to be set to 'True'. Defaults to `False`.
        disallowchpasswd : bool, optional
            Set to 'True' to disallow password change. Defaults to `False`.
        disabled : bool, optional
            Set to 'True' to disable the user. Required expireddate to be set. Defaults to `False`.
        expireddate : str, optional
            Set the expiry date. Requires disabled to be set to 'True'.
            Allowed values: 'now' or a 'YYYY/mm/dd' timestring.
        employeeNumber : str, optional
            The user's employee number.
        department : str, optional
            The user's department.
        employeeType : str, optional
            The user's employee type.
        title : str, optional
            The user's title.
        telephoneNumber : str, optional
            The user's telephone number.
        homePhone : str, optional
            The user's home phone number.
        mobile : strNone, optional
            The user's mobile number.
        postalAddress : str, optional
            The user's address.
        apple_birthday : str, optional
            The user's birthday. Format: 'YYYYmmdd000000Z'.
            e.g. for 2025/01/16, pass '20250116000000Z'

        Returns
        -------
        dict[str, bool]
            Returns {'success': bool}.

        Examples
        --------
        ```json
            {
              "success": true
            }
        ```
        """

        def _assert_expireddate_validity():
            """Check if the 'expireddate' and 'disabled' parameters are valid."""
            if disabled and not expireddate:
                raise ValueError(
                    "If you disable the user, you need to provide the 'expireddate' parameter.")
            if expireddate:
                if not disabled:
                    raise ValueError(
                        "If you set the 'expireddate' parameter, you also need to set 'disabled' to true.")
                if expireddate == "now":
                    return
                try:
                    datetime.strptime(expireddate, "%Y/%m/%d")
                except ValueError:
                    ValueError(
                        "The 'expireddate' parameter must be 'now' or 'YYYY/MM/DD'")

        _assert_expireddate_validity()

        api_name = "SYNO.DirectoryServer.User"
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']

        info_string = json.dumps({
            k: v for k, v in {
                'useruid': username,
                'descr': description,
                'email': email,
                'passwd': password,
                'confirmpasswd': password,
                'newusermail': newusermail,
                'send_password': send_password,
                'disallowchpasswd': disallowchpasswd,
                'disabled': disabled,
                'expireddate': expireddate
            }.items() if v is not None
        })

        if groups is None:
            groups = []
        if 'users' not in groups:
            groups.append('users')
        group_string = json.dumps([
            {'groupdn': f'cn={grp},{group_dn}', "join": True} for grp in groups
        ])

        extend_string = json.dumps({
            k: v for k, v in {
                'employeeNumber': employeeNumber,
                'departmentNumber': department,
                'employeeType': employeeType,
                'title': title,
                'telephoneNumber': telephoneNumber,
                'homePhone': homePhone,
                'mobile': mobile,
                'postalAddress': postalAddress,
                'appleBirthday': apple_birthday,
            }.items() if v is not None
        })

        req_param = {
            'api': api_name,
            'version': info['maxVersion'],
            'method': 'set',
            'is_create': 'true',
            'info': info_string,
            'group': group_string,
            'extend': extend_string,
        }
        return self.request_data(api_name, api_path, req_param)
