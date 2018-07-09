from . import auth as syn
import requests


class AudioStation:

    def __init__(self, ip_address, port, username, password):
        self.session = syn.Authentication(ip_address, port, username, password)

        self.session.login('AudioStation')
        self.session.get_api_list('AudioStation')

        self.audiostation_list = self.session.app_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

    def request_data(self, name, api_path, req_param, method=None, response_json=True):  # 'post' or 'get'

        if method is None:
            method = 'get'

        req_param['_sid'] = self._sid

        if method == 'get':
            url = ('%s%s' % (self.base_url, api_path)) + '?api=' + name
            response = requests.get(url, req_param)

            if response_json is True:
                return response.json()
            else:
                return response

        elif method == 'post':
            url = ('%s%s' % (self.base_url, api_path)) + '?api=' + name
            response = requests.post(url, req_param)

            if response_json is True:
                return response.json()
            else:
                return response

    def logout(self):
        self.session.logout('AudioStation')

    def get_info(self):
        api_name = 'SYNO.AudioStation.Info'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_playlist_info(self):
        api_name = 'SYNO.AudioStation.Playlist'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'library': 'all', 'limit': '100000', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_remote_player(self):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'type': 'all', 'additional': 'subplayer_list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_pinned_song(self):
        api_name = 'SYNO.AudioStation.Pin'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def device_id(self, device):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'getplaylist', 'id': device, 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    # You Must choose the device if any from list_remote_player()

    def remote_play(self, device):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'play'}

        return self.request_data(api_name, api_path, req_param)

    def remote_stop(self, device):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'stop'}

        return self.request_data(api_name, api_path, req_param)

    def remote_next(self, device):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'next'}

        return self.request_data(api_name, api_path, req_param)

    def remote_prev(self, device):
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.audiostation_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device, 'version': info['maxVersion'], 'action': 'prev'}

        return self.request_data(api_name, api_path, req_param)
