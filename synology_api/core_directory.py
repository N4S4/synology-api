"""
Synology Core Directory API wrapper.

This module provides a Python interface for managing directory services
on Synology NAS devices, including Azure SSO, domain configuration, LDAP,
OIDC, SAML, SSO settings, and directory service health checks.
"""

from __future__ import annotations
from typing import Optional
from . import base_api
import json


class CoreDirectory(base_api.BaseApi):
    """
    Core Directory and DirectoryServiceCheck API implementation for Synology NAS.

    Covers SYNO.Core.Directory.* and SYNO.Core.DirectoryServiceCheck.* endpoints
    not already present in core_sys_info.py.
    """

    # ================================================================== #
    #  SYNO.Core.Directory.*
    # ================================================================== #

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.Azure.SSO
    # ------------------------------------------------------------------ #

    def directory_azure_sso_get(self) -> dict[str, object] | str:
        """
        Get Azure SSO directory configuration.

        Returns
        -------
        dict[str, object] or str
            Azure SSO configuration.
        """
        api_name = 'SYNO.Core.Directory.Azure.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_azure_sso_set(
        self,
        enable: Optional[bool] = None,
        tenant_id: Optional[str] = None,
        client_id: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set Azure SSO directory configuration.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable Azure SSO.
        tenant_id : str, optional
            Azure AD tenant ID.
        client_id : str, optional
            Azure AD client/application ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.Azure.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()
        if tenant_id is not None:
            req_param['tenant_id'] = tenant_id
        if client_id is not None:
            req_param['client_id'] = client_id

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.Domain.Conf
    # ------------------------------------------------------------------ #

    def directory_domain_conf_get(self) -> dict[str, object] | str:
        """
        Get domain directory configuration.

        Returns
        -------
        dict[str, object] or str
            Domain configuration.
        """
        api_name = 'SYNO.Core.Directory.Domain.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_domain_conf_set(
        self,
        conf: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set domain directory configuration.

        Parameters
        ----------
        conf : str, optional
            JSON-encoded domain configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.Domain.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if conf is not None:
            req_param['conf'] = conf

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.Domain.Trust
    # ------------------------------------------------------------------ #

    def directory_domain_trust_get(self) -> dict[str, object] | str:
        """
        Get domain trust relationship information.

        Returns
        -------
        dict[str, object] or str
            Domain trust relationships.
        """
        api_name = 'SYNO.Core.Directory.Domain.Trust'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_domain_trust_set(
        self,
        trust: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set domain trust relationship configuration.

        Parameters
        ----------
        trust : str, optional
            JSON-encoded domain trust configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.Domain.Trust'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if trust is not None:
            req_param['trust'] = trust

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.LDAP.BaseDN
    # ------------------------------------------------------------------ #

    def directory_ldap_base_dn_get(self) -> dict[str, object] | str:
        """
        Get LDAP base DN configuration.

        Returns
        -------
        dict[str, object] or str
            LDAP base DN configuration.
        """
        api_name = 'SYNO.Core.Directory.LDAP.BaseDN'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_ldap_base_dn_set(
        self,
        base_dn: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set LDAP base DN configuration.

        Parameters
        ----------
        base_dn : str, optional
            LDAP base distinguished name.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.LDAP.BaseDN'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if base_dn is not None:
            req_param['base_dn'] = base_dn

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.LDAP.Login.Notify
    # ------------------------------------------------------------------ #

    def directory_ldap_login_notify_get(self) -> dict[str, object] | str:
        """
        Get LDAP login notification settings.

        Returns
        -------
        dict[str, object] or str
            LDAP login notification settings.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Login.Notify'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_ldap_login_notify_set(
        self,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set LDAP login notification settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable LDAP login notifications.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Login.Notify'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.LDAP.Profile
    # ------------------------------------------------------------------ #

    def directory_ldap_profile_get(self) -> dict[str, object] | str:
        """
        Get LDAP profile configuration.

        Returns
        -------
        dict[str, object] or str
            LDAP profile configuration.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_ldap_profile_set(
        self,
        profile: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set LDAP profile configuration.

        Parameters
        ----------
        profile : str, optional
            JSON-encoded LDAP profile configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if profile is not None:
            req_param['profile'] = profile

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.LDAP.Refresh
    # ------------------------------------------------------------------ #

    def directory_ldap_refresh_get(self) -> dict[str, object] | str:
        """
        Get LDAP refresh status.

        Returns
        -------
        dict[str, object] or str
            LDAP refresh status.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Refresh'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_ldap_refresh_set(self) -> dict[str, object] | str:
        """
        Trigger an LDAP refresh.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.LDAP.Refresh'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.LDAP.User
    # ------------------------------------------------------------------ #

    def directory_ldap_user_get(self) -> dict[str, object] | str:
        """
        Get LDAP user configuration.

        Returns
        -------
        dict[str, object] or str
            LDAP user configuration.
        """
        api_name = 'SYNO.Core.Directory.LDAP.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_ldap_user_set(
        self,
        user: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set LDAP user configuration.

        Parameters
        ----------
        user : str, optional
            JSON-encoded LDAP user configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.LDAP.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if user is not None:
            req_param['user'] = user

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.OIDC.SSO
    # ------------------------------------------------------------------ #

    def directory_oidc_sso_get(self) -> dict[str, object] | str:
        """
        Get OIDC SSO directory configuration.

        Returns
        -------
        dict[str, object] or str
            OIDC SSO configuration.
        """
        api_name = 'SYNO.Core.Directory.OIDC.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_oidc_sso_set(
        self,
        enable: Optional[bool] = None,
        issuer: Optional[str] = None,
        client_id: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set OIDC SSO directory configuration.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable OIDC SSO.
        issuer : str, optional
            OIDC issuer URL.
        client_id : str, optional
            OIDC client ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.OIDC.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()
        if issuer is not None:
            req_param['issuer'] = issuer
        if client_id is not None:
            req_param['client_id'] = client_id

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.CAS
    # ------------------------------------------------------------------ #

    def directory_sso_cas_get(self) -> dict[str, object] | str:
        """
        Get SSO CAS configuration.

        Returns
        -------
        dict[str, object] or str
            SSO CAS configuration.
        """
        api_name = 'SYNO.Core.Directory.SSO.CAS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_cas_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO CAS configuration.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded SSO CAS settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.CAS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.Profile
    # ------------------------------------------------------------------ #

    def directory_sso_profile_get(self) -> dict[str, object] | str:
        """
        Get SSO profile configuration.

        Returns
        -------
        dict[str, object] or str
            SSO profile configuration.
        """
        api_name = 'SYNO.Core.Directory.SSO.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_profile_set(
        self,
        profile: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO profile configuration.

        Parameters
        ----------
        profile : str, optional
            JSON-encoded SSO profile configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if profile is not None:
            req_param['profile'] = profile

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.SAML
    # ------------------------------------------------------------------ #

    def directory_sso_saml_get(self) -> dict[str, object] | str:
        """
        Get SSO SAML configuration.

        Returns
        -------
        dict[str, object] or str
            SSO SAML configuration.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_saml_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO SAML configuration.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded SSO SAML settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.SAML.Metadata
    # ------------------------------------------------------------------ #

    def directory_sso_saml_metadata_get(self) -> dict[str, object] | str:
        """
        Get SSO SAML metadata.

        Returns
        -------
        dict[str, object] or str
            SSO SAML metadata.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML.Metadata'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_saml_metadata_set(
        self,
        metadata: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO SAML metadata.

        Parameters
        ----------
        metadata : str, optional
            SAML metadata XML or JSON-encoded configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML.Metadata'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if metadata is not None:
            req_param['metadata'] = metadata

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.SAML.Status
    # ------------------------------------------------------------------ #

    def directory_sso_saml_status_get(self) -> dict[str, object] | str:
        """
        Get SSO SAML status.

        Returns
        -------
        dict[str, object] or str
            SSO SAML status.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_saml_status_set(
        self,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set SSO SAML status.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable SSO SAML.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.SAML.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.Setting
    # ------------------------------------------------------------------ #

    def directory_sso_setting_get(self) -> dict[str, object] | str:
        """
        Get SSO general settings.

        Returns
        -------
        dict[str, object] or str
            SSO general settings.
        """
        api_name = 'SYNO.Core.Directory.SSO.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_setting_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO general settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded SSO general settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.Status
    # ------------------------------------------------------------------ #

    def directory_sso_status_get(self) -> dict[str, object] | str:
        """
        Get SSO status.

        Returns
        -------
        dict[str, object] or str
            SSO status.
        """
        api_name = 'SYNO.Core.Directory.SSO.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_status_set(
        self,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set SSO status.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable SSO.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.Status'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.SSO.utils
    # ------------------------------------------------------------------ #

    def directory_sso_utils_get(self) -> dict[str, object] | str:
        """
        Get SSO utility information.

        Returns
        -------
        dict[str, object] or str
            SSO utility information.
        """
        api_name = 'SYNO.Core.Directory.SSO.utils'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_sso_utils_set(
        self,
        data: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SSO utility configuration.

        Parameters
        ----------
        data : str, optional
            JSON-encoded SSO utility data.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.SSO.utils'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if data is not None:
            req_param['data'] = data

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Directory.WebSphere.SSO
    # ------------------------------------------------------------------ #

    def directory_websphere_sso_get(self) -> dict[str, object] | str:
        """
        Get WebSphere SSO directory configuration.

        Returns
        -------
        dict[str, object] or str
            WebSphere SSO configuration.
        """
        api_name = 'SYNO.Core.Directory.WebSphere.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_websphere_sso_set(
        self,
        enable: Optional[bool] = None,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set WebSphere SSO directory configuration.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable WebSphere SSO.
        settings : str, optional
            JSON-encoded WebSphere SSO settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Directory.WebSphere.SSO'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)
