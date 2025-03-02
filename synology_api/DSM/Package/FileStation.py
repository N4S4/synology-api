from __future__ import annotations
from typing import Optional, Any
from datetime import datetime
import requests, tqdm, time, io, json, os, sys
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from urllib import parse
from treelib import Tree
from synology_api import base_api


class FileStation(base_api.BaseApi):
    """Implementation of FileStation API based on the Synology API documentation [link](https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/FileStation/All/enu/Synology_File_Station_API_Guide.pdf)
    """

    def get_info(self) -> dict[str, object]:
        """Get info about FileStation
        
            Returns
            -------
            dict[str, object]
                List of FileStation info
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "allow_normal_disable_html": true,   
                    "enable_list_usergrp": false,        
                    "enable_send_email_attachment": true,
                    "enable_view_google": true,
                    "enable_view_microsoft": true,
                    "hostname": "SYNO-FLORENTB",
                    "is_manager": true,
                    "items": [
                        {
                            "gid": 100
                        },
                        {
                            "gid": 101
                        },
                        {
                            "gid": 1023
                        }
                    ],
                    "support_file_request": true,
                    "support_sharing": true,
                    "support_vfs": true,
                    "support_virtual": {
                        "enable_iso_mount": true,
                        "enable_remote_mount": true
                    },
                    "support_virtual_protocol": [
                        "cifs",
                        "nfs",
                        "iso"
                    ],
                    "system_codepage": "fre",
                    "uid": 1027
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Info'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get'}

        return self.request_data(api_name, api_path, req_param)

    def get_list_share(self,
            additional: Optional[list[str]] = None,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            sort_by: Optional[str] = None,
            sort_direction: Optional[str] = None,
            onlywritable: bool = False
        ) -> dict[str, object]:
        """Get list of shared folders
        
            Parameters
            ----------
            additional : Optional[list[str]], optional
                Additionnal field to retrieve from shared folder. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","mount_point_type","sync_share","volume_status","indexed","hybrid_share","worm_share"]`.
            offset : Optional[int], optional
                Offset in the shared folder list. Defaults to `None`
            limit : Optional[int], optional
                Limit the len of the returned list. Defaults to `None`
            sort_by : Optional[str], optional
                Specify which file information to sort on. Defaults to `None`
                All fields know are: `["name","user","group","mtime","atime","ctime","crtime","posix"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `None`
                All possible direction are: `["asc","desc"]`
            onlywritable : bool, optional
                Force list of shared folder where the user as write access. Defaults to `False`
        
            Returns
            -------
            dict[str, object]
                List of shared folder in FileStation
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "offset": 0,
                    "shares": [
                        {
                            "isdir": true,      
                            "name": "docker",   
                            "path": "/docker"   
                        },
                        {
                            "isdir": true,      
                            "name": "Documents",
                            "path": "/Documents"
                        }
                    ],
                    "total": 2
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.List'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list_share',
            'onlywritable': onlywritable,
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'additional': json.dumps(additional)
        }

        return self.request_data(api_name, api_path, req_param)

    def get_file_list(self,
            folder_path: str,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            sort_by: Optional[str] = None,
            sort_direction: Optional[str] = None,
            pattern: Optional[list[str]] = None,
            filetype: Optional[str] = None,
            goto_path: Optional[str] = None,
            additional: Optional[list[str]] = None,
            check_dir: Optional[bool] = None
        ) -> dict[str, object]:
        """Get list of files in a folder
        
            Parameters
            ----------
            folder_path : str
                A listed folder path starting with a shared folder.
            offset : Optional[int], optional
                Specify how many files are skipped before beginning to return listed files. Defaults to `None`
            limit : Optional[int], optional
                Number of files requested. 0 indicates to list all files with a given folder. Defaults to `None`
            sort_by : Optional[str], optional
                Specify which file information to sort on. Defaults to `None`
                All fields known are: `["name","size","user","group","mtime","atime","ctime","crtime","posix","type"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `None`
                All possible direction are: `["asc","desc"]`
            pattern : Optional[list[str]], optional
                Given glob pattern(s) to find files whose names and extensions match a case insensitive glob pattern. Defaults to `None`
                Note: 1. If the pattern doesn't contain any glob syntax (? and *), * of glob syntax will be added at begin and end of the string automatically for partially matching the pattern.
            filetype : Optional[str], optional
                "file": only enumerate regular files; "dir": only enumerate folders; "all" enumerate regular files and folders. Defaults to `None`
                All fields know are: `["file","dir","all"]`
            goto_path : Optional[str], optional
                Folder path starting with a shared folder. Return all files and sub-folders within folder_path path until goto_path path recursively. Defaults to `None`
                Note: goto_path is only valid with parameter "additional" contains real_path. 
            additional : Optional[list[str]], optional
                Additionnal field to retrieve from file. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","type","mount_point_type"]`.
            check_dir : Optional[bool], optional
                _description_. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                _description_
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "files": [
                        {
                            "isdir": false,
                            "name": "compose.yaml",
                            "path": "/docker/compose.yaml"
                        }
                    ],
                    "offset": 0,
                    "total": 1
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.FileStation.List'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'action': 'list',
            'method': 'list',
            'folder_path': folder_path,
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'pattern': ', '.join(pattern) if isinstance(pattern, list) else pattern if isinstance(pattern, str) else None,
            'filetype': filetype,
            'goto_path': goto_path,
            'additional': json.dumps(additional),
            'check_dir': check_dir
        }

        return self.request_data(api_name, api_path, req_param)

    def get_file_info(self, path: list[str], additional: Optional[list[str]] = None) -> dict[str, object]:
        """Get information of file(s) / folder(s).

            Parameters
            ----------
            path : list[str]
                One or more folder/file path(s) starting with a shared folder
            additional : Optional[list[str]], optional
                Additionnal field to retrieve from file. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","type","mount_point_type"]`.
        
            Returns
            -------
            dict[str, object]
                Information of file(s) / folder(s)
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "files": [
                        {
                            "isdir": true,
                            "name": "Films",
                            "path": "/Films"
                        },
                        {
                            "isdir": true,
                            "name": "Documents",
                            "path": "/Documents"
                        }
                    ]
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.List'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'getinfo',
            'path': json.dumps(path),
            'additional': json.dumps(additional)
        }

        return self.request_data(api_name, api_path, req_param)

    def search_start(self,
            folder_path: str = None, recursive: Optional[bool] = None, pattern: Optional[list[str]] = None,
            extension: Optional[list[str]] = None, filetype: Optional[str] = None, size_from: Optional[int] = None,
            size_to: Optional[int] = None, mtime_from: Optional[int] = None, mtime_to: Optional[int] = None,
            crtime_from: Optional[int] = None, crtime_to: Optional[int] = None, atime_from: Optional[int] = None,
            atime_to: Optional[int] = None, owner: Optional[str] = None, group: Optional[str] = None
        ) -> dict[str, object]:
        """Start to search files according to given criteria. If more than one criterion is given in different parameters, searched files match all these criteria.
        
            Parameters
            ----------
            folder_path : str, optional
                A searched folder path starting with a shared folder. One or more folder paths to be searched, separated by commas "," and around brackets. Defaults to `None`
            recursive : Optional[bool], optional
                If searching files within a folder and subfolders recursively or not. Defaults to `None`
            pattern : Optional[list[str]], optional
                Given glob pattern(s) to find files whose names and extensions match a case insensitive glob pattern. Defaults to `None`
                Note: 1. If the pattern doesn't contain any glob syntax (? and *), * of glob syntax will be added at begin and end of the string automatically for partially matching the pattern.. Defaults to `None`
            extension : Optional[list[str]], optional
                Search for files whose extensions match a file type pattern in a case-insensitive glob pattern. If you give this criterion, folders aren't matched. Defaults to `None`
            filetype : Optional[str], optional
                "file": only enumerate regular files; "dir": only enumerate folders; "all" enumerate regular files and folders. Defaults to `None`
                All fields know are: `["file","dir","all"]`
            size_from : Optional[int], optional
                Search for files whose sizes are greater than the given byte size. Defaults to `None`
            size_to : Optional[int], optional
                Search for files whose sizes are less than the given byte size. Defaults to `None`
            mtime_from : Optional[int], optional
                Search for files whose last modified time after the given Linux timestamp (UTC) in second. Defaults to `None`
            mtime_to : Optional[int], optional
                Search for files whose last modified time before the given Linux timestamp (UTC) in second. Defaults to `None`
            crtime_from : Optional[int], optional
                Search for files whose create time after the given Linux timestamp (UTC) in second. Defaults to `None`
            crtime_to : Optional[int], optional
                Search for files whose create time before the given Linux timestamp (UTC) in second. Defaults to `None`
            atime_from : Optional[int], optional
                Search for files whose last access time after the given Linux timestamp (UTC) in second. Defaults to `None`
            atime_to : Optional[int], optional
                Search for files whose last access time before the given Linux timestamp (UTC) in second. Defaults to `None`
            owner : Optional[str], optional
                Search for files whose user name matches this criterion. This criterion is case-insensitive. Defaults to `None`
            group : Optional[str], optional
                Search for files whose group name matches this criterion. This criterion is case-insensitive. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                A unique ID for the search task
        
            Example return
            ----------
            ```json
            {
                "data": { 
                    "has_not_index_share": true,  
                    "taskid": "51CE617CF57B24E5" 
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.FileStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'folder_path': folder_path,
            'recursive': recursive,
            'pattern': ', '.join(pattern) if isinstance(pattern, list) else pattern if isinstance(pattern, str) else None,
            'extension': ', '.join(extension) if isinstance(extension, list) else extension if isinstance(extension, str) else None,
            'filetype': filetype,
            'size_from': size_from,
            'size_to': size_to,
            'mtime_from': mtime_from,
            'mtime_to': mtime_to,
            'crtime_from': crtime_from,
            'crtime_to': crtime_to,
            'atime_from': atime_from,
            'atime_to': atime_to,
            'owner': owner,
            'group': group
        }

        return self.request_data(api_name, api_path, req_param)

    def get_search_list(self,
            taskid: str,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            sort_by: Optional[str] = None,
            sort_direction: Optional[str] = None,
            pattern: Optional[list[str]] = None,
            filetype: Optional[str] = None,
            additional: Optional[list[str]] = None
        ) -> dict[str, object]:
        """List matched files in a search temporary database. You can check the finished value in response to know if the search operation is processing or has been finished.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the search task which is obtained from `search_start` method.
            offset : Optional[int], optional
                Specify how many files are skipped before beginning to return listed files. Defaults to `None`
            limit : Optional[int], optional
                Number of files requested. 0 indicates to list all files with a given folder. Defaults to `None`
            sort_by : Optional[str], optional
                Specify which file information to sort on. Defaults to `None`
                All fields known are: `["name","size","user","group","mtime","atime","ctime","crtime","posix","type"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `None`
                All possible direction are: `["asc","desc"]`
            pattern : Optional[list[str]], optional
                Given glob pattern(s) to find files whose names and extensions match a case insensitive glob pattern. Defaults to `None`
                Note: 1. If the pattern doesn't contain any glob syntax (? and *), * of glob syntax will be added at begin and end of the string automatically for partially matching the pattern.
            filetype : Optional[str], optional
                "file": only enumerate regular files; "dir": only enumerate folders; "all" enumerate regular files and folders. Defaults to `None`
                All fields know are: `["file","dir","all"]`
            additional : Optional[list[str]], optional
                Additionnal field to retrieve from file. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","type"]`.

            Returns
            -------
            dict[str, object]
                Infos about the search and the matched files.
        
            Example return
            ----------
            ```json
            {
                "data": {     
                    "files": [
                        {     
                            "isdir": false,
                            "name": "compose.yaml",
                            "path": "/docker/compose.yaml"
                        }
                    ],
                    "finished": true,
                    "offset": 0,
                    "total": 1
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'taskid': taskid,
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'pattern': ', '.join(pattern) if isinstance(pattern, list) else pattern if isinstance(pattern, str) else None,
            'filetype': filetype,
            'additional': json.dumps(additional)
        }

        return self.request_data(api_name, api_path, req_param)

    def stop_search_task(self, taskid: str | list[str]) -> dict[str, object]:
        """Stop the searching task(s). The search temporary database won't be deleted, so it's possible to list the search result using list method after stopping it
        
            Parameters
            ----------
            taskid : str | list[str]
                Unique ID(s) for the search task which are obtained from `search_start` method. Specify multiple search task IDs by using list type.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': json.dumps(taskid) if isinstance(taskid, list) else taskid,
        }

        return self.request_data(api_name, api_path, req_param)

    def clean_search_task(self, taskid: str | list[str]) -> dict[str, object]:
        """ Delete search temporary database(s).
        
            Parameters
            ----------
            taskid : str | list[str]
                Unique ID(s) for the search task which are obtained from `search_start` method. Specify multiple search task IDs by using list type.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Search'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'clean',
            'taskid': json.dumps(taskid) if isinstance(taskid, list) else taskid,
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_mount_point_list(self, mount_type: str, offset: Optional[int] = None, limit: Optional[int] = None,
            sort_by: Optional[str] = None, sort_direction: Optional[str] = None, additional: Optional[list[str]] = None
        ) -> dict[str, object]:
        """List all mount point folders on one given type of virtual file system.
        
            Parameters
            ----------
            mount_type : str
                A type of virtual file systems.
                All fields known are: `["cifs","nfs","iso"]`
            offset : Optional[int], optional
                Specify how many mount point folders are skipped before beginning to return listed files. Defaults to `None`
            limit : Optional[int], optional
                Number of mount point folders requested. 0 indicates to list all files with a given folder. Defaults to `None`
            sort_by : Optional[str], optional
                Specify which file information to sort on. Defaults to `None`
                All fields known are: `["name",,"user","group","mtime","atime","ctime","crtime","posix"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `None`
                All possible direction are: `["asc","desc"]`
            additional : Optional[list[str]], optional
                Additionnal field to retrieve from file. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","volume_status"]`.
        
            Returns
            -------
            dict[str, object]
                List of mount point folders
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "folders": [ 
                        { 
                            "additional": { 
                                "mount_point_type": "remote", 
                                "owner": { 
                                    "gid": 100, 
                                    "group": "users", 
                                    "uid": 1024, 
                                    "user": "admin" 
                                }, 
                                "perm": { 
                                    "acl": { 
                                        "append": true, 
                                        "del": true, 
                                        "exec": true, 
                                        "read": true, 
                                        "write": true 
                                    }, 
                                    "is_acl_mode": false, 
                                    "posix": 777 
                                }, 
                                "real_path": "/volume1/vidoe/remote", 
                                "time": { 
                                    "atime": 1372313445, 
                                    "crtime": 1320204670, 
                                    "ctime": 1371206944, 
                                    "mtime": 1371206944 
                                }, 
                                "volume_status": { 
                                    "freespace": 12282422599680, 
                                    "readonly": false, 
                                    "totalspace": 801958928384 
                                } 
                            }, 
                            "isdir": true, 
                            "name": "remote", 
                            "path": "/video/remote" 
                        }
                    ],
                    "offset": 0,
                    "total": 0
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.FileStation.VirtualFolder'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'type': mount_type,
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'additional': json.dumps(additional)
        }

        return self.request_data(api_name, api_path, req_param)

    def get_favorite_list(self,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            status_filter: Optional[str] = None,
            additional: Optional[str | list[str]] = None
        ) -> dict[str, object]:
        """List user's favorites.
        
            Parameters
            ----------
            offset : Optional[int], optional
                Specify how many favorites are skipped before beginning to return user's favorites. Defaults to `None`
            limit : Optional[int], optional
                Number of favorites requested. 0 indicates to list all favorites. Defaults to `None`
            status_filter : Optional[str], optional
                Show favorites with a given favorite status. Defaults to `None`
                All fields known are: `["valid","broken","all"]`
            additional : Optional[str  |  list[str]], optional
                Additionnal field to retrieve from file. Defaults to `None`
                All fields known are: `["real_path","owner","time","perm","mount_point_type"]`.
        
            Returns
            -------
            dict[str, object]
                List of user's favorites
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "favorites": [ 
                        { 
                            "isdir": true, 
                            "name": "My Video Shared folder", 
                            "path": "/video", 
                            "status": "valid" 
                        }, 
                        { 
                            "isdir": false, 
                            "name": "deletedfolder", 
                            "path": "/share/deletedfolder", 
                            "status": "broken" 
                        } 
                    ], 
                    "offset": 0, 
                    "total": 2
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'offset': offset,
            'limit': limit,
            'status_filter': status_filter,
            'additional': json.dumps(additional)
        }

        return self.request_data(api_name, api_path, req_param)

    def add_a_favorite(self, path: str, name: Optional[str] = None, index: Optional[int] = -1) -> dict[str, object]:
        """ Add a folder to user's favorites.
        
            Parameters
            ----------
            path : str
                A folder path starting with a shared folder is added to the user's favorites.
            name : Optional[str], optional
                A favorite name. Defaults to `None`
            index : Optional[int], optional
                Index of location of an added favorite. Defaults to `-1`
                If it's equal to -1, the favorite will be added to the last one in user's favorite.
                If it's between 0 ~ total number of favorites-1, the favorite will be inserted into user's favorites by the index.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'add',
            'path': path,
            'name': name,
            'index': index
        }

        return self.request_data(api_name, api_path, req_param)

    def delete_a_favorite(self, path: str) -> dict[str, object]:
        """Delete a favorite in user's favorites.
        
            Parameters
            ----------
            path : str
                A folder path starting with a shared folder is deleted from a user's favorites.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'path': path
        }

        return self.request_data(api_name, api_path, req_param)

    def clear_broken_favorite(self) -> dict[str, object]:
        """ Delete all broken statuses of favorites.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'clear_broken'
        }

        return self.request_data(api_name, api_path, req_param)

    def edit_favorite_name(self, path: str, new_name: str) -> dict[str, object]:
        """Edit a favorite name.
        
            Parameters
            ----------
            path : str
                A folder path starting with a shared folder is edited from a user's favorites.
            new_name : str
                New favorite name.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'edit',
            'path': path,
            'new_name': new_name
        }

        return self.request_data(api_name, api_path, req_param)

    def replace_all_favorite(self, path: str | list[str], name: str | list[str]) -> dict[str, object]:
        """ Replace multiple favorites of folders to the existing user's favorites.
        
            Parameters
            ----------
            path : str | list[str]
                One or more folder paths starting with a shared folder is added to the user's favorites.
                The number of paths must be the same as the number of favorite names in the name parameter.
                The first path parameter corresponds to the first name parameter.
            name : str | list[str]
                One or more new favorite names. The number of favorite names must be the same as the number of folder paths in the path parameter.
                The first name parameter corresponding to the first path  parameter.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.Favorite'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'edit',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'name': json.dumps(name) if isinstance(name, list) else name
        }

        return self.request_data(api_name, api_path, req_param)

    def get_thumbnail(self, path: str, size: Optional[str] = "small", rotate: Optional[int] = None) -> bytes:
        """ Get a thumbnail of a file.
        
            Parameters
            ----------
            path : str
                A file path starting with a shared folder.
            size : str
                The size of the thumbnail. Defaults to `small`
                All fields known are: `["small","medium","large","original"]`
            rotate : Optional[int], optional
                The angle of the thumbnail. Defaults to `None`
                All fields known are: `[0,1,2,3,4] = ["0°","90°","180°","270°","360°"]`
                
            Returns
            -------
            bytes
                The thumbnail of the file. If the file is not found, it will raise an exception.
                
        """
        
        api_name = 'SYNO.FileStation.Thumb'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': "get",
            'path': path,
            'size': size,
            'rotate': rotate
        }
        response = self.request_data(api_name, api_path, req_param, response_json=False)
        match response.status_code:
            case 200:
                return response.content
            case 404:
                raise Exception("File not found")
            case _:
                raise Exception(f"HTTP Status error : {response.status_code}")

    def start_dir_size_calc(self, path: str | list[str]) -> dict[str, object]:
        """Start to calculate size for one or more file/folder paths.
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths starting with a shared folder for calculating cumulative size
        
            Returns
            -------
            dict[str, object]
                Task ID for the size calculation request
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "51CBD7CD5C76E461"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'path': json.dumps(path) if isinstance(path, list) else path
        }
        return self.request_data(api_name, api_path, req_param)['data']['taskid']

    def get_dir_status(self, taskid: str) -> dict[str, object]:
        """Get the status of the size calculating task.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the task which is obtained from `start_dir_size_calc` method.
        
            Returns
            -------
            dict[str, object]
                Infos about the size calculating task
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "finished": true, 
                    "num_dir": 3, 
                    "num_file": 104, 
                    "total_size": 29973265 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }

        return self.request_data(api_name, api_path, req_param)

    def stop_dir_size_calc(self, taskid: str) -> dict[str, object]:
        """Stop the calculation.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the task which is obtained from `start_dir_size_calc` method.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.DirSize'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def start_md5_calc(self, file_path: str) -> dict[str, object]:
        """Start to get MD5 of a file.
        
            Parameters
            ----------
            file_path : str
                A file path starting with a shared folder for calculating MD5 value.
        
            Returns
            -------
            dict[str, object]
                Task ID for the size calculation request
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "51CBD7CD5C76E461"
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.MD5'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'file_path': file_path
        }
        return self.request_data(api_name, api_path, req_param)

    def get_md5_status(self, taskid: str) -> dict[str, object]:
        """ Get the status of the MD5 calculation task.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the task which is obtained from `start_md5_status` method.
        
            Returns
            -------
            dict[str, object]
                Finished status of the MD5 calculation task and the md5 of requested file
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "finished": true, 
                    "md5": "6336c5a59aa63dd2042783f88e15410a"
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.MD5'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def stop_md5_calc(self, taskid: str) -> dict[str, object]:
        """Stop calculating the MD5 of a file.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the task which is obtained from `start_md5_status` method.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.DirSize'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def check_permissions(self,
            path: str,
            filename: str,
            overwrite: Optional[bool] = False,
            create_only: Optional[bool] = True
        ) -> dict[str, object]:
        """Check if a logged-in user has write permission to create new files/folders in a given folder
        
            Parameters
            ----------
            path : str
                A folder path starting with a shared folder to check write permission
            filename : str
                A filename you want to write to given path
            overwrite : Optional[bool], optional
                The value could be one of following: Defaults to `False`
                - "true": overwrite the destination file if one exists. 
                - "false": skip if the destination file exists.
                
                Note: when it's not specified as true or false, it will be responded with error when the destination file exists. 
                
            create_only : Optional[bool], optional
                If set to "true", the permission will be allowed when there is non-existent file/folder. Defaults to `True`
        
            Returns
            -------
            dict[str, object]
                The request will get error response if no write permission for the specified path.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.CheckPermission'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'write',
            'path': path,
            'filename': filename,
            'overwrite': overwrite,
            'create_only': create_only
        }
        return self.request_data(api_name, api_path, req_param)

    def upload_file(self,
            dest_path: str,
            file_path: str,
            create_parents: bool = True,
            overwrite: bool = True,
            verify: bool = False,
            progress_bar: bool = True
        ) -> tuple[int, dict[str, object]]:
        """Upload a file to a given destination path.
        
            Parameters
            ----------
            dest_path : str
                A destination folder path starting with a shared folder.
            file_path : str
                A file path to be uploaded.
            create_parents : bool, optional
                Create parent folder(s) if none exist. Defaults to `True`
            overwrite : bool, optional
                If `True` overwrite the destination file if one exist else skip the upload if the destination file exist. Defaults to `True`
            verify : bool, optional
                If `True` use HTTPS else use HTTP. Defaults to `False`
            progress_bar : bool, optional
                Enable or note the progress bar in the stdout. Defaults to `True`
        
            Returns
            -------
            tuple[int, dict[str, object]]
                If failed return a tuple with the status code and the error message
                else return the response json
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Upload'
        info = self.gen_list[api_name]
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

    def get_shared_link_info(self, link_id: str) -> dict[str, object]:
        """ Get information of a sharing link by the sharing link ID
        
            Parameters
            ----------
            link_id : str
                A unique ID of a sharing link.
        
            Returns
            -------
            dict[str, object]
                Information about the sharing link
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "date_available": "0", 
                    "date_expired": "0", 
                    "has_password": false, 
                    "id": "pHTBKQf9", 
                    "isFolder": false, 
                    "link_owner": "admin", 
                    "name": "ITEMA_20448251-0.mp3", 
                    "path": "/test/ITEMA_20448251-0.mp3", 
                    "status": "valid", 
                    "url": "http://myds.com:5000/fbsharing/pHTBKQf9"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'getinfo',
            'id': link_id
        }
        return self.request_data(api_name, api_path, req_param)

    def get_shared_link_list(self, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None,
            sort_direction: Optional[str] = None, force_clean: Optional[bool] = None
        ) -> dict[str, object]:
        """List user's file sharing links
        
            Parameters
            ----------
            offset : Optional[int], optional
                Specify how many sharing links are skipped before beginning to return listed sharing links. Defaults to `None`
            limit : Optional[int], optional
                Number of sharing links requested. 0 means to list all sharing links. Defaults to `None`
            Specify which file information to sort on. Defaults to `None`
                All fields known are: `["name","isFolder","path","date_expired","date_available","status","has_password","id","url","link_owner"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `None`
                All possible direction are: `["asc","desc"]`
            force_clean : Optional[bool], optional
                If set to false, the data will be retrieved from cache database rapidly. If set to true, all sharing information including sharing statuses and user name of sharing owner will be synchronized. It consumes some time. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                Information about the sharing links
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "links": [ 
                        { 
                            "date_available": "0", 
                            "date_expired": "0", 
                            "has_password": false, 
                            "id": "pHTBKQf9", 
                            "isFolder": false, 
                            "link_owner": "admin", 
                            "name": "ITEMA_20448251-0.mp3", 
                            "path": "/test/ITEMA_20448251-0.mp3", 
                            "status": "valid", 
                            "url": "http://myds.com:5000/fbsharing/pHTBKQf9" 
                        } 
                    ], 
                    "offset": 0, 
                    "total": 1 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'force_clean': force_clean
        }
        return self.request_data(api_name, api_path, req_param)

    def create_sharing_link(self, path: str | list[str], password: Optional[str] = None, date_expired: Optional[str | int] = None,
            date_available: Optional[str | int] = None
        ) -> dict[str, object]:
        """Generate one or more sharing link(s) by file/folder path(s).
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths with which to generate sharing links.
            password : Optional[str], optional
                The password for the sharing link when accessing it. The max password length are 16 characters. Defaults to `None`
            date_expired : Optional[str  |  int], optional
                The expiration date for the sharing link, written in the format YYYYMM-DD. When set to 0 (default), the sharing link is permanent. Defaults to `None` 
                
                Note: SHOULD put the double quote outside expiration date and is based on user's DS date.
                
            date_available : Optional[str  |  int], optional
                The available date for the sharing link to become effective, written in the format YYYY-MM-DD. When set to 0 (default), the sharing link is valid immediately after creation. Defaults to `None`
                
                Note: SHOULD put the double quote outside available date and is based on user's DS date.
        
            Returns
            -------
            dict[str, object]
                Information about the sharing link(s) generated
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "links": [ 
                        { 
                            "error": 0, 
                            "id": "y4LmvpaX", 
                            "path": "/test/ITEMA_20445972-0.mp3", 
                            "qrcode": "iVBORw0KGgoAAAANSUh...", 
                            "url": "http://myds.com:5000/fbsharing/y4LmvpaX" 
                        } 
                    ] 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'create',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'password': password,
            'date_expired': date_expired,
            'date_available': date_available
        }

        return self.request_data(api_name, api_path, req_param)

    def delete_shared_link(self, link_id: str | list[str]) -> dict[str, object]:
        """Delete one or more sharing links.
        
            Parameters
            ----------
            link_id : str | list[str]
                Unique IDs of file sharing link(s) to be deleted
        
            Returns
            -------
            dict[str, object]
                Returns an empty success response if completed without error; otherwise returns error object array contains failed IDs
        
            Example return
            ----------
            ```json
            {,
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'id': json.dumps(link_id) if isinstance(link_id, list) else link_id
        }

        return self.request_data(api_name, api_path, req_param)

    def clear_invalid_shared_link(self) -> dict[str, object]:
        """Remove all expired and broken sharing links.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'clear_invalid'
        }

        return self.request_data(api_name, api_path, req_param)

    def edit_shared_link(self, link_id: str | list[str], password: Optional[str] = None, date_expired: Optional[str | int] = None,
            date_available: Optional[str | int] = None
        ) -> dict[str, object]:
        """Edit sharing link(s).
        
            Parameters
            ----------
            link_id : str | list[str]
                Unique ID(s) of sharing link(s) to edit.
            password : Optional[str], optional
                The password for the sharing link when accessing it. The max password length are 16 characters. Defaults to `None`
            date_expired : Optional[str  |  int], optional
                The expiration date for the sharing link, written in the format YYYYMM-DD. When set to 0 (default), the sharing link is permanent. Defaults to `None` 
                
                Note: SHOULD put the double quote outside expiration date and is based on user's DS date.
                
            date_available : Optional[str  |  int], optional
                The available date for the sharing link to become effective, written in the format YYYY-MM-DD. When set to 0 (default), the sharing link is valid immediately after creation. Defaults to `None`
                
                Note: SHOULD put the double quote outside available date and is based on user's DS date.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Sharing'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'edit',
            'id': json.dumps(link_id) if isinstance(link_id, list) else link_id,
            'password': password,
            'date_expired': date_expired,
            'date_available': date_available
        }
        return self.request_data(api_name, api_path, req_param)

    def create_folder(self, folder_path: str | list[str], name: str | list[str], 
            force_parent: Optional[bool] = False, additional: Optional[str | list[str]] = None
        ) -> dict[str, object]:
        """Create folders.
        
            Parameters
            ----------
            folder_path : str | list[str]
                One or more shared folder paths, separated by commas and around brackets.
                If `force_parent` is `true`, and `folder_path`  does not exist, the `folder_path` will be created.
                If `force_parent` is `false`, `folder_path` must exist or a false value will be returned. 
                The number of paths must be the same as the number of names in the name parameter.
                The first `folder_path` parameter corresponds to the first name parameter.
            name : str | list[str]
                One or more new folder names. 
                The number of names must be the same as the number of folder_paths paths in the `folder_path` parameter.
                The first `name` parameter corresponding to the first `folder_path` parameter.
            force_parent : Optional[bool], optional
                Defaults to `False`.
                If `true` : no error occurs if a folder exists and create parent folders as needed.
                If `false` : parent folders are not created.
            additional : Optional[str  |  list[str]], optional
                Additionnal field to retrieve from folder. Defaults to `None`
                All fields known are: `["real_path","size","owner","time","perm","type"]`.
        
            Returns
            -------
            dict[str, object]
                List of folder(s) created informations.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "folders": [ 
                        { 
                            "isdir": true, 
                            "name": "test", 
                            "path": "/video/test" 
                        } 
                    ]
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.CreateFolder'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'create',
            'folder_path': json.dumps(folder_path) if isinstance(folder_path, list) else folder_path,
            'name': json.dumps(name) if isinstance(name, list) else name,
            'force_parent': force_parent
        }
        return self.request_data(api_name, api_path, req_param)

    def rename_folder(self, path: str | list[str], name: str | list[str], additional: Optional[str | list[str]] = None, search_taskid: Optional[str] = None) -> dict[str, object]:
        """Rename folders.
        
            Parameters
            ----------
            path : str | list[str]
                One or more paths of files/folders to be renamed.
                The number of paths must be the same as the number of names in the `name` parameter.
                The first `path` parameter corresponds to the first `name` parameter.
            name : str | list[str]
                One or more new folder names. 
                The number of names must be the same as the number of paths paths in the `path` parameter.
                The first `name` parameter corresponding to the first `path` parameter.
            additional : Optional[str  |  list[str]], optional
                Defaults to `None`
                Additionnal field to retrieve from folder.
                All fields known are: `["real_path","size","owner","time","perm","type"]`.
            search_taskid : Optional[str], optional
                The task ID of the `search_start` method. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                List of folder(s) renamed informations.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "files": [ 
                        { 
                            "isdir": true, 
                            "name": "test", 
                            "path": "/video/test" 
                        } 
                    ]
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.Rename'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'rename',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'name': json.dumps(name) if isinstance(name, list) else name,
            'search_taskid': search_taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def start_copy_move(self,
            path: str | list[str],
            dest_folder_path: str,
            overwrite: Optional[bool] = None,
            remove_src: Optional[bool] = False,
            accurate_progress: Optional[bool] = True,
            search_taskid: Optional[str] = None
        ) -> dict[str, object]:
        """Start to copy/move files.
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths starting with a shared folder to copy/move.
            dest_folder_path : str
                A destination folder path where files/folders are copied/moved.
            overwrite : Optional[bool], optional
                Defaults to `None`.
                If `true` : overwrite all existing files with the same name.
                If `false` : skip all existing files with the same name.
                
                Note: do not overwrite or skip existed files. If there is any existing files, an error occurs (error code: 1003).
                
            remove_src : Optional[bool], optional
                Defaults to `False`.
                If `true`: move files/folders. If `false`: copy files/folders.
            accurate_progress : Optional[bool], optional
                Defaults to `True`.
                If `true` : calculate the progress by each moved/copied file within sub-folder.
                If `false` : calculate the progress by files which you give in path parameters. This calculates the progress faster, but is less precise.
            search_taskid : Optional[str], optional
                The task ID of the `search_start` method. Defaults to `None`.
        
            Returns
            -------
            dict[str, object]
                Return unique task ID for the copy/move task.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "FileStation_51D00B7912CDE0B0"
                },
                "success": true
            }
            ```
        """
        
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'dest_folder_path': dest_folder_path,
            'overwrite': overwrite,
            'remove_src': remove_src,
            'accurate_progress': accurate_progress,
            'search_taskid': search_taskid
        }

        return self.request_data(api_name, api_path, req_param)

    def get_copy_move_status(self, taskid: str) -> dict[str, object]:
        """ Get the copying/moving status.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the copy/move task which is obtained from `start_copy_move` method
        
            Returns
            -------
            dict[str, object]
                Infos about the copy/move task
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "dest_folder_path": "/video/test", 
                    "finished": false, 
                    "path": "/video/test.avi", 
                    "processed_size": 1057, 
                    "progress": 0.01812258921563625, 
                    "total": 58325 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def stop_copy_move_task(self, taskid: str) -> dict[str, object]:
        """ Stop a copy/move task
        
            Parameters
            ----------
            taskid : str
                A unique ID for the copy/move task which is obtained from `start_copy_move` method
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.CopyMove'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def start_delete_task(self,
            path: str | list[str],
            accurate_progress: Optional[bool] = True,
            recursive: Optional[bool] = True,
            search_taskid: Optional[str] = None
        ) -> dict[str, object]:
        """ Delete file(s)/folder(s). This is a non-blocking method. You should poll a request with `get_delete_status` method to get the task status or stop the task with `stop_delete_task` method.
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths starting with a shared folder to delete.
            accurate_progress : Optional[bool], optional
                Defaults to `True`
                If `true` : calculates the progress of each deleted file with the sub-folder recursively.
                If `false` : calculates the progress of files which you give in `path` parameters. The latter is faster than recursively, but less precise.
                Note: Only non-blocking methods suits using the `get_delete_status` method to get progress.
            recursive : Optional[bool], optional
                Defaults to `True`.
                If `true` : delete files/folders recursively.
                If `false` : Only delete first-level file/folder. If a deleted folder contains any file, an error occurs because the folder can't be directly deleted.
            search_taskid : Optional[str], optional
                A unique ID for the search task which is obtained from `search_start` method. It's used to delete the file in the search result. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                A unique task ID for the delete task.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "FileStation_51CEC9C979340E5A"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'accurate_progress': accurate_progress,
            'recursive': recursive,
            'search_taskid': search_taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def get_delete_status(self, taskid: str) -> dict[str, object]:
        """ Get the deleting status.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the delete task which is obtained from `start_delete_task` method.
        
            Returns
            -------
            dict[str, object]
                Infos about the delete task.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "finished": false, 
                    "path": "/video/1000", 
                    "processed_num": 193, 
                    "processing_path": "/video/1000/509", 
                    "progress": 0.03199071809649467, 
                    "total": 6033 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def stop_delete_task(self, taskid: str) -> dict[str, object]:
        """Stop a delete task.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the delete task which is obtained from `start_delete_task` method.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def delete_delete_task(self, path: str | list[str], recursive: Optional[bool] = True, search_taskid: Optional[str] = None) -> dict[str, object]:
        """ Delete files/folders. This is a blocking method. The response is not returned until the deletion operation is completed.
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths starting with a shared folder to delete.
            recursive : Optional[bool], optional
                Defaults to `True`.
                If `true` : Recursively delete files within a folder.
                If `false` : Only delete first-level file/folder. If a deleted folder contains any file, an error occurs because the folder can't be directly deleted.
            search_taskid : Optional[str], optional
                A unique ID for the search task which is obtained from `search_start` method. It's used to delete the file in the search result. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Delete'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'delete',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'recursive': recursive,
            'search_taskid': search_taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def start_extract_task(self, file_path: str, dest_folder_path: str, overwrite: Optional[bool] = False, 
            keep_dir: Optional[bool] = True, create_subfolder: Optional[bool] = False, codepage: Optional[str] = None,
            password: Optional[str] = None, item_id: Optional[str | list[str]] = None
        ) -> dict[str, object]:
        """Start to extract an archive. This is a non-blocking method. You should poll a request with `get_extract_status` method to get the task status or stop the task with `stop_extract_task` method.
        
            Parameters
            ----------
            file_path : str
                A file path of an archive to be extracted, starting with a shared folder
            dest_folder_path : str
                A destination folder path starting with a shared folder to which the archive will be extracted.
            overwrite : Optional[bool], optional
                Whether or not to overwrite if the extracted file exists in the destination folder. Defaults to `False`
            keep_dir : Optional[bool], optional
                Whether to keep the folder structure within an archive. Defaults to `True`
            create_subfolder : Optional[bool], optional
                Whether to create a subfolder with an archive name which archived files are extracted to. Defaults to `False`
            codepage : Optional[str], optional
                The language codepage used for decoding file name with an archive. Defaults to `None`
                All fields known are: `["enu","cht","chs","krn","ger","fre","ita","spn","jpn","dan","nor","sve","nld","rus","plk","ptb","ptg","hun","trk","csy"]`
            password : Optional[str], optional
                The password for extracting the file. Defaults to `None`
            item_id : Optional[str | list[str]], optional
                Item IDs of archived files used for extracting files within an archive. Item IDs could be listed by requesting the `get_file_list_of_archive` method. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                Unique task ID for the extract task.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "FileStation_51CBB59C68EFE6A3"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'file_path': file_path,
            'dest_folder_path': dest_folder_path,
            'overwrite': overwrite,
            'keep_dir': keep_dir,
            'create_subfolder': create_subfolder,
            'codepage': codepage,
            'password': password,
            'item_id': json.dumps(item_id) if isinstance(item_id, list) else item_id
        }
        return self.request_data(api_name, api_path, req_param)['data']['taskid']

    def get_extract_status(self, taskid: str) -> dict[str, object]:
        """Get the extract task status
        
            Parameters
            ----------
            taskid : str
                A unique ID for the extract task which is obtained from `start_extract_task` method
        
            Returns
            -------
            dict[str, object]
                Information about the extract task
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "dest_folder_path": "/download/download", 
                    "finished": false, 
                    "progress": 0.1 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def stop_extract_task(self, taskid: str) -> dict[str, object]:
        """Stop the extract task
        
            Parameters
            ----------
            taskid : str
                A unique ID for the extract task which is obtained from `start_extract_task` method
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def get_file_list_of_archive(self, file_path: str, offset: Optional[int] = 0, limit: Optional[int] = -1, 
            sort_by: Optional[str] = 'name', sort_direction: Optional[str] = 'asc', codepage: Optional[str] = None,
            password: Optional[str] = None, item_id: Optional[str] = None
        ) -> dict[str, object]:
        """ List archived files contained in an archive
        
            Parameters
            ----------
            file_path : str
                An archive file path starting with a shared folder to list.
            offset : Optional[int], optional
                Specify how many archived files are skipped before beginning to return listed archived files in an archive. Defaults to `0`.
            limit : Optional[int], optional
                Number of archived files requested. -1 indicates in an archive to list all archived files. Defaults to `-1`.
            sort_by : Optional[str], optional
                Specify which archived file information to sort on. Defaults to `'name'`
                All fields known are: `["name","size","pack_size","mtime"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `'asc'`
                All possible direction are: `["asc","desc"]`.
            codepage : Optional[str], optional
                The language codepage used for decoding file name with an archive. Defaults to `None`
                All fields known are: `["enu","cht","chs","krn","ger","fre","ita","spn","jpn","dan","nor","sve","nld","rus","plk","ptb","ptg","hun","trk","csy"]`
            password : Optional[str], optional
                The password for extracting the file.. Defaults to `None`
            item_id : Optional[str], optional
                Item ID of an archived folder to be listed within an archive. (None) or -1 will list archive files in a root folder within an archive. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                Information about the archived files
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "items": [ 
                        { 
                            "is_dir": false, 
                            "item_id": 1, 
                            "mtime": "2013-02-03 00:17:12", 
                            "name": "ITEMA_20445972-0.mp3", 
                            "pack_size": 51298633, 
                            "path": "ITEMA_20445972-0.mp3", 
                            "size": 51726464 
                        }, 
                        { 
                            "is_dir": false, 
                            "item_id": 0, 
                            "mtime": "2013-03-03 00:18:12", 
                            "name": "ITEMA_20455319-0.mp3", 
                            "pack_size": 51434239, 
                            "path": "ITEMA_20455319-0.mp3", 
                            "size": 51896448 
                        } 
                    ], 
                    "total":2 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Extract'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'file_path': file_path,
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'codepage': codepage,
            'password': password,
            'item_id': item_id
        }
        return self.request_data(api_name, api_path, req_param)

    def start_file_compression(self, path: str | list[str], dest_file_path: str, level: Optional[int] = 'moderate', 
            mode: Optional[str] = 'add', format: Optional[str] = 'zip', password: Optional[str] = None
        ) -> dict[str, object] | tuple[str]:
        """Start to compress file(s)/folder(s).
        
            Parameters
            ----------
            path : str | list[str]
                One or more file paths to be compressed, starting with a shared folder.
            dest_file_path : str
                A destination file path (including file name) of an archive for the compressed archive.
            level : Optional[int], optional
                Defaults to `'moderate'`.
                Compress level used, could be one of following values:
                - `moderate`: moderate compression and normal compression speed.
                - `store`: pack files with no compress. fastest: fastest compression speed but less compression.
                - `best`: slowest compression speed but optimal compression.
            mode : Optional[str], optional
                Defaults to `'add'`
                Compress mode used, could be one of following values:
                - `add`: Update existing items and add new files. If an archive does not exist, a new one is created.
                - `update`: Update existing items if newer on the file system and add new files. If the archive does not exist create a new archive.
                - `refreshen`: Update existing items of an archive if newer on the file system. Does not add new files to the archive.
                - `synchronize`: Update older files in the archive and add files that are not already in the archive.
            format : Optional[str], optional
                The compress format, ZIP or 7z format. Defaults to `'zip'`
                All fields known are: `["zip","7z"]`
            password : Optional[str], optional
                The password for the archive. Defaults to `None`
        
            Returns
            -------
            dict[str, object] | tuple[str]
                Unique task ID for the compress task.
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "taskid": "FileStation_51CBB25CC31961FD"
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'start',
            'path': json.dumps(path) if isinstance(path, list) else path,
            'dest_file_path': dest_file_path,
            'level': level,
            'mode': mode,
            'format': format,
            'password': password
        }
        return self.request_data(api_name, api_path, req_param)

    def get_compress_status(self, taskid: str) -> dict[str, object]:
        """ Get the compress task status
        
            Parameters
            ----------
            taskid : str
                A unique ID for the compress task. This is obtained from `start_file_compression` method.
        
            Returns
            -------
            dict[str, object]
                Information about the compress task
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "dest_file_path": "/download/download.zip", 
                    "finished": true 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'status',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def stop_compress_task(self, taskid: str) -> dict[str, object]:
        """Stop the compress task.
        
            Parameters
            ----------
            taskid : str
                A unique ID for the compress task. This is obtained from `start_file_compression` method.
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.Compress'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'stop',
            'taskid': taskid
        }
        return self.request_data(api_name, api_path, req_param)

    def get_list_of_all_background_task(self, offset: Optional[int] = 0, limit: Optional[int] = 0, 
            sort_by: Optional[str] = 'crtime', sort_direction: Optional[str] = 'asc', api_filter: Optional[str | list[str]] = None
        ) -> dict[str, object]:
        """List all background tasks including copy, move, delete, compress and extract tasks.
        
            Parameters
            ----------
            offset : Optional[int], optional
                Specify how many background tasks are skipped before beginning to return listed background tasks. Defaults to `0`
            limit : Optional[int], optional
                Number of background tasks requested. 0 indicates to list all background tasks. Defaults to `0`
            sort_by : Optional[str], optional
                Specify which information of the background task to sort on. Defaults to `'crtime'`
                All fields known are: `["crtime","finished"]`
            sort_direction : Optional[str], optional
                Specify to sort ascending or to sort descending. Defaults to `'asc'`
                All possible direction are: `["asc","desc"]`
            api_filter : Optional[str  |  list[str]], optional
                List background tasks with one or more given API name(s). If not given, all background tasks are listed. Defaults to `None`
                All fields known are: `["SYNO.FileStation.CopyMove","SYNO.FileStation.Delete","SYNO.FileStation.Compress","SYNO.FileStation.Extract"]`
        
            Returns
            -------
            dict[str, object]
                List of background tasks
        
            Example return
            ----------
            ```json
            {
                "data": {
                    "tasks": [ 
                        { 
                            "api": "SYNO.FileStation.CopyMove", 
                            "crtime": 1372926088, 
                            "finished": true, 
                            "method": "start", 
                            "params": { 
                                "accurate_progress": true, 
                                "dest_folder_path": "/video/test", 
                                "overwrite": true, 
                                "path": [ 
                                    "/video/test2/test.avi" 
                                ], 
                                "remove_src": false 
                            }, 
                            "path": "/video/test2/test.avi", 
                            "processed_size": 12800, 
                            "processing_path": "/video/test2/test.avi", 
                            "progress": 1, 
                            "taskid": "FileStation_51D53088860DD653", 
                            "total": 12800, 
                            "version": 1 
                        }, 
                        { 
                            "api": "SYNO.FileStation.Compress", 
                            "crtime": 1372926097, 
                            "finished": true, 
                            "method": "start", 
                            "params": { 
                                "dest_file_path": "/video/test/test.zip", 
                                "format": "zip", 
                                "level": "", 
                                "mode": "", 
                                "password": "", 
                                "path": [ 
                                    "/video/test/test.avi" 
                                ] 
                            }, 
                            "progress": 0, 
                            "taskid": "FileStation_51D53091A82CD948", 
                            "total": -1, 
                            "version": 1 
                        }, 
                        { 
                            "api": "SYNO.FileStation.Extract", 
                            "crtime": 1372926103, 
                            "finished": true, 
                            "method": "start", 
                            "params": { 
                                "create_subfolder": false, 
                                "dest_folder_path": "/video/test", 
                                "file_path": [ 
                                    "/video/test/test.zip" 
                                ], 
                                "keep_dir": true, 
                                "overwrite": false 
                            }, 
                            "progress": 1, 
                            "taskid": "FileStation_51D530978633C014", 
                            "total": -1, 
                            "version": 1 
                        }, 
                        { 
                            "api": "SYNO.FileStation.Delete",
                            "crtime": 1372926110, 
                            "finished": true, 
                            "method": "start", 
                            "params": { 
                                "accurate_progress": true, 
                                "path": [ 
                                    "/video/test/test.avi" 
                                ] 
                            }, 
                            "path": "/video/test/test.avi", 
                            "processed_num": 1, 
                            "processing_path": "/video/test/test.avi", 
                            "progress": 1, 
                            "taskid": "FileStation_51D5309EE1E10BD9", 
                            "total": 1, 
                            "version": 1 
                        } 
                    ], 
                    "offset": 0, 
                    "total": 4 
                },
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.BackgroundTask'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'list',
            'offset': offset,
            'limit': limit,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'filter': json.dumps(api_filter) if isinstance(api_filter, list) else api_filter
        }
        return self.request_data(api_name, api_path, req_param)
    
    def clear_all_finished_background_task(self, taskid: Optional[str | list[str]] = None) -> dict[str, object]:
        """Delete all finished background tasks.
        
            Parameters
            ----------
            taskid : Optional[str  |  list[str]], optional
                Unique IDs of finished copy, move, delete, compress or extract tasks. If it's not given, all finished tasks are deleted. Defaults to `None`
        
            Returns
            -------
            dict[str, object]
                No specific response. It returns an empty success response if completed without error.
        
            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """
        api_name = 'SYNO.FileStation.BackgroundTask'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['maxVersion'],
            'method': 'clear_finished',
            'taskid': json.dumps(taskid) if isinstance(taskid, list) else taskid
        }
        return self.request_data(api_name, api_path, req_param)
    
    def get_file(self, path: str | list[str], mode: str, dest_path: str = ".", chunk_size: int = 8192, verify: bool = False) -> Optional[io.BytesIO]:
        """Download a file
        
            Parameters
            ----------
            path : str | list[str]
                One or more file/folder paths starting with a shared folder to be downloaded. When more than one file is to be downloaded, files/folders will be compressed as a zip file.
            mode : str
                Mode used to download files/folders, value could be: 
                - `open`: print the file content to stdout
                - `download`: write the file content to a file based on the `dest_path` parameter
                - `serve`: return the file content as a stream
            dest_path : str, optional
                Destination folder where the file is downloaded, if mode is `download`. Defaults to `"."`
            chunk_size : int, optional
                Size of chunk to download. Defaults to `8192`
            verify : bool, optional
                If `True` use HTTPS else use HTTP. Defaults to `False`
        
            Returns
            -------
            Optional[io.BytesIO]
                If mode is `serve`, return the file content as a stream
        
        """
        api_name = 'SYNO.FileStation.Download'
        info = self.gen_list[api_name]
        api_path = info['path']

        session = requests.session()
        str_path: str = json.dumps(path) if isinstance(path, list) else path 
        url = ('%s%s' % (self.base_url, api_path)) + '?api=%s&version=%s&method=download&path=%s&mode=%s&_sid=%s' % (
            api_name, info['maxVersion'], str_path, mode, self._sid)

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
                    
                if isinstance(path, list):
                    if len(path) > 1:
                        file_name = f"{os.path.splitext(os.path.basename(path[0]))[0]}.zip"
                    else:
                        file_name = os.path.basename(path[0])
                else:
                    file_name = os.path.basename(path)
                with open(dest_path + "/" + file_name, 'wb') as f:
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
                Instance of the Tree of lib "Treelib", this will be modified by the method
        
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
    
