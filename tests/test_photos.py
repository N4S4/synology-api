
from typing import Mapping

from synology_api.photos import Photos

from .fixtures import device

def test_login( device: Mapping ):
	photos = Photos( **device )
	assert photos.get_userinfo() is not None and photos.get_userinfo().get( 'success' )
