
from sys import exit
from typing import cast, Optional

from click import argument, pass_context, group, option, Context, pass_obj
from dataclass_factory import Factory

from synology_cli import ctx as appctx, ApplicationContext
from synology_cli.photos import SynoPhotos, Folder, Album, Item, Member, Permission
from synology_cli.ui import dataclass_table

# global variable for functions below
synophotos: Optional[SynoPhotos] = None

@group( help='photos group' )
@option( '-u', '--url', is_flag=False, required=False, help='URL' )
@option( '-a', '--account', is_flag=False, required=False, help='Account' )
@option( '-p', '--password', is_flag=False, required=False, help='Password' )
@pass_context
def cli_photos( ctx: Context, url: str, account: str, password: str ):
    # set context object to application context
    ctx.obj = appctx

    # update account settings
    url = url if url else ctx.obj.cfg.active_profile().url
    account = account if account else ctx.obj.cfg.active_profile().account
    password = password if password else ctx.obj.cfg.active_profile().password

    # create service and attempt to log in
    ctx.obj.service = SynoPhotos( url=url, account=account, password=password )
    syno_response = ctx.obj.service.login() # todo: save sid to be able to skip login later? but for how long?
    if not syno_response.success:
        ctx.obj.console.print( f'error logging in: code={syno_response.error_code}' )
        exit( -1 )

    # set global object to ease access in functions below
    global synophotos
    synophotos = ctx.obj.service

# create

@cli_photos.command( 'create-album', help='creates a new album' )
@option( '-f', '--from-folder', required=False, help='id of folder to populate album with' )
@option( '-s', '--share-with', required=False, help='share album with' )
@argument( 'name', nargs=1, required=True )
@pass_obj
def create_album( ctx: ApplicationContext, name: str, from_folder: int = None, share_with: int = None ):
    album = synophotos.create_album( name )
    if from_folder:
        items = synophotos.list_items( from_folder, all_items=True, recursive=False )
        synophotos.add_items( album, items )
    
    ctx.print( album.id )

@cli_photos.command( 'create-folder', help='creates a new folder' )
@option( '-n', '--name', required=True, help='album name' )
@option( '-p', '--parent-id', required=False, help='parent id' )
@pass_obj
def create_folder( ctx: ApplicationContext, name: str, parent_id: int ):
    ctx.console.print( _ws( ctx ).create_folder( name, parent_id ) )

# count ... not sure if this is useful

@cli_photos.command('count-albums', help='counts the number of albums')
@pass_obj
def count_albums(ctx: ApplicationContext):
    ctx.console.print( synophotos.count_albums() )

@cli_photos.command('count-folders', help='counts the number of folders')
@argument( 'parent_id', nargs=1, required=False )
@pass_obj
def count_folders(ctx: ApplicationContext, parent_id: int = 0):
    ctx.console.print( synophotos.count_folders( parent_id ) )

@cli_photos.command('count-items', help='counts the number of items')
@option( '-f', '--folder-id', required=False, help='id of the parent folder' )
@option( '-a', '--album-id', required=False, help='id of the parent album' )
@pass_obj
def count_items(ctx: ApplicationContext, folder_id: int = None, album_id: int = None):
    ctx.console.print( synophotos.count_items( folder_id=folder_id, album_id=album_id ) )

# list

@cli_photos.command( 'list-folders', help='lists folders' )
@option( '-r', '--recursive', required=False, is_flag=True, help='include all folders recursively' )
@argument( 'parent_id', nargs=1, required=False )
@pass_obj
def list_folders( ctx: ApplicationContext, parent_id: int = 0, recursive: bool = False ):
    if parent_id == 0:
        parent_id = synophotos.root_folder().id

    ctx.print( synophotos.list_folders( parent_id, recursive ) )

@cli_photos.command( 'list-albums', help='lists albums' )
@pass_obj
def list_albums( ctx: ApplicationContext ):
    ctx.console.print( dataclass_table( _ws( ctx ).list_albums(), Album ) )

@cli_photos.command( 'list-items', help='lists items' )
@option( 'all_items', '-a', '--all', required=False, is_flag=True, help='skip paging and list all items' )
@option( '-r', '--recursive', required=False, is_flag=True, help='includes all items recursively' )
@argument( 'parent_id', nargs=1, required=False )
@pass_obj
def list_items( ctx: ApplicationContext, parent_id: int = 0, all_items: bool = False, recursive: bool = False ):
    if all_items or recursive:
        ctx.print( 'fetching items without paging and/or recursively, this might take a while ...' )
    ctx.print( synophotos.list_items( parent_id, all_items, recursive ) )

@cli_photos.command( 'list-user-groups', help='lists users and groups' )
@pass_obj
def list_user_groups( ctx: ApplicationContext ):
    ctx.print( synophotos.list_user_group() )

@cli_photos.command( 'get-root-folder', help='gets the root folder' )
@pass_obj
def get_root_folder( ctx: ApplicationContext ):
    ctx.print( _ws( ctx ).root_folder().id )

# sharing

@cli_photos.command( 'share-album', help='shares an album' )
@argument( 'album_id', nargs=1, required=True )
@pass_obj
def share_album( ctx: ApplicationContext, album_id: int ):
    ctx.print( synophotos.share_album( album_id ) )

@cli_photos.command( 'unshare-album', help='unshares an album' )
@argument( 'album_id', nargs=1, required=True )
@pass_obj
def unshare_album( ctx: ApplicationContext, album_id: int ):
    ctx.print( synophotos.unshare_album( album_id ) )

@cli_photos.command( 'grant-permission', help='grants sharing permissions' )
@option( '-r', '--role', required=False, default='view', help='permission role, can be "view", "download" or "upload"' )
@option( '-p', '--passphrase', required=True, help='passphrase, generated when sharing an album' )
@option( '-uid', '--user-id', required=False, help='user id' )
@option( '-gid', '--group-id', required=False, help='group id' )
@pass_obj
def grant_permission( ctx: ApplicationContext, passphrase: str, role: str = 'view', user_id: int = None, group_id: int = None ):
    id = group_id if group_id else user_id
    type = 'group' if group_id else 'user'
    permission = Permission( role=role, member=Member( id=id, type=type ) )
    ctx.print( synophotos.grant_permission( [ permission ], passphrase ) )

# helper

def _ws( ctx: ApplicationContext ) -> SynoPhotos:
    return cast( SynoPhotos, ctx.service )

def main( *args, **kwargs ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
