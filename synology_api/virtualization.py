from . import auth as syn


class Virtualization:

    def __init__(self, ip_address, port, username, password, secure=False):

        self.session = syn.Authentication(ip_address, port, username, password, secure)

        self.request_data = self.session.request_data

        self._taskid_list = []
        self._network_group_list = []
        self._storages_list = []
        self._host_operation_list = []
        self._vm_guest_id_list = []
        self._vm_guest_name_list = []
        self._vm_created_taskid_list = []

        self.session.login('Virtualization')
        self.session.get_api_list('Virtualization')

        self.file_station_list = self.session.app_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

    def get_task_list(self):
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._taskid_list = self.request_data(api_name, api_path, req_param)

        return self._taskid_list

    def clear_task(self, taskid):
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear'}

        if taskid is None:
            return 'Enter a valid taskid, choose between get_task_list results'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_task_info(self, taskid):
        api_name = 'SYNO.Virtualization.API.Task.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        if taskid is None:
            return 'Enter a valid taskid, choose between get_task_list results'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_network_group_list(self):
        api_name = 'SYNO.Virtualization.API.Network'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._network_group_list = self.request_data(api_name, api_path, req_param)

        return self._network_group_list

    def get_storage_operation(self):
        api_name = 'SYNO.Virtualization.API.Storage'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._storages_list = self.request_data(api_name, api_path, req_param)

        return self._storages_list

    def get_host_operation(self):
        api_name = 'SYNO.Virtualization.API.Host'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        self._host_operation_list = self.request_data(api_name, api_path, req_param)

        return self._host_operation_list

    def get_vm_operation(self, additional=False):
        api_name = 'SYNO.Virtualization.API.Guest'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional}

        info = self.request_data(api_name, api_path, req_param)

        for k, v in info['data']['guests']:
            if k == 'guest_id':
                self._vm_guest_id_list.append(info['data']['guests'][k])
            elif k == 'guest_name':
                self._vm_guest_name_list.append(info['data']['guests'][k])

        return info

    def get_specific_vm_info(self, additional=None, guest_id=None, guest_name=None):
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

    def set_vm_property(self, guest_id=None, guest_name=None, autorun=None, description=None, new_guest_name=None,
                        vcpu_num=None, vram_size=None):
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

    def delete_vm(self, guest_id, guest_name):
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

    def vm_power_on(self, guest_id=None, guest_name=None, host_id=None, host_name=None):
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

    def vm_force_power_off(self, guest_id=None, guest_name=None):
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

    def vm_shut_down(self, guest_id=None, guest_name=None):
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

    def get_images_list(self):
        api_name = 'SYNO.Virtualization.API.Guest.Image'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def delete_image(self, image_id=None, image_name=None):
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

    def create_image(self, auto_clean_task=True, storage_names=None, storage_ids=None, type=None, ds_file_path=None,
                     image_name=None):
        api_name = 'SYNO.Virtualization.API.Guest.Image'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create', 'auto_clean_task': auto_clean_task}

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

    # TODO create vitrual machine function
