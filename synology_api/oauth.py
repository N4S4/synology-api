"""
OAuth API wrapper for Synology DSM.

This module provides a class to interact with the Synology OAuth API.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class OAuth(base_api.BaseApi):
    """
    Interface for Synology OAuth API.

    Provides methods to interact with OAuth clients, tokens, and logs.
    """

    def clients(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        """
        Retrieve the list of OAuth clients.

        Parameters
        ----------
        offset : int, optional
            The starting index of the client list. Default is 0.
        limit : int, optional
            The maximum number of clients to retrieve. Default is 20.

        Returns
        -------
        dict[str, object] or str
            The API response containing the list of clients or an error message.
        """
        api_name = 'SYNO.OAUTH.Client'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def tokens(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        """
        Retrieve the list of OAuth tokens.

        Parameters
        ----------
        offset : int, optional
            The starting index of the token list. Default is 0.
        limit : int, optional
            The maximum number of tokens to retrieve. Default is 20.

        Returns
        -------
        dict[str, object] or str
            The API response containing the list of tokens or an error message.
        """
        api_name = 'SYNO.OAUTH.Token'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset: int = 0, limit: int = 20) -> dict[str, object] | str:
        """
        Retrieve the list of OAuth logs.

        Parameters
        ----------
        offset : int, optional
            The starting index of the log list. Default is 0.
        limit : int, optional
            The maximum number of logs to retrieve. Default is 20.

        Returns
        -------
        dict[str, object] or str
            The API response containing the list of logs or an error message.
        """
        api_name = 'SYNO.OAUTH.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'action': 'list',
                     'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)
