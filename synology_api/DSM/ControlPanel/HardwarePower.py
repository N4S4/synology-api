"""
Hardware power class for Synology DSM.
"""

from synology_api import base_api
import json
from typing import List


class HardwarePower(base_api.BaseApi):
    """
    Hardware power class for interacting with Synology DSM Hardware & Power settings.

    Supported methods:
    - Getters:

    - Setters:
    """

    def need_reboot(self) -> dict:
        """
        TODO: Determine usage of this method.

        Returns
        -------
        dict
            Return boolean value indicating if a reboot is needed.

        Examples
        --------
        ```json
        {
            "data": {
                "need_reboot": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.NeedReboot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_need_reboot(self) -> dict:
        """
        TODO: Determine usage of this method.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.NeedReboot'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_led_brightness_stats(self) -> dict:
        """
        Get LED brightness stats.

        Returns
        -------
        dict
            Return LED brightness default settigns and min / max.

        Examples
        --------
        ```json
        {
            "data": {
                "default": 3,
                "max": 3,
                "min": 0
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get_static_data'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_zram_settings(self) -> dict:
        """
        Get ZRAM settings.

        Returns
        -------
        dict
            Return ZRAM settings.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_zram": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.ZRAM'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_power_recovery_settings(self) -> dict:
        """
        Get power recovery settings.

        Returns
        -------
        dict
            Return power recovery settings.

        Examples
        --------
        ```json
        {
            "data": {
                "internal_lan_num": 2,
                "rc_power_config": true,
                "wol": [
                    {
                        "enable": false,
                        "idx": 1
                    },
                    {
                        "enable": false,
                        "idx": 2
                    }
                ],
                "wol1": false,
                "wol2": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.PowerRecovery'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_beep_control_settings(self) -> dict:
        """
        Get beep control settings.

        Returns
        -------
        dict
            Return beep control settings.

        Examples
        --------
        ```json
        {
            "data": {
                "enc_module_fail": true,
                "eunit_redundant_power_fail": true,
                "fan_fail": true,
                "poweroff_beep": true,
                "poweron_beep": true,
                "redundant_power_fail": true,
                "reset_beep": true,
                "sas_link_fail": true,
                "support_fan_fail": true,
                "support_poweroff_beep": true,
                "support_poweron_beep": true,
                "support_redundant_power_fail": false,
                "support_reset_beep": false,
                "support_volume_or_cache_crash": true,
                "volume_or_cache_crash": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.BeepControl'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_fan_speed_settings(self) -> dict:
        """
        Get fan speed settings.

        Returns
        -------
        dict
            Return fan speed settings.

        Examples
        --------
        ```json
        {
            "data": {
                "enc_module_fail": true,
                "eunit_redundant_power_fail": true,
                "fan_fail": true,
                "poweroff_beep": true,
                "poweron_beep": true,
                "redundant_power_fail": true,
                "reset_beep": true,
                "sas_link_fail": true,
                "support_fan_fail": true,
                "support_poweroff_beep": true,
                "support_poweron_beep": true,
                "support_redundant_power_fail": false,
                "support_reset_beep": false,
                "support_volume_or_cache_crash": true,
                "volume_or_cache_crash": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.FanSpeed'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_led_brightness_schedule(self) -> dict:
        """
        Get LED brightness settings.

        Returns
        -------
        dict
            Return LED brightness settings. Schedule is a 144 character string.
            1 character = 1 hour. Start from Sunday 00:00 to Saturday 23:00.
            0 = Default, 1= Ajusted, 2 = Off.

        Examples
        --------
        ```json
        {
            "data": {
                "led_brightness": 3,
                "schedule": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_power_schedule_settings(self) -> dict:
        """
        Get power schedule settings.

        Returns
        -------
        dict
            Return power schedule settings.

        Examples
        --------
        ```json
        {
            "data": {
                "poweroff_tasks": [],
                "poweron_tasks": []
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.PowerSchedule'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'load'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_hibernation_settings(self) -> dict:
        """
        Get hibernation settings.

        Returns
        -------
        dict
            Return hibernation settings.

        Examples
        --------
        ```json
        {
            "data": {
                "auto_poweroff_enable": false,
                "enable_log": false,
                "eunit_deep_sleep": 0,
                "eunit_dsleep_blacklist": "none",
                "hibernation_blacklist": "none",
                "ignore_netbios_broadcast": false,
                "internal_hd_idletime": 20,
                "sata_deep_sleep": 1,
                "sata_dsleep_blacklist": "none",
                "support_esata": "yes",
                "support_eunit_deep_sleep": false,
                "support_eunit_switch_mode": true,
                "usb_idletime": 0
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Hibernation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ups_settings(self) -> dict:
        """
        Get UPS settings.

        Returns
        -------
        dict
            Return UPS settings.

        Examples
        --------
        ```json
        {
            "data": {
                "ACL_enable": false,
                "ACL_list": [],
                "charge": 0,
                "delay_time": -1,
                "enable": false,
                "manufacture": "",
                "mode": "SLAVE",
                "model": "",
                "net_server_ip": "",
                "runtime": 0,
                "shutdown_device": false,
                "snmp_auth": false,
                "snmp_auth_key": false,
                "snmp_auth_type": "",
                "snmp_community": "",
                "snmp_mib": "",
                "snmp_privacy": false,
                "snmp_privacy_key": false,
                "snmp_privacy_type": "",
                "snmp_server_ip": "",
                "snmp_user": "",
                "snmp_version": "",
                "status": "usb_ups_status_unknown",
                "usb_ups_connect": false
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.ExternalDevice.UPS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_led_brightness(self, brightness: int = 3) -> dict:
        """
        Set LED brightness.

        Parameters
        ----------
        brightness : int
            LED brightness level (0-3). Default is `3`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'brightness': brightness
        }
        return self.request_data(api_name, api_path, req_param)

    def set_zram_settings(self, enable_zram: bool = False) -> dict:
        """
        Set ZRAM settings.

        Parameters
        ----------
        enable_zram : bool
            Enable or disable ZRAM. Default is `False`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.ZRAM'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable_zram': enable_zram
        }
        return self.request_data(api_name, api_path, req_param)

    def set_power_recovery_settings(self,
                                    enable: bool = False, wol1: bool = False, wol2: bool = False, wol3: bool = False
                                    ) -> dict:
        """
        Set power recovery settings. Note if a wol option is enabled, the enable option will be forced to `True`.

        Parameters
        ----------
        enable : bool
            Enable or disable power recovery configuration. Default is `False`.
        wol1 : bool
            Enable or disable Wake on LAN for port 1. Default is `False`.
        wol2 : bool
            Enable or disable Wake on LAN for port 2. Default is `False`.
        wol3 : bool
            Enable or disable Wake on LAN for port 3. Default is `False`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.PowerRecovery'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'wol1': wol1,
            'wol2': wol2,
            'wol3': wol3
        }
        return self.request_data(api_name, api_path, req_param)

    def set_beep_control_settings(self,
                                  fan_fail: bool = True, volume_or_cache_crash: bool = True,
                                  poweroff_beep: bool = True, poweron_beep: bool = True
                                  ) -> dict:
        """
        Set beep control settings.

        Parameters
        ----------
        fan_fail : bool
            Enable or disable fan failure beep. Default is `True`.
        volume_or_cache_crash : bool
            Enable or disable volume or cache crash beep. Default is `True`.
        poweroff_beep : bool
            Enable or disable power off beep. Default is `True`.
        poweron_beep : bool
            Enable or disable power on beep. Default is `True`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.BeepControl'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'fan_fail': fan_fail,
            'volume_or_cache_crash': volume_or_cache_crash,
            'poweroff_beep': poweroff_beep,
            'poweron_beep': poweron_beep
        }
        return self.request_data(api_name, api_path, req_param)

    def set_fan_speed_settings(self, fan_speed: str = "coolfan") -> dict:
        """
        Set fan speed settings.

        Parameters
        ----------
        fan_speed : str
            Fan speed level (0-2). Default is `quietfan`.
            Known values are `quietfan`, `coolfan`, and `fullspeed`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.FanSpeed'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'dual_fan_speed': fan_speed
        }
        return self.request_data(api_name, api_path, req_param)

    def set_led_brightness_schedule(self,
                                    led_brightness: int = 3, schedule: str = "1"*144
                                    ) -> dict:
        """
        Set LED brightness schedule.

        Parameters
        ----------
        led_brightness : int
            LED brightness level (0-3). Default is `3`.
        schedule : str
            Schedule string for LED brightness. 1 character = 1 hour. Start from Sunday 00:00 to Saturday 23:00.
            Default is `1` for all hours.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Led.Brightness'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'led_brightness': led_brightness,
            'schedule': schedule
        }
        return self.request_data(api_name, api_path, req_param)

    def set_hibernation_settings(self,
                                 internal_hd_idletime: int = 20, stat_deep_sleep: bool = True,
                                 ignore_netbios_broadcast: bool = False, usb_idletime: int = 0,
                                 enable_log: bool = False
                                 ) -> dict:
        """
        Set hibernation settings.

        Parameters
        ----------
        internal_hd_idletime : int
            Internal hard drive idle time in minutes. Default is `20`.
        stat_deep_sleep : bool
            Enable or disable SATA deep sleep. Default is `True`.
        ignore_netbios_broadcast : bool
            Enable or disable ignoring NetBIOS broadcast. Default is `False`.
        usb_idletime : int
            USB idle time in minutes. Default is `0`.
        enable_log : bool
            Enable or disable logging. Default is `False`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Hardware.Hibernation'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'internal_hd_idletime': internal_hd_idletime,
            'stat_deep_sleep': stat_deep_sleep,
            'ignore_netbios_broadcast': ignore_netbios_broadcast,
            'usb_idletime': usb_idletime,
            'enable_log': enable_log
        }
        return self.request_data(api_name, api_path, req_param)

    def set_ups_settings(self,
                         enable: bool = False, mode: str = "SLAVE", delay_time: str = "-1",
                         snmp_auth_key_dirty: bool = False, snmp_privacy_key_dirty: bool = False,
                         ) -> dict:
        """
        Set UPS settings.

        Parameters
        ----------
        enable : bool
            Enable or disable UPS. Default is `False`.
        mode : str
            UPS mode. Default is `SLAVE`.
            TODO: Determine valid values for this parameter.
        delay_time : str
            Delay time in seconds. Default is `-1`.
            TODO: Determine valid values for this parameter.
        snmp_auth_key_dirty : bool
            SNMP authentication key dirty flag. Default is `False`.
        snmp_privacy_key_dirty : bool
            SNMP privacy key dirty flag. Default is `False`.

        Returns
        -------
        dict
            Return success status.

        Examples
        --------
        ```json
        {
            "data": {
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.ExternalDevice.UPS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable,
            'mode': mode,
            'delay_time': delay_time,
            'snmp_auth_key_dirty': snmp_auth_key_dirty,
            'snmp_privacy_key_dirty': snmp_privacy_key_dirty
        }
        return self.request_data(api_name, api_path, req_param)

    def set_power_schedule(self, poweron_tasks: List[dict] = [], poweroff_tasks: List[dict] = []) -> dict:
        """
        Set the power schedule, poweron tasks and poweroff tasks.

        Parameters
        ----------
        poweron_tasks : List[dict], optional
            List of tasks for power on. Defaults to `[]`
            Example of a task:
            ```python
            {
                "enabled": True, # Enable or not the task
                "hour": 13, # Hour 0-23
                "min": 59, # Minutes 0-59
                "weekdays": "0,1,2,3,4,5,6" # All days of the week (Sunday, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday)
            }
            ```
        poweroff_tasks : List[dict], optional
            List of tasks for power off. Defaults to `[]`
            Example of a task:
            ```python
            {
                "enabled": True, # Enable or not the task
                "hour": 13, # Hour 0-23
                "min": 59, # Minutes 0-59
                "weekdays": "0,1,2,3,4,5,6" # All days of the week (Sunday, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday)
            }
            ```

        Returns
        -------
        dict
            List of tasks in power schedule.

        Examples
        --------
        ```json
        {
            "data": {
                "poweroff_tasks": [],
                "poweron_tasks": [
                    {
                        "enabled": true,
                        "hour": 0,
                        "min": 0,
                        "weekdays": "1,2,3,4,5"
                    }
                ]
            },
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Hardware.PowerSchedule'
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "version": info["maxVersion"],
            "method": "save",
            "poweron_tasks": json.dumps(poweron_tasks),
            "poweroff_tasks": json.dumps(poweroff_tasks)
        }

        return self.request_data(api_name, api_path, req_param)

    pass
