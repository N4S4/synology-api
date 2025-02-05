---
sidebar_position: 3
---

# Basic Usage
### Standard workflow
- Import desired API class
  
    ```python
    from synology_api.filestation import FileStation
    from synology_api.downloadstation import DownloadStation
    ```
- Authenticate
  
    ```python
    fs = FileStation(
        'Synology Ip',
        'Synology Port',
        'Username',
        'Password',
        secure=False,
        cert_verify=False,
        dsm_version=7,
        debug=True,
        otp_code=None
    )

    ds = DownloadStation(
        'Synology Ip',
        'Synology Port',
        'Username',
        'Password',
        secure=False,
        cert_verify=False,
        dsm_version=7,
        debug=True,
        otp_code=None
    )
    ```
- Run API method
    ```python
    fs_info = fs.get_info()
    ds_info = ds.get_info()
    ```

### Complete Example

:::note
The output for `FileStation` and `DownloadStation` is interactive by **default**.
:::
```python
from synology_api.filestation import FileStation
from synology_api.downloadstation import DownloadStation

fs = FileStation(
    'Synology Ip',
    'Synology Port',
    'Username',
    'Password',
    secure=False,
    cert_verify=False,
    dsm_version=7,
    debug=True,
    otp_code=None
)

ds = DownloadStation(
    'Synology Ip',
    'Synology Port',
    'Username',
    'Password',
    secure=False,
    cert_verify=False,
    dsm_version=7,
    debug=True,
    otp_code=None
)

fs_info = fs.get_info()
ds_info = ds.get_info()
```

:::info
The response data would be a `JSON` object parsed into a `Dict`:
:::
```python 
{
    "data": {
        "enable_list_usergrp": False,
        "hostname": "MyCloud",
        "is_manager": True,
        "items": [{"gid": 100}, {"gid": 101}],
        "support_file_request": True,
        "support_sharing": True,
        "support_vfs": True,
        "support_virtual": {"enable_iso_mount": True, "enable_remote_mount": True},
        "support_virtual_protocol": ["cifs", "nfs", "iso"],
        "system_codepage": "enu",
        "uid": 1026},
    },
    "success": True
}
```

:::note
For more information about the initialization params, refer to [BaseApi](../apis/base_api)