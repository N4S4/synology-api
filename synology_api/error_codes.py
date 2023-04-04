# source: pages 8 and 16 on PDF:
# https://global.download.synology.com/download/Document/Software/DeveloperGuide/Os/DSM/All/enu/DSM_Login_Web_API_Guide_enu.pdf

# NOTE: https://global.synologydownload.com/download/Document/Software/DeveloperGuide/Package/Calendar/2.4/enu
# /Synology_Calendar_API_Guide_enu.pdf, Refers to common error code # 160, "Insufficient application privilege" Page 10.

CODE_SUCCESS = 0
CODE_UNKNOWN = 9999
# 'Common' Error Codes:
error_codes = {
    CODE_SUCCESS: 'Success',
    100: 'Unknown error',
    101: 'No parameter of API, method or version',
    102: 'The requested API does not exist',
    103: 'The requested method does not exist',
    104: 'The requested version does not support the functionality',
    105: 'The logged in session does not have permission',
    106: 'Session timeout',
    107: 'Session interrupted by duplicated login',
    108: 'Failed to upload the file',
    109: 'The network connection is unstable or the system is busy',
    110: 'The network connection is unstable or the system is busy',
    111: 'The network connection is unstable or the system is busy',
    112: 'Preserve for other purpose',
    113: 'Preserve for other purpose',
    114: 'Lost parameters for this API',
    115: 'Not allowed to upload a file',
    116: 'Not allowed to perform for a demo site',
    117: 'The network connection is unstable or the system is busy',
    118: 'The network connection is unstable or the system is busy',
    119: 'Invalid session / SID not found.',
    # 120-149 Preserve for other purpose
    120: 'Preserve for other purpose',
    121: 'Preserve for other purpose',
    122: 'Preserve for other purpose',
    123: 'Preserve for other purpose',
    124: 'Preserve for other purpose',
    125: 'Preserve for other purpose',
    126: 'Preserve for other purpose',
    127: 'Preserve for other purpose',
    128: 'Preserve for other purpose',
    129: 'Preserve for other purpose',
    130: 'Preserve for other purpose',
    131: 'Preserve for other purpose',
    132: 'Preserve for other purpose',
    133: 'Preserve for other purpose',
    134: 'Preserve for other purpose',
    135: 'Preserve for other purpose',
    136: 'Preserve for other purpose',
    137: 'Preserve for other purpose',
    138: 'Preserve for other purpose',
    139: 'Preserve for other purpose',
    140: 'Preserve for other purpose',
    141: 'Preserve for other purpose',
    142: 'Preserve for other purpose',
    143: 'Preserve for other purpose',
    144: 'Preserve for other purpose',
    145: 'Preserve for other purpose',
    146: 'Preserve for other purpose',
    147: 'Preserve for other purpose',
    148: 'Preserve for other purpose',
    149: 'Preserve for other purpose',
    150: 'Request source IP does not match the login IP',
    160: 'Insufficient application privilege',
    CODE_UNKNOWN: 'Unknown Error',
}
# Source: https://global.synologydownload.com/download/Document/Software/DeveloperGuide/Os/DSM/All/enu
# /DSM_Login_Web_API_Guide_enu.pdf Page 16.
# https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/SurveillanceStation/All/enu
# /Surveillance_Station_Web_API.pdf Pages 32,33 Refers to Auth error code #411: 'Account Locked (when account max try
# exceed).'
auth_error_codes: dict[int, str] = {
    400: 'No such account or incorrect password',
    401: 'Disabled account',
    402: 'Denied permission',
    403: '2 - factor authentication code required',
    404: 'Failed to authenticate 2 - factor authentication code',
    406: 'Enforce to authenticate with 2 - factor authentication code',
    407: 'Blocked IP source',
    408: 'Expired password cannot change',
    409: 'Expired password',
    410: 'Password must be changed',
    411: 'Account Locked (when account max try exceed).',
}

# Source:https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/DownloadStation/All/enu/Synology_Download_Station_Web_API.pdf
# Page 29
download_station_error_codes: dict[int, str] = {
    400: 'File upload failed',
    401: 'Max number of tasks reached',
    402: 'Destination denied',
    403: 'Destination does not exist',
    404: 'Invalid task id',
    405: 'Invalid task action',
    406: 'No default destination',
    407: 'Set destination failed',
    408: 'File does not exist',
}

# TODO use the error code source https://cndl.synology.cn/download/Document/Software/DeveloperGuide/Package
#  /FileStation/All/enu/Synology_File_Station_API_Guide.pdf page 10~11
file_station_error_codes: dict[int, str] = {
    400: 'Invalid parameter of file operation',
    401: 'Unknown error of file operation',
    402: 'System is too busy',
    403: 'Invalid user does this file operation',
    404: 'Invalid group does this file operation',
    405: 'Invalid user and group does this file operation',
    406: "Can't get user/group information from the account server",
    407: 'Operation not permitted',
    408: 'No such file or directory',
    409: 'Non-supported file system',
    410: 'Failed to connect internet-based file system (e.g., CIFS)',
    411: 'Read-only file system',
    412: 'Filename too long in the non-encrypted file system',
    413: 'Filename too long in the encrypted file system',
    414: 'File already exists',
    415: 'Disk quota exceeded',
    416: 'No space left on device',
    417: 'Input/output error',
    418: 'Illegal name or path',
    419: 'Illegal file name',
    420: 'Illegal file name on FAT file system',
    421: 'Device or resource busy',
    599: 'No such task of the file operation',
}

# Source: https://global.synologydownload.com/download/Document/Software/DeveloperGuide/Package/Virtualization/All
# /enu/Synology_Virtual_Machine_Manager_API_Guide.pdf Page 8,9
virtualization_error_codes: dict[int, str] = {
    401: 'Bad parameter.',
    402: 'Operation failed.',
    403: 'Name conflict.',
    404: 'The number of iSCSI LUNs has reached the system limit. Note: vdisk is based on iSCSI LUN, which is also '
         'limited by the system.',
    500: 'The cluster is frozen. More than half of the hosts are offline.',
    501: 'The cluster is in the incompatible mode. Please upgrade to a compatible DSM version and try again.',
    600: 'The cluster is not ready.',
    601: 'The host is offline.',
    700: 'The storage is in invalid.',
    900: 'Failed to set a host to a virtual machine.',
    901: 'The virtual machine does not have a host.',
    902: 'Failed to power on a virtual machine due to insufficient CPU threads.',
    903: 'Failed to power on a virtual machine due to insufficient memory.',
    904: 'The status of virtual machine is online.',
    905: 'MAC conflict.',
    906: 'Failed to create virtual machine because the selected image is not found.',
    907: 'The status of virtual machine is offline.',
    908: 'Failed to power on a virtual machine due to insufficient CPU threads for reservation on the host.',
    909: 'Failed to power on the virtual machine because there is no corresponding networking on the host.',
    910: 'Only the VirtIO hard disk controller can be used to boot the virtual machine remotely.',
    911: 'Virtual machines with UEFI enabled cannot be powered on remotely.',
    1000: 'Cannot find task_id.',
    1001: 'Need Virtual Machine Manager Pro.',
    1400: 'The result of image creating is partial success.',
    1600: 'The virtual machine has been successfully edited. However, errors occurred while reserving the memory or '
          'CPU on the HA hosts.',
}

# Source: https://global.synologydownload.com/download/Document/Software/DeveloperGuide/Package/Calendar/2.4/enu
# /Synology_Calendar_API_Guide_enu.pdf Pages 10,11.
calendar_error_codes: dict[int, str] = {
    400: 'Invalid parameter of file operation',
    401: 'Unknown error of file operation',
    402: 'System is too busy',
    403: 'This user does not have permission to execute this operation',
    404: 'This group does not have permission to execute this operation',
    405: 'This user/group does not have permission to execute this operation',
    406: 'Cannot obtain user/group information from the account server',
    407: 'Operation not permitted',
    408: 'No such file or directory',
    409: 'File system not supported',
    410: 'Failed to connect internet-based file system (ex: CIFS)',
    411: 'Read-only file system',
    412: 'Filename too long in the non-encrypted file system',
    413: 'Filename too long in the encrypted file system',
    414: 'File already exists',
    415: 'Disk quota exceeded',
    416: 'No space left on device',
    417: 'Input/output error',
    418: 'Illegal name or path',
    419: 'Illegal file name',
    420: 'Illegal file name on FAT file system',
    421: 'Device or resource busy',
    599: 'No such task of the file operation',
}

# # Source: https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package
# /SurveillanceStation/All/enu/Surveillance_Station_Web_API.pdf NOTE: Pages 81, 131,132, 155, 190, 222, 305, 314,
# 321, 328, 451, 473 539, 556, contain unique items. Most of these are duplicate information, but they describe
# different methods, all the error codes I found are on # Pages: 71, 81, 85, 93, 103, 113, 131, 132, 139, 144, 155,
# 167, 169, 176, 187, 190, 191, 201, 211, 212, 217, 222, 227, #         241, 245, 249, 253, 264, 279, 281, 305, 314,
# 321, 328, 363, 365, 368, 369, 393, 395, 397, 403, 410, 412, 415, #         419, 430, 451, 473, 539, 556
surveillance_station_error_codes: dict[int, str] = {
    400: 'Execution failed.',
    401: 'Parameter invalid.',
    402: 'Camera disabled.',
    403: 'Insufficient license.',
    404: 'Codec activation failed',
    405: 'CMS server connection failed.',
    407: 'CMS closed.',
    412: 'Need to add license.',
    413: 'Reach the maximum of platform',
    414: 'Some events not exist.',
    415: 'message connect failed.',
    417: 'Test Connection Error.',
    418: 'Object is not exist. / The VisualStation ID does not exist.',
    419: 'Visualstation name repetition.',
    439: 'Too many items selected',
    446: 'Task Path already exist.',
    522: 'Original Task is Migrating',
    534: 'Exceed name length limitation.',
    543: 'The number of DVA tasks and face tasks exceed the limitation',
    548: 'The input video type of the DVA task is invalid',
    553: 'No face detected.',
    554: 'Face detected is too small.',
    555: 'Multiple faces detected.',
    556: 'The account try to set has exists.',
    557: 'No image data appended.',
    558: 'Add face group failed.',
    560: 'The camera try to apply to face task is occupied by another face task.',
    561: 'The number of face profile exceeds the maximum limit.',
    562: 'The number of face group exceeds the maximum limit.',
    563: 'The face profile is created or edited failed due to duplicated account.',
    564: 'The face result try to query doesn\'t exist',
    567: 'The face database is under synchronization.',
}
