"""
Regional options class for Synology DSM.
"""
from synology_api import base_api
import enum


class LanguageEnum(enum.Enum):
    """
    Enum for available languages in Synology DSM.
    """
    ENGLISH = "enu"
    FRENCH = "fre"
    GERMAN = "ger"
    GREEK = "gre"
    HEBREW = "heb"
    THAI = "tha"
    ITALIAN = "ita"
    SPANISH = "spn"
    TRADITIONAL_CHINESE = "cht"
    SIMPLIFIED_CHINESE = "chs"
    JAPANESE = "jpn"
    KOREAN = "krn"
    PORTUGUESE_BRAZIL = "ptb"
    RUSSIAN = "rus"
    DANISH = "dan"
    NORWEGIAN = "nor"
    SWEDISH = "sve"
    DUTCH = "nld"
    POLISH = "plk"
    PORTUGUESE_GALICIAN = "ptg"
    HUNGARIAN = "hun"
    TURKISH = "trk"
    CZECH = "csy"
    ARABIC = "ara"
    DEFAULT = "def"


class RegionalOptions(base_api.BaseApi):
    """
Regional options class for Synology DSM.
    """

    def get_time_info(self) -> dict:
        """
Get Date & Time information, Time Zone and Time Settings.

        Returns
        -------
        dict
            Date & Time information, Time Zone and Time Settings.

        Examples
        --------
        ```json
        {
            "data": {
                "date": "2025/9/15",
                "date_format": "d/m/Y",
                "enable_ntp": "ntp",
                "hour": 20,
                "minute": 48,
                "now": "Mon Sep 15 20:48:00 2025\n",
                "second": 0,
                "server": "time.google.com",
                "time_format": "H:i",
                "timestamp": 1757962080,
                "timezone": "Amsterdam"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_language_info(self) -> dict:
        """
        Get Language information.

        Returns
        -------
        dict
            Language information.

        Examples
        --------
        ```json
        {
            "data": {
                "codepage": "fre",
                "language": "def",
                "maillang": "fre"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.Language'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ntp_service_info(self) -> dict:
        """
        Get NTP Service information.

        Returns
        -------
        dict
            NTP Service information.

        Examples
        --------
        ```json
        {
            "data": {
                "enable": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_ntp_service_status(self) -> dict:
        """
        Get NTP Service status.

        Returns
        -------
        dict
            NTP Service status.

        Examples
        --------
        ```json
        {
            "data": {
                "ntp_status": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status'
        }
        return self.request_data(api_name, api_path, req_param)

    def list_timezone(self) -> dict:
        """
        List available time zones.

        Returns
        -------
        dict
            Available time zones.

        Examples
        --------
        ```json
        {
            "data": {
                "zonedata": [
                    {
                        "display": "(GMT-11:00) Samoa Standard Time; Midway Is.",
                        "offset": -39600,
                        "value": "Midway"
                    },
                    {
                        "display": "(GMT-10:00) Hawaii Standard Time",
                        "offset": -36000,
                        "value": "Hawaii"
                    },
                    {
                        "display": "(GMT-09:00) Alaska Standard Time",
                        "offset": -32400,
                        "value": "Alaska"
                    },
                    {
                        "display": "(GMT-08:00) Pacific Time (US & Canada); Tijuana",
                        "offset": -28800,
                        "value": "Pacific"
                    },
                    {
                        "display": "(GMT-07:00) Arizona",
                        "offset": -25200,
                        "value": "Arizona"
                    },
                    {
                        "display": "(GMT-07:00) Mountain Time (US & Canada)",
                        "offset": -25200,
                        "value": "Mountain"
                    },
                    {
                        "display": "(GMT-06:00) Central Time (US & Canada)",
                        "offset": -21600,
                        "value": "Central"
                    },
                    {
                        "display": "(GMT-06:00) Chihuahua, Mazatlan",
                        "offset": -21600,
                        "value": "Chihuahua"
                    },
                    {
                        "display": "(GMT-06:00) Central America Standard Time; Guatemala",
                        "offset": -21600,
                        "value": "Guatemala"
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'listzone'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_time_info(self, date_format: str, time_format: str, timezone: str, enable_ntp: str, server: str, date: str, hour: int, minute: int, second: int, change_time: bool = False) -> dict:
        """
        Set Date & Time information, Time Zone and Time Settings.

        Parameters
        ----------
        date_format : str
            Date format, known formats are `YYYY-MM-dd`, `YYYY/MM/dd`, `YYYY.MM.dd`, `dd-MM-YYYY`, `dd/MM/YYYY`, `dd.MM.YYYY`, `MM-dd-YYYY`, `MM/dd/YYYY`, `MM.dd.YYYY`.
        time_format : str
            Time format, known formats are `H:i`, `h:i A`.
        timezone : str
            Time zone, can be get from `list_timezone` field "value".
        enable_ntp : str
            NTP setting ('ntp' to enable, 'manual' to disable).
        server : str
            NTP server address, only if `enable_ntp` is set to 'ntp'.
        date : str
            Date in 'YYYY/MM/DD' format, only if `enable_ntp` is set to 'manual'.
        hour : int
            Hour (0-23), only if `enable_ntp` is set to 'manual'.
        minute : int
            Minute (0-59), only if `enable_ntp` is set to 'manual'.
        second : int
            Second (0-59), only if `enable_ntp` is set to 'manual'.
        change_time : bool, optional
            Whether to change the time immediately, defaults to False.

        Returns
        -------
        dict
            Response from the API.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'date_format': date_format,
            'time_format': time_format,
            'timezone': timezone,
            'enable_ntp': enable_ntp,
            'change_time': change_time
        }
        if enable_ntp == 'manual':
            req_param.update({
                'date': date,
                'hour': hour,
                'minute': minute,
                'second': second
            })
        elif enable_ntp == 'ntp':
            # server is required in this case
            req_param.update({
                'server': server
            })
        return self.request_data(api_name, api_path, req_param)

    def list_language(self) -> LanguageEnum:
        """
        List available languages.

        Returns
        -------
        LanguageEnum
            Available languages.
        """
        return LanguageEnum

    def set_language_info(self, language: LanguageEnum, maillang: LanguageEnum, codepage: LanguageEnum) -> dict:
        """
        Set Language information.

        Parameters
        ----------
        language : LanguageEnum
            Display language, you can use the `DEFAULT` from the LanguageEnum.
        maillang : LanguageEnum
            Notification language, you cannot use `DEFAULT` from the LanguageEnum.
        codepage : LanguageEnum
            Codepage, you cannot use `DEFAULT` from the LanguageEnum.

        Returns
        -------
        dict
            Response from the API.
        """
        api_name = 'SYNO.Core.Region.Language'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'language': language.value,
            'maillang': maillang.value,
            'codepage': codepage.value
        }
        return self.request_data(api_name, api_path, req_param)

    def set_ntp_service_info(self, enable: bool) -> dict:
        """
        Set NTP Service information.

        Parameters
        ----------
        enable : bool
            Whether to enable the NTP service.

        Returns
        -------
        dict
            Response from the API.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Region.NTP.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable': enable
        }
        return self.request_data(api_name, api_path, req_param)
