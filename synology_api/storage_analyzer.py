"""
Synology Storage Analyzer API wrapper.

This module provides a Python interface for retrieving storage usage reports and
analysis data on Synology NAS devices.
"""

from __future__ import annotations

from typing import Optional

from . import base_api


class StorageAnalyzer(base_api.BaseApi):
    """
    Synology Storage Analyzer API implementation.

    Provides read-only access to storage usage reports, report configuration, and
    analysis data.
    """

    def get_report_list(self) -> dict[str, object] | str:
        """
        Get the list of storage analysis reports.

        Returns
        -------
        dict[str, object] or str
            Report list or error message.
        """
        api_name = 'SYNO.Core.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_report(self, report_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Get a single storage analysis report.

        Parameters
        ----------
        report_id : str, optional
            Report ID (from get_report_list).

        Returns
        -------
        dict[str, object] or str
            Report details or error message.
        """
        api_name = 'SYNO.Core.Report'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        if report_id is not None:
            req_param['report_id'] = report_id

        return self.request_data(api_name, api_path, req_param)

    def get_config(self) -> dict[str, object] | str:
        """
        Get the storage analysis configuration.

        Returns
        -------
        dict[str, object] or str
            Configuration or error message.
        """
        api_name = 'SYNO.Core.Report.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_history(self) -> dict[str, object] | str:
        """
        Get the storage analysis history.

        Returns
        -------
        dict[str, object] or str
            History or error message.
        """
        api_name = 'SYNO.Core.Report.History'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_share_list(self) -> dict[str, object] | str:
        """
        Get the list of shares for storage analysis.

        Returns
        -------
        dict[str, object] or str
            Share list or error message.
        """
        api_name = 'SYNO.Core.Report.Util'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_share'}

        return self.request_data(api_name, api_path, req_param)

    def get_analyzer_data(self) -> dict[str, object] | str:
        """
        Get the storage analyzer data.

        Returns
        -------
        dict[str, object] or str
            Analyzer data or error message.
        """
        api_name = 'SYNO.Core.Report.Analyzer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getdata'}

        return self.request_data(api_name, api_path, req_param)
