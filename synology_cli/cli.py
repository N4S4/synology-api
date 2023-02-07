
from click import command, echo, group, option, pass_context

@group
@pass_context
def cli( ctx ):
    pass

# main commands

@cli.group( help='' )
@pass_context
def photos( ctx ):
    pass

# sub commands

@photos.command( 'create', help='creates photos' )
@pass_context
def photos_create( ctx ):
    print( 'invoked command photos create' )

@photos.command( 'list', help='lists photos' )
@pass_context
def photos_list( ctx ):
    print( 'invoked command photos list' )

@photos.command( 'remove', help='removes photos' )
@pass_context
def photos_remove( ctx ):
    print( 'invoked command photos remove' )

def main( args=None ):
    cli()  # trigger cli

if __name__ == '__main__':
    cli()
