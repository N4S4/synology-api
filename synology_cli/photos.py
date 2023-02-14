
from __future__ import annotations

from dataclasses import dataclass, field
from queue import SimpleQueue
from typing import List, Dict, Type, Callable

from .parameters.photos import BROWSE_ALBUM, BROWSE_ITEM, BROWSE_FOLDER, CREATE_ALBUM, CREATE_FOLDER, GET_FOLDER
from .parameters.webservice import ENTRY_URL
from .webservice import SynoWebService

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

    def list_albums(self) -> List[Album]:
        return self.get( ENTRY_URL, BROWSE_ALBUM ).as_list( Album )

    def list_folders(self, parent_id: int = 0, recursive: bool = False) -> List[Folder]:
        if recursive:
            root = self.folder( parent_id )
            folders, queue = [], [ root ]
            while len( queue ) > 0:
                parent = queue.pop( 0 )
                children = self.get(ENTRY_URL, {**BROWSE_FOLDER, 'id': parent.id}).as_list(Folder)
                folders.extend( children )
                queue.extend( children )
            return folders
        else:
            return self.get(ENTRY_URL, {**BROWSE_FOLDER, 'id': parent_id}).as_list(Folder)

    def list_items(self, parent_id: int = 0, all_items: bool = False, recursive: bool = False) -> List[Item]:
        items = []

        if parent_id == 0:
            parent_id = self.root_folder().id

        parent_ids = [parent_id]
        if recursive:
            parent_ids.extend( [p.id for p in self.list_folders( parent_id, recursive=True )] )
            all_items = True # recursive implies all_items, recursive + limiting does not make sense

        for parent_id in parent_ids:
            if all_items:
                limit, offset = BROWSE_ITEM.get( 'limit' ), BROWSE_ITEM.get('offset')
                while True:
                    page = self.get(ENTRY_URL, {**BROWSE_ITEM, 'folder_id': parent_id, 'limit': limit, 'offset': offset} ).as_list(Item)
                    if len( page ) > 0:
                        items.extend( page )
                        offset = offset + limit
                    else:
                        break
            else:
                items = self.get(ENTRY_URL, {**BROWSE_ITEM, 'folder_id': parent_id}).as_list(Item)

        return items

    def create_album( self, name: str ) -> Album:
        return self.get( ENTRY_URL, { **CREATE_ALBUM, 'name': name } ).as_obj( Album )

    def create_folder( self, name: str, parent_id: int = 0 ) -> int:
        return self.get( ENTRY_URL, { **CREATE_FOLDER, 'name': f'\"{name}\"', 'target_id': parent_id } )

    def folder( self, id: int ) -> Folder:
        return self.get( ENTRY_URL, { **GET_FOLDER, 'id': id } ).as_obj( Folder )

    def root_folder( self ) -> Folder:
        return self.folder( 0 )

    # old code below

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
