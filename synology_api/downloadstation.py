from .synology import Synology, api_call


class DownloadStation(Synology):

    # this is a function so that ithe value returned is not accidentally changed
    def app(self):
        return 'DownloadStation'

    def __init__(self, ip_address, port, username, password):
        super(DownloadStation, self).__init__(ip_address, port, username,
                                              password)
        self._bt_search_id = ''
        self._bt_search_id_list = []
        self.login(self.app())
        self.populate_api_dict(self.app())

    def logout(self):
        super().logout(self.app())

    @api_call
    def get_info(self):
        return self.api_request('Info', 'getinfo')

    @api_call
    def get_config(self):
        return self.api_request('Info', 'getconfig')

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

    @api_call
    def set_server_config(self, **kwargs):
        param = {}
        for key in kwargs.keys():
            param[str(key)] = kwargs[key]
        return self.api_request('Info', 'setserverconfig',
                                param=param)

    @api_call
    def schedule_info(self):
        return self.api_request('Schedule', 'getconfig')

    @api_call
    def schedule_set_config(self, enabled=False, emule_enabled=False):
        for b in [enabled, emule_enabled]:
            if b is not True and b is not False:
                raise TypeError(
                    "Parameter {b} must be True or False.".format(b=b))

        param = {'enabled': str(enabled).lower(),
                 'emule_enabled': str(emule_enabled).lower()}
        return self.api_request('Schedule', 'setconfig', param)

    @api_call
    def tasks_list(self, additional_param=None):
        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        param = {'additional': ",".join(additional_param)}

        return self.api_request('Task', 'list', param)

    @api_call
    def tasks_info(self, task_id, additional_param=None):
        if additional_param is None:
            additional_param = ['detail', 'transfer', 'file', 'tracker', 'peer']

        param = {'additional': ",".join(additional_param)}

        return self.api_request('Task', 'getinfo', param)

    @api_call
    def delete_task(self, task_id, force=False):
        if type(task_id) is list:
            task_id = ",".join(task_id)  # task_id is now type str
        param = {'id': task_id, 'force_complete': str(force).lower()}

        return self.api_request('Task', 'delete', param)

    @api_call
    def pause_task(self, task_id):
        if type(task_id) is list:
            task_id = ",".join(task_id)  # task_id is now type str
        param = {'id': task_id}

        return self.api_request('Task', 'pause', param)

    @api_call
    def resume_task(self, task_id):
        if type(task_id) is list:
            task_id = ",".join(task_id)  # task_id is now type str
        param = {'id': task_id}

        return self.api_request('Task', 'resume', param)

    @api_call
    def edit_task(self, task_id, destination='sharedfolder'):
        if type(task_id) is list:
            task_id = ",".join(task_id)  # task_id is now type str
        param = {'id': task_id, 'destination': destination}

        return self.api_request('Task', 'edit', param)

    @api_call
    def get_statistic_info(self):
        return self.api_request('Statistic', 'getinfo')

    @api_call
    def get_rss_info_list(self, offset=None, limit=None):

        param = {}
        if offset is not None:
            param['offset'] = offset
        if limit is not None:
            param['limit'] = limit
        if len(param) == 0:
            param = None

        return self.api_request('RSS.Site', 'list', param)

    @api_call
    def refresh_rss_site(self, rss_id):

        param = {'id': rss_id}
        if type(rss_id) is list:
            rss_id = ','.join(rss_id)
            param['id'] = rss_id

        return self.api_request('RSS.Site', 'refresh', param)

    @api_call
    def rss_feed_list(self, offset=None, limit=None, rss_id=None):

        param = {'id': rss_id}

        if type(rss_id) is list:
            rss_id = ','.join(rss_id)
            param['id'] = rss_id

        if offset is not None:
            param['offset'] = offset
        if limit is not None:
            param['limit'] = limit

        return self.api_request('RSS.Feed', 'list', param)

    @api_call
    def start_bt_search(self, keyword, module='all'):

        param = {'keyword': keyword, 'module': module}

        self._bt_search_id = self.api_request('BTSearch', 'start', param)['data']['taskid']

        self._bt_search_id_list.append(self._bt_search_id)

        return self._bt_search_id

    """
    method: get_bt_search_results
    args: taskid,
          offset,
          limit,
          sort_by,
          sort_direction,
          filter_category,
          filter_title
    """

    @api_call
    def get_bt_search_results(self, taskid, **kwargs):
        param = {}
        if type(taskid) is list:
            param['taskid'] = ','.join(taskid)
        param.update(kwargs)

        return self.api_request('BTSearch', 'list', param)

    @api_call
    def get_bt_search_category(self):
        return self.api_request('BTSearch', 'get')

    @api_call
    def clean_bt_search(self, taskid):

        param = {'taskid': taskid}
        if type(taskid) is list:
            param['taskid'] = ','.join(taskid)
            for item in taskid:
                self._bt_search_id_list.remove(item)
        else:
            self._bt_search_id_list.remove(taskid)

        return self.api_request('BTSearch', 'path', param)

    @api_call
    def get_bt_module(self):
        return self.api_request('BTSearch', 'getModule')
