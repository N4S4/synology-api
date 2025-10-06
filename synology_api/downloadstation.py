"""
Synology Download Station API wrapper.

This module provides a Python interface for managing downloads, tasks, RSS feeds, and BT searches
on Synology NAS devices using the Download Station application.
"""

from __future__ import annotations

import json
from typing import Optional, Any
from . import base_api


class DownloadStation(base_api.BaseApi):
    """
    Core Download Station API implementation for Synology NAS.

    This class provides methods to manage downloads, tasks, RSS feeds, and BT searches.

    Parameters
    ----------
    ip_address : str
        IP address or hostname of the Synology NAS.
    port : str
        Port number to connect to.
    username : str
        Username for authentication.
    password : str
        Password for authentication.
    secure : bool, optional
        Use HTTPS if True, HTTP if False (default is False).
    cert_verify : bool, optional
        Verify SSL certificates (default is False).
    dsm_version : int, optional
        DSM version (default is 7).
    debug : bool, optional
        Enable debug output (default is True).
    otp_code : Optional[str], optional
        One-time password for 2FA (default is None).
    device_id : Optional[str], optional
        Device ID (default is None).
    device_name : Optional[str], optional
        Device name (default is None).
    interactive_output : bool, optional
        Enable interactive output (default is True).
    download_st_version : int, optional
        Download Station API version (default is None).

    Methods
    -------
    get_info()
        Get Download Station info.
    get_config()
        Get Download Station config.
    set_server_config(...)
        Set Download Station server config.
    schedule_info()
        Get schedule info.
    schedule_set_config(...)
        Set schedule config.
    tasks_list(...)
        List download tasks.
    tasks_info(...)
        Get info for specific tasks.
    tasks_source(...)
        Download task source.
    create_task(...)
        Create a new download task.
    delete_task(...)
        Delete a download task.
    pause_task(...)
        Pause a download task.
    resume_task(...)
        Resume a download task.
    edit_task(...)
        Edit a download task.
    get_statistic_info()
        Get Download Station statistics.
    get_rss_info_list(...)
        Get RSS site info list.
    refresh_rss_site(...)
        Refresh RSS site.
    rss_feed_list(...)
        Get RSS feed list.
    start_bt_search(...)
        Start a BT search.
    get_bt_search_results(...)
        Get BT search results.
    get_bt_search_category()
        Get BT search categories.
    clean_bt_search(...)
        Clean BT search tasks.
    get_bt_module()
        Get BT search modules.
    """

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
        """
        Initialize the DownloadStation API wrapper.

        Parameters
        ----------
        ip_address : str
            IP address or hostname of the Synology NAS.
        port : str
            Port number to connect to.
        username : str
            Username for authentication.
        password : str
            Password for authentication.
        secure : bool, optional
            Use HTTPS if True, HTTP if False (default is False).
        cert_verify : bool, optional
            Verify SSL certificates (default is False).
        dsm_version : int, optional
            DSM version (default is 7).
        debug : bool, optional
            Enable debug output (default is True).
        otp_code : Optional[str], optional
            One-time password for 2FA (default is None).
        device_id : Optional[str], optional
            Device ID (default is None).
        device_name : Optional[str], optional
            Device name (default is None).
        interactive_output : bool, optional
            Enable interactive output (default is True).
        download_st_version : int, optional
            Download Station API version (default is None).
        """

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
        """
        Get Download Station info.

        Returns
        -------
        dict[str, object] or str
            Download Station info.
        """
        api_name = 'SYNO.DownloadStation.Info'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, req_param)

    def get_config(self) -> dict[str, object] | str:
        """
        Get Download Station config.

        Returns
        -------
        dict[str, object] or str
            Download Station config.
        """
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
        """
        Set Download Station server configuration.

        Parameters
        ----------
        bt_max_download : Optional[int], optional
            Maximum BT download speed.
        bt_max_upload : Optional[int], optional
            Maximum BT upload speed.
        emule_max_download : Optional[int], optional
            Maximum eMule download speed.
        emule_max_upload : Optional[int], optional
            Maximum eMule upload speed.
        nzb_max_download : Optional[int], optional
            Maximum NZB download speed.
        http_max_download : Optional[int], optional
            Maximum HTTP download speed.
        ftp_max_download : Optional[int], optional
            Maximum FTP download speed.
        emule_enabled : Optional[bool], optional
            Enable eMule.
        unzip_service_enabled : Optional[bool], optional
            Enable unzip service.
        default_destination : Optional[str], optional
            Default download destination.
        emule_default_destination : Optional[str], optional
            Default eMule download destination.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation.Info'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'setserverconfig'}

        for key, val in locals().items():
            if key not in ['self', 'api_name', 'info', 'api_path', 'req_param']:
                if val is not None:
                    req_param[str(key)] = val

        return self.request_data(api_name, api_path, req_param)

    def schedule_info(self) -> dict[str, object] | str:
        """
        Get Download Station schedule configuration.

        Returns
        -------
        dict[str, object] or str
            Schedule configuration.
        """
        api_name = 'SYNO.DownloadStation.Schedule'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'getconfig'}

        return self.request_data(api_name, api_path, req_param)

    def schedule_set_config(self, enabled: bool = False, emule_enabled: bool = False) -> dict[str, object] | str:
        """
        Set Download Station schedule configuration.

        Parameters
        ----------
        enabled : bool, optional
            Enable schedule (default is False).
        emule_enabled : bool, optional
            Enable eMule schedule (default is False).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
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
        """
        List download tasks.

        Parameters
        ----------
        additional_param : Optional[str or list[str]], optional
            Additional fields to retrieve.
        offset : int, optional
            Offset for pagination (default is 0).
        limit : int, optional
            Maximum number of tasks to retrieve (default is -1).

        Returns
        -------
        dict[str, object] or str
            List of download tasks.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'list', 'additional': additional_param, 'limit': limit,
                     'offset': offset}

        if additional_param is None:
            additional_param = ['detail', 'transfer',
                                'file', 'tracker', 'peer']

        req_param['additional'] = json.dumps(additional_param if isinstance(
            additional_param, list) else [additional_param])

        return self.request_data(api_name, api_path, req_param)

    def tasks_info(self, task_id, additional_param: Optional[str | list[str]] = None) -> dict[str, object] | str:
        """
        Get information for specific download tasks.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).
        additional_param : Optional[str or list[str]], optional
            Additional fields to retrieve.

        Returns
        -------
        dict[str, object] or str
            Task information.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get',
                     'id': task_id, 'additional': additional_param}

        if additional_param is None:
            additional_param = ['detail', 'transfer',
                                'file', 'tracker', 'peer']

        req_param['additional'] = json.dumps(additional_param if isinstance(
            additional_param, list) else [additional_param])
        req_param['id'] = json.dumps(
            task_id if isinstance(task_id, list) else [task_id])

        return self.request_data(api_name, api_path, req_param)

    def tasks_source(self, task_id) -> bytes:
        """
        Download task source.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).

        Returns
        -------
        bytes
            Task source content.
        """
        # DownloadStation2 is required here
        api_name = 'SYNO.DownloadStation2.Task.Source'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'download', 'id': task_id}

        return self.request_data(api_name, api_path, req_param, response_json=False).content

    def get_task_list(self, list_id: str) -> dict[str, any]:
        """
        Get info from a task list containing the files to be downloaded.

        This is to be used after creating a task, and before starting the download.

        Parameters
        ----------
        list_id : str
            List ID returned by create_task.

        Returns
        -------
        dict[str, any]
            A dictionary containing a task list information.

        Examples
        --------
        ```json
        {
            "data" : {
                "files" : [
                    {
                        "index" : 0,
                        "name" : "Pulp.Fiction.1994.2160p.4K.BluRay.x265.10bit.AAC5.1-[YTS.MX].mkv",
                        "size" : 2391069024
                    },
                    {
                        "index" : 1,
                        "name" : "YTSProxies.com.txt",
                        "size" : 604
                    },
                    {
                        "index" : 2,
                        "name" : "www.YTS.MX.jpg",
                        "size" : 53226
                    }
                ],
                "size" : 7835426779,
                "title" : "Pulp Fiction (1994) [2160p] [4K] [BluRay] [5.1] [YTS.MX]",
                "type" : "bt"
            },
        }
        ```
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task.List'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'],
                     'method': 'get', 'list_id': list_id}

        return self.request_data(api_name, api_path, req_param)

    def create_task(self, url, destination) -> dict[str, object] | str:
        """
        Create a new download task.

        Parameters
        ----------
        url : str
            Download URL.
        destination : str
            Download destination.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'create', 'type': 'url',
                     'create_list': 'true', 'destination': destination, 'url': f'["{url}"]'}

        return self.request_data(api_name, api_path, req_param)

    def delete_task(self, task_id: str, force: bool = False) -> dict[str, object] | str:
        """
        Delete a download task.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).
        force : bool, optional
            Force delete (default is False).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'delete', 'id': task_id,
                 'force_complete': str(force).lower()}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def pause_task(self, task_id: str) -> dict[str, object] | str:
        """
        Pause a download task.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'],
                 'method': 'pause', 'id': task_id}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def resume_task(self, task_id: str) -> dict[str, object] | str:
        """
        Resume a download task.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'],
                 'method': 'resume', 'id': task_id}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def edit_task(self, task_id: str, destination: str = 'sharedfolder') -> dict[str, object] | str:
        """
        Edit a download task.

        Parameters
        ----------
        task_id : str or list[str]
            Task ID(s).
        destination : str, optional
            New download destination (default is 'sharedfolder').

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.Task'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'edit',
                 'id': task_id, 'destination': destination}

        if type(task_id) is list:
            param['id'] = ",".join(task_id)

        return self.request_data(api_name, api_path, param)

    def download_task_list(
        self,
        list_id: str,
        file_indexes: list[int],
        destination: str,
        create_subfolder: bool = True
    ) -> dict[str, object] | str:
        """
        Download files from a task list.

        Parameters
        ----------
        list_id : str
            Task list ID.
        file_indexes : list[int]
            List of file indexes to download.
            For example, if `get_task_list()` returns `files: [{index: 0, name: "file1.txt"}, {index: 1, name: "file2.txt"}]`, then `file_indexes = [1]` will download only file2.txt.
        destination : str
            Download destination, e.g. 'sharedfolder/subfolder'
        create_subfolder : bool, optional
            Create subfolder. Defaults to `True`

        Returns
        -------
        dict[str, object] or str
            A dictionary containing the task_id for the started download task.

        Examples
        --------
        ```json
        {
            'data': {
                'task_id': 'username/SYNODLTaskListDownload1759340338C7C39ABA'
            }
        }
        ```
        """
        api_name = 'SYNO.DownloadStation' + \
            self.download_st_version + '.Task.List.Polling'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {
            'version': info['maxVersion'],
            'method': 'download',
            'list_id': list_id,
            'file_indexes': ",".join(map(str, file_indexes)),
            'destination': destination,
            'create_subfolder': create_subfolder
        }

        return self.request_data(api_name, api_path, param)

    def get_statistic_info(self) -> dict[str, object] | str:
        """
        Get Download Station statistics.

        Returns
        -------
        dict[str, object] or str
            Statistics information.
        """
        api_name = 'SYNO.DownloadStation.Statistic'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'getinfo'}

        return self.request_data(api_name, api_path, param)

    def get_rss_info_list(self, offset: Optional[int] = None, limit: Optional[int] = None) -> dict[str, object] | str:
        """
        Get RSS site info list.

        Parameters
        ----------
        offset : Optional[int], optional
            Offset for pagination.
        limit : Optional[int], optional
            Maximum number of RSS sites to retrieve.

        Returns
        -------
        dict[str, object] or str
            RSS site info list.
        """
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
        """
        Refresh an RSS site.

        Parameters
        ----------
        rss_id : Optional[str], optional
            RSS site ID.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation.RSS.Site'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'],
                 'method': 'refresh', 'id': rss_id}

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
        """
        Get RSS feed list.

        Parameters
        ----------
        rss_id : Optional[str], optional
            RSS site ID.
        offset : Optional[int], optional
            Offset for pagination.
        limit : Optional[int], optional
            Maximum number of RSS feeds to retrieve.

        Returns
        -------
        dict[str, object] or str
            RSS feed list.
        """
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
        """
        Start a BT search.

        Parameters
        ----------
        keyword : Optional[str], optional
            Search keyword.
        module : str, optional
            BT search module (default is 'all').

        Returns
        -------
        dict[str, object] or str
            BT search task information or message.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'start'}

        if keyword is None:
            return 'Did you enter a keyword to search?'
        else:
            param['keyword'] = keyword

        param['module'] = module

        self._bt_search_id = self.request_data(
            api_name, api_path, param)['data']['taskid']

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
        """
        Get BT search results.

        Parameters
        ----------
        taskid : Optional[str], optional
            BT search task ID.
        offset : Optional[int], optional
            Offset for pagination.
        limit : Optional[int], optional
            Maximum number of results to retrieve.
        sort_by : Optional[str], optional
            Field to sort by.
        sort_direction : Optional[str], optional
            Sort direction.
        filter_category : Optional[str], optional
            Filter by category.
        filter_title : Optional[str], optional
            Filter by title.

        Returns
        -------
        dict[str, object] or str
            BT search results.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'],
                 'method': 'list', 'taskid': taskid}

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
        """
        Get BT search categories.

        Returns
        -------
        dict[str, object] or str
            BT search categories.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, param)

    def clean_bt_search(self, taskid: Optional[str | list[str]] = None) -> dict[str, object] | str:
        """
        Clean BT search tasks.

        Parameters
        ----------
        taskid : Optional[str or list[str]], optional
            BT search task ID(s).

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'],
                 'method': 'clean', 'taskid': taskid}

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
        """
        Get BT search modules.

        Returns
        -------
        dict[str, object] or str
            BT search modules.
        """
        api_name = 'SYNO.DownloadStation' + self.download_st_version + '.BTSearch'
        info = self.download_list[api_name]
        api_path = info['path']
        param = {'version': info['maxVersion'], 'method': 'getModule'}

        return self.request_data(api_name, api_path, param)
