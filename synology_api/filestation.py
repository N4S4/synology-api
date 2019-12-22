import os
import time
from datetime import datetime

import requests
import sys
from urllib import parse

from .synology import Synology, api_call


class FileStation(Synology):

    @property
    def app(self):
        return 'FileStation'

    def __init__(self):

        super(FileStation, self).__init__()

        self._dir_taskid = ''
        self._dir_taskid_list = []
        self._md5_taskid = ''
        self._md5_taskid_list = []
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

        self.populate_api_dict(self.app())
        self.file_station_list = self.app_api_dict

    def logout(self, **kwargs):
        super().logout('FileStation')
    
    @api_call()
    def get_info(self):
        r = self.api_request('Info', 'getInfo')
        return r

    """
    method: get_list_share
    kwargs: additional,
            offset,
            limit,
            sort_by,
            sort_direction,
            only_writable
    """
    @api_call()
    def get_list_share(self, **kwargs):
        param = kwargs

        if 'additional' not in param.keys():
            param['additional'] = "real_path,size,owner,time"

        if type(param['additional']) is list:
            additional = kwargs.get('additional')
            param['additional'] = ','.join(additional)

        return self.api_request('List', 'list_share', param)

    """
    method: get_file_list
    args: folder_path
    kwargs: offset,
            limit,
            sort_by,
            sort_direction,
            pattern,
            filetype,
            goto_path,
            additional 
    """
    @api_call
    def get_file_list(self, folder_path, **kwargs): 
        
        param = kwargs

        param_keys = param.keys()

        if 'filetype' in param_keys:
            param['filetype'] = str(param['filetype']).lower()

        if 'additional' not in param_keys:
            param['additional'] = "real_path,size,owner,time"

        if type(param['additional']) is list:
            param['additional'] = ','.join(param['additional'])

        return self.api_request('List', 'list', param)

    @api_call
    def get_file_info(self, path=None, additional=None):
        param = {}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            param['path'] = path
        elif path is not None:
            param['path'] = path

        if additional is None:
            additional = ['real_path', 'size', 'owner', 'time']

        if type(additional) is list:
            additional = ','.join(additional)

        param['additional'] = additional

        return self.api_request('List', 'getinfo', param)

    # TODO  all working if specify extension check if correct [pattern, extension]
    #  it works if you put extension='...'
    @api_call
    def _search_start(self, folder_path, **kwargs):
            param = kwargs

            if 'time' in param.keys():
                t = param['time']
                is_str = isinstance(t, str)
                is_int = isinstance(t, int)

                if not is_str and is_int:
                    raise ValueError(
                            "Timestamp must be string or Unix timestamp, type is {t}.".format(
                                t=type(param['time'])))
                elif is_int and not is_str:
                    val = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
                    param['time'] = val
                else: #is_str is True, is_int might be True or False 
                    date = time.strptime(t, "%Y-%m-%d %H:%M:%S")
                    timestamp = time.mktime(date)
                    param['time'] = timestamp

            param['folder_path'] = '"{p}"'.format(p=param['folder_path'])

            if 'filetype' in param.keys():
                param['filetype'] = '"{f}"'.format(f=param['filetype'])

            return self.api_request('Search', 'start', param)

    """
    method: search_start
    args: folder_path
    kwargs: recursive,
            pattern,
            extension,
            filetype,
            size_from,
            site_to,
            mtime_from,
            mtime_to,
            crtime_from,
            crtime_to,
            atime_from,
            atime_to,
            owner,
            group
    """
    def search_start(self, folder_path, **kwargs):
        response = self._search_start(folder_path, **kwargs)

        if response['success']:
            self._search_taskid = response['data']['taskid']
            self._search_taskid_list.append(response['data']['taskid'])
        else:
            raise self.SynologyError(
                    "Could not start search task.\nResponse: {r}".format(
                        r=response))

        return response

    """
    method: get_search_list
    args: task_id
    kwargs: filetype,
            limit,
            sort_by,
            sort_direction,
            offset,
            additional
    """
    @api_call
    def get_search_list(self, task_id, **kwargs):
        param = kwargs
        param['taskid'] = task_id

        if 'filetype' in param.keys():
            param['filetype'] = param['filetype']

        if 'additional' not in param.keys():
            param['additional'] = ['size', 'owner', 'time']

        if type(param['additional']) is list:
            param['additional'] = str(param['additional'])

        return self.api_request('Search', 'list', param)
    
    @api_call
    def _stop_search_task(self, taskid):
        param = {}

        if taskid is None:
            if self._search_taskid is None:
                raise self.SynologyError(
                    "Tried to stop search tasks but none exist.")
            else:
                taskid = self._search_taskid

        param['taskid'] = taskid

        return self.api_request('Search', 'stop', param)

    def stop_search_task(self, taskid=None):
        response = self._stop_search_task(taskid)

        if not response['success']:
            raise self.SynologyError(
                "Could not stop search jobs. Response: {r}".format(r=response))

        self._search_taskid_list.remove(taskid)
        self._search_taskid = self._search_taskid_list[-1]

        return response 
    
    """
    method: stop_all_search_task
    args: log
    Argument 'log' should be an object with a method 'error', such as the
    logger from the standard logging library.
    Two values are returned: a list of the tasks which were not stopped
    (or an empty list), and the response of the first task that couldn't
    be stopped (or None if all were successfully stopped).
    """ 
    def stop_all_search_task(self, log=None):
        for task in self._search_taskid_list:
            try:
                response = self.stop_search_task(task)
            except self.SynologyError as err:
                if log is not None:
                    try:
                        log.error(str(err))
                    except AttributeError as err:
                        pass
                return self._search_taskid_list, response
        return self._search_taskid_list, None
    
    """
    method: get_mount_point_list
    args:
    kwargs: type,
            offset,
            limit,
            sort_by
            sort_direction,
            additional
    """
    @api_call
    def get_mount_point_list(self, **kwargs):
        param = kwargs

        if 'additional' not in param.keys():
            param['additional'] = ['real_path', 'size', 'owner', 'time']

        if type(param['additional']) is list:
            param['additional'] = str(param['additional'])

        return self.api_request('VirtualFolder', 'list', param)
    
    """
    method: get_favorite_list
    args:
    kwargs: offset,
            limit,
            sort_by,
            status_filter,
            additional
    """ 
    @api_call
    def get_favorite_list(self, **kwargs):
        param = kwargs

        if 'additional' not in param.keys():
            param['additional'] = ['real_path', 'size', 'owner', 'time']

        if type(param['additional']) is list:
            param['additional'] = str(param['additional'])

        return self.api_request('Favorite', 'list', param)
    
    @api_call
    def add_a_favorite(self, path, name=None, index=None):
        param = {'path': path}
        if name is not None:
            param['name'] = name
        if param['index'] is not None:
            param['index'] = index

        return self.api_request('Favorite', 'add', param)
    
    @api_call
    def delete_a_favorite(self, path):
        return self.api_request('Favorite', 'delete', {'path': path})
    
    @api_call
    def clear_broken_favorite(self):
        return self.api_request(self.app(), 'Favorite', 'clear_broken')
    
    @api_call
    def edit_favorite_name(self, path, new_name):
        return self.api_request('Favorite', 'edit',
                {'path': path, 'new_name': new_name})
    
    @api_call
    def replace_all_favorite(self, path, name):
        if type(path) is list:
            path = ",".join(path)

        if type(name) is list:
            path = ",".join(name)

        return self.api_request('Favorite', 'edit',
                {'path': path, 'name': name})
    
    @api_call
    def _start_dir_size_calc(self, path):
        if type(path) is list:
            path = str(path)

        return self.api_request('DirSize', 'start', path)

    def start_dir_size_calc(self, path):
        response = self._start_dir_size_calc(path)
        self._dir_taskid = response['data']['taskid']
        self._dir_taskid_list.append(self._dir_taskid)

        return response    
    
    @api_call
    def _stop_dir_size_calc(self, taskid):

        return self.api_request('DirName', 'stop',
                {'taskid': '"{t}"'.format(t=taskid)})

    def stop_dir_size_calc(self, taskid):
        response = self._stop_dir_size_calc(taskid)
        if not response['success']:
            raise self.SynologyError(
                    "Cannot stop task {t}.\nResponse: {r}".format(
                        t=taskid, r=response))
        self._dir_taskid_list.remove(taskid)
        if self._dir_taskid is taskid:
            self._dir_taskid = self._dir_taskid_list[-1]

        return response
    
    @api_call
    def get_dir_status(self, taskid=None):
            if taskid is None:
                if self._dir_taskid is None:
                    raise self.SynologyError("No DirSize tasks currently running.")
                else:
                    taskid = self._dir_taskid

            return self.api_request('DirSize', 'status',
                {'taskid': taskid})

    @api_call
    def _start_md5_calc(self, file_path):
        return self.api_request('MD5', 'start',
                {'file_path': file_path})

    def start_md5_calc(self, file_path):
        response = self._start_md5_calc(file_path)
        self._md5_taskid = response['data']['taskid']
        self._md5_taskid_list.append(self._md5_taskid)
        return response
    
    @api_call
    def get_md5_status(self, taskid=None):
        if taskid is None:
            if self._md5_taskid is not None:
                taskid = self._md5_taskid
            else:
                raise self.SynologyError("No MD5 tasks currently running.")

        return self.api_request('MD5', 'status',
                {'taskid': taskid})

    @api_call
    def _stop_md5_calc(self, taskid):
        self.api_request('MD5', 'stop',
                {'taskid': taskid})

    def stop_md5_calc(self, taskid):
        response = self._stop_md5_calc(taskid)
        if response['success']:
            self._md5_taskid_list.remove(taskid)
            if self._md5_taskid is taskid:
                self._md5_taskid = self._md5_taskid_list[-1]

        return response
    
    """
    method: check_permissions
    args: path, filename
    kwargs: overwrite, create_only
    """
    @api_call
    def check_permissions(self, path, filename, **kwargs):
        param = kwargs
        param['path'] = path
        param['filename'] = filename
        return self.api_request('CheckPermission', 'write', param)


    _url_ptrn = "{u}{p}?api={n}&version={m}&method=upload&_sid={s}"
    """
    method: upload_file
    args: dest_path, file_path, log, create_parets=True, overwrite=False
    FileStation.upload_file() works differently from other methods. Instead of
    sending a single requests.request(), it opens a requests.session() to
    upload the file found at 'file_path' on the client to 'dest_path' on the
    NAS. As such, it does not use the usual @api_call decorator.

    The 'log' argument is an object with an "error" method, such as the logger
    from Python's standard library "logging". This is used in case of an error
    during the file upload to make reporting on any errors easier. If any
    exceptions are caught, the method returns false. Note that it is on the 
    client to check for any errors regarding the file to be uploaded (such as
    anything covered by OSError).

    Note: I have not seen any other methods using a session yet, but if it's
    common enough it may be worthwhile to create another decorator similar to
    @api_call, such as @Synology.api_session.
    """
    def upload_file(self, dest_path, file_path, log,
            create_parents=True, overwrite=False):
        api_name = 'SYNO.FileStation.Upload'
        info = self.file_station_list[api_name]
        api_path = info['path']
        filename = os.path.basename(file_path)

        session = requests.session()
        try:
            with open(file_path, 'rb') as payload:
                url = self._url_ptrn.format(u=self.base_url, p=api_path,
                        n=api_name, m=info['minVersion'], s=self._sid)

                args = {
                    'path': dest_path,
                    'create_parents': create_parents,
                    'overwrite': overwrite,
                }

                file_info = {'file': (filename, payload,
                            'application/octet-stream')}

                r = session.post(url, data=args, files=file_info) 
                return r

        except ConnectionError as err:
            log.error("Could not connect to Synology.\nError: {e}".format(
                        e=str(err)))

        except requests.Timeout as err:
            log.error("Request timed out.\nError: {e}".format(e=str(err)))

        except requests.exceptions.RequestException as err:
            log.error("Session raised an exception.\nError: {e}".format(
                        e=str(err)))

        return False

    @api_call
    def get_shared_link_info(self, link_id):
        return self.api_request('Sharing', 'getinfo',
                {'id': link_id})
    
    """
    method: get_shared_link_list
    kwargs: offset,
            limit,
            sort_by,
            sort_direction,
            force_clean
    """
    @api_call
    def get_shared_link_list(self, **kwargs):
        return self.api_request('Sharing', 'list', kwargs)
    
    """
    method: create_sharing_link
    args: path
    kwargs: password,
            date_expired,
            date_available
    """ 
    @api_call
    def create_sharing_link(self, path, **kwargs):
        param = kwargs
        param['path'] = path
        return self.api_request('Sharing', 'create', param)

    @api_call
    def delete_shared_link(self, link_id):
        return self.api_request('Sharing', 'delete', {'id': link_id})
    
    @api_call
    def clear_invalid_shared_link(self):
        return self.api_request('Sharing', 'clear_invalid')
    
    """
    method: edit_shared_link
    args: link_id
    kwargs: password,
            date_expired,
            date_available
    """ 
    @api_call
    def edit_shared_link(self, link_id, **kwargs):
        param = kwargs
        param['id'] = link_id
        return self.api_request('Sharing', 'edit', param)
    
    """
    method: create_folder
    args: folder_path, name
    kwargs: force_parent, additional
    """    
    @api_call
    def create_folder(self, folder_path, name, **kwargs):
        param = kwargs

        if type(folder_path) is list:
            new_fp = []
            for path in folder_path:
                path = '"{p}"'.format(path)
                new_fp.append(path)
            folder_path = str(new_fp)
        param['folder_path'] = folder_path

        if type(name) is list:
            new_name = []
            for nm in name:
                nm = '"{n}"'.format(n=nm)
                new_name.append(nm) 
            name = str(new_name)
        param['name'] = name

        if 'additional' not in param.keys():
            param['additional'] = ['real_path', 'size', 'owner', 'time']

        if type(param['additional']) is list:
            param['additional'] = ','.join(param['additional'])

        return self.api_request('CreateFolder', 'create', param)

    """
    method: rename_folder
    args: path, name
    kwargs: additional, search_taskid
    """ 
    @api_call
    def rename_folder(self, path, name, **kwargs):
        param = kwargs

        if type(path) is list:
            new_path = []
            for np in path:
                np = '"{n}"'.format(n=np)
                new_path.append(np)
            path = str(new_path)
        param['path'] = path

        if type(name) is list:
            new_path = []
            for np in path:
                np = '"{n}"'.format(n=np)
                new_path.append(np)
            name = str(new_path)
        param['name'] = name

        if 'additional' not in param.keys():
            param['additional'] = ['real_path', 'size', 'owner', 'time']

        if type(param['additional']) is list:
            param['additional'] = ','.join(param['additional'])

        return self.api_request('Rename', 'rename', param)
    
    """
    method: start_copy_move
    args: path, dest_folder
    kwargs: overwite,
            remove_src,
            accurate_progress,
            search_taskid
    """
    @api_call
    def _start_copy_move(self, path, dest_folder, **kwargs):
        param = kwargs 

        if type(path) is list:
            path = str(path)
        param['path'] = path

        if type(dest_folder) is list:
            dest_folder = str(dest_folder)
        param['name'] = dest_folder

        return self.api_request('CopyMove', 'start', param)
        
    def start_copy_move(self, path, dest_folder, **kwargs): 
        response = self._start_copy_move(path, dest_folder, **kwargs)
        if response['success']:
            self._copy_move_taskid = response['data']['taskid']
            self._dir_taskid_list.append(self._copy_move_taskid)
        return response
    
    @api_call
    def get_copy_move_status(self, taskid):
        return self.api_request('CopyMove', 'status', {'taskid': taskid})
    
    @api_call
    def _stop_copy_move_task(self, taskid):
        return self.api_request('CopyMove', 'stop', taskid)

    def stop_copy_move_taks(self, taskid):
        response = self._stop_copy_move_task(taskid)
        
        if response['success']:
            self._copy_move_taskid_list.remove(taskid)
            if self._copy_move_taskid is taskid:
                self._copy_move_taskid = self._copy_move_taskid_list[-1]

        return response
   
    """
    method: start_delete_task
    args: path
    kwargs: accurate_progress,
            recursive,
            search_taskid
    """ 
    @api_call
    def _start_delete_task(self, path, **kwargs):
        param = kwargs

        if type(path) is list:
            path = str(path)
        param['path'] = path
        return self.api_request('Delete', 'start', param)
    
    def start_delete_task(self, path, **kwargs):
        response = self._start_delete_task(path, **kwargs)
        if response['success']:
            self._delete_taskid = response['data']['taskid']
            self._delete_taskid_list.append(self._delete_taskid)
        return response
    
    @api_call
    def get_delete_status(self, taskid):
        return self.api_request('Delete', 'status', {'taskid': taskid})
    
    @api_call
    def _stop_delete_task(self, taskid):
        return self.api_request('Delete', 'stop', {'taskid': taskid})
    
    def stop_delete_task(self, taskid):
        response = self._stop_delete_task(taskid)
        if response['success']:
            self._delete_taskid_list.remove(taskid)
            if self._delete_taskid is taskid:
                self._delete_taskid = self._delete_taskid_list[-1]
        return response 
    
    """
    method: delete_blocking_function
    args: path
    kwargs: recursive,
            search_taskid

    delete_blocking_function may appear to hang for a while. This is normal.
    TODO: possibly add async option?
    """
    @api_call
    def delete_blocking_function(self, path, **kwargs):
        param = kwargs

        if type(path) is list:
            path = str(path)
        param['path'] = path

        return self.api_request('Delete', 'delete', param)
    
    """
    method: start_extract_task
    args: file_path, dest_folder
    kwargs: overwrite,
            keep_dir,
            create_subfolder,
            codepage,
            password,
            item_id
    """
    @api_call
    def start_extract_task(self, file_path, dest_folder, **kwargs):

        param = kwargs
        param['file_path'] = file_path
        param['dest_folder_path'] = dest_folder
        
        response = self.api_request('Extract', 'start', param)

        self._extract_taskid = response['data']['taskid']
        self._extract_taskid_list.append(self._extract_taskid)

        return response
    def get_extract_status(self, taskid):
        return self.api_request('Extract', 'status', {'taskid': taskid})
    
    @api_call
    def _stop_extract_task(self, taskid):
        return self.api_request('Extract', 'stop', {'taskid': taskid})

    def stop_extract_task(self, taskid):
        response = self._stop_extract_task(taskid)
        if response['success']:
            self._extract_taskid_list.remove(taskid)
            if self._extract_taskid is taskid:
                self._extract_taskid = self._extract_taksid_list[-1]
        return response
    
    """
    method: get_archive_file_list
    args: file_path
    kwargs: offset,
            limit,
            sort_by,
            sort_direction,
            codepage,
            password,
            item_id
    """
    @api_call
    def get_archive_file_list(self, file_path, **kwargs):
        param = kwargs
        param['file_path'] = file_path
        return self.api_request('Extract', 'list', param)

    def start_file_compression(self, path=None, dest_file_path=None, level=None, mode=None,
                               compress_format=None, password=None):
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'start'}

        if type(path) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in path]
            path = new_path
            path = '[' + ','.join(path) + ']'
            param['path'] = path
        elif path is not None:
            param['path'] = path
        else:
            return 'Enter a valid path'

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'compress_format', '_password', '_api_path',
                           'param', 'path', 'new_path']:
                if val is not None:
                    param[str(key)] = val

        if dest_file_path is None:
            return 'Enter a valid dest_file_path'

        if compress_format is not None:
            param['format'] = compress_format

        if password is not None:
            param['_password'] = password

        self._compress_taskid = self.api_request(api_name, api_path, param)['data']['taskid']

        return 'You can now check the status of request with get_compress_status() , ' \
               'your id is: ' + self._compress_taskid

    def get_compress_status(self, taskid=None):
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'status'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            param['taskid'] = taskid

        return self.api_request(api_name, api_path, param)

    def stop_compress_task(self, taskid=None):
        api_name = 'SYNO.FileStation.Compress'
        info = self.file_station_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'stop'}

        if taskid is None:
            return 'Enter a valid taskid'
        else:
            param['taskid'] = taskid

        return self.api_request(api_name, api_path, param)

    def get_list_of_all_background_task(self, offset=None, limit=None, sort_by=None,
                                        sort_direction=None, api_filter=None):
        api_name = 'SYNO.FileStation.BackgroundTask'
        info = self.file_station_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'list'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'param']:
                if val is not None:
                    param[str(key)] = val

        if type(api_filter) is list:
            new_path = []
            [new_path.append('"' + x + '"') for x in api_filter]
            api_filter = new_path
            api_filter = '[' + ','.join(api_filter) + ']'
            param['api_filter'] = api_filter

        return self.api_request(api_name, api_path, param)

    def get_file(self, path=None, mode=None):
        api_name = 'SYNO.FileStation.Download'
        info = self.file_station_list[api_name]
        api_path = info['path']

        if path is None:
            return 'Enter a valid path'

        session = requests.session()

        url = ('%s%s' % (self.url, api_path)) + '?api=%s&version=%s&method=download&path=%s&mode=%s&_sid=%s' % (
                api_name, info['maxVersion'], parse.quote_plus(path), mode, self.sid)

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
