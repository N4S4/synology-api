"""
Synology Document Viewer API wrapper.

This module provides a Python interface for document conversion and indexing
on Synology NAS devices.
"""

from __future__ import annotations

from . import base_api


class DocumentViewer(base_api.BaseApi):
    """
    Synology Document Viewer API implementation.

    Provides read-only access to document conversion status and index information.
    """

    def get_index_list(self) -> dict[str, object] | str:
        """
        Get the document viewer index list.

        Returns
        -------
        dict[str, object] or str
            Index list or error message.
        """
        api_name = 'SYNO.DocumentViewer.Index'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_convert_info(self) -> dict[str, object] | str:
        """
        Get the document conversion information.

        Returns
        -------
        dict[str, object] or str
            Conversion info or error message.
        """
        api_name = 'SYNO.DocumentViewer.Convert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_poll_status(self) -> dict[str, object] | str:
        """
        Get the document conversion poll status.

        Returns
        -------
        dict[str, object] or str
            Poll status or error message.
        """
        api_name = 'SYNO.DocumentViewer.Convert'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'poll_status'}

        return self.request_data(api_name, api_path, req_param)
