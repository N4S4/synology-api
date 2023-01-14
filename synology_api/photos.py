from typing import Optional
from . import auth as syn
import json


class Photos:

    def __init__(self,
                    ip_address : str,
                    port : str,
                    username : str,
                    password : str,
                    secure : bool = False,
                    cert_verify : bool = False,
                    dsm_version : int = 7,
                    debug : bool = True,
                    otp_code : Optional[str] = None
                ) -> None:
        self.session : syn.Authentication = syn.Authentication(ip_address, port, username, password, secure,  cert_verify, dsm_version, debug, otp_code)

        self.session.login('Foto')
        self.session.get_api_list('Foto')

        self.request_data : function = self.session.request_data
        self.photos_list : dict[str, object] = self.session.app_api_list
        self._sid : str = self.session.sid
        self.base_url : str = self.session.base_url

        self._userinfo : dict[str, object] = None
        return

    def logout(self) -> None:
        self.session.logout('Foto')
        return

    def get_userinfo(self) -> dict[str, object]:
        if self._userinfo is not None:
            return self._userinfo

        api_name = 'SYNO.Foto.UserInfo'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'me'}
        self._userinfo = self.request_data(api_name, api_path, req_param)

        return self._userinfo

    def get_folder(self, folder_id:int=0) -> dict[str, object]:
        api_name = 'SYNO.Foto.Browse.Folder'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': folder_id}

        return self.request_data(api_name, api_path, req_param)

    def list_folders(self,
                        folder_id : int = 0,
                        limit : int = 1000,
                        offset : int = 0,
                        additional : Optional[str | list[str]] = None
                    ) -> dict[str, object]:
        return self._list_folders(folder_id, limit, offset, additional, 'SYNO.Foto.Browse.Folder')

    def list_teams_folders(self,
                            folder_id : int = 0,
                            limit : int = 2000,
                            offset : int = 0,
                            additional : Optional[str | list[str]] = None
                        ) -> dict[str, object]:
        return self._list_folders(folder_id, limit, offset, additional, 'SYNO.FotoTeam.Browse.Folder')

    def _list_folders(self,
                        folder_id : int,
                        limit : int,
                        offset : int,
                        additional : str|list[str],
                        api_name : str
                    ) -> dict[str, object]:
        if additional is None:
            additional = []
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'id': folder_id, 'limit': limit, 'offset': offset,
                     'additional': json.dumps(additional)}

        return self.request_data(api_name, api_path, req_param)

    def count_folders(self, folder_id:int=0) -> dict[str, object]:
        return self._count_folders(folder_id, 'SYNO.Foto.Browse.Folder')

    def count_team_folders(self, folder_id:int=0) -> dict[str, object]:
        return self._count_folders(folder_id, 'SYNO.FotoTeam.Browse.Folder')

    def _count_folders(self, folder_id:int, api_name:str) -> dict[str, object]:
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'count', 'id': folder_id}

        return self.request_data(api_name, api_path, req_param)

    def lookup_folder(self, path:str) -> Optional[dict[str, object]]:
        return self._lookup_folder(path, 'SYNO.FotoBrowse.Folder', 'SYNO.Foto.Browse.Folder')

    def lookup_team_folder(self, path:str) -> Optional[dict[str, object]]:
        return self._lookup_folder(path, 'SYNO.FotoTeam.Browse.Folder', 'SYNO.FotoTeam.Browse.Folder')

    def _lookup_folder(self, path:str, api_name_count:str, api_name_list:str) -> Optional[dict[str, object]]:
        parent = 0
        found_path = ''
        folder = ''
        for part in path.strip('/').split('/'):
            count_response = self._count_folders(parent, api_name_count)
            if not count_response['success']:
                return None
            count = count_response['data']['count']
            for offset in range(0, count, 1000):
                folders_response = self._list_folders(parent, limit=1000, offset=offset, additional=None,
                                                      api_name=api_name_list)
                if not folders_response['success']:
                    return None
                folder = next(filter(lambda elem: elem['name'] == '%s/%s' % (found_path, part),
                                     folders_response['data']['list']), None)
                if folder:
                    parent = folder['id']
                    found_path = folder['name']
                    break
            else:
                return None
        return folder

    def get_album(self, album_id:int, additional:Optional[str | list[str]]=None) -> dict[str, object]:
        if not isinstance(album_id, list):
            album_id = [album_id]
        if additional is None:
            additional = []
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': json.dumps(album_id),
                     'additional': json.dumps(additional)}

        return self.request_data(api_name, api_path, req_param)

    def list_albums(self, offset:int=0, limit:int=100) -> dict[str, object]:
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def suggest_condition(self, keyword:str, condition:Optional[str | list[str]]=None, user_id:Optional[str]=None) -> dict[str, object]:
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

    def create_album(self, name:str, condition:str|list[str]) -> dict[str, object]:
        api_name = 'SYNO.Foto.Browse.ConditionAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create', 'name': name,
                     'condition': json.dumps(condition)}

        return self.request_data(api_name, api_path, req_param)

    def delete_album(self, album_id:int | list[int]) -> dict[str, object]:
        if not isinstance(album_id, list):
            album_id = [album_id]
        api_name = 'SYNO.Foto.Browse.Album'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete', 'id': json.dumps(album_id)}

        return self.request_data(api_name, api_path, req_param)

    def set_album_condition(self, folder_id:int, condition:str | list[str]) -> dict[str, object]:
        api_name = 'SYNO.Foto.Browse.ConditionAlbum'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_condition', 'id': folder_id,
                     'condition': json.dumps(condition)}

        return self.request_data(api_name, api_path, req_param)

    def share_album(self,
                        album_id : int, 
                        permission : Optional[str | list[str]] = None, 
                        enabled : bool = True,
                        expiration : int | str = 0 # Expiry in other API's can either be unix timestamp or 'yyyy-mm-dd'
                    ) -> None:
        self._share('SYNO.Foto.Sharing.Passphrase', policy='album', permission=permission, album_id=album_id,
                    enabled=enabled, expiration=expiration)
        return

    def share_team_folder(self,
                            folder_id : int,
                            permission : Optional[str | list[str]] = None,
                            enabled : bool = True,
                            expiration : int | str = 0 # Expiry in other API's can either be unix timestamp or 'yyyy-mm-dd'
                        ) -> None:
        self._share('SYNO.FotoTeam.Sharing.Passphrase', policy='folder', permission=permission, folder_id=folder_id,
                    enabled=enabled, expiration=expiration)
        return

    def _share(self,
                api_name : str,
                policy : str,
                permission : str | list[str],
                expiration : int | str, # Expiry in other API's can either be unix timestamp or 'yyyy-mm-dd'
                **kwargs
            ) -> Optional[dict[str, object]]:
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set_shared', 'policy': policy, **kwargs}

        shared_response = self.request_data(api_name, api_path, req_param)
        if not shared_response['success']:
            return None

        if not permission:
            return shared_response

        passphrase = shared_response['data']['passphrase']

        req_param = {'version': info['maxVersion'], 'method': 'update', 'passphrase': passphrase,
                     'expiration': expiration, 'permission': json.dumps(permission)}
        return self.request_data(api_name, api_path, req_param)

    def list_shareable_users_and_groups(self, team_space_sharable_list:bool=False) -> dict[str, object]:
        api_name = 'SYNO.Foto.Sharing.Misc'
        info = self.photos_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_user_group',
                     'team_space_sharable_list': team_space_sharable_list}

        return self.request_data(api_name, api_path, req_param)
