"""
Synology Core Security (Auth/OTP/SmartBlock) API wrapper.

Covers SYNO.Core.SmartBlock.*, SYNO.Core.OTP.*, TrustDevice,
and DisableAdmin endpoints on Synology NAS devices.
"""

from __future__ import annotations
import json
from . import base_api


class CoreSecurityAuth(base_api.BaseApi):
    """
    Core Security Auth API for SmartBlock/OTP/TrustDevice/DisableAdmin.

    Covers SYNO.Core.SmartBlock.*, OTP.*, TrustDevice, and DisableAdmin endpoints.
    """

    # SYNO.Core.SmartBlock
    # ------------------------------------------------------------------

    def smartblock_get(self) -> dict[str, object] | str:
        """
        Get SmartBlock settings.

        Returns
        -------
        dict[str, object] or str
            SmartBlock settings.
        """
        api_name = 'SYNO.Core.SmartBlock'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set SmartBlock settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of SmartBlock settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.SmartBlock'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.SmartBlock.Device
    # ------------------------------------------------------------------

    def smartblock_device_get(self) -> dict[str, object] | str:
        """
        Get SmartBlock blocked devices.

        Returns
        -------
        dict[str, object] or str
            Blocked device information.
        """
        api_name = 'SYNO.Core.SmartBlock.Device'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_device_list(self) -> dict[str, object] | str:
        """
        List SmartBlock blocked devices.

        Returns
        -------
        dict[str, object] or str
            List of blocked devices.
        """
        api_name = 'SYNO.Core.SmartBlock.Device'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_device_delete(self, devices: list[str]) -> dict[str, object] | str:
        """
        Remove devices from the SmartBlock blocked list.

        Parameters
        ----------
        devices : list[str]
            List of device identifiers to remove.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.SmartBlock.Device'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'devices': json.dumps(devices),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.SmartBlock.Trusted
    # ------------------------------------------------------------------

    def smartblock_trusted_get(self) -> dict[str, object] | str:
        """
        Get SmartBlock trusted list.

        Returns
        -------
        dict[str, object] or str
            Trusted list entries.
        """
        api_name = 'SYNO.Core.SmartBlock.Trusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_trusted_list(self) -> dict[str, object] | str:
        """
        List SmartBlock trusted entries.

        Returns
        -------
        dict[str, object] or str
            List of trusted entries.
        """
        api_name = 'SYNO.Core.SmartBlock.Trusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_trusted_set(self, entries: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Set SmartBlock trusted list entries.

        Parameters
        ----------
        entries : list[dict[str, object]]
            List of trusted entry objects to set.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.SmartBlock.Trusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'entries': json.dumps(entries),
        }

        return self.request_data(api_name, api_path, req_param)

    def smartblock_trusted_delete(self, entries: list[str]) -> dict[str, object] | str:
        """
        Delete entries from the SmartBlock trusted list.

        Parameters
        ----------
        entries : list[str]
            List of entry identifiers to remove.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.SmartBlock.Trusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'entries': json.dumps(entries),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.SmartBlock.Untrusted
    # ------------------------------------------------------------------

    def smartblock_untrusted_get(self) -> dict[str, object] | str:
        """
        Get SmartBlock untrusted list.

        Returns
        -------
        dict[str, object] or str
            Untrusted list entries.
        """
        api_name = 'SYNO.Core.SmartBlock.Untrusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_untrusted_list(self) -> dict[str, object] | str:
        """
        List SmartBlock untrusted entries.

        Returns
        -------
        dict[str, object] or str
            List of untrusted entries.
        """
        api_name = 'SYNO.Core.SmartBlock.Untrusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_untrusted_set(self, entries: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Set SmartBlock untrusted list entries.

        Parameters
        ----------
        entries : list[dict[str, object]]
            List of untrusted entry objects to set.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.SmartBlock.Untrusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'entries': json.dumps(entries),
        }

        return self.request_data(api_name, api_path, req_param)

    def smartblock_untrusted_delete(self, entries: list[str]) -> dict[str, object] | str:
        """
        Delete entries from the SmartBlock untrusted list.

        Parameters
        ----------
        entries : list[str]
            List of entry identifiers to remove.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.SmartBlock.Untrusted'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'entries': json.dumps(entries),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.SmartBlock.User
    # ------------------------------------------------------------------

    def smartblock_user_get(self) -> dict[str, object] | str:
        """
        Get SmartBlock user-level block settings.

        Returns
        -------
        dict[str, object] or str
            User-level block settings.
        """
        api_name = 'SYNO.Core.SmartBlock.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_user_list(self) -> dict[str, object] | str:
        """
        List SmartBlock user-level blocks.

        Returns
        -------
        dict[str, object] or str
            List of user-level blocks.
        """
        api_name = 'SYNO.Core.SmartBlock.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def smartblock_user_set(self, users: list[dict[str, object]]) -> dict[str, object] | str:
        """
        Set SmartBlock user-level blocks.

        Parameters
        ----------
        users : list[dict[str, object]]
            List of user block objects to set.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.SmartBlock.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'users': json.dumps(users),
        }

        return self.request_data(api_name, api_path, req_param)

    def smartblock_user_delete(self, users: list[str]) -> dict[str, object] | str:
        """
        Delete SmartBlock user-level blocks.

        Parameters
        ----------
        users : list[str]
            List of user identifiers to unblock.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.SmartBlock.User'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'users': json.dumps(users),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.OTP
    # ------------------------------------------------------------------

    def otp_get(self) -> dict[str, object] | str:
        """
        Get OTP settings.

        Returns
        -------
        dict[str, object] or str
            OTP settings.
        """
        api_name = 'SYNO.Core.OTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def otp_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set OTP settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of OTP settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.OTP'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.OTP.Admin
    # ------------------------------------------------------------------

    def otp_admin_get(self) -> dict[str, object] | str:
        """
        Get OTP admin settings.

        Returns
        -------
        dict[str, object] or str
            OTP admin settings.
        """
        api_name = 'SYNO.Core.OTP.Admin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def otp_admin_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set OTP admin settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of OTP admin settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.OTP.Admin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.OTP.EnforcePolicy
    # ------------------------------------------------------------------

    def otp_enforce_policy_get(self) -> dict[str, object] | str:
        """
        Get OTP enforcement policy.

        Returns
        -------
        dict[str, object] or str
            OTP enforcement policy settings.
        """
        api_name = 'SYNO.Core.OTP.EnforcePolicy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def otp_enforce_policy_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set OTP enforcement policy.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of enforcement policy settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.OTP.EnforcePolicy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.OTP.Ex
    # ------------------------------------------------------------------

    def otp_ex_get(self) -> dict[str, object] | str:
        """
        Get extended OTP settings.

        Returns
        -------
        dict[str, object] or str
            Extended OTP settings.
        """
        api_name = 'SYNO.Core.OTP.Ex'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def otp_ex_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set extended OTP settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of extended OTP settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.OTP.Ex'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.OTP.Mail
    # ------------------------------------------------------------------

    def otp_mail_get(self) -> dict[str, object] | str:
        """
        Get OTP mail settings.

        Returns
        -------
        dict[str, object] or str
            OTP mail settings.
        """
        api_name = 'SYNO.Core.OTP.Mail'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def otp_mail_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set OTP mail settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of OTP mail settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.OTP.Mail'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.TrustDevice
    # ------------------------------------------------------------------

    def trust_device_get(self) -> dict[str, object] | str:
        """
        Get trusted device settings.

        Returns
        -------
        dict[str, object] or str
            Trusted device settings.
        """
        api_name = 'SYNO.Core.TrustDevice'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def trust_device_list(self) -> dict[str, object] | str:
        """
        List trusted devices.

        Returns
        -------
        dict[str, object] or str
            List of trusted devices.
        """
        api_name = 'SYNO.Core.TrustDevice'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def trust_device_delete(self, devices: list[str]) -> dict[str, object] | str:
        """
        Remove devices from the trusted list.

        Parameters
        ----------
        devices : list[str]
            List of device identifiers to remove.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation.
        """
        api_name = 'SYNO.Core.TrustDevice'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'devices': json.dumps(devices),
        }

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------
    # SYNO.Core.DisableAdmin
    # ------------------------------------------------------------------

    def disable_admin_get(self) -> dict[str, object] | str:
        """
        Get disabled admin account settings.

        Returns
        -------
        dict[str, object] or str
            Disabled admin account settings.
        """
        api_name = 'SYNO.Core.DisableAdmin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def disable_admin_set(self, **kwargs: object) -> dict[str, object] | str:
        """
        Set disabled admin account settings.

        Parameters
        ----------
        **kwargs : object
            Key-value pairs of admin disable settings to update.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation.
        """
        api_name = 'SYNO.Core.DisableAdmin'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set', **kwargs}

        return self.request_data(api_name, api_path, req_param)
