
from sys import exit as sysexit
from typing import cast, Optional

from click import argument, pass_context, group, option, Context, pass_obj
from rich.prompt import Prompt

from synology_cli import ctx as appctx, ApplicationContext
from synology_cli.photos import SynoPhotos, Album
from synology_cli.ui import dataclass_table
from synology_cli.webservice import FACTORY, SynoSession

# global variable for functions below
synophotos: Optional[SynoPhotos] = None

@group( help='photos group' )
@option( '-u', '--url', is_flag=False, required=False, hidden=True, help='URL' )
@option( '-a', '--account', is_flag=False, required=False, hidden=True, help='Account' )
@option( '-p', '--password', is_flag=False, required=False, hidden=True, help='Password' )
@pass_context
def cli_photos( ctx: Context, url: str, account: str, password: str ):
    # set context object to application context
    ctx.obj = appctx

    # create service and attempt to log in
    ctx.obj.service = SynoPhotos(
        url=url if url else ctx.obj.cfg.profile.get( 'url' ),
        account=account if account else ctx.obj.cfg.profile.get( 'account' ),
        password=password if password else ctx.obj.cfg.profile.get( 'password' )
    )

    # load existing session
    syno_session = FACTORY.load( ctx.obj.cfg.session, SynoSession ) if ctx.obj.cfg.session else None

    # attempt to log in, if no session exists
    # todo: check if saved session has been expired, but unclear how to detect that
    if not syno_session:
        syno_session = ctx.obj.service.login()
        if not syno_session.is_valid():
            if syno_session.error_code == 403: # 2FA requested
                otp_token = Prompt.ask( 'Enter 2FA code' )
                syno_session = ctx.obj.service.login( otp_token )
                if not syno_session.is_valid():
                    ctx.obj.console.print(f'error logging in: code={syno_session.error_code}, msg={syno_session.error_msg}')
                    sysexit( -1 )
            else:
                ctx.obj.console.print( f'error logging in: code={syno_session.error_code}, msg={syno_session.error_msg}' )
                sysexit( -1 )

        save_session = True # todo: make this configurable?
        if save_session:
            ctx.obj.cfg.sessions[ ctx.obj.cfg.config.get( 'profile' ) ] = syno_session.as_dict()
            ctx.obj.cfg.save_sessions()

    # set global object to ease access in functions below
    global synophotos
    synophotos = ctx.obj.service
    synophotos.session = syno_session

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
        synophotos.add_album_items(album, items)
    
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
@option( '-n', '--name', required=False, help='folders only which name contains provided name (case insensitive)' )
@argument( 'parent_id', nargs=1, required=False )
@pass_obj
def list_folders( ctx: ApplicationContext, parent_id: int = 0, name: str = None, recursive: bool = False ):
    if parent_id == 0:
        parent_id = synophotos.root_folder().id

    ctx.print( synophotos.list_folders( parent_id, name, recursive ) )

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
@option( '-r', '--role', required=False, default='view', help='permission role, can be "view", "download" or "upload"' )
@option( '-p', '--public', required=False, is_flag=True, help='shares an album publicly' )
@option( '-uid', '--user-id', required=False, help='shares an album with a user with the provided id' )
@option( '-gid', '--group-id', required=False, help='shares an album with a group with the provided id' )
@argument( 'album_id', nargs=1, required=True )
@pass_obj
def share_album(ctx: ApplicationContext, album_id: int, role: str = 'view', public: bool = False, user_id: int = None, group_id: int = None ):
    ctx.print( synophotos.share_album( album_id, role, public, user_id, group_id ).data )

@cli_photos.command( 'share-folder', help='creates an album from a folder and shares it' )
@option( '-n', '--album-name', required=False, help='name of the album to be created' )
@option( '-r', '--role', required=False, default='view', help='permission role, can be "view", "download" or "upload"' )
@option( '-p', '--public', required=False, is_flag=True, help='shares an album publicly' )
@option( '-uid', '--user-id', required=False, help='shares an album with a user with the provided id' )
@option( '-gid', '--group-id', required=False, help='shares an album with a group with the provided id' )
@argument( 'folder_id', nargs=1, required=True )
@pass_obj
def share_folder(ctx: ApplicationContext, folder_id: int, album_name: str = None, role: str = 'view', public: bool = False, user_id: int = None, group_id: int = None ):
    ctx.print( synophotos.share_folder( folder_id, album_name, role, public, user_id, group_id ).data )

@cli_photos.command( 'unshare-album', help='unshares an album' )
@argument( 'album_id', nargs=1, required=True )
@pass_obj
def unshare_album( ctx: ApplicationContext, album_id: int ):
    ctx.print( synophotos.unshare_album( album_id ) )

# finder for ids

@cli_photos.command( 'id', help='helps finding ids of various things' )
@option( '-u', '--user', required=False, is_flag=True, help='search for user id' )
@option( '-g', '--group', required=False, is_flag=True, help='search for group id' )
@argument( 'element', nargs=1, required=True )
@pass_obj
def find_id( ctx: ApplicationContext, element: str, user: bool, group: bool ):
    if user:
        ctx.print( synophotos.id_for_user( element ) )
    elif group:
        ctx.print( synophotos.id_for_group( element ) )

# helper

@cli_photos.command( 'profile', help='shows the name of the currently active profile' )
@pass_obj
def profile( ctx: ApplicationContext ):
    ctx.print( ctx.cfg.profile )

def _ws( ctx: ApplicationContext ) -> SynoPhotos:
    return cast( SynoPhotos, ctx.service )

def main( *args, **kwargs ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
