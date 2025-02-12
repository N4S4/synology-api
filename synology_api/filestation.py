from __future__ import annotations
from typing import Optional, Any
import os
import io
import time
from datetime import datetime

import requests
import tqdm
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import sys
from urllib import parse
from treelib import Tree
from . import base_api


class FileStation(base_api.BaseApi):

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
                 interactive_output: bool = True
                 ) -> None:

        super(FileStation, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                          dsm_version, debug, otp_code, device_id, device_name, 'FileStation')

        self._dir_taskid: str = ''
        self._dir_taskid_list: list[str] = []
        self._md5_calc_taskid: str = ''
        self._md5_calc_taskid_list: list[str] = []
        self._search_taskid: str = ''
        self._search_taskid_list: list[str] = []
        self._copy_move_taskid: str = ''
        self._copy_move_taskid_list: list[str] = []
        self._delete_taskid: str = ''
        self._delete_taskid_list: list[str] = []
        self._extract_taskid: str = ''
        self._extract_taskid_list: list[str] = []
        self._compress_taskid: str = ''
        self._compress_taskid_list: list[str] = []

        self.session.get_api_list('FileStation')

        self.file_station_list: Any = self.session.app_api_list

        self.interactive_output: bool = interactive_output

    def get_info(self) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_list_share(self,
                       additional: Optional[str | list[str]] = None,
                       offset: Optional[int] = None,
                       limit: Optional[int] = None,
                       sort_by: Optional[str] = None,
                       sort_direction: Optional[str] = None,
                       onlywritable: bool = False
                       ) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list_share'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def get_file_list(self,
                      folder_path: Optional[str] = None,
                      offset: Optional[int] = None,
                      limit: Optional[int] = None,
                      sort_by: Optional[str] = None,
                      sort_direction: Optional[str] = None,
                      pattern: Optional[str] = None,
                      filetype: Optional[str] = None,
                      goto_path: Optional[str] = None,
                      additional: Optional[str | list[str]] = None) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if folder_path is None:
            return 'Enter a valid folder_path'

        if filetype is not None:
            req_param['filetype'] = str(req_param['filetype']).lower()

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def get_file_info(self,
                      path: Optional[str] = None,
                      additional: Optional[str | list[str]] = None
                      ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.List'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = str(additional).replace("'", '"')

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    # TODO  all working if specify extension check if correct [pattern, extension]
    #  it works if you put extension='...'

    def search_start(self,
                     folder_path: Optional[str] = None,
                     recursive: Optional[bool] = None,
                     pattern: Optional[str] = None,
                     extension: Optional[str] = None,
                     filetype: Optional[str] = None,
                     size_from: Optional[int] = None,
                     size_to: Optional[int] = None,
                     mtime_from: Optional[str | int] = None,
                     mtime_to: Optional[str | int] = None,
                     crtime_from: Optional[str | int] = None,
                     crtime_to: Optional[str | int] = None,
                     atime_from: Optional[str | int] = None,
                     atime_to: Optional[str | int] = None,
                     owner: Optional[str] = None,
                     group: Optional[str] = None
                     ) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start', 'folder_path': ''}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param'] and 'time' not in key:
                if val is not None:
                    req_param[str(key)] = val
            if 'time' in key:
                if val is not None:
                    try:
                        date = time.strptime(val, "%Y-%m-%d %H:%M:%S")
                        timestamp = time.mktime(date)
                        req_param[key] = '"' + str(timestamp) + '"'
                    except ValueError:
                        try:
                            datetime.fromtimestamp(int(val)).strftime('%Y-%m-%d %H:%M:%S')
                            req_param[key] = '"' + val + '"'
                        except ValueError:
                            return 'Enter the correct Date Time format "YYY-MM-DD HH:MM:SS" or Unix timestamp'

        if folder_path is None:
            return 'Enter a valid folder_path'
        else:
            req_param['folder_path'] = '"' + folder_path + '"'

        if filetype is not None:
            req_param['filetype'] = '"' + filetype + '"'

        response = self.request_data(api_name, api_path, req_param)

        taskid = response['data']['taskid']
        self._search_taskid = '"{}"'.format(taskid)
        self._search_taskid_list.append('"' + response['data']['taskid'] + '"')

        message = ('You can now check the status of request with '
                   'get_search_list() , your id is: ' + self._search_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": taskid}

        return output

    def get_search_list(self,
                        task_id: str,
                        filetype: Optional[str] = None,
                        limit: Optional[int] = None,
                        sort_by: Optional[str] = None,
                        sort_direction: Optional[str] = None,
                        offset: Optional[int] = None,
                        additional: Optional[str | list[str]] = None
                        ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'taskid': ''}

        if task_id is None:
            return 'Enter a correct taskid, choose one of the following: ' + str(self._search_taskid_list)
        else:
            req_param['taskid'] = task_id

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional', 'task_id']:
                if val is not None:
                    req_param[str(key)] = val

        if filetype is not None:
            req_param['filetype'] = str(filetype).lower()

        if additional is None:
            additional = ['size', 'owner', 'time']

        if type(additional) is list:
            additional = '","'.join(additional)

        req_param['additional'] = '["' + additional + '"]'

        return self.request_data(api_name, api_path, req_param)

    def stop_search_task(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': self._search_taskid}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._search_taskid_list)

        self._search_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_all_search_task(self) -> str:
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': ''}

        assert len(self._search_taskid_list), 'Task list is empty' + str(self._search_taskid_list)

        for task_id in self._search_taskid_list:
            req_param['taskid'] = task_id
            self.request_data(api_name, api_path, req_param)

        self._search_taskid_list = []

        return 'All task are stopped'

    def get_mount_point_list(self,
                             mount_type: Optional[str] = None,
                             offset: Optional[int] = None,
                             limit: Optional[int] = None,
                             sort_by: Optional[str] = None,
                             sort_direction: Optional[str] = None,
                             additional: Optional[str | list[str]] = None
                             ) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.VirtualFolder'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        if mount_type is not None:
            req_param['type'] = mount_type

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional', 'mount_type']:
                if val is not None:
                    req_param[str(key)] = val

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def get_favorite_list(self,
                          offset: Optional[int] = None,
                          limit: Optional[int] = None,
                          sort_by: Optional[str] = None,
                          status_filter: Optional[str] = None,
                          additional: Optional[str | list[str]] = None
                          ) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'additional']:
                if val is not None:
                    req_param[str(key)] = val

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def add_a_favorite(self,
                       path: str,
                       name: Optional[str] = None,
                       index: Optional[int] = None
                       ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'add'}

        if path is None:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def delete_a_favorite(self, path: Optional[str] = None) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_broken_favorite(self) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_broken'}

        return self.request_data(api_name, api_path, req_param)

    def edit_favorite_name(self, path: str, new_name: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if path is None:
            return 'Enter a valid path'
        else:
            req_param['path'] = path

        if new_name is None:
            return 'Enter a valid new_name'
        else:
            req_param['new_name'] = new_name

        return self.request_data(api_name, api_path, req_param)

    def replace_all_favorite(self, path: str | list[str], name: str | list[str]):
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if type(path) is list:
            path = ','.join(path)
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        if type(name) is list:
            name = ','.join(name)
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = name
        else:
            return 'Enter a valid name'

        return self.request_data(api_name, api_path, req_param)

    def start_dir_size_calc(self, path: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']

        response_id = '"{}"'.format(taskid)
        self._dir_taskid = response_id
        self._dir_taskid_list.append(response_id)

        message = ('You can now check the status of request '
                   'with get_dir_status() , your id is: '
                   + response_id)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": taskid}

        return output

    def stop_dir_size_calc(self, taskid: str) -> str:
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': taskid}

        if taskid is None:
            return 'Enter a valid taskid choose between: ' + str(self._dir_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        self.request_data(api_name, api_path, req_param)
        self._dir_taskid_list.remove('"' + taskid + '"')

        return 'The task has been stopped'

    def get_dir_status(self, taskid: Optional[str] = None) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status', 'taskid': taskid}

        if taskid is None and self._dir_taskid != '':
            return 'Choose a taskid from this list: ' + str(self._dir_taskid)

        return self.request_data(api_name, api_path, req_param)

    def start_md5_calc(self, file_path: str) -> str | dict[str, object]:
        api_name = 'SYNO.FileStation.MD5'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if file_path is None:
            return 'Enter a correct file_path'
        else:
            req_param['file_path'] = file_path

        self._md5_calc_taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']
        self._md5_calc_taskid_list.append(self._md5_calc_taskid)

        message = ('You can now check the status of request with '
                   'get_md5_status() , your id is: ' + self._md5_calc_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._md5_calc_taskid}

        return output

    def get_md5_status(self, taskid: Optional[str] = None) -> str | dict[str, object]:
        api_name = 'SYNO.FileStation.MD5'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None and self._md5_calc_taskid != '':
            req_param['taskid'] = '"{taskid}"'.format(taskid=self._md5_calc_taskid)
        elif taskid is not None:
            req_param['taskid'] = '"{taskid}"'.format(taskid=taskid)
        else:
            return 'Did you run start_md5_calc() first? No task id found! ' + str(self._md5_calc_taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_md5_calc(self, taskid: str) -> str:
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': taskid}

        if taskid is None:
            return 'Enter a valid taskid choose between: ' + str(self._md5_calc_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        self.request_data(api_name, api_path, req_param)
        self._md5_calc_taskid_list.remove(taskid)

        return 'The task has been stopped'

    def check_permissions(self,
                          path: str,
                          filename: str,
                          overwrite: Optional[bool] = None,
                          create_only: Optional[bool] = None
                          ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.CheckPermission'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'write'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if path is None:
            return 'Enter a valid path'

        if filename is None:
            return 'Enter a valid name'

        return self.request_data(api_name, api_path, req_param)

    def upload_file(self,
                    dest_path: str,
                    file_path: str,
                    create_parents: bool = True,
                    overwrite: bool = True,
                    verify: bool = False,
                    progress_bar: bool = True
                    ) -> str | tuple[int, dict[str, object]]:
        api_name = 'SYNO.FileStation.Upload'
        info = self.file_station_list[api_name]
        api_path = info['path']
        filename = os.path.basename(file_path)

        session = requests.session()

        with open(file_path, 'rb') as payload:
            url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=upload&_sid=%s' % (
                api_name, info['minVersion'], self._sid)

            encoder = MultipartEncoder({
                'path': dest_path,
                'create_parents': str(create_parents).lower(),
                'overwrite': str(overwrite).lower(),
                'files': (filename, payload, 'application/octet-stream')
            })

            if progress_bar:
                bar = tqdm.tqdm(desc='Upload Progress',
                                total=encoder.len,
                                dynamic_ncols=True,
                                unit='B',
                                unit_scale=True,
                                unit_divisor=1024
                                )

                monitor = MultipartEncoderMonitor(encoder, lambda monitor: bar.update(monitor.bytes_read - bar.n))

                r = session.post(
                    url,
                    data=monitor,
                    verify=verify,
                    headers={"X-SYNO-TOKEN": self.session._syno_token, 'Content-Type': monitor.content_type}
                )

            else:
                r = session.post(
                    url,
                    data=encoder,
                    verify=verify,
                    headers={"X-SYNO-TOKEN": self.session._syno_token, 'Content-Type': encoder.content_type}
                )

        session.close()
        if r.status_code != 200 or not r.json()['success']:
            return r.status_code, r.json()

        return r.json()

    def get_shared_link_info(self, link_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def get_shared_link_list(self,
                             offset: Optional[int] = None,
                             limit: Optional[int] = None,
                             sort_by: Optional[str] = None,
                             sort_direction: Optional[str] = None,
                             force_clean: Optional[bool] = None
                             ) -> dict[str, object] | str:

        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_sharing_link(self,
                            path: str,
                            password: Optional[str] = None,
                            date_expired: Optional[str | int] = None,
                            date_available: Optional[str | int] = None,
                            expire_times: int = 0
                            ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create'}

        if date_expired:
            if str(date_expired)[0] != '"':
                date_expired = '"' + str(date_expired) + '"'
        if date_available:
            if str(date_available)[0] != '"':
                date_available = '"' + str(date_available) + '"'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if path is None:
            return 'Enter a valid path'

        return self.request_data(api_name, api_path, req_param)

    def delete_shared_link(self, link_id: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def clear_invalid_shared_link(self) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_invalid'}

        return self.request_data(api_name, api_path, req_param)

    def edit_shared_link(self,
                         link_id: str,
                         password: Optional[str] = None,
                         date_expired: Optional[str | int] = None,
                         date_available: Optional[str | int] = None,
                         expire_times: int = 0
                         ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if date_expired:
            if str(date_expired)[0] != '"':
                date_expired = '"' + str(date_expired) + '"'
        if date_available:
            if str(date_available)[0] != '"':
                date_available = '"' + str(date_available) + '"'

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_folder(self,
                      folder_path: str | list[str],
                      name: str | list[str],
                      force_parent: Optional[bool] = None,
                      additional: Optional[str | list[str]] = None
                      ) -> str | dict[str, object]:
        api_name = 'SYNO.FileStation.CreateFolder'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'folder_path', 'additional', 'name']:
                if val is not None:
                    req_param[str(key)] = val

        if type(folder_path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in folder_path]
            folder_path = new_path
            folder_path = '[' + ','.join(folder_path) + ']'
            req_param['folder_path'] = folder_path
        elif folder_path is not None:
            req_param['folder_path'] = folder_path
        else:
            return 'Enter a valid path'

        if type(name) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in name]
            name = new_path
            name = '[' + ','.join(name) + ']'
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = '"' + name + '"'
        else:
            return 'Enter a valid path'

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    def rename_folder(self,
                      path: str | list[str],
                      name: str | list[str],
                      additional: Optional[str | list[str]] = None,
                      search_taskid: Optional[str] = None
                      ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Rename'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'rename'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid folder path (folder path only ex. "/home/Drive/Downloads")'

        if type(name) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in name]
            name = new_path
            name = '[' + ','.join(name) + ']'
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = name
        else:
            return 'Enter a valid new folder name (new folder name only ex. "New Folder")'

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        if search_taskid is not None:
            req_param['search_taskid'] = search_taskid

        return self.request_data(api_name, api_path, req_param)

    def start_copy_move(self,
                        path: str | list[str],
                        dest_folder_path: str | list[str],
                        overwrite: Optional[bool] = None,
                        remove_src: Optional[bool] = None,
                        accurate_progress: Optional[bool] = None,
                        search_taskid: Optional[str] = None
                        ) -> str | dict[str, object]:
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        if type(dest_folder_path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in dest_folder_path]
            dest_folder_path = new_path
            dest_folder_path = '[' + ','.join(dest_folder_path) + ']'
            req_param['name'] = dest_folder_path
        elif dest_folder_path is not None:
            req_param['dest_folder_path'] = dest_folder_path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'additional',
                           'dest_folder_path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        self._copy_move_taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']
        self._dir_taskid_list.append(self._copy_move_taskid)

        message = ('You can now check the status of request with '
                   'get_copy_move_status() , your id is: '
                   + self._copy_move_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._copy_move_taskid}

        return output

    def get_copy_move_status(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid choose between ' + str(self._copy_move_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        return self.request_data(api_name, api_path, req_param)

    def stop_copy_move_task(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid choose between ' + str(self._copy_move_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._copy_move_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def start_delete_task(self,
                          path: str | list[str],
                          accurate_progress: Optional[bool] = None,
                          recursive: Optional[bool] = None,
                          search_taskid: Optional[str] = None
                          ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        self._delete_taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']
        self._delete_taskid_list.append(self._delete_taskid)

        message = ('You can now check the status of request with '
                   'get_delete_status() , task id is: '
                   + self._delete_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._delete_taskid}

        return output

    def get_delete_status(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._delete_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_delete_task(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._delete_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._delete_taskid_list.remove('"' + taskid + '"')

        return self.request_data(api_name, api_path, req_param)

    def delete_blocking_function(self,
                                 path: str,
                                 recursive: Optional[bool] = None,
                                 search_taskid: Optional[str] = None) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        'This function will stop your script until done! Do not interrupt '

        return self.request_data(api_name, api_path, req_param)

    def start_extract_task(self,
                           file_path: str,
                           dest_folder_path: str,
                           overwrite: Optional[bool] = None,
                           keep_dir: Optional[bool] = None,
                           create_subfolder: Optional[bool] = None,
                           codepage: Optional[str] = None,
                           password: Optional[str] = None,
                           item_id: Optional[str] = None
                           ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start', 'file_path': file_path,
                     'dest_folder_path': dest_folder_path}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if file_path is None:
            return 'Enter a valid file_path'

        if dest_folder_path is None:
            return 'Enter a valid dest_folder_path'

        self._extract_taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']
        self._extract_taskid_list.append(self._extract_taskid)

        message = ('You can now check the status of request with '
                   'get_extract_status() , your id is: '
                   + self._extract_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._extract_taskid}

        return output

    def get_extract_status(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._extract_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_extract_task(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._extract_taskid_list)
        else:
            req_param['taskid'] = taskid

        self._extract_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def get_file_list_of_archive(self,
                                 file_path: str,
                                 offset: Optional[int] = None,
                                 limit: Optional[int] = None,
                                 sort_by: Optional[str] = None,
                                 sort_direction: Optional[str] = None,
                                 codepage: Optional[str] = None,
                                 password: Optional[str] = None,
                                 item_id: Optional[str] = None
                                 ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if file_path is None:
            return 'Enter a valid file_path'

        return self.request_data(api_name, api_path, req_param)

    def start_file_compression(self,
                               path: str | list[str],
                               dest_file_path: str,
                               level: Optional[int] = None,
                               mode: Optional[str] = None,
                               compress_format: Optional[str] = None,
                               password: Optional[str] = None
                               ) -> dict[str, object] | str | tuple[str]:
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            req_param['path'] = path
        elif path is not None:
            req_param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'compress_format', '_password', '_api_path',
                           'req_param', 'path', 'new_path']:
                if val is not None:
                    req_param[str(key)] = val

        if dest_file_path is None:
            return 'Enter a valid dest_file_path'

        if compress_format is not None:
            req_param['format'] = compress_format

        if password is not None:
            req_param['_password'] = password

        self._compress_taskid = self.request_data(api_name, api_path, req_param)['data']['taskid']

        message = ('You can now check the status of request with '
                   'get_compress_status() , your id is: '
                   + self._compress_taskid)
        if self.interactive_output:
            output = message
        else:
            output = {"message": message, "taskid": self._compress_taskid}

        return output

    def get_compress_status(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_compress_task(self, taskid: str) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_list_of_all_background_task(self,
                                        offset: Optional[int] = None,
                                        limit: Optional[int] = None,
                                        sort_by: Optional[str] = None,
                                        sort_direction: Optional[str] = None,
                                        api_filter: Optional[str] = None
                                        ) -> dict[str, object] | str:
        api_name = 'SYNO.FileStation.BackgroundTask'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if type(api_filter) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in api_filter]
            api_filter = new_path
            api_filter = '[' + ','.join(api_filter) + ']'
            req_param['api_filter'] = api_filter

        return self.request_data(api_name, api_path, req_param)

    def get_file(self,
                 path: str,
                 mode: str,
                 dest_path: str = ".",
                 chunk_size: int = 8192,
                 verify: bool = False
                 ) -> Optional[str]:

        api_name = 'SYNO.FileStation.Download'
        info = self.file_station_list[api_name]
        api_path = info['path']

        if path is None:
            return 'Enter a valid path'

        session = requests.session()

        url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=download&path=%s&mode=%s&_sid=%s' % (
            api_name, info['maxVersion'], parse.quote_plus(path), mode, self._sid)

        if mode is None:
            return 'Enter a valid mode (open / download)'

        if mode == r'open':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:  # filter out keep-alive new chunks
                        sys.stdout.buffer.write(chunk)

        if mode == r'download':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                if not os.path.isdir(dest_path):
                    os.makedirs(dest_path)
                with open(dest_path + "/" + os.path.basename(path), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)

        if mode == r'serve':
            with session.get(url, stream=True, verify=verify, headers={"X-SYNO-TOKEN": self.session._syno_token}) as r:
                r.raise_for_status()
                return io.BytesIO(r.content)
            
    def generate_file_tree(self, folder_path: str, tree: Tree) -> None:
        """Generate the file tree based on the folder path you give, you need to create the root node before call this function
        
            Parameters
            ----------
            folder_path : str
                Folder path to generate file tree
            tree : Tree
                Instance of the Tree of lib "Treelib"
        
        """
        data: dict = self.get_file_list(
            folder_path=folder_path
        ).get("data")

        files = data.get("files")
        file: dict
        for file in files:
            file_name: str = file.get("name")
            file_path: str = file.get("path")
            if file.get("isdir"):
                
                tree.create_node(file_name, file_path, parent=folder_path)
                self.generate_file_tree(file_path, tree)
            else:
                tree.create_node(file_name, file_path, parent=folder_path)
    

# TODO SYNO.FileStation.Thumb to be done
