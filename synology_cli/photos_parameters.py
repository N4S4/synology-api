
# urls

# parameter sets

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

BROWSE_FOLDER_PARAMS = {
    **LIST,
    'api': 'SYNO.Foto.Browse.Folder',
    'folder_id': 0
}

BROWSE_ITEM_PARAMS = {
    **LIST,
    'api': 'SYNO.Foto.Browse.Item',
    'sort_by': 'filename',
    'sort_direction': 'asc',
}
