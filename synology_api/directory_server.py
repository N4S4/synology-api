"""Directory_server.py works with base_api_core to provide AD capabilities."""

from __future__ import annotations
import json
import time
from typing import Optional, Any
from . import base_api


class DirectoryServer(base_api.BaseApi):
    """
    The directory server API.

    Not all items within this class use the Active Directory API. Some use the Synology Entry API which proxies
    the request. Some are related to managing users in ways that are useful in the Directory Server context. For
    example, sending a user password reset email, or updating the user information. This api works slightly
    differently than other similar APIs. There are multi-leveled calls where Synology makes requests on behalf of
    the original request and relays information back. Additionally, the query-string api item is not used often in
    this class as API is defined within the actual request.

    The APIs in this class are tested working against the following scenarios:

    - Getters:
        - Get Active Directory information
        - List objects within a Base DN on the Active Directory Server
        - Check if an AD object within your Directory Server
        - Get the status of a running task such as the Domain status update
    - Setters:
        - Set the user's AD password
        - Update user information within the Directory Server
        - Update Synology's awareness of the current state of the Domain
    - Actions:
        - Create an AD user
        - Add an AD user to an AD group
        - Create a new AD group
        - Send a password reset email to any Synology user
        - Delete a list of items from the Directory Server
        - Delete a single item from the Directory Server
        - Perform an entry request to complete a Deletion
    """

    def get_directory_info(self) -> dict[str, object]:
        """
        Get directory info.

        Returns
        -------
        dict[str, object]
            Information about your domain.

        Examples
        --------
        ```json
        {
            "data": {
                "data": {
                "domainBasicInfo": {
                    "realm": "MY.DOMAIN.COM",
                    "workgroup": "NETBIOSNAME"
                },
                "domainControllers": [
                    {
                    "cn": "AD",
                    "dn": "CN=AD,OU=Domain Controllers,DC=MY,DC=DOMAIN,DC=COM",
                    "dnshostname": "AD.MY.DOMAIN.COM",
                    "roles": [
                        "pdc",
                        "rid",
                        "schema",
                        "naming",
                        "infrastructure"
                    ]
                    }
                ]
                },
                "status": "running"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.ActiveDirectory.Info'
        info = {'maxVersion': 3, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api_name, 'method': 'get',
                     'version': info['maxVersion']}
        return self.request_data(api_name, api_path, req_param)

    def list_directory_objects(self,
                               basedn: str,
                               offset: int = 0,
                               limit: int = 40,
                               objectCategory: list[str] = [
                                   "person", "group", "organizationalUnit", "computer", "container", "builtinDomain"]
                               ) -> dict[str, object]:
        """
        List directory objects.

        Parameters
        ----------
        basedn : str
            The Base DN for the search. E.g. `CN=Users,CN=MY,CN=DOMAIN,CN=COM` or `CN=MY,CN=DOMAIN,CN=COM`.
        offset : int, optional
            When searching large data, you may wish to start at a certain number, e.g. for 10 at a time one
            would set the limit to 10 and the offset by multiples of 10 for each request. Defaults to `0`.
        limit : int, optional
            The number of maximum objects to return. Defaults to `40`.
        objectCategory : list[str], optional
            The categories of items to search. E.g. `["organizationalUnit","container","builtinDomain"]` for a list of
            base server containers, and `["person","group","organizationalUnit","computer"]` for a list of contained objects.
            Defaults to `["person","group","organizationalUnit","computer","container","builtinDomain"]`.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary. The first level is the success to the AD server.  The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "data": [
                {
                    "accountExpiryTime": 910692730085,
                    "deletable": true,
                    "description": "This is a description of a user person",
                    "disabled": false,
                    "displayName": "John Doe",
                    "dn": "CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM",
                    "locked": false,
                    "mail": "jdoe@MY.EMAIL.COM",
                    "movable": true,
                    "name": "john",
                    "objectCategory": "person",
                    "passwordExpired": true,
                    "physicalDeliveryOfficeName": "official office of officers",
                    "primaryGroupToken": 0,
                    "renamable": true,
                    "sAMAccountName": "jdoe",
                    "showInAdvancedViewOnly": false,
                    "telephoneNumber": "123-444-5677"
                },
                ],
                "total": 99999
            },
            "success": true
        }
        ```
        """
        action = '"enum"'
        scope = '"one"'
        api = 'SYNO.ActiveDirectory.Directory'
        method = '"list"'
        info = {'maxVersion': 3, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api, 'action': action, 'basedn': '"'+basedn+'"', 'limit': limit, "method": method,
                     'objectCategory': json.dumps(objectCategory), 'offset': offset, 'scope': scope,  'version': info['maxVersion']}
        print(req_param)
        return self.request_data("", api_path, req_param, 'post')

    def create_new_user(
            self,
            logon_name: str,
            email: str,
            password: str,
            located_dn: str,
            description: str = '',
            account_is_disabled: str = 'false',
            cannot_change_password: str = 'false',
            change_password_next_logon: str = 'null',
            password_never_expire: str = 'true'
    ) -> dict[str, object]:
        """
        Create a new user.

        Parameters
        ----------
        logon_name : str
            The desired username. E.g. `jdoe`.
        email : str
            The desired email.
        password : str
            The plain-text password for the new user. E.g. `Password123`.
        located_dn : str
            The DN for the user. E.g. `CN=Users,CN=MY,CN=DOMAIN,CN=COM`.
        description : str, optional
            A description for the user.
        account_is_disabled : str
            Set to 'true' if the account should be disabled. Defaults to `False`.
        cannot_change_password : str, optional
            Set to 'true' if the user cannot change the password. Defaults to `False`.
        change_password_next_logon : str, optional
            Set to 'true' if the user must change password on next logon. Defaults to `False`.
        password_never_expire : str
            Set to 'true' if the password never expires.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.

        Notes
        -----
        The user can be created in AD, but not able to log on until the next synchronization occurs.
        Please note that synchronization with Synology is a separate step.

        Examples
        --------
        ```json
        {
            'data': {
                'dn': 'CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM',
                'name': 'NETBIOSNAME\\ababab'
            },
            'success': true
        }
        ```
        """

        api_name = "SYNO.ActiveDirectory.User"
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api_name, 'version': info['maxVersion'], 'method': 'create', 'logon_name': logon_name, 'email': email,
                     'located_dn': located_dn, 'password': password,  'description': description, 'account_is_disabled': account_is_disabled,
                     'cannot_change_password': cannot_change_password, 'change_password_next_logon': change_password_next_logon,
                     'password_never_expire': password_never_expire}
        return self.request_data(api_name, api_path, req_param)

    def reset_password(self,
                       username: str,
                       ) -> dict[str, object]:
        """
        Send a password reset email.

        This will trigger the password reset email from
        Control Panel>Notification>Rules>System>Reset password for your account to be sent to the user.

        Parameters
        ----------
        username : str
            The username to reset. E.g. `My Group`.

        Returns
        -------
        dict[str, object]
            The return object can be checked for the "success" to be a true or false.

        Notes
        -----
        In order to use this, Control Panel>User & Group>Advanced>"Allow non-administrator users to reset forgotten passwords via email" must be enabled.

        Examples
        --------
        ```json
        {
            "data": {
                "msg": 3
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Auth.ForgotPwd'
        newApi = {'maxVersion': 1, 'minVersion': 1,
                  'path': 'entry.cgi', 'requestFormat': 'JSON'}
        info = newApi
        api_path = info['path']
        req_param = {'method': 'send', 'user': '"' +
                     username+'"', 'version': newApi['maxVersion']}
        return self.request_data(api_name, api_path, req_param)

    def change_user_password(self, user_dn: str, password: str) -> dict[str, object]:
        """
        Change the user's password.

        Parameters
        ----------
        user_dn : str
            The user DN to be modified. E.g. `CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM`.
        password : str
            The new password to be set. E.g. `Password123`.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.

        Notes
        -----
        This is a compound dual-level request where the synology API proxies your request to the Directory Server.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": false,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.User",
                    "data": [
                    {
                        "code": 0,
                        "msg": "update record successfully"
                    }
                    ],
                    "method": "set",
                    "success": true,
                    "version": 2
                }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = "SYNO.Entry.Request"
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        compound = '[{"api":"SYNO.ActiveDirectory.User","method":"set","version":2,"userList":[{"dn":"' + \
            user_dn+'","enbl_change_password":true,"password":"'+password+'"}]}]'
        api_path = info['path']
        req_param = {"api": api_name, 'method': 'request', 'compound': compound,
                     'mode': 'sequential', 'stop_when_error': "true", 'version': info['maxVersion']}
        return self.request_data(api_name, api_path, req_param)

    def create_new_group(
            self,
            name: str,
            located_dn: str,
            email: Optional[str] = '',
            description: Optional[str] = '',
            type: Optional[str] = 'security',
            scope: Optional[str] = 'global'
    ) -> dict[str, object]:
        """
        Create a new AD group.

        Parameters
        ----------
        name : str
            The name of the group. E.g. `My Group`.
        located_dn : str
            The DN to place the group in. E.g. `CN=Groups,DC=MY,DC=DOMAIN,DC=COM`.
        email : str, optional
            The email address used to reference this group. Defaults to `""`.
        description : str, optional
            A description of the AD Group. Defaults to `""`.
        type : str, optional
            Example Options: `security`, `distribution`. Defaults to `"security"`.

            (definitions from https://docs.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups?view=o365-worldwide )
                - `distribution` (Distribution groups) are used for sending email
                    notifications to a group of people.
                - `security` - Security groups are used for granting access to resources
                    such as SharePoint sites.

        scope : str, optional
            Example Options: `local`, `global`, `universal`. Defaults to `"global"`.
                (Definitions from
                https://www.netwrix.com/active_directory_group_management.html )
                    - `local` (Domain Local Groups) should be used to manage permissions to
                    resources because this group can be applied everywhere in the domain.
                    A domain local group can include members of any type in the domain and
                    members from trusted domains. For example, suppose you need access
                    management for a collection of folders on one or more servers that
                    contain information for managers. The group you create for that purpose
                    should be a domain local group (ex. “DL_Managers_Modify”).
                    - `global` (Global Groups) are used primarily to define collections of
                    domain objects (users, other global groups and computers) based on
                    business roles, which means that they mostly serve as role groups.
                    Role-based groups of users (such as “HR” or “Marketing”) and role-based
                    groups of computers (such as a “Marketing Workstations”) areusually
                    global groups.
                    - `universal` (Universal Groups) in Active Directory are useful in
                    multi-domain forests. They enable you to define roles or manage
                    resources that span more than one domain. Each universal group is
                    stored in the domain of where it was created, but its group membership
                    is stored in the Global Catalog and replicated forest-wide. Don’t use
                    universal groups if you have only one domain.

        Returns
        -------
        dict[str, object]
            A success object, and data object containing the new dn and the netbios name of the group.

        Examples
        --------
        ```json
        {
            'data': {
                'dn': 'CN=My Group,CN=Groups,DC=MY,DC=DOMAIN,DC=COM',
                'name': 'NETBIOSNAME\\My Group'
            },
            'success': true
        }
        ```
        """
        api_name = 'SYNO.ActiveDirectory.Group'
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api_name, 'method': 'create', 'name': name, 'located_dn': located_dn,
                     'description': description, 'type': type, 'scope': scope, 'email': email, 'version': info['maxVersion']}
        return self.request_data(api_name, api_path, req_param)

    def add_user_to_group(self, userDn: str, groupDn: str) -> dict[str, object]:
        """
        Add a user as a member of a group.

        Parameters
        ----------
        userDn : str
            The fully qualified dn to add. E.g. `CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM`.
        groupDn : str
            The fully qualified dn of the group to which the user is to be added. E.g. `CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM`.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.
            The first level is the success to the AD server.  The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": false,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.Group.Member",
                    "data": {
                    "members": [
                        "CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM"
                    ]
                    },
                    "method": "add",
                    "success": true,
                    "version": 1
                }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Entry.Request'
        compound = '[{"api":"SYNO.ActiveDirectory.Group.Member","method":"add","version":"1","dn":"' + \
            groupDn+'","members":["'+userDn+'"]}]'
        method = 'request'
        mode = "sequential"
        stop_when_error = True
        newApi = {'maxVersion': 1, 'minVersion': 1,
                  'path': 'entry.cgi', 'requestFormat': 'JSON'}
        info = newApi
        api_path = info['path']
        req_param = {'api': api_name, 'compound': compound, 'method': method, 'mode': mode,
                     'stop_when_error': stop_when_error, 'version': newApi['maxVersion']}
        return self.request_data(api_name, api_path, req_param)

    def does_dn_exist(self, groupName: str) -> dict[str, object]:
        """
        Check if a container exists.

        This can be used to verify the username or group name is unique.

        Parameters
        ----------
        groupName : str
            The user, or group's name. E.g. `jdoe` or `My Cool Group`.
            Fully Qualified Domain Name such as `CN=My Cool Group,CN=Groups,DC=MY,DC=DOMAIN,DC=COM` are not successful.
            Improper case such as `my cool group` instead of `My Cool Group` are successful.

        Returns
        -------
        dict[str, object]
            `True` if the group exists. `False` if the group does not exist.

        Notes
        -----
        This will not check the container, only if a similarly named container already exists.
        """

        api_name = 'SYNO.ActiveDirectory.Group'
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'conflict', 'name': groupName}
        return self.request_data(api_name, api_path, req_param)['data']['isConflict']

    def modify_user_info(self,
                         user_dn: str = None,
                         firstName: str = None,
                         lastName: str = None,
                         displayName: str = None,
                         description: str = None,
                         initials: str = None,
                         physicalDeliveryOfficeName: str = None,
                         telephoneNumber: str = None,
                         web: str = None
                         ) -> dict[str, object]:
        """
        Modify user information within the Active Directory.

        Parameters
        ----------
        user_dn : str, optional
            The user DN to be modified. E.g. `CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM`.
        firstName : str, optional
            The First name of the user. E.g. `John`.
        lastName : str, optional
            The Last Name of the user. E.g. `Doe`.
        displayName : str, optional
            The Display name of the user. E.g. `John Doe`.
        description : str, optional
            The Description of the user. E.g. `The guy who just came in`.
        initials : str, optional
            The Initials of the user. E.g. `JD`.
        physicalDeliveryOfficeName : str, optional
            The office location in the user's place of business.
        telephoneNumber : str, optional
            The user's telephone number.
        web : str, optional
            The user's website or location on the web where information can be obtained.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.
            The first level is the success to the AD server. The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": true,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.User",
                    "error": {
                    "code": 10104,
                    "errors": [
                        {
                        "code": 10237,
                        "msg": "ldb updaterecords: modify"
                        }
                    ]
                    },
                    "method": "set",
                    "success": false,
                    "version": 2
                }
                ]
            },
            "success": true
        }
        ```
        """
        class Person:
            """Represents a user object for Active Directory modifications."""
            firstName
            lastName
            displayName
            description
            initials
            physicalDeliveryOfficeName
            telephoneNumber
            web
            user_dn
        userObject = Person()
        userObject.dn = user_dn
        if firstName is not None:
            userObject.firstName = firstName
        if lastName is not None:
            userObject.lastName = lastName
        if displayName is not None:
            userObject.displayName = displayName
        # if description is not None:
        #    userObject.description = description
        if initials is not None:
            userObject.initials = initials
        if physicalDeliveryOfficeName is not None:
            userObject.physicalDeliveryOfficeName = physicalDeliveryOfficeName
        if telephoneNumber is not None:
            userObject.telephoneNumber = telephoneNumber
        if web is not None:
            userObject.web = web

        theJsonObject = userObject.__dict__
        val = self.setEntryRequest(
            "SYNO.ActiveDirectory.User", "set", "userList", theJsonObject)

        return val

    def setEntryRequest(self, modificationAPI: str, method: str, nameOfObject: str, jsonObject: Any) -> dict[str, object]:
        """
        Modify an object within the Active Directory.

        Parameters
        ----------
        modificationAPI : str
            API to be used.
        method : str
            Method to be called.
        nameOfObject : str
            The user DN to be modified. E.g. `"CN=jdoe,CN=Users,DC=MY,DC=DOMAIN,DC=COM"`.
        jsonObject : str
            The json Object to be added, e.g., a user object.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.
            The first level is the success to the AD server.  The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": true,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.User",
                    "error": {
                    "code": 10104,
                    "errors": [
                        {
                        "code": 10237,
                        "msg": "ldb updaterecords: modify"
                        }
                    ]
                    },
                    "method": "set",
                    "success": false,
                    "version": 2
                }
                ]
            },
            "success": true
        }
        ```
        """
        compound = [{"api": modificationAPI, "method":  method,
                     "version": 2, nameOfObject: [jsonObject]}]
        api_name = "SYNO.Entry.Request"
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {"api": api_name, 'method': 'request', 'compound': json.dumps(
            compound), 'mode': '"sequential"', 'stop_when_error': True, 'version': info['maxVersion']}
        print(json.dumps(req_param))
        return self.request_data(api_name, api_path, req_param, "post")

    def update_domain_records(self) -> dict[str, object]:
        """
        Update the Synology users and groups database with information from Directory Server.

        This is a long-running and asynchronous task. You are given back a task_id, and you can use that task_id to check the status with the get_task_status(task_id) method.

        Returns
        -------
        dict[str, object]
            The 'data' object contains the 'task_id' used to track with the getTaskStatus() method.

        Notes
        -----
        Typical utilization of Update Domain requires starting the update job and waiting for
        completion. Waiting involves using the getTaskStatus and can be accomplished via a busy-wait method such as the following:

            ```python
            updateResponse=directory.updateDomain()
            status = directory.getTaskStatus(updateResponse['data']['task_id'])
            while status['data']['status'] == 'updating':
                status=directory.getTaskStatus(updateResponse['data']['task_id'])
            ```

        Examples
        --------
        ```json
        {
            "data": {
                "task_id": "@administrators/DomainUpdate6146195136397F2"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'domain_name': '"@all"',
                     'method': 'update_start', 'version': info['minVersion']}
        return self.request_data(api_name, api_path, req_param)

    def get_task_status(self, task_id: str) -> dict[str, object]:
        """
        Get the current status of a task running on the Directory Domain object.

        This is used to ensure the task is completed. For example, the primary utilization of this is when updating Synology's internal Domain user and group list.

        Until this method reports finish, the job is not completed, and it is not safe to operate under the assumption that users have been synchronized.

        Parameters
        ----------
        task_id : str
            The task ID to be tracked for status.

        Returns
        -------
        dict[str, object]
            The 'data' object contains the 'status' used to determine the current status. 'status' will be 'updating' or 'finish' if the job was started.
            The 'success' object will be true if the operation was successful, or false if failed.

        Examples
        --------
        ```json
        {
            'data': {
                'status': 'updating'
            },
            'success': true
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.Domain'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'method': 'update_status',
                     'task_id': task_id, 'version': info['minVersion']}
        return self.request_data(api_name, api_path, req_param)

    def deleteItems(self, dnList: list[str]) -> dict[str, object]:
        """
        Delete an array of DNs from AD.

        Parameters
        ----------
        dnList : list[str]
            The fully qualified DN to be removed from the directory server. E.g. `["CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM","CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM"]`.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.
            The first level is the success to the AD server.  The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": false,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.Polling",
                    "data": {
                    "data": [
                        {
                        "dn": "CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM",
                        "status": {}
                        }
                    ],
                    "finished": true,
                    "total": 1
                    },
                    "method": "get",
                    "success": true,
                    "version": 1
                }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.ActiveDirectory.Directory'
        info = {'maxVersion': 2, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        api_path = info['path']
        req_param = {'api': api_name, 'method': 'delete',
                     'dnList': json.dumps(dnList), 'version': 2}
        task_id = self.request_data(api_name, api_path, req_param)[
            'data']['task_id']
        returnValue = self.entryRequest(task_id)
        notFinished = True
        while 'data' in returnValue['data']['result'][0] and notFinished:
            notFinished = False
            for resultItem in returnValue['data']['result']:
                if not resultItem['data']['finished']:
                    notFinished = True
            if not notFinished:
                break
            returnValue = self.entryRequest(task_id)

        return returnValue

    def delete_item(self, dn: str) -> dict[str, object]:
        """
        Delete a DN from AD.

        Parameters
        ----------
        dn : str
            The fully qualified DN to be removed from the directory server. E.g. `CN=jdoe,CN=Users,CN=MY,CN=DOMAIN,CN=COM` or `CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM`.

        Returns
        -------
        dict[str, object]
            The result of this method is a dictionary object with a 'data' dictionary and a 'success' dictionary.
            The first level is the success to the AD server.  The second Data level is the status of the actual request.
            Since this is a compound request, the data contains an object with it's own request and results contained within. The object will explain any issues with the request.

        Examples
        --------
        ```json
        {
            "data": {
                "has_fail": false,
                "result": [
                {
                    "api": "SYNO.ActiveDirectory.Polling",
                    "data": {
                    "data": [
                        {
                        "dn": "CN=My Group,CN=Groups,CN=MY,CN=DOMAIN,CN=COM",
                        "status": {}
                        }
                    ],
                    "finished": true,
                    "total": 1
                    },
                    "method": "get",
                    "success": true,
                    "version": 1
                }
                ]
            },
            "success": true
        }
        ```
        """
        items = []
        items.append(dn)
        return self.deleteItems(items)

    def entryRequest(self, task_id: str) -> Any:
        """
        Perform an entry request for a task.

        Some requests require an entry. Delete, for example, requires an entry. If an entry is required, the task will not complete without an Entry Request.

        Parameters
        ----------
        task_id : str
            The ID of the task to be checked. This is provided when making a request.
            An example Task ID may look like this
                `@administrators/Synoads_SYNO.ActiveDirectory.Directory_delete6145EA17C4F03DA9`.

        Returns
        -------
        Any
            The result of the entry request.
        """
        api_name = 'SYNO.Entry.Request'
        info = {'maxVersion': 1, 'minVersion': 1,
                'path': 'entry.cgi', 'requestFormat': 'JSON'}
        compound = '[{"api":"SYNO.ActiveDirectory.Polling","method":"get","version":1,"task_id":"'+task_id+'"}]'
        api_path = info['path']
        req_param = {'api': api_name, 'method': 'request',  'compound': compound,
                     'mode': 'parallel', 'version': info['maxVersion']}
        return self.request_data(api_name, api_path, req_param)
