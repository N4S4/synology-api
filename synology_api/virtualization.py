"""
Virtualization API wrapper for Synology Virtual Machine Manager.

This module provides the Virtualization class for managing tasks, networks, storage, hosts, VMs, and images
on Synology NAS devices via the Virtual Machine Manager API.
"""

from __future__ import annotations
from typing import Optional, Any
from . import base_api


class Virtualization(base_api.BaseApi):
    """
    API wrapper for Synology Virtual Machine Manager.

    Provides methods to manage tasks, networks, storage, hosts, VMs, and images.
    Routes advertised by a NAS but not covered by a typed helper can be
    discovered with :meth:`get_unmapped_api_list` and called with
    :meth:`request_api`.

    Parameters
    ----------
    ip_address : str
        IP address of the Synology NAS.
    port : str
        Port number to connect to.
    username : str
        DSM username.
    password : str
        DSM password.
    secure : bool, optional
        Use HTTPS if True. Default is False.
    cert_verify : bool, optional
        Verify SSL certificate if True. Default is False.
    dsm_version : int, optional
        DSM version. Default is 7.
    debug : bool, optional
        Enable debug mode. Default is True.
    otp_code : str, optional
        One-time password for 2FA, if required.
    quickconnect_id : str, optional
        QuickConnect ID for relay-based access. Defaults to None.
    """

    _MAPPED_API_NAMES = frozenset({
        'SYNO.Virtualization.API.Task.Info',
        'SYNO.Virtualization.API.Network',
        'SYNO.Virtualization.API.Storage',
        'SYNO.Virtualization.API.Host',
        'SYNO.Virtualization.API.Guest',
        'SYNO.Virtualization.API.Guest.Action',
        'SYNO.Virtualization.API.Guest.Image',
    })

    def __init__(self,
                 ip_address: Optional[str] = None,
                 port: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 quickconnect_id: Optional[str] = None
                 ) -> None:
        """
        Initialize the Virtualization API wrapper.

        Parameters
        ----------
        ip_address : str
            IP address of the Synology NAS.
        port : str
            Port number.
        username : str
            DSM username.
        password : str
            DSM password.
        secure : bool, optional
            Use HTTPS if True. Default is False.
        cert_verify : bool, optional
            Verify SSL certificate if True. Default is False.
        dsm_version : int, optional
            DSM version. Default is 7.
        debug : bool, optional
            Enable debug mode. Default is True.
        otp_code : str, optional
            One-time password for 2FA, if required.
        quickconnect_id : str, optional
            QuickConnect ID for relay-based access. When provided, `ip_address`
            and `port` are not required.
        """

        super(Virtualization, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                             dsm_version, debug, otp_code, application='Core',
                                             quickconnect_id=quickconnect_id)

        self._taskid_list: Any = []
        self._network_group_list: Any = []
        self._storages_list: Any = []
        self._host_operation_list: Any = []
        self._vm_guest_id_list: Any = []
        self._vm_guest_name_list: Any = []
        self._vm_created_taskid_list: Any = []

        self.session.get_api_list('Virtualization')

        self.file_station_list: Any = self.session.app_api_list

    def get_unmapped_api_list(self) -> list[dict[str, object]]:
        """
        List Virtualization API routes advertised by this NAS without a typed wrapper.

        The route catalogue is DSM- and package-dependent, so this method
        reports routes discovered at runtime instead of relying on a fixed
        global list.

        Returns
        -------
        list of dict
            Unmapped API names with their endpoint path and maximum version.
        """
        return [
            {
                'api_name': api_name,
                'path': info['path'],
                'max_version': info['maxVersion'],
            }
            for api_name, info in self.file_station_list.items()
            if api_name.startswith('SYNO.Virtualization.')
            and api_name not in self._MAPPED_API_NAMES
        ]

    def request_api(
        self,
        api_name: str,
        api_method: str,
        params: Optional[dict[str, object]] = None,
        http_method: str = 'get',
    ) -> dict[str, object] | str | list:
        """
        Call a Virtualization route advertised by the connected NAS.

        Use this for a route returned by :meth:`get_unmapped_api_list` until
        a dedicated typed wrapper is added. Route names are restricted to
        the Virtualization namespace and must exist in this NAS's API list.

        Parameters
        ----------
        api_name : str
            Advertised ``SYNO.Virtualization.*`` API name.
        api_method : str
            Operation name accepted by the selected API route.
        params : dict, optional
            Operation-specific request parameters. Do not include ``version``
            or ``method``; they are supplied by this wrapper.
        http_method : str, optional
            HTTP transport method, either ``get`` or ``post``. Defaults to
            ``get``.

        Returns
        -------
        dict, list, or str
            Response returned by the Synology API.

        Raises
        ------
        ValueError
            If the route is not advertised by this NAS, is outside the
            Virtualization namespace, or the HTTP method is unsupported.
        """
        if not api_name.startswith('SYNO.Virtualization.'):
            raise ValueError('Only SYNO.Virtualization.* routes are supported')
        if api_name not in self.file_station_list:
            raise ValueError(f'Virtualization API is not available: {api_name}')
        if not api_method:
            raise ValueError('api_method must not be empty')
        if http_method not in {'get', 'post'}:
            raise ValueError("http_method must be 'get' or 'post'")

        route_info = self.file_station_list[api_name]
        req_param = {
            'version': route_info['maxVersion'],
            'method': api_method,
        }
        if params:
            reserved = {'version', 'method'}.intersection(params)
            if reserved:
                raise ValueError(
                    'params must not override version or method'
                )
            req_param.update(params)

        return self.request_data(
            api_name,
            route_info['path'],
            req_param,
            method=http_method,
        )

    def get_task_list(self) -> list[str] | dict[str, object] | str | list[object]:
        """
        Get the list of virtualization tasks.

        Returns
        -------
        list of str, dict, or str
            Task IDs on success, or the raw response when the API returns an
            error or an unexpected response shape.
        """
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        response = self.request_data(api_name, api_path, req_param)
        if isinstance(response, dict):
            data = response.get('data')
            if isinstance(data, dict) and isinstance(data.get('tasks'), list):
                self._taskid_list = data['tasks']
                return self._taskid_list

        self._taskid_list = response

        return self._taskid_list

    def clear_task(self, taskid: str) -> dict[str, object] | str:
        """
        Clear a specific task by its ID.

        Parameters
        ----------
        taskid : str
            Task ID to clear.

        Returns
        -------
        dict[str, object] or str
            Result of the clear operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear'}

        if taskid is None:
            return 'Enter a valid taskid, choose between get_task_list results'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_task_info(self, taskid: str) -> dict[str, object] | str:
        """
        Get information about a specific task.

        Parameters
        ----------
        taskid : str
            Task ID to retrieve information for.

        Returns
        -------
        dict[str, object] or str
            Task information or error message.
        """
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        if taskid is None:
            return 'Enter a valid taskid, choose between get_task_list results'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_network_group_list(self) -> list[dict[str, object]]:
        """
        Get the list of network groups.

        Returns
        -------
        list of dict
            List of network group information.
        """
        api_name = 'SYNO.Virtualization.API.Network'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._network_group_list = self.request_data(
            api_name, api_path, req_param)

        return self._network_group_list

    def get_storage_operation(self) -> list[str]:
        """
        Get the list of storage operations.

        Returns
        -------
        list of str
            List of storage operation information.
        """
        api_name = 'SYNO.Virtualization.API.Storage'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._storages_list = self.request_data(api_name, api_path, req_param)

        return self._storages_list

    def get_host_operation(self) -> list[str]:
        """
        Get the list of host operations.

        Returns
        -------
        list of str
            List of host operation information.
        """
        api_name = 'SYNO.Virtualization.API.Host'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._host_operation_list = self.request_data(
            api_name, api_path, req_param)

        return self._host_operation_list

    def get_vm_operation(self, additional: bool = False) -> dict[str, object] | str | list:
        """
        Get the list of virtual machines.

        Parameters
        ----------
        additional : bool, optional
            Whether to include additional information. Default is False.

        Returns
        -------
        dict
            Virtualization API response containing guest records and metadata.
        """
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'additional': additional}

        info = self.request_data(api_name, api_path, req_param)

        guests = info.get('data', {}).get('guests', [])
        self._vm_guest_id_list = [
            guest['guest_id'] for guest in guests
            if isinstance(guest, dict) and 'guest_id' in guest
        ]
        self._vm_guest_name_list = [
            guest['guest_name'] for guest in guests
            if isinstance(guest, dict) and 'guest_name' in guest
        ]

        return info

    def get_specific_vm_info(
        self,
        additional: Optional[str | list[str]] = None,
        guest_id: Optional[str] = None,
        guest_name: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Get information about a specific virtual machine.

        Parameters
        ----------
        additional : str or list of str, optional
            Additional fields to include.
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.

        Returns
        -------
        dict[str, object] or str
            VM information or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
        if guest_id is not None:
            req_param['guest_id'] = guest_id
        if additional is not None:
            req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def set_vm_property(
        self,
        guest_id: Optional[str] = None,
        guest_name: Optional[str] = None,
        autorun: Optional[int] = None,
        description: Optional[str] = None,
        new_guest_name: Optional[str] = None,
        vcpu_num: Optional[int] = None,
        vram_size: Optional[int] = None
    ) -> dict[str, object] | str:
        """
        Set properties for a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.
        autorun : int, optional
            Autorun setting (0: off, 1: last state, 2: on).
        description : str, optional
            VM description.
        new_guest_name : str, optional
            New VM name.
        vcpu_num : int, optional
            Number of virtual CPUs.
        vram_size : int, optional
            RAM size in MB.

        Returns
        -------
        dict[str, object] or str
            Result of the set operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'set'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None
        if autorun is not None:
            if (isinstance(autorun, bool)
                    or not isinstance(autorun, int)
                    or autorun not in (0, 1, 2)):
                return 'autorun must be 0 (off), 1 (last state) or 2 (on)'
            req_param['autorun'] = autorun

        if description is not None:
            if not isinstance(description, str):
                return 'description must be a string'
            req_param['description'] = description

        if new_guest_name is not None:
            if not isinstance(new_guest_name, str):
                return 'new_guest_name must be a string'
            req_param['new_guest_name'] = new_guest_name

        if vcpu_num is not None:
            if isinstance(vcpu_num, bool) or not isinstance(vcpu_num, int):
                return 'vcpu_num must be an integer'
            req_param['vcpu_num'] = vcpu_num

        if vram_size is not None:
            if isinstance(vram_size, bool) or not isinstance(vram_size, int):
                return 'vram_size must be an integer'
            req_param['vram_size'] = vram_size
        if len(req_param) == 3:
            return 'Specify at least one VM property to update'

        return self.request_data(api_name, api_path, req_param)

    def delete_vm(self, guest_id: Optional[str] = None, guest_name: Optional[str] = None) -> dict[str, object] | str:
        """
        Delete a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None

        return self.request_data(api_name, api_path, req_param)

    def vm_power_on(
        self,
        guest_id: Optional[str] = None,
        guest_name: Optional[str] = None,
        host_id: Optional[str] = None,
        host_name: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Power on a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.
        host_id : str, optional
            Host ID.
        host_name : str, optional
            Host name.

        Returns
        -------
        dict[str, object] or str
            Result of the power on operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Action'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'poweron'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None

        if host_id is not None:
            req_param['host_id'] = host_id
            host_name = None
        if host_name is not None:
            req_param['host_name'] = host_name
            host_id = None
        if host_id is None and host_name is None:
            print('host_id and host_name are not specified, it will follow autoselect option from the cluster settings')

        return self.request_data(api_name, api_path, req_param)

    def vm_force_power_off(
        self,
        guest_id: Optional[str] = None,
        guest_name: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Force power off a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.

        Returns
        -------
        dict[str, object] or str
            Result of the power off operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Action'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'poweroff'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None

        return self.request_data(api_name, api_path, req_param)

    def vm_shut_down(self, guest_id: Optional[str] = None, guest_name: Optional[str] = None) -> dict[str, object] | str:
        """
        Shut down a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        guest_name : str, optional
            Guest VM name.

        Returns
        -------
        dict[str, object] or str
            Result of the shutdown operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Action'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'shutdown'}

        if guest_id is None and guest_name is None:
            return 'Specify at least one guest_id or guest_name, you can get using get_vm_operation'
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None

        return self.request_data(api_name, api_path, req_param)

    def get_images_list(self) -> dict[str, object]:
        """
        Get the list of VM images.

        Returns
        -------
        dict[str, object]
            Dictionary containing image information.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Image'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def delete_image(self, image_id: Optional[str] = None, image_name: Optional[str] = None) -> dict[str, object] | str:
        """
        Delete a VM image.

        Parameters
        ----------
        image_id : str, optional
            Image ID.
        image_name : str, optional
            Image name.

        Returns
        -------
        dict[str, object] or str
            Result of the delete operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Image'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if image_id is None and image_name is None:
            return 'Specify at least one of image_id or image_name'
        if image_name is not None:
            req_param['image_name'] = image_name
            image_name = None
        if image_id is not None:
            req_param['image_id'] = image_id
            image_name = None

        return self.request_data(api_name, api_path, req_param)

    def create_image(
        self,
        auto_clean_task: bool = True,
        storage_names: Optional[str] = None,
        storage_ids: Optional[str] = None,
        type: Optional[str] = None,
        ds_file_path: Optional[str] = None,
        image_name: Optional[str] = None
    ) -> dict[str, object] | str:
        """
        Create a new VM image.

        Parameters
        ----------
        auto_clean_task : bool, optional
            Whether to auto-clean the task after creation. Default is True.
        storage_names : str, optional
            Storage names.
        storage_ids : str, optional
            Storage IDs.
        type : str, optional
            Image type ('disk', 'vdsm', or 'iso').
        ds_file_path : str, optional
            File path (should begin with a shared folder).
        image_name : str, optional
            Name of the image.

        Returns
        -------
        dict[str, object] or str
            Result of the create operation or error message.
        """
        api_name = 'SYNO.Virtualization.API.Guest.Image'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'create', 'auto_clean_task': auto_clean_task}

        if storage_names is None and storage_ids is None:
            return 'Specify at least one of storage_names or storage_ids'
        if storage_ids is not None:
            req_param['storage_ids'] = storage_ids
            storage_names = None
        if storage_names is not None:
            req_param['storage_names'] = storage_names
            storage_ids = None

        if type is None:
            return 'Specify what type between disk, vdsm or iso'
        if type is not None:
            req_param['type'] = type

        if ds_file_path is None:
            return 'Specify file path, the path should begin with a shared folder'
        if ds_file_path is not None:
            req_param['ds_file_path'] = ds_file_path

        if image_name is None:
            return 'Specify image_name'
        if image_name is not None:
            req_param['image_name'] = image_name

        return self.request_data(api_name, api_path, req_param)

    # TODO create vitrual machine function
