"""
Security Advisor API wrapper for Synology DSM.

This module provides a class to interact with the Synology Security Advisor API.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class SecurityAdvisor(base_api.BaseApi):
    """
    Interface for Synology Security Advisor API.

    Provides methods to retrieve general info, scan results, checklists,
    login activity, and configuration for Security Advisor.
    """

    def general_info(self) -> dict[str, object] | str:
        """
        Retrieve general information about Security Advisor location configuration.

        Returns
        -------
        dict[str, object] or str
            The API response containing location configuration or an error message.
        """
        api_name = 'SYNO.SecurityAdvisor.Conf.Location'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_scan(self) -> dict[str, object] | str:
        """
        Retrieve the current security scan configuration.

        Returns
        -------
        dict[str, object] or str
            The API response containing security scan configuration or an error message.
        """
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def checklist(self) -> dict[str, object] | str:
        """
        Retrieve the checklist for the Security Advisor.

        Returns
        -------
        dict[str, object] or str
            The API response containing the checklist or an error message.
        """
        api_name = 'SYNO.SecurityAdvisor.Conf.Checklist'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'group': 'home'}

        return self.request_data(api_name, api_path, req_param)

    def login_activity(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        """
        Retrieve login activity records.

        Parameters
        ----------
        offset : int, optional
            The starting index of the login activity list. Default is 0.
        limit : int, optional
            The maximum number of records to retrieve. Default is 20.

        Returns
        -------
        dict[str, object] or str
            The API response containing login activity records or an error message.
        """
        api_name = 'SYNO.SecurityAdvisor.LoginActivity'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'offser': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def advisor_config(self) -> dict[str, object] | str:
        """
        Retrieve Security Advisor configuration.

        Returns
        -------
        dict[str, object] or str
            The API response containing advisor configuration or an error message.
        """
        api_name = 'SYNO.SecurityAdvisor.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def scan_config(self) -> dict[str, object] | str:
        """
        Retrieve custom group enumeration for security scan configuration.

        Returns
        -------
        dict[str, object] or str
            The API response containing custom group enumeration or an error message.
        """
        api_name = 'SYNO.Core.SecurityScan.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'group_enum', 'argGroup': 'custom'}

        return self.request_data(api_name, api_path, req_param)

    def advisor_alert_set(self) -> dict:
        """
        Set or update the configuration.

        Returns
        -------
        dict
            API response from ``SYNO.SecurityAdvisor.Conf.Checklist.Alert``.
        """
        api_name = "SYNO.SecurityAdvisor.Conf.Checklist.Alert"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def advisor_login_get(self) -> dict:
        """
        Get user login activity log from Security Advisor.

        Returns
        -------
        dict
            API response from ``SYNO.SecurityAdvisor.LoginActivity.User``.
        """
        api_name = "SYNO.SecurityAdvisor.LoginActivity.User"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def advisor_report_create(self) -> dict:
        """
        Create a new user group.

        Returns
        -------
        dict
            API response from ``SYNO.SecurityAdvisor.Report``.
        """
        api_name = "SYNO.SecurityAdvisor.Report"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def advisor_report_list(self) -> dict:
        """
        List snapshot usage entries.

        Returns
        -------
        dict
            API response from ``SYNO.SecurityAdvisor.Report``.
        """
        api_name = "SYNO.SecurityAdvisor.Report"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def advisor_report_html_open(self) -> dict:
        """
        Open a snapshot usage tracking session.

        Returns
        -------
        dict
            API response from ``SYNO.SecurityAdvisor.Report.HTML``.
        """
        api_name = "SYNO.SecurityAdvisor.Report.HTML"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "open",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)
