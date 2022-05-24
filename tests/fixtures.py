
from importlib.resources import path
from json import loads as load_json
from pathlib import Path
from typing import Dict

from pytest import fixture

from synology_api.photos import Photos

CREDENTIALS_FILE = 'credentials.json'

with path( 'tests', '__init__.py' ) as p:
	credentials_path = Path( p.parent, CREDENTIALS_FILE )
	credentials = load_json( credentials_path.read_text( 'UTF-8' ) )
	DEVICE = credentials.get( credentials.get( 'device' ) )

@fixture
def device() -> Dict:
	return DEVICE

@fixture
def photos( device ) -> Photos:
	return Photos( **device )
