# Synology Wrapper

If you find yourself on this page,
most probably you are trying to develop something for your NAS,

this wrapper might come to your help to build your script.

I would like to specify that **I am Not** a programmer as I do it all
for hobby as is my passion and in my **little** free time.

Said this you will find many things can be simplified and I slowly will.

If you wish to help me you are welcome!


## Premise

I've tried this wrapper only with python3 
I do not know if it actually runs with previous versions 

## Prerequisites

Prior to install this wrapper you will need to install requests library.

## Installation

Just go to repository folder and run the setup.py it will install the wrapper for you.
from the command line go to the downloaded folder and run:

```
python3.6 setup.py install
```

or

```
pip3 install git+https://github.com/N4S4/synology-api
```


## Basic Usage

```python
from synology_api import filestation, downloadstation

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will login automatically 

fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password')

fl.get_info()

dwn = downloadstation.DownloadStation('Synology Ip', 'Synology Port', 'Username', 'Password')

dwn.get_info()

```

response would be json data

```json 
{'data': {'enable_list_usergrp': False,
  'hostname': 'MyCloud',
  'is_manager': True,
  'items': [{'gid': 100}, {'gid': 101}],
  'support_file_request': True,
  'support_sharing': True,
  'support_vfs': True,
  'support_virtual': {'enable_iso_mount': True, 'enable_remote_mount': True},
  'support_virtual_protocol': ['cifs', 'nfs', 'iso'],
  'system_codepage': 'enu',
  'uid': 1026},
 'success': True}
```

## Available Functions

There are quite few available functions so... I will need to write a documentation as  
I will slowly implement more functions, Synology APIs are plenty, too many for my little time.

This wrapper cover the following APIs for now:

| DownloadStation  | 
| ------------- | 
| SYNO.DownloadStation.Info  | 
| SYNO.DownloadStation.Schedule  | 
| SYNO.DownloadStation.Task  | 

| FileStation   |
| ------------- | 
| SYNO.FileStation.Info | 
| SYNO.FileStation.List | 
| SYNO.FileStation.Search | 
| SYNO.FileStation.VirtualFolder | 
| SYNO.FileStation.Favorite | 
| SYNO.FileStation.DirSize | 
| SYNO.FileStation.CheckPermission | 
| SYNO.FileStation.Sharing | 
| SYNO.FileStation.CreateFolder | 
| SYNO.FileStation.Rename | 
| SYNO.FileStation.CopyMove | 
| SYNO.FileStation.Delete | 
| SYNO.FileStation.Extract | 
| SYNO.FileStation.Compress | 
| SYNO.FileStation.BackgroundTask | 

####FileStation Functions list

To explain the use of some function I will divide all the functions in two sets

you can run the following set of functions at your will entering just the required data,


| Function | Description |
| --- | --- |
| get_info() | Provide File Station information |
| get_list_share() | List all shared folders.  |
| get_file_list() | Enumerate files in a given folder  |
| get_file_info() | Get information of file(s)  |
| get_mount_point_list()  | List all mount point folders on one given type of virtual file system  |
| get_favorite_list()  | List user’s favorites  |
| add_a_favorite()  | Add a folder to user’s favorites  |
| delete_a_favorite() | Delete a favorite in user’s favorites.  |
| clear_broken_favorite()  | Delete all broken statuses of favorites.  |
| edit_favorite_name() | Edit a favorite name  |
| replace_all_favorite() | Replace multiple favorites of folders to the existed user’s favorites.  |
| check_permission() | Check if a logged-in user has write permission to create new files/folders in a given folder  |
| get_shared_link_info() | Get information of a sharing link by the sharing link ID  |
| get_shared_link_list() | List user’s file sharing links.  |
| create_sharing_link() | Generate one or more sharing link(s) by file/folder path(s)  |
| delete_shared_link() | Delete one or more sharing links.  |
| clear_invalid_shared_link() | Remove all expired and broken sharing links  |
| edit_shared_link() | Edit sharing link(s)  |
| create_folder() | Create folders.  |
| rename_folder() | Rename a file/folder  |
| delete_blocking_function() | Delete files/folders. This is a blocking method. The response is not returned until the deletion
operation is completed. |
| get_file_list_of_archive()  | List archived files contained in an archive  |
| get_list_of_all_background_task()  | List all background tasks including copy, move, delete, compress and extract tasks  |

To run the following functions you'll have to start the task with the start function

| Function | Description |
| --- | --- |
| search_start()  | Search files according to given criteria.  |
| get_search_list()  | List matched files in a search temporary database.  |
| stop_search_task() | Stop the searching task |
| stop_all_search_task() | Stop the all searching tasks |
| start_dir_size_calc() | Start to calculate size for one or more file/folder paths. |
| get_dir_status() | Get the status of the size calculating task |
| stop_dir_size_calc() | Stop to calculate size |
| start_copy_move() | Start to copy/move files |
| get_copy_move_status() | Get the copying/moving status |
| stop_copy_move_task() | Stop a copy/move task. |
| start_delete_task() | Delete file(s)/folder(s). |
| get_delete_status() | Get the deleting status |
| stop_delete_task() | Stop a delete task |
| start_extract_task() | Start to extract an archive. |
| get_extract_status() | Get the extract task status |
| stop_extract_task() | Stop the extract task |
| start_file_compression() | Start to compress file(s)/folder(s). |
| get_compress_status() | Get the compress task status |
| stop_compress_task() | Stop the compress task |

####DownloadStations functions are:

| Function | Description |
| --- | --- |
| get_info()  | Download Station info  |
| get_config()  | Download Station Settings info  |
| set_server_config()  | Sets Download Station settings  |
| schedule_info()  | Provides advanced schedule settings info  |
| schedule_set_config()  | Sets advanced schedule settings.  |
| tasks_list()  | Provides task listing  |
| tasks_info()  | Provides detailed task information  |
| delete_task()  | Delete a Task  |
| pause_task()  | Pause a Task  |
| resume_task()  | Resume a task  |
| edit_task()  | Edit a Task  |


####What's still missing

There is still few missing function which is a work in progress:

| Missing in FileStation |
|----------------------|
| SYNO.FileStation.Upload | 
| SYNO.FileStation.Thumb  | 
| SYNO.FileStation.Download  | 

| Missing in DownloadStation |
|---|
|SYNO.DownloadStation.Task create|

### Bugs

Maybe? 

I hate bugs..

well report them please (if you'll ever use this code)

### Conclusions

There is still a lot to implement.

The code is probably is some parts twisted and I will try to optimize it at best

### Contributing

Just Don't Be Scared

### Authors

- Renato Visaggio - _Initial_ _Work_ - [N4S4](https://github.com/N4S4)





