from __future__ import annotations
from typing import Optional

import synology_api.auth
from . import base_api


class Docker(base_api.BaseApi):

    def containers(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': '-1', 'offset': '0', 'type': 'all'}

        return self.request_data(api_name, api_path, req_param)

    def container_resources(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container.Resource'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def system_resources(self) -> dict[str, object] | str:
        api_name = 'SYNO.Core.System.Utilization'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def downloaded_images(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': '-1', 'offset': '0',
                     "show_dsm": 'false'}

        return self.request_data(api_name, api_path, req_param)

    def images_registry_resources(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    #TODO not working
    def search_image(self, query : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'search', 'offset': 0, 'limit': 50, 'page_size': 50, 'q': query}

        return self.request_data(api_name, api_path, req_param)

    def list_projects(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    #TODO not working with project_id
    def get_project_info(self, project_id : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'name': project_id}

        return self.request_data(api_name, api_path, req_param)

    def start_container(self, container : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    def stop_container(self, container : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    def export_container_settings(self, container : str = None, path : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'export', 'name': container, 'path' : path}

        return self.request_data(api_name, api_path, req_param)

    def export_container(self, container : str = None, path : str = None) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'export', 'name': container, 'path' : path}

        return self.request_data(api_name, api_path, req_param)

    #TODO not working
    def get_logs(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}#, 'action': '"load"', 'offset': 0, 'limit': 1000,
                     #'sort_by': 'time', 'sort_dir': 'DESC', 'datefrom': 0, 'dateto': 0}

        return self.request_data(api_name, api_path, req_param)

    def docker_stats(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stats'}

        return self.request_data(api_name, api_path, req_param)
