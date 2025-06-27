from __future__ import annotations
from io import BytesIO
from zipfile import ZipFile
from typing import Optional
from . import base_api


class VPN(base_api.BaseApi):

    def settings_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status_load'}

        return self.request_data(api_name, api_path, req_param)

    def active_connections_list(self,
                                sort: str = 'login_time',
                                sort_dir: str = 'DESC',
                                start: int = 0,
                                limit: int = 100
                                ) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Management.Connection'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'enum', 'sort': sort, 'dir': sort_dir, 'start': start,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def log_list(self, start: int = 0, limit: int = 50, prtltype: int = 0) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Management.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'start': start, 'limit': limit,
                     'prtltype': prtltype}

        return self.request_data(api_name, api_path, req_param)

    def network_interface_setting(self) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Management.Interface'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load'}

        return self.request_data(api_name, api_path, req_param)

    def security_autoblock_setting(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.Security.AutoBlock'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def permission_setting(self, start: int = 0, limit: int = 100) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Management.Account'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'load', 'action': 'enum', 'start': str(start),
                     'limit': str(limit)}

        return self.request_data(api_name, api_path, req_param)

    def pptp_settings_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'load', 'serv_type': 'pptp'}

        return self.request_data(api_name, api_path, req_param)

    def openvpn_settings_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'load', 'serv_type': 'openvpn'}

        return self.request_data(api_name, api_path, req_param)

    def l2tp_settings_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.VPNServer.Settings.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'load', 'serv_type': 'l2tp'}

        return self.request_data(api_name, api_path, req_param)

    def openvpn_export_configuration(self, as_zip_file=False) -> bytes | ZipFile:
        """Downloads the openvpn\.zip containing the VPNConfig\.ovpn file

            Parameters
            ----------
            as_zip_file : bool
                If the bytes should be converted to a ZipFile

            Returns
            -------
            dict[str, object]
                A dictionary containing the OpenVPN configuration file as bytes or a ZipFile object if `as_zip_file` is True.
        """
        api_name = 'SYNO.VPNServer.Settings.Certificate'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'export', 'serv_type': 'openvpn'}
        zip_as_bytes = self.request_data(
            api_name, api_path, req_param, response_json=False).content
        if as_zip_file:
            return ZipFile(BytesIO(zip_as_bytes))
        return zip_as_bytes
