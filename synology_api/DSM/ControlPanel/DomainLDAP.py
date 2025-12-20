"""
Manage Domain and LDAP settings.
"""

from synology_api import base_api


class DomainLDAP(base_api.BaseApi):
    """
    Manage Domain and LDAP settings.
    """

    def get_ldap_info(self) -> dict:
        """
        Get LDAP information.

        Returns
        -------
        dict
            Informations about LDAP settings.

        Examples
        --------
        ```json
        {
            "data": {
                "base_dn": "dc=test_api,dc=dev",
                "enable_cifs": false,
                "enable_cifs_pam": false,
                "enable_client": false,
                "enable_client_certificate": false,
                "enable_idmap": false,
                "encryption": "no",
                "error": 2703,
                "expand_nested_groups": true,
                "is_syno_server": false,
                "ldap_schema": "rfc2307bis",
                "nested_group_level": 5,
                "profile": "standard",
                "server_address": "127.0.0.1",
                "tls_reqcert": false,
                "update_min": 60
            },
            "success": true,
        ```
        """

        api_name = 'SYNO.Core.Directory.LDAP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_domain_info(self) -> dict:
        """
        Get domain info.

        Returns
        -------
        dict
            Informations about domain settings.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_domain": false
            },
            "success": true,
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.Domain'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_sso_login_settings(self) -> dict:
        """
        Get SSO login settings.

        Returns
        -------
        dict
            Informations about SSO login settings.

        Examples
        --------
        ```json
        {
            "data": {
                "sso_default_login": false
            },
            "success": true,
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.SSO.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_synology_sso_settings(self) -> dict:
        """
        Get Synology SSO service settings.

        Returns
        -------
        dict
            Informations about Synology SSO service settings.

        Examples
        --------
        ```json
        {
            "data": {
                "allow_local_user": true,
                "appid": "",
                "enable_sso": false,
                "host": "",
                "name": "Synology SSO",
                "pingpong": null,
                "sso_default_login": false
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_sso_profile(self) -> dict:
        """
        Get SSO profile.

        Returns
        -------
        dict
            Informations about SSO profile.

        Examples
        --------
        ```json
        {
            "data": {
                "sso_enable": false,
                "sso_profile": ""
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.SSO.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_sam_sso_settings(self) -> dict:
        """
        Get SAM SSO settings.

        Returns
        -------
        dict
            Informations about SAM SSO settings.

        Examples
        --------
        ```json
        {
            "data": {
                "saml_allow_local_user": false,
                "saml_cert_detail": "",
                "saml_idp_entity_id": "",
                "saml_idp_signin_url": "",
                "saml_name": "SAML",
                "saml_response_signature": "response",
                "saml_system_date": "",
                "saml_valid_date": "",
                "sso_saml_enable": ""
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.SSO.SAM'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)

    def get_cas_sso_settings(self) -> dict:
        """
        Get CAS SSO settings.

        Returns
        -------
        dict
            Informations about CAS SSO settings.

        Examples
        --------
        ```json
        {
            "data": {
                "cas_allow_local_user": true,
                "cas_auth_url": "",
                "cas_name": "CAS",
                "cas_service_ids": "",
                "cas_validate_url": "",
                "sso_cas_enable": ""
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Directory.SSO.CAS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }

        return self.request_data(api_name, api_path, req_param)
