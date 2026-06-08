"""
Photos API wrapper for Synology DSM.

This module provides a class to interact with the Synology Photos API.
"""

from __future__ import annotations
from typing import Optional, Any
from . import base_api
import json


class Photos(base_api.BaseApi):
    """
    Interface for Synology Photos API.

    Provides methods to interact with Photos features such as retrieving user info,
    folders, albums, sharing, and items.

    Parameters
    ----------
    ip_address : str
        The IP address or hostname of the Synology NAS.
    port : str
        The port number to connect to.
    username : str
        The username for authentication.
    password : str
        The password for authentication.
    secure : bool, optional
        Whether to use HTTPS. Default is False.
    cert_verify : bool, optional
        Whether to verify SSL certificates. Default is False.
    dsm_version : int, optional
        DSM version. Default is 7.
    debug : bool, optional
        Enable debug output. Default is True.
    otp_code : str, optional
        One-time password for 2FA, if required.
    device_id : str, optional
        Device ID for the session.
    device_name : str, optional
        Device name for the session.
    quickconnect_id : str, optional
        QuickConnect ID for relay-based access. Defaults to None.
    """

    def __init__(self,
                 ip_address: Optional[str] = None,
                 port: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 device_id: Optional[str] = None,
                 device_name: Optional[str] = None,
                 quickconnect_id: Optional[str] = None
                 ) -> None:
        """
        Initialize the Photos API interface.

        Parameters
        ----------
        ip_address : str
            The IP address or hostname of the Synology NAS.
        port : str
            The port number to connect to.
        username : str
            The username for authentication.
        password : str
            The password for authentication.
        secure : bool, optional
            Whether to use HTTPS. Default is False.
        cert_verify : bool, optional
            Whether to verify SSL certificates. Default is False.
        dsm_version : int, optional
            DSM version. Default is 7.
        debug : bool, optional
            Enable debug output. Default is True.
        otp_code : str, optional
            One-time password for 2FA, if required.
        device_id : str, optional
            Device ID for the session.
        device_name : str, optional
            Device name for the session.
        quickconnect_id : str, optional
            QuickConnect ID for relay-based access. When provided, `ip_address`
            and `port` are not required.
        """

        super(Photos, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                     dsm_version, debug, otp_code, device_id, device_name, 'FotoStation',
                                     quickconnect_id=quickconnect_id)

        self.session.get_api_list('Foto')

        self.request_data: Any = self.session.request_data
        self.photos_list: Any = self.session.app_api_list
        self.base_url: str = self.session.base_url

        self._userinfo: Any = None

    def get_userinfo(self) -> Any:
        """
        Retrieve user information for the current session.

        Returns
        -------
        Any
            The user information data.
        """
        if self._userinfo is not None:
            return self._userinfo

        api_name = 'SYNO.Foto.UserInfo'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'me'}
        self._userinfo = self.request_data(api_name, api_path, req_param)

        return self._userinfo

    def get_folder(self, folder_id: int = 0) -> dict[str, object] | str:
        """
        Retrieve information about a specific folder.

        Parameters
        ----------
        folder_id : int, optional
            The ID of the folder. Default is 0.

        Returns
        -------
        dict[str, object] or str
            The folder information or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Folder'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'id': folder_id}

        return self.request_data(api_name, api_path, req_param)

    def list_folders(self,
                     folder_id: int = 0,
                     limit: int = 1000,
                     offset: int = 0,
                     additional: str | list[str] = None
                     ) -> dict[str, object] | str:
        """
        List folders in Personal Space.

        Parameters
        ----------
        folder_id : int, optional
            The parent folder ID. Default is 0.
        limit : int, optional
            Maximum number of folders to return. Default is 1000.
        offset : int, optional
            Number of folders to skip. Default is 0.
        additional : str or list of str, optional
            Additional fields to include.

        Returns
        -------
        dict[str, object] or str
            The list of folders or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Folder'
        return self._list_folders(folder_id, limit, offset, additional, api_name)

    def list_teams_folders(self,
                           folder_id: int = 0,
                           limit: int = 2000,
                           offset: int = 0,
                           additional: Optional[str | list[str]] = None
                           ) -> dict[str, object] | str:
        """
        List folders in Team Space.

        Parameters
        ----------
        folder_id : int, optional
            The parent folder ID. Default is 0.
        limit : int, optional
            Maximum number of folders to return. Default is 2000.
        offset : int, optional
            Number of folders to skip. Default is 0.
        additional : str or list of str, optional
            Additional fields to include.

        Returns
        -------
        dict[str, object] or str
            The list of team folders or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Folder'
        return self._list_folders(folder_id, limit, offset, additional, api_name)

    def _list_folders(self, folder_id: int, limit: int, offset: int, additional: Optional[str | list[str]],
                      api_name: str) -> Any:
        """
        Internal method to list folders.

        Parameters
        ----------
        folder_id : int
            The parent folder ID.
        limit : int
            Maximum number of folders to return.
        offset : int
            Number of folders to skip.
        additional : str or list of str, optional
            Additional fields to include.
        api_name : str
            API name to use.

        Returns
        -------
        Any
            The API response.
        """
        if additional is None:
            additional = []
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'id': folder_id, 'limit': limit, 'offset': offset,
                     'additional': json.dumps(additional)}

        return self.request_data(api_name, api_path, req_param)

    def count_folders(self, folder_id: int = 0) -> dict[str, object] | str:
        """
        Count folders in Personal Space.

        Parameters
        ----------
        folder_id : int, optional
            The parent folder ID. Default is 0.

        Returns
        -------
        dict[str, object] or str
            The count of folders or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Folder'
        return self._count_folders(folder_id, api_name)

    def count_team_folders(self, folder_id: int = 0) -> dict[str, object] | str:
        """
        Count folders in Team Space.

        Parameters
        ----------
        folder_id : int, optional
            The parent folder ID. Default is 0.

        Returns
        -------
        dict[str, object] or str
            The count of team folders or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Folder'
        return self._count_folders(folder_id, api_name)

    def _count_folders(self, folder_id: int, api_name: str) -> Any:
        """
        Internal method to count folders.

        Parameters
        ----------
        folder_id : int
            The parent folder ID.
        api_name : str
            API name to use.

        Returns
        -------
        Any
            The API response.
        """
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'count', 'id': folder_id}

        return self.request_data(api_name, api_path, req_param)

    def lookup_folder(self, path: str) -> dict[str, object] | str:
        """
        Lookup a folder by path in Personal Space.

        Parameters
        ----------
        path : str
            The folder path.

        Returns
        -------
        dict[str, object] or str
            The folder information or None if not found.
        """
        return self._lookup_folder(path, 'SYNO.Foto.Browse.Folder', 'SYNO.Foto.Browse.Folder')

    def lookup_team_folder(self, path: str) -> dict[str, object] | str:
        """
        Lookup a folder by path in Team Space.

        Parameters
        ----------
        path : str
            The folder path.

        Returns
        -------
        dict[str, object] or str
            The folder information or None if not found.
        """
        return self._lookup_folder(path, 'SYNO.FotoTeam.Browse.Folder', 'SYNO.FotoTeam.Browse.Folder')

    def _lookup_folder(self, path: str, api_name_count: str, api_name_list: str) -> Optional[dict[str, object]]:
        """
        Internal method to lookup a folder by path.

        Parameters
        ----------
        path : str
            The folder path.
        api_name_count : str
            API name for counting folders.
        api_name_list : str
            API name for listing folders.

        Returns
        -------
        dict[str, object] or None
            The folder information or None if not found.
        """
        parent = 0
        found_path = ''
        folder = ''
        for part in path.strip('/').split('/'):
            count_response = self._count_folders(parent, api_name_count)
            if not count_response['success']:
                return
            count = count_response['data']['count']
            for offset in range(0, count, 1000):
                folders_response = self._list_folders(parent, limit=1000, offset=offset, additional=None,
                                                      api_name=api_name_list)
                if not folders_response['success']:
                    return
                folder = next(filter(lambda elem: elem['name'] == '%s/%s' % (found_path, part),
                                     folders_response['data']['list']), None)
                if folder:
                    parent = folder['id']
                    found_path = folder['name']
                    break
            else:
                return
        return folder

    def get_album(self, album_id: str | int | list[str] | list[int], additional: Optional[str | list[str]] = None) -> dict[str, object] | str:
        """
        Retrieve information about a specific album.

        Parameters
        ----------
        album_id : str
            The album ID.
        additional : str or list of str, optional
            Additional fields to include.

        Returns
        -------
        dict[str, object] or str
            The album information or an error message.
        """
        if not isinstance(album_id, list):
            album_id = [int(album_id)]
        else:
            album_id = [int(x) for x in album_id]
        if additional is None:
            additional = []
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': json.dumps(album_id),
                     'additional': json.dumps(additional)}

        return self.request_data(api_name, api_path, req_param)

    def list_albums(self, offset: int = 0, limit: int = 100) -> dict[str, object] | str:
        """
        List albums.

        Parameters
        ----------
        offset : int, optional
            Number of albums to skip. Default is 0.
        limit : int, optional
            Maximum number of albums to return. Default is 100.

        Returns
        -------
        dict[str, object] or str
            The list of albums or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def suggest_condition(self,
                          keyword: str,
                          condition: Optional[list[str]] = None,
                          user_id: Optional[str] = None
                          ) -> dict[str, object] | str:
        """
        Suggest album conditions based on a keyword.

        Parameters
        ----------
        keyword : str
            The keyword to suggest conditions for.
        condition : list of str, optional
            List of conditions to use. Default is ['general_tag'].
        user_id : str, optional
            User ID to use. If None, uses the current user.

        Returns
        -------
        dict[str, object] or str
            The suggested conditions or an error message.
        """
        if condition is None:
            condition = ['general_tag']
        if user_id is None:
            user_id = self.get_userinfo()['data']['id']

        api_name = 'SYNO.Foto.Browse.ConditionAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'suggest', 'user_id': user_id, 'keyword': keyword,
                     'condition': json.dumps(condition)}

        return self.request_data(api_name, api_path, req_param)

    def create_album(self, name: str, condition: list[str]) -> dict[str, object] | str:
        """
        Create a new album with the specified condition.

        Parameters
        ----------
        name : str
            The name of the album.
        condition : list of str
            The condition for the album.

        Returns
        -------
        dict[str, object] or str
            The API response for album creation.
        """
        api_name = 'SYNO.Foto.Browse.ConditionAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create', 'name': '"'+name+'"',
                     'condition': json.dumps(condition)}

        return self.request_data(api_name, api_path, req_param)

    def delete_album(self, album_id: str | int | list[str] | list[int]) -> dict[str, object] | str:
        """
        Delete an album by ID.

        Parameters
        ----------
        album_id : str or int or list of str or int
            The album ID or list of album IDs.

        Returns
        -------
        dict[str, object] or str
            The API response for album deletion.
        """
        if not isinstance(album_id, list):
            album_id = [int(album_id)]
        else:
            album_id = [int(x) for x in album_id]
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'delete', 'id': json.dumps(album_id)}

        return self.request_data(api_name, api_path, req_param)

    def create_normal_album(self, name: str, item_ids: list[int]) -> dict[str, object] | str:
        """
        Create a normal (manual) album with the specified items.

        Parameters
        ----------
        name : str
            The name of the album.
        item_ids : list of int
            List of item IDs to add to the album.

        Returns
        -------
        dict[str, object] or str
            The API response. Album data is in ``data['album']``.
        """
        api_name = 'SYNO.Foto.Browse.NormalAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'create',
                     'name': '"' + name + '"',
                     'item': json.dumps(item_ids)}

        return self.request_data(api_name, api_path, req_param)

    def rename_album(self, album_id: int, name: str) -> dict[str, object] | str:
        """
        Rename an album.

        Parameters
        ----------
        album_id : int
            The ID of the album to rename.
        name : str
            The new name for the album.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'set_name', 'id': album_id,
                     'name': name}

        return self.request_data(api_name, api_path, req_param)

    def get_normal_album(self, album_id: int) -> dict[str, object] | str:
        """
        Retrieve information about a normal (manual) album.

        Parameters
        ----------
        album_id : int
            The album ID.

        Returns
        -------
        dict[str, object] or str
            The album information or an error message.
        """
        api_name = 'SYNO.Foto.Browse.NormalAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'id': album_id}

        return self.request_data(api_name, api_path, req_param)

    def list_categories(self) -> dict[str, object] | str:
        """
        List photo categories (recently added, geocoding, general tag, video).

        Returns
        -------
        dict[str, object] or str
            The list of categories or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Category'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def list_concepts(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List AI-detected concepts (tags, objects, scenes).

        Parameters
        ----------
        offset : int, optional
            Number of concepts to skip. Default is 0.
        limit : int, optional
            Maximum number of concepts to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of concepts or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Concept'
        return self._list_tags(api_name, offset, limit)

    def list_team_concepts(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List AI-detected concepts in Team Space.

        Parameters
        ----------
        offset : int, optional
            Number of concepts to skip. Default is 0.
        limit : int, optional
            Maximum number of concepts to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of concepts or an error message.
        """
        return self._list_tags('SYNO.FotoTeam.Browse.Concept', offset, limit)

    def count_concepts(self) -> dict[str, object] | str:
        """
        Count AI-detected concepts.

        Returns
        -------
        dict[str, object] or str
            The count of concepts or an error message.
        """
        return self._count_tags('SYNO.Foto.Browse.Concept')

    def count_team_concepts(self) -> dict[str, object] | str:
        """
        Count AI-detected concepts in Team Space.

        Returns
        -------
        dict[str, object] or str
            The count of concepts or an error message.
        """
        return self._count_tags('SYNO.FotoTeam.Browse.Concept')

    def list_general_tags(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List general tags.

        Parameters
        ----------
        offset : int, optional
            Number of tags to skip. Default is 0.
        limit : int, optional
            Maximum number of tags to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of tags or an error message.
        """
        api_name = 'SYNO.Foto.Browse.GeneralTag'
        return self._list_tags(api_name, offset, limit)

    def list_team_general_tags(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List general tags in Team Space.

        Parameters
        ----------
        offset : int, optional
            Number of tags to skip. Default is 0.
        limit : int, optional
            Maximum number of tags to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of tags or an error message.
        """
        return self._list_tags('SYNO.FotoTeam.Browse.GeneralTag', offset, limit)

    def count_general_tags(self) -> dict[str, object] | str:
        """
        Count general tags.

        Returns
        -------
        dict[str, object] or str
            The count of tags or an error message.
        """
        return self._count_tags('SYNO.Foto.Browse.GeneralTag')

    def count_team_general_tags(self) -> dict[str, object] | str:
        """
        Count general tags in Team Space.

        Returns
        -------
        dict[str, object] or str
            The count of tags or an error message.
        """
        return self._count_tags('SYNO.FotoTeam.Browse.GeneralTag')

    def list_geocoding(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List geocoding locations from all photos.

        Parameters
        ----------
        offset : int, optional
            Number of locations to skip. Default is 0.
        limit : int, optional
            Maximum number of locations to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of geocoding locations or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Geocoding'
        return self._list_tags(api_name, offset, limit)

    def list_team_geocoding(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List geocoding locations in Team Space.

        Parameters
        ----------
        offset : int, optional
            Number of locations to skip. Default is 0.
        limit : int, optional
            Maximum number of locations to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of geocoding locations or an error message.
        """
        return self._list_tags('SYNO.FotoTeam.Browse.Geocoding', offset, limit)

    def count_geocoding(self) -> dict[str, object] | str:
        """
        Count geocoding locations.

        Returns
        -------
        dict[str, object] or str
            The count of geocoding locations or an error message.
        """
        return self._count_tags('SYNO.Foto.Browse.Geocoding')

    def count_team_geocoding(self) -> dict[str, object] | str:
        """
        Count geocoding locations in Team Space.

        Returns
        -------
        dict[str, object] or str
            The count of geocoding locations or an error message.
        """
        return self._count_tags('SYNO.FotoTeam.Browse.Geocoding')

    def list_persons(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List detected persons (face recognition).

        Parameters
        ----------
        offset : int, optional
            Number of persons to skip. Default is 0.
        limit : int, optional
            Maximum number of persons to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of persons or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Person'
        return self._list_tags(api_name, offset, limit)

    def list_team_persons(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List detected persons in Team Space.

        Parameters
        ----------
        offset : int, optional
            Number of persons to skip. Default is 0.
        limit : int, optional
            Maximum number of persons to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of persons or an error message.
        """
        return self._list_tags('SYNO.FotoTeam.Browse.Person', offset, limit)

    def count_persons(self) -> dict[str, object] | str:
        """
        Count detected persons.

        Returns
        -------
        dict[str, object] or str
            The count of persons or an error message.
        """
        return self._count_tags('SYNO.Foto.Browse.Person')

    def count_team_persons(self) -> dict[str, object] | str:
        """
        Count detected persons in Team Space.

        Returns
        -------
        dict[str, object] or str
            The count of persons or an error message.
        """
        return self._count_tags('SYNO.FotoTeam.Browse.Person')

    def get_person(self, person_id: int) -> dict[str, object] | str:
        """
        Get information about a detected person.

        Parameters
        ----------
        person_id : int
            The person ID (from ``list_persons()``).

        Returns
        -------
        dict[str, object] or str
            The person information or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Person'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': person_id}

        return self.request_data(api_name, api_path, req_param)

    def rename_person(self, person_id: int, name: str
                      ) -> dict[str, object] | str:
        """
        Rename a detected person.

        Parameters
        ----------
        person_id : int
            The person ID (from ``list_persons()``).
        name : str
            The new name for the person. Use ``'Unnamed'`` to clear.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Browse.Person'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'id': person_id, 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def list_items_by_person(self, person_id: int, offset: int = 0,
                             limit: int = 1000,
                             additional: Optional[list[str]] = None
                             ) -> dict[str, object] | str:
        """
        List photos of a specific person.

        Parameters
        ----------
        person_id : int
            The person ID (from ``list_persons()``).
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.
        additional : list of str, optional
            Additional fields to include (e.g., ``['thumbnail', 'person']``).

        Returns
        -------
        dict[str, object] or str
            The list of photos or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'offset': offset, 'limit': limit,
                     'person_id': person_id}

        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def get_team_person(self, person_id: int) -> dict[str, object] | str:
        """
        Get information about a detected person in Team Space.

        Parameters
        ----------
        person_id : int
            The person ID (from ``list_team_persons()``).

        Returns
        -------
        dict[str, object] or str
            The person information or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Person'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': person_id}

        return self.request_data(api_name, api_path, req_param)

    def list_items_by_team_person(self, person_id: int, offset: int = 0,
                                  limit: int = 1000,
                                  additional: Optional[list[str]] = None
                                  ) -> dict[str, object] | str:
        """
        List Team Space photos of a specific person.

        Parameters
        ----------
        person_id : int
            The person ID (from ``list_team_persons()``).
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.
        additional : list of str, optional
            Additional fields to include.

        Returns
        -------
        dict[str, object] or str
            The list of photos or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'offset': offset, 'limit': limit,
                     'person_id': person_id}

        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def list_recently_added(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List recently added items.

        Parameters
        ----------
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of recently added items or an error message.
        """
        api_name = 'SYNO.Foto.Browse.RecentlyAdded'
        return self._list_tags(api_name, offset, limit)

    def list_team_recently_added(self, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List recently added items in Team Space.

        Parameters
        ----------
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of recently added items or an error message.
        """
        return self._list_tags('SYNO.FotoTeam.Browse.RecentlyAdded', offset, limit)

    def count_recently_added(self) -> dict[str, object] | str:
        """
        Count recently added items.

        Returns
        -------
        dict[str, object] or str
            The count of recently added items or an error message.
        """
        return self._count_tags('SYNO.Foto.Browse.RecentlyAdded')

    def count_team_recently_added(self) -> dict[str, object] | str:
        """
        Count recently added items in Team Space.

        Returns
        -------
        dict[str, object] or str
            The count of recently added items or an error message.
        """
        return self._count_tags('SYNO.FotoTeam.Browse.RecentlyAdded')

    def get_timeline(self) -> dict[str, object] | str:
        """
        Get the timeline sections.

        Returns
        -------
        dict[str, object] or str
            The timeline sections or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Timeline'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_team_timeline(self) -> dict[str, object] | str:
        """
        Get the Team Space timeline sections.

        Returns
        -------
        dict[str, object] or str
            The timeline sections or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Timeline'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_similar_timeline(self) -> dict[str, object] | str:
        """
        Get the similar-items timeline.

        Returns
        -------
        dict[str, object] or str
            The similar timeline sections or an error message.
        """
        api_name = 'SYNO.Foto.Browse.SimilarTimeline'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_team_similar_timeline(self) -> dict[str, object] | str:
        """
        Get the Team Space similar-items timeline.

        Returns
        -------
        dict[str, object] or str
            The similar timeline sections or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.SimilarTimeline'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def list_similar_items(self, item_id: int, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List items similar to the specified item.

        Parameters
        ----------
        item_id : int
            The ID of the reference item.
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of similar items or an error message.
        """
        api_name = 'SYNO.Foto.Browse.SimilarItem'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'offset': offset, 'limit': limit, 'id': item_id}

        return self.request_data(api_name, api_path, req_param)

    def list_team_similar_items(self, item_id: int, offset: int = 0, limit: int = 1000) -> dict[str, object] | str:
        """
        List items similar to the specified item in Team Space.

        Parameters
        ----------
        item_id : int
            The ID of the reference item.
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.

        Returns
        -------
        dict[str, object] or str
            The list of similar items or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.SimilarItem'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'offset': offset, 'limit': limit, 'id': item_id}

        return self.request_data(api_name, api_path, req_param)

    def _list_tags(self, api_name: str, offset: int = 0, limit: int = 1000) -> Any:
        """
        Internal method to list tag-like entities (concepts, tags, persons, etc.).

        Parameters
        ----------
        api_name : str
            API name to use.
        offset : int, optional
            Number of items to skip. Default is 0.
        limit : int, optional
            Maximum number of items to return. Default is 1000.

        Returns
        -------
        Any
            The API response.
        """
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def _count_tags(self, api_name: str) -> Any:
        """
        Internal method to count tag-like entities.

        Parameters
        ----------
        api_name : str
            API name to use.

        Returns
        -------
        Any
            The API response.
        """
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'count'}

        return self.request_data(api_name, api_path, req_param)

    def set_album_condition(self, folder_id: int, condition: list[str]) -> dict[str, object] | str:
        """
        Set the condition for an album.

        Parameters
        ----------
        folder_id : int
            The folder ID.
        condition : list of str
            The condition to set.

        Returns
        -------
        dict[str, object] or str
            The API response for setting the condition.
        """
        api_name = 'SYNO.Foto.Browse.ConditionAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_condition', 'id': folder_id,
                     'condition': json.dumps(condition)}

        return self.request_data(api_name, api_path, req_param)

    def share_album(self,
                    album_id: str,
                    permission: Optional[str | list[str]] = None,
                    enabled: bool = True,
                    expiration: int | str = 0
                    ) -> Any:
        """
        Share an album with specified permissions.

        Parameters
        ----------
        album_id : str
            The album ID.
        permission : str or list of str, optional
            Permissions to set.
        enabled : bool, optional
            Whether sharing is enabled. Default is True.
        expiration : int or str, optional
            Expiration time for the share. Default is 0.

        Returns
        -------
        Any
            The API response for sharing the album.
        """
        api_name = 'SYNO.Foto.Sharing.Passphrase'
        return self._share(api_name, policy='album', permission=permission, album_id=album_id,
                           enabled=enabled, expiration=expiration)

    def share_team_folder(self,
                          folder_id: int,
                          permission: Optional[str] = None,
                          enabled: bool = True,
                          expiration: int | str = 0
                          ) -> Any:
        """
        Share a team folder with specified permissions.

        Parameters
        ----------
        folder_id : int
            The folder ID.
        permission : str, optional
            Permissions to set.
        enabled : bool, optional
            Whether sharing is enabled. Default is True.
        expiration : int or str, optional
            Expiration time for the share. Default is 0.

        Returns
        -------
        Any
            The API response for sharing the team folder.
        """
        api_name = 'SYNO.FotoTeam.Sharing.Passphrase'
        return self._share(api_name, policy='folder', permission=permission, folder_id=folder_id,
                           enabled=enabled, expiration=expiration)

    def _share(self,
               api_name: str,
               policy: str,
               permission: str,
               expiration: int | str,
               **kwargs
               ) -> dict[str, object] | Any:
        """
        Internal method to share an album or folder.

        Parameters
        ----------
        api_name : str
            API name to use.
        policy : str
            Sharing policy.
        permission : str
            Permissions to set.
        expiration : int or str
            Expiration time for the share.
        **kwargs
            Additional keyword arguments.

        Returns
        -------
        dict[str, object] or Any
            The API response for sharing.
        """
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'set_shared', 'policy': policy, **kwargs}

        shared_response = self.request_data(api_name, api_path, req_param)
        if not shared_response['success']:
            return

        if not permission:
            return shared_response

        passphrase = shared_response['data']['passphrase']

        req_param = {'version': info['maxVersion'], 'method': 'update', 'passphrase': passphrase,
                     'expiration': expiration, 'permission': json.dumps(permission)}
        return self.request_data(api_name, api_path, req_param)

    def list_shareable_users_and_groups(self, team_space_sharable_list: bool = False) -> dict[str, object] | str:
        """
        List users and groups that can be shared with.

        Parameters
        ----------
        team_space_sharable_list : bool, optional
            Whether to include team space sharable list. Default is False.

        Returns
        -------
        dict[str, object] or str
            The list of users and groups or an error message.
        """
        api_name = 'SYNO.Foto.Sharing.Misc'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_user_group',
                     'team_space_sharable_list': team_space_sharable_list}

        return self.request_data(api_name, api_path, req_param)

    def list_item_in_folders(self, offset: int = 0, limit: int = 1000, folder_id: Optional[int] = None,
                             sort_by: str = 'filename', sort_direction: str = 'desc', type: str = None,
                             passphrase: str = None, additional: Optional[list[str]] = None
                             ) -> dict[str, object] | str:
        """
        List items in a Personal Space folder.

        Parameters
        ----------
        offset : int
            Specify how many items are skipped before beginning to return listed items.
        limit : int
            Number of items requested. Default is 1000.
        folder_id : int, required
            ID of the folder returned by ``list_folders``.
        sort_by : str, optional
            Possible values: 'filename', 'filesize', 'takentime', 'item_type'.
        sort_direction : str, optional
            Possible values: 'asc' or 'desc'. Defaults to: 'desc'.
        type : str, optional
            Possible values: 'photo', 'video', 'live'.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.
            Possible values:
                `["thumbnail","resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]`.

        Returns
        -------
        dict[str, object] or str
            The list of items or an error message.
        """
        return self._list_items_in_folder(
            'SYNO.Foto.Browse.Item', offset, limit, folder_id, sort_by, sort_direction, type, passphrase, additional)

    def list_item_in_team_folders(self, offset: int = 0, limit: int = 1000, folder_id: Optional[int] = None,
                                  sort_by: str = 'filename', sort_direction: str = 'desc', type: str = None,
                                  passphrase: str = None, additional: Optional[list[str]] = None
                                  ) -> dict[str, object] | str:
        """
        List items in a Team Space folder.

        Parameters
        ----------
        offset : int
            Specify how many items are skipped before beginning to return listed items.
        limit : int
            Number of items requested. Default is 1000.
        folder_id : int, required
            ID of the folder returned by ``list_teams_folders``.
        sort_by : str, optional
            Possible values: 'filename', 'filesize', 'takentime', 'item_type'.
        sort_direction : str, optional
            Possible values: 'asc' or 'desc'. Defaults to: 'desc'.
        type : str, optional
            Possible values: 'photo', 'video', 'live'.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.
            Possible values:
                `["thumbnail","resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]`.

        Returns
        -------
        dict[str, object] or str
            The list of team items or an error message.
        """
        return self._list_items_in_folder(
            'SYNO.FotoTeam.Browse.Item', offset, limit, folder_id, sort_by, sort_direction, type, passphrase, additional)

    def list_items_in_album(self, album_id: int, offset: int = 0, limit: int = 1000,
                            sort_by: str = 'filename', sort_direction: str = 'desc',
                            type: str = None, passphrase: str = None,
                            additional: Optional[list[str]] = None
                            ) -> dict[str, object] | str:
        """
        List items in an album.

        Parameters
        ----------
        album_id : int, required
            The ID of the album (from ``list_albums()``).
        offset : int, optional
            Specify how many items are skipped before beginning to return listed items.
        limit : int, optional
            Number of items requested. Default is 1000.
        sort_by : str, optional
            Possible values: ``'filename'``, ``'filesize'``, ``'takentime'``, ``'item_type'``.
        sort_direction : str, optional
            Possible values: ``'asc'`` or ``'desc'``. Defaults to ``'desc'``.
        type : str, optional
            Possible values: ``'photo'``, ``'video'``, ``'live'``.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.
            Possible values:
                ``["thumbnail", "resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]``.

        Returns
        -------
        dict[str, object] or str
            The list of album items or an error message.
        """
        return self._list_items_in_album(
            album_id, offset, limit, sort_by, sort_direction, type, passphrase, additional)

    def count_items_in_album(self, album_id: int) -> dict[str, object] | str:
        """
        Count items in an album.

        Parameters
        ----------
        album_id : int
            The ID of the album.

        Returns
        -------
        dict[str, object] or str
            The count of album items or an error message.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'count', 'id': album_id}

        return self.request_data(api_name, api_path, req_param)

    def _list_items_in_album(self, album_id: int, offset: int, limit: int, sort_by: str,
                             sort_direction: str, item_type: Optional[str],
                             passphrase: Optional[str], additional: Optional[list[str]]) -> Any:
        """
        Internal method to list items in an album.

        Parameters
        ----------
        album_id : int
            The ID of the album.
        offset : int
            Specify how many items are skipped before beginning to return listed items.
        limit : int
            Number of items requested.
        sort_by : str
            Sort field.
        sort_direction : str
            Sort direction.
        item_type : str, optional
            Item type filter.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.

        Returns
        -------
        Any
            The API response.
        """
        if limit <= 0:
            raise ValueError(
                'limit must be greater than 0 for Synology Photos item listing.')

        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit,
                     'id': album_id, 'sort_by': sort_by, 'sort_direction': sort_direction}

        if item_type:
            req_param['type'] = item_type
        if passphrase:
            req_param['passphrase'] = passphrase
        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def list_items_in_team_album(self, album_id: int, offset: int = 0, limit: int = 1000,
                                 sort_by: str = 'filename', sort_direction: str = 'desc',
                                 type: str = None, passphrase: str = None,
                                 additional: Optional[list[str]] = None
                                 ) -> dict[str, object] | str:
        """
        List items in a Team Space album.

        Parameters
        ----------
        album_id : int, required
            The ID of the Team Space album (from ``list_albums()``).
        offset : int, optional
            Specify how many items are skipped before beginning to return listed items.
        limit : int, optional
            Number of items requested. Default is 1000.
        sort_by : str, optional
            Possible values: ``'filename'``, ``'filesize'``, ``'takentime'``, ``'item_type'``.
        sort_direction : str, optional
            Possible values: ``'asc'`` or ``'desc'``. Defaults to ``'desc'``.
        type : str, optional
            Possible values: ``'photo'``, ``'video'``, ``'live'``.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.
            Possible values:
                ``["thumbnail", "resolution", "orientation", "video_convert", "video_meta", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id", "address", "person"]``.

        Returns
        -------
        dict[str, object] or str
            The list of album items or an error message.
        """
        return self._list_items_in_album_team(
            album_id, offset, limit, sort_by, sort_direction, type, passphrase, additional)

    def count_items_in_team_album(self, album_id: int) -> dict[str, object] | str:
        """
        Count items in a Team Space album.

        Parameters
        ----------
        album_id : int
            The ID of the Team Space album.

        Returns
        -------
        dict[str, object] or str
            The count of album items or an error message.
        """
        api_name = 'SYNO.FotoTeam.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'count', 'id': album_id}

        return self.request_data(api_name, api_path, req_param)

    def _list_items_in_album_team(self, album_id: int, offset: int, limit: int, sort_by: str,
                                  sort_direction: str, item_type: Optional[str],
                                  passphrase: Optional[str], additional: Optional[list[str]]) -> Any:
        """
        Internal method to list items in a Team Space album.

        Parameters
        ----------
        album_id : int
            The ID of the Team Space album.
        offset : int
            Specify how many items are skipped before beginning to return listed items.
        limit : int
            Number of items requested.
        sort_by : str
            Sort field.
        sort_direction : str
            Sort direction.
        item_type : str, optional
            Item type filter.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.

        Returns
        -------
        Any
            The API response.
        """
        if limit <= 0:
            raise ValueError(
                'limit must be greater than 0 for Synology Photos item listing.')

        api_name = 'SYNO.FotoTeam.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit,
                     'id': album_id, 'sort_by': sort_by, 'sort_direction': sort_direction}

        if item_type:
            req_param['type'] = item_type
        if passphrase:
            req_param['passphrase'] = passphrase
        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def _list_items_in_folder(self, api_name: str, offset: int, limit: int, folder_id: Optional[int], sort_by: str,
                              sort_direction: str, item_type: Optional[str], passphrase: Optional[str],
                              additional: Optional[list[str]]) -> Any:
        """
        Internal method to list items in a Photos folder.

        Parameters
        ----------
        api_name : str
            API name to use.
        offset : int
            Specify how many items are skipped before beginning to return listed items.
        limit : int
            Number of items requested.
        folder_id : int
            ID of the folder.
        sort_by : str
            Sort field.
        sort_direction : str
            Sort direction.
        item_type : str, optional
            Item type filter.
        passphrase : str, optional
            Passphrase for a shared album.
        additional : list, optional
            Additional fields to include.

        Returns
        -------
        Any
            The API response.
        """
        if folder_id is None:
            raise ValueError(
                'folder_id is required; call list_folders() or list_teams_folders() first to find it.')
        if limit <= 0:
            raise ValueError(
                'limit must be greater than 0 for Synology Photos item listing.')

        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit,
                     'folder_id': folder_id, 'sort_by': sort_by, 'sort_direction': sort_direction}

        if item_type:
            req_param['type'] = item_type
        if passphrase:
            req_param['passphrase'] = passphrase
        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def list_search_filters(self) -> dict[str, object] | str:
        """
        List available search filters.

        Returns
        -------
        dict[str, object] or str
            The list of search filters or an error message.
        """
        api_name = 'SYNO.Foto.Search.Filter'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_guest_settings(self) -> dict[str, object] | str:
        """
        Retrieve guest settings for Photos.

        Returns
        -------
        dict[str, object] or str
            The guest settings or an error message.
        """
        api_name = 'SYNO.Foto.Setting.Guest'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_index_status(self) -> dict[str, object] | str:
        """
        Get the indexing status for photos.

        Returns
        -------
        dict[str, object] or str
            The index status counters (basic, thumbnail, metadata, face, concept, geo)
            or an error message.
        """
        api_name = 'SYNO.Foto.Index'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_team_index_status(self) -> dict[str, object] | str:
        """
        Get the Team Space indexing status for photos.

        Returns
        -------
        dict[str, object] or str
            The index status counters or an error message.
        """
        api_name = 'SYNO.FotoTeam.Index'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_admin_settings(self) -> dict[str, object] | str:
        """
        Get the admin settings for Photos.

        Returns
        -------
        dict[str, object] or str
            The admin settings (package version, global config) or an error message.
        """
        api_name = 'SYNO.Foto.Setting.Admin'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def set_admin_settings(self, **kwargs) -> dict[str, object] | str:
        """
        Set admin settings for Photos.

        Parameters
        ----------
        **kwargs : dict
            Admin settings key-value pairs to set.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Setting.Admin'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    def get_user_settings(self) -> dict[str, object] | str:
        """
        Get the user settings for Photos.

        Returns
        -------
        dict[str, object] or str
            The user settings (theme, sort, AME status) or an error message.
        """
        api_name = 'SYNO.Foto.Setting.User'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def set_user_settings(self, **kwargs) -> dict[str, object] | str:
        """
        Set user settings for Photos.

        Parameters
        ----------
        **kwargs : dict
            User settings key-value pairs to set.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Setting.User'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    def get_team_space_settings(self) -> dict[str, object] | str:
        """
        Get Team Space settings.

        Returns
        -------
        dict[str, object] or str
            The Team Space settings (enabled, concepts, person, similar) or an error message.
        """
        api_name = 'SYNO.Foto.Setting.TeamSpace'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def set_team_space_settings(self, **kwargs) -> dict[str, object] | str:
        """
        Set Team Space settings.

        Parameters
        ----------
        **kwargs : dict
            Team Space settings key-value pairs to set.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Setting.TeamSpace'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    def get_wizard_settings(self) -> dict[str, object] | str:
        """
        Get the wizard (first-time setup) settings for Photos.

        Returns
        -------
        dict[str, object] or str
            The wizard settings or an error message.
        """
        api_name = 'SYNO.Foto.Setting.Wizard'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def set_wizard_settings(self, **kwargs) -> dict[str, object] | str:
        """
        Set wizard (first-time setup) settings for Photos.

        Parameters
        ----------
        **kwargs : dict
            Wizard settings key-value pairs to set.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Setting.Wizard'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    def get_mobile_compatibility(self) -> dict[str, object] | str:
        """
        Get mobile version compatibility info.

        Returns
        -------
        dict[str, object] or str
            The mobile compatibility settings or an error message.
        """
        api_name = 'SYNO.Foto.Setting.MobileCompatibility'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_item_info(self, item_id: int, additional: Optional[list[str]] = None
                      ) -> dict[str, object] | str:
        """
        Get detailed information about a photo item.

        Parameters
        ----------
        item_id : int
            The item ID (from ``list_items_in_album()`` or ``list_item_in_folders()``).
        additional : list of str, optional
            Additional fields to include.
            Possible values:
                ``["exif", "gps", "tag", "description", "person", "address",
                "thumbnail", "resolution", "orientation"]``.

        Returns
        -------
        dict[str, object] or str
            The item information. Detail fields are in ``data['list'][0]['additional']``.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': json.dumps([item_id])}

        if additional:
            req_param['additional'] = json.dumps(additional)

        return self.request_data(api_name, api_path, req_param)

    def set_item_description(self, item_id: int, description: str
                             ) -> dict[str, object] | str:
        """
        Set the description of a photo item.

        Parameters
        ----------
        item_id : int
            The item ID.
        description : str
            The new description. Pass an empty string to clear it.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'id': json.dumps([item_id]),
                     'description': '"' + description + '"'}

        return self.request_data(api_name, api_path, req_param)

    def set_item_favorite(self, item_id: int, favorite: bool = True
                          ) -> dict[str, object] | str:
        """
        Set or unset the favorite flag on a photo item.

        Parameters
        ----------
        item_id : int
            The item ID.
        favorite : bool, optional
            ``True`` to mark as favorite, ``False`` to unmark. Default is ``True``.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_favorite',
                     'id': json.dumps([item_id]),
                     'favorite': favorite}

        return self.request_data(api_name, api_path, req_param)

    def set_item_rating(self, item_id: int, rating: int = 0
                        ) -> dict[str, object] | str:
        """
        Set the star rating of a photo item (0-5).

        Parameters
        ----------
        item_id : int
            The item ID.
        rating : int, optional
            Star rating from 0 to 5. Default is 0.

        Returns
        -------
        dict[str, object] or str
            The API response.
        """
        api_name = 'SYNO.Foto.Browse.Item'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'id': json.dumps([item_id]),
                     'rating': rating}

        return self.request_data(api_name, api_path, req_param)

    def search_suggestions(self, keyword: str) -> dict[str, object] | str:
        """
        Get search suggestions for a keyword.

        Parameters
        ----------
        keyword : str
            The search keyword.

        Returns
        -------
        dict[str, object] or str
            The search suggestions or an error message.
        """
        api_name = 'SYNO.Foto.Search.Search'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'suggest',
                     'keyword': keyword}

        return self.request_data(api_name, api_path, req_param)

    def download_item(self, item_id: int, dest_path: str = None
                      ) -> Optional[str]:
        """
        Download a photo item to a file.

        Parameters
        ----------
        item_id : int
            The item ID to download.
        dest_path : str, optional
            The destination file path. If not provided, saves to the current
            directory using the item's filename.

        Returns
        -------
        str or None
            The path to the downloaded file, or ``None`` if the download failed.
        """
        import os

        api_name = 'SYNO.Foto.Download'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'download',
                     'unit_id': json.dumps([item_id])}

        response = self.request_data(api_name, api_path, req_param,
                                     response_json=False)

        if response.status_code == 200 and len(response.content) > 100:
            if dest_path is None:
                dest_path = os.path.basename(str(item_id)) + '.jpg'
            with open(dest_path, 'wb') as f:
                f.write(response.content)
            return dest_path

        return None
