# pylint: disable=line-too-long, too-many-lines
"""
Synology Photo access (via Synology APIs DSM 7)

    - class Photos : the API
    - class DatePhoto : facilities for timestamps in API

"""
from __future__ import annotations
from pathlib import PurePosixPath
from typing import Optional, Any
import json
from datetime import datetime, timedelta
import pytz
from . import base_api
from .exceptions import PhotosError, APIError


# error code when raising PhotosError from this file
API_ERROR = 1212


class Photos(base_api.BaseApi):
    """Implements access to APIs Synology Photo (DSM 7)

    ### Notes :

    - Some methods take a `team` parameter for specify the space to work on :

        * in personal space when False
        * in shared space when True

    - Most methods use **kwargs to pass no mandatory attributes to API. Example with list_albums(**kwargs)  :
        ``` python
        albums = synofoto.list_albums(limit=10, sort_by='album_name', sort_direction='asc')
        ```

    - The maximum for "limit" argument is 5000, greater value raise PhotosError

    ## Methods available
    ### General methods
    * get_userinfo
    * get_admin_settings
    * get_guest_settings

    #### methods on folders
    * list_folders
    * count_folders
    * lookup_folder
    * get_folder
    * photos_in_folder
    * count_photos_in_folder
    * share_team_folder

    #### methods on albums
    * list_albums
    * get_albums
    * count_albums
    * count_photos_in_album
    * suggest_condition
    * create_normal_album
    * delete_album
    * add_photos_to_album
    * delete_photos_from_album
    * delete_conditional_album
    * set_album_condition
    * share_album
    * photos_in_album

    * list_shareable_users_and_groups

    #### methods on filters
    * count_photos_with_filter
    * photos_with_filter
    * list_search_filters

    #### methods on photos
    * photos_from_ids
    * photo_download
    * thumbnail_download

    #### methods on keywords (search in geolocalisation address, filename, description, identifier, ...?)
    * count_photos_with_keyword
    * photos_with_keyword

    #### methods on tags (search in geolocalisation address, filename, description, identifier, ...?)
    * count_general_tags
    * general_tags
    * general_tag
    * count_photos_with_tag
    * photos_with_tag

    #### methods on timeline
    * get_timeline
    * photos_with_timeline

    ## `additional` attribute
    Some extra informations can be retrieve by using `additional` in various methods.

    `additional` is a list of string defining informations to retrieve and passed via **kwargs to methods.

    It can be, depending of method type, a list in :
        "access_permission", "sharing_info", "thumbnail", "resolution", "orientation", "video_convert",
        "video_meta", "address", "provider_user_id", "exif", "tag", "description", "gps", "geocoding_id",
        "rating", "motion_photo", "person"

    ## `sort_by` attribute
    * for photos list, value in :
        "filename": file name
        "filesize": file size
        "takentime": time of taking image
        "item_type": type of the item (photo, video, motionphoto, live, photo360, video360, burst)
    * for albums list :
        * in ["album_name", "album_type", "start_time", "create_time", "share_status"],

    ## Structures returned
    ### Photo structure
        ```json
        {
        "filename":"IMG_20210723_201314.JPG",
        "filesize":13078975,
        "folder_id":1989,
        "id":80716,
        "indexed_time":1633867030761,
        "owner_user_id":2,
        "time":1627071194,
        "type":"photo"
        },
        ```

    ### Folder structure
        ```json
        {
        "additional": {
            "access_permission": {
                "download": true,
                "manage": true,
                "own": true,
                "upload": true,
                "view": true
            },
            "thumbnail": []
        },
        "id": 624,
        "name": "/Saint-Cyr-La-Rosi\u00e8re",
        "owner_user_id": 0,
        "parent": 1,
        "passphrase": "",
        "shared": false,
        "sort_by": "default",
        "sort_direction": "default"
        }
        ```


    ### Album structure
        ``` json
        {
        "cant_migrate_condition":{},
        "condition":{},
        "create_time":1633947628,
        "end_time":1631815585,
        "freeze_album":false,
        "id":8,
        "item_count":3,
        "name":"My Album Name",
        "owner_user_id":2,
        "passphrase":"",
        "shared":false,
        "sort_by":"default",
        "sort_direction":"default",
        "start_time":1631387203,
        "temporary_shared":false,
        "type":"normal",
        "version":442042
        },
        ```

    ### Filter structure
        ``` json
        {
            "aperture":[
                { "id":25, "name":"F1.8"},
            ],
            "camera":[
                { "id":14, "name":"NIKON D5500" },
            ],
            "exposure_time_group":[
                {
                    "start": {"den":1, "num":0}
                    "end": {"den":3000, "num":1},
                },
            ],
            "flash":[0, 16, 24 ],
            "focal_length_group":[
                { "end":22, "start":0},
            ],
            "folder_filter":[
                {
                    "id":1990,
                    "name":"/myfolder2",
                    "owner_user_id":2,
                    "parent":74,
                    "passphrase":"",
                    "shared":false,
                    "sort_by":"default",
                    "sort_direction":"default"
                }
            ],
            "general_tag":[
                {"id":1273, "name":"2021"},
            ],
            "geocoding":[
                {
                    "children":[
                    {
                        "children":[

                        ],
                        "id":227,
                        "level":4,
                        "name":"Eastern Region"
                    }
                    ],
                    "id":225,
                    "level":1,
                    "name":"Iceland"
                },
        ...

            ],
            "iso":[
                {"id":52, "name":"16"},
        ...
            ],
            "item_type":[
                {"id":0, "name":"photo"},
                {"id":1, "name":"video"},
                {"id":1, "name":"photo360"},
            ],
            "lens":[
                {
                    "id":7,
                    "name":"Nikon AF-S DX Nikkor 18-140mm f/3.5-5.6G ED VR"
                },
        ...
            ],
            "person":[
                {
                    "cover":7,
                    "id":1,
                    "item_count":7,
                    "name":"Mister X",
                    "show":true
                }
            ],
            "time":[
                {
                    "end_time":1633046399,
                    "month":9,
                    "start_time":1630454400,
                    "year":2021
                },
        ...
            ]
        },
        ```

    ### Tags structure
        ```json
            [
                {
                    "id": 21,
                    "item_count": 4791,
                    "name": "Person"
                },
                {
                    "id": 7,
                    "item_count": 576,
                    "name": "Music"
                }
            ]
        ```

    ### Timeline Section structure
        ```json
            {
            "limit": 104,
            "list": [
                {
                    "day": 14,
                    "item_count": 34,
                    "month": 7,
                    "year": 2023
                },
                {
                    "day": 3,
                    "item_count": 2,
                    "month": 6,
                    "year": 2023
                },
            ],
            "offset": 0
        }
        ```
    """

    def __init__(
        self,
        ip_address: str,
        port: str,
        username: str,
        password: str,
        secure: bool = False,
        cert_verify: bool = False,
        dsm_version: int = 7,
        debug: bool = True,
        otp_code: Optional[str] = None,
    ) -> None:
        """Constructor : Login in Synology Photo"""
        super(Photos, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                     dsm_version, debug, otp_code)

        self.session.get_api_list('Foto')

        self.request_data: Any = self.session.request_data
        self.photos_list: Any = self.session.app_api_list
        self.base_url: str = self.session.base_url

        self._userinfo: Any = None
        self._tags = {False: None, True: None}
        self.avail_filters = {False: None, True: None}

    def logout(self) -> None:
        """Logout from Synology Photo API"""
        self.session.logout("Foto")

    def _request_data(
        self,
        api_name: str,
        req_param: dict[str, object],
        method: Optional[str] = None,
        response_json: bool = True,
    ) -> dict[str, object] | str | list | object:
        """internal generic request data"""
        info = self.photos_list[api_name]
        req_param["version"] = info["maxVersion"]

        # convert to json data
        for k, v in req_param.items():
            if isinstance(v, bool):
                req_param[k] = str(v).lower()
            if isinstance(v, list) or isinstance(v, dict):
                req_param[k] = json.dumps(v)

        return self.request_data(api_name, info["path"], req_param, method, response_json)

    def get_userinfo(self) -> dict[str, object]:
        """Get logged user info

        ### Typical return :
            ``` json
            {
                "enabled": true,
                "id": 1,
                "is_admin": true,
                "is_migration_finished": true,
                "name": "My Name",
                "profile": {
                    "email": "itsme@email.com",
                    "emails": [
                        "itsme@email.com"
                    ],
                    "groups": null,
                    "id": "9f517c9f-77b3-4799-9bc7-6891dabfe9c7",
                    "nickName": "",
                    "photo": "",
                    "preferredColor": "#94bf13",
                    "preferredLanguage": "def",
                    "timezone": "Amsterdam",
                    "timezoneUI": "def",
                    "title": "User",
                    "uid": 1027,
                    "userName": "Me"
                },
                "uid": 1050
            }
            ```
        """
        if self._userinfo is not None:
            return self._userinfo

        req_param = {"method": "me"}
        self._userinfo = self._request_data("SYNO.Foto.UserInfo", req_param)
        return self._userinfo

    def _count(self, api_name: str, **kwargs) -> int:
        """internal generic count"""
        req_param = dict({"method": "count"}, **kwargs)
        return self._request_data(api_name, req_param)["data"]["count"]

    def _method_list(self, api_name, http_method="post", **kwargs) -> dict[str, object]:
        """internal generic list"""
        req_param = dict(**kwargs)
        if "method" not in req_param:
            req_param["method"] = "list"
        if "offset" not in req_param:
            req_param["offset"] = 0
        if "limit" not in req_param:
            req_param["limit"] = 1000
        if "sort_by" not in req_param:
            req_param["sort_by"] = "filename"
        if "sort_direction" not in req_param:
            req_param["sort_direction"] = "desc"
        return self._request_data(api_name, req_param, method=http_method)

    #
    # methods on folder
    #

    def get_folder(self, folder_id: int = 0, team: bool = False, **kwargs) -> dict[str, object]:
        """Get folder description.
        Return root folder for space when folder_id=0 or omitted
        ### Parameter
            folder_id : folder identifier.
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
          folder dict
        """
        api_name = "SYNO.FotoTeam.Browse.Folder" if team else "SYNO.Foto.Browse.Folder"
        req_param = dict({"method": "get", "id": folder_id}, **kwargs)
        return self._request_data(api_name, req_param)["data"]["folder"]

    def list_folders(self, folder_id: int, team: bool = False, **kwargs) -> list[dict[str, object]]:
        """List sub-folders in folder
        ### Parameter
            folder_id : folder identifier
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
          list of folder dict
        """
        api_name = "SYNO.FotoTeam.Browse.Folder" if team else "SYNO.Foto.Browse.Folder"
        req_param = dict({"id": folder_id}, **kwargs)
        return self._method_list(api_name, http_method="post", **req_param)["data"]["list"]

    def count_folders(self, folder_id: int = 0, team: bool = False) -> int:
        """Count sub-folders in folder
        ### Parameter
            folder_id : folder identifier
            team : personal or shared space
        ### Return
          folders count
        """
        api_name = "SYNO.FotoTeam.Browse.Folder" if team else "SYNO.Foto.Browse.Folder"
        return self._count(api_name, id=folder_id)

    def lookup_folder(self, path: str, root_folder: int = 0, team: bool = False, **kwargs) -> dict[str, object] | None:
        """Lookup for folder
        ### Parameter
            path : path to lookup
            root_folder : starting folder id for lookup
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
          folder dict or None
        """
        if root_folder == 0 and path == "/":
            return self.get_folder(root_folder, team=team, **kwargs)
        if root_folder != 0:
            if path.startswith("/"):
                path = path[1:]
            folder = self.get_folder(root_folder, team=team)
            path = str(PurePosixPath(folder["name"]).joinpath(path))
        parent = 0
        found_path = ""
        folder = ""
        for part in path.strip("/").split("/"):
            count = self.count_folders(parent, team)
            for offset in range(0, count, 1000):
                kwargs["offset"] = offset
                folders_response = self.list_folders(parent, team, **kwargs)
                folder = next(
                    filter(
                        lambda elem: elem["name"] == f"{found_path}/{part}",
                        folders_response,
                    ),
                    None,
                )
                if folder:
                    parent = folder["id"]
                    found_path = folder["name"]
                    break
            else:
                return
        return folder

    def count_photos_in_folder(self, folder_id: int, team: bool = False) -> int:
        """Count items in folder
        ### Parameters
            folder_id : folder identifier
            team : personal or shared space
        ### Return
          photos count
        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        return self._count(api_name, folder_id=folder_id)

    def photos_in_folder(self, folder_id: int, team: bool = False, **kwargs) -> list[dict[str, object]]:
        """List photos in folder
        ### Parameters
            folder_id : starting folder id for lookup
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
          list of photo dict
        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        req_param = dict({"folder_id": folder_id}, **kwargs)
        return self._method_list(api_name, http_method="post", **req_param)["data"]["list"]

    #
    # methods on albums
    #

    def get_albums(self, album_ids: int | list[int] | str, **kwargs) -> list[dict[str, object]] | None:
        """Get albums descriptions from identifiers or name
        ### Parameter
            * album_ids :
                * album identifier if type `int`,
                * list of albums identifier if type `list`
                * album name if type `str`
        ### kwargs parameters
            * additional: list in ["sharing_info", "thumbnail", ...]
        ### Return
          albums list or None
        """
        if isinstance(album_ids, str):
            count = self.count_albums()
            for album in self.list_albums(limit=count):
                if album["name"].lower() == album_ids.lower():
                    return [album]
            return None

        req_param = dict(
            {
                "method": "get",
                "id": album_ids if isinstance(album_ids, list) else [album_ids],
            },
            **kwargs,
        )
        return self._request_data("SYNO.Foto.Browse.Album", req_param)["data"]["list"]

    def list_albums(self, **kwargs) -> dict[str, object] | str:
        """Get albums list
        ### kwargs parameters
            offset, limit,

            sort_by : in ["album_name", "album_type", "start_time", "create_time", "share_status"],

            sort_direction: in ["asc", "desc"],

            additional : list in ["sharing_info", "thumbnail", ... ]

            category : in ["normal_share_with_me", "normal", "shared"]

        ### Return
            albums list
        """
        if "sort_by" not in kwargs:
            kwargs["sort_by"] = "album_name"
        return self._method_list("SYNO.Foto.Browse.Album", http_method="post", **kwargs)["data"]["list"]

    def count_albums(self) -> int:
        """Count albums
        ### Return
            albums count
        """
        return self._count("SYNO.Foto.Browse.Album")

    def suggest_condition(
        self,
        keyword: str,
        condition: Optional[list[str]] = None,
        user_id: Optional[str] = None,
    ) -> dict[str, object] | str:
        """suggest album condition"""
        if condition is None:
            condition = ["general_tag"]
        if user_id is None:
            user_id = self.get_userinfo()["data"]["id"]

        req_param = {
            "method": "suggest",
            "user_id": user_id,
            "keyword": keyword,
            "condition": condition,
        }

        return self._request_data("SYNO.Foto.Browse.ConditionAlbum", req_param)

    def create_normal_album(self, name: str, id_photos: list[int] | int) -> dict[str, object]:
        """create normal album (without condition)
        ### Parameter
            * name : album name
            * id_photos : photo or list of photos identifier to add
        ### Return
            a dictionnary {'album': {...}, 'error_list': [...]}
        """
        req_param = {
            "method": "create",
            "name": name,
            "item": [id_photos] if isinstance(id_photos, int) else id_photos,
        }
        return self._request_data("SYNO.Foto.Browse.NormalAlbum", req_param)["data"]

    def add_photos_to_album(self, album_id, id_photos: list[int] | int) -> dict[str, object]:
        """add photos to normal album
        ### Parameter
            * album_id : album identifier
            * id_photos : photo or list of photos identifier to add
        ### Return
             dictionnary {'error_list': [...]}
        """
        req_param = {
            "method": "add_item",
            "id": album_id,
            "item": [id_photos] if isinstance(id_photos, int) else id_photos,
        }
        return self._request_data("SYNO.Foto.Browse.NormalAlbum", req_param)["data"]

    def delete_photos_from_album(self, album_id, id_photos: list[int] | int) -> dict[str, object]:
        """delete photos from normal album
        ### Parameter
            * album_id : album identifier
            * id_photos : photo or list of photos identifier to remove
        ### Return
            {"success" : True|False}
        """
        if isinstance(id_photos, int):
            id_photos = [id_photos]
        req_param = {
            "method": "delete_item",
            "id": album_id,
            "item": [id_photos] if isinstance(id_photos, int) else id_photos,
        }
        return self._request_data("SYNO.Foto.Browse.NormalAlbum", req_param)

    def create_conditional_album(self, name: str, condition: list[str]) -> dict[str, object] | str:
        """create conditional album"""
        req_param = {"method": "create", "name": name, "condition": condition}
        return self._request_data("SYNO.Foto.Browse.ConditionAlbum", req_param)

    def delete_album(self, album_id: list[int] | int) -> dict[str, object] | str:
        """delete album
        ### Parameter
            * album_id : album identifier or list of album identifiers
         ### Return
            {"success" : True|False}
        """
        req_param = {
            "method": "delete",
            "id": [album_id] if isinstance(album_id, int) else album_id,
        }
        return self._request_data("SYNO.Foto.Browse.Album", req_param)

    def set_album_condition(self, folder_id: int, condition: list[str]) -> dict[str, object] | str:
        """set conditions on album"""
        req_param = {
            "method": "set_condition",
            "id": folder_id,
            "condition": json.dumps(condition),
        }
        return self._request_data("SYNO.Foto.Browse.ConditionAlbum", req_param)

    def share_album(
        self,
        album_id: str,
        permission: Optional[str | list[str]] = None,
        enabled: bool = True,
        expiration: int | str = 0,
    ) -> Any:
        """share album"""
        self._share(
            "SYNO.Foto.Sharing.Passphrase",
            policy="album",
            permission=permission,
            album_id=album_id,
            enabled=enabled,
            expiration=expiration,
        )

    def share_team_folder(
        self,
        folder_id: int,
        permission: Optional[str] = None,
        enabled: bool = True,
        expiration: int | str = 0,
    ) -> Any:
        """share folder"""
        self._share(
            "SYNO.FotoTeam.Sharing.Passphrase",
            policy="folder",
            permission=permission,
            folder_id=folder_id,
            enabled=enabled,
            expiration=expiration,
        )

    def _share(
        self,
        api_name: str,
        policy: str,
        permission: str,
        expiration: int | str,
        **kwargs,
    ) -> dict[str, object] | Any:
        """internal share (album/folder)"""
        req_param = {"method": "set_shared", "policy": policy, **kwargs}

        shared_response = self._request_data(api_name, req_param)
        if not shared_response["success"]:
            return

        if not permission:
            return shared_response

        passphrase = shared_response["data"]["passphrase"]

        req_param = {
            "method": "update",
            "passphrase": passphrase,
            "expiration": expiration,
            "permission": json.dumps(permission),
        }
        return self._request_data(api_name, req_param)

    def list_shareable_users_and_groups(self, team_space_sharable_list: bool = False) -> dict[str, object] | str:
        """list shareable users and groups"""
        req_param = {
            "method": "list_user_group",
            "team_space_sharable_list": team_space_sharable_list,
        }

        return self._request_data("SYNO.Foto.Sharing.Misc", req_param)

    def count_photos_in_album(self, album_id: int) -> int:
        """Count photo in an album
        ### Return
            photos count
        """
        return self._count("SYNO.Foto.Browse.Item", album_id=album_id)

    def photos_in_album(self, album_id: int = 0, **kwargs) -> dict[str, object]:
        """List photos in album
        ### Parameter
        * album_id : album identifier
        ### kwargs parameters
            offset, limit,

            id : photo identifiers list (use method `get`)

            sort_by : in ["filename", "filesize", "item_type", "takentime"],

            additional : list in ["sharing_info", "thumbnail", ... ]
        ### Return
            photo list
        """
        req_param = dict({"album_id": album_id}, **kwargs)
        if "id" in req_param:
            req_param["method"] = "get"
        return self._method_list("SYNO.Foto.Browse.Item", http_method="post", **req_param)["data"]["list"]

    #
    # methods on filters
    #

    def count_photos_with_filter(self, folder_id: int, filters: dict[str, object], team: bool = False) -> int:
        """Count photos with filter
        ### Parameter
            folder_id : folder id
            filters : filters
            team : personal or shared space
        ### Return
          photos count
        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        req_param = dict({"folder": [folder_id], "method": "count_with_filter"}, **filters)
        return self._request_data(api_name, req_param, method="post")["data"]["count"]

    def photos_with_filter(
        self, folder_id: int, filters: dict[str, object], team: bool = False, **kwargs
    ) -> dict[str, object]:
        """
        List items with filter in folder
        ### Parameter
            folder_id : folder id
            filters : filters
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_direction, additional

            sort_by : in ["filename", "filesize", "item_type", "takentime"],

            general_tag_policy : in ["or", "and"]. Required if several conditions
        ### Return
            photos list
        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        req_param = dict(
            {
                "method": "list_with_filter",
                "folder": [folder_id],
            },
            **filters,
            **kwargs,
        )
        return self._method_list(api_name, http_method="post", **req_param)["data"]["list"]

    def list_search_filters(
        self,
        settings: dict[str, object] = None,
        folder_id: int = 0,
        team: bool = False,
        **kwargs,
    ) -> list[dict[str, object]]:
        """List Search Filters for folder
        ### Parameters
            * settings : dictionnary of filter categories to retrieve

            Example :
            ```  json
            settings = {
                "focal_length_group":False, "general_tag":True, "iso":True,
                "exposure_time_group":True, "camera":True, "item_type":True,
                "time":False, "aperture":True, "flash":True, "person":False,
                "geocoding":True, "rating":True, "lens":True,
            }
            ```
            * folder_id : folder identifier to work on (0 for all filters from root)
            * team : personal or shared space
        ### kwargs parameters
        ### Return
            filters list
        """
        api_name = "SYNO.FotoTeam.Search.Filter" if team else "SYNO.Foto.Search.Filter"
        if settings:
            kwargs["setting"] = settings
        if folder_id:
            kwargs["folder"] = [folder_id] if isinstance(folder_id, int) else folder_id
        kwargs["method"] = "list"
        return self._request_data(api_name, req_param=kwargs, method="post")["data"]

    #
    # methods on photos
    #

    def photos_from_ids(self, photo_ids: int | list[int], team: bool = False, **kwargs) -> list[dict[str, object]]:
        """Get photos list infos from identifiers
        ### Parameters
            photo_ids : photo identifier, or list of folder identifier
            team : personal or shared space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
            photos list
        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        photo_ids = [photo_ids] if isinstance(photo_ids, int) else photo_ids
        req_param = dict(
            {
                "method": "get",
                "id": photo_ids,
            },
            **kwargs,
        )
        return self._request_data(api_name, req_param)["data"]["list"]

    def photo_download(self, photo_id: int, team: bool | None = None) -> bytes:
        """Download Photo
        ### Parameters
            photo_id : photo identifier
            team : personal or shared space
        ### Return
            Raw image data
        """
        # determine if photo is in personal or shared space
        if team is None:
            team = len(self.photos_from_ids(photo_id, True)) > 0
        api_name = "SYNO.FotoTeam.Download" if team else "SYNO.Foto.Download"
        if isinstance(photo_id, int):
            photo_id = [photo_id]
        req_param = {"method": "download", "unit_id": photo_id}
        try:
            data = self._request_data(api_name, req_param, method="post", response_json=False)
        except PhotosError as _e:
            raise PhotosError(APIError(API_ERROR, f"photo {photo_id} not found")) from _e
        return data.content

    def thumbnail_download(
        self,
        photo_id: int,
        size: str,
        cache_key: str | None = None,
        team: bool | None = None,
    ) -> bytes:
        """Thumbnail Download
        ### Parameters
            * photo_id: photo identifier
            * size: thumbnail size required in ["sm", "m", "xl"]
            * cache_key : None or thumbnail cache_key returned when `additional`=["thumbnail"] is requested in get_photo, photos_in_folder, ...
            * team : None, False for personal space, or True for shared space

        When cache_key or team is None, a call to 'photos_from_ids' is done for determine space and get thumbnail structure.
        ### Return
            Raw image data
        """

        if team is None or cache_key is None:
            cache_key = None
            for team in [False, True]:
                photos = self.photos_from_ids(photo_id, team, additional=["thumbnail"])
                if photos:
                    cache_key = photos[0]["additional"]["thumbnail"]["cache_key"]
                    break
            if not cache_key:
                raise PhotosError(APIError(API_ERROR, f"thumbnail {photo_id} not found"))
        api_name = "SYNO.FotoTeam.Thumbnail" if team else "SYNO.Foto.Thumbnail"
        req_param = {
            "method": "get",
            "id": photo_id,
            "size": size,
            "type": "unit",
            "cache_key": cache_key,
        }
        try:
            data = self._request_data(api_name, req_param, method="post", response_json=False)
        except PhotosError as _e:
            raise PhotosError(API_ERROR, f"thumbnail {photo_id} not found") from _e
        return data.content

    #
    # methods on keywords
    #

    def count_photos_with_keyword(self, keyword: str, team: bool = False) -> int:
        """Count photos with keyword in geolocalisation address, filename, description, identifier, ...
        ### Parameters
            * keyword : keyword to search
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            keyword count
        """
        api_name = "SYNO.FotoTeam.Search.Search" if team else "SYNO.Foto.Search.Search"
        req_param = {"method": "count_item", "keyword": keyword}
        return self._request_data(api_name, req_param, method="post")["data"]["count"]

    def photos_with_keyword(self, keyword: str, team: bool = False, **kwargs) -> dict[str, object]:
        """Search photos with keyword in geolocalisation address, filename, description, identifier, ...

        Warning : the method is case sensitive
        ### Parameters
            * keyword : keyword to search
            * team : space to use: personal (`False`) or shared (`True`) space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
            photo list
        """
        api_name = "SYNO.FotoTeam.Search.Search" if team else "SYNO.Foto.Search.Search"
        req_param = dict({"method": "list_item", "keyword": keyword}, **kwargs)
        return self._method_list(api_name, **req_param)["data"]["list"]

    #
    # methods on tags (=identifiers)
    #

    def _load_tags(self, team: bool = False, force: bool = False):
        """internal load tags"""
        if force or not self._tags[team]:
            self._tags[team] = self.general_tags(team)
        return self._tags[team]

    def count_general_tags(self, team: bool = False) -> int:
        """Count all tags (identifiers)
        ### Parameters
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            tags count
        """
        api_name = "SYNO.FotoTeam.Browse.GeneralTag" if team else "SYNO.Foto.Browse.GeneralTag"
        return self._count(api_name)

    def general_tags(self, team: bool = False, **kwargs) -> list[dict[str, object]]:
        """Get all tags (identifiers)
        ### Parameters
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            * tags list
        ### Typical return

        ``` json
            [
                {
                    "id": 21,
                    "item_count": 4791,
                    "name": "Person"
                },
                {
                    "id": 7,
                    "item_count": 576,
                    "name": "Music"
                }
            ]
        ```
        """
        api_name = "SYNO.FotoTeam.Browse.GeneralTag" if team else "SYNO.Foto.Browse.GeneralTag"
        self._tags[team] = self._method_list(api_name, **kwargs)["data"]["list"]
        return self._tags[team]

    def general_tag(self, tag: int | list[int] | str, team: bool = False, **kwargs) -> list[dict[str, object]] | None:
        """Get specific tag
        ### Parameters
            * tag : tag(s) to retrieve. Can be an id (int), a list of id (int) or a tag name (str)
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            * tags list

        ### Typical return :
        ``` json
            [ {
                "additional": {},
                "id": 192,
                "item_count": 7,
                "name": "Cheval"
            }, ]
        ```
        """
        api_name = "SYNO.FotoTeam.Browse.GeneralTag" if team else "SYNO.Foto.Browse.GeneralTag"

        if isinstance(tag, int):
            tag = [tag]

        if isinstance(tag, str):
            tags = self._load_tags(team)
            for tag_obj in tags:
                if tag_obj["name"].lower() == tag.lower():
                    return [tag_obj]
            return None

        req_param = dict({"method": "get", "id": tag}, **kwargs)
        return self._request_data(api_name, req_param=req_param, method="post")["data"]["list"]

    def count_photos_with_tag(self, tag: str, team: bool = False) -> int:
        """count photos with specific tag
        ### Parameters
            * tag : tag to search
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            * photos count

        """
        tags = self._load_tags(team)
        for tag_obj in tags:
            if tag_obj["name"].lower() == tag.lower():
                return tag_obj["item_count"]
        return 0

    def photos_with_tag(self, tag_name: str, team: bool = False, **kwargs) -> list[dict[str, object]]:
        """get photos list with specific tag
        ### Parameters
            * tag_name : tag to search
            * team : space to use: personal (`False`) or shared (`True`) space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...

            sort_by : in ["filename", "filesize", "item_type", "takentime"],

        ### Return
            * photos list

        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        tags = self.general_tag(tag_name, team)
        if tags is None:
            return []
        req_param = dict({"general_tag_id": tags[0]["id"]}, **kwargs)
        return self._method_list(api_name, http_method="post", **req_param)["data"]["list"]

    def get_admin_settings(self) -> dict[str, object] | str:
        """### Get admin settings
        Typical return:
            ``` json
            {
                "default_thumbnail_size": "sm",
                "display_photo_info_to_guest": true,
                "enable_person": true,
                "enable_user_sharing": true,
                "exclude_extension": []
            },
            ```
        """
        return self._request_data("SYNO.Foto.Setting.Admin", {"method": "get"})

    def get_guest_settings(self) -> dict[str, object] | str:
        """### Get guest settings
        Typical return:
            ``` json
            {
                "alias": "photo",
                "default_thumbnail_size": "sm",
                "display_photo_info_to_guest": true,
                "enable_converted_original_jpeg": false,
                "enable_home_service": true,
                "enable_team_space": true,
                "has_hevc": true
            },
            ```
        """
        return self._request_data("SYNO.Foto.Setting.Guest", {"method": "get"})

    def _load_avail_filters(self, team: bool) -> None:
        """internal load avail filters for space"""
        if self.avail_filters[team] is not None:
            return
        filter_settings = {
            "focal_length_group": True,
            "general_tag": True,
            "iso": True,
            "exposure_time_group": True,
            "camera": True,
            "item_type": True,
            "time": False,
            "aperture": True,
            "flash": True,
            "person": True,
            "geocoding": True,
            "rating": True,
            "lens": True,
        }
        self.avail_filters[team] = self.list_search_filters(filter_settings, team=team)

    def build_filters(self, filters, team=False):
        """Rebuild a filter dictionnary expressed with item names
        ### Parameters
            * filters : filters to process
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            * filter dictionnary directly usable with filter methods
        ### Filter keys
        Filters keys available are "aperture", "camera", "general_tag", "iso", "lens", "item_type", time, geocoding
        * key "time" is a list of periods (start, endtime). Can be tuple[datetime, datetime] or list[tuple[datetime, datetime]].
          Will be replaced by list[int]
        * key "focal_length_group" is a list of focal range (start, end). Can be a tuple[int, int] or list[tuple[int, int]]
        * keys "aperture", "camera", "general_tag", "iso", "lens", "item_type" can be `str` or `list[str]`. Will replaced by `list[int]`
        * keys "flash", "rating" (type list[int]) are modified

        ### Example :
            ```python
            build_filters({
                'rating': [4,5],
                'general_tag':["Beach", "Sun"],
                'camera': ["DSC-RX100M3", "NIKON D7100"],
                'lens': [21, "55.0-300.0 mm f/4.5-5.6"],
                'iso': ["100", "120"],
                'aperture': ["F4.5", "F10",],
                'item_type':"photo",
                'time': [(datetime(2000, 1, 1), datetime(2004,12,31))] },
                team=False)
            ```
            will return :
            ```json
                { "aperture": [13, 11],
                  "camera": [4, 3],
                  "general_tag": [1, 18],
                  "iso": [2, 52],
                  "item_type": [0],
                  "lens": [21, 4],
                  "rating": [4, 5] }
            ```
        """

        def get_code(key: str, value: str, team: bool) -> int | None:
            if isinstance(value, int):
                return value
            self._load_avail_filters(team)
            section = self.avail_filters[team][key]
            for dict_idname in section:
                vname = dict_idname["name"]
                if vname.lower() == value.lower():
                    return dict_idname["id"]
            raise PhotosError(APIError(API_ERROR, f'Incorrect value for filter["{key}"] : {value}'))

        filters = dict(filters)
        for key, values in filters.items():
            if key in ["aperture", "camera", "general_tag", "iso", "lens", "item_type"]:
                if isinstance(values, list):
                    for item in values:
                        if isinstance(item, int):
                            continue
                        id_list = filters[key].index(item)
                        filters[key][id_list] = get_code(key, item, team)
                elif isinstance(values, str):
                    filters[key] = [get_code(key, values, team)]
                elif isinstance(values, int):
                    filters[key] = [values]
                else:
                    raise PhotosError(APIError(
                        API_ERROR,
                        f'Incorrect value type for filter["{key}"] : {type(values).__name__}',
                        )
                    )

            elif key == "time":
                if isinstance(values, list):
                    for index, item in enumerate(values):
                        if isinstance(item, dict):
                            continue  # no check for dict
                        elif isinstance(item, tuple) and len(item) == 2:
                            if isinstance(item[0], datetime) and isinstance(item[1], datetime):
                                filters[key][index] = {
                                    "start_time": int(item[0].timestamp()),
                                    "end_time": int(item[1].timestamp()),
                                }
                            elif isinstance(item[0], int) and isinstance(item[1], int):
                                filters[key][index] = {
                                    "start_time": item[0],
                                    "end_time": item[1],
                                }
                        else:
                            raise PhotosError(APIError(API_ERROR, 'Incorrect value type for filter["time"]'))
                elif (
                    isinstance(values, tuple)
                    and len(values) == 2
                    and isinstance(values[0], datetime)
                    and isinstance(values[1], datetime)
                ):
                    filters[key] = [
                        {
                            "start_time": int(values[0].timestamp()),
                            "end_time": int(values[1].timestamp()),
                        }
                    ]
                else:
                    raise PhotosError(APIError(API_ERROR, 'Incorrect value type for filter["time"]'))

            elif key == "focal_length_group":
                if isinstance(values, tuple) and len(values) == 2:
                    filters[key] = [{"start": values[0], "end": values[1]}]
                elif isinstance(values, list):
                    for index, item in enumerate(values):
                        if isinstance(item, dict):
                            continue  # no check for dict
                        if isinstance(item, tuple) and len(values) == 2:
                            filters[key][index] = {"start": item[0], "end": item[1]}

            elif key in ["exposure_time_group", "geocoding", "person"]:
                # TODO ...
                pass

        return filters

    #
    # timeline methods
    #

    def get_timeline(self, unit: str, team: bool = False, **kwargs) -> list[dict[str, object]]:
        """Get timeline
        ### Parameters
            * unit : group timeline by "day" or "month"
            * team : space to use: personal (`False`) or shared (`True`) space
        ### Return
            * timeline section list

        """
        api_name = "SYNO.FotoTeam.Browse.Timeline" if team else "SYNO.Foto.Browse.Timeline"
        req_param = dict({"timeline_group_unit": unit, "method": "get"}, **kwargs)
        return self._request_data(api_name, req_param, method="post")["data"]["section"]

    def photos_with_timeline(
        self, unit: str, start_time: int, end_time: int, team: bool = False, **kwargs
    ) -> list[dict[str, object]]:
        """Get photos in timeline portion
        ### Parameters
            * unit : group timeline by "day" or "month"
            * start_time, end_time : date range of photos to retrieve
            * team : space to use: personal (`False`) or shared (`True`) space
        ### kwargs parameters
            offset, limit, sort_by, sort_direction, additional, ...
        ### Return
            photos list

        """
        api_name = "SYNO.FotoTeam.Browse.Item" if team else "SYNO.Foto.Browse.Item"
        req_param = dict(
            {
                "timeline_group_unit": unit,
                "start_time": start_time,
                "end_time": end_time,
                "method": "list",
            },
            **kwargs,
        )
        if "offset" not in req_param:
            req_param["offset"] = 0
        if "limit" not in req_param:
            req_param["limit"] = 500
        return self._request_data(api_name, req_param, method="post")["data"]["list"]


class DatePhoto:
    """Implements date/timestamp support for Synology Photos

    ### Usage :

        ```  python
        for photo in synofoto.photos_in_album(synofoto.get_albums("Family Album "))
            date_photo = DatePhoto.from_timestamp(photo['time'])
            print(f'name: "{photo["filename"]}" date photo: {date_photo.to_string()}')
        ```
    """

    def __init__(self, dateval: int | float | datetime | None):
        if isinstance(dateval, float):
            dateval = int(dateval)
        elif isinstance(dateval, int):
            if dateval >= 0:
                self.date = datetime.fromtimestamp(dateval, pytz.timezone("UTC"))
            else:
                self.date = datetime(1970, 1, 1) + timedelta(seconds=dateval)
        else:
            self.date = dateval.replace(tzinfo=pytz.timezone("UTC"))
        self._fmt = "%d/%m/%Y-%H:%M:%S"

    def set_default_string_format(self, new_format: str) -> None:
        """set default string format when using to_string()"""
        self._fmt = new_format

    @classmethod
    def from_date(cls, year: int, month: int, day: int) -> DatePhoto:
        """Constructor using date only"""
        date = datetime(day=day, month=month, year=year, tzinfo=pytz.timezone("UTC"))
        return cls(date)

    @classmethod
    def from_timestamp(cls, value: int) -> DatePhoto:
        """Constructor using timetamp"""
        return cls(value)

    def to_string(self, fmt: str = None) -> str:
        """return string date"""
        if not fmt:
            fmt = self._fmt
        return self.date.strftime(fmt)

    def to_timestamp(self) -> int:
        """return timestamp"""
        return int(self.date.timestamp())

    def start_of_day(self) -> DatePhoto:
        """return new date : the start of day"""
        return DatePhoto(self.date.replace(hour=0, minute=0, second=0))

    def end_of_day(self) -> DatePhoto:
        """return new date : the end of day"""
        return DatePhoto(self.date.replace(hour=23, minute=59, second=59))

    def start_of_month(self) -> DatePhoto:
        """return new date : the start of month"""
        return DatePhoto(self.date.replace(day=1, hour=0, minute=0, second=0))

    def end_of_month(self) -> DatePhoto:
        """return new date : the end of month"""
        # The day 28 exists in every month. 4 days later, it's always next month
        next_month = self.date.replace(day=28) + timedelta(days=4)
        # subtracting the number of the current day brings us back one month
        # return next_month - datetime.timedelta(days=next_month.day)
        return DatePhoto((next_month - timedelta(days=next_month.day)).replace(hour=23, minute=59, second=59))

    def __eq__(self, other):
        if not isinstance(other, DatePhoto):
            return False
        return self.date == other.date
