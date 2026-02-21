"""
Synology Core iSCSI API wrapper.

This module provides a Python interface for managing iSCSI LUNs and Targets.

Notes
-----
Synology does not publish a full public spec for these endpoints. This file is therefore a
best-effort wrapper built from:

- The output of Synology's official CLI helper `synoiscsiwebapi` (method inventory and
  argument hints).
- Observed parameter conventions from other open-source integrations (CSI drivers).
- Reverse-engineering of DSM Diskstation requests.

Available APIs:
- `SYNO.Core.ISCSI.LUN`
- `SYNO.Core.ISCSI.Target`

See full docs:
https://N4S4.github.io/synology-api/docs/
"""

from json import dumps as _json

import time
from typing import Any, Optional, Union, Literal, Sequence, List

from . import base_api

# -----------------------------
# Utilities
# -----------------------------

def _ensure_list(value: Optional[Union[str | int, Sequence[str | int]]]) -> list[str | int]:
    """
    Normalize a single string/int or a sequence of strings/ints into a list.

    Parameters
    ----------
    value : int | str or Sequence[int | str]
        Input value.

    Returns
    -------
    list[str | int]
        List with one (if non-sequence input) or more elements.
    """
    if value is None:
        return []
    if isinstance(value, str) or isinstance(value, int):
        return [value]
    return list(value)


# -----------------------------
# Abstract ISCSI API
# -----------------------------

class ISCSI(base_api.BaseApi):
    """Abstract wrapper class for SYNO.Core.ISCSI.<xxx> requests."""
    pass

# -----------------------------
# LUN API
# -----------------------------

class LUN(base_api.BaseApi):
    """
    API wrapper for Synology iSCSI LUN management. This class targets the `SYNO.Core.ISCSI.LUN` WebAPI.

    Methods
    -------
    - Getters:
        - List LUNs
        - Get LUN details
    - Setters:
        - Update LUN properties
    - Actions:
        - Create / delete LUN
        - Clone LUN
        - Map / unmap targets

    Notes
    -----
    - LUN names cannot contain special characters (only "-" allowed).
    - Notes on LUN types:
        - `BLOCK`: disabled in DSM 7.3.2,
        - `FILE`: minimal LUN type, thick provisioning,
        - `THIN`: minimal LUN type, thin provisioning,
        - `ADV`: legacy thin-provisionning type, featuring advanced options,
        - `BLUN` types: modern implementation based on BTRFS volumes (unavailable for ext4 filesystems) featuring advanced options,
        - `SINK`, `BLUN_SINK`, `BLUN_THICK_SINK`: likely used internally by DSM for Snapshot Replication targets,
        - `CINDER`, `CINDER_BLUN`, `CINDER_BLUN_THICK`: Integrated with OpenStack Cinder

    Examples
    --------
    List LUNs
    ```python
    from synology_api.core_iscsi import LUN

    lun_api = LUN('IP', 'PORT', 'USER', 'PASSWORD')
    lun_list = lun_api.list()

    print(lun_list['data']['luns'])
    ```

    Create a new LUN
    ```
    my_lun = lun_api.create(
        'my-LUN-1234',   # Special characters other than "-" trigger API errors upon creation
        'THIN',          # Non-legacy and non-internal LUN types include: 'FILE', 'THIN' (ext4 and btrfs) ; 'BLUN', 'BLUN_THICK' (btrfs)
        '/volume1',      # Note the leading '/'
        1024**3,         # Size in bytes
        description="Project XYZ"
    )

    print(my_lun)
    # -> {'data': {'lun_id': 7, 'uuid': 'ac36dabc-6e23-40e0-8956-c8bc8a00397e'}, 'success': True}
    ```

    Get information for a given LUN (e.g. the one just created)
    ```python
    uuid = my_lun['data']['uuid']
    lun_info = lun_api.get(uuid)

    print(lun_info['data'])  # Includes import & sync information
    print(lun_info['data']['lun'])
    ```

    Trigger LUN deletion
    ```python
    lun_del_response = lun_api.delete(uuid)   # Single LUN deletion
    multiple_lun_del_response = lun_api.delete([uuid1, uuid2, ...])   # Multiple LUN deletion

    # Wait until complete deletion
    safe_lun_del_response = lun_api.safe_delete(uuid)
    ```

    Set new characteristics for a given LUN (when allowed by context)
    ```python
    uuid = my_lun['data']['uuid']

    lun_api.set(uuid, new_name='my-LUN-4321', new_type='BLUN')
    ```

    Clone LUN
    ```python
    uuid = my_lun['data']['uuid']

    print(
        lun_api.clone(uuid, 'my-cloned-LUN', dst_location='/volume2')
    )
    # -> {'data': {'dst_lun_uuid': '58407cf0-a5d9-480d-98cc-53d8ac691f96'}, 'success': True}
    ```
    """

    _API_NAME = "SYNO.Core.ISCSI.LUN"

    def _request(self, method: str, params: dict[str, Any], version: Optional[Union[int, str]] = None) -> dict[str, object]:
        """
        Utility wrapper for calling BaseApi.request_data().

        Parameters
        ----------
        method : str
            API method name.
        params : dict[str, Any]
            Dictionary of parameters.
        version : Optional[Union[int, str]], optional
            API method version. Leave blank for highest available version call.

        Returns
        -------
        dict[str, object]
            API response.
        """
        info = self.gen_list[self._API_NAME]
        api_path = info["path"]
        req_param = {
            "version": str(version if version is not None else info.get("maxVersion", 1)),
            "method": method,
        }
        req_param.update({k: v for k, v in params.items() if v is not None})
        return self.request_data(self._API_NAME, api_path, req_param)

    # --------
    # LUN core
    # --------

    def create(
        self,
        name: str,
        type: Literal[
            "FILE",
            "THIN",
            "BLUN",
            "BLUN_THICK",
            "ADV",
            "SINK",
            "CINDER",
            "CINDER_BLUN",
            "CINDER_BLUN_THICK",
            "BLUN_SINK",
            "BLUN_THICK_SINK",
            "BLOCK",
        ],
        location: str,
        size: str | int,
        description: Optional[str] = None,
        extent_size: Optional[Union[int, str]] = None,
        emulate_caw: Optional[bool] = None,
        emulate_3pc: Optional[bool] = None,
        emulate_tpu: Optional[bool] = None,
        emulate_tpws: Optional[bool] = None,
        emulate_fua_write: Optional[bool] = None,
        emulate_sync_cache: Optional[bool] = None,
        can_snapshot: Optional[bool] = None,
        src_lun_dir: Optional[str] = None,
        src_lun_file: Optional[str] = None
    ) -> dict:
        """
        Create a new iSCSI LUN.

        Parameters
        ----------
        name : str
            LUN name.
        type : {"FILE","THIN","ADV","BLUN","BLUN_THICK",...}
            LUN type. Availability depends on filesystem and DSM version.
        location : str
            Target location, typically a volume path (example: `"/volume1"`).
        size : int or str
            LUN size in bytes.
        description : str, optional
            Optional textual description.
        extent_size : int or str, optional
            Extent size (may be ignored depending on type). [Untested]
        emulate_caw : bool, optional
            Enable SCSI COMPARE AND WRITE (CAW) support.
            Allows atomic compare-and-write operations, typically used
            by clustered filesystems or applications requiring
            conditional block updates. When enabled, the LUN reports
            support for the CAW command to the initiator.

        emulate_3pc : bool, optional
            Enable SCSI Third-Party Copy (XCOPY) support.
            Allows block-level offloaded copy operations between
            devices without transferring data through the initiator.
            Used by hypervisors and storage-aware backup systems.

        emulate_tpu : bool, optional
            Enable SCSI UNMAP support (Thin Provisioning UNMAP).
            Allows the initiator to explicitly deallocate logical
            block ranges that are no longer in use (e.g. filesystem
            discard/TRIM). Required for proper space reclamation
            on thin-provisioned LUNs.

        emulate_tpws : bool, optional
            Enable SCSI WRITE SAME support with thin provisioning
            semantics (Thin Provisioning WRITE SAME).
            Allows large zero-write operations that may be interpreted
            by the storage backend as deallocation hints. Often used
            as an alternative or complement to UNMAP for space
            reclamation.

        emulate_fua_write : bool, optional
            Enable handling of the SCSI Force Unit Access (FUA) bit
            on write commands (DSM 7+).
            When enabled, write commands marked with FUA are forced
            to stable storage before completion is reported. Disabling
            this may improve performance but can weaken durability
            guarantees.

        emulate_sync_cache : bool, optional
            Enable support for the SCSI SYNCHRONIZE CACHE command
            (DSM 7+).
            When enabled, explicit cache flush requests from the
            initiator are honored, ensuring that buffered writes are
            committed to stable storage. Disabling this may increase
            performance at the cost of reduced crash-consistency
            guarantees.
        can_snapshot : bool, optional
            Enable snapshot capability for the LUN.
            When set, the LUN is eligible for snapshot creation and
            snapshot-based operations (e.g. cloning, replication).
            Valid only for thin-provisioned LUN types.

        src_lun_dir : str, optional
            Source lun directory (likely) for creation based on snapshot import.
        src_lun_file : str, optional
            Source lun file (likely) for creation based on snapshot import.

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            "data": {
                "lun_id": 0,
                "uuid": "2e349f91-e2a4-45dc-ba1c-774eb80d8b6f"
            },
            "success": true
        }
        ```
        """

        params: dict[str, Any] = {
            "name": name,
            "type": type,
            "location": location,
            "size": int(size)
        }

        # Build dev_attribs list in proper format, based on kwargs
        dev_attribs = []
        for key, val in (
            ("emulate_tpws", emulate_tpws),
            ("emulate_caw", emulate_caw),
            ("emulate_3pc", emulate_3pc),
            ("emulate_tpu", emulate_tpu),
            ("emulate_fua_write", emulate_fua_write),
            ("emulate_sync_cache", emulate_sync_cache),
            ("can_snapshot", can_snapshot)
        ):
            if val is not None:
                dev_attribs.append({
                    "dev_attrib": key,
                    "enable": int(val)
                })
        if dev_attribs:
            params.update({"dev_attribs": _json(dev_attribs)})

        # Optional arguments
        for key, val in (
            ("description", description),
            ("extent_size", extent_size),
            ("src_lun_dir", src_lun_dir),
            ("src_lun_file", src_lun_file)
        ):
            if val is not None:
                params[key] = val

        return self._request("create", params)

    def delete(
        self,
        uuid_or_uuids_list: str | Sequence[str]
    ) -> dict:
        """
        Delete one or more LUNs.

        Parameters
        ----------
        uuid_or_uuids_list : str | Sequence[str]
            LUN UUID or list of LUN UUIDs

        Returns
        -------
        dict[str, object]
            API response.
        """

        # Don't risk a useless API error if no uuid is actually provided
        if not uuid_or_uuids_list:
            return {}

        params = {
            "uuid": '""',
            "uuids": _json(_ensure_list(uuid_or_uuids_list))
        }

        return self._request("delete", params)

    def safe_delete(
        self,
        uuid_or_uuids_list: str | Sequence[str],
        min_request_delay: float = 1.
    ) -> dict:
        """
        Delete one or more LUNs, awaiting for complete deletion before returning.

        Parameters
        ----------
        uuid_or_uuids_list : str | Sequence[str]
            LUN UUID or list of LUN UUIDs
        min_request_delay : float, optional
            Minimum delay (in seconds) between two calls to LUN.list() when checking for complete deletion.

        Returns
        -------
        dict[str, object]
            API response.
        """

        # Don't risk a useless API error if no uuid is actually provided
        if not uuid_or_uuids_list:
            return {}

        uuid_list = _ensure_list(uuid_or_uuids_list)

        params = {
            "uuid": '""',
            "uuids": _json(uuid_list)
        }

        ret = self._request("delete", params)

        # Request LUN list at most once every `min_request_delay` seconds, awaiting for complete deletion
        last_ts = 0
        while uuid_list:
            if time.time() - last_ts < min_request_delay:
                time.sleep((time.time() - last_ts)/10)

            last_ts = time.time()
            uuid_list = [lun['uuid'] for lun in self.list(
            )['data']['luns'] if lun['uuid'] in uuid_list]

        return ret

    def list(
        self,
        types: List[str] = [
            "BLOCK",
            "FILE",
            "THIN",
            "ADV",
            "SINK",
            "CINDER",
            "CINDER_BLUN",
            "CINDER_BLUN_THICK",
            "BLUN",
            "BLUN_THICK",
            "BLUN_SINK",
            "BLUN_THICK_SINK",
        ],
        additional_info: List[str] = [
            "is_action_locked",
            "is_mapped",
            "extent_size",
            "allocated_size",
            "status",
            "allow_bkpobj",
            "flashcache_status",
            "family_config",
            "snapshot_info",
        ],
        location: Optional[str] = None
    ) -> dict:
        """
        List available LUNs.

        Parameters
        ----------
        types : List[str], optional
            Type of LUNS to retrieve.
            Defaults to `[ "BLOCK", "FILE", "THIN", "ADV", "SINK", "CINDER", "CINDER_BLUN", "CINDER_BLUN_THICK", "BLUN", "BLUN_THICK", "BLUN_SINK", "BLUN_THICK_SINK" ]`.
            Possible values:
            - `"BLOCK"`
            - `"FILE"`
            - `"THIN"`
            - `"ADV"`
            - `"SINK"`
            - `"CINDER"`
            - `"CINDER_BLUN"`
            - `"CINDER_BLUN_THICK"`
            - `"BLUN"`
            - `"BLUN_THICK"`
            - `"BLUN_SINK"`
            - `"BLUN_THICK_SINK"`
        additional_info : List[str], optional
            Additional LUN information to include in the response. Specify `[]` to get only basic information.
            Defaults to `[ "is_action_locked", "is_mapped", "extent_size", "allocated_size", "status", "allow_bkpobj", "flashcache_status", "family_config", "snapshot_info" ]`.
            Possible values:
            - `"is_action_locked"`
            - `"is_mapped"`
            - `"extent_size"`
            - `"allocated_size"`
            - `"status"`
            - `"allow_bkpobj"`
            - `"flashcache_status"`
            - `"family_config"`
            - `"snapshot_info"`
        location : str, optional
            Filter by location.

        Returns
        -------
        dict[str, object]
            API response containing LUN list.

        Examples
        --------
        ```json
        {
            "data": {
                "luns": [
                    {
                        "allocated_size": 0,
                        "block_size": 512,
                        "create_from": "",
                        "description": "",
                        "dev_attribs": [
                            {
                                "dev_attrib": "emulate_3pc",
                                "enable": 1
                            },
                            {
                                "dev_attrib": "emulate_tpws",
                                "enable": 1
                            },
                            {
                                "dev_attrib": "emulate_caw",
                                "enable": 1
                            },
                            {
                                "dev_attrib": "emulate_tpu",
                                "enable": 1
                            },
                            {
                                "dev_attrib": "emulate_fua_write",
                                "enable": 0
                            },
                            {
                                "dev_attrib": "emulate_sync_cache",
                                "enable": 0
                            },
                            {
                                "dev_attrib": "can_snapshot",
                                "enable": 1
                            }
                        ],
                        "dev_attribs_bitmap": 31,
                        "dev_config": "",
                        "dev_qos": {
                            "dev_limit": 0,
                            "dev_reservation": 0,
                            "dev_weight": 0,
                            "iops_enable": 0
                        },
                        "direct_io_pattern": 0,
                        "extent_size": 0,
                        "family_config": {
                            "parent_lun_name": "",
                            "parent_lun_uuid": "",
                            "parent_snapshot_time": 0,
                            "parent_snapshot_uuid": ""
                        },
                        "flashcache_id": -1,
                        "flashcache_status": "no_cache",
                        "is_action_locked": false,
                        "is_mapped": true,
                        "location": "/volume2",
                        "lun_id": 6,
                        "name": "LUN-1",
                        "restored_time": 0,
                        "retention": null,
                        "scheduled_task": [
                            {
                                "general": {
                                    "snap_rotate": true,
                                    "snap_type": "app",
                                    "task_enabled": false,
                                    "task_name": "Task LUN-1",
                                    "tid": -1,
                                    "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                },
                                "schedule": {
                                    "date": "2025/3/24",
                                    "date_type": 0,
                                    "hour": 0,
                                    "last_work_hour": 0,
                                    "min": 0,
                                    "monthly_week": [],
                                    "next_trigger_time": "",
                                    "repeat": 0,
                                    "repeat_hour": 0,
                                    "repeat_hour_store_config": null,
                                    "repeat_min": 0,
                                    "repeat_min_store_config": null,
                                    "week_name": "0,1,2,3,4,5,6"
                                }
                            }
                        ],
                        "size": 1073741824,
                        "snapshots": [
                            {
                                "create_time": 1742739365,
                                "description": "test",
                                "is_app_consistent": false,
                                "is_user_locked": true,
                                "mapped_size": 0,
                                "name": "SnapShot-1",
                                "parent_lun_id": 6,
                                "parent_uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                "root_path": "/volume2",
                                "snapshot_id": 1,
                                "snapshot_time": 1742739365,
                                "status": {
                                    "progress": {
                                        "percent": -1,
                                        "step": "waiting"
                                    },
                                    "type": "Healthy"
                                },
                                "taken_by": "user",
                                "total_size": 1073741824,
                                "type": 2,
                                "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                "version": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                            }
                        ],
                        "status": "normal",
                        "type": 263,
                        "type_str": "BLUN",
                        "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "vpd_unit_sn": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    }
                ]
            },
            "success": true
        }
        ```
        """

        # Discard unknown types
        types = list(set(types).intersection([
            "BLOCK",
            "FILE",
            "THIN",
            "ADV",
            "SINK",
            "CINDER",
            "CINDER_BLUN",
            "CINDER_BLUN_THICK",
            "BLUN",
            "BLUN_THICK",
            "BLUN_SINK",
            "BLUN_THICK_SINK",
        ]))
        # Discard unknown 'addition_info' fields

        additional_info = list(set(additional_info).intersection([
            "is_action_locked",
            "is_mapped",
            "extent_size",
            "allocated_size",
            "status",
            "allow_bkpobj",
            "flashcache_status",
            "family_config",
            "snapshot_info",
        ]))

        params: dict[str, Any] = {
            "types": _json(types),
            "additional": _json(additional_info),
            "location": location
        }
        return self._request("list", params)

    def get(
        self,
        uuid: str,
        additional_info: List[str] = [
            "is_action_locked",
            "is_mapped",
            "extent_size",
            "allocated_size",
            "status",
            "import_status",
            "sync_progress",
            "is_vhost_mapped",
            "is_bound",
            "whitelist",
            "flashcache_status",
            "family_config"
        ]
    ) -> dict:
        """
        Get a specific LUN.

        Parameters
        ----------
        uuid : str
            LUN UUID.
        additional_info : List[str], optional
            Additional LUN information to include in the response. Specify `[]` to get only basic information.
            Defaults to `[ "is_action_locked", "is_mapped", "extent_size", "allocated_size", "status", "import_status", "sync_progress", "is_vhost_mapped", "is_bound", "whitelist", "flashcache_status", "family_config" ]`.
            Possible values:
            - `"is_action_locked"`
            - `"is_mapped"`
            - `"extent_size"`
            - `"allocated_size"`
            - `"status"`
            - `"import_status"`
            - `"sync_progress"`
            - `"is_vhost_mapped"`
            - `"is_bound"`
            - `"whitelist"`
            - `"flashcache_status"`
            - `"family_config"`

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'data': {
                'import_done': 0,
                'import_errno': 18990593,
                'import_total': 0,
                'lun': {
                    'allocated_size': 4294967296,
                    'block_size': 512,
                    'create_from': '',
                    'description': '',
                    'dev_attribs': [
                        {'dev_attrib': 'emulate_3pc', 'enable': 0},
                        {'dev_attrib': 'emulate_tpws', 'enable': 0},
                        {'dev_attrib': 'emulate_caw', 'enable': 1},
                        {'dev_attrib': 'emulate_tpu', 'enable': 0},
                        {'dev_attrib': 'emulate_fua_write', 'enable': 0},
                        {'dev_attrib': 'emulate_sync_cache', 'enable': 0},
                        {'dev_attrib': 'can_snapshot', 'enable': 0}
                    ],
                    'dev_attribs_bitmap': 2,
                    'dev_config': '',
                    'dev_qos': {
                        'dev_limit': 0,
                        'dev_reservation': 0,
                        'dev_weight': 0,
                        'iops_enable': 0
                    },
                    'direct_io_pattern': 0,
                    'extent_size': 0,
                    'family_config': {
                        'parent_lun_name': '',
                        'parent_lun_uuid': '',
                        'parent_snapshot_time': 0,
                        'parent_snapshot_uuid': ''
                    },
                    'flashcache_id': -1,
                    'flashcache_status': 'no_cache',
                    'is_action_locked': False,
                    'is_bound': False,
                    'is_mapped': True,
                    'is_vhost_mapped': False,
                    'location': '/volume2',
                    'lun_id': 1,
                    'max_snapshot_count': 256,
                    'name': 'xxxxx',
                    'restored_time': 0,
                    'size': 4294967296,
                    'status': 'normal',
                    'sync_done': 0,
                    'sync_errno': 0,
                    'sync_total': 0,
                    'type': 259,
                    'type_str': 'BLUN_THICK',
                    'uuid': 'f699bc85-3be4-4eb0-9332-020b47143169',
                    'vpd_unit_sn': 'f699bc85-3be4-4eb0-9332-020b47143169'
                },
                'sync_done': 0,
                'sync_errno': 0,
                'sync_total': 0,
                'whitelist': ['0.0.0.0', '0.0.0.0']
            },
            'success': True
        }
        ```
        """

        additional_info = list(set(additional_info).intersection([
            "is_action_locked",
            "is_mapped",
            "extent_size",
            "allocated_size",
            "status",
            "import_status",
            "sync_progress",
            "is_vhost_mapped",
            "is_bound",
            "whitelist",
            "flashcache_status",
            "family_config"
        ]))

        params: dict[str, Any] = {"uuid": _json(uuid)}
        if additional_info:
            params["additional"] = _json(additional_info)

        return self._request("get", params)

    def set(
        self,
        uuid: str,
        new_name: Optional[str] = None,
        new_size: Optional[str | int] = None,
        new_type: Optional[Literal[
            "FILE",
            "THIN",
            "BLUN",
            "BLUN_THICK",
            "ADV",
            "SINK",
            "CINDER",
            "CINDER_BLUN",
            "CINDER_BLUN_THICK",
            "BLUN_SINK",
            "BLUN_THICK_SINK",
            "BLOCK",
        ]] = None,
        new_location: Optional[str] = None,
        emulate_caw: Optional[bool] = None,
        emulate_3pc: Optional[bool] = None,
        emulate_tpu: Optional[bool] = None,
        emulate_tpws: Optional[bool] = None,
        emulate_fua_write: Optional[bool] = None,
        emulate_sync_cache: Optional[bool] = None,
        can_snapshot: Optional[bool] = None
    ) -> dict:
        """
        Update LUN properties.

        Parameters
        ----------
        uuid : str
            LUN UUID.
        new_name : str, optional
            Rename LUN.
        new_size : int or str, optional
            Resize LUN (may be unsupported in many cases).
        new_type : {"BLOCK","FILE","THIN","ADV","BLUN","BLUN_THICK"}, optional
            Change type (may be unsupported in many cases).
        new_location : str, optional
            Move LUN location (may be unsupported in many cases).

        emulate_caw : bool, optional
            Enable SCSI COMPARE AND WRITE (CAW) support.
            Allows atomic compare-and-write operations, typically used
            by clustered filesystems or applications requiring
            conditional block updates. When enabled, the LUN reports
            support for the CAW command to the initiator.

        emulate_3pc : bool, optional
            Enable SCSI Third-Party Copy (XCOPY) support.
            Allows block-level offloaded copy operations between
            devices without transferring data through the initiator.
            Used by hypervisors and storage-aware backup systems.

        emulate_tpu : bool, optional
            Enable SCSI UNMAP support (Thin Provisioning UNMAP).
            Allows the initiator to explicitly deallocate logical
            block ranges that are no longer in use (e.g. filesystem
            discard/TRIM). Required for proper space reclamation
            on thin-provisioned LUNs.

        emulate_tpws : bool, optional
            Enable SCSI WRITE SAME support with thin provisioning
            semantics (Thin Provisioning WRITE SAME).
            Allows large zero-write operations that may be interpreted
            by the storage backend as deallocation hints. Often used
            as an alternative or complement to UNMAP for space
            reclamation.

        emulate_fua_write : bool, optional
            Enable handling of the SCSI Force Unit Access (FUA) bit
            on write commands (DSM 7+).
            When enabled, write commands marked with FUA are forced
            to stable storage before completion is reported. Disabling
            this may improve performance but can weaken durability
            guarantees.

        emulate_sync_cache : bool, optional
            Enable support for the SCSI SYNCHRONIZE CACHE command
            (DSM 7+).
            When enabled, explicit cache flush requests from the
            initiator are honored, ensuring that buffered writes are
            committed to stable storage. Disabling this may increase
            performance at the cost of reduced crash-consistency
            guarantees.

        can_snapshot : bool, optional
            Enable snapshot capability for the LUN.
            When set, the LUN is eligible for snapshot creation and
            snapshot-based operations (e.g. cloning, replication).
            Valid only for thin-provisioned LUN types.

        Returns
        -------
        dict[str, object]
            API response (e.g. `{'success': True}`).
        """

        params: dict[str, Any] = {
            "uuid": _json(uuid)
        }

        # Build dev_attribs list in proper format, based on kwargs
        dev_attribs = []
        for key, val in (
            ("emulate_tpws", emulate_tpws),
            ("emulate_caw", emulate_caw),
            ("emulate_3pc", emulate_3pc),
            ("emulate_tpu", emulate_tpu),
            ("emulate_fua_write", emulate_fua_write),
            ("emulate_sync_cache", emulate_sync_cache),
            ("can_snapshot", can_snapshot)
        ):
            if val is not None:
                dev_attribs.append({
                    "dev_attrib": key,
                    "enable": int(val)
                })
        if dev_attribs:
            params.update({"dev_attribs": _json(dev_attribs)})

        # Optional arguments
        for key, val in (
            ("new_name", new_name),
            ("new_size", new_size),
            ("new_type", new_type),
            ("new_location", new_location)
        ):
            if val is not None:
                params[key] = val

        return self._request("set", params)

    # --------
    # Cloning
    # --------

    def clone(
        self,
        src_lun_uuid: str,
        dst_lun_name: str,
        clone_type: Optional[str] = None,
        dst_location: Optional[str] = None,
        dst_node_uuid: Optional[str] = None,
        dst_address: Optional[str] = None,
        dst_port: Optional[Union[int, str]] = None,
        is_data_encrypted: Optional[bool] = None,
        is_soft_feas_ignored: Optional[bool] = None,
        is_data_clone: Optional[bool] = None
    ) -> dict[str, object]:
        """
        Clone a LUN.

        Parameters
        ----------
        src_lun_uuid : str
            Source LUN UUID.
        dst_lun_name : str
            Destination LUN name.
        clone_type : str, optional
            Clone type.
        dst_location : str, optional
            Destination location.
        dst_node_uuid : str, optional
            Destination node UUID (for remote scenarios).
        dst_address : str, optional
            Destination address (for remote scenarios).
        dst_port : int or str, optional
            Destination port (for remote scenarios).
        is_data_encrypted : bool, optional
            Whether data is encrypted in transit ?
        is_soft_feas_ignored : bool, optional
            Ignore "soft-feasibility"
        is_data_clone : bool, optional
            Unknown flag

        Returns
        -------
        dict[str, object]
            API response.
        """
        params = {
            "src_lun_uuid": _json(src_lun_uuid),
            "dst_lun_name": dst_lun_name,

            **{key: val for key, val in {
                "clone_type": clone_type,
                "dst_location": dst_location,
                "dst_node_uuid": dst_node_uuid,
                "dst_address": dst_address,
                "dst_port": dst_port,
                "is_data_encrypted": is_data_encrypted,
                "is_soft_feas_ignored": is_soft_feas_ignored,
                "is_data_clone": is_data_clone
            }.items() if val is not None}
        }

        return self._request("clone", params)

    def stop_clone(self, src_lun_uuid: str) -> dict[str, object]:
        """
        Stop an in-progress clone operation.

        Parameters
        ----------
        src_lun_uuid : str
            Source LUN UUID.

        Returns
        -------
        dict[str, object]
            API response.
        """
        return self._request("stop_clone", {"src_lun_uuid": _json(src_lun_uuid)})

    # ----------------
    # Target mapping
    # ----------------

    def map_target(
        self,
        uuid: str,
        target_ids: Union[int, str] | Sequence[Union[int, str]]
    ) -> dict[str, object]:
        """
        Map a LUN to one or more targets.

        Parameters
        ----------
        uuid : str
            LUN UUID.
        target_ids : (int or str) or Sequence[int or str]
            Target ID or IDs.

        Returns
        -------
        dict[str, object]
            API response.
        """
        return self._request(
            "map_target",
            {
                "uuid": _json(uuid),
                "target_ids": _json([int(tid) for tid in _ensure_list(target_ids)])
            }
        )

    def unmap_target(
        self,
        uuid: str,
        target_ids: Union[int, str] | Sequence[Union[int, str]]
    ) -> dict[str, object]:
        """
        Unmap a LUN from one or more targets.

        Parameters
        ----------
        uuid : str
            LUN UUID.
        target_ids : (int or str) or Sequence[int or str]
            Target ID or IDs.

        Returns
        -------
        dict[str, object]
            API response.
        """
        return self._request(
            "unmap_target",
            {
                "uuid": _json(uuid),
                "target_ids": _json([int(tid) for tid in _ensure_list(target_ids)])
            }
        )

    # ----------
    # Snapshots
    # ----------

    # TODO

# -----------------------------
# Target API
# -----------------------------

class Target(base_api.BaseApi):
    """
    API wrapper for Synology iSCSI Target management. This class targets the `SYNO.Core.ISCSI.Target` WebAPI.

    Methods
    -------
    - Getters:
        - List targets
        - Get target details
    - Setters:
        - Update target properties (name/iqn/session limits/checksums/auth)
    - Actions:
        - Create / delete
        - Enable / disable
        - Map / unmap LUNs

    Examples
    --------
    List targets
    ```python
    from synology_api.core_iscsi import Target

    target_api = LUN('IP', 'PORT', 'USER', 'PASSWORD')
    target_list = target_api.list()

    print(target_list['data']['targets'])
    ```

    Create a new target
    ```
    my_target = target_api.create(
        'my-target-1234',
        'iqn.2000-01.com.synology:xyz'
    )

    print(my_target)
    # -> {'data': {'target_id': 4}, 'success': True}
    ```

    Get information for a given target (e.g. the one just created)
    ```python
    tid = my_target['data']['target_id']
    target_info = target_api.get(tid)

    print(target_info['data']['target'])
    # -> {'auth_type': 0,
    # 'connected_sessions': [],
    # 'has_data_checksum': False,
    # 'has_header_checksum': False,
    # 'iqn': 'iqn.2000-01.com.synology:xyz',
    # 'is_default_target': False,
    # 'is_enabled': True,
    # 'mapped_luns': [],
    # 'mapping_index': 0,
    # 'max_recv_seg_bytes': 262144,
    # 'max_send_seg_bytes': 262144,
    # 'max_sessions': 1,
    # 'mutual_password': '',
    # 'mutual_user': '',
    # 'name': 'my-target-1234',
    # 'network_portals': [{'interface_name': 'all', 'ip': '', 'port': 3260}],
    # 'password': '',
    # 'status': 'online',
    # 'target_id': 4,
    # 'user': ''}
    ```

    Set new characteristics for a given target
    ```python
    target_api.set(tid, new_name='my-target-4321', new_iqn='iqn.2000-01.com.synology:zyx')
    target_api.set(tid, max_sessions=0) # Allow for multiple sessions (no limit)
    ```

    Enable/disable target
    ```python
    target_api.disable(tid)
    print(target_api.get(tid)['data']['target']['status'])
    # -> "offline"

    target_api.enable(tid)
    print(target_api.get(tid)['data']['target']['status'])
    # -> "online"
    ```

    Map/unmap LUNs to target
    ```python
    target_api.map_lun(tid, uuid) # Map a single LUN
    target_api.map_lun(tid, [uuid1, uuid2, ...]) # Map multiple LUNs at once

    target_api.unmap_lun(tid, uuid) # Unmap a single LUN
    target_api.unmap_lun(tid, [uuid1, uuid2, ...]) # Unmap multiple LUNs at once
    ```

    Delete target
    ```python
    print(target_api.delete(tid))
    # -> {'success': True}
    ```
    """

    _API_NAME = "SYNO.Core.ISCSI.Target"

    def _request(self, method: str, params: dict[str, Any], version: Optional[Union[int, str]] = None) -> dict[str, object]:
        """
        Utility wrapper for calling BaseApi.request_data().

        Parameters
        ----------
        method : str
            API method name.
        params : dict[str, Any]
            Dictionary of parameters.
        version : Optional[Union[int, str]], optional
            API method version. Leave blank for highest available version call.

        Returns
        -------
        dict[str, object]
            API response.
        """
        info = self.gen_list[self._API_NAME]
        api_path = info["path"]
        req_param = {
            "version": str(version if version is not None else info.get("maxVersion", 1)),
            "method": method,
        }
        req_param.update({k: v for k, v in params.items() if v is not None})
        return self.request_data(self._API_NAME, api_path, req_param)

    # -----------
    # Target core
    # -----------

    def create(
        self,
        name: str,
        iqn: str,
        auth_type: Literal[0, 1, 2] = 0,
        max_sessions: Optional[int] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        mutual_user: Optional[str] = None,
        mutual_password: Optional[str] = None
    ) -> dict[str, object]:
        """
        Create a target.

        Parameters
        ----------
        name : str
            Target name.
        iqn : str
            ISCSI Qualified Name.
        auth_type : {0,1,2}, optional
            Authentication type:
            - `0` -> none (default)
            - `1` -> single CHAP
            - `2` -> mutual CHAP
        max_sessions : int, optional
            Maximum sessions (use `0` for unlimited on some systems).
        user : str, optional
            CHAP username (client). Requires `auth_type` >= 1.
        password : str, optional
            CHAP password (client). Requires `auth_type` >= 1.
        mutual_user : str, optional
            Mutual CHAP username (server). Requires `auth_type` == 2.
        mutual_password : str, optional
            Mutual CHAP password (server). Requires `auth_type` == 2.

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'data': {
                'target_id': 3
            },
            'success': True
        }
        ```
        """
        params = {
            "name": name,
            "iqn": iqn,
            "auth_type": auth_type
        }

        if max_sessions:
            params["max_sessions"] = max_sessions

        if auth_type >= 1:
            params.update({
                "user": user,
                "password": password
            })

        if auth_type == 2:
            params.update({
                "mutual_user": mutual_user,
                "mutual_password": mutual_password
            })

        return self._request("create", params)

    def delete(self, target_id: Union[int, str]) -> dict[str, object]:
        """
        Delete a target.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        ```
        """
        return self._request("delete", {"target_id": _json(str(target_id))})

    def list(
        self,
        additional_info: List[str] = [
            "mapped_lun",
            "acls",
            "connected_sessions",
            "status"
        ],
        lun_uuid: Optional[str] = None
    ) -> dict[str, object]:
        """
        List available iSCSI targets.

        Parameters
        ----------
        additional_info : List[str]
            Additional information to include in the response. Specify `[]` to get only basic information.
            Defaults to `["mapped_lun","acls","connected_sessions","status"]`
        lun_uuid : str, optional
            Filter targets mapped to LUN with provided uuid.

        Returns
        -------
        dict[str, object]
            API response containing iSCSI target list.

        Examples
        --------
        ```json
        {
            'data': {
                'targets': [
                    {
                        'auth_type': 0,
                        'connected_sessions': [],
                        'has_data_checksum': False,
                        'has_header_checksum': False,
                        'iqn': 'iqn.2025-01.com.synology:raspberry-pi',
                        'is_default_target': False,
                        'is_enabled': True,
                        'mapped_luns': [
                            {
                                'lun_uuid': 'f699bc85-3be4-4eb0-9332-020b47143169',
                                'mapping_index': 1
                            }
                        ],
                        'mapping_index': -1,
                        'max_recv_seg_bytes': 262144,
                        'max_send_seg_bytes': 262144,
                        'max_sessions': 1,
                        'mutual_password': '',
                        'mutual_user': '',
                        'name': 'raspberry-pi',
                        'network_portals': [
                            {'interface_name': 'all', 'ip': '', 'port': 3260}
                        ],
                        'password': '',
                        'status': 'online',
                        'target_id': 1,
                        'user': ''
                    },
                    {
                        'auth_type': 0,
                        'connected_sessions': [],
                        'has_data_checksum': False,
                        'has_header_checksum': False,
                        'iqn': 'iqn.2000-01.com.synology:xxx.default-target.xxxxxxx',
                        'is_default_target': True,
                        'is_enabled': True,
                        'mapped_luns': [],
                        'mapping_index': -1,
                        'max_recv_seg_bytes': 262144,
                        'max_send_seg_bytes': 262144,
                        'max_sessions': 1,
                        'mutual_password': '',
                        'mutual_user': '',
                        'name': 'Synology iSCSI Target',
                        'network_portals': [
                            {'interface_name': 'all', 'ip': '', 'port': 3260}
                        ],
                        'password': '',
                        'status': 'online',
                        'target_id': 2,
                        'user': ''
                    }
                ]
            },
            'success': True
        }
        ```
        """
        params: dict[str, Any] = {}

        if additional_info:
            params['additional'] = _json(additional_info)

        if lun_uuid:
            params['lun_uuid'] = _json(lun_uuid)

        return self._request("list", params)

    def get(
        self,
        target_id: Union[int, str],
        additional_info: List[str] = [
            "mapped_lun",
            "acls",
            "connected_sessions",
            "status"
        ]
    ) -> dict[str, object]:
        """
        Get information on iSCSI target with id `target_id`.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.
        additional_info : List[str]
            Additional information to include in the response. Specify `[]` to get only basic information.
            Defaults to `["mapped_lun","acls","connected_sessions","status"]`

        Returns
        -------
        dict[str, object]
            API response containing iSCSI target info.

        Examples
        --------
        ```json
        {
            'data': {
                'target': {
                    'auth_type': 0,
                    'connected_sessions': [],
                    'has_data_checksum': False,
                    'has_header_checksum': False,
                    'iqn': 'iqn.2000-01.com.synology:xxx.default-target.xxxxxxx',
                    'is_default_target': True,
                    'is_enabled': True,
                    'mapped_luns': [],
                    'mapping_index': 0,
                    'max_recv_seg_bytes': 262144,
                    'max_send_seg_bytes': 262144,
                    'max_sessions': 1,
                    'mutual_password': '',
                    'mutual_user': '',
                    'name': 'Synology iSCSI Target',
                    'network_portals': [{'interface_name': 'all', 'ip': '', 'port': 3260}],
                    'password': '',
                    'status': 'online',
                    'target_id': 2,
                    'user': ''
                }
            },
            'success': True
        }
        ```
        """

        params: dict[str, Any] = {
            "target_id": _json(str(target_id))
        }

        if additional_info:
            params['additional'] = _json(additional_info)

        return self._request("get", params)

    def set(
        self,
        target_id: Union[int, str],
        new_name: Optional[str] = None,
        new_iqn: Optional[str] = None,
        max_sessions: Optional[int] = None,
        auth_type: Optional[Literal[0, 1, 2]] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        mutual_user: Optional[str] = None,
        mutual_password: Optional[str] = None,
        has_header_checksum: Optional[bool] = None,
        has_data_checksum: Optional[bool] = None,
        max_recv_seg_bytes: Optional[int] = None,
        max_send_seg_bytes: Optional[int] = None
    ) -> dict[str, object]:
        """
        Update target properties.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.
        new_name : str, optional
            New target name.
        new_iqn : str, optional
            New target iqn.
        max_sessions : int, optional
            Maximum sessions (use `0` for unlimited on some systems).
        auth_type : {0,1,2}, optional
            New authentication type:
            - `0` -> none
            - `1` -> single CHAP
            - `2` -> mutual CHAP
        user : str, optional
            CHAP username (client). Requires `auth_type` >= 1.
        password : str, optional
            CHAP password (client). Requires `auth_type` >= 1.
        mutual_user : str, optional
            Mutual CHAP username (server). Requires `auth_type` == 2.
        mutual_password : str, optional
            Mutual CHAP password (server). Requires `auth_type` == 2.
        has_header_checksum : bool, optional
            Enable CRC (cyclic redundancy check) header digest. Typically redundant in Ethernet + TCP settings.
        has_data_checksum : bool, optional
            Enable CRC (cyclic redundancy check) data digest. Typically redundant in Ethernet + TCP settings.
        max_recv_seg_bytes : int, optional
            Maximum receive segment bytes. Available values in Diskstation GUI are 4096, 8192, 65536, 262144 (default).
        max_send_seg_bytes : int, optional
            Maximum send segment bytes. Available values in Diskstation GUI are 4096, 8192, 65536, 262144 (default).

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        ```
        """
        params = {
            "target_id": _json(str(target_id)),
            **{k: v for k, v in {
                "name": new_name,
                "iqn": new_iqn,
                "max_sessions": max_sessions,
                "has_data_checksum": has_data_checksum,
                "auth_type": auth_type,
                "user": user,
                "password": password,
                "mutual_user": mutual_user,
                "mutual_password": mutual_password,
                "max_recv_seg_bytes": max_recv_seg_bytes,
                "max_send_seg_bytes": max_send_seg_bytes,
                "has_header_checksum": has_header_checksum,
            }.items() if v is not None}
        }
        return self._request("set", params)

    # --------------
    # Enable/disable
    # --------------

    def enable(self, target_id: Union[int, str]) -> dict[str, object]:
        """
        Enable a target.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        """
        return self._request("enable", {"target_id": _json(str(target_id))})

    def disable(self, target_id: Union[int, str]) -> dict[str, object]:
        """
        Disable a target.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        """
        return self._request("disable", {"target_id": _json(str(target_id))})

    # -------------
    # LUN mappings
    # -------------

    def map_lun(
        self,
        target_id: Union[int, str],
        lun_uuid_or_uuids_list: str | Sequence[str]
    ) -> dict[str, object]:
        """
        Map one or more LUNs to a target.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.
        lun_uuid_or_uuids_list : str | Sequence[str]
            LUN UUID or list of LUN UUIDs

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        """
        return self._request(
            "map_lun",
            {
                "target_id": _json(str(target_id)),
                "lun_uuids": _json(_ensure_list(lun_uuid_or_uuids_list))
            }
        )

    def unmap_lun(
        self,
        target_id: Union[int, str],
        lun_uuid_or_uuids_list: str | Sequence[str]
    ) -> dict[str, object]:
        """
        Unmap one or more LUNs from a target.

        Parameters
        ----------
        target_id : int | str
            Integer id of iSCSI target.
        lun_uuid_or_uuids_list : str | Sequence[str]
            LUN UUID or list of LUN UUIDs

        Returns
        -------
        dict[str, object]
            API response.

        Examples
        --------
        ```json
        {
            'success': True
        }
        """
        return self._request(
            "unmap_lun",
            {
                "target_id": _json(str(target_id)),
                "lun_uuids": _json(_ensure_list(lun_uuid_or_uuids_list))
            }
        )
