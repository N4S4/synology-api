"""
Synology Core External Device API wrapper.

Provides a Python interface for managing external devices on Synology NAS,
including Bluetooth, printers, and storage expansion units.
"""

from __future__ import annotations
from typing import Optional
from . import base_api


class CoreExternalDevice(base_api.BaseApi):
    """
    Core External Device API implementation for Synology NAS.

    Covers Bluetooth, printer (driver, network, USB, OAuth), and storage
    (expansion unit, settings) endpoints not handled by other modules.
    """

    # ------------------------------------------------------------------ #
    #  Bluetooth                                                          #
    # ------------------------------------------------------------------ #

    def bluetooth_get(self) -> dict[str, object] | str:
        """
        Get Bluetooth adapter status.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_set(self, enable: bool = True) -> dict[str, object] | str:
        """
        Enable or disable the Bluetooth adapter.

        Parameters
        ----------
        enable : bool, optional
            The enable value.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth set operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'enable': str(enable).lower()}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_list(self) -> dict[str, object] | str:
        """
        List discovered Bluetooth devices.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth device list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_get(self, device_id: str) -> dict[str, object] | str:
        """
        Get information for a specific Bluetooth device.

        Parameters
        ----------
        device_id : str
            The device id value.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth device get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_connect(self, device_id: str) -> dict[str, object] | str:
        """
        Connect to a Bluetooth device.

        Parameters
        ----------
        device_id : str
            The device id value.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth device connect operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'connect',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_device_disconnect(self, device_id: str) -> dict[str, object] | str:
        """
        Disconnect a Bluetooth device.

        Parameters
        ----------
        device_id : str
            The device id value.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth device disconnect operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Device'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'disconnect',
                     'id': device_id}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_settings_get(self) -> dict[str, object] | str:
        """
        Get Bluetooth settings.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth settings get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Settings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def bluetooth_settings_set(self, discoverable: Optional[bool] = None,
                               name: Optional[str] = None) -> dict[str, object] | str:
        """
        Set Bluetooth settings.

        Parameters
        ----------
        discoverable : str, optional
            The discoverable value.
        name : str, optional
            The name value.

        Returns
        -------
        dict[str, object] or str
            Result of the bluetooth settings set operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Bluetooth.Settings'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'set'}
        if discoverable is not None:
            req_param['discoverable'] = str(discoverable).lower()
        if name is not None:
            req_param['name'] = name

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Default Permission                                                 #
    # ------------------------------------------------------------------ #

    def default_permission_get(self) -> dict[str, object] | str:
        """
        Get default permission settings for external devices.

        Returns
        -------
        dict[str, object] or str
            Result of the default permission get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def default_permission_set(self, permission: str) -> dict[str, object] | str:
        """
        Set default permission for external devices.

        Parameters
        ----------
        permission : str
            The permission value.

        Returns
        -------
        dict[str, object] or str
            Result of the default permission set operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.DefaultPermission'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'permission': permission}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer                                                            #
    # ------------------------------------------------------------------ #

    def printer_list(self) -> dict[str, object] | str:
        """
        List all printers.

        Returns
        -------
        dict[str, object] or str
            Result of the printer list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_get(self, printer_id: str) -> dict[str, object] | str:
        """
        Get printer information.

        Parameters
        ----------
        printer_id : str
            The printer id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_clean(self, printer_id: str) -> dict[str, object] | str:
        """
        Clean the print queue for a printer.

        Parameters
        ----------
        printer_id : str
            The printer id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer clean operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clean',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer Driver                                                     #
    # ------------------------------------------------------------------ #

    def printer_driver_list(self) -> dict[str, object] | str:
        """
        List available printer drivers.

        Returns
        -------
        dict[str, object] or str
            Result of the printer driver list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Driver'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_driver_get(self, driver_id: str) -> dict[str, object] | str:
        """
        Get a specific printer driver.

        Parameters
        ----------
        driver_id : str
            The driver id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer driver get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Driver'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': driver_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer Network                                                    #
    # ------------------------------------------------------------------ #

    def printer_network_list(self) -> dict[str, object] | str:
        """
        List network printers.

        Returns
        -------
        dict[str, object] or str
            Result of the printer network list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_network_create(self, host: str, port: int = 9100,
                               driver_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Add a network printer.

        Parameters
        ----------
        host : str
            The host value.
        port : int, optional
            The port value.
        driver_id : str, optional
            The driver id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer network create operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'create',
            'host': host, 'port': port}
        if driver_id is not None:
            req_param['driver_id'] = driver_id

        return self.request_data(api_name, api_path, req_param)

    def printer_network_delete(self, printer_id: str) -> dict[str, object] | str:
        """
        Remove a network printer.

        Parameters
        ----------
        printer_id : str
            The printer id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer network delete operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_network_host_list(self) -> dict[str, object] | str:
        """
        List network printer hosts discovered on the network.

        Returns
        -------
        dict[str, object] or str
            Result of the printer network host list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.Network.Host'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer OAuth                                                      #
    # ------------------------------------------------------------------ #

    def printer_oauth_get(self) -> dict[str, object] | str:
        """
        Get OAuth settings for cloud printing.

        Returns
        -------
        dict[str, object] or str
            Result of the printer oauth get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.OAuth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def printer_oauth_set(self, token: str) -> dict[str, object] | str:
        """
        Set OAuth token for cloud printing.

        Parameters
        ----------
        token : str
            The token value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer oauth set operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.OAuth'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set',
                     'token': token}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Printer USB                                                        #
    # ------------------------------------------------------------------ #

    def printer_usb_list(self) -> dict[str, object] | str:
        """
        List USB printers.

        Returns
        -------
        dict[str, object] or str
            Result of the printer usb list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def printer_usb_get(self, printer_id: str) -> dict[str, object] | str:
        """
        Get USB printer information.

        Parameters
        ----------
        printer_id : str
            The printer id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer usb get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    def printer_usb_release(self, printer_id: str) -> dict[str, object] | str:
        """
        Release a USB printer from the server.

        Parameters
        ----------
        printer_id : str
            The printer id value.

        Returns
        -------
        dict[str, object] or str
            Result of the printer usb release operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Printer.USB'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'release',
                     'id': printer_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Storage — Expansion Unit                                           #
    # ------------------------------------------------------------------ #

    def storage_eunit_list(self) -> dict[str, object] | str:
        """
        List connected expansion units.

        Returns
        -------
        dict[str, object] or str
            Result of the storage eunit list operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.EUnit'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def storage_eunit_get(self, unit_id: str) -> dict[str, object] | str:
        """
        Get expansion unit details.

        Parameters
        ----------
        unit_id : str
            The unit id value.

        Returns
        -------
        dict[str, object] or str
            Result of the storage eunit get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.EUnit'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': unit_id}

        return self.request_data(api_name, api_path, req_param)

    # ------------------------------------------------------------------ #
    #  Storage — Setting                                                  #
    # ------------------------------------------------------------------ #

    def storage_setting_get(self) -> dict[str, object] | str:
        """
        Get external storage settings.

        Returns
        -------
        dict[str, object] or str
            Result of the storage setting get operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def storage_setting_set(self,
                            auto_format: Optional[bool] = None,
                            auto_mount: Optional[bool] = None) -> dict[str, object] | str:
        """
        Set external storage settings.

        Parameters
        ----------
        auto_format : str, optional
            The auto format value.
        auto_mount : str, optional
            The auto mount value.

        Returns
        -------
        dict[str, object] or str
            Result of the storage setting set operation.
        """
        api_name = 'SYNO.Core.ExternalDevice.Storage.Setting'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param: dict[str, object] = {
            'version': info['maxVersion'], 'method': 'set'}
        if auto_format is not None:
            req_param['auto_format'] = str(auto_format).lower()
        if auto_mount is not None:
            req_param['auto_mount'] = str(auto_mount).lower()

        return self.request_data(api_name, api_path, req_param)
