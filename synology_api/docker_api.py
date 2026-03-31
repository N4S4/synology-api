"""
Docker API implementation for Synology NAS.

Provides full coverage of all 12 SYNO.Docker.* API endpoints:
    - SYNO.Docker.Container       — Container lifecycle (list, get, start, stop, restart, delete, create, signal, export, stats)
    - SYNO.Docker.Container.Log   — Per-container log retrieval
    - SYNO.Docker.Container.PkgProfile — Package-managed container profiles
    - SYNO.Docker.Container.Profile    — Container profile export/import
    - SYNO.Docker.Container.Resource   — Container resource usage
    - SYNO.Docker.Image           — Image management (list, pull, delete, export, import)
    - SYNO.Docker.Log             — Docker daemon / global logs
    - SYNO.Docker.Migrate         — Migration utilities
    - SYNO.Docker.Network         — Network management (list, create, delete)
    - SYNO.Docker.Project         — Compose project management (list, get, create, update, start, stop, delete, build)
    - SYNO.Docker.Registry        — Registry management (get, set, create, delete, search, tags, using)
    - SYNO.Docker.Utils           — Docker utility operations
"""
from __future__ import annotations
from typing import Optional
import json

import synology_api.auth
from . import base_api


class Docker(base_api.BaseApi):
    """
    Docker API implementation.

    Provides methods to interact with Docker containers, images, registries,
    networks, projects, logs, migration, and utilities on a Synology NAS.

    Covers all 12 ``SYNO.Docker.*`` API namespaces exposed by DSM.
    """

    def containers(self) -> dict[str, object] | str:
        """
        Get list of containers.

            Returns
            -------
            dict[str, object]
                A dictionary containing the containers information.

            Examples
            --------
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
        req_param = {'version': info['maxVersion'], 'method': 'list',
                     'limit': '-1', 'offset': '0', 'type': 'all'}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to containers_resources?

    def container_resources(self) -> dict[str, object] | str:
        """
        Get resources of all containers.

            Returns
            -------
            dict[str, object]
                A dictionary containing the resources information of the containers.

            Examples
            --------
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

    # TODO: move to code_sys_utilization?
    def system_resources(self) -> dict[str, object] | str:
        """
        Get system resources.

            Returns
            -------
            dict[str, object]
                A dictionary containing the system resources information.

            Examples
            --------
            ```json
            {
               "data" : {
                  "cpu" : {
                     "15min_load" : 14,
                     "1min_load" : 29,
                     "5min_load" : 16,
                     "device" : "System",
                     "other_load" : 2,
                     "system_load" : 0,
                     "user_load" : 1
                  },
                  "disk" : {
                     "disk" : [
                        {
                           "device" : "sata2",
                           "display_name" : "Drive 2",
                           "read_access" : 0,
                           "read_byte" : 0,
                           "type" : "internal",
                           "utilization" : 0,
                           "write_access" : 0,
                           "write_byte" : 0
                        },
                        {
                           "device" : "sata1",
                           "display_name" : "Drive 1",
                           "read_access" : 0,
                           "read_byte" : 0,
                           "type" : "internal",
                           "utilization" : 0,
                           "write_access" : 0,
                           "write_byte" : 0
                        }
                     ],
                     "total" : {
                        "device" : "total",
                        "read_access" : 0,
                        "read_byte" : 0,
                        "utilization" : 0,
                        "write_access" : 0,
                        "write_byte" : 0
                     }
                  },
                  "lun" : [],
                  "memory" : {
                     "avail_real" : 444840,
                     "avail_swap" : 4163752,
                     "buffer" : 21716,
                     "cached" : 2658180,
                     "device" : "Memory",
                     "memory_size" : 4194304,
                     "real_usage" : 21,
                     "si_disk" : 0,
                     "so_disk" : 0,
                     "swap_usage" : 7,
                     "total_real" : 3983740,
                     "total_swap" : 4489140
                  },
                  "network" : [
                     {
                        "device" : "total",
                        "rx" : 6822,
                        "tx" : 6336
                     },
                     {
                        "device" : "eth0",
                        "rx" : 0,
                        "tx" : 0
                     },
                     {
                        "device" : "eth1",
                        "rx" : 0,
                        "tx" : 0
                     },
                     {
                        "device" : "eth2",
                        "rx" : 6822,
                        "tx" : 6336
                     }
                  ],
                  "nfs" : [],
                  "smb" : {
                     "smb_cmd" : [],
                     "smb_cpu" : [],
                     "smb_rwpkt" : []
                  },
                  "space" : {
                     "total" : {
                        "device" : "total",
                        "read_access" : 0,
                        "read_byte" : 0,
                        "utilization" : 0,
                        "write_access" : 0,
                        "write_byte" : 0
                     },
                     "volume" : [
                        {
                           "device" : "dm-1",
                           "display_name" : "volume1",
                           "read_access" : 0,
                           "read_byte" : 0,
                           "utilization" : 0,
                           "write_access" : 0,
                           "write_byte" : 0
                        }
                     ]
                  },
                  "time" : 1749998465
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Core.System.Utilization'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to list_downloaded_images?
    def downloaded_images(self, limit: int = -1, offset: int = 0, show_dsm: bool = False) -> dict[str, object] | str:
        """
        List of docker images available on Synology NAS.

            Parameters
            ----------
            limit : int, optional
                The maximum number of docker images to return. Defaults -1 (all).

            offset : int, optional
                The offset for pagination. Defaults to 0.

            show_dsm : bool, optional
                Defaults to False.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of downloaded images.

            Examples
            --------
            ```json
            {
               "data" : {
                  "images" : [
                     {
                        "created" : 1745034718,
                        "description" : "",
                        "digest" : "",
                        "id" : "sha256:14300de7e087290520999f00d6a12b61385d1fe780ea83f38eabb7e8be66225f",
                        "remote_digest" : "",
                        "repository" : "caddy",
                        "size" : 50509416,
                        "tags" : [ "alpine" ],
                        "upgradable" : false,
                        "virtual_size" : 50509416
                     }
                  ],
                  "limit" : 1,
                  "offset" : 0,
                  "total" : 1
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'limit': limit, 'offset': offset,
                     "show_dsm": json.dumps(show_dsm)}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to list_registries?
    def images_registry_resources(self) -> dict[str, object] | str:
        """
        Get list of docker registries.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of docker registries.

            Examples
            --------
            ```json
            {
               "data" : {
                  "offset" : 0,
                  "registries" : [
                     {
                        "enable_registry_mirror" : false,
                        "enable_trust_SSC" : true,
                        "mirror_urls" : [],
                        "name" : "Docker Hub",
                        "syno" : true,
                        "url" : "https://registry.hub.docker.com"
                     }
                  ],
                  "total" : 1,
                  "using" : "Docker Hub"
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def network(self) -> dict[str, object] | str:
        """
        Get list of docker networks.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of docker networks.

            Examples
            --------
            ```json
            {
               "data" : {
                  "network" : [
                     {
                        "containers" : [ "vault" ],
                        "driver" : "bridge",
                        "enable_ipv6" : false,
                        "gateway" : "172.22.0.1",
                        "id" : "b741915823aacdffc8ab806ab348e198c2c486b4dd5df2627b0d586259926b1a",
                        "iprange" : "",
                        "name" : "vault_default",
                        "subnet" : "172.22.0.0/16"
                     },
                     {
                        "containers" : [],
                        "driver" : "host",
                        "enable_ipv6" : false,
                        "gateway" : "",
                        "id" : "2fc7ebae3901359e7bc9d7b50fad1f6aa2f8c1076474cadc9f83b3256f921ff3",
                        "iprange" : "",
                        "name" : "host",
                        "subnet" : ""
                     }
                  ]
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename search_images_in_registries?
    def search_image(self, query: str = None) -> dict[str, object] | str:
        """
        Search for docker image in all available registries.

            Parameters
            ----------
            query : str
                Name of the docker image to search for. Defaults to None.

            Returns
            -------
            dict[str, object]
                A dictionary containing the search results for the docker image.

            Examples
            --------
            ```json
            {
               "data" : {
                  "data" : [
                     {
                        "description" : "Caddy 2 is a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go.",
                        "downloads" : 650989718,
                        "is_automated" : false,
                        "is_official" : true,
                        "name" : "caddy",
                        "registry" : "https://registry.hub.docker.com",
                        "star_count" : 881
                     },
                     {
                        "description" : "Caddy is a lightweight, general-purpose web server.",
                        "downloads" : 111974910,
                        "is_automated" : true,
                        "is_official" : false,
                        "name" : "abiosoft/caddy",
                        "registry" : "https://registry.hub.docker.com",
                        "star_count" : 289
                     }
                  ],
                  "limit" : 50,
                  "offset" : 0,
                  "page_size" : 50,
                  "total" : 6647
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        # version 1 contains methods: search, tags, get, create, set, using, delete
        # version 2 contains methods: tags
        req_param = {'version': 1, 'method': 'search',
                     'offset': 0, 'limit': 50, 'page_size': 50, 'q': query}

        return self.request_data(api_name, api_path, req_param)

    def list_projects(self) -> dict[str, object] | str:
        """
        Get list of projects.

            Returns
            -------
            dict[str, object]
                A dictionary containing the list of projects.

            Examples
            --------
            ```json
            {
               "data" : {
                  "187b2816-fd6c-4f87-b178-6d94806c7404" : {
                     "containerIds" : [ "21bbe0c6a5d3b246f347367826a78db47f0f334a44bd6621e084f68f0ad63044" ],
                     "created_at" : "2025-03-14T14:07:04.874304Z",
                     "enable_service_portal" : true,
                     "id" : "187b2816-fd6c-4f87-b178-6d94806c7404",
                     "is_package" : false,
                     "name" : "project1",
                     "path" : "/volume1/docker/project1",
                     "service_portal_name" : "project1",
                     "service_portal_port" : 53,
                     "service_portal_protocol" : "http",
                     "services" : [
                        {
                           "display_name" : "project1 (project)",
                           "id" : "Docker-Project-187b2816-fd6c-4f87-b178-6d94806c7404",
                           "proxy_target" : "http://127.0.0.1:53",
                           "service" : "Docker-Project-187b2816-fd6c-4f87-b178-6d94806c7404",
                           "type" : "reverse_proxy"
                        }
                     ],
                     "share_path" : "/docker/project1",
                     "state" : "",
                     "status" : "STOPPED",
                     "updated_at" : "2025-03-14T15:17:31.840634Z",
                     "version" : 2
                  },
                  "3c091e8b-f68f-4161-97a3-fc3db3f4bdc9" : {
                     "containerIds" : [ "ee220111cff2d2e7b9d764a4b781f9e23faa3cd7f3048d315aa6c95d48f0a1e4" ],
                     "created_at" : "2025-05-27T08:33:03.213407Z",
                     "enable_service_portal" : false,
                     "id" : "3c091e8b-f68f-4161-97a3-fc3db3f4bdc9",
                     "is_package" : false,
                     "name" : "project2",
                     "path" : "/volume1/docker/project2",
                     "service_portal_name" : "",
                     "service_portal_port" : 0,
                     "service_portal_protocol" : "",
                     "services" : [],
                     "share_path" : "/docker/project2",
                     "state" : "",
                     "status" : "RUNNING",
                     "updated_at" : "2025-06-15T10:38:52.247951Z",
                     "version" : 2
                  }
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_project_info(self, project_id: str = None) -> dict[str, object] | str:
        """
        Get information about a specific project.

            Parameters
            ----------
            project_id : str
                ID of the project to get information about. Defaults to None.

            Returns
            -------
            dict[str, object]
                A dictionary containing the project information.

            Examples
            --------
            ```json
            {
               "data" : {
                  "containerIds" : [ "1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf" ],
                  "containers" : [
                     {
                        "AppArmorProfile" : "docker-default",
                        "Args" : [ "server", "-config=/vault/file/" ],
                        "Config" : {
                           "AttachStderr" : true,
                           "AttachStdin" : false,
                           "AttachStdout" : true,
                           "Cmd" : null,
                           "Domainname" : "",
                           "Entrypoint" : [ "vault", "server", "-config=/vault/file/" ],
                           "Env" : [
                              "VAULT_RAFT_PATH=/vault/file",
                              "VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200",
                              "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                              "NAME=vault",
                              "VERSION="
                           ],
                           "ExposedPorts" : {
                              "8200/tcp" : {}
                           },
                           "Healthcheck" : {
                              "Interval" : 30000000000,
                              "Retries" : 5,
                              "Test" : [ "CMD", "vault", "status" ],
                              "Timeout" : 10000000000
                           },
                           "Hostname" : "vault",
                           "Image" : "hashicorp/vault:latest",
                           "Labels" : {
                              "com.docker.compose.config-hash" : "6a08fb0e6d57f8ad25b3d78cac40d369be831be5cf98406520e514d68aa03251",
                              "com.docker.compose.container-number" : "1",
                              "com.docker.compose.depends_on" : "",
                              "com.docker.compose.image" : "sha256:2006f053b116f3a57dad1d8fff9d19c13f3e801e594dcbd58e219d4ccb654337",
                              "com.docker.compose.oneoff" : "False",
                              "com.docker.compose.project" : "vault",
                              "com.docker.compose.project.config_files" : "/volume1/docker/vault/compose.yaml",
                              "com.docker.compose.project.working_dir" : "/volume1/docker/vault",
                              "com.docker.compose.replace" : "1153d033ece9eb4242926f805a211daed65922652fdf73ffcf8147e20e4c0ce2",
                              "com.docker.compose.service" : "vault",
                              "com.docker.compose.version" : "2.20.1",
                              "description" : "Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.",
                              "maintainer" : "Vault Team <vault@hashicorp.com>",
                              "name" : "Vault",
                              "release" : "322786e236e268532e4b189845971ba67b5cbb23",
                              "revision" : "322786e236e268532e4b189845971ba67b5cbb23",
                              "summary" : "Vault is a tool for securely accessing secrets.",
                              "vendor" : "HashiCorp",
                              "version" : "1.19.4"
                           },
                           "OnBuild" : null,
                           "OpenStdin" : false,
                           "StdinOnce" : false,
                           "Tty" : false,
                           "User" : "",
                           "Volumes" : {
                              "/vault/file" : {},
                              "/vault/logs" : {}
                           },
                           "WorkingDir" : "/"
                        },
                        "Created" : "2025-05-25T17:57:06.296933361Z",
                        "Driver" : "btrfs",
                        "ExecIDs" : null,
                        "GraphDriver" : {
                           "Data" : null,
                           "Name" : "btrfs"
                        },
                        "HostConfig" : {
                           "AutoRemove" : false,
                           "Binds" : [
                              "/volume1/docker/vault/data:/vault/file:rw",
                              "/volume1/docker/vault/logs:/vault/logs:rw",
                              "/volume1/docker/vault/config:/vault/config:rw",
                              "/volume1/docker/vault/plugins:/vault/plugins:rw",
                              "/etc/localtime:/etc/localtime:ro"
                           ],
                           "BlkioDeviceReadBps" : null,
                           "BlkioDeviceReadIOps" : null,
                           "BlkioDeviceWriteBps" : null,
                           "BlkioDeviceWriteIOps" : null,
                           "BlkioWeight" : 0,
                           "BlkioWeightDevice" : null,
                           "CapAdd" : [ "IPC_LOCK" ],
                           "CapDrop" : null,
                           "Cgroup" : "",
                           "CgroupParent" : "",
                           "CgroupnsMode" : "host",
                           "ConsoleSize" : [ 0, 0 ],
                           "ContainerIDFile" : "",
                           "CpuCount" : 0,
                           "CpuPercent" : 0,
                           "CpuPeriod" : 0,
                           "CpuQuota" : 0,
                           "CpuRealtimePeriod" : 0,
                           "CpuRealtimeRuntime" : 0,
                           "CpuShares" : 768,
                           "CpusetCpus" : "",
                           "CpusetMems" : "",
                           "DeviceCgroupRules" : null,
                           "DeviceRequests" : null,
                           "Devices" : null,
                           "Dns" : [],
                           "DnsOptions" : [],
                           "DnsSearch" : [],
                           "ExtraHosts" : [],
                           "GroupAdd" : null,
                           "IOMaximumBandwidth" : 0,
                           "IOMaximumIOps" : 0,
                           "IpcMode" : "private",
                           "Isolation" : "",
                           "Links" : null,
                           "LogConfig" : {
                              "Config" : {},
                              "Type" : "db"
                           },
                           "MaskedPaths" : [
                              "/proc/asound",
                              "/proc/acpi",
                              "/proc/kcore",
                              "/proc/keys",
                              "/proc/latency_stats",
                              "/proc/timer_list",
                              "/proc/timer_stats",
                              "/proc/sched_debug",
                              "/proc/scsi",
                              "/sys/firmware"
                           ],
                           "Memory" : 536870912,
                           "MemoryReservation" : 0,
                           "MemorySwap" : 1073741824,
                           "MemorySwappiness" : null,
                           "NanoCpus" : 0,
                           "NetworkMode" : "vault_default",
                           "OomKillDisable" : false,
                           "OomScoreAdj" : 0,
                           "PidMode" : "",
                           "PidsLimit" : null,
                           "PortBindings" : {
                              "8200/tcp" : [
                                 {
                                    "HostIp" : "",
                                    "HostPort" : "8205"
                                 }
                              ]
                           },
                           "Privileged" : false,
                           "PublishAllPorts" : false,
                           "ReadonlyPaths" : [
                              "/proc/bus",
                              "/proc/fs",
                              "/proc/irq",
                              "/proc/sys",
                              "/proc/sysrq-trigger"
                           ],
                           "ReadonlyRootfs" : false,
                           "RestartPolicy" : {
                              "MaximumRetryCount" : 5,
                              "Name" : "on-failure"
                           },
                           "Runtime" : "runc",
                           "SecurityOpt" : [ "no-new-privileges:true" ],
                           "ShmSize" : 67108864,
                           "UTSMode" : "",
                           "Ulimits" : null,
                           "UsernsMode" : "",
                           "VolumeDriver" : "",
                           "VolumesFrom" : null
                        },
                        "HostnamePath" : "/volume1/@docker/containers/1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf/hostname",
                        "HostsPath" : "/volume1/@docker/containers/1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf/hosts",
                        "Id" : "1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf",
                        "Image" : "sha256:2006f053b116f3a57dad1d8fff9d19c13f3e801e594dcbd58e219d4ccb654337",
                        "LogPath" : "/volume1/@docker/containers/1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf/log.db",
                        "MountLabel" : "",
                        "Mounts" : [
                           {
                              "Destination" : "/vault/plugins",
                              "Mode" : "rw",
                              "Propagation" : "rprivate",
                              "RW" : true,
                              "Source" : "/volume1/docker/vault/plugins",
                              "Type" : "bind"
                           },
                           {
                              "Destination" : "/etc/localtime",
                              "Mode" : "ro",
                              "Propagation" : "rprivate",
                              "RW" : false,
                              "Source" : "/etc/localtime",
                              "Type" : "bind"
                           },
                           {
                              "Destination" : "/vault/config",
                              "Mode" : "rw",
                              "Propagation" : "rprivate",
                              "RW" : true,
                              "Source" : "/volume1/docker/vault/config",
                              "Type" : "bind"
                           },
                           {
                              "Destination" : "/vault/file",
                              "Mode" : "rw",
                              "Propagation" : "rprivate",
                              "RW" : true,
                              "Source" : "/volume1/docker/vault/data",
                              "Type" : "bind"
                           },
                           {
                              "Destination" : "/vault/logs",
                              "Mode" : "rw",
                              "Propagation" : "rprivate",
                              "RW" : true,
                              "Source" : "/volume1/docker/vault/logs",
                              "Type" : "bind"
                           }
                        ],
                        "Name" : "/vault",
                        "NetworkSettings" : {
                           "Bridge" : "",
                           "EndpointID" : "",
                           "Gateway" : "",
                           "GlobalIPv6Address" : "",
                           "GlobalIPv6PrefixLen" : 0,
                           "HairpinMode" : false,
                           "IPAddress" : "",
                           "IPPrefixLen" : 0,
                           "IPv6Gateway" : "",
                           "LinkLocalIPv6Address" : "",
                           "LinkLocalIPv6PrefixLen" : 0,
                           "MacAddress" : "",
                           "Networks" : {
                              "vault_default" : {
                                 "Aliases" : [ "vault", "vault", "1f2aa674d794" ],
                                 "DriverOpts" : null,
                                 "EndpointID" : "",
                                 "Gateway" : "",
                                 "GlobalIPv6Address" : "",
                                 "GlobalIPv6PrefixLen" : 0,
                                 "IPAMConfig" : null,
                                 "IPAddress" : "",
                                 "IPPrefixLen" : 0,
                                 "IPv6Gateway" : "",
                                 "Links" : null,
                                 "MacAddress" : "",
                                 "NetworkID" : "b741915823aacdffc8ab806ab348e198c2c486b4dd5df2627b0d586259926b1a"
                              }
                           },
                           "Ports" : {},
                           "SandboxID" : "d523ddff9d90b2ecc74f20c33db7b4898fa2869f10899ccc6567febd64d7142c",
                           "SandboxKey" : "/var/run/docker/netns/d523ddff9d90",
                           "SecondaryIPAddresses" : null,
                           "SecondaryIPv6Addresses" : null
                        },
                        "Path" : "vault",
                        "Platform" : "linux",
                        "ProcessLabel" : "",
                        "ResolvConfPath" : "/volume1/@docker/containers/1f2aa674d7942c25789c144c1e4ea04388e5a914e1ed3d7a1b8978f8f2f81ebf/resolv.conf",
                        "RestartCount" : 5,
                        "State" : {
                           "Dead" : false,
                           "Error" : "",
                           "ExitCode" : 1,
                           "FinishedAt" : "2025-05-25T17:57:30.266770048Z",
                           "Health" : {
                              "FailingStreak" : 0,
                              "Log" : [],
                              "Status" : "unhealthy"
                           },
                           "OOMKilled" : false,
                           "Paused" : false,
                           "Pid" : 0,
                           "Restarting" : false,
                           "Running" : false,
                           "StartedAt" : "2025-05-25T17:57:30.184237615Z",
                           "Status" : "exited"
                        }
                     }
                  ],
                  "content" : "docker-compose.yml contet",
                  "created_at" : "2025-05-25T17:31:00.875402Z",
                  "enable_service_portal" : false,
                  "id" : "b4d44e6c-5ab4-45f7-b380-481ef9839df1",
                  "is_package" : false,
                  "name" : "vault",
                  "path" : "/volume1/docker/vault",
                  "service_portal_name" : "",
                  "service_portal_port" : 0,
                  "service_portal_protocol" : "",
                  "services" : null,
                  "share_path" : "/docker/vault",
                  "state" : "",
                  "status" : "STOPPED",
                  "updated_at" : "2025-05-25T17:57:06.257863Z",
                  "version" : 2
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'id': project_id}

        return self.request_data(api_name, api_path, req_param)

    def start_container(self, container: str = None) -> dict[str, object] | str:
        """
        Start a container by its name.

            Parameters
            ----------
            container : str
                The name of the container.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Examples
            --------
            ```json
            {
               "data" : {
                  "cpu" : 0,
                  "memory" : 21241856,
                  "memoryPercent" : 0.52071672677993774,
                  "name" : "glance",
                  "start_dependent_container" : false
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'start', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    def stop_container(self, container: str = None) -> dict[str, object] | str:
        """
        Stop a container by its name.

            Parameters
            ----------
            container : str
                The name of the container.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the stop operation.

            Examples
            --------
            ```json
            {
               "data" : {
                  "cpu" : 0,
                  "memory" : 0,
                  "memoryPercent" : 0,
                  "name" : "glance"
               },
               "httpd_restart" : false,
               "success" : true
            }
            ```
        """

        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to export_container_profile?
    def export_container_settings(self, container: str = None, path: str = None) -> dict[str, object] | str:
        """
        Export container profile.

            file \\<container\\>.syno.json will be created in the specified path.

            Parameters
            ----------
            container : str
                The name of the container.

            path : str, optional
                The path on filesystem of Synology NAS where the container settings will be exported.
                If not specified, the file will be offered as a download through the browser.
                For example: `/docker/nging`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Examples
            --------
            ```json
                {
                   "data" : {},
                   "httpd_restart" : false,
                   "success" : true
                }
            ```
        """
        api_name = 'SYNO.Docker.Container.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'export', 'name': container, 'path': path}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to export_container_profile_and_content?
    def export_container(self, container: str = None, path: str = None) -> dict[str, object] | str:
        """
        Export container profile and content to a specified path on Synology nas.

            archive \\<container\\>.syno.txz will be created in the specified path.

            Parameters
            ----------
            container : str
                The name of the container.

            path : str
                The path on filesystem of Synology NAS where the container settings will be exported.
                For example: `/docker/nging`.

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Examples
            --------
            ```json
                {
                   "data" : {},
                   "httpd_restart" : false,
                   "success" : true
                }
            ```
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'export', 'name': container, 'path': path}

        return self.request_data(api_name, api_path, req_param)

    def get_logs(self, name: str = None, from_date: str = None, to_date: str = None,
                 level: str = None, keyword: str = None, sort_dir: str = 'DESC', offset: int = 0,
                 limit: int = 1000
                 ) -> dict[str, object] | str:
        """
        Get list of container logs.

            Parameters
            ----------
            name : str
                The name of the container.

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

            Examples
            --------
            ```json
                {
                    "data": {
                        "limit": 1,
                        "logs": [
                            {
                                "created": "2025-06-15T10:38:55.869358659Z",
                                "docid": "1",
                                "stream": "stderr",
                                "text": "2025/06/15 10:38:55 Starting server on :8080"
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
        """
        Get containers resource usage statistics.

            Returns
            -------
            dict[str, object]
                A dictionary containing the resource usage statistics of the containers.

            Examples
            --------
            ```json
                {
                   "data" : {
                      "ee220111cff2d2e7b9d764a4b781f9e23faa3cd7f3048d315aa6c95d48f0a1e4" : {
                         "blkio_stats" : {
                            "io_merged_recursive" : [],
                            "io_queue_recursive" : [],
                            "io_service_bytes_recursive" : [],
                            "io_service_time_recursive" : [],
                            "io_serviced_recursive" : [],
                            "io_time_recursive" : [],
                            "io_wait_time_recursive" : [],
                            "sectors_recursive" : []
                         },
                         "cpu_stats" : {
                            "cpu_usage" : {
                               "percpu_usage" : [ 286394951, 245078386, 304613157, 186566695 ],
                               "total_usage" : 1022653189,
                               "usage_in_kernelmode" : 380000000,
                               "usage_in_usermode" : 580000000
                            },
                            "online_cpus" : 4,
                            "system_cpu_usage" : 990015100000000,
                            "throttling_data" : {
                               "periods" : 0,
                               "throttled_periods" : 0,
                               "throttled_time" : 0
                            }
                         },
                         "id" : "ee220111cff2d2e7b9d764a4b781f9e23faa3cd7f3048d315aa6c95d48f0a1e4",
                         "memory_stats" : {
                            "limit" : 4079349760,
                            "max_usage" : 22630400,
                            "stats" : {
                               "active_anon" : 5500928,
                               "active_file" : 1294336,
                               "cache" : 15626240,
                               "dirty" : 0,
                               "hierarchical_memory_limit" : 9223372036854771712,
                               "hierarchical_memsw_limit" : 9223372036854771712,
                               "inactive_anon" : 0,
                               "inactive_file" : 14331904,
                               "mapped_file" : 11005952,
                               "pgfault" : 43383,
                               "pgmajfault" : 6,
                               "pgpgin" : 33405,
                               "pgpgout" : 28247,
                               "rss" : 5500928,
                               "rss_huge" : 0,
                               "total_active_anon" : 5500928,
                               "total_active_file" : 1294336,
                               "total_cache" : 15626240,
                               "total_dirty" : 0,
                               "total_inactive_anon" : 0,
                               "total_inactive_file" : 14331904,
                               "total_mapped_file" : 11005952,
                               "total_pgfault" : 43383,
                               "total_pgmajfault" : 6,
                               "total_pgpgin" : 33405,
                               "total_pgpgout" : 28247,
                               "total_rss" : 5500928,
                               "total_rss_huge" : 0,
                               "total_unevictable" : 0,
                               "total_writeback" : 0,
                               "unevictable" : 0,
                               "writeback" : 0
                            },
                            "usage" : 21127168
                         },
                         "name" : "/glance",
                         "networks" : {
                            "eth0" : {
                               "rx_bytes" : 876,
                               "rx_dropped" : 0,
                               "rx_errors" : 0,
                               "rx_packets" : 10,
                               "tx_bytes" : 0,
                               "tx_dropped" : 0,
                               "tx_errors" : 0,
                               "tx_packets" : 0
                            }
                         },
                         "num_procs" : 0,
                         "pids_stats" : {},
                         "precpu_stats" : {
                            "cpu_usage" : {
                               "total_usage" : 0,
                               "usage_in_kernelmode" : 0,
                               "usage_in_usermode" : 0
                            },
                            "throttling_data" : {
                               "periods" : 0,
                               "throttled_periods" : 0,
                               "throttled_time" : 0
                            }
                         },
                         "preread" : "0001-01-01T00:00:00Z",
                         "read" : "2025-06-15T14:11:00.431111646Z",
                         "storage_stats" : {}
                      }
                   },
                   "httpd_restart" : false,
                   "success" : true
                }

            ```
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stats'}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Container — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def get_container(self, name: str) -> dict[str, object] | str:
        """
        Get detailed information about a single container.

        Parameters
        ----------
        name : str
            The name of the container.

        Returns
        -------
        dict[str, object]
            Detailed container inspect data (Config, HostConfig, State, etc.).
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def restart_container(self, container: str) -> dict[str, object] | str:
        """
        Restart a container by name.

        Parameters
        ----------
        container : str
            The name of the container to restart.

        Returns
        -------
        dict[str, object]
            Result of the restart operation.
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'restart', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    def delete_container(self, name: str, force: bool = False) -> dict[str, object] | str:
        """
        Delete a container.

        Parameters
        ----------
        name : str
            The name of the container to delete.
        force : bool, optional
            Force-remove a running container. Defaults to False.

        Returns
        -------
        dict[str, object]
            Result of the delete operation.
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'delete', 'name': name,
                     'force': json.dumps(force)}

        return self.request_data(api_name, api_path, req_param)

    def create_container(self, profile: dict) -> dict[str, object] | str:
        """
        Create a new container from a profile definition.

        Parameters
        ----------
        profile : dict
            A container profile dictionary containing image, name, port
            bindings, volume mounts, environment variables, etc.
            Matches the JSON format produced by ``export_container_settings``.

        Returns
        -------
        dict[str, object]
            Result of the creation, including the new container name.
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'create',
                     'profile': json.dumps(profile)}

        return self.request_data(api_name, api_path, req_param, method='post')

    def signal_container(self, name: str, signal: int = 15) -> dict[str, object] | str:
        """
        Send a signal to a running container.

        Parameters
        ----------
        name : str
            The name of the container.
        signal : int, optional
            Unix signal number to send. Defaults to 15 (SIGTERM).

        Returns
        -------
        dict[str, object]
            Result of the signal operation.
        """
        api_name = 'SYNO.Docker.Container'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'signal', 'name': name, 'signal': signal}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Container.PkgProfile  (NEW — package-managed profiles)
    # ──────────────────────────────────────────────────────────────────────

    def get_pkg_profile(self, name: str) -> dict[str, object] | str:
        """
        Get the profile of a package-managed container.

        Package-managed containers are created by Synology packages
        (e.g. Surveillance Station, MailPlus) rather than by users directly.

        Parameters
        ----------
        name : str
            The name of the package-managed container.

        Returns
        -------
        dict[str, object]
            The package profile definition for the container.
        """
        api_name = 'SYNO.Docker.Container.PkgProfile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def list_pkg_profiles(self) -> dict[str, object] | str:
        """
        List all package-managed container profiles.

        Returns
        -------
        dict[str, object]
            A list of all package-managed container profiles.
        """
        api_name = 'SYNO.Docker.Container.PkgProfile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Container.Profile — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def get_container_profile(self, name: str) -> dict[str, object] | str:
        """
        Get the full profile/configuration of a container.

        Parameters
        ----------
        name : str
            The name of the container.

        Returns
        -------
        dict[str, object]
            The full container profile (image, ports, volumes, env, etc.).
        """
        api_name = 'SYNO.Docker.Container.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def import_container_profile(self, name: str, profile: dict) -> dict[str, object] | str:
        """
        Import / apply a profile to a container.

        Parameters
        ----------
        name : str
            The name of the container to update.
        profile : dict
            The profile dictionary to apply.

        Returns
        -------
        dict[str, object]
            Result of the import operation.
        """
        api_name = 'SYNO.Docker.Container.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'import', 'name': name,
                     'profile': json.dumps(profile)}

        return self.request_data(api_name, api_path, req_param, method='post')

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Image — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def pull_image(self, repository: str, tag: str = 'latest') -> dict[str, object] | str:
        """
        Pull a Docker image from the active registry.

        Parameters
        ----------
        repository : str
            The repository name (e.g. ``"nginx"``, ``"grafana/grafana"``).
        tag : str, optional
            The image tag to pull. Defaults to ``"latest"``.

        Returns
        -------
        dict[str, object]
            Result of the pull operation.
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'pull', 'repository': repository, 'tag': tag}

        return self.request_data(api_name, api_path, req_param)

    def delete_image(self, name: str, tag: str = 'latest') -> dict[str, object] | str:
        """
        Delete a local Docker image.

        Parameters
        ----------
        name : str
            The repository name (e.g. ``"nginx"``).
        tag : str, optional
            The image tag to delete. Defaults to ``"latest"``.

        Returns
        -------
        dict[str, object]
            Result of the delete operation.
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'delete', 'name': name, 'tag': tag}

        return self.request_data(api_name, api_path, req_param)

    def export_image(self, name: str, tag: str = 'latest',
                     path: str = '/docker') -> dict[str, object] | str:
        """
        Export a Docker image to a tar archive on the NAS.

        Parameters
        ----------
        name : str
            The repository name.
        tag : str, optional
            The image tag. Defaults to ``"latest"``.
        path : str, optional
            Destination path on the NAS. Defaults to ``"/docker"``.

        Returns
        -------
        dict[str, object]
            Result of the export operation.
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'export', 'name': name, 'tag': tag, 'path': path}

        return self.request_data(api_name, api_path, req_param)

    def import_image(self, path: str) -> dict[str, object] | str:
        """
        Import a Docker image from a tar archive on the NAS.

        Parameters
        ----------
        path : str
            Path to the image archive on the NAS filesystem
            (e.g. ``"/docker/nginx_latest.tar"``).

        Returns
        -------
        dict[str, object]
            Result of the import operation.
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'import', 'path': path}

        return self.request_data(api_name, api_path, req_param, method='post')

    def get_image(self, name: str, tag: str = 'latest') -> dict[str, object] | str:
        """
        Get detailed information about a local Docker image.

        Parameters
        ----------
        name : str
            The repository name.
        tag : str, optional
            The image tag. Defaults to ``"latest"``.

        Returns
        -------
        dict[str, object]
            Detailed image metadata.
        """
        api_name = 'SYNO.Docker.Image'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'name': name, 'tag': tag}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Registry — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def create_registry(self, name: str, url: str,
                        username: Optional[str] = None,
                        password: Optional[str] = None,
                        enable_trust_ssc: bool = True) -> dict[str, object] | str:
        """
        Add a new Docker registry.

        Parameters
        ----------
        name : str
            Display name for the registry.
        url : str
            Registry URL (e.g. ``"https://ghcr.io"``).
        username : str, optional
            Authentication username.
        password : str, optional
            Authentication password.
        enable_trust_ssc : bool, optional
            Trust self-signed certificates. Defaults to True.

        Returns
        -------
        dict[str, object]
            Result of the create operation.
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'create',
                     'name': name, 'url': url,
                     'enable_trust_SSC': json.dumps(enable_trust_ssc)}
        if username is not None:
            req_param['username'] = username
        if password is not None:
            req_param['password'] = password

        return self.request_data(api_name, api_path, req_param)

    def set_registry(self, name: str, url: str,
                     username: Optional[str] = None,
                     password: Optional[str] = None,
                     enable_trust_ssc: bool = True) -> dict[str, object] | str:
        """
        Update an existing Docker registry configuration.

        Parameters
        ----------
        name : str
            Display name of the registry to update.
        url : str
            Registry URL.
        username : str, optional
            Authentication username.
        password : str, optional
            Authentication password.
        enable_trust_ssc : bool, optional
            Trust self-signed certificates. Defaults to True.

        Returns
        -------
        dict[str, object]
            Result of the update operation.
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'set',
                     'name': name, 'url': url,
                     'enable_trust_SSC': json.dumps(enable_trust_ssc)}
        if username is not None:
            req_param['username'] = username
        if password is not None:
            req_param['password'] = password

        return self.request_data(api_name, api_path, req_param)

    def delete_registry(self, name: str) -> dict[str, object] | str:
        """
        Remove a Docker registry.

        Parameters
        ----------
        name : str
            The display name of the registry to remove.

        Returns
        -------
        dict[str, object]
            Result of the delete operation.
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'delete', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def set_using_registry(self, name: str) -> dict[str, object] | str:
        """
        Set the active (default) Docker registry.

        Parameters
        ----------
        name : str
            The display name of the registry to make active.

        Returns
        -------
        dict[str, object]
            Result of the operation.
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'using', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def get_image_tags(self, repository: str, offset: int = 0,
                       limit: int = 50) -> dict[str, object] | str:
        """
        List available tags for an image in the registry.

        Uses v2 of the Registry API for paginated tag listing.

        Parameters
        ----------
        repository : str
            The image repository name (e.g. ``"nginx"``).
        offset : int, optional
            Pagination offset. Defaults to 0.
        limit : int, optional
            Maximum tags to return. Defaults to 50.

        Returns
        -------
        dict[str, object]
            A dictionary containing the list of available tags.
        """
        api_name = 'SYNO.Docker.Registry'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': 2, 'method': 'tags',
                     'name': repository, 'offset': offset, 'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Network — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def create_network(self, name: str, driver: str = 'bridge',
                       subnet: Optional[str] = None,
                       gateway: Optional[str] = None,
                       ip_range: Optional[str] = None,
                       enable_ipv6: bool = False) -> dict[str, object] | str:
        """
        Create a new Docker network.

        Parameters
        ----------
        name : str
            Name of the network.
        driver : str, optional
            Network driver. Defaults to ``"bridge"``.
        subnet : str, optional
            Subnet in CIDR notation (e.g. ``"172.28.0.0/16"``).
        gateway : str, optional
            Gateway IP address.
        ip_range : str, optional
            Allocatable IP range in CIDR notation.
        enable_ipv6 : bool, optional
            Enable IPv6 on the network. Defaults to False.

        Returns
        -------
        dict[str, object]
            Result of the creation, including the new network ID.
        """
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'create',
            'name': name, 'driver': driver,
            'enable_ipv6': json.dumps(enable_ipv6),
        }
        if subnet is not None:
            req_param['subnet'] = subnet
        if gateway is not None:
            req_param['gateway'] = gateway
        if ip_range is not None:
            req_param['iprange'] = ip_range

        return self.request_data(api_name, api_path, req_param)

    def delete_network(self, name: str) -> dict[str, object] | str:
        """
        Delete a Docker network.

        Parameters
        ----------
        name : str
            The name of the network to delete.

        Returns
        -------
        dict[str, object]
            Result of the delete operation.
        """
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'delete', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    def get_network(self, name: str) -> dict[str, object] | str:
        """
        Get detailed information about a Docker network.

        Parameters
        ----------
        name : str
            The name of the network.

        Returns
        -------
        dict[str, object]
            Network details including driver, subnet, containers, etc.
        """
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'name': name}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Project — additional methods
    # ──────────────────────────────────────────────────────────────────────

    def create_project(self, name: str, share_path: str,
                       content: str,
                       enable_service_portal: bool = False,
                       service_portal_name: Optional[str] = None,
                       service_portal_port: Optional[int] = None,
                       service_portal_protocol: str = 'http') -> dict[str, object] | str:
        """
        Create a new Docker Compose project.

        Parameters
        ----------
        name : str
            Project name.
        share_path : str
            Shared-folder path where the compose file lives
            (e.g. ``"/docker/myproject"``).
        content : str
            The docker-compose YAML content as a string.
        enable_service_portal : bool, optional
            Enable the DSM reverse-proxy portal. Defaults to False.
        service_portal_name : str, optional
            Portal display name.
        service_portal_port : int, optional
            Portal target port.
        service_portal_protocol : str, optional
            Portal protocol. Defaults to ``"http"``.

        Returns
        -------
        dict[str, object]
            Result including the new project ID.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'create',
            'name': name, 'share_path': share_path,
            'content': content,
            'enable_service_portal': json.dumps(enable_service_portal),
            'service_portal_protocol': service_portal_protocol,
        }
        if service_portal_name is not None:
            req_param['service_portal_name'] = service_portal_name
        if service_portal_port is not None:
            req_param['service_portal_port'] = service_portal_port

        return self.request_data(api_name, api_path, req_param, method='post')

    def update_project(self, project_id: str, content: str,
                       enable_service_portal: Optional[bool] = None,
                       service_portal_name: Optional[str] = None,
                       service_portal_port: Optional[int] = None,
                       service_portal_protocol: Optional[str] = None) -> dict[str, object] | str:
        """
        Update an existing Docker Compose project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.
        content : str
            Updated docker-compose YAML content.
        enable_service_portal : bool, optional
            Update the portal setting.
        service_portal_name : str, optional
            Update portal name.
        service_portal_port : int, optional
            Update portal port.
        service_portal_protocol : str, optional
            Update portal protocol.

        Returns
        -------
        dict[str, object]
            Result of the update operation.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'update',
            'id': project_id, 'content': content,
        }
        if enable_service_portal is not None:
            req_param['enable_service_portal'] = json.dumps(
                enable_service_portal)
        if service_portal_name is not None:
            req_param['service_portal_name'] = service_portal_name
        if service_portal_port is not None:
            req_param['service_portal_port'] = service_portal_port
        if service_portal_protocol is not None:
            req_param['service_portal_protocol'] = service_portal_protocol

        return self.request_data(api_name, api_path, req_param, method='post')

    def delete_project(self, project_id: str, preserve_content: bool = False) -> dict[str, object] | str:
        """
        Delete a Docker Compose project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.
        preserve_content : bool, optional
            Keep the compose file on disk. Defaults to False.

        Returns
        -------
        dict[str, object]
            Result of the delete operation.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete',
                     'id': project_id,
                     'preserve_content': json.dumps(preserve_content)}

        return self.request_data(api_name, api_path, req_param)

    def start_project(self, project_id: str) -> dict[str, object] | str:
        """
        Start (``docker compose up``) a project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.

        Returns
        -------
        dict[str, object]
            Result of the start operation.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'start', 'id': project_id}

        return self.request_data(api_name, api_path, req_param)

    def stop_project(self, project_id: str) -> dict[str, object] | str:
        """
        Stop (``docker compose down``) a project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.

        Returns
        -------
        dict[str, object]
            Result of the stop operation.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'stop', 'id': project_id}

        return self.request_data(api_name, api_path, req_param)

    def build_project(self, project_id: str) -> dict[str, object] | str:
        """
        Build (``docker compose build``) images for a project.

        Parameters
        ----------
        project_id : str
            The UUID of the project.

        Returns
        -------
        dict[str, object]
            Result of the build operation.
        """
        api_name = 'SYNO.Docker.Project'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'build', 'id': project_id}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Log  (NEW — Docker daemon / global logs)
    # ──────────────────────────────────────────────────────────────────────

    def get_docker_logs(self, offset: int = 0, limit: int = 50,
                        sort_dir: str = 'DESC',
                        keyword: Optional[str] = None,
                        level: Optional[str] = None) -> dict[str, object] | str:
        """
        Get Docker daemon-level / global logs.

        These are logs from the Docker engine itself, not from individual
        containers. Use ``get_logs()`` for per-container logs.

        Parameters
        ----------
        offset : int, optional
            Pagination offset. Defaults to 0.
        limit : int, optional
            Maximum number of log entries to return. Defaults to 50.
        sort_dir : str, optional
            Sort direction (``"ASC"`` or ``"DESC"``). Defaults to ``"DESC"``.
        keyword : str, optional
            Keyword filter.
        level : str, optional
            Log level filter (e.g. ``"error"``, ``"warn"``).

        Returns
        -------
        dict[str, object]
            Docker daemon log entries.
        """
        api_name = 'SYNO.Docker.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'get',
            'offset': offset, 'limit': limit, 'sort_dir': sort_dir,
        }
        if keyword is not None:
            req_param['keyword'] = keyword
        if level is not None:
            req_param['level'] = level

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Migrate  (NEW — migration utilities)
    # ──────────────────────────────────────────────────────────────────────

    def get_migrate_status(self) -> dict[str, object] | str:
        """
        Get the migration status of Docker containers / configuration.

        Checks whether containers require migration (e.g. after a DSM or
        Docker package upgrade).

        Returns
        -------
        dict[str, object]
            Current migration status.
        """
        api_name = 'SYNO.Docker.Migrate'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def start_migration(self) -> dict[str, object] | str:
        """
        Start the Docker migration process.

        Triggers migration of containers that require updating after a
        DSM or Docker package upgrade.

        Returns
        -------
        dict[str, object]
            Result of the migration start.
        """
        api_name = 'SYNO.Docker.Migrate'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        return self.request_data(api_name, api_path, req_param)

    # ──────────────────────────────────────────────────────────────────────
    #  SYNO.Docker.Utils  (NEW — utility operations)
    # ──────────────────────────────────────────────────────────────────────

    def get_docker_utils_info(self) -> dict[str, object] | str:
        """
        Get Docker utility information.

        Returns general Docker engine information such as version, storage
        driver, volumes path, and capability flags.

        Returns
        -------
        dict[str, object]
            Docker engine utility information.
        """
        api_name = 'SYNO.Docker.Utils'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def docker_prune(self) -> dict[str, object] | str:
        """
        Prune unused Docker resources.

        Removes unused containers, networks, images, and build cache
        (equivalent to ``docker system prune``).

        Returns
        -------
        dict[str, object]
            Result of the prune operation, including space reclaimed.
        """
        api_name = 'SYNO.Docker.Utils'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'prune'}

        return self.request_data(api_name, api_path, req_param)

    def get_docker_version(self) -> dict[str, object] | str:
        """
        Get Docker engine version information.

        Returns
        -------
        dict[str, object]
            Docker version details (version, API version, go version, etc.).
        """
        api_name = 'SYNO.Docker.Utils'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'version'}

        return self.request_data(api_name, api_path, req_param)
