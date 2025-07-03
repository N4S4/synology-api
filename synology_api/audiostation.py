"""AudioStation API module for interacting with Synology AudioStation services."""
from __future__ import annotations
from typing import Optional
from . import base_api


class AudioStation(base_api.BaseApi):
    """A class to interact with Synology AudioStation API."""

    def get_info(self) -> dict[str, object] | str:
        """
        Retrieve general information about the AudioStation service.

        Returns
        -------
        dict[str, object]
            A dictionary containing the service information or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}
        return self.request_data(api_name, api_path, req_param)

    def get_playlist_info(self) -> dict[str, object] | str:
        """
        Retrieve information about playlists in AudioStation.

        Returns
        -------
        dict[str, object]
            A dictionary containing playlist information or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.Playlist'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'library': 'all',
                     'limit': '100000', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_remote_player(self) -> dict[str, object] | str:
        """
        Retrieve a list of remote players available in AudioStation.

        Returns
        -------
        dict[str, object]
            A dictionary containing information about remote players, or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'type': 'all',
                     'additional': 'subplayer_list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def list_pinned_song(self) -> dict[str, object] | str:
        """
        Retrieve a list of pinned songs in AudioStation.

        Returns
        -------
        dict[str, object]
            A dictionary containing information about pinned songs, or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.Pin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'list', 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    def device_id(self, device: str) -> dict[str, object] | str:
        """
        Retrieve the playlist for a specific remote device in AudioStation.

        Parameters
        ----------
        device : str
            The ID of the remote device.

        Returns
        -------
        dict[str, object]
            A dictionary containing the playlist information for the specified device.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'getplaylist',
                     'id': device, 'version': info['maxVersion']}

        return self.request_data(api_name, api_path, req_param)

    # You Must choose the device if any from list_remote_player()

    def remote_play(self, device: str) -> dict[str, object] | str:
        """
        Start playback on a specified remote device in AudioStation.

        Parameters
        ----------
        device : str
            The ID of the remote device on which to start playback.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the playback status or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device,
                     'version': info['maxVersion'], 'action': 'play'}

        return self.request_data(api_name, api_path, req_param)

    def remote_stop(self, device: str) -> dict[str, object] | str:
        """
        Stop playback on a specified remote device in AudioStation.

        Parameters
        ----------
        device : str
            The ID of the remote device on which to stop playback.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the stop status or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device,
                     'version': info['maxVersion'], 'action': 'stop'}

        return self.request_data(api_name, api_path, req_param)

    def remote_next(self, device: str) -> dict[str, object] | str:
        """
        Skip to the next track on a specified remote device in AudioStation.

        Parameters
        ----------
        device : str
            The ID of the remote device on which to skip to the next track.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the status of the operation or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device,
                     'version': info['maxVersion'], 'action': 'next'}

        return self.request_data(api_name, api_path, req_param)

    def remote_prev(self, device: str) -> dict[str, object] | str:
        """
        Skip to the previous track on a specified remote device in AudioStation.

        Parameters
        ----------
        device : str
            The ID of the remote device on which to skip to the previous track.

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the status of the operation or a string in case of an error.
        """
        api_name = 'SYNO.AudioStation.RemotePlayer'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'method': 'control', 'id': device,
                     'version': info['maxVersion'], 'action': 'prev'}

        return self.request_data(api_name, api_path, req_param)
