from __future__ import annotations
from typing import Optional
from . import base_api
import json


class Snapshot(base_api.BaseApi):
    """Class for interacting with Snapshot APIs.

        Supported methods:
            - Getters: 
                - Get all snapshots

            - Setters:
                - Set snapshot attributes
            
            - Actions:
                - Create snapshot
                - Delete snapshot

        This class implements APIs to manage snapshots.
        There is no documentation for these APIs, so the implementation is based on network inspection.

        Examples
        --------
        List snapshots for a share:
        ```python
        from synology_api import snapshot
        ss = snapshot.Snapshot('IP', 'PORT', 'USER', 'PASSWORD')
        resp = ss.list_snapshots('share_name')
        print(resp)
        ```

        Create a snapshot for a share:
        ```python
        resp = ss.create_snapshot('share_name')
        print(resp)
        ```

        Delete snapshots for a share:
        ```python
        resp = ss.delete_snapshots('share_name', ['snapshot_name'])
        print(resp)
        ```

        Set attributes for a snapshot:
        ```python
        resp = ss.set_snapshot_attr('share_name', 'snapshot_name', description='new description', lock=True)
        print(resp)
        ```
    """

    def list_snapshots(self,
                       share_name: str,
                       attribute_filter: list[str] = [],
                       additional_attribute: list[str] = [],
                       offset: int = 0,
                       limit: int = -1) -> dict[str, object]:
        """List snapshots for a share.

            Parameters
            ----------
            share_name : str
                Name of the share to list snapshots for

            attribute_filter : list[str], optional
                List of attributes filter to apply. Defaults to `[]` (no filter).

                Each attribute filter is a string in the format of `"attr==value"` or `"attr=value"` and optionally prefixed with `!` to negate the filter.

                The following are examples of valid attribute filters:
                    - `["!hide==true", "desc==abc"]` -> hide is not true and desc is exactly abc
                    - `["desc=abc"]` -> desc has abc in it

            additional_attribute : list[str], optional
                List of snapshot attributes whose values are included in the response.
                Defaults to `[]` (only time is returned).

                Note that not all attributes are available via API. The following are confirmed to work:
                    - desc
                    - lock
                    - worm_lock
                    - schedule_snapshot

            offset : int, optional
                Offset to start listing from. Defaults to `0`.

            limit : int, optional
                Number of snapshots to return. Defaults to `-1` (all).

            Returns
            -------
            dict[str, object]
                API response if successful, error message if not

            Example return
            ----------
            ```json
            {
                "data": {
                    "snapshots": [
                        {
                            "desc": "",
                            "lock": true,
                            "schedule_snapshot": false,
                            "time": "GMT+09-2023.09.11-23.23.40",
                            "worm_lock": true,
                            "worm_lock_begin": "1694442321",
                            "worm_lock_day": "1",
                            "worm_lock_end": "1694528721"
                        }
                    ],
                    "total": 1
                },
                "success": true
            }
            ```
        """

        api_name = 'SYNO.Core.Share.Snapshot'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '2',
                     'method': 'list',
                     'name': share_name,
                     'filter': json.dumps({"attr": attribute_filter}),
                     'additional': json.dumps(additional_attribute),
                     'offset': offset,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def create_snapshot(self,
                        share_name: str,
                        description: str = "",
                        lock: bool = False,
                        immutable: bool = False,
                        immutable_days: int = 7,
                        ) -> dict[str, object]:
        """Create a snapshot for a share.

            Parameters
            ----------
            share_name : str
                Name of the share to create a snapshot for.

            description : str, optional
                Description of the snapshot. Defaults to `""`.

            lock : bool, optional
                Whether to lock the snapshot. Defaults to `False`.

            immutable : bool, optional
                Whether to make the snapshot immutable. Defaults to `False`.

            immutable_days : int, optional
                Number of days to make the snapshot immutable for. Defaults to `7`.
                Must be greater than `0`. Mandatory if immutable is `True`.

            Returns
            -------
            dict[str, object]
                API response if successful, error message if not

            Example return
            ----------
            ```json:
            {
                "data": "GMT+09-2023.09.12-00.33.20",
                "success": true
            }
            ```
        """

        api_name = 'SYNO.Core.Share.Snapshot'
        info = self.gen_list[api_name]
        api_path = info['path']

        snapinfo = {
            "desc": description,
            "lock": lock,
        }
        if immutable == True:
            snapinfo['worm_lock'] = True
            if immutable_days < 1:
                return "immutable_days must be greater than 0"
            snapinfo['worm_lock_day'] = immutable_days
        req_param = {'version': '1',
                     'method': 'create',
                     'snapinfo': json.dumps(snapinfo),
                     'name': share_name}

        return self.request_data(api_name, api_path, req_param)

    def delete_snapshots(self,
                         share_name: str,
                         snapshots: list[str]
                         ) -> dict[str, object]:
        """Delete snapshots for a share.

            Parameters
            ----------
            share_name : str
                Name of the share to delete snapshots for

            snapshots : list[str]
                List of snapshots to delete

            Returns
            -------
            dict[str, object]
                API response if successful, error message if not

            Example return
            ----------
            ```json
            {
                "success": true
            }
            ```
        """

        api_name = 'SYNO.Core.Share.Snapshot'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'delete',
                     'name': share_name,
                     'snapshots': json.dumps(snapshots)}

        return self.request_data(api_name, api_path, req_param)

    def set_snapshot_attr(self,
                          share_name: str,
                          snapshot: str,
                          description: Optional[str] = None,
                          lock: Optional[bool] = None,
                          immutable: Optional[bool] = None,
                          immutable_days: Optional[int] = None
                          ) -> dict[str, object]:
        """Set attributes for a snapshot.

            Parameters
            ----------
            share_name : str
                Name of the share to set attributes for

            snapshot : str
                Name of the snapshot to set attributes for

            description : str, optional
                Description of the snapshot. Defaults to `None` (no change).

            lock : bool, optional
                Whether to lock the snapshot. Defaults to `None` (no change).

            immutable : bool, optional
                Whether to make the snapshot immutable. Defaults to `None` (no change).

            immutable_days : int, optional
                Number of days to make the snapshot immutable for. Defaults to `None` (no change).
                Must be greater than `0`. Mandatory if immutable is `True`.

            Returns
            -------
            dict[str, object]
                API response if successful, error message if not

            Example return
            ----------
            ```json	
            {
                "success": true
            }
            ```
        """

        api_name = 'SYNO.Core.Share.Snapshot'
        info = self.gen_list[api_name]
        api_path = info['path']

        snapinfo = {}
        if description is not None:
            snapinfo['desc'] = description
        if lock is not None:
            snapinfo['lock'] = lock
        if immutable is not None:
            if immutable == False:
                return "immutable cannot be set to False"
            if immutable_days is None:
                return "immutable_days must be specified if immutable is True"
            if immutable_days < 1:
                return "immutable_days must be greater than 0"
            snapinfo['worm_lock'] = True
            snapinfo['worm_lock_day'] = immutable_days
        req_param = {'version': '1',
                     'method': 'set',
                     'snapinfo': json.dumps(snapinfo),
                     'name': share_name,
                     'snapshot': snapshot}

        return self.request_data(api_name, api_path, req_param)
