"""
Synology Core Security API wrapper.

This module provides a Python interface for managing security settings on
Synology NAS devices, including auto-block rules, firewall configuration,
DoS protection, SmartBlock, OTP, and trusted device management.
"""

from __future__ import annotations
import json
from . import base_api


class CoreSecurity(base_api.BaseApi):
    """
    Core Security API implementation for Synology NAS.

    Provides methods to manage security features including auto-block rules,
    firewall settings, DoS protection, SmartBlock, OTP, and trusted devices.
    """

    # ------------------------------------------------------------------
    # SYNO.Core.Security.AutoBlock.Rules
    # ------------------------------------------------------------------

    def autoblock_rules_get(self) -> dict[str, object] | str:
        """
        Get auto-block rules.

        Returns
        -------
        dict[str, object] or str
            Auto-block rules configuration.
        """
        api_name = 'SYNO.Core.Security.AutoBlock.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def autoblock_rules_list(self) -> dict[str, object] | str:
        """
        List all auto-block rules.

        Returns
        -------
        dict[str, object] or str
            List of auto-block rules.
        """
        api_name = 'SYNO.Core.Security.AutoBlock.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def autoblock_rules_set(self, rules: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Set auto-block rules.

        Parameters
        ----------
        rules : list[dict[str, object]]
            List of rule objects to apply.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.AutoBlock.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'rules': json.dumps(rules),
        }

        return self.request_data(api_name, api_path, req_param)

    def autoblock_rules_delete(self, rules: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Delete auto-block rules.

        Parameters
        ----------
        rules : list[dict[str, object]]
            List of rule objects to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.Security.AutoBlock.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'rules': json.dumps(rules),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.DSM
    # ------------------------------------------------------------------

    def security_dsm_get(self) -> dict[str, object] | str:
        """
        Get DSM security settings.

        Returns
        -------
        dict[str, object] or str
            DSM security settings.
        """
        api_name = 'SYNO.Core.Security.DSM'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_dsm_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set DSM security settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of DSM security settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.DSM'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.DSM.Embed
    # ------------------------------------------------------------------

    def security_dsm_embed_get(self) -> dict[str, object] | str:
        """
        Get DSM embed security settings.

        Returns
        -------
        dict[str, object] or str
            DSM embed security settings.
        """
        api_name = 'SYNO.Core.Security.DSM.Embed'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_dsm_embed_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set DSM embed security settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of embed security settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.DSM.Embed'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.DSM.Proxy
    # ------------------------------------------------------------------

    def security_dsm_proxy_get(self) -> dict[str, object] | str:
        """
        Get DSM proxy security settings.

        Returns
        -------
        dict[str, object] or str
            DSM proxy security settings.
        """
        api_name = 'SYNO.Core.Security.DSM.Proxy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_dsm_proxy_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set DSM proxy security settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of proxy security settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.DSM.Proxy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.DoS
    # ------------------------------------------------------------------

    def security_dos_get(self) -> dict[str, object] | str:
        """
        Get DoS protection settings.

        Returns
        -------
        dict[str, object] or str
            DoS protection settings.
        """
        api_name = 'SYNO.Core.Security.DoS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def security_dos_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set DoS protection settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of DoS protection settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.DoS'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall
    # ------------------------------------------------------------------

    def firewall_get(self) -> dict[str, object] | str:
        """
        Get firewall status and settings.

        Returns
        -------
        dict[str, object] or str
            Firewall status and settings.
        """
        api_name = 'SYNO.Core.Security.Firewall'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set firewall settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of firewall settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.Firewall'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Adapter
    # ------------------------------------------------------------------

    def firewall_adapter_get(self) -> dict[str, object] | str:
        """
        Get firewall adapter configuration.

        Returns
        -------
        dict[str, object] or str
            Firewall adapter configuration.
        """
        api_name = 'SYNO.Core.Security.Firewall.Adapter'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_adapter_list(self) -> dict[str, object] | str:
        """
        List firewall adapters.

        Returns
        -------
        dict[str, object] or str
            List of firewall adapters.
        """
        api_name = 'SYNO.Core.Security.Firewall.Adapter'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Conf
    # ------------------------------------------------------------------

    def firewall_conf_get(self) -> dict[str, object] | str:
        """
        Get firewall configuration.

        Returns
        -------
        dict[str, object] or str
            Firewall configuration.
        """
        api_name = 'SYNO.Core.Security.Firewall.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_conf_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set firewall configuration.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of firewall configuration to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Conf'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Geoip
    # ------------------------------------------------------------------

    def firewall_geoip_get(self) -> dict[str, object] | str:
        """
        Get geo-IP blocking settings.

        Returns
        -------
        dict[str, object] or str
            Geo-IP blocking settings.
        """
        api_name = 'SYNO.Core.Security.Firewall.Geoip'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_geoip_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set geo-IP blocking settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of geo-IP blocking settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Geoip'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Profile.Apply
    # ------------------------------------------------------------------

    def firewall_profile_apply(self, profile_name: str = '') -> dict[str, object] | str:
        """
        Apply a firewall profile.

        Parameters
        ----------
        profile_name : str, optional
            Name of the firewall profile to apply. Defaults to empty string.

        Returns
        -------
        dict[str, object] or str
            Result of the apply operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Profile.Apply'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'profile_name': profile_name,
        }

        return self.request_data(api_name, api_path, req_param)

    def firewall_profile_apply_status(self) -> dict[str, object] | str:
        """
        Get the status of a firewall profile apply operation.

        Returns
        -------
        dict[str, object] or str
            Status of the apply operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Profile.Apply'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Rules
    # ------------------------------------------------------------------

    def firewall_rules_get(self) -> dict[str, object] | str:
        """
        Get firewall rules.

        Returns
        -------
        dict[str, object] or str
            Firewall rules configuration.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_rules_list(self) -> dict[str, object] | str:
        """
        List all firewall rules.

        Returns
        -------
        dict[str, object] or str
            List of firewall rules.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_rules_set(self, rules: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Set firewall rules.

        Parameters
        ----------
        rules : list[dict[str, object]]
            List of firewall rule objects to apply.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'rules': json.dumps(rules),
        }

        return self.request_data(api_name, api_path, req_param)

    def firewall_rules_delete(self, rules: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Delete firewall rules.

        Parameters
        ----------
        rules : list[dict[str, object]]
            List of firewall rule objects to delete.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'rules': json.dumps(rules),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.Security.Firewall.Rules.Serv
    # ------------------------------------------------------------------

    def firewall_rules_serv_get(self) -> dict[str, object] | str:
        """
        Get service-based firewall rules.

        Returns
        -------
        dict[str, object] or str
            Service-based firewall rules.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules.Serv'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def firewall_rules_serv_list(self) -> dict[str, object] | str:
        """
        List service-based firewall rules.

        Returns
        -------
        dict[str, object] or str
            List of service-based firewall rules.
        """
        api_name = 'SYNO.Core.Security.Firewall.Rules.Serv'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
