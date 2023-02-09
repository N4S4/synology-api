
from typing import cast

from click import pass_context, group, option, Context
from rich import box
from rich.console import Console
from rich.pretty import Pretty as pp
from rich.table import Table

from synology_cli import ctx as appctx
from synology_cli.webapi import SynoWebApi

@group( 'api', help='api information' )
@option( '-u', '--url', is_flag=False, required=False, help='URL' )
@option( '-a', '--account', is_flag=False, required=False, help='Account' )
@option( '-p', '--password', is_flag=False, required=False, help='Password' )
@pass_context
def cli_webapi( ctx: Context, url: str, account: str, password: str ):
    ctx.obj = appctx
    url = url if url else ctx.obj.cfg.active_profile().url
    account = account if account else ctx.obj.cfg.active_profile().account
    password = password if password else ctx.obj.cfg.active_profile().password
    ctx.obj.service = SynoWebApi( url=url )

@cli_webapi.command( 'list', help='lists API entrypoints' )
@pass_context
def api_list( ctx: Context ):
    all_apis = cast( SynoWebApi, ctx.obj.service ).info()

    console = Console()

    table = Table( box=box.MINIMAL, show_header=False, show_footer=False )
    table.add_row(
        '[blue]api name[/blue]',
        '[blue]path[/blue]',
        '[blue]minimum version[/blue]',
        '[blue]maximum version[/blue]',
        '[blue]request format[/blue]',
    )
    for key, value in all_apis.get( 'data' ).items():
        table.add_row(
            key,
            value.get( 'path' ),
            pp( value.get( 'minVersion' ) ),
            pp( value.get( 'maxVersion' ) ),
            pp( value.get( 'requestFormat' ) ),
        )

    console.print( table )

def main( *args, **kwargs ):
    cli_webapi()  # trigger cli

if __name__ == '__main__':
    main()
