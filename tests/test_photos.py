
from typing import Mapping

from synology_api.photos import Photos

from .fixtures import device
from .fixtures import photos

def test_login( device: Mapping ):
	photos = Photos( **device )
	assert photos.get_userinfo() is not None and photos.get_userinfo().get( 'success' )

def test_count_folders( photos: Photos ):
	# find 'root' folder first
	parent_id = 0
	response = photos.list_folders( 0 )
	if 'data' in response and response.get( 'success', False ):
		for item in response.get( 'data' ).get( 'list', [] ):
			parent_id = item['parent']
			break

	assert parent_id > 0

	response = photos.count_folders( parent_id )
	assert 'data' in response and response.get( 'success' )
