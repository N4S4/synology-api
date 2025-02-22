from synology_api import base_api
import json

class ApplicationPrivileges(base_api.BaseApi):
    
    def list_all(self, offset: int = 0, limit: int = 20) -> dict:
        """List applications privileges.
        
            Parameters
            ----------
            offset : int, optional
                Offset in the application list. Defaults to `0`
            limit : int, optional
                Limit the len of the returned list. Defaults to `20`
        
            Returns
            -------
            dict
                List of applications privileges.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "applications": [
                        {
                            "app_id": "SYNO.AFP",
                            "grant_by_default": true,
                            "grant_type": [
                                "local",
                                "domain",
                                "ldap"
                            ],
                            "isInternal": true,
                            "name": "AFP",
                            "service_type": "modules/LegacyApps",
                            "supportIP": true
                        },
                        {
                            "app_id": "SYNO.Desktop",
                            "grant_by_default": true,
                            "grant_type": [
                                "local",
                                "domain",
                                "ldap"
                            ],
                            "isInternal": true,
                            "name": "DSM",
                            "service_type": "modules/LegacyApps",
                            "supportIP": true
                        }
                    ],
                    "offset": 0,
                    "total": 2
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.AppPriv.App'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'offset': offset,
            'limit': limit
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_entities(self, app_id: str, type: str = "local", filter_type: str = "all", rule_type: str = "user", offset: int = 0, limit: int = 50) -> dict:
        """List entities of the specify app_id.
        
            Parameters
            ----------
            app_id : str
                Application ID
            type : str, optional
                Type to filter for rule_type. Defaults to `"local"`
                Example: for rule_type = "user", type = "local"
                All known values are: `["local"]`
            filter_type : str, optional
                Filter actual rules. Defaults to `"all"`
                All known values are: `["all", "allow", "deny", "any", "custom"]`
            rule_type : str, optional
                Type of the rule. Defaults to `"user"`
                All known values are: `["user", "group"]`
            offset : int, optional
                Offset in entity list. Defaults to `0`
            limit : int, optional
                Limit the len of the returned list. Defaults to `50`
        
            Returns
            -------
            dict
                Return list of entity available
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "offset": 0,
                    "total": 3,
                    "users": [
                        {
                            "name": "admin"
                        },
                        {
                            "name": "guest"
                        },
                        {
                            "name": "test_api"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.AppPriv'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'action': 'list',
            'offset': offset,
            'limit': limit,
            'type': type,
            'app_id': app_id,
            'filter_type': filter_type,
            'rule_type': rule_type
        }
        
        return self.request_data(api_name, api_path, req_param)
        
    def list_app_rules(self, app_id: str) -> dict:
        """Retrieve application rules.
        
            Parameters
            ----------
            app_id : str
                Application ID
        
            Returns
            -------
            dict
                List of rules
        
            Example return
            ----------
            ```json
            "data": {
                    "rules": [
                        {
                            "allow_ip": [
                                "0.0.0.0"
                            ],
                            "app_id": "SYNO.AFP",
                            "deny_ip": [],
                            "entity_name": "everyone",
                            "entity_type": "everyone"
                        },
                        {
                            "allow_ip": [
                                "0.0.0.0"
                            ],
                            "app_id": "SYNO.AFP",
                            "deny_ip": [],
                            "entity_name": "test_api",
                            "entity_type": "user"
                        },
                        {
                            "allow_ip": [
                                "0.0.0.0"
                            ],
                            "app_id": "SYNO.AFP",
                            "deny_ip": [],
                            "entity_name": "test_group",
                            "entity_type": "group"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'app_id': app_id
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def set_app_rules(self, app_id: str, rules: list) -> dict:
        """Set application rules.
        
            Parameters
            ----------
            app_id : str
                Application ID
            rules : list
                List of rules, a rule is a dict with the following keys:
                ```json
                {
                    "entity_type":"user",
                    "entity_name":"test_api",
                    "app_id":"SYNO.AFP",
                    "allow_ip":["0.0.0.0"],
                    "deny_ip":[]
                }
                ```

            Returns
            -------
            dict
                Success
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'app_id': app_id,
            'rules': json.dumps(rules)
        }
        
        return self.request_data(api_name, api_path, req_param)
        
    def delete_app_rules(self, app_id: str, rules: list) -> dict:
        """Delete application rules.
        
            Parameters
            ----------
            app_id : str
                Application ID
            rules : list
                List of rules, a rule is a dict with the following keys:
                ```json
                {
                    "entity_type":"user",
                    "entity_name":"test_api",
                    "app_id":"SYNO.AFP",
                    "allow_ip":["0.0.0.0"],
                    "deny_ip":[]
                }
                ```

            Returns
            -------
            dict
                Success
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.Core.AppPriv.Rule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'app_id': app_id,
            'rules': json.dumps(rules)
        }
        
        return self.request_data(api_name, api_path, req_param)
        
        
        