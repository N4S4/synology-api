"""Synology Hyper Backup API."""
from __future__ import annotations
from . import base_api


class Backup(base_api.BaseApi):
    """Synology Hyper Backup API."""

    def backup_repository_get(self, task_id: str) -> dict[str, object] | str:
        """
        Get repository information for a given task.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            Repository information.
        """
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'],
                     'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_repository_list(self) -> dict[str, object] | str:
        """
        Get a list of all present repositories in Hyper Backup.

        Returns
        -------
        dict[str, object] or str
            List of repositories.
        """
        api_name = 'SYNO.Backup.Repository'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_list(self) -> dict[str, object] | str:
        """
        Get current restoring information and a list of present tasks in Hyper Backup.

        Returns
        -------
        dict[str, object] or str
            List of tasks and restoring information.
        """
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_status(self, task_id: str) -> dict[str, object] | str:
        """
        Get status and state of a task.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            Status and state information.
        """
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'],
                     'method': 'status', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_get(self, task_id: str) -> dict[str, object] | str:
        """
        Get detailed task information.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            Task information.
        """
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'],
                     'method': 'get', 'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_result(self, task_id: str) -> dict[str, object] | str:
        """
        Get last result summary information of a task.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            Last result summary.
        """
        api_name = 'SYNO.Backup.Task'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'status', 'blOnline': 'false',
                     'additional': '["last_bkp_time","next_bkp_time","last_bkp_result","is_modified","last_bkp_progress"]',
                     'task_id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def backup_task_run(self, task_id: str) -> dict[str, object] | str:
        """
        Run backup task for corresponding task_id.

        If the task is not in backupable state, the API will return an error, usually 44xx.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Cancel currently running backup task.

        If the task is not running, the API will return an error, usually 44xx.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Suspend currently running backup task.

        If the task is not running or not yet suspendable, the API will return an error, usually 44xx.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Discard currently suspended backup task.

        If the task is not suspended, the request will not fail, and will fail to discard the task, leaving the task state as "Failed".

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Resume currently suspended backup task.

        If the task is not suspended, the request will not fail, and will fail to resume the task, leaving the task state as "Failed".

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Remove one or more backup tasks.

        Data in destination will not be removed. It is still possible to relink the task using the original .hbk file.
        The API requires an array of tasks to remove, it should be passed as a string with the following format:
        `task_id_list = '[29]'` or `task_id_list = '[29,15]'`

        Parameters
        ----------
        task_id_list : str
            List of task IDs as a string.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Run integrity check for backup task.

        If the task is running, the request will not fail, and will fail to perform the integrity check due to target being busy.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        Cancel currently running integrity check for backup task.

        If integrity check is not running, the API will return an error, usually 44xx.

        Parameters
        ----------
        task_id : str
            Task ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.Backup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'error_detect_cancel',
            'task_id': task_id
        }
        return self.request_data(api_name, api_path, req_param)

    def hb_logs_get(
        self,
        limit: int = 1000,
        offset: int = 0,
        filter_keyword: str = '',
        # filter_level: str = '', For some reason when passing filter_level, the API returns error 120.
        filter_date_from: int = 0,
        filter_date_to: int = 0
    ) -> dict[str, object] | str:
        """
        Get Hyper Backup UI logs.

        `filter_date_from` and `filter_date_to` need to be passed in epoch format.

        Parameters
        ----------
        limit : int, optional
            Maximum number of logs to return (default is 1000).
        offset : int, optional
            Offset for pagination (default is 0).
        filter_keyword : str, optional
            Keyword to filter logs (default is '').
        filter_date_from : int, optional
            Start date in epoch format (default is 0).
        filter_date_to : int, optional
            End date in epoch format (default is 0).

        Returns
        -------
        dict[str, object] or str
            Logs information.
        """
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

    def vault_target_list(self) -> dict[str, object]:
        """
        List all available targets in Vault.

        Returns
        -------
        dict[str, object]
            List of available targets.
        """
        api_name = 'SYNO.Backup.Service.VersionBackup.Target'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['minVersion'], 'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def vault_concurrency_get(self) -> dict[str, object]:
        """
        Get number of concurrent tasks allowed to run in HB Vault.

        Returns
        -------
        dict[str, object]
            Number of concurrent tasks (default is 2).
        """
        api_name = 'SYNO.Backup.Service.VersionBackup.Config'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)

    def vault_concurrency_set(self, parallel_backup_limit: int = 2) -> dict[str, object]:
        """
        Set number of concurrent tasks allowed to run in HB Vault.

        Parameters
        ----------
        parallel_backup_limit : int, optional
            Number of concurrent tasks (default is 2).

        Returns
        -------
        dict[str, object]
            API response.
        """
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
        """
        Get settings of a target.

        Parameters
        ----------
        target_id : int
            Target ID.

        Returns
        -------
        dict[str, object]
            Target settings.
        """
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
        """
        Get statistics for a given task.

        Parameters
        ----------
        task_id : int
            Task ID.

        Returns
        -------
        dict[str, object]
            Task statistics.
        """
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

    def vault_target_logs_get(
        self,
        target_id: int,
        limit: int = 1000,
        offset: int = 0
    ) -> dict[str, object]:
        """
        Get logs for a given target.

        Parameters
        ----------
        target_id : int
            Target ID.
        limit : int, optional
            Maximum number of logs to return (default is 1000).
        offset : int, optional
            Offset for pagination (default is 0).

        Returns
        -------
        dict[str, object]
            Logs information.
        """
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

    def backup_app_get_icon(self) -> dict:
        """
        Get the Hyper Backup application icon.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App``.
        """
        api_name = "SYNO.Backup.App"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_icon",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_app_list(self) -> dict:
        """
        List all backup tasks currently configured in Hyper Backup.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Backup``.
        """
        api_name = "SYNO.Backup.App.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_app_mysql_check(self) -> dict:
        """
        Check whether MySQL/MariaDB backup support is available on the NAS.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Backup``.
        """
        api_name = "SYNO.Backup.App.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "mysql_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_app_surveillance_check(self) -> dict:
        """
        Check whether Surveillance Station backup support is available on the NAS.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Backup``.
        """
        api_name = "SYNO.Backup.App.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "surveillance_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_app_list(self) -> dict:
        """
        List available restore points/tasks in Hyper Backup.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Restore``.
        """
        api_name = "SYNO.Backup.App.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_app_mysql_check(self) -> dict:
        """
        Check whether MySQL/MariaDB restore capability is available.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Restore``.
        """
        api_name = "SYNO.Backup.App.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "mysql_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_app_surveillance_check(self) -> dict:
        """
        Check whether Surveillance Station restore capability is available.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.App.Restore``.
        """
        api_name = "SYNO.Backup.App.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "surveillance_check",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_backup(self) -> dict:
        """
        Trigger an automatic backup based on the configured schedule.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "backup",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_download_private_key(self) -> dict:
        """
        Download the private key used for encrypted backup archives.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "download_private_key",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_get(self) -> dict:
        """
        Get the current auto-backup configuration (schedule, targets, encryption).

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_get_meta(self) -> dict:
        """
        Get metadata about the auto-backup configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_meta",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_list(self) -> dict:
        """
        List all auto-backup configuration entries.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_restore(self) -> dict:
        """
        Restore system configuration from an auto-backup archive.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "restore",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_set(self) -> dict:
        """
        Set or update the auto-backup configuration.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_status(self) -> dict:
        """
        Get the current status of auto-backup operations.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "status",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def autobackup_config_upload_private_key(self) -> dict:
        """
        Upload a private key for encrypting future auto-backup archives.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.AutoBackup``.
        """
        api_name = "SYNO.Backup.Config.AutoBackup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "upload_private_key",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_config_download(self) -> dict:
        """
        Download a system configuration backup archive.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Backup``.
        """
        api_name = "SYNO.Backup.Config.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "download",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_config_list(self) -> dict:
        """
        List available system configuration backup archives.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Backup``.
        """
        api_name = "SYNO.Backup.Config.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_config_start(self) -> dict:
        """
        Start a system configuration backup immediately.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Backup``.
        """
        api_name = "SYNO.Backup.Config.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "start",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def backup_config_status(self) -> dict:
        """
        Get the status of a system configuration backup operation.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Backup``.
        """
        api_name = "SYNO.Backup.Config.Backup"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "status",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_check(self) -> dict:
        """
        Verify the integrity and compatibility of a restore archive.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_delete(self) -> dict:
        """
        Delete a saved system configuration restore archive.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_list(self) -> dict:
        """
        List available system configuration restore archives.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_list_conflict(self) -> dict:
        """
        List any conflicts detected in a restore archive.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list_conflict",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_start(self) -> dict:
        """
        Start a system configuration restore operation.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "start",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_status(self) -> dict:
        """
        Get the status of a restore operation.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "status",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def restore_config_upload(self) -> dict:
        """
        Upload a system configuration archive for restore.

        Returns
        -------
        dict
            API response from ``SYNO.Backup.Config.Restore``.
        """
        api_name = "SYNO.Backup.Config.Restore"
        info = self.gen_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "upload",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)


class S2SServer(base_api.BaseApi):
    """Synology S2S (Server-to-Server) backup API wrapper."""

    def s2s_server_get(self) -> dict:
        """
        Get the current Server-to-Server backup server configuration (task list, schedule, targets).

        Returns
        -------
        dict
            API response from ``SYNO.S2S.Server``.
        """
        api_name = "SYNO.S2S.Server"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def s2s_server_set(self) -> dict:
        """
        Set or update the Server-to-Server backup server configuration.

        Returns
        -------
        dict
            API response from ``SYNO.S2S.Server``.
        """
        api_name = "SYNO.S2S.Server"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)


# ------------------------------------------------------------------
# Disaster Recovery / Snapshot Replication
# ------------------------------------------------------------------


class DRNode(base_api.BaseApi):
    """Synology Disaster Recovery / Snapshot Replication API wrapper."""

    def dr_node_check_and_reset(self) -> dict:
        """
        Check the DR node status and reset if needed (used during setup/recovery).

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_and_reset",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_get_net_info(self) -> dict:
        """
        Get network information for the local DR node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_net_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_get_remote_net_info(self) -> dict:
        """
        Get network information for the remote DR partner node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_remote_net_info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_info(self) -> dict:
        """
        Get general information and status of the DR node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_reset(self) -> dict:
        """
        Reset the DR node configuration to factory defaults.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "reset",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_test_connection(self) -> dict:
        """
        Test the network connection to the remote DR partner node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_connection",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_test_download_speed(self) -> dict:
        """
        Run a download speed test to the remote DR partner.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_download_speed",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_test_privilege(self) -> dict:
        """
        Verify that the DR node has sufficient privileges for replication.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_privilege",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_node_test_sync_speed(self) -> dict:
        """
        Run a sync speed benchmark between local and remote DR nodes.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node``.
        """
        api_name = "SYNO.DR.Node"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_sync_speed",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_create(self) -> dict:
        """
        Create credentials for authenticating with a remote DR partner node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_delete(self) -> dict:
        """
        Delete stored DR partner credentials.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_get(self) -> dict:
        """
        Get the current DR partner credential details.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_list(self) -> dict:
        """
        List all stored DR partner credentials.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_relay(self) -> dict:
        """
        Relay/forward credentials through an intermediate DR node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "relay",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_reverse_create(self) -> dict:
        """
        Create reverse credentials so the partner node can authenticate back.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "reverse_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_set(self) -> dict:
        """
        Set or update DR partner credentials.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_temp_create(self) -> dict:
        """
        Create temporary credentials for one-time DR operations.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "temp_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_temp_reverse_create(self) -> dict:
        """
        Create temporary reverse credentials for partner node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "temp_reverse_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_test_create(self) -> dict:
        """
        Test-validate credential creation parameters before committing.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_test_reverse_create(self) -> dict:
        """
        Test-validate reverse credential parameters before committing.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_reverse_create",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_credential_test_set(self) -> dict:
        """
        Test-validate credential update parameters before committing.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Credential``.
        """
        api_name = "SYNO.DR.Node.Credential"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "test_set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_session_create(self) -> dict:
        """
        Create a new DR replication session with the partner node.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Session``.
        """
        api_name = "SYNO.DR.Node.Session"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "create",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_session_delete(self) -> dict:
        """
        Delete/terminate an existing DR replication session.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Session``.
        """
        api_name = "SYNO.DR.Node.Session"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_session_find(self) -> dict:
        """
        Find and enumerate active DR replication sessions.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Session``.
        """
        api_name = "SYNO.DR.Node.Session"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "find",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_session_get(self) -> dict:
        """
        Get details and status of a specific DR replication session.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Session``.
        """
        api_name = "SYNO.DR.Node.Session"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_session_temp_create(self) -> dict:
        """
        Create a temporary DR session for testing or one-off sync.

        Returns
        -------
        dict
            API response from ``SYNO.DR.Node.Session``.
        """
        api_name = "SYNO.DR.Node.Session"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "temp_create",
            "version": 2,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_log_clear(self) -> dict:
        """
        Clear all entries from the Disaster Recovery log.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Log``.
        """
        api_name = "SYNO.DisasterRecovery.Log"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "clear",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_log_export(self) -> dict:
        """
        Export the Disaster Recovery log to a downloadable file.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Log``.
        """
        api_name = "SYNO.DisasterRecovery.Log"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "export",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_log_list(self) -> dict:
        """
        List all entries in the Disaster Recovery log.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Log``.
        """
        api_name = "SYNO.DisasterRecovery.Log"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "list",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_check_worm_lockable(self) -> dict:
        """
        Check whether a snapshot can be WORM-locked (Write Once Read Many).

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "check_worm_lockable",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_clear_worm_lock_notify_time(self) -> dict:
        """
        Clear the WORM lock expiration notification timer.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "clear_worm_lock_notify_time",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_delete(self) -> dict:
        """
        Delete a retention policy entry.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "delete",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_get(self) -> dict:
        """
        Get the current snapshot retention policy configuration.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_get_timezone(self) -> dict:
        """
        Get the timezone used for retention policy scheduling.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_timezone",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_get_worm_lock(self) -> dict:
        """
        Get the WORM lock configuration for protected snapshots.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "get_worm_lock",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_info(self) -> dict:
        """
        Get general information about the retention policy settings.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "info",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_notify_worm_lock_disable(self) -> dict:
        """
        Disable WORM lock expiration notifications.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "notify_worm_lock_disable",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_set(self) -> dict:
        """
        Set or update the snapshot retention policy.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_set_timezone(self) -> dict:
        """
        Set the timezone used for retention policy scheduling.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_timezone",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)

    def dr_retention_set_worm_lock(self) -> dict:
        """
        Enable/configure WORM lock protection for snapshots.

        Returns
        -------
        dict
            API response from ``SYNO.DisasterRecovery.Retention``.
        """
        api_name = "SYNO.DisasterRecovery.Retention"
        info = self.core_list[api_name]
        api_path = info["path"]
        req_param = {
            "method": "set_worm_lock",
            "version": 1,
        }
        return self.request_data(api_name, api_path, req_param)
