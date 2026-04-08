"""
Synology Core System API wrapper (extended endpoints).

This module covers SYNO.Core.System, Region, Theme, Desktop, Help,
UISearch, and settings endpoints that are NOT already provided by
other modules such as core_sys_info.SysInfo.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class CoreSystem(base_api.BaseApi):
    """
    Extended Core System API implementation for Synology NAS.

    This class provides methods for system reset button, region/NTP,
    theme customisation, desktop settings, help, UI search, and
    personal/group/user settings.
    """

    # ─── SYNO.Core.System.ResetButton ──────────────────────────────────

    def reset_button_get(self) -> dict[str, object] | str:
        """
        Get reset button configuration.

        Returns
        -------
        dict[str, object] or str
            Reset button configuration.
        """
        api_name = 'SYNO.Core.System.ResetButton'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def reset_button_set(self,
                         enabled: bool = True) -> dict[str, object] | str:
        """
        Enable or disable the hardware reset button.

        Parameters
        ----------
        enabled : bool, optional
            Enable if True, disable if False. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.System.ResetButton'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enabled': str(enabled).lower()}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Region.Language ─────────────────────────────────────

    def region_language_get(self) -> dict[str, object] | str:
        """
        Get system language settings.

        Returns
        -------
        dict[str, object] or str
            Language configuration.
        """
        api_name = 'SYNO.Core.Region.Language'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def region_language_set(self, language: str) -> dict[str, object] | str:
        """
        Set system language.

        Parameters
        ----------
        language : str
            Language code (e.g., 'enu', 'cht', 'jpn').

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Region.Language'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'language': language}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Region.NTP ──────────────────────────────────────────

    def region_ntp_get(self) -> dict[str, object] | str:
        """
        Get NTP settings.

        Returns
        -------
        dict[str, object] or str
            NTP configuration.
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def region_ntp_set(self, enabled: bool = True,
                       server: Optional[str] = None) -> dict[str, object] | str:
        """
        Set NTP configuration.

        Parameters
        ----------
        enabled : bool, optional
            Enable NTP synchronisation. Defaults to True.
        server : str, optional
            NTP server address.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Region.NTP'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enabled': str(enabled).lower()}
        if server is not None:
            req_param['server'] = server

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Region.NTP.DateTimeFormat ───────────────────────────

    def ntp_datetime_format_get(self) -> dict[str, object] | str:
        """
        Get date/time format settings.

        Returns
        -------
        dict[str, object] or str
            Date/time format configuration.
        """
        api_name = 'SYNO.Core.Region.NTP.DateTimeFormat'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ntp_datetime_format_set(self,
                                date_format: Optional[str] = None,
                                time_format: Optional[str] = None) -> dict[str, object] | str:
        """
        Set date/time format.

        Parameters
        ----------
        date_format : str, optional
            Date format string (e.g., 'YYYY/MM/DD').
        time_format : str, optional
            Time format string (e.g., 'HH:mm').

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Region.NTP.DateTimeFormat'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if date_format is not None:
            req_param['date_format'] = date_format
        if time_format is not None:
            req_param['time_format'] = time_format

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Region.NTP.Server ───────────────────────────────────

    def ntp_server_get(self) -> dict[str, object] | str:
        """
        Get NTP server configuration.

        Returns
        -------
        dict[str, object] or str
            NTP server settings.
        """
        api_name = 'SYNO.Core.Region.NTP.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def ntp_server_set(self, enabled: bool = True) -> dict[str, object] | str:
        """
        Enable or disable the NAS as an NTP server.

        Parameters
        ----------
        enabled : bool, optional
            Enable NTP server if True. Defaults to True.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Region.NTP.Server'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enabled': str(enabled).lower()}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Theme.AppPortalLogin ────────────────────────────────

    def theme_app_portal_login_get(self) -> dict[str, object] | str:
        """
        Get app portal login theme settings.

        Returns
        -------
        dict[str, object] or str
            App portal login theme configuration.
        """
        api_name = 'SYNO.Core.Theme.AppPortalLogin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def theme_app_portal_login_set(self,
                                   **kwargs: object) -> dict[str, object] | str:
        """
        Set app portal login theme.

        Parameters
        ----------
        **kwargs : object
            Theme key-value pairs (e.g., title, background).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Theme.AppPortalLogin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Theme.Desktop ───────────────────────────────────────

    def theme_desktop_get(self) -> dict[str, object] | str:
        """
        Get desktop theme settings.

        Returns
        -------
        dict[str, object] or str
            Desktop theme configuration.
        """
        api_name = 'SYNO.Core.Theme.Desktop'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def theme_desktop_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set desktop theme.

        Parameters
        ----------
        **kwargs : object
            Theme key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Theme.Desktop'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Theme.FileSharingLogin ──────────────────────────────

    def theme_file_sharing_login_get(self) -> dict[str, object] | str:
        """
        Get file sharing login theme settings.

        Returns
        -------
        dict[str, object] or str
            File sharing login theme configuration.
        """
        api_name = 'SYNO.Core.Theme.FileSharingLogin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def theme_file_sharing_login_set(self,
                                     **kwargs: object) -> dict[str, object] | str:
        """
        Set file sharing login theme.

        Parameters
        ----------
        **kwargs : object
            Theme key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Theme.FileSharingLogin'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Theme.Image ─────────────────────────────────────────

    def theme_image_get(self) -> dict[str, object] | str:
        """
        Get theme image settings.

        Returns
        -------
        dict[str, object] or str
            Theme image configuration.
        """
        api_name = 'SYNO.Core.Theme.Image'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def theme_image_list(self) -> dict[str, object] | str:
        """
        List available theme images.

        Returns
        -------
        dict[str, object] or str
            List of theme images.
        """
        api_name = 'SYNO.Core.Theme.Image'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Theme.Login ─────────────────────────────────────────

    def theme_login_get(self) -> dict[str, object] | str:
        """
        Get login page theme settings.

        Returns
        -------
        dict[str, object] or str
            Login page theme configuration.
        """
        api_name = 'SYNO.Core.Theme.Login'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def theme_login_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set login page theme.

        Parameters
        ----------
        **kwargs : object
            Theme key-value pairs (e.g., title, background).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Theme.Login'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.Defs ────────────────────────────────────────

    def desktop_defs_get(self) -> dict[str, object] | str:
        """
        Get desktop definitions.

        Returns
        -------
        dict[str, object] or str
            Desktop definitions.
        """
        api_name = 'SYNO.Core.Desktop.Defs'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.Initdata ───────────────────────────────────

    def desktop_initdata_get(self) -> dict[str, object] | str:
        """
        Get desktop initialisation data.

        Returns
        -------
        dict[str, object] or str
            Desktop initialisation data.
        """
        api_name = 'SYNO.Core.Desktop.Initdata'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.JSUIString ──────────────────────────────────

    def desktop_jsui_string_get(self) -> dict[str, object] | str:
        """
        Get desktop JS UI string resources.

        Returns
        -------
        dict[str, object] or str
            JS UI string data.
        """
        api_name = 'SYNO.Core.Desktop.JSUIString'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.PersonalUpdater ─────────────────────────────

    def desktop_personal_updater_get(self) -> dict[str, object] | str:
        """
        Get desktop personal updater settings.

        Returns
        -------
        dict[str, object] or str
            Personal updater configuration.
        """
        api_name = 'SYNO.Core.Desktop.PersonalUpdater'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def desktop_personal_updater_set(self,
                                     **kwargs: object) -> dict[str, object] | str:
        """
        Set desktop personal updater settings.

        Parameters
        ----------
        **kwargs : object
            Updater configuration key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Desktop.PersonalUpdater'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.SessionData ─────────────────────────────────

    def desktop_session_data_get(self) -> dict[str, object] | str:
        """
        Get desktop session data.

        Returns
        -------
        dict[str, object] or str
            Desktop session data.
        """
        api_name = 'SYNO.Core.Desktop.SessionData'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.Timeout ─────────────────────────────────────

    def desktop_timeout_get(self) -> dict[str, object] | str:
        """
        Get desktop session timeout settings.

        Returns
        -------
        dict[str, object] or str
            Timeout configuration.
        """
        api_name = 'SYNO.Core.Desktop.Timeout'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def desktop_timeout_set(self,
                            timeout_minutes: int = 15) -> dict[str, object] | str:
        """
        Set desktop session timeout.

        Parameters
        ----------
        timeout_minutes : int, optional
            Timeout in minutes. Defaults to 15.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Desktop.Timeout'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'timeout': timeout_minutes}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.UIString ────────────────────────────────────

    def desktop_ui_string_get(self) -> dict[str, object] | str:
        """
        Get desktop UI string resources.

        Returns
        -------
        dict[str, object] or str
            UI string data.
        """
        api_name = 'SYNO.Core.Desktop.UIString'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Desktop.Upgrade ─────────────────────────────────────

    def desktop_upgrade_get(self) -> dict[str, object] | str:
        """
        Get desktop upgrade notification status.

        Returns
        -------
        dict[str, object] or str
            Desktop upgrade notification data.
        """
        api_name = 'SYNO.Core.Desktop.Upgrade'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.Help ────────────────────────────────────────────────

    def help_get(self, topic: Optional[str] = None) -> dict[str, object] | str:
        """
        Get help content.

        Parameters
        ----------
        topic : str, optional
            Help topic identifier. If None, returns general help.

        Returns
        -------
        dict[str, object] or str
            Help content.
        """
        api_name = 'SYNO.Core.Help'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if topic is not None:
            req_param['topic'] = topic

        return self.request_data(api_name, api_path, req_param)

    def help_list(self) -> dict[str, object] | str:
        """
        List available help topics.

        Returns
        -------
        dict[str, object] or str
            List of help topics.
        """
        api_name = 'SYNO.Core.Help'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.UISearch ────────────────────────────────────────────

    def ui_search_get(self, query: str) -> dict[str, object] | str:
        """
        Search the DSM UI.

        Parameters
        ----------
        query : str
            Search query string.

        Returns
        -------
        dict[str, object] or str
            Search results.
        """
        api_name = 'SYNO.Core.UISearch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'query': query}

        return self.request_data(api_name, api_path, req_param)

    def ui_search_list(self) -> dict[str, object] | str:
        """
        List all searchable UI items.

        Returns
        -------
        dict[str, object] or str
            List of searchable UI items.
        """
        api_name = 'SYNO.Core.UISearch'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.PersonalSettings ────────────────────────────────────

    def personal_settings_get(self) -> dict[str, object] | str:
        """
        Get personal settings for the current user.

        Returns
        -------
        dict[str, object] or str
            Personal settings.
        """
        api_name = 'SYNO.Core.PersonalSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def personal_settings_set(self,
                              **kwargs: object) -> dict[str, object] | str:
        """
        Set personal settings for the current user.

        Parameters
        ----------
        **kwargs : object
            Settings key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.PersonalSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.GroupSettings ───────────────────────────────────────

    def group_settings_get(self,
                           group: Optional[str] = None) -> dict[str, object] | str:
        """
        Get group settings.

        Parameters
        ----------
        group : str, optional
            Group name. If None, returns all group settings.

        Returns
        -------
        dict[str, object] or str
            Group settings.
        """
        api_name = 'SYNO.Core.GroupSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if group is not None:
            req_param['group'] = group

        return self.request_data(api_name, api_path, req_param)

    def group_settings_set(self, group: str,
                           **kwargs: object) -> dict[str, object] | str:
        """
        Set group settings.

        Parameters
        ----------
        group : str
            Group name.
        **kwargs : object
            Settings key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.GroupSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'group': group}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)

    # ─── SYNO.Core.UserSettings ────────────────────────────────────────

    def user_settings_get(self,
                          user: Optional[str] = None) -> dict[str, object] | str:
        """
        Get user settings.

        Parameters
        ----------
        user : str, optional
            Username. If None, returns current user settings.

        Returns
        -------
        dict[str, object] or str
            User settings.
        """
        api_name = 'SYNO.Core.UserSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}
        if user is not None:
            req_param['user'] = user

        return self.request_data(api_name, api_path, req_param)

    def user_settings_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set user settings.

        Parameters
        ----------
        **kwargs : object
            Settings key-value pairs.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.UserSettings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        req_param.update(kwargs)

        return self.request_data(api_name, api_path, req_param)
