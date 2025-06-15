---
sidebar_position: 12
title: 🚧 Docker
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Docker
:::warning
 
This API is not documented yet.
 
:::
## Overview
Docker API implementation.

This class provides methods to interact with Docker containers, images, registries, and projects on a Synology NAS.

Supported actions:
    - **Getters** :
        - Get list of containers
        - Get resources of all containers
        - Get system resources
        - List of docker images
        - Get list of docker registries
        - Get list of container logs
        - Get containers resource usage statistics
        - Search for docker image in all available registries
        - Get list of projects
        - Get list of docker networks

    - **Setters** :
        -

    - **Actions** :
        - Export container profile
        - Export container profile and content
## Methods
### `containers`
Get list of containers.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the containers information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `container_resources`
Get resources of all containers.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container.Resource` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the resources information of the containers.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `system_resources`
Get system resources  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Core.System.Utilization` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the system resources information.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `downloaded_images`
List of docker images available on Synology NAS.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Image` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_limit_** `int`  
The maximum number of docker images to return. Defaults -1 (all).  
  
**_offset_** `int`  
The offset for pagination. Defaults to 0.  
  
**_show_dsm_** `bool`  
Defaults to False.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the list of downloaded images.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `images_registry_resources`
Get list of docker registries.  
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
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Registry` 
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `network`
Get list of docker networks.  
Example return
--------------
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
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Network` 
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `search_image`
Search for docker image in all available registries.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Registry` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_query_** `str`  
name of the docker image to search for. Defaults to None.  
  
**_Example return_** ``  
  
  
**_--------------_** ``  
  
  
**_```json_** ``  
  
  
**_{_** ``  
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
  
**_}_** ``  
  
  
**_```_** ``  
  
  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `list_projects`
Get list of projects.  
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
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Project` 
</div>
  
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `get_project_info`
Get information about a specific project.  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Project` 
</div>
  



---


### `start_container`
Start a container by its name.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_container_** `str`  
The name of the container  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the export operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `stop_container`
Stop a container by its name.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_container_** `str`  
The name of the container  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the stop operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


### `export_container_settings`
Export container profile  
file <container>.syno.json will be created in the specified path.  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container.Profile` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_container_** `str`  
The name of the container  
  
**_path_** `str`  
The path on filesystem of Synology NAS where the container settings will be exported.
If not specified, the file will be offered as a download through the browser.
For example: `/docker/nging`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the export operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
       "data" : {},
       "httpd_restart" : false,
       "success" : true
    }
```
</details>



---


### `export_container`
Export container profile and content to a specified path on Synology nas.  
archive <container>.syno.txz will be created in the specified path.  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_container_** `str`  
The name of the container  
  
**_path_** `str`  
The path on filesystem of Synology NAS where the container settings will be exported.
For example: `/docker/nging`  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the result of the export operation.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
```json
    {
       "data" : {},
       "httpd_restart" : false,
       "success" : true
    }
```
</details>



---


### `get_logs`
Get list of container logs.  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container.Log` 
</div>
  



---


### `docker_stats`
Get containers resource usage statistics.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.Docker.Container` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object]`  
A dictionary containing the resource usage statistics of the containers.  

</div>
#### Example return
<details>
<summary>Click to expand</summary>
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
</details>



---


