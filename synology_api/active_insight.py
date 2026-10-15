"""
Synology Active Insight API wrapper.

This module provides a Python interface for retrieving system health, monitoring and
license information from Synology Active Insight on NAS devices.
"""

from __future__ import annotations

from . import base_api


class ActiveInsight(base_api.BaseApi):
    """
    Synology Active Insight API implementation.

    Provides read-only access to license, package status, settings, and data
    collection configuration.
    """

    def get_license(self) -> dict[str, object] | str:
        """
        Get the Active Insight license information.

        Returns
        -------
        dict[str, object] or str
            License info or error message.
        """
        api_name = 'SYNO.ActiveInsight.License'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_package_status(self) -> dict[str, object] | str:
        """
        Get the Active Insight package status.

        Returns
        -------
        dict[str, object] or str
            Package status or error message.
        """
        api_name = 'SYNO.ActiveInsight.Package'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_status'}

        return self.request_data(api_name, api_path, req_param)

    def get_relation_manager(self) -> dict[str, object] | str:
        """
        Get the Active Insight relation manager configuration.

        Returns
        -------
        dict[str, object] or str
            Relation manager config or error message.
        """
        api_name = 'SYNO.ActiveInsight.RelationManager'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_setting(self) -> dict[str, object] | str:
        """
        Get the Active Insight settings.

        Returns
        -------
        dict[str, object] or str
            Settings or error message.
        """
        api_name = 'SYNO.ActiveInsight.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)
