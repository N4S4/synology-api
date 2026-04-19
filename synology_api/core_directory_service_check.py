"""
Synology Core DirectoryServiceCheck API wrapper.

Provides a Python interface for directory service health checks
on Synology NAS devices, including domain join, LDAP, and
domain validation checks.
"""

from __future__ import annotations
from typing import Optional
from . import base_api
import json


class CoreDirectoryServiceCheck(base_api.BaseApi):
    """
    Core DirectoryServiceCheck API implementation for Synology NAS.

    Covers SYNO.Core.DirectoryServiceCheck.* endpoints.
    """

    # ================================================================== #
    #  SYNO.Core.DirectoryServiceCheck.*
    # ================================================================== #

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.Common
    # ------------------------------------------------------------------ #

    def directory_service_check_common_get(self) -> dict[str, object] | str:
        """
        Get common directory service check results.

        Returns
        -------
        dict[str, object] or str
            Common directory service check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Common'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_common_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger a common directory service check.

        Parameters
        ----------
        action : str, optional
            Check action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Common'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.Debug
    # ------------------------------------------------------------------ #

    def directory_service_check_debug_get(self) -> dict[str, object] | str:
        """
        Get directory service debug check results.

        Returns
        -------
        dict[str, object] or str
            Debug check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Debug'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_debug_set(
        self,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set directory service debug check mode.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable debug mode.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Debug'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.Domain
    # ------------------------------------------------------------------ #

    def directory_service_check_domain_get(self) -> dict[str, object] | str:
        """
        Get domain directory service check results.

        Returns
        -------
        dict[str, object] or str
            Domain service check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Domain'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_domain_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger a domain directory service check.

        Parameters
        ----------
        action : str, optional
            Check action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Domain'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.DomainJoin
    # ------------------------------------------------------------------ #

    def directory_service_check_domain_join_get(self) -> dict[str, object] | str:
        """
        Get domain join service check results.

        Returns
        -------
        dict[str, object] or str
            Domain join check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainJoin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_domain_join_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger a domain join service check.

        Parameters
        ----------
        action : str, optional
            Check action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainJoin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.DomainService
    # ------------------------------------------------------------------ #

    def directory_service_check_domain_service_get(self) -> dict[str, object] | str:
        """
        Get domain service directory check results.

        Returns
        -------
        dict[str, object] or str
            Domain service check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_domain_service_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger a domain service directory check.

        Parameters
        ----------
        action : str, optional
            Check action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainService'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.DomainValidation
    # ------------------------------------------------------------------ #

    def directory_service_check_domain_validation_get(self) -> dict[str, object] | str:
        """
        Get domain validation check results.

        Returns
        -------
        dict[str, object] or str
            Domain validation check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainValidation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_domain_validation_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger a domain validation check.

        Parameters
        ----------
        action : str, optional
            Validation action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.DomainValidation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.LDAP
    # ------------------------------------------------------------------ #

    def directory_service_check_ldap_get(self) -> dict[str, object] | str:
        """
        Get LDAP directory service check results.

        Returns
        -------
        dict[str, object] or str
            LDAP service check results.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.LDAP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_ldap_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Trigger an LDAP directory service check.

        Parameters
        ----------
        action : str, optional
            Check action to perform.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.LDAP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.DirectoryServiceCheck.Progress
    # ------------------------------------------------------------------ #

    def directory_service_check_progress_get(self) -> dict[str, object] | str:
        """
        Get directory service check progress.

        Returns
        -------
        dict[str, object] or str
            Directory service check progress.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Progress'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def directory_service_check_progress_set(
        self,
        action: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set directory service check progress action.

        Parameters
        ----------
        action : str, optional
            Progress action (e.g., 'start', 'stop').

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.DirectoryServiceCheck.Progress'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if action is not None:
            req_param['action'] = action

        return self.request_data(api_name, api_path, req_param)
