from . import base_api_core


class Backup(base_api_core.Core):
    def __init__(self, ip_address, port, username, password, secure=False, cert_verify=False):
        super(Backup, self).__init__(ip_address, port, username, password, secure, cert_verify)

    def backup_repository_get(self):
        api_name = 'SYNO.Backup.Repository'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)
        
    def backup_repository_list(self):
        api_name = 'SYNO.Backup.Repository'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
        
    def backup_task_list(self):
        api_name = 'SYNO.Backup.Task'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
        
    def backup_task_status(self):
        api_name = 'SYNO.Backup.Task'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        return self.request_data(api_name, api_path, req_param)
        
    def backup_task_get(self):
        api_name = 'SYNO.Backup.Task'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

