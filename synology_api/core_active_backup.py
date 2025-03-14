from __future__ import annotations
from . import base_api

import time
import json

class ActiveBackupBusiness(base_api.BaseApi):
    """Active Backup for Business API Implementation.

        This class provides methods to interact with the Active Backup for Business package.

        Supported methods:
            - Getters: 
                - Get package settings
                - Get tasks information
                - Get tasks versions information
                - Get devices information
                - Get devices transfer size
                - Get hypervisors information
                - Get package / devices / tasks logs
                - Get task history
                - Get task result details
                - Get storage information 
            - Setters:
                - Set maximum concurrent devices
                - Set retention policy execution time
                - Set bandwidth control
                - Set use package certificate
            - Actions:
                - Run backup
                - Cancel backup
                - Remove task
                - Remove version
    """

    def __create_filter(
            self,
            log_level: str = "",
            keyword: str = "",
            from_date: int = 0,
            to_date: int = 0,
            task_status: str = "",
            result_status: str = "",
            backup_type: str = "",
            action_type: str = ""
        ):
        """
        Create a filter dictionary based on the provided parameters.
        """
        log_level_map = {
            'error': 0,
            'warning': 1,
            'information': 2
        }
        result_status_map = {
            'success': 2,
            'partial_success': 3,
            'fail': 4,
            'cancel': 5,
            'no_backup': 6 
        }
        backup_type_map = {
            'vm': 1,
            'pc': 2,
            'physical_server': 3,
            'file_server': 4,
            'nas': 5
        }
        action_type_map = {
            'backup': 1,
            'dedup_data': 1048576,
            'restore': [128,1024,2048],
            'migrate': 256,
            'delete_target': 65536,
            'delete_version': 131072,
            'delete_host': 262144,
            'relink': 2097152,
            'create_task': 268435456
        }

        filter = {}
        if keyword != "":
            filter['key_word'] = keyword
        if from_date > 0: 
            filter['from_timestamp'] = from_date
        if to_date > 0: 
            filter['to_timestamp'] = to_date
        if task_status:
            filter['status'] = task_status

        if log_level and log_level in log_level_map:
            filter['log_level'] = log_level_map[log_level]

        if result_status and result_status in result_status_map:
            filter['status'] = result_status_map[result_status]

        if backup_type and backup_type in backup_type_map:
            filter['backup_type'] = backup_type_map[backup_type]

        if action_type and action_type in action_type_map:
            filter['job_action'] = action_type_map[action_type]

        return filter

    def get_settings(self) -> dict[str, object]:
        """Get the package settings including certificate information.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing the current settings.
            
            Example return
            --------------
            ```json
            {
                "data": {
                    "cert_info": {
                        "cert_from_dsm": {
                            "cert_common_name": "xxxxx.myds.me",
                            "cert_issuer": "R10",
                            "cert_san": [
                                "*.xxxxx.myds.me",
                                "xxxxx.myds.me"
                            ],
                            "cert_tillTime": "May 29 18:54:13 2025 GMT"
                        },
                        "cert_from_package": {
                            "cert_common_name": "Active Backup for Business",
                            "cert_issuer": "Synology Active Backup for Business",
                            "cert_san": [
                                "Active Backup for Business"
                            ],
                            "cert_tillTime": "Apr 17 19:14:52 2034 GMT"
                        },
                        "cert_use_package": true
                    },
                    "settings": [
                        {
                            "id": 1,
                            "name": "max_concurrent_devices",
                            "value": "5"
                        },
                        {
                            "id": 2,
                            "name": "memory_usage_limit_percentage",
                            "value": "75"
                        },
                        {
                            "id": 3,
                            "name": "package_cert_id",
                            "value": "dyAaL7"
                        },
                        {
                            "id": 4,
                            "name": "enable_global_bandwidth_control",
                            "value": "false"
                        },
                        {
                            "id": 5,
                            "name": "global_backup_bandwidth_number",
                            "value": "0"
                        },
                        {
                            "id": 6,
                            "name": "enable_ip_range_bandwidth_control",
                            "value": "false"
                        },
                        {
                            "id": 7,
                            "name": "full_backup_task_ids",
                            "value": "2"
                        },
                        {
                            "name": "retention_run_hour",
                            "value": "14"
                        },
                        {
                            "name": "retention_run_min",
                            "value": "50"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_concurrent_devices(self, value: int) -> dict[str, object]:
        """Set the maximum number of concurrent devices that can be backed up at the same time.

            Note: You can run multiple concurrent backup devices, but only up to the maximum limit you set—provided that your NAS's RAM usage does not exceed its limit.
            
            Note: This setting will be effective starting from the next backup.
        
            Parameters
            ----------
            value : int
                Maximum number of concurrent devices.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        settings = [{
            'name': 'max_concurrent_devices',
            'value': str(value)
        }]

        req_param = {
            'version': '1',
            'method': 'set',
            'settings': json.dumps(settings)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_retention_policy_exec_time(self, hour: int, minute: int) -> dict[str, object]:
        """Set the time of day when the retention policy will be executed.
        
            Parameters
            ----------
            hour : int
                Hour in 24-hour format (0 - 23) when the retention policy will be executed.

            minute : int
                Minute (0 - 59) when the retention policy will be executed
        
            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        settings = [
            { 'name': 'retention_run_hour', 'value': str(hour) },
            { 'name': 'retention_run_min', 'value': str(minute) }
        ]

        req_param = {
            'version': '1',
            'method': 'set',
            'settings': json.dumps(settings)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_traffic_throttle(
            self,
            traffic_control: dict[str, object] = { "enable": False, "bandwidth": 0 },
            ip_range: list[str] = ["", ""]
        ) -> dict[str, object]:
        """Set the global bandwidth control and IP range bandwidth control.

            Note: Applies only to PC, Physical Server and NAS devices. 
            
            Note: When multiple tasks run simultaneously, the system will evenly distribute the throttled traffic.

            Parameters
            ----------
            traffic_control : dict[str, object], optional
                Traffic control settings. 
                
                Defaults to `{ 'enable': False, 'bandwidth': 0 }` (disable traffic throttling).

                Bandwidth should be specified in MB/s.

            ip_range : list[str], optional
                If specified, traffic control will only be applied to this IP range. 
                
                Defaults to `["", ""]` (disable IP range bandwidth control).
                
                First index should contain the IP range start, second index the IP range end. Only supports IPv4 format.

                Example: 
                ```python
                ["192.168.0.1", "192.168.0.10"]
                ```
        
            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']
        settings = []

        def item(key: str, value: str) -> dict[str, str]:
            return { 'name': key, 'value': value }

        if traffic_control['enable'] and traffic_control['bandwidth'] > -1:
            settings.append(item('enable_global_bandwidth_control', 'true'))
            settings.append(item('global_backup_bandwidth_number', str(traffic_control['bandwidth'])))

            if ip_range[0] and ip_range[1]:
                settings.append(item('enable_ip_range_bandwidth_control', 'true'))
                settings.append(item('bandwidth_control_ip_start', ip_range[0]))
                settings.append(item('bandwidth_control_ip_end', ip_range[1]))
            else: 
                settings.append(item('enable_ip_range_bandwidth_control', 'false'))
        else:
            settings.append(item('enable_global_bandwidth_control', 'false'))

        req_param = {
            'version': '1',
            'method': 'set',
            'settings': json.dumps(settings)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def set_use_pkg_cert(self, use_package_cert: bool) -> dict[str, object]:	
        """Set whether to use the self signed certificate provided by the package.
        
            Parameters
            ----------
            use_package_cert : bool
                Use the certificate provided by the package.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """	
        api_name = 'SYNO.ActiveBackup.Setting'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'set',
            'settings': '[]',
            'cert_use_package': use_package_cert
        }

        return self.request_data(api_name, api_path, req_param)

    def list_vm_hypervisor(self) -> dict[str, object]:
        """Get a list of all configured hypervisors present in ABB.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing a list of hypervisors.
        """
        # TODO: Add return example to docstring

        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list'
        }

        return self.request_data(api_name, api_path, req_param)

    def list_device_transfer_size(
            self, 
            time_start: int = int(time.time() - 86400), 
            time_end: int = int(time.time())
        ) -> dict[str, object]:
        """Get a list of all devices and their respective transfer size for the given time frame.
        
            Parameters
            ----------
            time_start : int, optional
                Time window start time. Format must be epoch date in seconds. Defaults to 24 hours ago.
                
            time_end : int, optional
                Time window end time. Format must be epoch date in seconds. Defaults to current time.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing a list of devices and their transfer size.
        
            Example return
            ----------
            ```json
            {
                "data" : {
                    "device_list" : [
                        {
                            "device" : {
                                "agent_token" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                "agentless_auth_policy" : 0,
                                "auto_discovery" : false,
                                "backup_type" : 2,
                                "create_time" : 1709413484,
                                "device_id" : 5,
                                "device_uuid" : "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
                                "dsm_model" : "",
                                "dsm_unique" : "",
                                "host_ip" : "192.168.0.63",
                                "host_name" : "xxxxx",
                                "host_port" : 0,
                                "hypervisor_id" : "",
                                "inventory_id" : 0,
                                "login_password" : "",
                                "login_time" : 1709413493,
                                "login_user" : "xxxx",
                                "login_user_id" : 1026,
                                "os_name" : "Windows 11(64-bit)",
                                "vm_moid_path" : ""
                            },
                            "transfer_list" : [
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 342,
                                    "processed_bytes" : 0,
                                    "result_id" : 587,
                                    "status" : 5,
                                    "time_end" : 1741895385,
                                    "time_start" : 1741894511,
                                    "transfered_bytes" : 1523580928
                                },
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 343,
                                    "processed_bytes" : 0,
                                    "result_id" : 589,
                                    "status" : 5,
                                    "time_end" : 1741896408,
                                    "time_start" : 1741896176,
                                    "transfered_bytes" : 6909067264
                                },
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 344,
                                    "processed_bytes" : 0,
                                    "result_id" : 590,
                                    "status" : 5,
                                    "time_end" : 1741896716,
                                    "time_start" : 1741896624,
                                    "transfered_bytes" : 444596224
                                },
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 346,
                                    "processed_bytes" : 0,
                                    "result_id" : 591,
                                    "status" : 2,
                                    "time_end" : 1741901184,
                                    "time_start" : 1741896737,
                                    "transfered_bytes" : 482689236992
                                },
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 347,
                                    "processed_bytes" : 0,
                                    "result_id" : 593,
                                    "status" : 2,
                                    "time_end" : 1741946439,
                                    "time_start" : 1741946267,
                                    "transfered_bytes" : 2122801152
                                },
                                {
                                    "config_device_id" : 5,
                                    "device_name" : "xxxxx",
                                    "device_result_id" : 348,
                                    "processed_bytes" : 0,
                                    "result_id" : 595,
                                    "status" : 2,
                                    "time_end" : 1741972250,
                                    "time_start" : 1741971826,
                                    "transfered_bytes" : 8208736256
                                }
                            ]
                        },
                    ],
                    "total" : 1
                },
                "success" : true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list_device_transfer_size',
            'time_start': time_start,
            'time_end': time_end
        }

        return self.request_data(api_name, api_path, req_param)

    def list_tasks(
            self,
            task_id: int = -1,
            backup_type: str = "",
            status: str = "",
            from_date: int = 0,
            to_date: int = 0,
            include_versions: bool = False,
        ) -> dict[str, object]:
        """Get information of one or all tasks. 
        
            Parameters
            ----------
            task_id : int, optional
                Get information of specific task. Defaults to `-1` (all tasks)

            backup_type : str, optional
                Return only tasks matching the device type provided. Defaults to `""` (all device types).

                Possible values:
                - `"vm"`
                - `"pc"`
                - `"physical_server"`
                - `"file_server"`
                - `"nas"`


                Note that values are different when returned by the API.  

                Return values mappings:
                - `1` -> `vm`
                - `2` -> `pc`
                - `3` -> `physical_server`
                - `4` -> `file_server`
                - `5` -> `nas`

            status : str, optional
                Return only tasks matching the status provided. Defaults to `""` (all status).

                Possible values:
                - `"backingup"`
                - `"waiting"`
                - `"deleting"`
                - `"unscheduled"`

            from_date : int, optional
                Only include tasks for which last backup is greater or equal to this date. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            to_date : int, optional
                Only include tasks for which last backup is less or equal to this date. Format must be epoch date in seconds. Defaults to `0` (no time limit).

            include_versions : bool, optional
                Include versions information in the response. Defaults to `False`.
            
            Returns
            -------
            dict[str, object]
                Dictionary containing a list of tasks.
            
            Example return
            --------------
            ```json
            {
                "data": {
                    "has_devices": true,
                    "has_dsm_agent": false,
                    "has_hyperv_inventories": false,
                    "has_linux_agent": false,
                    "has_mac_agent": false,
                    "has_vmware_inventories": false,
                    "has_windows_agent": true,
                    "tasks": [{
                        "agentless_backup_path" : "",
                        "agentless_backup_policy" : 0,
                        "agentless_enable_block_transfer" : false,
                        "agentless_enable_dedup" : false,
                        "agentless_enable_windows_vss" : false,
                        "allow_manual_backup" : true,
                        "backup_cache_content" : {
                            "cached_enabled" : false
                        },
                        "backup_external" : false,
                        "backup_type" : 2,
                        "bandwidth" : 0,
                        "bandwidth_content" : {
                            "backup_bandwidth_base" : 0,
                            "backup_bandwidth_number" : 0,
                            "enable" : false
                        },
                        "cbt_enable_mode" : 1,
                        "connection_timeout" : 0,
                        "custom_volume" : [],
                        "datastore_reserved_percentage" : 0,
                        "dedup_api_restore" : true,
                        "dedup_path" : "",
                        "device_count" : 1,
                        "devices" : [{
                            "agent_can_backup" : true,
                            "agent_driver_status" : "enable",
                            "agent_status" : "online",
                            "agent_token" : "xxxxxxxxxxxxxxx",
                            "agentless_auth_policy" : 0,
                            "auto_discovery" : false,
                            "backup_type" : 2,
                            "create_time" : 1709413484,
                            "device_id" : 5,
                            "device_uuid" : "xxxxxxxxxxxx",
                            "driver_status" : null,
                            "dsm_model" : "",
                            "dsm_unique" : "",
                            "host_ip" : "192.168.0.63",
                            "host_name" : "xxxxxxxxx",
                            "host_port" : 0,
                            "hypervisor_id" : "",
                            "inventory_id" : 0,
                            "login_password" : "",
                            "login_time" : 1709413493,
                            "login_user" : "xxxx",
                            "login_user_id" : 1026,
                            "os_name" : "Windows 11(64-bit)",
                            "platform_type" : 1,
                            "vm_moid_path" : ""
                        }],
                        "enable_app_aware_bkp" : false,
                        "enable_compress_transfer" : true,
                        "enable_datastore_aware" : false,
                        "enable_dedup" : true,
                        "enable_encrypt_transfer" : true,
                        "enable_notify" : false,
                        "enable_shutdown_after_complete" : false,
                        "enable_verification" : false,
                        "enable_wake_up" : false,
                        "enable_windows_working_state" : false,
                        "last_result" : {
                            "backup_type" : 2,
                            "detail_path" : "",
                            "error_count" : 0,
                            "job_action" : 1,
                            "none_count" : 0,
                            "result_id" : 593,
                            "status" : 2,
                            "success_count" : 0,
                            "task_config" : {
                                "device_list" : [
                                    {
                                        "device_id" : 5,
                                        "host_name" : "xxxxxxxxxx"
                                    }
                                ]
                            },
                            "task_id" : 5,
                            "task_name" : "xxxxxxxxxxx",
                            "time_end" : 1741946439,
                            "time_start" : 1741946267,
                            "transfered_bytes" : 2122801152,
                            "warning_count" : 0
                        },
                        "last_version_id" : 163,
                        "max_concurrent_devices" : 0,
                        "next_trigger_time" : 1742176800,
                        "pre_post_script_setting" : {
                            "post_script_path" : "",
                            "pre_script_path" : "",
                            "script_exec_mode" : 0
                        },
                        "repo_dir" : "@ActiveBackup",
                        "retention_policy" : {
                            "gfs_days" : "7",
                            "gfs_months" : "12",
                            "gfs_weeks" : "4",
                            "gfs_years" : "3",
                            "keep_all" : false,
                            "keep_versions" : 10
                        },
                        "sched_content" : {
                            "backup_window" : "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                            "enable_backup_window" : false,
                            "is_continuous_paused" : false,
                            "repeat_hour" : 0,
                            "repeat_type" : "Weekly",
                            "run_hour" : 3,
                            "run_min" : 0,
                            "run_weekday" : [ 1, 2, 3, 4, 5 ],
                            "schedule_setting_type" : 1,
                            "start_day" : 0,
                            "start_month" : 0,
                            "start_year" : 0
                        },
                        "sched_id" : 0,
                        "sched_modify_time" : 1709413646,
                        "share_compressed" : false,
                        "share_name" : "ActiveBackupforBusiness",
                        "source_type" : 2,
                        "storage_compress_algorithm" : 0,
                        "storage_encrypt_algorithm" : 0,
                        "storage_id" : 1,
                        "target_dir" : "xxxxxxxxxxx",
                        "target_status" : "online",
                        "task_id" : 5,
                        "task_name" : "xxx",
                        "unikey" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "verification_policy" : 120,
                        "version_count" : 2,
                        "versions" : [
                        {
                            "crypto_key_id" : 0,
                            "data_format" : 1,
                            "folder_name" : "ActiveBackup_2025-03-14_105745",
                            "is_snapshot" : true,
                            "locked" : false,
                            "status" : 3,
                            "time_end" : 1741946439,
                            "time_start" : 1741946267,
                            "used_size" : 0,
                            "version_id" : 163
                        },
                        {
                            "crypto_key_id" : 0,
                            "data_format" : 1,
                            "folder_name" : "ActiveBackup_2025-03-13_211215",
                            "is_snapshot" : true,
                            "locked" : false,
                            "status" : 3,
                            "time_end" : 1741901184,
                            "time_start" : 1741896737,
                            "used_size" : 0,
                            "version_id" : 162
                        },
                        ],
                        "view_type" : "",
                        "vm_folder" : null
                    }],
                    "total": 1
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        filter = self.__create_filter(
            backup_type=backup_type, 
            task_status=status,
            from_date=from_date,
            to_date=to_date
        )

        # This API requires the task_id inside filters instead of an independent param
        if task_id > -1:
            filter['task_id'] = task_id

        req_param = {
            'version': '1',
            'method': 'list',
            'load_status': True,
            'load_result': True,
            'load_devices': True,
            'load_versions': include_versions,
            'filter': json.dumps(filter)
        }

        return self.request_data(api_name, api_path, req_param)
    
    def list_logs(
            self,
            task_id: int = -1,
            log_level: str = "",
            keyword: str = "",
            from_date: int = 0,
            to_date: int = 0,
            offset: int = 0, 
            limit: int = 200,
        ) -> dict[str, object]:
        """Get logs from the package, tasks and devices. From `[Activities -> Log]` screen in ABB.

            For specific task logs `[Task List -> Details -> Log]`, specify `task_id` parameter.

            Parameters
            ----------
            task_id : int, optional
                Get logs of specific task. Defaults to `-1` (all logs - package/tasks/devices)
            
            log_level : str, optional
                Type of logs to return. Defaults to `""` (all types).

                Possible values:  
                - `"error"`
                - `"warning"`
                - `"information"`

                
                Note that values are different when returned by the API. 
                
                Return values mappings:
                - 0 -> `error`
                - 1 -> `warning`
                - 2 -> `information`

            keyword : str, optional
                Keyword used to filter the results. Defaults to `""`.

            from_date : int, optional
                Date from which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            to_date : int, optional
                Date until which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            offset : int, optional
                Offset results by this value. Defaults to `0`.
            
            limit : int, optional
                Amount of results to be returned. Defaults to `200`.

            Returns
            -------
            dict[str, object]
                Dictionary containing a list of logs.

            Example return
            --------------
            ```json
            {
                "count": 1,
                "logs": [
                    {
                        "backup_type": 4,
                        "device_id": 6,
                        "device_name": "xxxx",
                        "error_code": 0,
                        "log_id": 5525,
                        "log_level": 0,
                        "log_time": 1741897498,
                        "log_type": 1104,
                        "other_params": {
                            "backup_type": 4,
                            "device_id": 6,
                            "device_name": "xxxx",
                            "platform_type": 0,
                            "task_id": 8,
                            "task_name": "xxxxxxxx",
                            "user_id": 0,
                            "user_name": ""
                        },
                        "result_id": 592,
                        "task_id": 8,
                        "task_name": "xxxxxxxx",
                        "user_id": 0,
                        "user_name": ""
                    }
                ]
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        filter = self.__create_filter(log_level, keyword, from_date, to_date)

        req_param = {
            'version': '1',
            'method': 'list_log',
            'offset': offset,
            'limit': limit,
            'filter': json.dumps(filter)
        }

        if task_id > -1:
            req_param['task_id'] = task_id
        
        return self.request_data(api_name, api_path, req_param)
    
    def task_history(
            self,
            task_id: int = -1,
            status: str = "",
            keyword: str = "",
            backup_type: str = "",
            action_type: str = "",
            from_date: int = 0,
            to_date: int = 0,
            offset: int = 0, 
            limit: int = 200
        ) -> dict[str, object]:
        """Return the history of task execution.

            Parameters
            ----------
            task_id : int, optional
                Get logs of specific task. Defaults to `-1` (all tasks)
            
            status : str, optional
                Return only tasks matching the status provided. Defaults to `""` (all status).

                Possible values:  
                - `"success"`
                - `"partial_success"`
                - `"fail"`
                - `"cancel"`

                
                Note that values are different when returned by the API. 
                
                Return values mappings:
                - `2` -> `success`
                - `3` -> `partial_success`
                - `4` -> `fail`
                - `5` -> `cancel`

            backup_type : str, optional
                Return only tasks matching the device type provided. Defaults to `""` (all device types).

                Possible values:  
                - `"vm"`
                - `"pc"`
                - `"physical_server"`
                - `"file_server"`
                - `"nas"`

                
                Note that values are different when returned by the API. 
                
                Return values mappings:
                - `1` -> `vm`
                - `2` -> `pc`
                - `3` -> `physical_server`
                - `4` -> `file_server`
                - `5` -> `nas`

            action_type : str, optional
                Return only tasks matching the task type provided. Defaults to `""` (all task types).

                Possible values:  
                - `"backup"`
                - `"dedup_data"`
                - `"restore"`
                - `"migrate"`
                - `"delete_targe"`
                - `"delete_version"`
                - `"delete_host"`
                - `"relink"`
                - `"create_task"`

                
                Note that values are different when returned by the API. 
                
                Return values mappings:
                - `1` -> `backup`
                - `1048576` -> `dedup_data`
                - `[128,1024,2048]` -> `restore`
                - `256` -> `migrate`
                - `65536` -> `delete_target`
                - `131072` -> `delete_version`
                - `262144` -> `delete_host`
                - `2097152` -> `relink`
                - `268435456` -> `create_task`

            keyword : str, optional
                Keyword used to filter the results. Defaults to `""`.

            from_date : int, optional
                Date from which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            to_date : int, optional
                Date until which the results will start. Format must be epoch date in seconds. Defaults to `0` (no time limit).
            
            offset : int, optional
                Offset results by this value. Defaults to `0`.
            
            limit : int, optional
                Amount of results to be returned. Defaults to `200`.

            Returns
            -------
            dict[str, object]
                Dictionary containing a list of results.

            Example return
            --------------
            ```json
            {
                "data": {
                    "count": 1,
                    "results": [
                        {
                            "backup_type": 2,
                            "detail_path": "",
                            "error_count": 0,
                            "job_action": 131072,
                            "none_count": 0,
                            "result_id": 594,
                            "status": 2,
                            "success_count": 1,
                            "task_config": {
                                "device_list": [
                                    {
                                        "host_name": "xxxxxxx"
                                    }
                                ]
                            },
                            "task_id": 5,
                            "task_name": "xxxxxxxxxxx",
                            "time_end": 1741952422,
                            "time_start": 1741952402,
                            "warning_count": 0
                        },
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        filter = self.__create_filter(
            status=status, 
            keyword=keyword, 
            backup_type=backup_type, 
            action_type=action_type,
            from_date=from_date,
            to_date=to_date
        )

        req_param = {
            'version': '1',
            'method': 'list_result',
            'offset': offset,
            'limit': limit,
            'filter': json.dumps(filter)
        }

        if task_id > -1:
            req_param['task_id'] = task_id
        
        return self.request_data(api_name, api_path, req_param)
    
    def result_details(
            self, 
            result_id: int, 
            limit: int = 500, 
            order_by: str = "log_level", 
            direction: str = "ASC"
        ) -> dict[str, object]:
        """Get details of a task result log. `result_id` can be retrieved from `list_logs()` function.
        
            Parameters
            ----------
            result_id : int
                ID of the result to get details from.

            limit : int, optional
                Amount of results to be returned. Defaults to `500`.

            order_by : str, optional
                What to order the results by. Defaults to `"log_level"`.

                Possible values:
                - `"log_level"`
                - `"log_time"`

            direction : str, optional
                Direction of the order. Defaults to `"ASC"`.

                Possible values:
                - `"ASC"`
                - `"DESC"`
        
            Returns
            -------
            dict[str, object]
                Dictionary containing a list of result details.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "count": 2,
                    "result_detail_list": [
                        {
                            "error_code": 0,
                            "log_level": 0,
                            "log_time": 1741897456,
                            "log_type": 6002,
                            "other_params": {
                                "fs_error": -65,
                                "os_name": "smb",
                                "path": "/D",
                                "task_id": 8
                            },
                            "result_detail_id": 9526,
                            "result_id": 592
                        },
                        {
                            "error_code": 0,
                            "log_level": 0,
                            "log_time": 1741897498,
                            "log_type": 1104,
                            "other_params": {
                                "os_name": "smb",
                                "path": "",
                                "task_id": 8,
                                "task_name": "SMB LAPTOP"
                            },
                            "result_detail_id": 9527,
                            "result_id": 592
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Log'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list_result_detail',
            'result_id': result_id,
            'limit': limit,
            'order_by': order_by,
            'direction': direction
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def list_storage(self) -> dict[str, object]:
        """Get a list of all storage devices present in ABB.
        
            Returns
            -------
            dict[str, object]
                A dictionary containing a list of storage devices.
        
            Example return
            ----------
            ```json
            {
                "data" : {
                    "storages" : [
                        {
                            "automount_iv" : "",
                            "automount_location" : "",
                            "backup_tasks" : [],
                            "compacting" : false,
                            "compacting_percentage" : 0,
                            "compressed_size" : 0,
                            "dedup_size" : 1617010274304,
                            "delete_tasks" : [],
                            "delete_versions" : [],
                            "device_count" : 4,
                            "device_info" : {
                            "agentless_count" : 1,
                            "agentless_size" : 0,
                            "dsm_count" : 0,
                            "dsm_size" : 0,
                            "pc_count" : 2,
                            "pc_size" : 6128863440896,
                            "server_count" : 1,
                            "server_size" : 0,
                            "vm_count" : 0,
                            "vm_size" : 0
                            },
                            "fs_name" : "btrfs",
                            "fs_type" : 3,
                            "mounted" : true,
                            "relink_state" : {
                            "alive" : false,
                            "owner" : true,
                            "state" : 0
                            },
                            "repo_dir" : "@ActiveBackup",
                            "share_name" : "ActiveBackupforBusiness",
                            "storage_compress_algorithm" : 0,
                            "storage_encrypt_algorithm" : 0,
                            "storage_id" : 1,
                            "vol_name" : "Volume 3",
                            "volume_path" : "/volume3"
                        }
                    ]
                },
                "success" : true
                }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Share'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'list_storage'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_run(self, task_ids: list[int]) -> dict[str, object]:
        """Trigger a backup event for the given tasks. 
        
            Parameters
            ----------
            task_ids : list[int]
                List of task IDs to trigger the backup event. 
                
                Even if only one task is specified, a list has to be passed as argument.
        
            Returns
            -------
            dict[str, object]
                Dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'backup',
            'task_ids': str(task_ids),
            'trigger_type': '1'
        }

        return self.request_data(api_name, api_path, req_param)

    def backup_task_cancel(self, task_ids: list[int]) -> dict[str, object]:
        """Cancel specified ongoing task.
        
            Parameters
            ----------
            task_ids : list[int]
                List of task IDs to trigger the cancellation event. 
                
                Even if only one task is specified, a list has to be passed as argument.
        
            Returns
            -------
            dict[str, object]
                Dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'cancel',
            'task_ids': str(task_ids)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_remove(self, task_ids: list[int]) -> dict[str, object]:
        """Remove the given tasks from ABB.

            Warning: This will remove the task and all its versions from the NAS. The backed up data will not be preserved after this operation.  
        
            Parameters
            ----------
            task_ids : list[int]
                List of task IDs to remove. 
                
                Even if only one task is specified, a list has to be passed as argument.
        
            Returns
            -------
            dict[str, object]
                Dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'remove',
            'task_ids': str(task_ids)
        }
        
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_delete_versions(self, task_id: int, versions_ids: list[int]) -> dict[str, object]:
        """Delete the specified versions from a task.

            Warning: This will remove the specified versions from the NAS. The corresponding versions data will not be preserved after this operation.  
        
            Parameters
            ----------
            task_id : int
                Task ID from which to delete the versions.

            versions_ids : list[int]
                List of version IDs to delete.
        
            Returns
            -------
            dict[str, object]
                Dictionary containing the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.ActiveBackup.Version'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {
            'version': '1',
            'method': 'delete',
            'task_id': task_id,
            'version_ids': str(versions_ids)
        }
        
        return self.request_data(api_name, api_path, req_param)