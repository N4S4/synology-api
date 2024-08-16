from __future__ import annotations
from . import base_api


class Backup(base_api.BaseApi):

    def backup_repository_get(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_repository_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_list(self) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_status(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_get(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_result(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'blOnline': 'false',
                     'additional': '["last_bkp_time","next_bkp_time","last_bkp_result","is_modified","last_bkp_progress"]',
                     'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_run(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'backup',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_cancel(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'cancel',
            'task_state': 'backupable',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_suspend(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'suspend',
            'task_state': 'backupable',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_discard(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'discard',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_resume(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'resume',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def backup_task_remove(self, task_id_list: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'delete',
            'is_remove_data': 'false',
            'task_id_list': task_id_list
        }
        return self.request_data(api_name, api_path, req_param)
    
    def integrity_check_run(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'error_detect',
            'detect_data': True,
            'sessId': 'null',
            'sessKey': 'null',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def integrity_check_cancel(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'error_detect_cancel',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)

    def hb_logs_get(self, 
                    limit: int = 1000, 
                    offset: int = 0,
                    filter_keyword: str = '',
                    # filter_level: str = '', For some reason when passing filter_level, the API returns error 120.
                    filter_date_from: int = 0,
                    filter_date_to: int = 0) -> dict[str, object] | str:
        api_name = 'SYNO.SDS.Backup.Client.Common.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'list',
            'limit': limit,
            'offset': offset,
            'filter_keyword': filter_keyword,
            # 'filter_level': filter_level,
            'filter_date_from': filter_date_from,
            'filter_date_to': filter_date_to
        }
        return self.request_data(api_name, api_path, req_param)

    def vault_target_list(self) -> dict[str, object]:  # TODO not working
        api_name = 'SYNO.Backup.Service.VersionBackup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
