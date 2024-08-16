from __future__ import annotations
from . import base_api


class Backup(base_api.BaseApi):

    def backup_repository_get(self, task_id: str) -> dict[str, object] | str:
        '''
        Get repository information for given task.   
        '''
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_repository_list(self) -> dict[str, object] | str:
        '''
        Get a list of all present repositories in Hyper Backup.
        '''
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_list(self) -> dict[str, object] | str:
        '''
        Get current restoring information and a list of present tasks in Hyper Backup.
        '''
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_status(self, task_id: str) -> dict[str, object] | str:
        '''
        Get status and state of task.    
        '''
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_get(self, task_id: str) -> dict[str, object] | str:
        '''
        Get detailed task information.  
        '''
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_result(self, task_id: str) -> dict[str, object] | str:
        '''
        Get last result summary information of a task.
        '''
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'blOnline': 'false',
                     'additional': '["last_bkp_time","next_bkp_time","last_bkp_result","is_modified","last_bkp_progress"]',
                     'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_run(self, task_id: str) -> dict[str, object] | str:
        '''
        Run backup task for corresponding task_id.
        If the task is not in backupable state, the API will return an error, usually 44xx.
        '''
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
        '''
        Cancel currently running backup task.
        If the task is not running, the API will return an error, usually 44xx.
        '''
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
        '''
        Suspend currently running backup task.
        If the task is not running or not yet suspendable, the API will return an error, usually 44xx.
        '''
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
        '''
        Discard currently suspended backup task.
        If the task is not suspended, the request will not fail, and will fail to discard the task, leaving the task state as "Failed".
        '''
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
        '''
        Discard currently suspended backup task.
        If the task is not suspended, the request will not fail, and will fail to resume the task, leaving the task state as "Failed".
        '''
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
        '''
        Remove one or more backup tasks.
        Data in destination will not be removed. It is still possible to relink the task using the original .hbk file.
        The API requires an array of tasks to remove, it should be passed as a string with the following format:
        `task_id_list = '[29]'` || `task_id_list = '[29,15]'` 
        '''
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'delete',
            'is_remove_data': False,
            'task_id_list': task_id_list
        }
        return self.request_data(api_name, api_path, req_param)
    
    def integrity_check_run(self, task_id: str) -> dict[str, object] | str:
        '''
        Run integrity check for backup task.
        If the task is running, the request will not fail, and will fail to perform the integrity check due to target is busy.
        '''
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
        '''
        Cancel currently running integrity check for backup task.
        If integrity check is not running, the API will return an error, usually 44xx.
        '''
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
        '''
        Get Hyper Backup UI logs.

        `filter_date_from` and `filter_date_to` need to be passed in epoch format.
        '''
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

    def vault_target_list(self) -> dict[str, object]:  # Should be working now
        '''
        List all available targets in Vault.
        '''
        api_name = 'SYNO.Backup.Service.VersionBackup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def vault_concurrency_get(self) -> dict[str, object]:
        '''
        Get number of concurrent tasks allowed to run in HB Vault. Default value is 2.
        '''
        api_name = 'SYNO.Backup.Service.VersionBackup.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def vault_concurrency_set(self, parallel_backup_limit: int = 2) -> dict[str, object]:
        '''
        Set number of concurrent tasks allowed to run in HB Vault. Default value is 2.
        '''
        api_name = 'SYNO.Backup.Service.VersionBackup.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'set',
            'parallel_backup_limit': parallel_backup_limit
        }
        return self.request_data(api_name, api_path, req_param)
    
    def vault_target_settings_get(self, target_id: int) -> dict[str, object]:
        '''
        Get settings of target.
        '''
        api_name = 'SYNO.Backup.Service.VersionBackup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'detail',
            'target_id': target_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def vault_task_statistics_get(self, task_id: int) -> dict[str, object]:
        '''
        Get statistics for given task.
        '''
        api_name = 'SYNO.SDS.Backup.Server.Common.Statistic'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get',
            'additional': '["volume_size"]',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)
    
    def vault_target_logs_get(self, 
                              target_id: int, 
                              limit: int = 1000, 
                              offset: int = 0) -> dict[str, object]:
        '''
        Get logs for given task.
        '''
        api_name = 'SYNO.SDS.Backup.Server.Common.Log'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'list',
            'limit': limit,
            'offset': offset,
            'filter_target_id': target_id
        }
        return self.request_data(api_name, api_path, req_param)