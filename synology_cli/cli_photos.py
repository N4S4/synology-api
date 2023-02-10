
from typing import cast

from click import pass_context, group, option, Context, argument

from synology_cli import ctx as appctx
from synology_cli.photos import SynoPhotos, Folder
from synology_cli.ui import dataclass_table

@group( help='photos group' )
@option( '-u', '--url', is_flag=False, required=False, help='URL' )
@option( '-a', '--account', is_flag=False, required=False, help='Account' )
@option( '-p', '--password', is_flag=False, required=False, help='Password' )
@pass_context
def cli_photos( ctx: Context, url: str, account: str, password: str ):
    ctx.obj = appctx
    url = url if url else ctx.obj.cfg.active_profile().url
    account = account if account else ctx.obj.cfg.active_profile().account
    password = password if password else ctx.obj.cfg.active_profile().password
    ctx.obj.service = SynoPhotos( url=url, account=account, password=password )

@cli_photos.command( 'create', help='creates photos' )
@pass_context
def photos_create( ctx ):
    print( 'invoked command photos create' )

@cli_photos.command( 'ls', help='lists photos' )
@option( '-a', '--album-id', required=False, help='id of the album to list' )
@option( '-f', '--folder-id', required=False, help='id of the folder to list' )
@pass_context
def photos_list( ctx: Context, folder_id: int = None, album_id: int = None ):
    syno_photos = cast( SynoPhotos, ctx.obj.service )
    syno_response = syno_photos.login()
    if syno_response.success:
        ctx.obj.console.print( dataclass_table( syno_photos.browse_folder( folder_id or 0 ), Folder ) )
    else:
        ctx.obj.console.print( f'error logging in: code={syno_response.error_code}' )
    pass

@cli_photos.command( 'remove', help='removes photos' )
@pass_context
def photos_remove( ctx ):
    print( 'invoked command photos remove' )

def main( *args, **kwargs ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
