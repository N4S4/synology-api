
from click import group, option, pass_context
from synology_cli import ctx as appctx
from synology_cli.cli_photos import cli_photos
from synology_cli.cli_webapi import cli_webapi

@group
@option( '-a', '--account', is_flag=False, required=False, help='User Account' )
@option( '-p', '--password', is_flag=False, required=False, help='Password' )
@option( '-u', '--url', is_flag=False, required=False, help='URL' )
@pass_context
def cli( ctx, url: str, account: str, password: str ):
    ctx.obj = appctx
    # override config values in config file
    appctx.cfg.active_profile().url = url if url else appctx.cfg.active_profile().url
    appctx.cfg.active_profile().account = account if account else appctx.cfg.active_profile().account
    appctx.cfg.active_profile().password = password if password else appctx.cfg.active_profile().password

# main commands, sub commands are defined in submodules

cli.add_command( cli_webapi, 'api' )
cli.add_command( cli_photos, 'photos' )

# sub commands

def main( args=None ):
    cli()  # trigger cli

if __name__ == '__main__':
    cli()
