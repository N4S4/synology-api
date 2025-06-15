from __future__ import annotations
from typing import Optional

import synology_api.auth
from . import base_api


class Docker(base_api.BaseApi):

    def containers(self) -> dict[str, object] | str:
        """Get list of containers.

            Returns
            -------
            dict[str, object]
                A dictionary containing the containers information.

            Example return
            --------------
            ```json
            {
                "data": {
                    "1111aaaa-22bb-33cc-44dd-555555eeeeee": {
                        "containerIds": [
                            "21bbe0c6a5d3b246f347367826a78db47f0f334a44bd6621e084f68f0ad63044"
                        ],
                        "created_at": "2025-03-14T14:07:04.874304Z",
                        "enable_service_portal": true,
                        "id": "187b2816-fd6c-4f87-b178-6d94806c7404",
                        "is_package": false,
                        "name": "pihole",
                        "path": "/volume1/docker/test",
                        "service_portal_name": "test",
                        "service_portal_port": 53,
                        "service_portal_protocol": "http",
                        "services": [
                            {
                                "display_name": "test (project)",
                                "id": "Docker-Project-187b2816-fd6c-4f87-b178-6d94806c7404",
                                "proxy_target": "http://127.0.0.1:53",
                                "service": "Docker-Project-187b2816-fd6c-4f87-b178-6d94806c7404",
                                "type": "reverse_proxy"
                            }
                        ],
                        "share_path": "/docker/test",
                        "state": "",
                        "status": "STOPPED",
                        "updated_at": "2025-03-14T15:17:31.840634Z",
                        "version": 2
                    },
                    "2222bbbb-33cc-44dd-55ee-666666ffffff": {
                        "containerIds": [
                            "d9301fc3aa925514760e7714a489cc2d14a26ed6e8169479ac6c356de6b5a7d9",
                            "89d63c6c3c4e299c82c2dcc4ba353c4c1e6c1c938b572153fe9f615646edc4f6",
                            "4a37c7a4a5cab34658071972c2c2bc3ff89dc6dc1407fd98751c7f227574a088",
                            "6df4151b6e24ea3b68b62851d65c8a830e342085f6f9cf0cfdf1e6f98357d9b1",
                            "1a1088cdf8d56e2443c22fa5c6f5658384ba894fe050d82b9214fb84342b0d93",
                            "36984528684d20c775ac67b3a286e48a5aa8ba73a36f58cfd062a8649d457328"
                        ],
                        "created_at": "2024-07-21T11:01:31.019924Z",
                        "enable_service_portal": true,
                        "id": "d787e5ac-1b6a-4dd4-a2d9-35bcd5ad9577",
                        "is_package": false,
                        "name": "test2",
                        "path": "/volume1/docker/test2",
                        "service_portal_name": "test2-server",
                        "service_portal_port": 2283,
                        "service_portal_protocol": "http",
                        "services": [
                            {
                                "display_name": "test2 (project)",
                                "id": "Docker-Project-d787e5ac-1b6a-4dd4-a2d9-35bcd5ad9577",
                                "proxy_target": "http://127.0.0.1:2283",
                                "service": "Docker-Project-d787e5ac-1b6a-4dd4-a2d9-35bcd5ad9577",
                                "type": "reverse_proxy"
                            }
                        ],
                        "share_path": "/docker/test2",
                        "state": "",
                        "status": "ERROR",
                        "updated_at": "2025-06-12T14:48:08.127657Z",
                        "version": 2
                    }
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': '-1', 'offset': '0', 'type': 'all'}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to containers_resources?
    def container_resources(self) -> dict[str, object] | str:
        """Get resources of all containers.

            Returns
            -------
            dict[str, object]
                A dictionary containing the resources information of the containers.

            Example return
            --------------
            ```json
                {
                    "data": {
                        "resources": [
                            {
                                "cpu": 0,
                                "memory": 21106688,
                                "memoryPercent": 0.517403244972229,
                                "name": "container1"
                            },
                            {
                                "cpu": 0,
                                "memory": 0,
                                "memoryPercent": 0,
                                "name": "container2"
                            },
                            {
                                "cpu": 0,
                                "memory": 0,
                                "memoryPercent": 0,
                                "name": "stopped_container"
                            }
                        ]
                    },
                    "httpd_restart": false,
                    "success": true
                }
            ```
        """

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

    def get_logs(self, name : str = None, from_date : str = None, to_date : str = None,
                 level : str = None, keyword : str = None, sort_dir : str = 'DESC', offset : int = 0,
                 limit: int = 1000
                 ) -> dict[str, object] | str:
        """Get list of container logs.

            Parameters
            ----------
            name : str
                The name of the container

            from_date : str, optional
                The start date for the logs. Defaults to None.

            to_date : str, optional
                The end date for the logs. Defaults to None.

            level : str, optional
                The log level to filter by. Defaults to None.

            keyword : str, optional
                Keyword to filter logs. Defaults to None.

            sort_dir : str, optional
                Sort direction for the logs, either 'ASC' or 'DESC'. Defaults to 'DESC'.

            offset : int, optional
                The offset for pagination. Defaults to 0.

            limit : int, optional
                The maximum number of logs to return. Defaults to 1000.

            Returns
            -------
            dict[str, object]
                A dictionary containing the logs from the specified container.

            Example return
            --------------
            ```json
                {
                    "data": {
                        "limit": 1,
                        "logs": [
                            {
                                "created": "2025-06-15T10:38:55.869358659Z",
                                "docid": "1",
                                "stream": "stderr",
                                "text": "2025/06/15 10:38:55 Starting server on :8080 (base-url: \"\", assets-path: \"\")\n"
                            }
                        ],
                        "offset": 0,
                        "total": 1
                    },
                    "success": true
                }
            ```
        """

        api_name = 'SYNO.Docker.Container.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'name': name, 'from': from_date, 'to': to_date, 'level': level, 'keyword': keyword,
                     'sort_dir': sort_dir, 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param, method="post")

    def docker_stats(self) -> dict[str, object] | str:
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stats'}

        return self.request_data(api_name, api_path, req_param)
