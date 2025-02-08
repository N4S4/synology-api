import json
from typing import Any
from . import base_api


class User(base_api.BaseApi):
    """Core User API implementation.

        Supported actions:
            - Getters: 
                - Get all users
                - Password policies
                - Password expiry

            - Setters:
                - Set user password policy
            
            - Actions:
                - Create new user
                - Modify user
                - Delete user
                - User join/leave group
    """
    
    def get_users(
        self, offset: int = 0, limit: int = -1, sort_by: str = "name", sort_direction: str = "ASC", additional: list[str] = []
    ) -> dict[str, object]:
        """Retrieve groups information.

            Parameters
            ----------
            offset : int, optional
                The offset of the groups to retrieve. Defaults to `0`.

            limit : int, optional
                The maximum number of groups to retrieve. Defaults to `-1` .

            sort_by : str, optional
                Sort by a specific field. Defaults to `"name"`.

            sort_direction : str, optional
                The sort direction. Defaults to `"ASC"` else `"DESC"`.
                
            additional : list[str], optional
                Additional fields to retrieve. Defaults to `[]`.
                
                All fields known are: `["description","email","expired","cannot_chg_passwd","passwd_never_expire","password_last_change", "groups", "2fa_status"]`.


            Returns
            -------
            dict[str, object]
                A dictionary containing the groups information.

            Example return
            --------------
            ```json
            {
                "data": {
                    "offset": 0,
                    "total": 5,
                    "users": [
                    {
                        "description": "System default user",
                        "email": "",
                        "expired": "now",
                        "name": "admin",
                        "passwd_never_expire": true
                    },
                    {
                        "description": "Guest",
                        "email": "",
                        "expired": "now",
                        "name": "guest",
                        "passwd_never_expire": true
                    },
                    {
                        "description": "",
                        "email": "",
                        "expired": "normal",
                        "name": "test_api",
                        "passwd_never_expire": true
                    },
                    {
                        "description": "test description",
                        "email": "testemail@test.com",
                        "expired": "normal",
                        "name": "test_user",
                        "passwd_never_expire": true
                    }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.User"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": info['minVersion'],
            "type": "local", # TODO: Test with ldap and parameter "all"
            "offset": offset,
            "limit": limit,
            "sort_by": sort_by,
            "sort_direction": sort_direction,
            "additional": json.dumps(additional)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def get_user(self, name: str, additional: list[str] = []) -> dict[str, object]:
        """Retrieve a user information.

            Parameters
            ----------
            name : str
                The name of the user.

            additional : list[str], optional
                Additional fields to retrieve. Defaults to `[]`.

                All fields known are: `["description","email","expired","cannot_chg_passwd","passwd_never_expire","password_last_change","is_password_pending"]`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the user information.

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User",
                "data": {
                    "users": [
                        {
                            "cannot_chg_passwd": false,
                            "description": "",
                            "email": "",
                            "expired": "normal",
                            "is_password_pending": false,
                            "name": "test_api",
                            "passwd_never_expire": true,
                            "password_last_change": 19789,
                            "uid": 1027
                        }
                    ]
                },
                "method": "get",
                "success": true,
                "version": 1
            }
            ```
        """
        api_name = "SYNO.Core.User"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "type": "local",
            "version": info['minVersion'],
            "name": name,
            "additional": json.dumps(additional)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def create_user(
        self, name: str, password: str, description: str = "", email: str = "", expire: str = "never", cannot_chg_passwd: bool = False,
        passwd_never_expire: bool = True, notify_by_email: bool = False, send_password: bool = False
    ) -> dict[str, object]:
        """Create a new user.

            Parameters
            ----------
            name : str
                The name of the user.

            password : str
                The password of the user.

            description : str, optional
                The description of the user. Defaults to `""`.

            email : str, optional
                The email of the user. Defaults to `""`.

            expire : str, optional
                The expiration date of the user. Defaults to `"never"`.

            cannot_chg_passwd : bool, optional
                Whether the password can be changed. Defaults to `False`.

            passwd_never_expire : bool, optional
                Whether the password should never expire. Defaults to `True`.

            notify_by_email : bool, optional
                Whether to notify by email. Defaults to `False`.

            send_password : bool, optional
                Whether to send the password. Defaults to `False`.
            
            Returns
            -------
            dict[str, object]
                A dictionary containing the user information.

            Example return
            --------------
            ```json
            { 
                "data":
                {
                    "name":"toto",
                    "uid": 1030
                },
                "success": true
            }
            ```
        """
        
        api_name = "SYNO.Core.User"
        info = self.core_list[api_name]
        api_path = info["path"]

        req_param = {
            "method": "create",
            "version": info['minVersion'],
            "name": name,
            "description": description,
            "email": email,
            "expired": expire,
            "cannot_chg_passwd": cannot_chg_passwd,
            "passwd_never_expire": passwd_never_expire,
            "notify_by_email": notify_by_email,
            "send_password": send_password,
        }
        param_enc = {
            "password": password
        }
        # Using https
        if self.session._secure:
            req_param.update(param_enc)
        # Using http and self encrypted
        else:
            encrypted_param = self.session.encrypt_params(param_enc)
            req_param.update(encrypted_param)
    
        
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def modify_user(
        self, name: str, new_name: str, password: str = "", description: str = "", email: str = "", expire: str = "never", cannot_chg_passwd: bool = False,
        passwd_never_expire: bool = True, notify_by_email: bool = False, send_password: bool = False
    ) -> dict[str, object]:
        """Modify a user.

            Parameters
            ----------
            name : str
                The name of the actual user.

            new_name : str
                The new name of the user.

            password : str, optional
                The password of the user. Defaults to `""`.

            description : str, optional
                The description of the user. Defaults to `""`.

            email : str, optional
                The email of the user. Defaults to `""`.

            expire : str, optional
                The expiration date of the user. Defaults to `"never"`.

            cannot_chg_passwd : bool, optional
                Whether the password can be changed. Defaults to `False`.

            passwd_never_expire : bool, optional
                Whether the password should never expire. Defaults to `True`.

            notify_by_email : bool, optional
                Whether to notify by email. Defaults to `False`.

            send_password : bool, optional
                Whether to send the password. Defaults to `False`.
            
            Returns
            -------
            dict[str, object]
                A dictionary containing the user information.

            Example return
            --------------
            ```json
            {
                "data":{
                    "name": "test_user2",
                    "password_last_change": 20106,
                    "uid": 1028
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.User"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": info['minVersion'],
            "name": name,
            "new_name": new_name,
            "description": description,
            "email": email,
            "expired": expire,
            "cannot_chg_passwd": cannot_chg_passwd,
            "passwd_never_expire": passwd_never_expire,
            "notify_by_email": notify_by_email,
            "send_password": send_password
        }
        # Using https
        if self.session._secure:
            req_param.update({"password": password})
        # Using http and self encrypted
        else:
            req_param.update(self.session.encrypt_params({"password": password}))
            
        return self.request_data(api_name, api_path, req_param, method="post")
    
    def delete_user(self, name: str) -> dict[str, object]:
        """Delete a user.

            Parameters
            ----------
            name : str
                The name of the user to delete.

            Returns
            -------
            dict[str, object]
                A dictionary containing the user information.

            Example return
            --------------
            ```json
            {
                "data": {
                    "name": "toto",
                    "uid": 1030
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.User"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": info['minVersion'],
            "name": name
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def affect_groups(self, name: str, join_groups: list[str] = [], leave_groups: list[str] = []) -> dict[str, object]:
        """Affect or disaffect groups to a user.

            Tip: This request is asynchronous and will return a task id to check the status of the join task. Use `affect_groups_status` func to check the status of the task.

            Parameters
            ----------
            name : str
                The name of the user.

            join_groups : list[str]
                The names of the groups to join.

            leave_groups : list[str]
                The names of the groups to leave.
                
                
            Returns
            -------
            dict[str, object]
                A dictionary containing the task id to check the status of the join task. Use `affect_groups_status` func to check the status of the task.   

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User.Group",
                "data": {
                    "task_id": "@administrators/groupbatch1737238746C6723E33"
                },
                "method": "join",
                "success": true,
                "version": 1
            }
            ```
        """
        
        api_name = "SYNO.Core.User.Group"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "join",
            "version": info['minVersion'],
            "join_group": json.dumps(join_groups),
            "leave_group":json.dumps(leave_groups),
            "name":name
        }
        return self.request_data(api_name, api_path, req_param)
    
    def affect_groups_status(self, task_id:str):
        """Get the status of a join task.
        
            Parameters
            ----------
            task_id : str
                The task id of the join task.
                
            Returns
            -------
            dict[str, object]
                A dictionary containing the status of the join task.

            Example return
            --------------
            ```json
            {
                "data": {
                    "auto_remove": false,
                    "data": {
                        "name": "test_user2",
                        "pid": 18126,
                        "progress": 1,
                        "total": 1,
                        "uid": 1028
                    },
                    "finish": false,
                    "info": {
                        "api": "SYNO.Core.User.Group",
                        "group": "admin",
                        "method": "join",
                        "prefix": "groupbatch",
                        "version": 1
                    },
                    "success": true
                },
                "success": true
            }
            ```
        """
        api_name = "SYNO.Core.User.Group"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "join_status",
            "version": info['minVersion'],
            "task_id": task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_password_policy(self) -> dict[str, object]:
        """Get the password policy.

            Returns
            -------
            dict[str, object]
                A dictionary containing the password policy information.

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User.PasswordPolicy",
                "data": {
                    "enable_reset_passwd_by_email": false,
                    "password_must_change": false,
                    "strong_password": {
                        "exclude_username": true,
                        "history_num": 0,
                        "included_numeric_char": true,
                        "included_special_char": false,
                        "min_length": 8,
                        "min_length_enable": true,
                        "mixed_case": true
                    }
                },
                "method": "get",
                "success": true,
                "version": 1
            }
            ```
        """
        api_name = "SYNO.Core.User.PasswordPolicy"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": info['minVersion']
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_password_policy(
        self, enable_reset_passwd_by_email: bool = False, password_must_change: bool = False,
        exclude_username: bool = True, included_numeric_char: bool = True, included_special_char: bool = False,
        min_length: int = 8, min_length_enable: bool = True, mixed_case: bool = True,
        exclude_common_password: bool = False, exclude_history: bool = False
    ) -> dict[str, object]:
        """Set the password policy.

            Parameters
            ----------
            enable_reset_passwd_by_email : bool, optional 
                Defaults to `False`.

            password_must_change : bool, optional 
                Defaults to `False`.

            exclude_username : bool, optional 
                Defaults to `True`.

            included_numeric_char : bool, optional 
                Defaults to `True`.

            included_special_char : bool, optional 
                Defaults to `False`.

            min_length : int, optional 
                Defaults to `8`.

            min_length_enable : bool, optional 
                Defaults to `True`.

            mixed_case : bool, optional 
                Defaults to `True`.

            exclude_common_password : bool, optional 
                Defaults to `False`.

            exclude_history : bool, optional 
                Defaults to `False`.

            Returns
            -------
            dict[str, object]
                A dictionary indicating the success of the operation.
            
            Example return
            --------------
            ```json
                {
                    "api": "SYNO.Core.User.PasswordPolicy",
                    "data": {},
                    "method": "set",
                    "success": true,
                    "version": 1
                }
            ```
        """
                
        api_name = "SYNO.Core.User.PasswordPolicy"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": info['minVersion'],
            "enable_reset_passwd_by_email": enable_reset_passwd_by_email,
            "password_must_change": password_must_change,
            "strong_password":{
                "exclude_username": exclude_username,
                "included_numeric_char": included_numeric_char,
                "included_special_char": included_special_char,
                "min_length_enable": min_length_enable,
                "min_length": min_length,
                "mixed_case": mixed_case,
                "exclude_common_password": exclude_common_password,
                "exclude_history":exclude_history
            }
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_password_expiry(self) -> dict[str, object]:
        """Get the password expiry.

            Returns
            -------
            dict[str, object]
                A dictionary containing the password expiry information.

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User.PasswordExpiry",
                "data": {
                    "allow_reset_after_expired": true,
                    "enable_login_prompt": false,
                    "enable_mail_notification": false,
                    "mail_notification_days": "",
                    "min_age_enable": false,
                    "password_expire_enable": false
                },
                "method": "get",
                "success": true,
                "version": 1
            }
            ```
        """
        api_name = "SYNO.Core.User.PasswordExpiry"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": info['minVersion']
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_password_expiry(
        self, password_expire_enable: bool = False, max_age: int = 30, min_age_enable: bool = False, min_age: int = 1,
        enable_login_prompt: bool = False, login_prompt_days: int = 1, allow_reset_after_expired: bool = True,
        enable_mail_notification: bool = False, never_expired_list: list[str] = []
    ) -> dict[str, object]:
        """Set the password expiry.
        
            Parameters
            ----------
            password_expire_enable : bool, optional
                Enable password expiry. Defaults to `False`.

            max_age : int, optional
                Maximum time before password expiry. Defaults to `30`.

            min_age_enable : bool, optional
                Enable minimum time before password expiry. Defaults to `False`.

            min_age : int, optional
                Minimum time before password expiry. Defaults to `1`.

            enable_login_prompt : bool, optional
                Enable login prompt. Defaults to `False`.

            login_prompt_days : int, optional
                Days before login prompt. Defaults to `1`.

            allow_reset_after_expired : bool, optional
                Allow reset after password expiry. Defaults to `True`.

            enable_mail_notification : bool, optional
                Enable mail notification. Defaults to `False`.

            never_expired_list : list[str], optional
                List of users that should never expire.
            
            Returns
            -------
            dict[str, object]
                A dictionary indicating the success of the operation.

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User.PasswordExpiry",
                "method": "set",
                "success": true,
                "version": 1
            }
            ```
        """
        
        api_name = "SYNO.Core.User.PasswordExpiry"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": info["minVersion"],
            "password_expire_enable": password_expire_enable,
            "max_age": max_age,
            "min_age_enable": min_age_enable,
            "min_age": min_age,
            "enable_login_prompt": enable_login_prompt,
            "login_prompt_days": login_prompt_days,
            "allow_reset_after_expired": allow_reset_after_expired,
            "enable_mail_notification": enable_mail_notification,
            "never_expired_list": json.dumps(never_expired_list)
        }
        return self.request_data(api_name, api_path, req_param)
    
        
    def password_confirm(self, password: str) -> dict[str, object]:
        """Issues a passowrd/session comparison to ensure the given password matches the auth of the current session.

            Note: This is needed by some APIs as a confirmation method, for example, when creating/modifying a scheduled task with root permissions, seldom needed by end users.

            Parameters
            ----------
            password : str
                The password with which the session was initiated.

            Returns
            -------
            dict[str, object]
                A dictionary containing a `SynoConfirmPWToken`, or an error message.

            Example return
            --------------
            ```json
            {
                "data": {
                    "SynoConfirmPWToken": "xxxxx"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.User.PasswordConfirm'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'auth'}
        # Using https
        if self.session._secure:
            req_param.update({"password": password})
        # Using http and self encrypted
        else:
            req_param.update(self.session.encrypt_params({"password": password}))
            
        return self.request_data(api_name, api_path, req_param, method="post")
    
    
    def get_username_policy(self) -> dict[str, object]:
        """Get the username policy (List of username that are not usable).

            Returns
            -------
            dict[str, object]
                A dictionary containing the username policy information.

            Example return
            --------------
            ```json
            {
                "api": "SYNO.Core.User.UsernamePolicy",
                "data": ["root", "rootuser", "rootusr", "admin", "administrator", "adm", "adminuser", "adminusr", "user",…],
                "method": "get",
                "success": true,
                "version": 1
            }
            ```
        """
        api_name = "SYNO.Core.User.UsernamePolicy"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": info['minVersion']
        }
        return self.request_data(api_name, api_path, req_param)