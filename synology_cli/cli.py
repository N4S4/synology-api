
from click import command, echo, group, option, pass_context
from synology_cli.cli_photos import cli_photos

@group
@pass_context
def cli( ctx ):
    pass

# main commands, sub commands are defined in submodules

cli.add_command( cli_photos )

# sub commands

def main( args=None ):
    cli()  # trigger cli

if __name__ == '__main__':
    cli()
