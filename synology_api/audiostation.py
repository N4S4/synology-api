from typing import Optional
from . import auth as syn


class AudioStation:

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

        self.session.login('AudioStation')
        self.session.get_api_list('AudioStation')

        self.request_data : function = self.session.request_data
        self.audiostation_list : dict[str, object] = self.session.app_api_list
        self._sid : str = self.session.sid
        self.base_url : str = self.session.base_url

    def logout(self) -> None:
        self.session.logout('AudioStation')
        return

    def get_info(self) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.Info'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_playlist_info(self) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.Playlist'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'library': 'all', 'limit': '100000', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_remote_player(self) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'type': 'all', 'additional': 'subplayer_list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_pinned_song(self) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.Pin'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def device_id(self, device:str) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'getplaylist', 'id': device, 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    # You Must choose the device if any from list_remote_player()

    def remote_play(self, device:str) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'play'}

        return self.request_data(api_name, api_path, req_param)

    def remote_stop(self, device:str) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'stop'}

        return self.request_data(api_name, api_path, req_param)

    def remote_next(self, device:str) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'next'}

        return self.request_data(api_name, api_path, req_param)

    def remote_prev(self, device:str) -> dict[str, object]:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'prev'}

        return self.request_data(api_name, api_path, req_param)
