from __future__ import annotations
from typing import Optional, Any
from . import base_api


class DownloadStation(base_api.BaseApi):

    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 device_id: Optional[str] = None,
                 device_name: Optional[str] = None,
                 interactive_output: bool = True,
                 download_st_version: int = None
                 ) -> None:

        super(DownloadStation, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                              dsm_version, debug, otp_code, device_id, device_name, 'DownloadStation')

        self._bt_search_id: str = ''
        self._bt_search_id_list: list[str] = []
        self.session.get_api_list('DownloadStation')

        self.download_list: Any = self.session.app_api_list

        self.interactive_output: bool = interactive_output

        if download_st_version == 2:
            self.download_st_version = '2'
        else:
            self.download_st_version = ''

    def get_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.Info'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_config(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.Info'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getconfig'}

        return self.request_data(api_name, api_path, req_param)

    def set_server_config(self,
                          bt_max_download: Optional[int] = None,
                          bt_max_upload: Optional[int] = None,
                          emule_max_download: Optional[int] = None,
                          emule_max_upload: Optional[int] = None,
                          nzb_max_download: Optional[int] = None,
                          http_max_download: Optional[int] = None,
                          ftp_max_download: Optional[int] = None,
                          emule_enabled: Optional[bool] = None,
                          unzip_service_enabled: Optional[bool] = None,
                          default_destination: Optional[str] = None,
                          emule_default_destination: Optional[str] = None
                          ) -> dict[str, object] | str:

        api_name = 'SYNO.DownloadStation.Info'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'setserverconfig'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def schedule_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.Schedule'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getconfig'}

        return self.request_data(api_name, api_path, req_param)

    def schedule_set_config(self, enabled: bool = False, emule_enabled: bool = False) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.Schedule'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'setconfig', 'enabled': str(enabled).lower(),
                     'emule_enabled': str(emule_enabled).lower()}

        if type(enabled) is not bool or type(emule_enabled) is not bool:
            return 'Please set enabled to True or False'

        return self.request_data(api_name, api_path, req_param)

    def tasks_list(self,
                   additional_param: Optional[str | list[str]] = None,
                   offset: int = 0,
                   limit: int = -1
                   ) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional_param, 'limit': limit,
                     'offset': offset}

        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        if type(additional_param) is list:
            req_param['additional'] = ",".join(additional_param)

        return self.request_data(api_name, api_path, req_param)

    def tasks_info(self, task_id, additional_param: Optional[str | list[str]] = None) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo', 'id': task_id, 'additional': additional_param}

        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        if type(additional_param) is list:
            req_param['additional'] = ",".join(additional_param)

        if type(task_id) is list:
            req_param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, req_param)

    def tasks_source(self, task_id) -> bytes:
        # DownloadStation2 is required here
        api_name = 'SYNO.DownloadStation2.Task.Source'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'download', 'id': task_id}

        return self.request_data(api_name, api_path, req_param, response_json=False).content

    def create_task(self, url, destination) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create', 'type': 'url',
                     'create_list': 'true', 'destination': destination, 'url': f'["{url}"]'}

        return self.request_data(api_name, api_path, req_param)

    def delete_task(self, task_id: str, force: bool = False) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'delete', 'id': task_id,
                 'force_complete': str(force).lower()}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def pause_task(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'pause', 'id': task_id}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def resume_task(self, task_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'resume', 'id': task_id}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def edit_task(self, task_id: str, destination: str = 'sharedfolder') -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'edit', 'id': task_id, 'destination': destination}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def get_statistic_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.Statistic'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, param)

    def get_rss_info_list(self, offset: Optional[int] = None, limit: Optional[int] = None) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.RSS.Site'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'list'}

        if offset is not None:
            param['offset'] = offset
        if limit is not None:
            param['limit'] = limit

        return self.request_data(api_name, api_path, param)

    def refresh_rss_site(self, rss_id: Optional[str] = None) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation.RSS.Site'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'refresh', 'id': rss_id}

        if rss_id is None:
            return 'Enter a valid ID check if you have any with get_rss_list()'
        elif type(rss_id) is list:
            rss_id = ','.join(rss_id)
            param['id'] = rss_id

        return self.request_data(api_name, api_path, param)

    def rss_feed_list(self,
                      rss_id: Optional[str] = None,
                      offset: Optional[int] = None,
                      limit: Optional[int] = None
                      ) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.RSS.Feed'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'list', 'id': rss_id}

        if rss_id is None:
            return 'Enter a valid ID check if you have any with get_rss_list()'
        elif type(rss_id) is list:
            rss_id = ','.join(rss_id)
            param['id'] = rss_id

        if offset is not None:
            param['offset'] = offset
        if limit is not None:
            param['limit'] = limit

        return self.request_data(api_name, api_path, param)

    def start_bt_search(self, keyword: Optional[str] = None, module: str = 'all') -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'start'}

        if keyword is None:
            return 'Did you enter a keyword to search?'
        else:
            param['keyword'] = keyword

        param['module'] = module

        self._bt_search_id = self.request_data(api_name, api_path, param)['data']['taskid']

        self._bt_search_id_list.append(self._bt_search_id)

        message = ('You can now check the status of request with '
                   'get_bt_search_results(), your id is: '
                   + self._bt_search_id)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._bt_search_id}

        return output

    def get_bt_search_results(self,
                              taskid: Optional[str] = None,
                              offset: Optional[int] = None,
                              limit: Optional[int] = None,
                              sort_by: Optional[str] = None,
                              sort_direction: Optional[str] = None,
                              filter_category: Optional[str] = None,
                              filter_title: Optional[str] = None
                              ) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'list', 'taskid': taskid}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'param', 'taskid']:
                if val is not None:
                    param[str(key)] = val

        if taskid is None:
            return 'Enter a valid taskid, you can choose one of ' + str(self._bt_search_id_list)
        elif type(taskid) is list:
            param['taskid'] = ','.join(taskid)

        return self.request_data(api_name, api_path, param)

    def get_bt_search_category(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, param)

    def clean_bt_search(self, taskid: Optional[str | list[str]] = None) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'clean', 'taskid': taskid}

        if taskid is None:
            return 'Enter a valid taskid, you can choose one of ' + str(self._bt_search_id_list)
        elif type(taskid) is list:
            param['taskid'] = ','.join(taskid)
            for item in taskid:
                self._bt_search_id_list.remove(item)
        else:
            self._bt_search_id_list.remove(taskid)

        return self.request_data(api_name, api_path, param)

    def get_bt_module(self) -> dict[str, object] | str:
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'getModule'}

        return self.request_data(api_name, api_path, param)
