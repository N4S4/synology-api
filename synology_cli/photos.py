
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from queue import SimpleQueue
from typing import Optional, List, Dict, Type, Union, Callable

from .photos_parameters import BROWSE_ALBUM, BROWSE_ITEM
from .webservice import ENTRY_URL
from .webservice import SynoWebService

# urls

# parameter sets

BROWSE_FOLDER_PARAMS = {
    'api': 'SYNO.Foto.Browse.Folder',
    'method': 'list',
    'version': 2,
    'offset': 0,
    'limit': 50,
    'folder_id': 0,
    'format': 'sid',
    '_sid': None
}

BROWSE_ITEM_PARAMS = {
    'api': 'SYNO.Foto.Browse.Item',
    'method': 'list',
    'version': 2,
    'offset': 0,
    'limit': 50,
    'sort_by': 'filename',
    'sort_direction': 'asc',
    'format': 'sid',
    '_sid': None
}

def list_items(self, folder_id=0, album_id=0, limit=1000, offset=0, additional=None):
    api_name = 'SYNO.Foto.Browse.Item'
    api_path = self.photos_list[api_name]['path']
    additional = additional or []
    req_param = {
        'method': 'list',
        'version': self.photos_list[api_name]['maxVersion'],
        'offset': offset,
        'limit': limit,
        'sort_by': 'filename',
        'sort_direction': 'asc',
#            'type': 'photo',
#            'passphrase': '',
        'additional': json.dumps(additional),
        #'additional': ["thumbnail", "resolution", "orientation", "video_convert", "video_meta"]
    }
    # add folder_id/album_id, depending on which parent is used
    if folder_id > 0:
        req_param['folder_id'] = folder_id
    elif album_id > 0:
        req_param['album_id'] = album_id

    return self.request_data(api_name, api_path, req_param, method='post')

@dataclass
class Item:

    filename: str = field( default=None )
    filesize: int = field( default=None )
    folder_id: int = field( default=None )
    id: int = field( default=None )
    owner_user_id: int = field( default=None )
    time: int = field( default=None )
    indexed_time: int = field( default=None )
    type: str = field( default=None )
    live_type: str = field( default=None )
    additional: List[str] = field( default=None )

    # additional fields
    #folder: Folder = field( init=False, default=None )
    #albums: List[Album] = field( init=False, default_factory=list )

    @classmethod
    def table_fields(cls) -> List[str]:
        return ['id', 'filename', 'filesize', 'folder_id', 'owner_user_id']

@dataclass
class Folder:

    name: str = field( default=None )
    id: int = field( default=0 )
    parent: int = field( default=0 )
    owner_user_id: int = field( default=0 )
    passphrase: str = field( default=None )
    shared: bool = field( default=False )
    sort_by: str = field( default=None )
    sort_direction: str = field( default=None )
    additional: List[str] = field( default=None )

    # additional fields
    # items: List[Item] = field( init=False, default_factory=list )
    # subfolders: List[Folder] = field( init=False, default_factory=list )

    # metadata for table printing -> we're doing this via classmethod
    # table_fields: ClassVar[List[str]] = field( default=[ 'id', 'name' ] )

    @classmethod
    def table_fields( cls ) -> List[str]:
        return [ 'id', 'name', 'parent', 'owner_user_id', 'shared' ]

    def is_root(self) -> bool:
        return True if self.id == self.parent else False

@dataclass
class Album:

    name: str = field( default=None )
    id: int = field( default=0 )
    shared: bool = field( default=False )
    temporary_shared: bool = field( default=False )
    cant_migrate_condition: Dict = field( default=None )
    condition: Dict = field( default=None )
    create_time: int = field( default=0 )
    end_time: int = field( default=0 )
    freeze_album: bool = field( default=False )
    item_count: int = field( default=0 )
    owner_user_id: int = field( default=0 )
    passphrase: str = field( default=None )
    sort_by: str = field( default=None )
    sort_direction: str = field( default=None )
    start_time: int = field( default=0 )
    type: str = field( default=None )
    version: int = field( default=0 )

    # additional fields
    # items: [] = field( init=False, default_factory=list )

    @classmethod
    def table_fields( cls ) -> List[str]:
        return [ 'id', 'name', 'item_count', 'owner_user_id', 'shared' ]

    def is_shared(self) -> bool:
        return self.shared or self.temporary_shared

@dataclass
class SynoPhotos( SynoWebService ):

    def browse_albums( self ) -> List[Album]:
        return self.get_list_to_dataclass( ENTRY_URL, BROWSE_ALBUM, Album )

    def browse_folder( self, id: int = 0 ) -> List[Folder]:
        return self.get_list_to_dataclass( ENTRY_URL, { **BROWSE_FOLDER_PARAMS, 'id': id }, Folder )

    def browse_items( self, id: int = 0 ) -> List[Item]:
        return self.get_list_to_dataclass( ENTRY_URL, { **BROWSE_ITEM, 'id': id }, Item )

    def list_items( self, parent: Union[Folder, Album]=None, folder_id=0, album_id=0 ) -> List[Item]:
        # when Folder/Album was provided, overwrite folder_id/album_id
        if type( parent ) is Folder:
            folder_id = parent.id
        elif type( parent ) is Album:
            album_id = parent.id

        if folder_id > 0:
            return self._process_response( self.inst.list_items( folder_id=folder_id ), Item )
        elif album_id > 0:
            return self._process_response(self.inst.list_items(album_id=album_id), Item)
        else:
            return []

    def traverse_folders(self, fn_folder: Callable = None, fn_item: Callable = None ) -> List[Folder]:
        folders = []
        q = SimpleQueue()
        q.put(self.root_folder())

        while not q.empty():
            # get/process next folder
            folder = q.get()
            if fn_folder:
                fn_folder( folder )
            folders.append( folder )

            # process items
            items = self.list_items(folder)
            for item in items:
                folder.items.append( item )
                item.folder = folder
                if fn_item:
                    fn_item( item )

            # store sub folders
            for f in self.list_folders(folder):
                folder.subfolders.append( f )
                q.put(f)
        return folders

    def traverse_albums(self, fn_album: Callable = None, fn_item: Callable = None) -> List[Album]:
        albums = []
        for album in self.list_albums():
            # add album to album list
            albums.append( album )

            # process items in album
            for item in self.list_items( album_id=album.id ):
                album.items.append( item )
                item.albums.append( album )

                if fn_item:
                    fn_item( item )

            # finally post process album
            if fn_album:
                fn_album( album )

        return albums

    def traverse_items(self) -> List[Item]:
        item_map = {}
        def process_item( item: Item ):
            if item.id not in item_map.keys():
                item_map[item.id] = item

        def process_album( album: Album ):
            folder_items = []
            for album_item in album.items:
                folder_item = item_map.get( album_item.id )
                if folder_item:
                    folder_items.append( folder_item )
                    folder_item.albums.append( album )
                else:
                    print( 'warning: album item not in folder items -> investigate!' )
            album.items = folder_items

        self.traverse_folders( fn_item=process_item )
        self.traverse_albums( fn_album=process_album )

        return list( item_map.values() )

    # noinspection PyMethodMayBeStatic
    def _process_response(self, response: Dict, cls: Type ) -> List:
        rval = []

        if 'data' in response and response.get('success', False):
            for item in response.get('data').get('list', []):
                rval.append(cls(**item))

        return rval
