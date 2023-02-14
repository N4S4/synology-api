
# urls

BROWSE_NORMAL_ALBUM_URL = '{url}/entry.cgi/SYNO.Foto.Browse.NormalAlbum'

# parameter sets

SID = {
    'format': 'sid',
    '_sid': None
}

COUNT = {
	'method': 'count',
	'version': 1,
    **SID,
}

CREATE = {
    'method': 'create',
    'version': 1,
    **SID,
}

GET = {
    'method': 'get',
    'version': 2,
    **SID,
}

LIST = {
    'method': 'list',
    'version': 2,
    'offset': 0,
    'limit': 100,
    **SID,
}

BROWSE_ALBUM = {
    **LIST,
    'api': 'SYNO.Foto.Browse.Album',
}

BROWSE_FOLDER = {
    **LIST,
    'api': 'SYNO.Foto.Browse.Folder',
    'folder_id': 0
}

BROWSE_ITEM = {
    **LIST,
    'api': 'SYNO.Foto.Browse.Item',
    'sort_by': 'filename',
    'sort_direction': 'asc',
}

COUNT_ALBUM = {
    **COUNT,
    'api': 'SYNO.Foto.Browse.Album',
}

GET_FOLDER = {
    'api': 'SYNO.Foto.Browse.Folder',
    'id': 0,
    'additional': '["access_permission"]', # ???
    **GET,
}

CREATE_ALBUM = {
    **CREATE,
    'api': 'SYNO.Foto.Browse.NormalAlbum',
    'name': None,
    # this should be '[1,2,3]' with the numbers being item ids,
    # but can be empty as well (although the Web UI does not allow that)
    'item': '[]',
}

CREATE_FOLDER = {
    **CREATE,
    'api': 'SYNO.Foto.Browse.Folder',
    'target_id': None, # id of the parent folder
    'name': None, # name of the folder
}

ADD_ITEM_TO_ALBUM = {
    'api': 'SYNO.Foto.Browse.NormalAlbum',
    'method': 'add_item',
    'version': 1,
    'id': 0,
    'item': '[]' # should be '[1,2,3]'
}
