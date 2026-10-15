"""
Synology Contacts API wrapper.

This module provides a Python interface for accessing contacts, address books, labels,
and organizational units on Synology NAS devices.
"""

from __future__ import annotations

import json
from typing import Optional

from . import base_api


class Contacts(base_api.BaseApi):
    """
    Synology Contacts API implementation.

    Provides read-only access to address books, contacts, labels, external sources,
    and organizational units.
    """

    def get_addressbook_list(self) -> dict[str, object] | str:
        """
        Get the list of address books.

        Returns
        -------
        dict[str, object] or str
            Address book list or error message.
        """
        api_name = 'SYNO.Contacts.Addressbook'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_contact_list(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> dict[str, object] | str:
        """
        Get the list of contacts.

        Parameters
        ----------
        limit : int, optional
            Maximum number of contacts to return.
        offset : int, optional
            Starting index for pagination.

        Returns
        -------
        dict[str, object] or str
            Contact list or error message.
        """
        api_name = 'SYNO.Contacts.Contact'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        if limit is not None:
            req_param['limit'] = limit
        if offset is not None:
            req_param['offset'] = offset

        return self.request_data(api_name, api_path, req_param)

    def get_contact(self, contact_id: str) -> dict[str, object] | str:
        """
        Get a single contact by ID.

        Parameters
        ----------
        contact_id : str
            Contact ID.

        Returns
        -------
        dict[str, object] or str
            Contact details or error message.
        """
        api_name = 'SYNO.Contacts.Contact'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'contact_id': contact_id}

        return self.request_data(api_name, api_path, req_param)

    def get_label_list(self) -> dict[str, object] | str:
        """
        Get the list of labels.

        Returns
        -------
        dict[str, object] or str
            Label list or error message.
        """
        api_name = 'SYNO.Contacts.Label'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_info(self) -> dict[str, object] | str:
        """
        Get the current user information.

        Returns
        -------
        dict[str, object] or str
            User info or error message.
        """
        api_name = 'SYNO.Contacts.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_ou_list(self) -> dict[str, object] | str:
        """
        Get the list of organizational units.

        Returns
        -------
        dict[str, object] or str
            Organizational unit list or error message.
        """
        api_name = 'SYNO.Contacts.OU'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_external_source_list(self) -> dict[str, object] | str:
        """
        Get the list of external contact sources.

        Returns
        -------
        dict[str, object] or str
            External source list or error message.
        """
        api_name = 'SYNO.Contacts.ExternalSource'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def create_contact(
        self,
        full_name: str,
        addressbook_id: Optional[int] = None,
        **kwargs
    ) -> dict[str, object] | str:
        """
        Create a new contact.

        Parameters
        ----------
        full_name : str
            Contact full name.
        addressbook_id : int, optional
            Target address book ID.
        **kwargs : dict[str, object]
            Additional contact fields (email, phone, company, etc.).

        Returns
        -------
        dict[str, object] or str
            Created contact or error message.
        """
        api_name = 'SYNO.Contacts.Contact'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'create', 'full_name': full_name}

        if addressbook_id is not None:
            req_param['addressbook_id'] = addressbook_id
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    def delete_contact(self, contact_id: int) -> dict[str, object] | str:
        """
        Delete a contact by ID.

        Parameters
        ----------
        contact_id : int
            Contact ID.

        Returns
        -------
        dict[str, object] or str
            Result or error message.
        """
        api_name = 'SYNO.Contacts.Contact'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'delete', 'ids': json.dumps([contact_id])}

        return self.request_data(api_name, api_path, req_param)

    def set_contact(
        self,
        contact_id: int,
        **kwargs
    ) -> dict[str, object] | str:
        """
        Update an existing contact.

        Parameters
        ----------
        contact_id : int
            Contact ID.
        **kwargs : dict[str, object]
            Contact fields to update.

        Returns
        -------
        dict[str, object] or str
            Updated contact or error message.
        """
        api_name = 'SYNO.Contacts.Contact'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'set', 'id': contact_id}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

