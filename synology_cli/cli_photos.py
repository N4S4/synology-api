from typing import cast

from click import pass_context, group, option, Context
from rich import box

from rich.console import Console
from rich.pretty import Pretty as pp
from rich.table import Table

from synology_cli import ctx as appctx
from synology_cli.photos import SynoPhotos

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

@cli_photos.command( 'list', help='lists photos' )
@pass_context
def photos_list( ctx: Context ):
    root_folder = cast( SynoPhotos, ctx.obj.service ).root_folder()

    console = Console()

    table = Table( box=box.MINIMAL, show_header=False, show_footer=False )
    table.add_row(
        '[blue]id[/blue]',
        '[blue]name[/blue]',
        '[blue]parent[/blue]',
        '[blue]owner_user_id[/blue]',
        '[blue]shared[/blue]',
    )
    for f in root_folder:
        table.add_row(
            pp( f.get( 'id' ) ),
            f.get( 'name' ),
            pp( f.get( 'parent' ) ),
            pp( f.get( 'owner_user_id' ) ),
            pp( f.get( 'shared' ) ),
        )

    console.print( table )

@cli_photos.command( 'remove', help='removes photos' )
@pass_context
def photos_remove( ctx ):
    print( 'invoked command photos remove' )

def main( *args, **kwargs ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
