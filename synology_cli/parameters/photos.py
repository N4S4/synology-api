
# urls

BROWSE_NORMAL_ALBUM_URL = '{url}/entry.cgi/SYNO.Foto.Browse.NormalAlbum'

# parameter sets

CREATE = {
    'method': 'create',
    'version': '1',
    'format': 'sid',
    '_sid': None
}

LIST = {
    'method': 'list',
    'version': 2,
    'offset': 0,
    'limit': 50,
    'format': 'sid',
    '_sid': None
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
