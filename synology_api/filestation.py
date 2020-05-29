import os
import time
from datetime import datetime

import requests
import sys
from urllib import parse

from . import auth as syn


class FileStation:

    def __init__(self, ip_address, port, username, password, secure=False):

        self.session = syn.Authentication(ip_address, port, username, password, secure)

        self._dir_taskid = ''
        self._dir_taskid_list = []
        self._md5_calc_taskid = ''
        self._md5_calc_taskid_list = []
        self._search_taskid = ''
        self._search_taskid_list = []
        self._copy_move_taskid = ''
        self._copy_move_taskid_list = []
        self._delete_taskid = ''
        self._delete_taskid_list = []
        self._extract_taskid = ''
        self._extract_taskid_list = []
        self._compress_taskid = ''
        self._compress_taskid_list = []
        self.request_data = self.session.request_data

        self.session.login('FileStation')
        self.session.get_api_list('FileStation')

        self.file_station_list = self.session.app_api_list
        self._sid = self.session.sid
        self.base_url = self.session.base_url

        print('You are now logged in!')

    def logout(self):
        self.session.logout('FileStation')

    def get_info(self):
        api_name = 'SYNO.FileStation.Info'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', '_sid': self._sid}

        return self.request_data(api_name, api_path, req_param)

    def get_list_share(self, additional=None, offset=None, limit=None, sort_by=None,
                       sort_direction=None, onlywritable=False):

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

    def get_file_list(self, folder_path=None, offset=None, limit=None, sort_by=None,
                      sort_direction=None, pattern=None, filetype=None, goto_path=None, additional=None):

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

    def get_file_info(self, path=None, additional=None):
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
            additional = ','.join(additional)

        req_param['additional'] = additional

        return self.request_data(api_name, api_path, req_param)

    # TODO  all working if specify extension check if correct [pattern, extension]
    #  it works if you put extension='...'

    def search_start(self, folder_path=None, recursive=None, pattern=None, extension=None, filetype=None,
                     size_from=None, size_to=None, mtime_from=None, mtime_to=None, crtime_from=None, crtime_to=None,
                     atime_from=None, atime_to=None, owner=None, group=None):

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

        self._search_taskid = '"' + response['data']['taskid'] + '"'
        self._search_taskid_list.append('"' + response['data']['taskid'] + '"')

        return 'You can now check the status of request with get_search_list() , your id is: ' + self._search_taskid

    def get_search_list(self, task_id=None, filetype=None, limit=None, sort_by=None, sort_direction=None,
                        offset=None, additional=None):
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

    def stop_search_task(self, taskid=None):
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': self._search_taskid}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._search_taskid_list)

        self._search_taskid_list.remove(taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_all_search_task(self):
        api_name = 'SYNO.FileStation.Search'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop', 'taskid': ''}

        assert len(self._search_taskid_list) is not 0, 'Task list is empty' + str(self._search_taskid_list)

        for task_id in self._search_taskid_list:
            req_param['taskid'] = task_id
            self.request_data(api_name, api_path, req_param)

        self._search_taskid_list = []

        return 'All task are stopped'

    def get_mount_point_list(self, mount_type=None, offset=None, limit=None, sort_by=None,
                             sort_direction=None, additional=None):

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

    def get_favorite_list(self, offset=None, limit=None, sort_by=None,
                          status_filter=None, additional=None):

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

    def add_a_favorite(self, path=None, name=None, index=None):
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

    def delete_a_favorite(self, path=None):
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def clear_broken_favorite(self):
        api_name = 'SYNO.FileStation.Favorite'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_broken'}

        return self.request_data(api_name, api_path, req_param)

    def edit_favorite_name(self, path=None, new_name=None):
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

    def replace_all_favorite(self, path=None, name=None):
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

    def start_dir_size_calc(self, path=None):
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

        response_id = '"' + self.request_data(api_name, api_path, req_param)['data']['taskid'] + '"'

        self._dir_taskid = response_id
        self._dir_taskid_list.append(response_id)

        return 'You can now check the status of request with get_dir_status() , your id is: ' + self._dir_taskid

    def stop_dir_size_calc(self, taskid=None):
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

    def get_dir_status(self, taskid=None):
        api_name = 'SYNO.FileStation.DirSize'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status', 'taskid': taskid}

        if taskid is None and self._dir_taskid is not '':
            req_param['taskid'] = self._dir_taskid
        else:
            return 'Did you run start_dir_size_calc() first? No task id found!' + str(self._dir_taskid_list)

        return self.request_data(api_name, api_path, req_param)

    def start_md5_calc(self, file_path=None):
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

        return 'You can now check the status of request with get_md5_status() , your id is: ' + self._md5_calc_taskid

    def get_md5_status(self, taskid=None):
        api_name = 'SYNO.FileStation.MD5'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None and self._md5_calc_taskid is not '':
            req_param['taskid'] = '"{taskid}"'.format(taskid=self._md5_calc_taskid)
        elif taskid is not None:
            req_param['taskid'] = '"{taskid}"'.format(taskid=taskid)
        else:
            return 'Did you run start_md5_calc() first? No task id found! ' + str(self._md5_calc_taskid)

        return self.request_data(api_name, api_path, req_param)

    def stop_md5_calc(self, taskid=None):
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

    def check_permissions(self, path=None, filename=None, overwrite=None, create_only=None):
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

    def upload_file(self, dest_path, file_path, create_parents=True, overwrite=True):
        api_name = 'SYNO.FileStation.Upload'
        info = self.file_station_list[api_name]
        api_path = info['path']
        filename = os.path.basename(file_path)

        session = requests.session()

        with open(file_path, 'rb') as payload:
            url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=upload&_sid=%s' % (
                api_name, info['minVersion'], self._sid)

            args = {
                'path': dest_path,
                'create_parents': create_parents,
                'overwrite': overwrite,
            }

            files = {'file': (filename, payload, 'application/octet-stream')}

            r = session.post(url, data=args, files=files)

            if r.status_code is 200 and r.json()['success']:
                return 'Upload Complete'
            else:
                return r.status_code, r.json()

    def get_shared_link_info(self, link_id=None):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def get_shared_link_list(self, offset=None, limit=None, sort_by=None,
                             sort_direction=None, force_clean=None):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_sharing_link(self, path=None, password=None, date_expired=None,
                            date_available=None):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        if path is None:
            return 'Enter a valid path'

        return self.request_data(api_name, api_path, req_param)

    def delete_shared_link(self, link_id=None):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'delete'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        return self.request_data(api_name, api_path, req_param)

    def clear_invalid_shared_link(self):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'clear_invalid'}

        return self.request_data(api_name, api_path, req_param)

    def edit_shared_link(self, link_id=None, password=None, date_expired=None,
                         date_available=None):
        api_name = 'SYNO.FileStation.Sharing'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'edit'}

        if link_id is None:
            return 'Enter a valid id'
        else:
            req_param['id'] = link_id

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def create_folder(self, folder_path=None, name=None, force_parent=None, additional=None):
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

    def rename_folder(self, path=None, name=None, additional=None, search_taskid=None):
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
            return 'Enter a valid path'

        if type(name) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in name]
            name = new_path
            name = '[' + ','.join(name) + ']'
            req_param['name'] = name
        elif name is not None:
            req_param['name'] = name
        else:
            return 'Enter a valid path'

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        req_param['additional'] = additional

        if search_taskid is not None:
            req_param['search_taskid'] = search_taskid

        return self.request_data(api_name, api_path, req_param)

    def start_copy_move(self, path=None, dest_folder_path=None, overwrite=None, remove_src=None,
                        accurate_progress=None, search_taskid=None):
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

        return 'You can now check the status of request with get_copy_move_status() , ' \
               'your id is: ' + self._copy_move_taskid

    def get_copy_move_status(self, taskid=None):
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid choose between ' + str(self._copy_move_taskid_list)
        else:
            req_param['taskid'] = '"' + taskid + '"'

        return self.request_data(api_name, api_path, req_param)

    def stop_copy_move_task(self, taskid=None):
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

    def start_delete_task(self, path=None, accurate_progress=None, recursive=None, search_taskid=None):
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

        return 'You can now check the status of request with get_delete_status() , ' \
               'task id is: ' + self._delete_taskid

    def get_delete_status(self, taskid=None):
        api_name = 'SYNO.FileStation.Delete'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._delete_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_delete_task(self, taskid=None):
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

    def delete_blocking_function(self, path=None, recursive=None, search_taskid=None):
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

    def start_extract_task(self, file_path=None, dest_folder_path=None, overwrite=None, keep_dir=None,
                           create_subfolder=None, codepage=None, password=None, item_id=None):
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

        return 'You can now check the status of request with get_extract_status() , ' \
               'your id is: ' + self._extract_taskid

    def get_extract_status(self, taskid=None):
        api_name = 'SYNO.FileStation.Extract'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid, choose between ' + str(self._extract_taskid_list)
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_extract_task(self, taskid=None):
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

    def get_file_list_of_archive(self, file_path=None, offset=None, limit=None, sort_by=None,
                                 sort_direction=None, codepage=None, password=None, item_id=None):
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

    def start_file_compression(self, path=None, dest_file_path=None, level=None, mode=None,
                               compress_format=None, password=None):
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

        return 'You can now check the status of request with get_compress_status() , ' \
               'your id is: ' + self._compress_taskid

    def get_compress_status(self, taskid=None):
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def stop_compress_task(self, taskid=None):
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            req_param['taskid'] = taskid

        return self.request_data(api_name, api_path, req_param)

    def get_list_of_all_background_task(self, offset=None, limit=None, sort_by=None,
                                        sort_direction=None, api_filter=None):
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

    def get_file(self, path=None, mode=None):
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
            with session.get(url, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        sys.stdout.buffer.write(chunk)

        if mode == r'download':
            with session.get(url, stream=True) as r:
                r.raise_for_status()
                with open(os.path.basename(path), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)

# TODO SYNO.FileStation.Thumb to be done
