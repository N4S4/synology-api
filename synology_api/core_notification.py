"""
Synology Core Notification API wrapper.

This module provides a Python interface for managing notification settings
on Synology NAS devices, including mail, push, SMS, Line, CMS, and
advanced filter/variable configuration.
"""

from __future__ import annotations
from typing import Optional
from . import base_api
import json


class CoreNotification(base_api.BaseApi):
    """
    Core Notification API implementation for Synology NAS.

    Covers SYNO.Core.Notification.Advance, CMS, Line, Mail, Push, SMS,
    and Sysnotify endpoints not already present in core_sys_info.py.
    """

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.CustomizedData
    # ------------------------------------------------------------------ #

    def notification_advance_customized_data_get(self) -> dict[str, object] | str:
        """
        Get advanced notification customized data.

        Returns
        -------
        dict[str, object] or str
            Customized notification data.
        """
        api_name = 'SYNO.Core.Notification.Advance.CustomizedData'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_customized_data_set(
        self,
        data: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification customized data.

        Parameters
        ----------
        data : str, optional
            JSON-encoded customized data payload.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.CustomizedData'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if data is not None:
            req_param['data'] = data

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.FilterSettings
    # ------------------------------------------------------------------ #

    def notification_advance_filter_settings_get(self) -> dict[str, object] | str:
        """
        Get advanced notification filter settings.

        Returns
        -------
        dict[str, object] or str
            Filter settings configuration.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_filter_settings_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification filter settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded filter settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.FilterSettings.Profile
    # ------------------------------------------------------------------ #

    def notification_advance_filter_profile_get(self) -> dict[str, object] | str:
        """
        Get advanced notification filter settings profile.

        Returns
        -------
        dict[str, object] or str
            Filter settings profile.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_filter_profile_set(
        self,
        profile: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification filter settings profile.

        Parameters
        ----------
        profile : str, optional
            JSON-encoded profile data.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Profile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if profile is not None:
            req_param['profile'] = profile

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.FilterSettings.Template
    # ------------------------------------------------------------------ #

    def notification_advance_filter_template_get(self) -> dict[str, object] | str:
        """
        Get advanced notification filter settings template.

        Returns
        -------
        dict[str, object] or str
            Filter settings template.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_filter_template_set(
        self,
        template: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification filter settings template.

        Parameters
        ----------
        template : str, optional
            JSON-encoded template data.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if template is not None:
            req_param['template'] = template

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.Variables
    # ------------------------------------------------------------------ #

    def notification_advance_variables_get(self) -> dict[str, object] | str:
        """
        Get advanced notification variables.

        Returns
        -------
        dict[str, object] or str
            Notification variables.
        """
        api_name = 'SYNO.Core.Notification.Advance.Variables'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_variables_set(
        self,
        variables: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification variables.

        Parameters
        ----------
        variables : str, optional
            JSON-encoded variables data.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.Variables'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if variables is not None:
            req_param['variables'] = variables

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Advance.WarningPercentage
    # ------------------------------------------------------------------ #

    def notification_advance_warning_percentage_get(self) -> dict[str, object] | str:
        """
        Get advanced notification warning percentage thresholds.

        Returns
        -------
        dict[str, object] or str
            Warning percentage configuration.
        """
        api_name = 'SYNO.Core.Notification.Advance.WarningPercentage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_advance_warning_percentage_set(
        self,
        percentage: Optional[int] = None
    ) -> dict[str, object] | str:
        """
        Set advanced notification warning percentage thresholds.

        Parameters
        ----------
        percentage : int, optional
            Warning percentage threshold value.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Advance.WarningPercentage'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if percentage is not None:
            req_param['percentage'] = percentage

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.CMS
    # ------------------------------------------------------------------ #

    def notification_cms_get(self) -> dict[str, object] | str:
        """
        Get CMS notification settings.

        Returns
        -------
        dict[str, object] or str
            CMS notification settings.
        """
        api_name = 'SYNO.Core.Notification.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_cms_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set CMS notification settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded CMS notification settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.CMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.CMS.Conf
    # ------------------------------------------------------------------ #

    def notification_cms_conf_get(self) -> dict[str, object] | str:
        """
        Get CMS notification configuration.

        Returns
        -------
        dict[str, object] or str
            CMS notification configuration.
        """
        api_name = 'SYNO.Core.Notification.CMS.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_cms_conf_set(
        self,
        conf: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set CMS notification configuration.

        Parameters
        ----------
        conf : str, optional
            JSON-encoded CMS notification configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.CMS.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if conf is not None:
            req_param['conf'] = conf

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Line
    # ------------------------------------------------------------------ #

    def notification_line_get(self) -> dict[str, object] | str:
        """
        Get Line notification configuration.

        Returns
        -------
        dict[str, object] or str
            Line notification configuration.
        """
        api_name = 'SYNO.Core.Notification.Line'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_line_set(
        self,
        token: Optional[str] = None,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set Line notification configuration.

        Parameters
        ----------
        token : str, optional
            Line notification access token.
        enable : bool, optional
            Enable or disable Line notifications.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Line'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if token is not None:
            req_param['token'] = token
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Mail
    # ------------------------------------------------------------------ #

    def notification_mail_get(self) -> dict[str, object] | str:
        """
        Get mail notification settings.

        Returns
        -------
        dict[str, object] or str
            Mail notification settings.
        """
        api_name = 'SYNO.Core.Notification.Mail'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set mail notification settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded mail notification settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Mail'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Mail.Auth
    # ------------------------------------------------------------------ #

    def notification_mail_auth_get(self) -> dict[str, object] | str:
        """
        Get mail notification authentication settings.

        Returns
        -------
        dict[str, object] or str
            Mail authentication settings.
        """
        api_name = 'SYNO.Core.Notification.Mail.Auth'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_auth_set(
        self,
        auth_type: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set mail notification authentication settings.

        Parameters
        ----------
        auth_type : str, optional
            Authentication type (e.g., 'plain', 'login').
        username : str, optional
            SMTP authentication username.
        password : str, optional
            SMTP authentication password.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Mail.Auth'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if auth_type is not None:
            req_param['auth_type'] = auth_type
        if username is not None:
            req_param['username'] = username
        if password is not None:
            req_param['password'] = password

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Mail.Oauth
    # ------------------------------------------------------------------ #

    def notification_mail_oauth_get(self) -> dict[str, object] | str:
        """
        Get mail notification OAuth settings.

        Returns
        -------
        dict[str, object] or str
            Mail OAuth settings.
        """
        api_name = 'SYNO.Core.Notification.Mail.Oauth'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_oauth_set(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        refresh_token: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set mail notification OAuth settings.

        Parameters
        ----------
        client_id : str, optional
            OAuth client ID.
        client_secret : str, optional
            OAuth client secret.
        refresh_token : str, optional
            OAuth refresh token.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Mail.Oauth'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if client_id is not None:
            req_param['client_id'] = client_id
        if client_secret is not None:
            req_param['client_secret'] = client_secret
        if refresh_token is not None:
            req_param['refresh_token'] = refresh_token

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Mail.Profile.Conf
    # ------------------------------------------------------------------ #

    def notification_mail_profile_conf_get(self) -> dict[str, object] | str:
        """
        Get mail notification profile configuration.

        Returns
        -------
        dict[str, object] or str
            Mail profile configuration.
        """
        api_name = 'SYNO.Core.Notification.Mail.Profile.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_mail_profile_conf_set(
        self,
        profile: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set mail notification profile configuration.

        Parameters
        ----------
        profile : str, optional
            JSON-encoded mail profile configuration.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Mail.Profile.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if profile is not None:
            req_param['profile'] = profile

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Push
    # ------------------------------------------------------------------ #

    def notification_push_get(self) -> dict[str, object] | str:
        """
        Get push notification settings.

        Returns
        -------
        dict[str, object] or str
            Push notification settings.
        """
        api_name = 'SYNO.Core.Notification.Push'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_set(
        self,
        enable: Optional[bool] = None
    ) -> dict[str, object] | str:
        """
        Set push notification settings.

        Parameters
        ----------
        enable : bool, optional
            Enable or disable push notifications.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Push'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if enable is not None:
            req_param['enable'] = str(enable).lower()

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Push.AuthToken
    # ------------------------------------------------------------------ #

    def notification_push_auth_token_get(self) -> dict[str, object] | str:
        """
        Get push notification authentication token.

        Returns
        -------
        dict[str, object] or str
            Push authentication token information.
        """
        api_name = 'SYNO.Core.Notification.Push.AuthToken'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_auth_token_set(
        self,
        token: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set push notification authentication token.

        Parameters
        ----------
        token : str, optional
            Push authentication token.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Push.AuthToken'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if token is not None:
            req_param['token'] = token

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Push.Mobile
    # ------------------------------------------------------------------ #

    def notification_push_mobile_get(self) -> dict[str, object] | str:
        """
        Get mobile push notification settings.

        Returns
        -------
        dict[str, object] or str
            Mobile push notification settings.
        """
        api_name = 'SYNO.Core.Notification.Push.Mobile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_mobile_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set mobile push notification settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded mobile push settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Push.Mobile'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Push.Webhook.Provider
    # ------------------------------------------------------------------ #

    def notification_push_webhook_provider_get(self) -> dict[str, object] | str:
        """
        Get push notification webhook provider configuration.

        Returns
        -------
        dict[str, object] or str
            Webhook provider configuration.
        """
        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_push_webhook_provider_set(
        self,
        provider: Optional[str] = None,
        url: Optional[str] = None,
        token: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set push notification webhook provider configuration.

        Parameters
        ----------
        provider : str, optional
            Webhook provider name.
        url : str, optional
            Webhook endpoint URL.
        token : str, optional
            Webhook authentication token.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if provider is not None:
            req_param['provider'] = provider
        if url is not None:
            req_param['url'] = url
        if token is not None:
            req_param['token'] = token

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.SMS
    # ------------------------------------------------------------------ #

    def notification_sms_get(self) -> dict[str, object] | str:
        """
        Get SMS notification settings.

        Returns
        -------
        dict[str, object] or str
            SMS notification settings.
        """
        api_name = 'SYNO.Core.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_sms_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SMS notification settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded SMS notification settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.SMS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.SMS.Provider
    # ------------------------------------------------------------------ #

    def notification_sms_provider_get(self) -> dict[str, object] | str:
        """
        Get SMS notification provider configuration.

        Returns
        -------
        dict[str, object] or str
            SMS provider configuration.
        """
        api_name = 'SYNO.Core.Notification.SMS.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_sms_provider_set(
        self,
        provider: Optional[str] = None,
        api_key: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set SMS notification provider configuration.

        Parameters
        ----------
        provider : str, optional
            SMS provider name.
        api_key : str, optional
            SMS provider API key.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.SMS.Provider'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if provider is not None:
            req_param['provider'] = provider
        if api_key is not None:
            req_param['api_key'] = api_key

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  SYNO.Core.Notification.Sysnotify
    # ------------------------------------------------------------------ #

    def notification_sysnotify_get(self) -> dict[str, object] | str:
        """
        Get system notification settings.

        Returns
        -------
        dict[str, object] or str
            System notification settings.
        """
        api_name = 'SYNO.Core.Notification.Sysnotify'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def notification_sysnotify_set(
        self,
        settings: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Set system notification settings.

        Parameters
        ----------
        settings : str, optional
            JSON-encoded system notification settings.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Core.Notification.Sysnotify'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}
        if settings is not None:
            req_param['settings'] = settings

        return self.request_data(api_name, api_path, req_param)
