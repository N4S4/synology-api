
# urls

BROWSE_NORMAL_ALBUM_URL = '{url}/entry.cgi/SYNO.Foto.Browse.NormalAlbum'

# parameter sets

SID = {
    'format': 'sid',
    '_sid': None
}

# parameter sets for various operations

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

COUNT_FOLDER = {
    **COUNT,
    'api': 'SYNO.Foto.Browse.Folder',
    'id': 0,
}

COUNT_ITEM = {
    **COUNT,
    'api': 'SYNO.Foto.Browse.Item',
}

COUNT_ITEM_FOLDER = {
    **COUNT_ITEM,
    'folder_id': 0,
}

COUNT_ITEM_ALBUM = {
    **COUNT_ITEM,
    'album_id': 0,
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

LIST_USER_GROUP = {
    **SID,
	'api': 'SYNO.Foto.Sharing.Misc',
	'method': 'list_user_group',
	'version': 1,
	'team_space_sharable_list': 'false'
}

SHARE_ALBUM = {
	'api': 'SYNO.Foto.Sharing.Passphrase',
	'method': 'set_shared',
	'version': 1,
	'policy': 'album',
	'album_id': 0,
	'enabled': 'false' # or "true"
}

UPDATE_PERMISSION = {
	'api': 'SYNO.Foto.Sharing.Passphrase',
	'method': 'update',
	'version': 1,
	'passphrase': None, # \"-escaped string, not sure if this is needed, is created when sharing an album
	'expiration': 0, # unknown what is meant by 0, maybe seconds to expiration?
	'permission': None, # this is a json string, with " escaped as \"
}

SAMPLE_PERMISSION = [{
    'role': 'view',
    'action': 'update',
    'member': {
        'type': 'user',
        'id': 1000
    }
}]

SAMPLE_PERMISSION_STR = r'[{\"role\": \"view\", \"action\": \"update\", \"member\": {\"type\": \"user\", \"id\": 1000}}]'
