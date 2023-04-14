
from click import group, option, pass_context
from synology_cli import ctx as appctx
from synology_cli.cli_photos import cli_photos
from synology_cli.cli_webapi import cli_webapi

@group
@option( '-a', '--account', is_flag=False, required=False, hidden=True, help='User Account' )
@option( '-p', '--password', is_flag=False, required=False, hidden=True, help='Password' )
@option( '-u', '--url', is_flag=False, required=False, hidden=True, help='URL' )
@pass_context
def cli( ctx, url: str, account: str, password: str ):
    ctx.obj = appctx
    # override config values in config file
    url = url if url else ctx.obj.cfg.active_profile().get( 'url' )
    account = account if account else ctx.obj.cfg.active_profile().get( 'account' )
    password = password if password else ctx.obj.cfg.active_profile().get( 'password' )

# main commands, sub commands are defined in submodules

cli.add_command( cli_webapi, 'api' )
cli.add_command( cli_photos, 'photos' )

# sub commands

def main( args=None ):
    cli()  # trigger cli

if __name__ == '__main__':
    cli()
