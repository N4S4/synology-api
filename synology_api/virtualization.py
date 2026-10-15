"""
Virtualization API wrapper for Synology Virtual Machine Manager.

This module provides the Virtualization class for managing tasks, networks, storage, hosts, VMs, and images
on Synology NAS devices via the Virtual Machine Manager API.
"""

from __future__ import annotations

import json
from typing import Optional, Any

from . import base_api


class Virtualization(base_api.BaseApi):
    """
    API wrapper for Synology Virtual Machine Manager.

    Provides methods to manage tasks, networks, storage, hosts, VMs, and images.

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

    def get_task_list(self) -> list[str]:
        """
        Get the list of virtualization tasks.

        Returns
        -------
        list of str
            List of task IDs.
        """
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._taskid_list = self.request_data(api_name, api_path, req_param)

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
            req_param['task_id'] = taskid

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
            req_param['task_id'] = taskid

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

    def get_vm_operation(self, additional: bool = False) -> list[dict[str, object]]:
        """
        Get the list of virtual machines.

        Parameters
        ----------
        additional : bool, optional
            Whether to include additional information. Default is False.

        Returns
        -------
        list of dict
            List of VM information.
        """
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'list', 'additional': additional}

        info = self.request_data(api_name, api_path, req_param)

        for guest in info['data']['guests']:
            if 'guest_id' in guest:
                self._vm_guest_id_list.append(guest['guest_id'])
            if 'guest_name' in guest:
                self._vm_guest_name_list.append(guest['guest_name'])

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
        if autorun is not None and isinstance(autorun, int):
            req_param['autorun'] = autorun
        else:
            return 'autorun value must be an integer 0 (off), 1 (last state) or 2 (on)'

        if description is not None and isinstance(description, str):
            req_param['description'] = description
        else:
            return 'description must be a string, guest description'

        if new_guest_name is not None and isinstance(new_guest_name, str):
            req_param['new_guest_name'] = new_guest_name
        else:
            return 'new_guest_name must be a string, new guest name'

        if vcpu_num is not None and isinstance(vcpu_num, int):
            req_param['vcpu_num'] = vcpu_num
            return 'vcpu_num must be an integer, specify cpu number'

        if vram_size is not None and isinstance(vram_size, int):
            req_param['vram_size'] = vram_size
        else:
            return 'vram_size must be integer, specify ram size in MB'

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
        req_param = {'version': info['maxVersion'], 'method': 'create'}

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
            return 'Specify at least one of storage_names or storge_ids'
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

    def get_snapshot_list(self, guest_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Get the list of snapshots for a virtual machine.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.

        Returns
        -------
        dict[str, object] or str
            Snapshot list (gsnaps array) or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Snap'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        if guest_id is None:
            return 'Specify guest_id, you can get using get_vm_operation'
        req_param['guest_id'] = guest_id

        return self.request_data(api_name, api_path, req_param)

    def create_snapshot(self, guest_id: Optional[str] = None, desc: Optional[str] = None,
                        is_user_locked: bool = False, taken_by: str = 'user') -> dict[str, object] | str:
        """
        Create a snapshot of a virtual machine.

        Non-blocking: returns a task_id, poll get_task_info to check completion.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        desc : str, optional
            Snapshot description.
        is_user_locked : bool, optional
            Whether to lock the snapshot against automatic retention removal.
        taken_by : str, optional
            Who took the snapshot (username).

        Returns
        -------
        dict[str, object] or str
            Result containing task_id, or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Snap'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create_start'}

        if guest_id is None:
            return 'Specify guest_id, you can get using get_vm_operation'
        req_param['guest_id'] = guest_id
        if desc is not None:
            req_param['desc'] = desc
        req_param['taken_by'] = taken_by
        req_param['is_user_locked'] = is_user_locked

        return self.request_data(api_name, api_path, req_param)

    def delete_snapshot(self, guest_id: Optional[str] = None, gsnap_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Delete a snapshot of a virtual machine.

        Non-blocking: returns a task_id. The snapshot id (gsnap_id) is obtained from
        get_snapshot_list.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        gsnap_id : str, optional
            Snapshot ID (from get_snapshot_list).

        Returns
        -------
        dict[str, object] or str
            Result containing task_id, or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Snap'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete_start'}

        if guest_id is None or gsnap_id is None:
            return 'Specify guest_id and gsnap_id, you can get using get_vm_operation and get_snapshot_list'
        req_param['gsnap_ids'] = json.dumps([gsnap_id])
        req_param['deleted_by'] = 'user'
        req_param['site'] = 'main'

        return self.request_data(api_name, api_path, req_param)

    def restore_snapshot(self, guest_id: Optional[str] = None, gsnap_id: Optional[str] = None,
                         is_gsnap_created: bool = False, poweroff_guest: bool = True) -> dict[str, object] | str:
        """
        Restore a virtual machine from a snapshot.

        Non-blocking: returns a task_id.

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.
        gsnap_id : str, optional
            Snapshot ID (from get_snapshot_list).
        is_gsnap_created : bool, optional
            Whether to take a snapshot of the current state before restoring.
        poweroff_guest : bool, optional
            Whether to power off the guest before restoring.

        Returns
        -------
        dict[str, object] or str
            Result containing task_id, or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Snap'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'restore_start'}

        if guest_id is None or gsnap_id is None:
            return 'Specify guest_id and gsnap_id, you can get using get_vm_operation and get_snapshot_list'
        req_param['guest_id'] = guest_id
        req_param['gsnap_id'] = gsnap_id
        req_param['is_gsnap_created'] = is_gsnap_created
        req_param['poweroff_guest'] = poweroff_guest

        return self.request_data(api_name, api_path, req_param)

    def create_protection_plan(self, name: str, guest_id: str) -> dict[str, object] | str:
        """
        Create a VMM protection plan (Local Snapshot) for a virtual machine.

        Note: this API is implemented in version 1 only on the NAS (version 2
        returns error 103 for create/delete). The ``guest_id`` parameter is
        singular, not ``guest_ids``.

        Parameters
        ----------
        name : str
            Protection plan name.
        guest_id : str
            Guest VM ID.

        Returns
        -------
        dict[str, object] or str
            Result containing ``protect_id``, or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Plan'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'create',
                     'name': name, 'guest_id': guest_id}

        return self.request_data(api_name, api_path, req_param)

    def delete_protection_plan(self, protect_id: str) -> dict[str, object] | str:
        """
        Delete a VMM protection plan.

        Note: this API is implemented in version 1 only on the NAS.

        Parameters
        ----------
        protect_id : str
            Protection plan ID (from create_protection_plan or list_protection_plan).

        Returns
        -------
        dict[str, object] or str
            Result or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Plan'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'delete',
                     'protect_id': protect_id}

        return self.request_data(api_name, api_path, req_param)

    def list_protection_plan(self) -> dict[str, object] | str:
        """
        List VMM protection plans.

        Returns
        -------
        dict[str, object] or str
            Plan list (``protect_ids`` array) or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Plan'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': 1, 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_host_list(self) -> dict[str, object] | str:
        """
        Get the list of VMM hosts (v2 API).

        Returns
        -------
        dict[str, object] or str
            Host list or error message.
        """
        api_name = 'SYNO.Virtualization.Host'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_host_basic_list(self) -> dict[str, object] | str:
        """
        Get the basic list of VMM hosts (v2 API).

        Returns
        -------
        dict[str, object] or str
            Basic host list or error message.
        """
        api_name = 'SYNO.Virtualization.Host'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_basic'}

        return self.request_data(api_name, api_path, req_param)

    def get_network_list(self) -> dict[str, object] | str:
        """
        Get the list of VMM networks (v2 API).

        Returns
        -------
        dict[str, object] or str
            Network list or error message.
        """
        api_name = 'SYNO.Virtualization.Network'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_repo_list(self) -> dict[str, object] | str:
        """
        Get the list of VMM repositories (v2 API).

        Returns
        -------
        dict[str, object] or str
            Repository list or error message.
        """
        api_name = 'SYNO.Virtualization.Repo'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_guest_list_basic(self) -> dict[str, object] | str:
        """
        Get the basic list of VMM guests (v2 API).

        Returns
        -------
        dict[str, object] or str
            Basic guest list or error message.
        """
        api_name = 'SYNO.Virtualization.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_basic'}

        return self.request_data(api_name, api_path, req_param)

    def get_log_list(self) -> dict[str, object] | str:
        """
        Get the list of VMM logs.

        Returns
        -------
        dict[str, object] or str
            Log list or error message.
        """
        api_name = 'SYNO.Virtualization.Log'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_setting_general(self) -> dict[str, object] | str:
        """
        Get the VMM general settings.

        Returns
        -------
        dict[str, object] or str
            General settings or error message.
        """
        api_name = 'SYNO.Virtualization.Setting.General'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_package_list(self) -> dict[str, object] | str:
        """
        Get the list of VMM packages.

        Returns
        -------
        dict[str, object] or str
            Package list or error message.
        """
        api_name = 'SYNO.Virtualization.Package'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def get_login_info(self) -> dict[str, object] | str:
        """
        Get the VMM user login information.

        Returns
        -------
        dict[str, object] or str
            Login info or error message.
        """
        api_name = 'SYNO.Virtualization.User'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_login_info'}

        return self.request_data(api_name, api_path, req_param)

    def check_guest_availability(self, guest_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Check guest VM availability (read-only, safe pre-flight check).

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.

        Returns
        -------
        dict[str, object] or str
            Availability check result or error message.
        """
        api_name = 'SYNO.Virtualization.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'check_availability'}

        if guest_id is not None:
            req_param['guest_id'] = guest_id

        return self.request_data(api_name, api_path, req_param)

    def snapshot_can_do(self, guest_id: Optional[str] = None) -> dict[str, object] | str:
        """
        Check whether a snapshot operation can be performed (read-only validator).

        Parameters
        ----------
        guest_id : str, optional
            Guest VM ID.

        Returns
        -------
        dict[str, object] or str
            Feasibility result or error message.
        """
        api_name = 'SYNO.Virtualization.GuestProtect.Snap'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'can_do'}

        if guest_id is not None:
            req_param['guest_id'] = guest_id

        return self.request_data(api_name, api_path, req_param)

    # TODO create vitrual machine function
