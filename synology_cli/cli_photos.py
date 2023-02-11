
from sys import exit
from typing import cast

from click import pass_context, group, option, Context, pass_obj

from synology_cli import ctx as appctx, ApplicationContext
from synology_cli.photos import SynoPhotos, Folder, Album, Item
from synology_cli.ui import dataclass_table

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
    syno_response = ctx.obj.service.login()
    if not syno_response.success:
        ctx.obj.console.print( f'error logging in: code={syno_response.error_code}' )
        exit( -1 )

@cli_photos.command( 'list', help='lists items' )
@option( '-a', '--album-id', required=False, help='id of the album to list' )
@option( '-f', '--folder-id', required=False, help='id of the folder to list' )
@pass_obj
def photos_list( ctx: ApplicationContext, folder_id: int = None, album_id: int = None ):
    ctx.console.print( dataclass_table( ctx.service.browse_folder( folder_id or 0 ), Folder ) )

@cli_photos.command( 'list-albums', help='lists albums' )
@pass_obj
def list_albums( ctx: ApplicationContext ):
    ctx.console.print( dataclass_table( ctx.service.browse_albums(), Album ) )

@cli_photos.command( 'list-items', help='lists items' )
@option( '-f', '--folder-id', required=False, help='id of the folder to list' )
@pass_obj
def list_items( ctx: ApplicationContext, folder_id: int = None ):
    ctx.console.print( dataclass_table( ctx.service.browse_items( folder_id or 0 ), Item ) )

def main( *args, **kwargs ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
