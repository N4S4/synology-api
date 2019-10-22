from .synology import Synology

class DownloadStation(Synology):

    def __init__(self, ip_address, port, username, password):
        super(DownloadStation, self).__init__(ip_address, port, username,
                password)
        self.app = 'DownloadStation'
        self._bt_search_id = ''
        self._bt_search_id_list = []
        self.login(self.app)
        self.populate_api_dict(self.app)

    def logout(self):
        self.logout(self.app)
    
    @self.api_call
    def get_info(self):
        return self.api_request(self.app, 'Info', 'getinfo')
    
    @self.api_call
    def get_config(self):
        return self.api_request(self.app, 'Info', 'getconfig')
    
    """
    Method: set_server_config
    Args: bt_max_dl=None, bt_max_ul=None, 
          emule_max_dl=None, emule_max_ul=None,
          nzb_max_dl=None,
          http_max_dl=None,
          ftp_max_dl=None,
          emule_enabled=False,
          unzip_service_enabled=False,
          default_destination=None,
          emule_default_destination=None
    """
    @self.api_call
    def set_server_config(self, **kwargs):
        param = {}
        for key in kwargs.keys():
            param[str(key)] = kwargs[key]
        return self.api_request(self.app, 'Info', 'setserverconfig',
                param=param)
    
    @self.api_call
    def schedule_info(self):
        return self.api_request(self.app, 'Schedule', 'getconfig')
    
    @self.api_call
    def schedule_set_config(self, enabled=False, emule_enabled=False):
        for b in [enabled, emule_enabled]:
            if b != True and b != False:
                raise TypeError(
                        "Parameter {b} must be True or False.".format(b=b))

        param = {'enabled': str(enabled).lower(), 
                 'emule_enabled': str(emule_enabled).lower()}
        return self.api_request(self.app, 'Schedule', 'setconfig', param)
    
    @self.api_call
    def tasks_list(self, additional_param=None):
        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        param = {'additional': ",".join(additional_param)}

        return self.api_request(self.app, 'Task', 'list', param)
    
    @self.api_call
    def tasks_info(self, task_id, additional_param=None):
        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        param = {'additional': ",".join(additional_param)}

        return self.api_request(self.app, 'Task', 'getinfo', param)
    
    @self.api_call
    def delete_task(self, task_id, force=False):
        if type(task_id) is list:
            task_id = ",".join(task_id) #task_id is now type str
        param = {'id': task_id, 'force_complete': str(force).lower()}

        return self.api_request(self.app, 'Task', 'delete', param)
    
    @self.api_call
    def pause_task(self, task_id):
        if type(task_id) is list:
            task_id  = ",".join(task_id) #task_id is now type str
        param = {'id': task_id}

        return self.api_request(self.app, 'Task', 'pause', param)

    @self.api_call
    def resume_task(self, task_id): 
        if type(task_id) is list:
            task_id = ",".join(task_id) #task_id is now type str
        param = {'id': task_id}

        return self.api_request(self.app, 'Task', 'resume', param)
    
    @self.api_call
    def edit_task(self, task_id, destination='sharedfolder'):
        if type(task_id) is list:
            task_id = ",".join(task_id) #task_id is now type str
        param = {'id': task_id, 'destination': destination}

        return self.api_request(self.app, 'Task', 'edit', param)
    
    @self.api_call
    def get_statistic_info(self):
        return self.api_request(self.app, 'Statistic', 'getinfo')
    
    @self.api_call
    def get_rss_info_list(self, offset=None, limit=None):
        api_name = 'SYNO.DownloadStation.RSS.Site'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'list'}

        if offset is not None:
            param['offset'] = offset
        if limit is not None:
            param['limit'] = limit

        return self.request_data(api_name, api_path, param)
    
    @self.api_call
    def refresh_rss_site(self, rss_id=None):
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
    
    @self.api_call
    def rss_feed_list(self, rss_id=None, offset=None, limit=None):
        api_name = 'SYNO.DownloadStation.RSS.Feed'
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

    @self.api_call
    def start_bt_search(self, keyword=None, module='all'):
        api_name = 'SYNO.DownloadStation.BTSearch'
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

        return 'You can now check the status of request with get_bt_search_results(), your id is: ' + self._bt_search_id

    @self.api_call
    def get_bt_search_results(self, taskid=None, offset=None, limit=None, sort_by=None, sort_direction=None,
                              filter_category=None, filter_title=None):
        api_name = 'SYNO.DownloadStation.BTSearch'
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
    
    @self.api_call
    def get_bt_search_category(self):
        api_name = 'SYNO.DownloadStation.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, param)

    @self.api_call
    def clean_bt_search(self, taskid=None):
        api_name = 'SYNO.DownloadStation.BTSearch'
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

    @self.api_call
    def get_bt_module(self):
        api_name = 'SYNO.DownloadStation.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'getModule'}

        return self.request_data(api_name, api_path, param)

