
from logging import getLogger
from synology_cli.cli import main as main_cli

log = getLogger( __name__ )

def main():
	main_cli()

if __name__ == '__main__':
	main()
