from typing import Optional
from . import base_api_core


class Docker(base_api_core.Core):
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
        super(Docker, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug, otp_code)
        return

    def containers(self) -> dict[str, object]:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': '-1', 'offset': '0', 'type': 'all'}

        return self.request_data(api_name, api_path, req_param)

    def container_resources(self) -> dict[str, object]:
        api_name = 'SYNO.Docker.Container.Resource'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def system_resources(self) -> dict[str, object]:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def downloaded_images(self) -> dict[str, object]:
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': '-1', 'offset': '0',
                     "show_dsm": 'false'}

        return self.request_data(api_name, api_path, req_param)

    def images_registry_resources(self) -> dict[str, object]:
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network(self) -> dict[str, object]:
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
