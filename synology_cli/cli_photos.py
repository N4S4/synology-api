
from click import pass_context, group

@group( help='photos group' )
@pass_context
def cli_photos( ctx ):
    pass

@cli_photos.command( 'create', help='creates photos' )
@pass_context
def photos_create( ctx ):
    print( 'invoked command photos create' )

@cli_photos.command( 'list', help='lists photos' )
@pass_context
def photos_list( ctx ):
    print( 'invoked command photos list' )

@cli_photos.command( 'remove', help='removes photos' )
@pass_context
def photos_remove( ctx ):
    print( 'invoked command photos remove' )

def main( args=None ):
    cli_photos()  # trigger cli

if __name__ == '__main__':
    main()
