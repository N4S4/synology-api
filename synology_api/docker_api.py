from __future__ import annotations
from typing import Optional
import json

import synology_api.auth
from . import base_api


class Docker(base_api.BaseApi):
    """Docker API implementation.

        Supported actions:
            - Getters:
                - Get list of containers
                - Get resources of all containers
                - Get system resources
                - List of docker images
                - Get list of docker registries
                - Get list of container logs
                - Get containers resource usage statistics
                - Search for docker image in all available registries.
                - Get list of projects.

            - Setters:
                -

            - Actions:
                - Export container profile
                - Export container profile and content
    """
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

    # TODO: move to code_sys_utilization?
    def system_resources(self) -> dict[str, object] | str:
        """Get system resources

            Returns
            -------
            dict[str, object]
                A dictionary containing the system resources information.

            Example return
            --------------
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
    def downloaded_images(self, limit : int = -1, offset : int = 0, show_dsm : bool = False) -> dict[str, object] | str:
        """List of docker images available on Synology NAS.

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

            Example return
            --------------
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
        """Get list of docker registries.

            Example return
            --------------
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
        api_name = 'SYNO.Docker.Network'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename search_images_in_registries?
    def search_image(self, query : str = None) -> dict[str, object] | str:
        """Search for docker image in all available registries.

            Parameters
            ----------
            query : str
                name of the docker image to search for. Defaults to None.

            Example return
            --------------
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
                     },
                     ...
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
        req_param = {'version': 1, 'method': 'search', 'offset': 0, 'limit': 50, 'page_size': 50, 'q': query}

        return self.request_data(api_name, api_path, req_param)

    def list_projects(self) -> dict[str, object] | str:
        """Get list of projects.

            Example return
            --------------
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

    def get_project_info(self, project_id : str = None) -> dict[str, object] | str:
        """Get information about a specific project.

            Parameters
            ----------
            project_id : str
                ID of the project to get information about. Defaults to None.
                IDs of projects can be obtained from the `list_projects` method.


            Example return
            --------------
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
                  "content" : "services:\n  vault:\n    image: hashicorp/vault:latest\n    container_name: vault\n    hostname: vault\n    mem_limit: 512m\n    cpu_shares: 768\n    security_opt:\n      - no-new-privileges:true\n    cap_add:\n      - IPC_LOCK\n    entrypoint: vault server -config=/vault/file/\n    healthcheck:\n      test: [\"CMD\", \"vault\", \"status\"]\n      interval: 30s\n      timeout: 10s\n      retries: 5\n    ports:\n      - 8205:8200\n    volumes:\n      - /volume1/docker/vault/logs:/vault/logs:rw\n      - /volume1/docker/vault/data:/vault/file:rw\n      - /volume1/docker/vault/config:/vault/config:rw\n      - /volume1/docker/vault/plugins:/vault/plugins:rw\n      - /etc/localtime:/etc/localtime:ro\n    environment:\n      VAULT_DEV_LISTEN_ADDRESS: 0.0.0.0:8200\n      VAULT_RAFT_PATH: /vault/file\n      \n    restart: on-failure:5",
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
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': project_id}

        return self.request_data(api_name, api_path, req_param)

    def start_container(self, container : str = None) -> dict[str, object] | str:
        """Start a container by its name.

            Parameters
            ----------
            container : str
                The name of the container

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Example return
            --------------
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
        req_param = {'version': info['maxVersion'], 'method': 'start', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    def stop_container(self, container : str = None) -> dict[str, object] | str:
        """Stop a container by its name.

            Parameters
            ----------
            container : str
                The name of the container

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the stop operation.

            Example return
            --------------
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
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'name': container}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to export_container_profile?
    def export_container_settings(self, container : str = None, path : str = None) -> dict[str, object] | str:
        """Export container profile

            file <container>.syno.json will be created in the specified path.

            Parameters
            ----------
            container : str
                The name of the container

            path : str, optional
                The path on filesystem of Synology NAS where the container settings will be exported.
                If not specified, the file will be offered as a download through the browser.
                For example: `/docker/nging`

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Example return
            --------------
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
        req_param = {'version': info['maxVersion'], 'method': 'export', 'name': container, 'path' : path}

        return self.request_data(api_name, api_path, req_param)

    # TODO: rename to export_container_profile_and_content?
    def export_container(self, container : str = None, path : str = None) -> dict[str, object] | str:
        """Export container profile and content to a specified path on Synology nas.

            archive <container>.syno.txz will be created in the specified path.

            Parameters
            ----------
            container : str
                The name of the container

            path : str
                The path on filesystem of Synology NAS where the container settings will be exported.
                For example: `/docker/nging`

            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the export operation.

            Example return
            --------------
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
        """Get containers resource usage statistics.

            Returns
            -------
            dict[str, object]
                A dictionary containing the resource usage statistics of the containers.

            Example return
            --------------
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
