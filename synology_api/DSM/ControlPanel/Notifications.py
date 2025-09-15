"""
Notifications API endpoint.
"""
from synology_api import base_api
import json


class Notifications(base_api.BaseApi):
    """
    Notifications API endpoint.
    """

    def list_filter_settings(self) -> dict:
        """
        List current filter settings.

        Returns
        -------
        dict
            Current filter settings including enabled rule levels and types.

        Examples
        --------
        ```json
        {
            "data": {
                "All": [
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "AutoBlockAdd",
                        "source": "dsm",
                        "tag": "AutoBlockAdd",
                        "title": "IP address blocked",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_WARN",
                        "name": "AutoBlockDatabaseRulesWarning",
                        "source": "dsm",
                        "tag": "AutoBlockDatabaseRulesWarning",
                        "title": "Too many IP addresses in the Block List on %HOSTNAME%",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_ERROR",
                        "name": "CMSClientConnectFailed",
                        "source": "dsm",
                        "tag": "CMSClientConnectFailed",
                        "title": "Unable to connect to the CMS Host",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "CMSClientDetachSuccess",
                        "source": "dsm",
                        "tag": "CMSClientDetachSuccess",
                        "title": "Disjoined from CMS host",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "CMSClientJoinSuccess",
                        "source": "dsm",
                        "tag": "CMSClientJoinSuccess",
                        "title": "Joined CMS host",
                        "warnPercent": 1
                    }
                ],
                "send_welcome_mail": false,
                "sender_mail": "test@gmail.com",
                "sender_name": "",
                "smtp_auth": {
                    "enable": true,
                    "user": "test@gmail.com"
                },
                "smtp_info": {
                    "port": 465,
                    "server": "smtp.gmail.com",
                    "ssl": true
                },
                "subject_prefix": "[SYNO-FLORENTB]"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def list_event(self) -> dict:
        """
        List recent notification events.

        Returns
        -------
        dict
            Recent notification events including timestamps, app IDs, levels, and messages.

        Examples
        --------
        ```json
        {
            "data": {
                "All": [
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "AutoBlockAdd",
                        "source": "dsm",
                        "tag": "AutoBlockAdd",
                        "title": "IP address blocked",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_WARN",
                        "name": "AutoBlockDatabaseRulesWarning",
                        "source": "dsm",
                        "tag": "AutoBlockDatabaseRulesWarning",
                        "title": "Too many IP addresses in the Block List on %HOSTNAME%",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_ERROR",
                        "name": "CMSClientConnectFailed",
                        "source": "dsm",
                        "tag": "CMSClientConnectFailed",
                        "title": "Unable to connect to the CMS Host",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "CMSClientDetachSuccess",
                        "source": "dsm",
                        "tag": "CMSClientDetachSuccess",
                        "title": "Disjoined from CMS host",
                        "warnPercent": 1
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_filter_rule_settings(self, template_id: int) -> dict:
        """
        Get the filter settings for a specific template.

        Parameters
        ----------
        template_id : int
            The ID of the template to retrieve settings for.

        Returns
        -------
        dict
            API response containing the filter settings for the specified template.

        Examples
        --------
        ```json
        {
            "data": {
                "All": [
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "enabled": false,
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_INFO",
                        "name": "AutoBlockAdd",
                        "source": "dsm",
                        "tag": "AutoBlockAdd",
                        "title": "IP address blocked",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "enabled": true,
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_WARN",
                        "name": "AutoBlockDatabaseRulesWarning",
                        "source": "dsm",
                        "tag": "AutoBlockDatabaseRulesWarning",
                        "title": "Too many IP addresses in the Block List on %HOSTNAME%",
                        "warnPercent": 1
                    },
                    {
                        "appid": "SYNO.SDS.AdminCenter.Application",
                        "enabled": true,
                        "format": "mail",
                        "group": "System",
                        "level": "NOTIFICATION_ERROR",
                        "name": "CMSClientConnectFailed",
                        "source": "dsm",
                        "tag": "CMSClientConnectFailed",
                        "title": "Unable to connect to the CMS Host",
                        "warnPercent": 1
                    }
                ],
                "template_id": 5,
                "template_name": "test"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get',
            'template_id': template_id
        }
        return self.request_data(api_name, api_path, req_param)

    def get_push_mail(self) -> dict:
        """
        Get push mail configuration.

        Returns
        -------
        dict
            Push notification configuration details including service status and linked devices.

        Examples
        --------
        ```json
        {
            "data": {
                "enable_mail": true,
                "mail": [
                    "test@gmail.com"
                ],
                "subject_prefix": "",
                "template_id": 1
            },
            "success": true
        }
        """
        api_name = 'SYNO.Core.Notification.Push.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def refresh_token(self) -> dict:
        """
        Refresh the push notification token.

        Returns
        -------
        dict
            Status of the token refresh operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'refresh_token'
        }
        return self.request_data(api_name, api_path, req_param)

    def set_mail_config(self,
                        enable_mail: bool,
                        enable_oauth: bool,
                        subject_prefix: str,
                        smtp_info: dict,
                        send_welcome_mail: bool,
                        sender_name: str,
                        sender_mail: str,
                        oauth_provider: str) -> dict:
        """
        Set the mail configuration for notifications.

        Parameters
        ----------
        enable_mail : bool
            Enable mail notifications.
        enable_oauth : bool
            Enable OAuth authentication.
        subject_prefix : str
            Prefix for the email subject.
        smtp_info : dict
            SMTP server information, e.g.:
            {"server": "smtp.gmail.com", "port": 465, "ssl": True}
        send_welcome_mail : bool
            Send a welcome mail after configuration.
        sender_name : str
            Name of the sender.
        sender_mail : str
            Email address of the sender.
        oauth_provider : str
            OAuth provider (e.g., "gmail").

        Returns
        -------
        dict
            API response.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'enable_mail': enable_mail,
            'enable_oauth': enable_oauth,
            'subject_prefix': subject_prefix,
            'smtp_info': json.dumps(smtp_info),
            'send_welcome_mail': send_welcome_mail,
            'sender_name': sender_name,
            'sender_mail': sender_mail,
            'oauth_provider': oauth_provider
        }
        return self.request_data(api_name, api_path, req_param)

    def send_test_mail(self, smtp_info: dict, mail: list[str], subject_prefix: str) -> dict:
        """
        Send a test mail to verify the mail configuration.

        Parameters
        ----------
        smtp_info : dict
            SMTP server information, e.g.:
            {"server": "smtp.gmail.com", "port": 465, "ssl": True}
        mail : list[str]
            List of email addresses to send the test email to.
        subject_prefix : str
            Prefix for the email subject.

        Returns
        -------
        dict
            Status of the test email operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'send_test',
            'smtp_info': json.dumps(smtp_info) if smtp_info else None,
            'mail': json.dumps(mail) if mail else None,
            'subject_prefix': subject_prefix
        }
        return self.request_data(api_name, api_path, req_param)

    def send_test_push_mail(self, target_id_list: list[int] = None) -> dict:
        """
        Send a test push mail to synology account.

        Parameters
        ----------
        target_id_list : list[int], optional
            List of target IDs to send the test push mail to. If None, sends to all linked devices.

        Returns
        -------
        dict
            Status of the test email operation.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Mail'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'send_test'
        }
        if target_id_list:
            req_param['target_id_list'] = json.dumps(target_id_list) if len(
                target_id_list) > 1 else target_id_list[0]

        return self.request_data(api_name, api_path, req_param)

    def create_mail_profile(self, template_id: int, mail: list[str]) -> dict:
        """
        Create a new mail profile for notifications.

        Parameters
        ----------
        template_id : int
            ID of the filter template to use. Use `list_filter_template` to get available templates.
        mail : list[str]
            List of email addresses to receive notifications.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail.Profile.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'create',
            'template_id': template_id,
            'mail': json.dumps(mail)
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_mail_profile(self, profile_id: int, template_id: int, mail: list[str]) -> dict:
        """
        Edit an existing mail profile for notifications.

        Parameters
        ----------
        profile_id : int
            ID of the profile to edit. Use `get_mail_config` to get existing profiles.
        template_id : int
            ID of the filter template to use. Use `list_filter_template` to get available templates.
        mail : list[str]
            List of email addresses to receive notifications.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail.Profile.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'profile_id': profile_id,
            'template_id': template_id,
            'mail': json.dumps(mail)
        }
        return self.request_data(api_name, api_path, req_param)

    def delete_mail_profile(self, profile_id: int) -> dict:
        """
        Delete a mail profile for notifications.

        Parameters
        ----------
        profile_id : int
            ID of the profile to delete. Use `get_mail_config` to get existing profiles.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Mail.Profile.Conf'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'profile_id': profile_id
        }
        return self.request_data(api_name, api_path, req_param)

    def create_filter_rule(self, template_name: str, settings: list[dict]) -> dict:
        """
        Create a new notification filter rule template.

        Parameters
        ----------
        template_name : str
            The name of the filter template.
        settings : list of dict
            List of filter settings, e.g.:
            [
                {"tag": "AutoBlockAdd", "enabled": False},
                {"tag": "AutoBlockDatabaseRulesWarning", "enabled": True},
                ...
            ]

        Returns
        -------
        dict
            template ID.

        Examples
        --------
        ```json
        {
            "data": {
                "template_id": 2
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'create',
            'template_name': template_name,
            'settings': json.dumps(settings)
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_filter_rule(self, template_id: int, template_name: str, settings: list[dict]) -> dict:
        """
        Edit an existing notification filter rule template.

        Parameters
        ----------
        template_id : int
            ID of the filter template to edit. Use `list_filter_template` to get existing templates.
        template_name : str
            The name of the filter template.
        settings : list of dict
            List of filter settings, e.g.:
            [
                {"tag": "AutoBlockAdd", "enabled": False},
                {"tag": "AutoBlockDatabaseRulesWarning", "enabled": True},
                ...
            ]

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set',
            'template_id': template_id,
            'template_name': template_name,
            'settings': json.dumps(settings)
        }
        return self.request_data(api_name, api_path, req_param)

    def delete_filter_rule(self, template_id: int) -> dict:
        """
        Delete a notification filter rule template.

        Parameters
        ----------
        template_id : int
            ID of the filter template to delete. Use `list_filter_template` to get existing templates.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.FilterSettings.Template'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'delete',
            'template_id': template_id
        }
        return self.request_data(api_name, api_path, req_param)

    def list_push_service(self) -> dict:
        """
        List available push notification services.

        Returns
        -------
        dict
            Available push notification services.

        Examples
        --------
        ```json
        {
            "data": {
                "count": 1,
                "list": [
                {
                    "app_version": "2.5.4-468",
                    "device_name": "IN2013",
                    "firmware_version": "13",
                    "profile_id": 5,
                    "target_id": 61451444,
                    "template_id": 2
                }
                ],
                "success": true
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Mobile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)

    def get_push_service_auth_token(self) -> dict:
        """
        Get authentication token for push notification services.

        Returns
        -------
        dict
            Authentication token details.

        Examples
        --------
        ```json
        {
            "data": {
                "oauth_id": xxxxxxxxxxxxxxxxxxx,
                "pushbrowser_server": "https://notification.synology.com/web/",
                "register_token": "YOUR_REGISTER_TOKEN"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Mobile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def unpair_push_service(self, target_id: int) -> dict:
        """
        Unpair a push notification service.

        Parameters
        ----------
        target_id : int
            Target ID of the push service to unpair. Use `list_push_service` to get existing services.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Mobile'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'unpair',
            'target_id_list': str(target_id)
        }
        return self.request_data(api_name, api_path, req_param)

    def list_webhook(self) -> dict:
        """
        List configured webhooks for notifications.

        Returns
        -------
        dict
            Configured webhooks details.

        Examples
        --------
        ```json
        {
            "data": {
                "count": 1,
                "list": [
                    {
                        "profile_id": 6,
                        "target_config": {
                        "interval": 0,
                        "needssl": true,
                        "port": 443,
                        "prefix": "[SYNO-FLORENTB]",
                        "provider": "test",
                        "req_header": "",
                        "req_method": "get",
                        "req_param": "",
                        "sepchar": " ",
                        "type": "custom",
                        "url": "https://webhook.site/558e159f-2dd8-48a1-8afb-ee9715ef5753?text=%40%40TEXT%40%40",
                        "use_default_lang": true
                        },
                        "target_id": 6,
                        "target_name": "test",
                        "target_type": "webhook",
                        "template_config": {
                        "default_enabled_rule_level": "NOTIFICATION_ERROR",
                        "default_type": "Critical",
                        "is_default": true
                        },
                        "template_id": 3,
                        "template_name": "Critical"
                    }
                ]
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list'
        }
        return self.request_data(api_name, api_path, req_param)

    def _format_req_list(self, req_list):
        """
        Convert a list of dicts or tuples to Synology API string format. Example: [{"name": "X-Token", "value": "abc"}, {"name": "X-Id", "value": "123"}] -> "X-Token:abc\rX-Id:123\r".

        Parameters
        ----------
        req_list : list of dict
            List of dicts with 'name' and 'value' keys.

        Returns
        -------
        str
            Formatted string for Synology API.
        """
        if not req_list:
            return "\r"
        formatted = "".join(
            f"{item['name']}:{item['value']}\r" for item in req_list)
        return formatted

    def create_webhook(self,
                       provider: str,
                       url: str,
                       template_id: int,
                       req_header: list = None,
                       req_param: list = [
                           {"name": "text", "value": "@@TEXT@@"}],
                       port: int = 443,
                       type_: str = "custom",
                       interval: int = 0,
                       req_method: str = "get",
                       needssl: bool = True,
                       use_default_lang: bool = True,
                       prefix: str = "",
                       sepchar: str = " ") -> dict:
        """
        Create a new webhook provider for notifications, formatting req_header and req_param as required.

        Parameters
        ----------
        provider : str
            The provider name.
        url : str
            The webhook URL.
        template_id : int
            The template ID.
        req_header : list of dict, optional
            Example: [{"name": "X-Token", "value": "abc"}].
        req_param : list of dict, optional
            Example: [{"name": "X-Token", "value": "abc"}].
        port : int, optional
            The port to use (default: 443).
        type_ : str, optional
            The type of webhook (default: "custom"). Only "custom" is supported, TODO: Add others types.
        interval : int, optional
            The interval (default: 0).
        req_method : str, optional
            The HTTP request method (default: "get").
        needssl : bool, optional
            Whether SSL is needed (default: True).
        use_default_lang : bool, optional
            Use default language (default: True).
        prefix : str, optional
            Prefix for the notification (default: "").
        sepchar : str, optional
            Separator character (default: " ").

        Returns
        -------
        dict
            API response success.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """

        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param_dict = {
            'version': info['maxVersion'],
            'method': 'create',
            'type': type_,
            'port': port,
            'template_id': template_id,
            'interval': interval,
            'req_method': req_method,
            'req_header': self._format_req_list(req_header),
            'req_param': self._format_req_list(req_param),
            'needssl': needssl,
            'provider': provider,
            'use_default_lang': use_default_lang,
            'prefix': prefix,
            'sepchar': sepchar,
            'url': url
        }

        return self.request_data(api_name, api_path, req_param_dict)

    def edit_webhook(self,
                     profile_id: int,
                     provider: str,
                     url: str,
                     template_id: int,
                     req_header: list = None,
                     req_param: list = None,
                     port: int = 443,
                     type_: str = "custom",
                     interval: int = 0,
                     req_method: str = "get",
                     needssl: bool = True,
                     use_default_lang: bool = True,
                     prefix: str = "",
                     sepchar: str = " ") -> dict:
        """
        Update (set) a webhook provider for notifications, formatting req_header and req_param as required.

        Parameters
        ----------
        profile_id : int
            The profile ID of the webhook provider.
        provider : str
            The provider name.
        url : str
            The webhook URL.
        template_id : int
            The template ID.
        req_header : list of dict, optional
            Example: [{"name": "X-Token", "value": "abc"}]
        req_param : list of dict, optional
            Example: [{"name": "foo", "value": "bar"}]
        port : int, optional
            The port to use (default: 443).
        type_ : str, optional
            The type of webhook (default: "custom"). Only "custom" is supported, TODO: Add others types.
        interval : int, optional
            The interval (default: 0).
        req_method : str, optional
            The HTTP request method (default: "get").
        needssl : bool, optional
            Whether SSL is needed (default: True).
        use_default_lang : bool, optional
            Use default language (default: True).
        prefix : str, optional
            Prefix for the notification (default: "").
        sepchar : str, optional
            Separator character (default: " ").

        Returns
        -------
        dict
            API response.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param_dict = {
            'version': info['maxVersion'],
            'method': 'set',
            'profile_id': profile_id,
            'type': type_,
            'port': port,
            'template_id': template_id,
            'interval': interval,
            'req_method': req_method,
            'req_header': self._format_req_list(req_header),
            'req_param': self._format_req_list(req_param),
            'needssl': needssl,
            'provider': provider,
            'use_default_lang': use_default_lang,
            'prefix': prefix,
            'sepchar': sepchar,
            'url': url
        }
        return self.request_data(api_name, api_path, req_param_dict)

    def delete_webhook(self, profile_id: int) -> dict:
        """
        Delete a webhook provider for notifications.

        Parameters
        ----------
        profile_id : int
            The profile ID of the webhook provider to delete.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Push.Webhook.Provider'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'profile_id': profile_id
        }
        return self.request_data(api_name, api_path, req_param)

    def get_variables(self) -> dict:
        """
        Get notification variables such as company name and HTTP URL.

        Returns
        -------
        dict
            Notification variables including company name and HTTP URL.

        Examples
        --------
        ```json
        {
            "data": {
                "company_name": "Synology",
                "http_url": "http://www.synology.com"
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.Variables'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_variables(self, company_name: str, http_url: str) -> dict:
        """
        Edit notification variables such as company name and HTTP URL.

        Parameters
        ----------
        company_name : str
            The company name to set.
        http_url : str
            The HTTP URL to set.

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        # If http_url is not empty, verify it's a valid URL
        if http_url and not (http_url.startswith("http://") or http_url.startswith("https://")):
            raise ValueError(
                "http_url must start with 'http://' or 'https://'")

        api_name = 'SYNO.Core.Notification.Advance.Variables'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'company_name': company_name,
            'http_url': http_url
        }
        return self.request_data(api_name, api_path, req_param)

    def get_event_message(self, event_tag: str) -> dict:
        """
Get the subject and message for a specific event tag.

        Parameters
        ----------
        event_tag : str
            The event tag to retrieve (e.g., "ActiveBackupOffice365_restore_warning").

        Returns
        -------
        dict
            API response containing the subject and message for the specified event tag.

        Examples
        --------
        ```json
        {
            "data": {
                "content": "",
                "default_content": "Les données [%SERVICENAME%] du compte [%SRCUSERNAME%] ont été partiellement restaurées sur le compte [%DESTUSERNAME%] par [%TRIGGER%] (succès : %SUCCESSNUM% ; avertissement : %WARNINGNUM%).\nHeure de début : %STARTTIME%\nHeure de fin : %ENDTIME%\nConnectez-vous à la console d'administration d'Active Backup for Microsoft 365 pour plus d'informations, puis réessayez plus tard.\n\nDe %HOSTNAME%",
                "default_subject": "%PACKAGENAME% - Les données de sauvegarde sur [%HOSTNAME%] ont été partiellement restaurées",
                "subject": ""
            },
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.CustomizedData'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get',
            'event_tag': event_tag
        }
        return self.request_data(api_name, api_path, req_param)

    def edit_event_message(self, event_tag: str, subject: str, message: str) -> dict:
        """
        Edit the subject and message for a specific event tag.

        Parameters
        ----------
        event_tag : str
            The event tag to edit (e.g., "ActiveBackupOffice365_restore_warning").
        subject : str
            The subject template for the event.
        message : str
            The message template for the event. Must be a valid html <div>...</div> with text in it.
            E.g., "<div>Les données [%SERVICENAME%] du compte [%SRCUSERNAME%] ont été partiellement restaurées sur le compte [%DESTUSERNAME%] par [%TRIGGER%] (succès&nbsp;: %SUCCESSNUM%&nbsp;; avertissement&nbsp;: %WARNINGNUM%).<br>Heure de début&nbsp;: %STARTTIME%<br>Heure de fin&nbsp;: %ENDTIME%<br>Connectez-vous à la console d'administration d'Active&nbsp;Backup for&nbsp;Microsoft&nbsp;365 pour plus d'informations, puis réessayez plus tard.<br><br>De %HOSTNAME%</div>".

        Returns
        -------
        dict
            API response success status.

        Examples
        --------
        ```json
        {
            "success": true
        }
        ```
        """
        api_name = 'SYNO.Core.Notification.Advance.CustomizedData'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'event_tag': event_tag,
            'subject': subject,
            'message': message
        }
        return self.request_data(api_name, api_path, req_param)
