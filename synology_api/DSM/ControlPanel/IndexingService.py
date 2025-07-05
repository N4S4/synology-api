from synology_api import base_api

class IndexingService(base_api.BaseApi):
    """
    Indexing service class for interacting with Synology DSM Indexing service settings.
    
    Supported methods:
    - Getters:
        
    - Setters:

    """
    
    def get_indexed_folders(self) -> dict:
        """Get indexed folders.
        
            Returns
            -------
            dict
                Return list of folders indexed by the indexing service.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "folders": [
                        {
                            "default": false,
                            "exist": true,
                            "name": "Films",
                            "path": "/Films",
                            "types": [
                                "video"
                            ]
                        },
                        {
                            "default": false,
                            "exist": true,
                            "name": "Series",
                            "path": "/Series",
                            "types": [
                                "video"
                            ]
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing.IndexFolder'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_media_indexing_status(self) -> dict:
        """Get media indexing status.
        
            Returns
            -------
            dict
                Return the status of the media indexing service.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "reindexing": false
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_thumbnail_quality_settings(self) -> dict:
        """Get thumbnail quality settings.
        
            Returns
            -------
            dict
                Return the thumbnail quality settings.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "packages": [],
                    "thumbnail_quality": "normal"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing.ThumbnailQuality'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_shuduler_settings(self) -> dict:
        """Get scheduler settings.
        
            Returns
            -------
            dict
                Return the scheduler settings of the indexing service.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "duration": 1,
                    "manual_action_by_user": "none",
                    "mode": "schedule",
                    "start": {
                        "hour": 0
                    },
                    "week": [
                        true,
                        true,
                        true,
                        true,
                        true,
                        true,
                        true
                    ]
                },
                "success": true,
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing.Scheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'get'
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_indexed_folders(self, folders: list) -> dict:
        """Set indexed folders.
        
            Parameters
            ----------
            folders : list
                A list of dictionaries representing the folders to be indexed. Each dictionary should contain:
                - `path`: The path of the folder to be indexed.
                - `name`: The name of the folder.
                - `default`: A boolean indicating if this is a default folder. Should be `False`
                - `types`: A list of media types to index in the folder (e.g., `["video"]`). Fiels are `photo`, `video`, `music`.
                
                example:
                ```json
                [
                    {
                        "path": "/Films",
                        "name": "Films",
                        "default": false,
                        "types": ["video"]
                    },
                    {
                        "path": "/Series",
                        "name": "Series",
                        "default": false,
                        "types": ["video"]
                    }
                ]
                ```
        
            Returns
            -------
            dict
                Return the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing.IndexFolder'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'folders': folders
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_thumbnail_quality_settings(self, quality: str = "normal") -> dict:
        """Set thumbnail quality settings.
        
            Parameters
            ----------
            quality : str
                The desired thumbnail quality setting. Options are `normal`, `high`. Default to `normal`.
        
            Returns
            -------
            dict
                Return the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "thumbnail_quality": "normal"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.Core.MediaIndexing.ThumbnailQuality'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'quality': quality
        }
        return self.request_data(api_name, api_path, req_param)
    
    def set_shudler_settings(self, mode: str = "always", start_hour: int = 0, duration: int = 1, week: list = [True, True, True, True, True, True, True]) -> dict:
        """Set scheduler settings.
        
            Parameters
            ----------
            mode : str
                The scheduling mode. Options are `schedule`, `always`. Default to `always`.
            start_hour : int
                The hour to start the indexing service. Default to `0`. Not used if `mode` is set to `always`.
            duration : int
                The duration in hours for the indexing service. Default to `1`. Not used if `mode` is set to `always`.
            week : list
                A list of booleans indicating which days of the week the service should run. Default to `[True, True, True, True, True, True, True]`. Not used if `mode` is set to `always`.
        
            Returns
            -------
            dict
                Return the result of the operation.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "duration": 1,
                    "manual_action_by_user": "none",
                    "mode": "schedule",
                    "start": {
                        "hour": 0
                    },
                    "week": [
                        true,
                        true,
                        true,
                        true,
                        true,
                        true,
                        true
                    ]
                },
                "success": true
            }
            ```
        """
        if week is None:
            week = [True] * 7
        
        api_name = 'SYNO.Core.MediaIndexing.Scheduler'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'set',
            'mode': mode,
            'start': {'hour': start_hour},
            'duration': duration,
            'week': week
        }
        return self.request_data(api_name, api_path, req_param)
    
    
    pass