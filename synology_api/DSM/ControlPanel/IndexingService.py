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
    
    pass