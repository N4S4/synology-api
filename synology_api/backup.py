from . import auth as syn


class Backup:
    def __init__(self, ip_address, port, username, password, secure=False):

        self.session = syn.Authentication(ip_address, port, username, password, secure)

        self.session.login('Core')
        self.session.get_api_list('Core')
        self.session.get_api_list()

        self.request_data = self.session.request_data
        self.core_list = self.session.app_api_list
        self.gen_list = self.session.full_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

        print('You are now logged in!')

    def logout(self):
        self.session.logout('Core')

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

