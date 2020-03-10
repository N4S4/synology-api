from .synology import Synology, api_call


class AudioStation(Synology):


    app = 'AudioStation'

    def __init__(self, ip_address, port, username, password):
        super(AudioStation, self).__init__(ip_address, port, username,
                                           password)

        self.login(self.app)
        self.populate_api_dict(self.app)

        print('You are now logged in!')

    def logout(self):
        super().logout(self.app)

    @api_call()
    def get_info(self):
        return self.api_request('Info', 'getinfo')

    '''
       Method: list
       Args: library = all
       limit = 100000
       '''

    @api_call()
    def get_playlist_info(self):
        param = {'library': 'all', 'limit': '100000'}
        return self.api_request('Playlist', 'getinfo', param)

    '''
    methid: list
    type: all
    additional: subplayer_list
    '''

    @api_call()
    def list_remote_player(self):
        param = {'type': 'all', 'additional': 'subplayer_list'}

        return self.api_request('RemotePlayer', 'list', param)


    @api_call()
    def list_pinned_song(self):
        return self.api_request('Pin', 'list')

    '''
    id: device
    '''
    @api_call()
    def device_id(self, device):
        param = {'id': device}

        return self.api_request('RemotePLayer', 'getplaylist', param)

    # You Must choose the device if any from list_remote_player()

    @api_call()
    def remote_play(self, device):
        param = {'id': device}

        return self.api_request('RemotePlayer', 'control', param)

    '''
    id: device
    action: stop
    '''
    @api_call()
    def remote_stop(self, device):
        param = {'id': device, 'action': 'stop'}

        return self.api_request('RemotePlayer', 'control', param)

    @api_call()
    def remote_next(self, device):
        param = {'id': device, 'action': 'next'}

        return self.api_request('RemotePlayer', 'control', param)

    @api_call()
    def remote_prev(self, device):
        param = {'id': device, 'action': 'prev'}

        return self.api_request('RemotePlayer', 'control', param)
