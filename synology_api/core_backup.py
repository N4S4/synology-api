from typing import Optional
from . import base_api_core


class Backup(base_api_core.Core):
    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None
                 ) -> None:
        super(Backup, self).__init__(ip_address, port, username, password, secure, cert_verify, dsm_version, debug,
                                     otp_code)
        return

    def backup_repository_get(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': taskid}

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

    def backup_task_status(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'task_id': taskid}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_get(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'get', 'task_id': taskid}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_result(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'blOnline': 'false',
                     'additional': '["last_bkp_time","next_bkp_time","last_bkp_result","is_modified","last_bkp_progress"]',
                     'task_id': taskid}

        return self.request_data(api_name, api_path, req_param)

    def vault_target_list(self) -> dict[str, object]:  # TODO not working
        api_name = 'SYNO.Backup.Service.VersionBackup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)
