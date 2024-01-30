from __future__ import annotations
from typing import Optional
from . import base_api


class AudioStation(base_api.BaseApi):

    def get_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}
        return self.request_data(api_name, api_path, req_param)

    def get_playlist_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.Playlist'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'library': 'all', 'limit': '100000', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_remote_player(self) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'type': 'all', 'additional': 'subplayer_list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_pinned_song(self) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.Pin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def device_id(self, device: str) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'getplaylist', 'id': device, 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    # You Must choose the device if any from list_remote_player()

    def remote_play(self, device: str) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'play'}

        return self.request_data(api_name, api_path, req_param)

    def remote_stop(self, device: str) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'stop'}

        return self.request_data(api_name, api_path, req_param)

    def remote_next(self, device: str) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'next'}

        return self.request_data(api_name, api_path, req_param)

    def remote_prev(self, device: str) -> dict[str, object] | str:
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'prev'}

        return self.request_data(api_name, api_path, req_param)
