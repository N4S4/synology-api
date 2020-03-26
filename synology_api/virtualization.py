from .synology import Synology
from .synology import api_call


class Virtualization(Synology):
    app = 'Virtualization'

    @api_call()
    def get_task_list(self):
        return self.api_request('API.Task.Info', 'list')

    @api_call()
    def clear_task(self, taskid):
        if taskid is None:
            raise ValueError("Invalid taskid")

        return self.api_request('API.Task.Info', 'clear', {'taskid': taskid})

    @api_call()
    def get_task_info(self, taskid):
        if taskid is None:
            raise ValueError("Invalid taskid")

        return self.api_request('API.Task.Info', 'get', {'taskid': taskid})

    @api_call()
    def get_network_group_list(self):
        return self.api_request('API.Network', 'list')

    @api_call()
    def get_storage_operation(self):
        return self.api_request('API.Storage', 'list')

    @api_call()
    def get_host_operation(self):
        return self.api_request('API.Host', 'list')

    @api_call()
    def get_vm_operation(self, additional=False):
        return self.api_request('API.Guest', 'list', {'additional': additional})

    @staticmethod
    def _get_vm(guest_id, guest_name):
        req_param = {}

        if guest_id is None and guest_name is None:
            raise ValueError('Specify at least one guest_id or guest_name, you can get using get_vm_operation')
        if guest_name is not None:
            req_param['guest_name'] = guest_name
            guest_id = None
        if guest_id is not None:
            req_param['guest_id'] = guest_id
            guest_name = None
        return req_param

    @api_call()
    def get_specific_vm_info(self, additional=False, guest_id=None, guest_name=None):
        req_param = {}
        if guest_id is None and guest_name is None:
            raise ValueError('Specify at least one guest_id or guest_name, you can get using get_vm_operation')
        if guest_name is not None:
            req_param['guest_name'] = guest_name
        if guest_id is not None:
            req_param['guest_id'] = guest_id

        req_param['additional'] = additional

        return self.api_request('API.Guest', 'get', req_param)

    @api_call()
    def set_vm_property(self, guest_id=None, guest_name=None, autorun=None, description=None, new_guest_name=None,
                        vcpu_num=None, vram_size=None):
        req_param = self._get_vm(guest_id, guest_name)
        if autorun is not None and isinstance(autorun, int) and autorun in [0, 1, 2]:
            req_param['autorun'] = autorun
        else:
            raise ValueError('autorun value must be an integer 0 (off), 1 (last state) or 2 (on)')

        if description is not None and isinstance(description, str):
            req_param['description'] = description
        else:
            raise ValueError('description must be a string, guest description')

        if new_guest_name is not None and isinstance(new_guest_name, str):
            req_param['new_guest_name'] = new_guest_name
        else:
            raise ValueError('new_guest_name must be a string, new guest name')

        if vcpu_num is not None and isinstance(vcpu_num, int):
            req_param['vcpu_num'] = vcpu_num
            raise ValueError('vcpu_num must be an integer, specify cpu number')

        if vram_size is not None and isinstance(vram_size, int):
            req_param['vram_size'] = vram_size
        else:
            raise ValueError('vram_size must be integer, specify ram size in MB')

        return self.api_request('API.Guest', 'set', req_param)

    @api_call()
    def delete_vm(self, guest_id=None, guest_name=None):
        req_param = self._get_vm(guest_id, guest_name)

        return self.api_request('API.Guest', 'delete', req_param)

    @api_call()
    def vm_power_on(self, guest_id=None, guest_name=None, host_id=None, host_name=None):
        req_param = self._get_vm(guest_id, guest_name)

        if host_id is not None:
            req_param['host_id'] = host_id
            host_name = None
        if host_name is not None:
            req_param['host_name'] = host_name
            host_id = None
        if host_id is None and host_name is None:
            print('host_id and host_name are not specified, it will follow autoselect option from the cluster settings')

        return self.api_request('API.Guest.Action', 'poweron', req_param)

    @api_call()
    def vm_force_power_off(self, guest_id=None, guest_name=None):
        req_param = self._get_vm(guest_id, guest_name)

        return self.api_request('API.Guest.Action', 'poweroff', req_param)

    @api_call()
    def vm_shut_down(self, guest_id=None, guest_name=None):
        req_param = self._get_vm(guest_id, guest_name)

        return self.api_request('API.Guest.Action', 'shutdown', req_param)

    @api_call()
    def get_images_list(self):
        return self.api_request('API.Guest.Image', 'list')

    @api_call()
    def delete_image(self, image_id=None, image_name=None):
        req_param = {}

        if image_id is None and image_name is None:
            raise ValueError('Specify at least one of image_id or image_name')
        if image_name is not None:
            req_param['image_name'] = image_name
            image_name = None
        if image_id is not None:
            req_param['image_id'] = image_id
            image_name = None

        return self.api_request('API.Guest.Image', 'delete', req_param)

    @api_call()
    def create_image(self, auto_clean_task=True, storage_names=None, storage_ids=None, type=None, ds_file_path=None,
                     image_name=None):

        req_param = {'auto_clean_task': auto_clean_task}

        if storage_names is None and storage_ids is None:
            raise ValueError('Specify at least one of storage_names or storge_ids')
        if storage_ids is not None:
            req_param['storage_ids'] = storage_ids
            storage_names = None
        if storage_names is not None:
            req_param['storage_names'] = storage_names
            storage_ids = None

        if type is None:
            raise ValueError('Specify what type between disk, vdsm or iso')
        if type is not None:
            req_param['type'] = type

        if ds_file_path is None:
            raise ValueError('Specify file path, the path should begin with a shared folder')
        if ds_file_path is not None:
            req_param['ds_file_path'] = ds_file_path

        if image_name is None:
            raise ValueError('Specify image_name')
        if image_name is not None:
            req_param['image_name'] = image_name

        return self.api_request('API.Guest.Image', 'create', req_param)

    # TODO create vitrual machine function
